# Dynamsoft FAQ

Source for the FAQ site covering Dynamsoft's products, published at [dynamsoft.com/faq](https://www.dynamsoft.com/faq). This repo holds the Barcode Reader, MRZ Scanner, and licensing FAQs; Dynamic Web TWAIN (a separate product line, not part of Capture Vision) has its own FAQ section linked from the homepage (`index.md`) but sourced from a different repo.

## Writing or editing an article

See [`AGENTS.md`](AGENTS.md) for the FAQ article structure, frontmatter, linking, and archive-directory conventions.

## Building and deploying

The site is built with Jekyll using a shared theme/layout maintained in [dynamsoft-docs/Docs-Template-Repo](https://github.com/dynamsoft-docs/Docs-Template-Repo), which this repo doesn't include locally. Pushes to `main` and `preview` trigger the CI workflows in `.github/workflows/main.yml`, which build and sync to production and the preview/testing environment respectively.

## Checking links

`check_links.py` crawls the repo's Markdown files and reports broken links. Run it before submitting a change that touches links:

```bash
python check_links.py
```
