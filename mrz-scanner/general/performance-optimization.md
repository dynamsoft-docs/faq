---
layout: default-layout
title: Performance Options for Accuracy and Speed - MRZ Scanner JS FAQs
keywords: Dynamsoft MRZ Scanner, FAQ, performance, accuracy, speed, multi frame cross filter, enableMultiFrameCrossFilter
description: Are there any performance options to improve accuracy or speed? - MRZ Scanner JS FAQs.
needAutoGenerateSidebar: true
---

# Are there any performance options to improve accuracy or speed?

Yes. The scanner uses a multi-frame result cross filter to enhance accuracy. This filter is enabled by default, which helps reduce recognition errors by cross-verifying results across multiple frames. In [`MRZScannerViewConfig`](https://www.dynamsoft.com/mrz-scanner/docs/web/api/mrz-scanner.html#mrzscannerviewconfig), you can disable it to increase scanning speed, though this may slightly reduce accuracy.

To disable the cross filter:

```js
const mrzScanner = new Dynamsoft.MRZScanner({
    license: "YOUR_LICENSE_KEY",
    scannerViewConfig: {
        enableMultiFrameCrossFilter: false // default: false
    }
});
````

---

| **Option**                  | **Property**                  | **Default** | **Effect**                                      |
| --------------------------- | ----------------------------- | ----------- | ----------------------------------------------- |
| Multi-frame cross filtering | `enableMultiFrameCrossFilter` | `false`      | Improves accuracy; disabling may increase speed |

---

> 💡 **Note**:
> Disabling multi-frame cross filtering can make scanning faster, but may increase the risk of recognition errors.
