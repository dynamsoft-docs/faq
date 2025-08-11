---
layout: default-layout
title: Customizing the Scanner UI - MRZ Scanner JS FAQs
keywords: Dynamsoft MRZ Scanner, FAQ, customize UI, hide scan guide, format selector, upload button, MRZScannerViewConfig
description: How can I customize the scanner UI (hide the scan guide, format selector, upload button, etc.)? - MRZ Scanner JS FAQs.
needAutoGenerateSidebar: true
---

# How can I customize the scanner UI (hide the scan guide, format selector, upload button, etc.)?

[<< Back to FAQ index](index.md)

The [`MRZScannerViewConfig`](https://www.dynamsoft.com/mrz-scanner/docs/web/api/mrz-scanner.html#mrzscannerviewconfig) interface allows you to control many UI elements of the Dynamsoft MRZ Scanner. You can show or hide features such as the scan guide, file upload button, format selector, sound toggle, and the “Powered By Dynamsoft” footer. Additional options include enabling or disabling multi-frame cross filtering, specifying accepted file types, and providing a custom `uploadFileConverter`.

For example, to hide the scan guide and disable multi-frame cross filtering:

```js
const mrzScanner = new Dynamsoft.MRZScanner({
    license: "YOUR_LICENSE_KEY",
    scannerViewConfig: {
        showScanGuide: true,
        showFormatSelector: true,
        showUploadImage: true,
    }
});
````

For more configurable elements, please view our guide [here](https://www.dynamsoft.com/mrz-scanner/docs/web/guides/mrz-scanner-customization.html#mrzscannerviewconfig-overview).

> 💡 **Note**:
> Hiding unnecessary UI elements and adjusting options can help streamline the user experience and tailor the scanner for your workflow.
