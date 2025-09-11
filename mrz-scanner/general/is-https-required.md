---
layout: default-layout
title: HTTPS Requirement and Browser Support - MRZ Scanner JS FAQs
keywords: Dynamsoft MRZ Scanner, FAQ, HTTPS, browser support, secure context, WebAssembly, Chrome, Firefox, Safari, Edge
description: Does the Dynamsoft MRZ Scanner require HTTPS and which browsers are supported? - MRZ Scanner JS FAQs.
needAutoGenerateSidebar: true
---

# Does the MRZ Scanner require HTTPS, and which browsers are supported?

Yes. The Dynamsoft MRZ Scanner JavaScript edition requires your application to be served over **HTTPS** due to browser restrictions on camera access and licensing requirements. The only exceptions are `localhost` and local file paths during development.

In addition, the scanner depends on several modern browser features, including **WebAssembly**, **Blob**, **URL/createObjectURL**, and **Web Workers**.

---

## Supported Browsers

| **Browser**  | **Minimum Version** |
|--------------|---------------------|
| Chrome       | 78                  |
| Firefox      | 79                  |
| Safari       | 15                  |
| Edge         | 92                  |

---

> 💡 **Note**:  
> Camera access and licensing will not function in unsecured (HTTP) environments. For production deployments, always use HTTPS.
