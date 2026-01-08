---
layout: default-layout
title: Is HTTPs absolutely required?
keywords: Dynamsoft Barcode Reader, FAQ, tech basic, HTTPS
description: Is HTTPs absolutely required?
needAutoGenerateSidebar: false
---

# Is HTTPS absolutely required?

HTTPS is required to utilize `getUserMedia`/`MediaDevices` and initialize online license keys. If HTTPS is not enabled, you won't be able to use a camera and you will need an offline license key.

> 1. If you don't want to use a camera, you can enable [singleFrameMode](https://www.dynamsoft.com/camera-enhancer/docs/web/programming/javascript/api-reference/acquisition.html?product=dbr&lang=javascript#singleframemode) to scan barcodes on existing images.
> 2. During evaluation & testing, you can use 'http://localhost' which allows camera usage as well as online licensing.

