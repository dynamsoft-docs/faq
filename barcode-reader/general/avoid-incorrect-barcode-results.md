---
layout: default-layout
title: How to Avoid Incorrect Barcode Results?
keywords: Dynamsoft Barcode Reader, FAQ, Troubleshooting / User Cases, avoid incorrect barcode results, minResultConfidence, minBarcodeTextLength
description: Improve barcode decoding accuracy in Dynamsoft Barcode Reader by configuring minResultConfidence and minBarcodeTextLength on SimplifiedBarcodeReaderSettings.
needAutoGenerateSidebar: false
---

# How to avoid incorrect barcode results?

`SimplifiedBarcodeReaderSettings` — a sub-parameter of `SimplifiedCaptureVisionSettings` — exposes the same two filtering properties across every edition of Dynamsoft Barcode Reader (Server, Web, and Mobile), under each platform's own API reference, e.g. [C++](https://www.dynamsoft.com/barcode-reader/docs/server/programming/cplusplus/api-reference/simplified-barcode-reader-settings.html) and [JavaScript](https://www.dynamsoft.com/barcode-reader/docs/web/programming/javascript/api-reference/interfaces/simplified-barcode-reader-settings.html):

- **minResultConfidence** – raise this value (default `30`) to require a higher confidence before a result is returned. 50 or higher is a good starting point if you're seeing unreliable reads.
- **minBarcodeTextLength** – set this to the minimum length your barcode text should be; results shorter than this are discarded. For example, if your barcode text should always be at least 10 characters long, set it to `10` so the SDK ignores shorter, likely-incorrect results.

**Example (JavaScript):**
```javascript
let settings = await router.getSimplifiedSettings('ReadSingleBarcode');
settings.barcodeSettings.minResultConfidence = 40; //setting confidence
settings.barcodeSettings.minBarcodeTextLength = 5; //setting barcodeTextLength
await router.updateSettings('ReadSingleBarcode', settings);
```
