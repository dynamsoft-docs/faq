---
layout: default-layout
title: Editing Parsed MRZ Results - MRZ Scanner JS FAQs
keywords: Dynamsoft MRZ Scanner, FAQ, edit MRZ result, allowResultEditing, MRZResultViewConfig, result correction
description: Can users edit the parsed MRZ results? - MRZ Scanner JS FAQs.
needAutoGenerateSidebar: true
---

# Can users edit the parsed MRZ results?

[<< Back to FAQ index](index.md)

Yes. The [`MRZResultViewConfig`](https://www.dynamsoft.com/mrz-scanner/docs/web/api/mrz-scanner.html#mrzresultviewconfig) interface includes an `allowResultEditing` property (default: `false`) that enables editing of the parsed MRZ fields. When set to `true`, the result view will display the MRZ data in an editable format, allowing users to correct any errors before proceeding.

For example, to allow result editing:

```js
const mrzScanner = new Dynamsoft.MRZScanner({
    license: "YOUR_LICENSE_KEY",
    resultViewConfig: {
        allowResultEditing: true, // default: false
        showOriginalImage: true, // default: true
    }
});
````

---

| **Feature**       | **Property**         | **Default** |
| ----------------- | -------------------- | ----------- |
| Allow result edit | `allowResultEditing` | `false`     |

---

> 💡 **Note**:
> You may choose to allow the user to edit the result fields after cross-checking them with the info present on the document itself by displaying the original document with `showOriginalImage: true`.
