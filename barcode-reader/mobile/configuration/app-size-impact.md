---
layout: default-layout
title: App Size Impact - DBR Mobile FAQs
keywords: Dynamsoft Barcode Reader, FAQ, Mobile, Android, iOS, app size, bundle size, native libraries
description: Learn how integrating Dynamsoft Barcode Reader SDK affects the app size on Android and iOS.
needAutoGenerateSidebar: true
---

# How much does the SDK increase my app size?

When integrating the Dynamsoft Barcode Reader (DBR) SDK into your mobile application, the increase in app size is mainly due to native libraries packaged for different architectures. Here's what you need to know:

---

## Download Size vs Installed Size

**Compressed download size** is the actual file size users need to download when installing your app.

**Installed size** is the total space the app occupies on the user's device after installation. While it affects storage usage, it is generally less critical on modern devices with ample storage.

> **Tip:** Prioritize reducing download size to improve user experience and meet app store requirements.

---

## Android

### Size impact (arm64-v8a example)

| Dynamsoft Barcode Reader SDK | Size         |
| ---------------------------- | ------------ |
| Download Size                | **~10.3 MB** |
| Install Size                 | **~24 MB**   |

---

## iOS

| Dynamsoft Barcode Reader SDK | Size         |
| ---------------------------- | ------------ |
| Download Size(Thinned IPA)   | **~9.3 MB**  |
| Install Size                 | **~24.4 MB** |

---

## Flutter / React Native / MAUI

When using hybrid frameworks like Flutter, React Native, or MAUI:

- The app still includes native binaries for Android/iOS under the hood.
- Therefore, the **size impact is similar** to native apps.

---

## Need to reduce the SDK size?

If your app has **strict size constraints**, we offer a **paid customization service**.

We can help:

- Remove unused barcode symbologies
- Exclude features not needed by your app
- Deliver a **lighter-weight SDK** tailored to your usage

📩 To learn more, please [contact us](https://www.dynamsoft.com/company/contact/).

---
