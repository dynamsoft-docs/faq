---
layout: default-layout
title: Restricting Scanning to Specific Document Types - MRZ Scanner JS FAQs
keywords: Dynamsoft MRZ Scanner, FAQ, restrict document type, passport only, MRZScannerConfig, mrzFormatType
description: How do I restrict scanning to specific document types (e.g., only passports)? - MRZ Scanner JS FAQs.
needAutoGenerateSidebar: true
---

[<< Back to FAQ index](index.md)

# How do I restrict scanning to specific document types (e.g., only passports)?

You can restrict the Dynamsoft MRZ Scanner to only scan specific document types by setting the `mrzFormatType` property of [`MRZScannerConfig`](https://www.dynamsoft.com/mrz-scanner/docs/web/api/mrz-scanner.html#mrzscannerconfig). Specify an array of formats to limit scanning. For example, to allow only passports (TD3) and TD1 ID cards:

```js
const mrzScanner = new Dynamsoft.MRZScanner({
    license: "YOUR_LICENSE_KEY",
    mrzFormatType: ["passport", "td1"]
});
````

When only a single format is specified, the format selector UI will not appear.

---

| **Format**     | **Value**  |
| -------------- | ---------- |
| Passport (TD3) | "passport" |
| ID Card (TD1)  | "td1"      |
| ID Card (TD2)  | "td2"      |

---

> 💡 **Note**:
> Limiting the format enhances user experience and accuracy by hiding the format selector UI when only one format is allowed.

