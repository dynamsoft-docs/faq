---
layout: default-layout
title: Can Barcode Reader SDK read PDF files? Do I need to pay for this feature?
keywords: Dynamsoft Barcode Reader, FAQ, DBR Introduction, General, PDF
description: Can Barcode Reader SDK read PDF files? Do I need to pay for this feature?
needAutoGenerateSidebar: false
---

## Can Barcode Reader SDK read PDF files? Do I need to pay for this feature?

Yes — **Dynamsoft Barcode Reader supports reading barcodes from PDF files** in most editions (see the official [Features](https://www.dynamsoft.com/barcode-reader/features/#Decode-Barcodes) page).  
The **only exceptions** are the **JavaScript edition** and the **Mobile edition**, which currently do **not** support PDF decoding.

### Do I need an extra license to read PDF files?
No. **Reading from PDF files does not require any additional license**. It is fully included in the standard SDK license.

### Additional Note: Multithreading Limitation
Please be aware that **PDF decoding does not support multithreading**.  
Even if your application uses multiple threads, PDF files will still be processed **single-threaded** due to the way PDF pages are handled internally.

If you need higher performance, it is recommended to **convert PDF pages into images** and then decode them in parallel.
