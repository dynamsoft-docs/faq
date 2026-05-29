---
layout: default-layout
title: How to create custom settings template?
keywords: Dynamsoft Barcode Reader, FAQ, DBR Introduction, General, runtime settings, template
description: How to create custom settings template?
needAutoGenerateSidebar: false
---

# How to create custom settings template?

One of the strengths of the Dynamsoft Barcode Reader is its wide range of customizable options that can optimize the performance of the SDK. Whether your priority is read rate or speed, these settings can be tailored to suit various use cases.

If you are looking to create your own custom settings template for use with the [InitSettingsFromFile](https://www.dynamsoft.com/capture-vision/docs/server/programming/cplusplus/api-reference/capture-vision-router/settings.html?product=dbr&repoType=server#initsettingsfromfile) method, please follow these steps:

1. Visit the main [online demo](https://demo.dynamsoft.com/barcode-reader/).

2. On the left-hand side, locate the settings menu. Click on **Advanced Settings** to access the full range of options.

3. Modify the settings as needed.

4. To obtain the template, scroll to the bottom of the settings menu where you can find the full settings presented as a **Struct** or a **Template**. The **Struct** offers a more readable format, while the actual JSON code is available under **Template**.

5. Copy the JSON code from the **Template** section and paste it into your own JSON file, or download the template JSON file directly from the demo.

6. The downloaded template corresponds to the specific version of Dynamsoft Barcode Reader, specified in the title at top-left corner (e.g. "Ver. 11.4.20"). Please make sure to use the template with the same version. Otherwise, it may have conflicts issue.

With these steps, you will have your own template ready for use with the [InitSettingsFromFile](https://www.dynamsoft.com/capture-vision/docs/server/programming/cplusplus/api-reference/capture-vision-router/settings.html?product=dbr&repoType=server#initsettingsfromfile) method!

For more information on using `InitSettingsFromFile` method, please refer to **User Guide** > **Explore Features** > **Advanced Features** > **Use SimplifiedCaptureVisionSettings or Templates**.