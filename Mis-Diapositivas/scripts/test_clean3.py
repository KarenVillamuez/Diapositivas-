# -*- coding: utf-8 -*-
"""
Prueba Clean 3: Armonía total de proporciones para B3 sin textos residuales.
"""
import os
from playwright.sync_api import sync_playwright

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ARTIFACT_DIR = r"C:\Users\ASUS\.gemini\antigravity-ide\brain\a6624504-511c-4b9d-bc9a-468e348bde40"
TEMP_HTML = os.path.join(ROOT_DIR, "temp_preview_s5_clean3.html")

BASE_TEMPLATE = """<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Preview Clean 3 Slide 5</title>
  <link rel="stylesheet" href="styles.css?v=9999">
</head>
<body>
  <main id="presentation-viewport">
    <div id="slides-stage">
      {SLIDE_CONTENT}
    </div>
  </main>
</body>
</html>"""

CONTENT_3 = """
<section class="slide s-white active" id="slide-preview-clean-3">
  <header class="slide-header">
    <div class="sh-left">
      <span class="sh-red-bar"></span>
      <span class="sh-category">01 &middot; CONTEXTO Y PROBLEMA RURAL</span>
    </div>
    <img src="assets/image6.png" alt="#LoxTIC" class="sh-loxtic">
  </header>
  <div class="sh-divider"></div>

  <div class="slide-content-area" style="justify-content: center; padding-top: 10px; padding-bottom: 20px;">
    <h2 class="s-lead-question" style="font-size: 46px; font-weight: 800; margin-bottom: 36px; line-height: 1.2;">
      De la brecha de conectividad a las preguntas que guiaron el benchmark
    </h2>

    <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 36px; align-items: stretch;">
      
      <!-- Columna 1 -->
      <div style="background: var(--c-pink-bg); border-top: 8px solid var(--c-wine-primary); padding: 48px 38px; display: flex; flex-direction: column; justify-content: center;">
        <div style="font-family: var(--font-mono); font-size: 20px; font-weight: 700; color: var(--c-wine-primary); letter-spacing: 2px; margin-bottom: 12px;">
          01 &middot; LA REALIDAD
        </div>
        <div style="font-family: var(--font-sans); font-size: 76px; font-weight: 800; color: var(--c-wine-primary); line-height: 1; margin-bottom: 16px;">
          58.6%
        </div>
        <h3 style="font-family: var(--font-sans); font-size: 32px; font-weight: 700; color: var(--c-text-dark); margin-bottom: 16px;">
          Brecha Rural
        </h3>
        <p style="font-family: var(--font-sans); font-size: 28px; color: var(--c-gray-text); line-height: 1.45; margin: 0;">
          Hogares rurales en Colombia <strong>sin acceso a internet</strong> (DANE 2024).
        </p>
      </div>

      <!-- Columna 2 -->
      <div style="background: var(--c-pink-bg); border-top: 8px solid var(--c-red-accent); padding: 48px 38px; display: flex; flex-direction: column; justify-content: center;">
        <div style="font-family: var(--font-mono); font-size: 20px; font-weight: 700; color: var(--c-red-accent); letter-spacing: 2px; margin-bottom: 12px;">
          02 &middot; PREGUNTA 1
        </div>
        <div style="font-family: var(--font-sans); font-size: 76px; font-weight: 800; color: var(--c-red-accent); line-height: 1; margin-bottom: 16px;">
          SLM
        </div>
        <h3 style="font-family: var(--font-sans); font-size: 32px; font-weight: 700; color: var(--c-text-dark); margin-bottom: 16px;">
          Elecci&oacute;n de Modelo
        </h3>
        <p style="font-family: var(--font-sans); font-size: 28px; color: var(--c-gray-text); line-height: 1.45; margin: 0;">
          &iquest;Cu&aacute;l modelo compacto ofrece <strong>fluidez y precisi&oacute;n</strong> en CPU escolar?
        </p>
      </div>

      <!-- Columna 3 -->
      <div style="background: var(--c-pink-bg); border-top: 8px solid var(--c-gold); padding: 48px 38px; display: flex; flex-direction: column; justify-content: center;">
        <div style="font-family: var(--font-mono); font-size: 20px; font-weight: 700; color: #9A7200; letter-spacing: 2px; margin-bottom: 12px;">
          03 &middot; PREGUNTA 2
        </div>
        <div style="font-family: var(--font-sans); font-size: 76px; font-weight: 800; color: #9A7200; line-height: 1; margin-bottom: 16px;">
          Offline
        </div>
        <h3 style="font-family: var(--font-sans); font-size: 32px; font-weight: 700; color: var(--c-text-dark); margin-bottom: 16px;">
          Auditor&iacute;a de Calidad
        </h3>
        <p style="font-family: var(--font-sans); font-size: 28px; color: var(--c-gray-text); line-height: 1.45; margin: 0;">
          &iquest;C&oacute;mo auditar y calificar respuestas pedag&oacute;gicas <strong>sin internet</strong>?
        </p>
      </div>

    </div>
  </div>

  <div class="slide-footer-rule"></div>
  <footer class="slide-footer">
    <span class="sf-left">VI CONGRESO CARTAGENA &middot; 2026</span>
    <span class="sf-right">LOHACEMOSXTIC.COM &middot; SLM OFFLINE</span>
  </footer>
</section>
"""

def generate_clean_3():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(viewport={"width": 1920, "height": 1080})

        full_html = BASE_TEMPLATE.format(SLIDE_CONTENT=CONTENT_3)
        with open(TEMP_HTML, "w", encoding="utf-8") as f:
            f.write(full_html)

        page.goto("http://localhost:8085/temp_preview_s5_clean3.html", wait_until="networkidle")
        page.wait_for_timeout(600)

        out_root = os.path.join(ROOT_DIR, "slide_05_b3_clean_3.png")
        out_artifact = os.path.join(ARTIFACT_DIR, "slide_05_b3_clean_3.png")

        page.screenshot(path=out_root)
        page.screenshot(path=out_artifact)
        print("-> Captura guardada: slide_05_b3_clean_3.png")
        browser.close()

    if os.path.exists(TEMP_HTML):
        os.remove(TEMP_HTML)

if __name__ == "__main__":
    generate_clean_3()
