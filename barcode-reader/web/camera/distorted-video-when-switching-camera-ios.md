---
layout: default-layout
title: Why does the camera video look distorted after switching cameras on iOS 27?
keywords: iOS 27, camera, distorted, video, switching camera, portrait, Safari, Chrome, Edge, Firefox, WebKit, Dynamsoft Camera Enhancer, Dynamsoft Barcode Reader, Dynamsoft MRZ Scanner
description: On iOS 27, switching the active camera in portrait mode can make the live video stream render distorted. This is a known iOS bug affecting all browsers; a workaround is available starting with dynamsoft-barcode-reader-bundle 11.6.3200 and dynamsoft-capture-vision-bundle 3.6.3200.
needAutoGenerateSidebar: false
---

# Why does the camera video look distorted after switching cameras on iOS 27?

## Symptom

On devices running **iOS 27**, while your page is in **portrait mode**, switching the active camera device (for example, toggling between the front and back camera, or between multiple back cameras) at a capture resolution under 1080p can cause the live video stream to render distorted — squeezed into a small box instead of filling the video container correctly.

**Expected rendering:**

![Camera video rendering correctly on iOS]({{site.assets}}img/ios-27-switching-camera-expected.jpg)

**Distorted rendering after switching cameras:**

![Camera video rendering distorted after switching cameras on iOS 27]({{site.assets}}img/ios-27-switching-camera-distorted.jpg)

## Root cause

This is an **iOS platform bug**, not an issue specific to any Dynamsoft SDK. It reproduces in Safari, Chrome, Edge, and Firefox on iOS 27, since all browsers on iOS share the same underlying WebKit camera stack.

We reported this issue to Apple during the iOS 27 beta program. As of iOS 27 RC, Apple has not yet shipped a fix.

## Who is affected

Any web app that uses [Dynamsoft Camera Enhancer](https://www.dynamsoft.com/camera-enhancer/docs/web/) to render the camera video stream can be affected, including:

- Dynamsoft Barcode Reader JavaScript SDK (`dynamsoft-barcode-reader-bundle`, `dynamsoft-capture-vision-bundle`)
- Dynamsoft MRZ Scanner

## Workaround

We've added a workaround for this iOS behavior starting with:

- `dynamsoft-barcode-reader-bundle` **11.6.3200** and above
- `dynamsoft-capture-vision-bundle` **3.6.3200** and above

**We recommend upgrading to one of these versions or later** before iOS 27 is publicly released.

If you're not able to upgrade right away, avoid switching the camera device while in portrait mode at a resolution under 1080p on iOS 27 — for example, prompt users to select a camera device before opening the video stream, rather than switching afterward.

## Need more help?

If you're still seeing distorted video after upgrading, or if you have any questions, please [contact the Dynamsoft Support team](https://www.dynamsoft.com/contact/).
