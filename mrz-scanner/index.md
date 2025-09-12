---
layout: default-layout
title: MRZ Scanner FAQ
keywords: faq, mrz, mrz scanner, dynamsoft, license, general
description: Index page for the MRZ Scanner FAQ site with large navigation buttons.
needAutoGenerateSidebar: true
noTitleIndex: true
---

# MRZ Scanner FAQ

Choose a category to get started.

<!-- Responsive 2x2-style grid (wraps to 1xN on small screens) -->
<style>
  .faq-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
    gap: 20px;
    margin: 24px 0 8px 0;
  }
  .faq-tile {
    display: block;
    text-decoration: none;
    padding: 28px 24px;
    border-radius: 16px;
    border: 1px solid rgba(0,0,0,0.06);
    box-shadow: 0 6px 16px rgba(0,0,0,0.06);
    transition: transform 0.08s ease, box-shadow 0.12s ease, border-color 0.12s ease;
    background: #fff;
  }
  .faq-tile:hover,
  .faq-tile:focus {
    transform: translateY(-2px);
    box-shadow: 0 10px 22px rgba(0,0,0,0.10);
    border-color: rgba(0,0,0,0.12);
    outline: none;
  }
  .faq-tile h2 {
    margin: 0 0 8px 0;
    font-size: 2.5rem;
    line-height: 1.2;
  }
  .faq-tile p {
    margin: 0;
    color: #444;
  }

  /* Prefer 2 columns on wider viewports for a "2x2" feel; auto-fit handles wrapping with 3 tiles */
  @media (min-width: 720px) {
    .faq-grid {
      grid-template-columns: repeat(2, 1fr);
    }
  }
</style>

<div class="faq-grid">

  <!-- General -->
  <a class="faq-tile" href="/faq/mrz-scanner/general/index.html" aria-label="General MRZ Scanner FAQs">
    <h2>📚 General</h2>
    <p>Common questions, requirements, and behavior of the MRZ Scanner.</p>
  </a>

  <!-- License -->
  <a class="faq-tile" href="/faq/mrz-scanner/license/index.html" aria-label="License FAQs">
    <h2>🔑License</h2>
    <p>How licensing works, trial vs. production, and deployment guidance.</p>
  </a>

</div>

---

## Quick Links

- [What MRZ formats does the Dynamsoft MRZ Scanner support?](/faq/mrz-scanner/general/mrz-formats-supported.html)
- [Can the MRZ Scanner process static images or PDFs, or does it only work with a live camera? ](/faq/mrz-scanner/general/static-image-and-pdf-support.html)
- [Does the MRZ Scanner perform any data validation on the decoded results?](/faq/mrz-scanner/general/data-validation.html)
- [How can I customize the scanner UI (hide the scan guide, format selector, upload button, etc.)?](/faq/mrz-scanner/general/ui-customization.html)
- [How do I handle the scanned results in my application?](/faq/mrz-scanner/general/handling-results.html)
- [How to expand the quota for a runtime license?](/faq/mrz-scanner/license/expand-quota-for-runtime-license.html)
- [How does license tracking work?](/faq/mrz-scanner/license/how-license-tracking-works.html)
- [SDK works without internet?](/faq/mrz-scanner/license/sdk-works-without-internet.html)
- [How to track license usage?](/faq/mrz-scanner/license/track-license.html)
- [How to get a free trial?](/faq/mrz-scanner/license/dbr-free-trial.html)
