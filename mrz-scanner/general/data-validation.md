---
layout: default-layout
title: Data Validation of Decoded Results - MRZ Scanner JS FAQs
keywords: Dynamsoft MRZ Scanner, FAQ, MRZ, validation, check digit, client-side, decoded results
description: Does the MRZ Scanner perform any data validation on the decoded results? - MRZ Scanner JS FAQs.
needAutoGenerateSidebar: true
---

# Does the MRZ Scanner perform any data validation on the decoded results?

No. The Dynamsoft MRZ Scanner performs image capture, enhancement, and MRZ parsing entirely on the client device, but it **does not validate** the decoded fields or their contents. 

If your workflow requires additional validation (such as verifying check digits), your application must implement these checks after obtaining the parsed MRZ data.

---

> 💡 **Note**:  
> Validation logic (e.g., for check digits or document integrity) should be implemented by your application as needed.
