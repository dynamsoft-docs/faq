---
layout: default-layout
title: Why does the camera video look distorted after switching cameras on iOS 27?
keywords: iOS 27, camera, distorted, video, switching camera, Safari, Chrome, Edge, Firefox, WebKit, Dynamsoft Camera Enhancer, Dynamsoft Barcode Reader, Dynamsoft MRZ Scanner
description: On iOS 27, switching the active camera or capture resolution can make the live video preview render distorted or fit its container incorrectly. Fixed in dynamsoft-barcode-reader-bundle 11.6.3200 and dynamsoft-capture-vision-bundle 3.6.3200; a CSS workaround is available for some versions.
needAutoGenerateSidebar: false
---

# Why does the camera video look distorted after switching cameras on iOS 27?

## Applicable Products

This article applies to:

- Dynamsoft Barcode Reader (DBR) JavaScript SDK (`dynamsoft-barcode-reader-bundle`) 11.6.3000 and earlier
- Dynamsoft Capture Vision (DCV) JavaScript SDK (`dynamsoft-capture-vision-bundle`) 3.6.3000 and earlier

## Summary

On iOS 27, switching cameras or changing resolution can make the live camera preview render incorrectly. The exact behavior depends on the SDK version:

| Version | Behavior |
|---|---|
| DBR 11.4 – 11.6.3000 (DCV 3.4 – 3.6.3000) | The preview renders distorted — squeezed or stretched instead of filling its container. Intermittent: the same switch can render correctly on one attempt and distorted on the next. |
| DBR 11.2 and earlier (DCV 3.2 and earlier) | The preview isn't distorted, but it no longer fits its container — shown at the wrong zoom or size and not extending to the borders. |

It's reproducible on Safari, Chrome, Edge, and Firefox — all iOS browsers share WebKit's camera implementation, so we suspect the issue originates there rather than in any Dynamsoft SDK. It does not occur on iOS 26.

> [!NOTE]
> Reported to Apple, but not confirmed as an Apple bug and still open as of iOS 27 RC. Details here may change if Apple ships a fix.

<div style="display: flex; flex-wrap: wrap; gap: 16px; margin: 16px 0;">
  <figure style="flex: 1 1 260px; max-width: 320px; margin: 0; text-align: center;">
    <img src="{{site.assets}}img/ios-27-switching-camera-expected.jpg" alt="Camera video rendering correctly on iOS" style="width: 100%; height: auto;">
    <figcaption><strong>Expected</strong></figcaption>
  </figure>
  <figure style="flex: 1 1 260px; max-width: 320px; margin: 0; text-align: center;">
    <img src="{{site.assets}}img/ios-27-switching-camera-distorted.jpg" alt="Camera video rendering distorted after switching cameras on iOS 27" style="width: 100%; height: auto;">
    <figcaption><strong>Distorted after switching cameras</strong></figcaption>
  </figure>
</div>

## Resolution

### Recommended: upgrade

Upgrade to `dynamsoft-barcode-reader-bundle` **11.6.3200+** or `dynamsoft-capture-vision-bundle` **3.6.3200+**, which include a built-in workaround. This is the only fix for DBR 11.2 / DCV 3.2 and earlier.

### If you can't upgrade yet: temporary CSS workaround (11.4 – 11.6.3000 only)

On these versions the distortion requires `object-fit: fill` on the video element plus an ancestor using `display: flex` with `flex: 0 0 auto`, so overriding `object-fit` with `cover` on the `<video>` element that [Dynamsoft Camera Enhancer](https://www.dynamsoft.com/camera-enhancer/docs/web/) renders avoids it:

```css
.dm-camera-core-container video {
  object-fit: cover !important;
}
```

`!important` is needed because the SDK sets `object-fit` inline. The JavaScript equivalent, via [`CameraView.getUIElement()`](https://www.dynamsoft.com/barcode-reader/docs/web/programming/javascript/user-guide/index.html#customizing-the-ui):

```javascript
let cameraView = await Dynamsoft.DCE.CameraView.createInstance();
let videoElement = cameraView.getUIElement().querySelector('video');
videoElement?.style.setProperty('object-fit', 'cover', 'important');
```

> [!WARNING]
> `cover` crops rather than stretches to preserve the aspect ratio — confirm that trade-off works for your UI. This is a temporary workaround, not a replacement for upgrading.

## Need more help?

[Contact the Dynamsoft Support team](https://www.dynamsoft.com/contact/).
