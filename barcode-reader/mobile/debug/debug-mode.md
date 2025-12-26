## How to use Debug Mode in Barcode Scanner X?

If you are experiencing app crashes in your own application or you’ve come across some barcode(s) that you can’t read and you have exhausted all of the other troubleshooting methods, Debug Mode of the [BarcodeScannerX](https://www.dynamsoft.com/barcode-reader/sdk-mobile/#appDemo) demo app can help offer one last effort to resolve these issues.

This next section will explain how to toggle on debug mode on the demo app, and will then dive into how to collect crash logs and/or image samples.

1. From the home screen, go to Advanced Scan.

    <img src="../assets/any_codes.png" alt="Home screen"  width="50%" height="50%">

2. Tap the settings icon at the top-right corner.

    <img src="../assets/any_codes_setting.png" alt="Advanced scan"  width="50%" height="50%">

3. Tap Debug Mode to see the drop-down list.

    <img src="../assets/debug_mode.jpg" alt="Debug mode"  width="50%" height="50%">

### Debug Mode - Crash Logger

If you are encountering an app crash caused by Dynamsoft Barcode Reader or Dynamsoft Camera Enhancer SDK, you need to use the Crash Logger.

1. Toggle on Crash Logger

    <img src="../assets/crash_toggle_on.jpg" alt="Crash toggle on"  width="50%" height="50%">

2. After Crash Logger is toggled on, please go ahead and scan codes until you reproduce the crash issue.

3. After the app crashes, re-open BarcodeScannerX app and go to Advanced Scan -> settings. Tap the "Share" button to share the log files with the [Dynamsoft support team](https://www.dynamsoft.com/contact/?ver=latest).

    <img src="../assets/crash_share.jpg" alt="Crash share"  width="50%" height="50%">

### Debug Mode - Image Cropper

If you are having trouble reading barcodes, you should use the Image Cropper to capture some sample image(s) or frame(s) and send them to the Dynamsoft Support Team:

1. Toggle on Image Cropper

    <img src="../assets/image_cropper_toggle.jpg" alt="Image crop toggle on"  width="50%" height="50%">

2. After Image Cropper is toggled on, an image crop icon will show up at the bottom left of Advanced Scan

    <img src="../assets/crop.jpg" alt="crop"  width="50%" height="50%">

3. Tap the image crop icon to crop and share the original frames with the [Dynamsoft support team](https://www.dynamsoft.com/contact/?ver=latest). Our support team will investigate the video frames and get back to you with a solution as soon as possible.

## How to Enable QR Code Model 1 in Barcode Scanner X?

Nowadays, most QR codes are QR code Model 2. BarcodeScannerX, by default, only support QR code Model 2. If you want to test QR code Model 1 on BarcodeScannerX, here is what you can do: 

1. Visit Dynamsoft barcode reader <a href="https://demo.dynamsoft.com/barcode-reader/" target="_blank">online demo</a>.
2. Click on Advanced Settings

   <div align="left">
      <p><img src="../assets/advanced-settings.jpg" width="40%" alt="advanced settings"></p>
   </div>

3. Check **EnableQRCodeModel1**.(You can modify any other settings as you like)
4. Save the template.

   <div align="left">
      <p><img src="../assets/save-template.jpg" width="40%" alt="save template"></p>
   </div>

5. Send the template to <a href="https://www.dynamsoft.com/contact/?ver=latest" target="_blank">Dynamsoft support team</a>.
6. We will generate and send a link to you.
7. Click **Import Template** in the Advanced Scan settings of BarcodeScannerX. Then input the link.
8. Now you can scan QR code Model 1!