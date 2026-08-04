# Dynamsoft FAQ

Source for the FAQ site covering Dynamsoft's products, published at [dynamsoft.com/faq](https://www.dynamsoft.com/faq). This repo holds the Barcode Reader, MRZ Scanner, and licensing FAQs; Dynamic Web TWAIN (a separate product line, not part of Capture Vision) has its own FAQ section linked from the homepage (`index.md`) but sourced from a different repo.

## Structure

Each FAQ article is a Markdown file with Jekyll frontmatter:

```markdown
---
layout: default-layout
title: <SEO-facing page title>
keywords: <comma-separated keywords>
description: <SEO-facing description>
needAutoGenerateSidebar: false
---

# <The actual question, as an H1>

Answer content...
```

Top-level product areas:

- `barcode-reader/` — general, mobile, server, and web edition FAQs
- `mrz-scanner/` — MRZ Scanner FAQs
- `license/` — licensing FAQs shared across products

Each subdirectory has its own `index.md` that links to every article in that section — when adding a new article, add a link to it there too.

`*/archive/*` directories hold historical, version-pinned content (e.g. `-v9.6.40`, `-v10.4.2000`). They're excluded from the Jekyll build (see `_config.yml`) and kept only for reference — don't link to them from live pages.

## Building and deploying

The site is built with Jekyll using a shared theme/layout maintained in [dynamsoft-docs/Docs-Template-Repo](https://github.com/dynamsoft-docs/Docs-Template-Repo), which this repo doesn't include locally. Pushes to `main` and `preview` trigger the CI workflows in `.github/workflows/main.yml`, which build and sync to production and the preview/testing environment respectively.

## Checking links

`check_links.py` crawls the repo's Markdown files and reports broken links. Run it before submitting a change that touches links:

```bash
python check_links.py
```
