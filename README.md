# Dynamsoft FAQ

Source for the FAQ site covering Dynamsoft's products, published at [dynamsoft.com/faq](https://www.dynamsoft.com/faq). This repo holds the Barcode Reader, MRZ Scanner, and licensing FAQs; Dynamic Web TWAIN (a separate product line, not part of Capture Vision) has its own FAQ section linked from the homepage (`index.md`) but sourced from a different repo.

## Writing or editing an article

See [`AGENTS.md`](AGENTS.md) for the FAQ article structure, frontmatter, linking, and archive-directory conventions.

## Building and deploying

The site is built with Jekyll using a shared theme/layout maintained in [dynamsoft-docs/Docs-Template-Repo](https://github.com/dynamsoft-docs/Docs-Template-Repo), which this repo doesn't include locally. Pushes to `main` and `preview` trigger the CI workflows in `.github/workflows/main.yml`, which build and sync to production and the preview/testing environment respectively.

For a local preview, install Git, Ruby/Bundler, and rsync (Bash) or robocopy (PowerShell), then run from the repository root:

```bash
./scripts/dev.sh
```

Or on Windows:

```powershell
./scripts/dev.ps1
```

The scripts clone the shared template's preview branch into `.dev/`, merge it with this FAQ source, install gems, and serve Jekyll at `http://localhost:5555/faq/`. The generated `.dev/` workspace is ignored by Git and omits archived FAQ content and local worktrees. Use `--no-serve` / `-NoServe` to prepare without serving, then rerun without that flag to serve; `--no-template-update` / `-NoTemplateUpdate` reuses the cloned template. Changes to FAQ files require rerunning the script to refresh the merged workspace.

## Checking links

`check_links.py` checks external HTTP(S) links in publishable FAQ Markdown (not archived pages or generated workspaces). It verifies HTTPS certificates, reports confirmed 4xx and Dynamsoft soft-404 pages as failures, and reports access-denied, rate-limited, server, and network errors as inconclusive warnings. It does not check relative links or anchors; the shared Jekyll template performs its own internal-link check during the build.

`python check_links.py` checks all published Markdown and exits nonzero for confirmed broken URLs. Existing broken URLs may be reported until fixed. GitHub Actions checks only URLs newly introduced since the PR base or preceding push, so legacy failures do not block unrelated changes. The separate `Check-Links` job must pass before the build-and-sync jobs run on `main` and `preview`.