# Agent guide: writing and wiring FAQ articles

This file is for AI agents (and anyone else) authoring or editing FAQ content in this repo. See `README.md` for what this repo is and how it's built.

## Adding a new article

Create a Markdown file in the right product/topic directory (see "Directory map" below) with this frontmatter and structure:

```markdown
---
layout: default-layout
title: <SEO-facing page title>
keywords: <comma-separated keywords>
description: <SEO-facing description, often the question itself>
needAutoGenerateSidebar: false
---

# <The actual question, phrased as a question>

Answer content...
```

Rules:

- **Always include the H1.** It must be the real question the article answers — not a changelog-style heading, not omitted. If you're not sure how to phrase it, check the link text used for this article in its directory's `index.md`; that's the canonical phrasing.
- **Link it from `index.md`.** Every subdirectory (`barcode-reader/general/`, `barcode-reader/web/configuration/`, `mrz-scanner/general/`, etc.) has an `index.md` that lists every article in that section. A new article with no entry there is orphaned — it exists but no one can navigate to it. Add a bullet there when you add the file, and remove the bullet if you remove the file.
- **Internal links use `.html`, not `.md`.** Link to sibling/other articles as `some-page.html` (Jekyll serves the built output), and to a parent-directory archive as `../archive/some-page.html`, etc. A link ending in `.md` will not resolve on the live site.
- **Don't add "back to index" links inside articles.** They were deliberately removed repo-wide; the sidebar/index already provides navigation.
- **Images** go through a site variable per product/edition — `{{site.dbr_web_assets}}`, `{{site.dbr_mobile_assets}}`, `{{site.dbr_server_assets}}` (defined in `_config.yml`), pointing at that edition's `assets/` directory. Before referencing an image, confirm the file actually exists at that path — a stale or placeholder filename (e.g. a literal `undefined.png`) will silently 404.
- **Write the answer as a direct statement, not a raw Q&A fragment.** Don't leave phrasing like "Yes — ..." or "This can be expanded ..." floating with no visible question or antecedent above it — the H1 is the question; the body should read as its answer, not as a leftover snippet.
- **Don't duplicate a section under a second heading.** If a "what's new"/changelog-style heading and a "how to" heading right below it cover the same ground, merge them.

## Directory map

- `barcode-reader/general/` — cross-edition Barcode Reader FAQs
- `barcode-reader/mobile/`, `barcode-reader/server/`, `barcode-reader/web/` — edition-specific Barcode Reader FAQs, each split into topic subdirectories (`configuration/`, `capabilities/`, `debug/`, `scan-setting/`, etc.)
- `mrz-scanner/general/` — MRZ Scanner FAQs
- `license/` — licensing FAQs shared across products

## Archived content (`*/archive/*`)

Directories named `archive` under `barcode-reader/{mobile,server,web}/` hold historical, version-pinned content (e.g. `-v9.6.40`, `-v10.4.2000` snapshots). They are:

- Excluded from the Jekyll build via `_config.yml`'s `exclude:` list — not hosted, not in `sitemap.xml`.
- Not linked from any live index or sidebar, and shouldn't be. Don't add new links into an `archive/` directory from a live page.
- Not to be "modernized" — if you're editing a file in `archive/`, fix only structural issues (a truly broken build, a factual error introduced by your own change), not stale APIs or old terminology; that staleness is the point.

If you find yourself wanting to *add* content to an archive directory, it almost certainly belongs in the live directory instead.

## Before finishing

Run the link checker from the repo root and fix anything it flags in files you touched:

```bash
python check_links.py
```
