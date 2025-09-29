---
layout: default-layout
title: How to avoid incorrect barcode results?
keywords: Dynamsoft Barcode Reader, FAQ, JavaScript, Troubleshooting / User Cases, avoid incorrect barcode results
description: How to avoid incorrect barcode results?
needAutoGenerateSidebar: false
---

# How to avoid incorrect barcode results?

[<< Back to FAQ index](index.md)

- One method is to raise the value of [minResultConfidence](https://www.dynamsoft.com/barcode-reader/docs/web/programming/javascript/api-reference/interface/RuntimeSettings.html#minresultconfidence) of the `RuntimeSettings` to a value of 50 or higher. It is set to 30 by default.
- If the issue has to do with the length of the text result, you can try setting a minimum length for the barcode text(s) that are returned by the SDK. By setting the [minBarcodeTextLength](https://www.dynamsoft.com/barcode-reader/docs/web/programming/javascript/api-reference/interface/RuntimeSettings.html#minbarcodetextlength) property of the `RuntimeSettings`, the SDK can ignore results that are consistently coming out shorter than expected.
---

> **Notice (Temporary Issue)**  
> This is a known issue in the current release and will be fixed in the next version.  
>  
> As a temporary solution, please set `IncludeTrailingCheckDigit` to `0` in the `BarcodeFormatSpecification` for Code128.  
> This will prevent the SDK from returning the trailing check digit.

### CODE_128 decoding returns an extra byte?

When using DBR v11, you may notice that decoding a **CODE_128** barcode returns one extra byte at the end if you call `item.get_bytes()`.

**Cause**  
By default, DBR includes the trailing check digit for CODE_128 in the decoded byte results.

**Solution**  
Set `IncludeTrailingCheckDigit` to `0` in the `BarcodeFormatSpecification` for Code128.

**Example JSON Configuration**

```json
{
  "BarcodeFormatSpecificationOptions": [
    {
      "Name": "bfs1",
      "BarcodeFormatIds": [
        "BF_CODE_128"
      ],
      "MinResultConfidence": 30,
      "RequireStartStopChars": 1,
      "ReturnPartialBarcodeValue": 1,
      "VerifyCheckDigit": 0,
      "IncludeTrailingCheckDigit": 0
    }
  ],
  #...Other Settings
}
