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

The scripts clone the shared template's preview branch into `.dev/`, merge it with this FAQ source, install gems, and serve Jekyll at `http://localhost:5555/faq/`. The generated `.dev/` workspace is ignored by Git. Use `--no-serve` / `-NoServe` to prepare without serving, or `--no-template-update` / `-NoTemplateUpdate` to reuse the cloned template. Changes to FAQ files require rerunning the script to refresh the merged workspace.

## Checking links

`check_links.py` crawls the repo's Markdown files and reports broken links. Run it before submitting a change that touches links:

```bash
python check_links.py
```