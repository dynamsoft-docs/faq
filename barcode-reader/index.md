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
  <a class="faq-tile" href="/faq/barcode-reader/general/index.html" aria-label="General Barcode Reader FAQs">
    <h2>📚 General</h2>
    <p>Common questions, requirements, and core features of the Barcode Reader.</p>
  </a>

  <!-- License -->
  <a class="faq-tile" href="/faq/barcode-reader/license/index.html" aria-label="License FAQs">
    <h2>🔑 License</h2>
    <p>Licensing details, trial vs. production, activation, and deployment guidance.</p>
  </a>

  <!-- Mobile -->
  <a class="faq-tile" href="/faq/barcode-reader/mobile/index.html" aria-label="Barcode Reader Mobile FAQs">
    <h2>📱 Mobile</h2>
    <p>Mobile SDK usage, platform-specific setup, and optimization tips.</p>
  </a>

  <!-- Server -->
  <a class="faq-tile" href="/faq/barcode-reader/server/index.html" aria-label="Barcode Reader Server FAQs">
    <h2>🖥️ Server/Desktop/Embedded</h2>
    <p>Server/Desktop/Embedded SDK usage, platform-specific setup, and optimization tips.</p>
  </a>

  <!-- Web -->
  <a class="faq-tile" href="/faq/barcode-reader/web/index.html" aria-label="Barcode Reader Web FAQs">
    <h2>🌐 Web</h2>
    <p>Web SDK setup, browser compatibility, configuration, and UI customization.</p>
  </a>

</div>
