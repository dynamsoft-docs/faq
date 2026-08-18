---
layout: default-layout
title: How do I remove the license warning or expiration pop-up in Dynamsoft Barcode Reader?
keywords: Dynamsoft Barcode Reader, FAQ, tech basic, barcodeReader, barcodeScanner, pop-up window
description: How do I remove the license warning or expiration pop-up in Dynamsoft Barcode Reader?
needAutoGenerateSidebar: false
---

# How do I remove the license warning or expiration pop-up in Dynamsoft Barcode Reader?

When using Dynamsoft Barcode Reader SDK without a valid license or with a temporary license, a warning pop-up appears at startup to notify you of the licensing status.

**Temporary License Warning**

With a temporary license, the SDK provides 24 hours of usage for testing purposes and displays the following warning:

![warning_info]({{site.dbr_web_assets}}warning-information.png)

**Expired License Warning**

After the 24-hour period expires, the warning changes to indicate the license has expired, and scanning functionality is disabled:

![expired_info]({{site.dbr_web_assets}}expired-information.png)

**Solution**

To remove these warnings and restore full functionality, initialize the SDK with either:

- A **purchased license**, or
- A **30-day trial license**

Once a valid license is applied, the temporary license warnings will no longer appear. You can refer [here](https://www.dynamsoft.com/barcode-reader/downloads/#javascript) to apply for a 30 day trial license. 

