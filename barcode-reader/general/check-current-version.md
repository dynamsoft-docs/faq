---
layout: default-layout
title: How to Verify the Dynamsoft Barcode Reader JS SDK Version
keywords: Dynamsoft Barcode Reader, FAQ, tech basic, check version, current version
description: Step-by-step guide to identifying the current version of the Dynamsoft JS Barcode Reader SDK in web apps using API, npm, or CDN methods.
needAutoGenerateSidebar: false
---

# How to check the version of the SDK I am currently using?

There are multiple ways to check the version currently being used -

- The first way is to use the [version API](https://www.dynamsoft.com/barcode-reader/docs/web/programming/javascript/api-reference/barcode-reader-module-class.html#getversion). Using this API in the browser console should print out the version of the library being used by the web app.
- If you are using the library via npm or yarn, then you can check the version of the package via

    ```bash
    npm –v dynamsoft-javascript-barcode
    ```

- If you are including the library via the CDN link, then the version number should be mentioned in that reference link.

<div class="sample-code-prefix template2"></div>
   >- Javascript
   >- Objective-C
   >- Swift
   >- Android
   >- Python
   >- C++
   >- C#
   >
>
```javascript
const version = Dynamsoft.DBR.BarcodeReaderModule.getVersion();
console.log(version);
```
>
```objc
NSString *version = [DSBarcodeReaderModule getVersion];
NSLog(@"Dynamsoft Barcode Reader Version: %@", version);
```
>
```swift
let version = BarcodeReaderModule.getVersion()
print("Dynamsoft Barcode Reader Version: \(version)")
```
>
```java
BarcodeReaderModule reader = BarcodeReaderModule();
String versionInfo = reader.getVersion();
```
>
```python
reader = BarcodeReaderModule()
print(reader.get_version())
```
>
```c++
const char* version = CBarcodeReaderModule::GetVersion();
```
>
```csharp
string version = CBarcodeReaderModule.GetVersion();
```
