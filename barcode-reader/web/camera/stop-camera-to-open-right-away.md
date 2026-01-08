---
layout: default-layout
title: How to enable the camera on the click of a button?
keywords: Dynamsoft Barcode Reader, FAQ, tech basic, stop camera stream, start scanning
description: How to enable the camera on the click of a button?
needAutoGenerateSidebar: false
---

# How to enable the camera on the click of a button?

## Version 10 and above
```javascript
let startScanBtn = document.getElementById("StartScanning"); // double check the ID of the button

startScanBtn.addEventListener("click", async function () {
  router = await Dynamsoft.CVR.CaptureVisionRouter.createInstance();
  let view = await Dynamsoft.DCE.CameraView.createInstance();
  cameraEnhancer = await Dynamsoft.DCE.CameraEnhancer.createInstance(view);
  router.setInput(cameraEnhancer);
  const resultReceiver = new Dynamsoft.CVR.CapturedResultReceiver();
  resultReceiver.onCapturedResultReceived = (result) => {
    /* Do something with the result */
  };
  router.addResultReceiver(resultReceiver);
  await cameraEnhancer.open();
  await router.startCapturing("ReadSingleBarcode");
})
```

## version 9

Instead of creating the `BarcodeScanner` instance on page load, trigger the creation on the click of the `Start Scanning` button instead, as shown in the sample code below -

```javascript
let startScanBtn = document.getElementById("StartScanning"); // double check the ID of the button
startScanBtn.addEventListener("click", async function () {
  let scanner = await Dynamsoft.DBR.BarcodeScanner.createInstance();
  scanner.onFrameRead = (results) => {
    console.log(results);
  };
  scanner.onUniqueRead = (txt, result) => {
    alert(txt);
  };
  await scanner.show();
});
```
