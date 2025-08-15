---
layout: default-layout
title: Why is there a difference between the barcode formats listed under the 1D license and those shown on the website?
keywords: Dynamsoft Barcode Reader, FAQ, license, barcode format, BF_ONED, 1D license
description: Understanding the discrepancies between licensed 1D barcode formats and website documentation
needAutoGenerateSidebar: false
---

[<< Back to FAQ index](../index.md#scan-settings)

# Why is there a difference between the barcode formats listed under the 1D license and those shown on the website?

## Overview

There are discrepancies between the barcode formats included in the `BF_ONED` license and those listed on our website documentation. This FAQ explains these differences and how to properly configure your application.

## Licensed 1D Formats (BF_ONED)

For licensing purposes, the `BF_ONED` value includes the following barcode formats:

| Format             | Barcode Format ID     |
| ------------------ | --------------------- |
| Codabar            | `BF_CODABAR`          |
| Code 128           | `BF_CODE_128`         |
| Code 39            | `BF_CODE_39`          |
| Code 39 Extended   | `BF_CODE_39_EXTENDED` |
| Code 93            | `BF_CODE_93`          |
| EAN-13             | `BF_EAN_13`           |
| EAN-8              | `BF_EAN_8`            |
| Industrial 2 of 5  | `INDUSTRIAL_25`       |
| Interleaved 2 of 5 | `BF_ITF`              |
| UPC-A              | `BF_UPC_A`            |
| UPC-E              | `BF_UPC_E`            |
| MSI Code           | `BF_MSI_CODE`         |
| Code 11            | `BF_CODE_11`          |

## Additional Formats Listed on Website

On our website, we also show the following additional 1D barcode types that are **not** included in `BF_ONED`:

- Code 32
- Matrix 2 of 5
- GS1 DataBar
- Telepen

These extra formats are not technically included in `BF_ONED`, which may cause confusion.

## Support Status for Additional Formats

| Format        | Supported with 1D License | Requires Explicit Inclusion in barcodeFormatIds | Notes                     |
| ------------- | ------------------------- | ----------------------------------------------- | ------------------------- |
| Code 32       | ✅ Yes                    | ✅ Yes                                          | Not in BF_ONED by default |
| Matrix 2 of 5 | ✅ Yes                    | ✅ Yes                                          | Not in BF_ONED by default |
| Telepen       | ✅ Yes                    | ✅ Yes                                          | Not in BF_ONED by default |
| GS1 DataBar   | ❌ No                     | —                                               | Requires separate license |

## How to Enable Additional Supported Formats

To enable scanning for Code 32, Matrix 2 of 5, or Telepen, you must explicitly specify these formats in your code configuration:

```javascript
{
  "barcodeFormatIds": [
    "BF_ONED",
    "BF_CODE_32",
    "BF_MATRIX_2_OF_5",
    "BF_TELEPEN"
  ]
}
```

## Future Improvements

We are considering the following improvements:

| Option                          | Description                                                            |
| ------------------------------- | ---------------------------------------------------------------------- |
| ✅ Update product definition    | Include the extra 1D formats in BF_ONED by default                     |
| ✅ Update website documentation | Clearly state which barcodes are covered under the standard 1D license |

If you've encountered issues or confusion regarding this discrepancy, we encourage you to share feedback with our support team.
