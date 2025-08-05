---
layout: default-layout
title: Handling Scanned Results - MRZ Scanner JS FAQs
keywords: Dynamsoft MRZ Scanner, FAQ, handle result, onDone, resultViewConfig, MRZResult, callback
description: How do I handle the scanned results in my application? - MRZ Scanner JS FAQs.
needAutoGenerateSidebar: true
---

# How do I handle the scanned results in my application?

[<< Back to FAQ index](index.md)

To handle scanned results, provide an `onDone` callback within [`MRZResultViewConfig`](https://www.dynamsoft.com/mrz-scanner/docs/web/api/mrz-scanner.html#mrzresultviewconfig). When the user clicks the Done button, your callback receives an [`MRZResult`](https://www.dynamsoft.com/mrz-scanner/docs/web/api/mrz-scanner.html#mrzresult) object, which includes status codes, the parsed data, and an image of the MRZ. Your application can then process the fields as needed, such as logging or submitting data.

For example, to log the first name and status code:

```js
const mrzScanner = new Dynamsoft.MRZScanner({
    license: "YOUR_LICENSE_KEY",
    resultViewConfig: {
        onDone: (result) => {
            // result: MRZResult
            console.log("First name:", result.data.firstName);
            console.log("Status code:", result.status.code);
        }
    }
});
````

---

| **Callback** | **Location**       | **Description**                                  |
| ------------ | ------------------ | ------------------------------------------------ |
| `onDone`     | `resultViewConfig` | Called when user clicks Done; receives MRZResult |

---

> 💡 **Note**:
> The `MRZResult` object provides the decoded fields, the scan status, and the captured MRZ image. You can implement custom workflows or validation based on these values.
