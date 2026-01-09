---
layout: default-layout
title: How to resolve the expected magic word error that occurs when using DBR-JS?
keywords: Dynamsoft Barcode Reader, FAQ, tech basic, Magic Word, MIME
description: How to resolve the expected magic word error that occurs when using DBR-JS?
needAutoGenerateSidebar: false
---

## What's new in version v11.0.3000?

- Support for debug mode using `?debug=true`
- Custom template upload feature
- Video frame saving during debugging
- Improved UI with:
  - Single/Multiple barcode toggle
  - Scan Mode selection (Speed, Balance, Coverage)
  - Barcode Color Options (Inverted, Normal, Both)

---

## Enable debug mode

Append `?debug=true` to the demo URL.  
Example: https://demo.dynamsoft.com/barcode-reader-js/?debug=true

In debug mode:

- You can upload **custom templates** compatible with v11.0.3000
- You can **save video frames**

---

<div align="left">
    <p><img src="/assets/undefined.png" width="40%" alt="advanced settings"></p>
</div>

## Upload a custom template

1. Enable debug mode with `?debug=true`
2. Use the **custom template upload** button (bottom-left of the UI)
3. Upload a compatible `.json` template for v11.0.3000

**Note:** Once a template is uploaded, changing other settings will have no effect until the template is cleared.

---

## Save video frames

Yes — in **debug mode**, you can save video frames for testing and analysis (top-right of the UI).

---

## Useful Links

- [Demo Page](https://demo.dynamsoft.com/barcode-reader-js/)
- [Documentation](https://www.dynamsoft.com/barcode-reader/docs/web/)

---
