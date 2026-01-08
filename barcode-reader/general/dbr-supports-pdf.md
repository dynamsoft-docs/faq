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

### How to scan specific pages of a pdf file?
When processing PDF files, you can use the **[`set_pages()`](https://www.dynamsoft.com/capture-vision/docs/server/programming/python/api-reference/utility/directory-fetcher.html?product=dbr&lang=python#set_pages)** method to specify which pages should be scanned.  
This helps improve performance by avoiding unnecessary page processing.

- DirectoryFetcher

```python
# Example DirectoryFetcher: process only page 1 and page 3
# (page index follows the SDK's page numbering rules)
fetcher = DirectoryFetcher()
fetcher.set_directory("PATH_TO_YOUR_FOLDER")
fetcher.set_pages([1, 3])

cvr.set_input(fetcher)
```

- FileFetcher

```python
# Example FileFetcher: process only page 1 and page 3
# (page index follows the SDK's page numbering rules)
fetcher = FileFetcher()
fetcher.set_file("PATH_TO_YOUR_PDF")
fetcher.set_pages([1, 3])

cvr.set_input(fetcher)
```

### Additional Note: Multithreading Limitation
Please be aware that **PDF decoding does not support multithreading**.  
Even if your application uses multiple threads, PDF files will still be processed **single-threaded** due to the way PDF pages are handled internally.

If you need higher performance, it is recommended to **convert PDF pages into images** and then decode them in parallel.
