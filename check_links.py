"""Check external links in published FAQ Markdown (Python 3.10+, standard library)."""

import argparse
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
import re
import ssl
import subprocess
import sys
from urllib.error import HTTPError, URLError
from urllib.parse import urldefrag, urlsplit
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parent
PUBLISHED_ROOTS = {"barcode-reader", "mrz-scanner", "license"}
MARKDOWN_LINK = re.compile(r"!?\[[^\]\n]*\]\(\s*<?(https?://[^\s)>]+)", re.I)
REFERENCE_LINK = re.compile(r"^\s{0,3}\[[^\]]+\]:\s*<?(https?://[^\s>]+)", re.I)
HTML_LINK = re.compile(r"\b(?:href|src)\s*=\s*['\"](https?://[^'\"]+)", re.I)
AUTOLINK = re.compile(r"<(https?://[^>\s]+)>", re.I)
FENCE = re.compile(r"^\s*(`{3,}|~{3,})")


def published(path):
    parts = path.parts
    return (path.suffix.lower() == ".md" and
            ((len(parts) == 1 and parts[0] in {"index.md", "search.md"}) or
             (parts[0] in PUBLISHED_ROOTS and "archive" not in parts)))


def links(text):
    """Return URL -> first line number, omitting fenced examples and fragments."""
    found = {}
    fence = None
    for number, line in enumerate(text.splitlines(), 1):
        marker = FENCE.match(line)
        if marker:
            run = marker.group(1)
            if fence is None:
                fence = run
            elif run[0] == fence[0] and len(run) >= len(fence):
                fence = None
            continue
        if fence:
            continue
        for pattern in (MARKDOWN_LINK, REFERENCE_LINK, HTML_LINK, AUTOLINK):
            for match in pattern.finditer(line):
                url = urldefrag(match.group(1).rstrip(".,;"))[0]
                found.setdefault(url, number)
    return found


def git(*args):
    return subprocess.run(["git", *args], cwd=ROOT, check=True, capture_output=True).stdout


def candidates(base_ref):
    if not base_ref:
        for root in ("index.md", "search.md", *sorted(PUBLISHED_ROOTS)):
            path = ROOT / root
            if path.is_file():
                yield Path(root), set()
            elif path.is_dir():
                for file in sorted(path.rglob("*.md")):
                    rel = file.relative_to(ROOT)
                    if published(rel):
                        yield rel, set()
        return

    # Compare URLs, not just files: old failures must not block unrelated edits.
    fields = git("diff", "--name-status", "--find-renames", "-z", base_ref, "HEAD", "--").decode().split("\0")
    index = 0
    while index < len(fields) - 1:
        status = fields[index]
        index += 1
        old_path = fields[index]
        index += 1
        new_path = old_path
        if status[0] in "RC":
            new_path = fields[index]
            index += 1
        rel = Path(new_path)
        if status[0] == "D" or not published(rel) or not (ROOT / rel).is_file():
            continue
        previous = set()
        if status[0] != "A":
            previous = set(links(git("show", f"{base_ref}:{old_path}").decode("utf-8")))
        yield rel, previous


def check(url):
    """Return (broken, explanation); None means the remote result is inconclusive."""
    try:
        request = Request(url, headers={"User-Agent": "FAQ-Link-Checker/1.0"})
        with urlopen(request, timeout=15) as response:  # default verified TLS context
            final_host = urlsplit(response.url).hostname or ""
            if final_host == "dynamsoft.com" or final_host.endswith(".dynamsoft.com"):
                body = response.read(50000).decode("utf-8", errors="replace").lower()
                if (re.search(r'id=["\']pagenotfound["\']', body) or
                        re.search(r"<title>\s*(?:404|page not found|oops! that page can't be found)", body)):
                    return True, "Dynamsoft soft 404"
            return False, "OK"
    except HTTPError as error:
        if error.code in (401, 403, 408, 429) or error.code >= 500:
            return None, f"HTTP {error.code} (inconclusive)"
        return True, f"HTTP {error.code}"
    except URLError as error:
        if isinstance(error.reason, ssl.SSLCertVerificationError):
            return True, f"TLS certificate verification failed: {error.reason}"
        return None, f"Network error (inconclusive): {error.reason}"
    except (TimeoutError, OSError) as error:
        return None, f"Network error (inconclusive): {error}"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--base-ref", help="Only check URLs added since this git revision (for CI)")
    args = parser.parse_args()
    try:
        occurrences = {}
        files = 0
        for path, previous in candidates(args.base_ref):
            files += 1
            for url, line in links((ROOT / path).read_text(encoding="utf-8")).items():
                if url not in previous:
                    occurrences.setdefault(url, []).append(f"{path.as_posix()}:{line}")
    except (OSError, UnicodeError, subprocess.CalledProcessError) as error:
        print(f"Cannot scan FAQ links: {error}", file=sys.stderr)
        return 2

    print(f"Checking {len(occurrences)} external URL(s) in {files} published Markdown file(s).")
    broken = warnings = 0
    with ThreadPoolExecutor(max_workers=8) as pool:
        futures = {pool.submit(check, url): url for url in occurrences}
        for future in as_completed(futures):
            url = futures[future]
            try:
                result, reason = future.result()
            except Exception as error:
                result, reason = None, f"Unexpected check error (inconclusive): {error}"
            if result is False:
                continue
            if result is True:
                broken += 1
            else:
                warnings += 1
            for location in occurrences[url]:
                print(f"{location}: {'BROKEN' if result else 'WARNING'} {url} — {reason}")
    print(f"Result: {broken} broken URL(s), {warnings} inconclusive URL(s).")
    return 1 if broken else 0


if __name__ == "__main__":
    sys.exit(main())
