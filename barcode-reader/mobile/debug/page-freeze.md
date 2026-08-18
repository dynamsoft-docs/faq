---
layout: default-layout
title: Solve Page Freeze - DBR Mobile FAQs
keywords: Dynamsoft Barcode Reader, FAQ, Mobile, tech basic, ios, android, freeze, page, license
description: Why does the page sometimes freeze when I start the scanner? - DBR Mobile FAQs.
needAutoGenerateSidebar: true
---

# Why does the page sometimes freeze when I start the scanner?

Before a barcode reader instance can be created, a one-time connection for license validation needs to occur when the app initializes (or whenever the license is set before the barcode reader instance creation). Sometimes, this license validation could take a second to complete and could cause the UI to appear frozen.

A potential "freeze" of the page can occur if [`initLicense()`](https://www.dynamsoft.com/capture-vision/docs/mobile/programming/ios/api-reference/license/license-manager.html?product=dbr&lang=objectivec-swift#initlicense) is called multiple times in a single process. For example, if you call `initLicense` in both the `AppDelegate` and the `ViewController`, a conflict might occur. Please make sure that `initLicense` is called only once, ideally in the `AppDelegate`.

To help troubleshoot whether the method is being called multiple times, we recommend stepping through the code using a debugger.

---
