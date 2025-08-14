---
layout: default-layout
title: Static Image and PDF Support - MRZ Scanner JS FAQs
keywords: Dynamsoft MRZ Scanner, FAQ, static images, PDF, camera, server, desktop, JavaScript, mobile
description: Can the MRZ Scanner process static images or PDFs, or does it only work with a live camera? - MRZ Scanner JS FAQs.
needAutoGenerateSidebar: true
---

# Can the MRZ Scanner process static images or PDFs, or does it only work with a live camera?

[<< Back to FAQ index](index.md)

All editions of the Dynamsoft MRZ Scanner (server/desktop, mobile, and JavaScript) support scanning **static image files** in addition to live camera capture.

However, **only the server and desktop editions support direct PDF processing**. The JavaScript and mobile editions do **not** natively support PDF files; if you need to process a PDF in these editions, you must first convert the PDF into image files using an external tool or library.

---

| **Edition**        | **Static Images** | **PDF Files**     | **Live Camera** |
|--------------------|:----------------:|:-----------------:|:---------------:|
| Server/Desktop     | Yes              | Yes               | —               |
| Mobile             | Yes              | No<sup>†</sup>    | Yes             |
| JavaScript         | Yes              | No<sup>†</sup>    | Yes             |

<sup>†</sup> *PDF files must be converted to images for use with Mobile and JavaScript editions.*

---

> 💡 **Note**:  
> If you require PDF processing in the JavaScript or mobile edition, use an external converter to transform PDFs into image formats supported by the MRZ Scanner.
