# -*- coding: utf-8 -*-
import os
from playwright.sync_api import sync_playwright

ROOT_DIR = r'C:\Users\ASUS\Desktop\Diapositivas-Cartagena'
ARTIFACT_DIR = r'C:\Users\ASUS\.gemini\antigravity-ide\brain\a6624504-511c-4b9d-bc9a-468e348bde40'
TEMP_HTML = os.path.join(ROOT_DIR, 'temp_preview_s3_c.html')

BASE_TEMPLATE = """<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Preview Simplificada Slide 3</title>
  <link rel="stylesheet" href="styles.css?v=999">
</head>
<body>
  <main id="presentation-viewport">
    <div id="slides-stage">
      {SLIDE_CONTENT}
    </div>
  </main>
  <script src="app.js?v=999"></script>
</body>
</html>"""

# ==============================================================================
# VARIANTE C1: ULTRA-MINIMALISTA (Solo Número Grande + Título Claro, CERO texto pequeño)
# ==============================================================================
CONTENT_C1 = """
<section class="slide s-white active" id="slide-preview-3c1">
  <header class="slide-header">
    <div class="sh-left">
      <span class="sh-red-bar"></span>
      <span class="sh-category">ESTRUCTURA DE LA PONENCIA</span>
    </div>
    <img src="assets/image6.png" alt="#LoxTIC" class="sh-loxtic">
  </header>
  <div class="sh-divider"></div>

  <div class="slide-content-area" style="justify-content: center; padding-top: 25px; padding-bottom: 30px;">
    <h2 class="s-lead-question" style="margin-bottom: 45px; font-size: 38px;">
      Ruta de la Presentación
    </h2>

    <div style="display: flex; gap: 28px; max-width: 1650px; align-items: stretch;">
      
      <!-- Paso 01 -->
      <div style="flex: 1; background: #FAF5F5; border-top: 8px solid var(--c-wine-primary); padding: 50px 32px; display: flex; flex-direction: column; justify-content: center; min-height: 380px;">
        <div style="font-family: var(--font-sans); font-size: 76px; font-weight: 800; color: var(--c-wine-primary); line-height: 1; margin-bottom: 24px;">01</div>
        <div style="width: 48px; height: 4px; background: var(--c-wine-primary); margin-bottom: 24px;"></div>
        <h3 style="font-family: var(--font-sans); font-size: 32px; font-weight: 700; color: var(--c-text-dark); line-height: 1.3; margin: 0;">
          Contexto y Problema Rural
        </h3>
      </div>

      <!-- Paso 02 -->
      <div style="flex: 1; background: #FAF5F5; border-top: 8px solid #8B263E; padding: 50px 32px; display: flex; flex-direction: column; justify-content: center; min-height: 380px;">
        <div style="font-family: var(--font-sans); font-size: 76px; font-weight: 800; color: #8B263E; line-height: 1; margin-bottom: 24px;">02</div>
        <div style="width: 48px; height: 4px; background: #8B263E; margin-bottom: 24px;"></div>
        <h3 style="font-family: var(--font-sans); font-size: 32px; font-weight: 700; color: var(--c-text-dark); line-height: 1.3; margin: 0;">
          Metodología y Pipeline RAG
        </h3>
      </div>

      <!-- Paso 03 -->
      <div style="flex: 1; background: #FAF5F5; border-top: 8px solid var(--c-red-accent); padding: 50px 32px; display: flex; flex-direction: column; justify-content: center; min-height: 380px;">
        <div style="font-family: var(--font-sans); font-size: 76px; font-weight: 800; color: var(--c-red-accent); line-height: 1; margin-bottom: 24px;">03</div>
        <div style="width: 48px; height: 4px; background: var(--c-red-accent); margin-bottom: 24px;"></div>
        <h3 style="font-family: var(--font-sans); font-size: 32px; font-weight: 700; color: var(--c-text-dark); line-height: 1.3; margin: 0;">
          Resultados y Hallazgos
        </h3>
      </div>

      <!-- Paso 04 -->
      <div style="flex: 1; background: #FAF5F5; border-top: 8px solid var(--c-gold); padding: 50px 32px; display: flex; flex-direction: column; justify-content: center; min-height: 380px;">
        <div style="font-family: var(--font-sans); font-size: 76px; font-weight: 800; color: #9A7200; line-height: 1; margin-bottom: 24px;">04</div>
        <div style="width: 48px; height: 4px; background: var(--c-gold); margin-bottom: 24px;"></div>
        <h3 style="font-family: var(--font-sans); font-size: 32px; font-weight: 700; color: var(--c-text-dark); line-height: 1.3; margin: 0;">
          Conclusiones y Recomendaciones
        </h3>
      </div>

    </div>
  </div>

  <div class="slide-footer-rule"></div>
  <footer class="slide-footer">
    <span class="sf-left">VI CONGRESO CARTAGENA · 2026</span>
    <span class="sf-right">LOHACEMOSXTIC.COM · SLM OFFLINE</span>
  </footer>
</section>
"""

