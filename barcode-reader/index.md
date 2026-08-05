---
layout: default-layout
title: Barcode Reader FAQ
keywords: faq, dbr, barcode reader, dynamsoft, license, general, mobile, server, web
description: Index page for the Barcode Reader FAQ site.
needAutoGenerateSidebar: true
noTitleIndex: true
---

# Barcode Reader FAQ

Choose a category to get started.

<style>
  .faq-grid {
    display: grid;

    /*
     * Automatically switches between one and multiple columns according
     * to the actual content width, not the browser viewport width.
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

    font-size: clamp(1.35rem, 2vw, 1.75rem);
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

    font-size: 1.3rem;
    line-height: 1.3;
  }

  .faq-title {
    min-width: 0;
  }

  .faq-tile p {
    margin: 0;

    color: #4b5563;
    font-size: 1rem;
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
    href="/faq/barcode-reader/general/index.html"
    aria-label="General Barcode Reader FAQs"
  >
    <h2>
      <span class="faq-icon" aria-hidden="true">📚</span>
      <span class="faq-title">General</span>
    </h2>

    <p>
      Common questions, requirements, and core features of the Barcode Reader.
    </p>
  </a>

  <!-- License -->
  <a
    class="faq-tile"
    href="/faq/barcode-reader/license/index.html"
    aria-label="Barcode Reader License FAQs"
  >
    <h2>
      <span class="faq-icon" aria-hidden="true">🔑</span>
      <span class="faq-title">License</span>
    </h2>

    <p>
      Licensing details, trial versus production, activation, and deployment
      guidance.
    </p>
  </a>

  <!-- Mobile -->
  <a
    class="faq-tile"
    href="/faq/barcode-reader/mobile/index.html"
    aria-label="Barcode Reader Mobile FAQs"
  >
    <h2>
      <span class="faq-icon" aria-hidden="true">📱</span>
      <span class="faq-title">Mobile</span>
    </h2>

    <p>
      Mobile SDK usage, platform-specific setup, and optimization tips.
    </p>
  </a>

  <!-- Server, Desktop, and Embedded -->
  <a
    class="faq-tile"
    href="/faq/barcode-reader/server/index.html"
    aria-label="Barcode Reader Server, Desktop, and Embedded FAQs"
  >
    <h2>
      <span class="faq-icon" aria-hidden="true">🖥️</span>
      <span class="faq-title">Server / Desktop / Embedded</span>
    </h2>

    <p>
      Server, desktop, and embedded SDK usage, platform-specific setup, and
      optimization tips.
    </p>
  </a>

  <!-- Web -->
  <a
    class="faq-tile"
    href="/faq/barcode-reader/web/index.html"
    aria-label="Barcode Reader Web FAQs"
  >
    <h2>
      <span class="faq-icon" aria-hidden="true">🌐</span>
      <span class="faq-title">Web</span>
    </h2>

    <p>
      Web SDK setup, browser compatibility, configuration, and UI customization.
    </p>
  </a>

</div>
