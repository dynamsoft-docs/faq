---
layout: default-layout
title: Can I read barcodes from existing files?
keywords: Dynamsoft Barcode Reader, FAQ, tech basic, existing file
description: Can I read barcodes from existing files?
needAutoGenerateSidebar: false
---

# Can I read barcodes from existing files?

Yes, the JavaScript SDK supports reading from a file in local memory. 

## Version 10 and above
```javascript
let router = await Dynamsoft.CVR.CaptureVisionRouter.createInstance();
// Use the router to perform a job.
let results = await router.capture("blob:https://demo.dynamsoft.com/afb84bd2-e8cb-4b96-92b6-36dc89783692", "ReadSingleBarcode");
// ...
// Release the resources after the job is finished.
router.dispose();
```

## Version 9.x
```javascript
let reader = await Dynamsoft.DBR.BarcodeReader.createInstance();
let results = await reader.decode(imageSource);
```

> [this article](https://www.dynamsoft.com/barcode-reader/docs/web/programming/javascript/samples-demos/index.html) shows more details.
