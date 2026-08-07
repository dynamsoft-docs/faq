---
layout: default-layout
title: MRZ Scanner FAQ - Formats, Licensing, Usage & Integration
keywords: faq, mrz, mrz scanner, dynamsoft, license, general
description: Index page for the MRZ Scanner FAQ site with large navigation buttons.
needAutoGenerateSidebar: true
noTitleIndex: true
---

# MRZ Scanner FAQ

Choose a category to get started.

<style>
  .faq-grid {
    display: grid;

    /*
     * Automatically switches between one and multiple columns according
     * to the available container width, not the browser viewport width.
     */
    grid-template-columns: repeat(
      auto-fit,
      minmax(min(100%, 280px), 1fr)
    );

    gap: 20px;
    margin: 24px 0 8px;
    align-items: stretch;
  }

  .faq-tile {
    /*
     * Prevent long headings from forcing a grid column to become wider.
     */
    min-width: 0;
    min-height: 180px;

    display: flex;
    flex-direction: column;

    padding: 24px;

    color: inherit;
    text-decoration: none;

    background: #fff;
    border: 1px solid #e5e7eb;
    border-radius: 14px;

    box-shadow:
      0 4px 8px rgba(0, 0, 0, 0.03),
      0 8px 20px rgba(0, 0, 0, 0.04);

    transition:
      transform 0.15s ease,
      box-shadow 0.15s ease,
      border-color 0.15s ease;
  }

  .faq-tile:hover {
    color: inherit;
    text-decoration: none;

    transform: translateY(-2px);
    border-color: #4a9af5;

    box-shadow:
      0 6px 12px rgba(0, 0, 0, 0.05),
      0 12px 28px rgba(0, 0, 0, 0.08);
  }

  .faq-tile:focus-visible {
    outline: 3px solid rgba(74, 154, 245, 0.35);
    outline-offset: 3px;
  }

  .faq-tile h2 {
    min-width: 0;

    display: flex;
    align-items: flex-start;
    gap: 10px;

    margin: 0 0 12px;

    font-size: clamp(1.75rem, 1.1rem + 1.2vw, 2.5rem);
    line-height: 1.25;
    font-weight: 600;

    /*
     * Allows long titles to wrap instead of changing the grid width.
     */
    overflow-wrap: anywhere;
    word-break: normal;
  }

  .faq-icon {
    flex: 0 0 auto;

    font-size: 1em;
    line-height: 1.3;
  }

  .faq-title {
    min-width: 0;
  }

  .faq-tile p {
    margin: 0;

    color: #4b5563;
    line-height: 1.55;
  }

  /*
   * Disable animation for visitors who prefer reduced motion.
   */
  @media (prefers-reduced-motion: reduce) {
    .faq-tile {
      transition: none;
    }

    .faq-tile:hover {
      transform: none;
    }
  }
</style>

<div class="faq-grid">

  <!-- General -->
  <a
    class="faq-tile"
    href="/faq/mrz-scanner/general/index.html"
    aria-label="General MRZ Scanner FAQs"
  >
    <h2>
      <span class="faq-icon" aria-hidden="true">📚</span>
      <span class="faq-title">General</span>
    </h2>

    <p>
      Common questions, requirements, and behavior of the MRZ Scanner.
    </p>
  </a>

  <!-- License -->
  <a
    class="faq-tile"
    href="/faq/mrz-scanner/license/index.html"
    aria-label="MRZ Scanner License FAQs"
  >
    <h2>
      <span class="faq-icon" aria-hidden="true">🔑</span>
      <span class="faq-title">License</span>
    </h2>

    <p>
      How licensing works, trial versus production, and deployment guidance.
    </p>
  </a>

</div>

---

## Quick Links

- [What MRZ formats does the Dynamsoft MRZ Scanner support?](/faq/mrz-scanner/general/mrz-formats-supported.html)
- [Can the MRZ Scanner process static images or PDFs, or does it only work with a live camera?](/faq/mrz-scanner/general/static-image-and-pdf-support.html)
- [Does the MRZ Scanner perform any data validation on the decoded results?](/faq/mrz-scanner/general/data-validation.html)
- [How can I customize the scanner UI (hide the scan guide, format selector, upload button, etc.)?](/faq/mrz-scanner/general/ui-customization.html)
- [How do I handle the scanned results in my application?](/faq/mrz-scanner/general/handling-results.html)
- [How to expand the quota for a runtime license?](/faq/mrz-scanner/license/expand-quota-for-runtime-license.html)
- [How does license tracking work?](/faq/mrz-scanner/license/how-license-tracking-works.html)
- [SDK works without internet?](/faq/mrz-scanner/license/sdk-works-without-internet.html)
- [How to track license usage?](/faq/mrz-scanner/license/track-license.html)
- [How to get a free trial?](/faq/mrz-scanner/license/dbr-free-trial.html)
