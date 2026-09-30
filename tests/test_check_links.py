import contextlib
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import urlsplit
import io
from pathlib import Path
import subprocess
import sys
import tempfile
import threading
import unittest
from unittest.mock import patch

import check_links


class LinkHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        status = {"/missing": 404, "/blocked": 403}.get(urlsplit(self.path).path, 200)
        self.send_response(status)
        self.end_headers()
        self.wfile.write(b"available")

    def log_message(self, *args):
        pass


class LinkCheckerTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.server = ThreadingHTTPServer(("127.0.0.1", 0), LinkHandler)
        cls.thread = threading.Thread(target=cls.server.serve_forever)
        cls.thread.start()
        cls.base_url = f"http://127.0.0.1:{cls.server.server_port}"

    @classmethod
    def tearDownClass(cls):
        cls.server.shutdown()
        cls.server.server_close()
        cls.thread.join()

    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        (self.root / "barcode-reader" / "general").mkdir(parents=True)
        (self.root / "barcode-reader" / "web" / "archive").mkdir(parents=True)

    def run_checker(self, *args):
        output = io.StringIO()
        with patch.object(check_links, "ROOT", self.root), patch.object(sys, "argv", ["check_links.py", *args]), contextlib.redirect_stdout(output):
            code = check_links.main()
        return code, output.getvalue()

    def git(self, *args):
        return subprocess.check_output(["git", *args], cwd=self.root, stderr=subprocess.DEVNULL).decode().strip()

    def test_full_scan_fails_on_broken_published_link_but_skips_archives(self):
        (self.root / "index.md").write_text(f"[ok]({self.base_url}/okay)\n", encoding="utf-8")
        (self.root / "barcode-reader" / "general" / "example.md").write_text(
            f"[missing]({self.base_url}/missing)\n[blocked]({self.base_url}/blocked)\n", encoding="utf-8")
        (self.root / "barcode-reader" / "web" / "archive" / "old.md").write_text(
            "[old](http://127.0.0.1:1/missing)\n", encoding="utf-8")
        code, output = self.run_checker()
        self.assertEqual(code, 1)
        self.assertIn("example.md:1: BROKEN", output)
        self.assertIn("example.md:2: WARNING", output)
        self.assertIn("1 broken URL(s), 1 inconclusive URL(s)", output)
        self.assertNotIn("archive", output)

    def test_changed_mode_checks_only_new_urls(self):
        article = self.root / "barcode-reader" / "general" / "example.md"
        article.write_text(f"[existing]({self.base_url}/missing)\n", encoding="utf-8")
        self.git("init")
        self.git("-c", "user.name=Test", "-c", "user.email=test@example.com", "commit", "--allow-empty", "-m", "initial")
        self.git("add", ".")
        self.git("-c", "user.name=Test", "-c", "user.email=test@example.com", "commit", "-m", "old links")
        base = self.git("rev-parse", "HEAD")
        article.write_text(
            f"[existing]({self.base_url}/missing)\n[new]({self.base_url}/okay)\n", encoding="utf-8")
        self.git("add", ".")
        self.git("-c", "user.name=Test", "-c", "user.email=test@example.com", "commit", "-m", "new link")
        code, output = self.run_checker("--base-ref", base)
        self.assertEqual(code, 0)
        self.assertIn("Checking 1 external URL(s)", output)
        self.assertNotIn("BROKEN", output)
        article.write_text(article.read_text(encoding="utf-8") + f"[new bad]({self.base_url}/missing?new=1)\n", encoding="utf-8")
        # Changed URLs in the same file are compared with the base commit, not with another URL's status.
        self.git("add", ".")
        self.git("-c", "user.name=Test", "-c", "user.email=test@example.com", "commit", "-m", "another link")
        code, output = self.run_checker("--base-ref", base)
        self.assertEqual(code, 1)
        self.assertIn("Checking 2 external URL(s)", output)
        self.assertIn("example.md:3: BROKEN", output)


if __name__ == "__main__":
    unittest.main()
