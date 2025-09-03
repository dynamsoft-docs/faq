---
layout: home-page
title: Dynamsoft Capture Vision FAQ
keywords: faq, capture vision, dcv, dynamsoft, barcode reader, mrz scanner
description: Dynamsoft Capture Vision FAQ Documentation
needAutoGenerateSidebar: false
noTitleIndex: true
---

# Dynamsoft Capture Vision FAQ

Select a product below to browse its FAQs.

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

  @media (min-width: 720px) {
    .faq-grid {
      grid-template-columns: repeat(2, 1fr);
    }
  }
</style>

<div class="faq-grid">

  <!-- Dynamic Web TWAIN -->
  <a class="faq-tile" href="/web-twain/docs/faq/" aria-label="Dynamic Web TWAIN FAQs">
    <h2>🖨️ Dynamic Web TWAIN</h2>
    <p>Image viewing and editing, UI customization, security, and error troubleshooting.</p>
  </a>

  <!-- Barcode Reader -->
  <a class="faq-tile" href="/faq/barcode-reader/" aria-label="Barcode Reader FAQs">
    <h2>📲 Barcode Reader</h2>
    <p>General usage, requirements, configuration, and troubleshooting guides.</p>
  </a>

  <!-- MRZ Scanner -->
  <a class="faq-tile" href="/faq/mrz-scanner/" aria-label="MRZ Scanner FAQs">
    <h2>🛂 MRZ Scanner</h2>
    <p>Setup, supported formats, UI customization, and integration examples.</p>
  </a>

</div>
