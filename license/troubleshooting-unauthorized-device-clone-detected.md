---
layout: default-layout
title: Error -20151 Unauthorized Device Clone Detected
keywords: Dynamsoft Barcode Reader, Error -20151, Unauthorized Device Clone, License Error, DBR FAQ, License Validation
description: Understand the cause of error -20151 Unauthorized Device Clone Detected in Dynamsoft Barcode Reader and how to resolve it.
needAutoGenerateSidebar: false
---

# Troubleshoot - Error -20151 — Unauthorized Device Clone Detected

## What does error **-20151** mean?

The error **-20151: Unauthorized device clone detected** indicates that the license system has identified abnormal behavior suggesting that the same license is being used on what appears to be a cloned or altered device environment.

This is a **security protection mechanism** designed to prevent license misuse.

---

## 🔍 Common Causes

### 1️⃣ System Time Was Modified
If the **system date or time was manually changed** (for example, rolling the clock backward or forward), the license validation logic may interpret this as a potential cloning or tampering attempt.

Typical scenarios include:
- Manual system time adjustment  
- Time rollback after OS restore or snapshot  
- VM snapshot restore with outdated system time  

---

### 2️⃣ Switching SDK Versions Within a Short Period of Time
Rapidly **switching between different SDK versions** (for example, upgrading and downgrading, or running multiple major versions back-to-back) within a short timeframe can also trigger this error.

This may happen when:
- Testing multiple SDK versions on the same machine  
- Running parallel applications using different SDK versions  
- Rolling back to an older version shortly after upgrading  

The license system may treat this as an abnormal environment change.

---

## ✅ Recommended Solutions

- Ensure the **system time is correct** and synchronized with an official time source.
- Avoid frequently switching between different SDK versions on the same device.
- If testing multiple versions is required, allow sufficient time between version changes.
- Restart the system after correcting time settings or completing upgrades.

---

## 📩 Still Experiencing the Issue?

If the issue persists after verifying the above:
- Please contact our support team.
- Provide your **license key**, **SDK version**, and a brief description of your environment and recent changes.

