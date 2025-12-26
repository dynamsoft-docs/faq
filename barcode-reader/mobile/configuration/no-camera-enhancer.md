---
layout: default-layout
title: Use AVCaptureSession, CameraX or third-party camera modules - DBR Mobile FAQs.
keywords: Dynamsoft Barcode Reader, FAQ, Mobile, tech basic, android, ios, requirements
description: How can I use AVCaptureSession, CameraX or third-party camera modules with Dynamsoft Barcode Reader? - DBR Android FAQs.
needAutoGenerateSidebar: true
---

# How can I use AVCaptureSession, CameraX or third-party camera modules with Dynamsoft Barcode Reader - Android?

# Android

## CameraX

If you are using the CameraX, you can view [HelloWorld/DecodeWithCamerX sample](https://github.com/Dynamsoft/barcode-reader-mobile-samples/tree/main/android/FoundationalAPISamples/DecodeWithCameraX) for a quick start.

## Third-Party Camera Module

If you are using a third-party camera module, what you have to do is:

- Create a class that extends [ImageSourceAdapter](https://www.dynamsoft.com/capture-vision/docs/mobile/programming/android/api-reference/core/basic-structures/image-source-adapter.html?product=dbr&lang=android). In this class, you need to implement the video capture features and the [`getImage`](https://www.dynamsoft.com/capture-vision/docs/mobile/programming/android/api-reference/core/basic-structures/image-source-adapter.html#getimage) method of [ImageSourceAdapter](https://www.dynamsoft.com/capture-vision/docs/mobile/programming/android/api-reference/core/basic-structures/image-source-adapter.html?product=dbr&lang=android).
- Create an instance of your camera class.
- Create an instance of the [CaptureVisionRouter](https://www.dynamsoft.com/capture-vision/docs/mobile/programming/android/api-reference/capture-vision-router/multiple-file-processing.html?product=dbr&lang=android) class. Then trigger the [`setInput`](https://www.dynamsoft.com/capture-vision/docs/mobile/programming/android/api-reference/capture-vision-router/multiple-file-processing.html#setinput) method with the instance of your camera class as the parameter.
- Trigger the [`startCapturing`](https://www.dynamsoft.com/capture-vision/docs/mobile/programming/android/api-reference/capture-vision-router/multiple-file-processing.html#startcapturing) method to start the barcode decoding.

# iOS

## AVCaptureSession

If you are using the CameraX, you can view [HelloWorld/DecodeWithAVCaptureSession sample](https://github.com/Dynamsoft/barcode-reader-mobile-samples/tree/main/ios/FoundationalAPISamples/DecodeWithAVCaptureSession) for a quick start.

## Third-Party Camera Module

If you are using a third-party camera module, what you have to do is:

- Create a class that extends [DSImageSourceAdapter](https://www.dynamsoft.com/capture-vision/docs/mobile/programming/ios/api-reference/core/basic-structures/image-source-adapter.html?product=dbr&lang=objectivec-swift). In this class, you need to implement the video capture features and the [`getImage`](https://www.dynamsoft.com/capture-vision/docs/mobile/programming/ios/api-reference/core/basic-structures/image-source-adapter.html?product=dbr&lang=objectivec-swift) method of [DSImageSourceAdapter](https://www.dynamsoft.com/capture-vision/docs/mobile/programming/ios/api-reference/core/basic-structures/image-source-adapter.html?product=dbr&lang=objectivec-swift).
- Create an instance of your camera class.
- Create an instance of the [DSCaptureVisionRouter](https://www.dynamsoft.com/capture-vision/docs/mobile/programming/ios/api-reference/capture-vision-router/multiple-file-processing.html?product=dbr&lang=objectivec-swift) class. Then trigger the [`setInput`](https://www.dynamsoft.com/capture-vision/docs/mobile/programming/ios/api-reference/capture-vision-router/multiple-file-processing.html?product=dbr&lang=objectivec-swift#setinput) method with the instance of your camera class as the parameter.
- Trigger the [`startCapturing`](https://www.dynamsoft.com/capture-vision/docs/mobile/programming/ios/api-reference/capture-vision-router/multiple-file-processing.html?product=dbr&lang=objectivec-swift#startcapturing) method to start the barcode decoding.
