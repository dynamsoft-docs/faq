---
layout: default-layout
title: Is Dynamsoft Barcode Reader (DBR) Deterministic?
keywords: Dynamsoft Barcode Reader, FAQ, tech basic, deterministic, result variability, 
description: Dynamsoft Barcode Reader (DBR) generally produces consistent results under unchanged conditions but can show variability in specific scenarios due to parallel processing and result limits. 
needAutoGenerateSidebar: true
---

# Is Dynamsoft Barcode Reader (DBR) deterministic?

In most cases, yes.

When the following conditions remain unchanged, DBR will generally produce the same results for the same input image:
- The same input image
- The same SDK version
- The same programming language edition
- The same runtime settings
- The same platform and hardware environment

However, there are specific scenarios where the final reported results may vary between runs due to processing order and parallel execution.

---

## Q: When can results differ between runs?

### Scenario 1: Multiple Barcodes with a Limited Expected Barcode Count (All Versions)

This behavior applies to all versions of DBR.

If an image contains multiple readable barcodes but the settings limit the number of expected results, multiple barcode regions may be processed concurrently. When more valid barcodes are present than the configured result limit, the subset of returned barcodes may vary between runs.

**For example:**
- An image contains 7 barcodes.
- The application is configured to return only 4 barcodes.
- Different barcode regions may complete processing at different times, thus returning 4 different codes out of 7 each time.

In these cases, all returned results are valid barcodes from the image, but the subset returned may not always be identical.

### Scenario 2: Breadth-First Multi-Thread Decoding (DBR v11.6.1000+)

Starting with DBR v11.6.1000 (and corresponding DCV v3.6.1000), a breadth-first multi-thread decoding architecture was introduced to improve performance.
In this mode, multiple decoding tasks may execute simultaneously. Since thread completion order is not guaranteed, the final result can vary when multiple valid decoding paths exist.

**For example:**
- Deblur Mode A produces Result A.
- Deblur Mode B produces Result B.

Because both tasks run in parallel, the reported result may depend on which task completes first.

---

## Q: Does this mean DBR "hallucinates" like an LLM?

No.

DBR is not a generative AI system and does not generate, infer, predict, or invent barcode content.

All decoded results originate directly from information present in the source image. Any variation that may occur is due to processing order, thread scheduling, or result-selection behavior among multiple valid decoding outcomes. The SDK does not fabricate barcode values or produce results that are not supported by the image.

This behavior is fundamentally different from large language models (LLMs), whose outputs are generated probabilistically.

> [!Enterprise Note:]
> Dynamsoft barcode decoding is not a generative AI system. All returned results are derived from image content and supported by the data present in the image. Any observed variability is due to processing and result-selection order, not the creation of new, inferred, or fabricated information. This distinction is particularly important for organizations evaluating determinism, validation, auditability, or regulatory requirements.

---

## Q: Can I guarantee deterministic results?

In scenarios where strict repeatability is required, deterministic behavior can be achieved by configuring the SDK to use a single decoding thread:

`MaxParallelTasks = 1`

This ensures decoding tasks are processed in a consistent sequence rather than in parallel.

Please note that reducing the thread count may decrease overall decoding performance.

---

## Q: What is the recommended approach?

- Use the default multi-threaded configuration when maximum performance and throughput are the primary goals.
- Use MaxParallelTasks = 1 when strict repeatability is required for testing, validation, compliance, auditing, or other deterministic workflows.

---

## Summary

- DBR does not hallucinate or generate barcode data.
- Under identical conditions, DBR generally produces consistent results.
- Images containing multiple valid barcodes with a constrained expected barcode count may produce different valid result subsets.
- Starting with DBR v11.6.1000, breadth-first multi-thread decoding can introduce additional nondeterministic result selection in certain circumstances due to parallel task execution.
- Deterministic behavior can be enforced by setting MaxParallelTasks = 1, with a corresponding performance tradeoff.