# ==============================================================================
# VARIANTE C2: CON 1 FRASE SENCILLA Y DIRECTA (en 24px, sin jerga pretenciosa)
# ==============================================================================
CONTENT_C2 = """
<section class="slide s-white active" id="slide-preview-3c2">
  <header class="slide-header">
    <div class="sh-left">
      <span class="sh-red-bar"></span>
      <span class="sh-category">ESTRUCTURA DE LA PONENCIA</span>
    </div>
    <img src="assets/image6.png" alt="#LoxTIC" class="sh-loxtic">
  </header>
  <div class="sh-divider"></div>

  <div class="slide-content-area" style="justify-content: center; padding-top: 15px; padding-bottom: 25px;">
    <h2 class="s-lead-question" style="margin-bottom: 38px; font-size: 38px;">
      Ruta de la Presentación
    </h2>

    <div style="display: flex; gap: 28px; max-width: 1650px; align-items: stretch;">
      
      <!-- Paso 01 -->
      <div style="flex: 1; background: #FAF5F5; border-top: 8px solid var(--c-wine-primary); padding: 40px 28px; display: flex; flex-direction: column; min-height: 380px;">
        <div style="font-family: var(--font-sans); font-size: 64px; font-weight: 800; color: var(--c-wine-primary); line-height: 1; margin-bottom: 16px;">01</div>
        <h3 style="font-family: var(--font-sans); font-size: 28px; font-weight: 700; color: var(--c-text-dark); line-height: 1.3; min-height: 72px; margin-bottom: 14px;">
          Contexto y Problema Rural
        </h3>
        <div style="width: 44px; height: 3px; background: var(--c-wine-primary); margin-bottom: 18px;"></div>
        <p style="font-family: var(--font-sans); font-size: 24px; line-height: 1.45; color: var(--c-gray-text); margin: 0;">
          Brecha de conectividad y necesidad de tutoría local sin internet.
        </p>
      </div>

      <!-- Paso 02 -->
      <div style="flex: 1; background: #FAF5F5; border-top: 8px solid #8B263E; padding: 40px 28px; display: flex; flex-direction: column; min-height: 380px;">
        <div style="font-family: var(--font-sans); font-size: 64px; font-weight: 800; color: #8B263E; line-height: 1; margin-bottom: 16px;">02</div>
        <h3 style="font-family: var(--font-sans); font-size: 28px; font-weight: 700; color: var(--c-text-dark); line-height: 1.3; min-height: 72px; margin-bottom: 14px;">
          Metodología y Pipeline RAG
        </h3>
        <div style="width: 44px; height: 3px; background: #8B263E; margin-bottom: 18px;"></div>
        <p style="font-family: var(--font-sans); font-size: 24px; line-height: 1.45; color: var(--c-gray-text); margin: 0;">
          Diseño del tutor en computadores escolares sin GPU.
        </p>
      </div>

      <!-- Paso 03 -->
      <div style="flex: 1; background: #FAF5F5; border-top: 8px solid var(--c-red-accent); padding: 40px 28px; display: flex; flex-direction: column; min-height: 380px;">
        <div style="font-family: var(--font-sans); font-size: 64px; font-weight: 800; color: var(--c-red-accent); line-height: 1; margin-bottom: 16px;">03</div>
        <h3 style="font-family: var(--font-sans); font-size: 28px; font-weight: 700; color: var(--c-text-dark); line-height: 1.3; min-height: 72px; margin-bottom: 14px;">
          Resultados y Hallazgos
        </h3>
        <div style="width: 44px; height: 3px; background: var(--c-red-accent); margin-bottom: 18px;"></div>
        <p style="font-family: var(--font-sans); font-size: 24px; line-height: 1.45; color: var(--c-gray-text); margin: 0;">
          Evaluación algorítmica frente al criterio de los docentes.
        </p>
      </div>

      <!-- Paso 04 -->
      <div style="flex: 1; background: #FAF5F5; border-top: 8px solid var(--c-gold); padding: 40px 28px; display: flex; flex-direction: column; min-height: 380px;">
        <div style="font-family: var(--font-sans); font-size: 64px; font-weight: 800; color: #9A7200; line-height: 1; margin-bottom: 16px;">04</div>
        <h3 style="font-family: var(--font-sans); font-size: 28px; font-weight: 700; color: var(--c-text-dark); line-height: 1.3; min-height: 72px; margin-bottom: 14px;">
          Conclusiones y Recomendaciones
        </h3>
        <div style="width: 44px; height: 3px; background: var(--c-gold); margin-bottom: 18px;"></div>
        <p style="font-family: var(--font-sans); font-size: 24px; line-height: 1.45; color: var(--c-gray-text); margin: 0;">
          Directrices prácticas para implementar IA en el aula real.
        </p>
      </div>

    </div>
  </div>

  <div class="slide-footer-rule"></div>
  <footer class="slide-footer">
    <span class="sf-left">VI CONGRESO CARTAGENA · 2026</span>
    <span class="sf-right">LOHACEMOSXTIC.COM · SLM OFFLINE</span>
  </footer>
</section>
"""

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page(viewport={"width": 1920, "height": 1080})

    for name, content, out_file in [
        ('C1_minimalista', CONTENT_C1, 'slide_03_c1_minimalista.png'),
        ('C2_frase_simple', CONTENT_C2, 'slide_03_c2_frase_simple.png')
    ]:
        full_html = BASE_TEMPLATE.replace('{SLIDE_CONTENT}', content)
        with open(TEMP_HTML, 'w', encoding='utf-8') as f:
            f.write(full_html)
        page.goto(f"file:///{TEMP_HTML.replace(os.sep, '/')}")
        page.wait_for_load_state('networkidle')
        page.wait_for_timeout(350)
        dest_path = os.path.join(ARTIFACT_DIR, out_file)
        page.screenshot(path=dest_path)
        print(f"Captured {name} -> {dest_path}")

    browser.close()

if os.path.exists(TEMP_HTML):
    os.remove(TEMP_HTML)
