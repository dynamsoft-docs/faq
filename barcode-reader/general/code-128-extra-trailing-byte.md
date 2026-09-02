---
layout: default-layout
title: CODE_128 Decoding Returns an Extra Byte? – FAQ
keywords: Dynamsoft Barcode Reader, FAQ, Troubleshooting / User Cases, CODE_128, IncludeTrailingCheckDigit
description: Fix Dynamsoft Barcode Reader v11 CODE_128 decoding returning an extra trailing check digit byte by setting IncludeTrailingCheckDigit to 0.
needAutoGenerateSidebar: false
---

# CODE_128 decoding returns an extra byte?

When using DBR v11, you may notice that decoding a **CODE_128** barcode returns one extra byte at the end if you call `item.get_bytes()`.

**Cause**  
By default, DBR includes the trailing check digit for CODE_128 in the decoded byte results. This is a known issue in versions 11.0.0 - 11.0.6000 and has been fixed in version 11.2.

**Solution**  
Set `IncludeTrailingCheckDigit` to `0` in the `BarcodeFormatSpecification` for Code128. This will prevent the SDK from returning the trailing check digit.

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
```
