---
layout: default-layout
title: What barcode types are supported by Dynamsoft Barcode Reader?
keywords: Dynamsoft Barcode Reader, FAQ, DBR Introduction, General, formats
description: What barcode types are supported by Dynamsoft Barcode Reader?
needAutoGenerateSidebar: false
---

## What barcode types are supported by Dynamsoft Barcode Reader?

[<< Back to FAQ index](index.md)


Most common barcode formats are enabled by default. The full list of supported barcode formats can be found [here](https://www.dynamsoft.com/barcode-reader/docs/core/introduction/?ver=latest#supported-barcode-formats).

However, please note that the following formats require **manual configuration** before they can be decoded:
- **Code 32**  
- **Matrix 2 of 5**  
- **Telepen**

### Step-by-Step Guide

#### Step 1. Configure Barcode Formats
Update your code to explicitly enable **only the licensed formats**. Here are examples for enabling **Multiple Formats**(Use bitwise OR (|) to combine formats):

<div class="sample-code-prefix template2"></div>
   >- Javascript
   >- Objective-C
   >- Swift
   >- Android
   >- Python
   >- C++
   >- C#
   >
>
```javascript
let settings = await router.getSimplifiedSettings("ReadSingleBarcode");
// Enable QR Code and OneD
settings.barcodeSettings.barcodeFormatIds = 
  Dynamsoft.DBR.EnumBarcodeFormat.BF_MATRIX_25 | Dynamsoft.DBR.EnumBarcodeFormat.BF_CODE_32 | Dynamsoft.DBR.EnumBarcodeFormat.TELEPEN;
await router.updateSettings("ReadSingleBarcode", settings);
await router.startCapturing("ReadSingleBarcode");
```
>
```objc
DSBarcodeScannerConfig *config = [[DSBarcodeScannerConfig alloc] init];
config.barcodeFormats = DSBarcodeFormatQRCode | DSBarcodeFormatOned; ;
```
>
```swift
let config = BarcodeScannerConfig()
config.barcodeFormats = [.oneD, .qrCode]
```
>
```java
try {
   // Obtain current runtime settings. `cvr` is an instance of `CaptureVisionRouter`.
   // Here we use `EnumPresetTemplate.PT_READ_BARCODES` as an example. You can change it to your own template name or the name of other preset template.
   SimplifiedCaptureVisionSettings captureVisionSettings = cvr.getSimplifiedSettings(EnumPresetTemplate.PT_READ_BARCODES);
   captureVisionSettings.barcodeSettings.barcodeFormatIds = EnumBarcodeFormat.BF_MATRIX_25 | EnumBarcodeFormat.BF_CODE_32 | EnumBarcodeFormat.TELEPEN;
   // Update the settings. Remember to specify the same template name you used when getting the settings.
   cvr.updateSettings(EnumPresetTemplate.PT_READ_BARCODES, captureVisionSettings);
} catch (CaptureVisionRouterException e) {
   e.printStackTrace();
}
```
>
```python
cvr_instance = CaptureVisionRouter()
# Obtain current runtime settings of `CCaptureVisionRouter` instance.
err_code, err_str, settings = cvr_instance.get_simplified_settings(EnumPresetTemplate.PT_READ_BARCODES.value)
# Specify the barcode formats by enumeration values.
# Use "|" to enable multiple barcode formats at one time.
settings.barcode_settings.barcode_format_ids = EnumBarcodeFormat.BF_MATRIX_25.value | EnumBarcodeFormat.BF_CODE_32.value | EnumBarcodeFormat.TELEPEN.value
# Update the settings.
err_code, err_str = cvr_instance.update_settings(EnumPresetTemplate.PT_READ_BARCODES.value, settings)
```
>
```c++
char szErrorMsg[256] = {0};
// Obtain current runtime settings of `CCaptureVisionRouter` instance.
CCaptureVisionRouter* cvr = new CCaptureVisionRouter;
SimplifiedCaptureVisionSettings settings;
cvr->GetSimplifiedSettings(CPresetTemplate::PT_READ_BARCODES, &settings);
// Specify the barcode formats by enumeration values.
// Use "|" to enable multiple barcode formats at one time.
settings.barcodeSettings.barcodeFormatIds = BF_MATRIX_25 | BF_CODE_32 | TELEPEN;
// Update the settings.
cvr->UpdateSettings(CPresetTemplate::PT_READ_BARCODES, &settings, szErrorMsg, 256);
```
>
```csharp
using (CaptureVisionRouter cvr = new CaptureVisionRouter())
{
   SimplifiedCaptureVisionSettings settings;
   string errorMsg;
   // Obtain current runtime settings of `CCaptureVisionRouter` instance.
   cvr.GetSimplifiedSettings(PresetTemplate.PT_READ_BARCODES, out settings);
   // Specify the barcode formats by enumeration values.
   // Use "|" to enable multiple barcode formats at one time.
   settings.barcodeSettings.barcodeFormatIds = (ulong)(EnumBarcodeFormat.BF_MATRIX_25 | EnumBarcodeFormat.BF_CODE_32 | EnumBarcodeFormat.TELEPEN;
   // Update the settings.
   cvr.UpdateSettings(PresetTemplate.PT_READ_BARCODES, settings, out errorMsg);  
}
```
