---
layout: default-layout
title: Enable Debug Mode in DBR-JS | Dynamsoft
keywords: Dynamsoft Barcode Reader, FAQ, tech basic, Magic Word, MIME
description: Enable debug mode, upload custom JSON templates, save video frames, and customize scan settings in Dynamsoft Barcode Reader JS.
needAutoGenerateSidebar: false
---

# How to enable and use debug mode in DBR-JS?

## Enable debug mode

Starting from v11.0.3000, you can enable the demo's debug mode by appending `?debug=true` to the demo URL, for example:  
https://demo.dynamsoft.com/barcode-reader-js/?debug=true

This version also adds:

- Custom template upload feature
- Video frame saving during debugging
- Improved UI with:
  - Single/Multiple barcode toggle
  - Scan Mode selection (Speed, Balance, Coverage)
  - Barcode Color Options (Inverted, Normal, Both)

---

<div align="left">
    <p><img src="{{site.dbr_web_assets}}upload-template.png" width="40%" alt="advanced settings"></p>
</div>

## Upload a custom template

1. Enable debug mode with `?debug=true`
2. Use the **custom template upload** button (bottom-left of the UI)
3. Upload a compatible `.json` template for v11.0.3000

**Note:** Once a template is uploaded, changing other settings will have no effect until the template is cleared.

---

## Save video frames

In debug mode, you can save video frames for testing and analysis using the button in the top-right of the UI.

---

## Useful Links

- [Demo Page](https://demo.dynamsoft.com/barcode-reader-js/)
- [Documentation](https://www.dynamsoft.com/barcode-reader/docs/web/)

---
