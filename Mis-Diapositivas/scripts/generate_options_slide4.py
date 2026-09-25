# -*- coding: utf-8 -*-
"""
Genera y captura las 3 opciones de diseño para el Slide 4 (Separador Sección 1)
para que el usuario pueda compararlas visualmente.
"""
import os
from playwright.sync_api import sync_playwright

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ARTIFACT_DIR = r"C:\Users\ASUS\.gemini\antigravity-ide\brain\a6624504-511c-4b9d-bc9a-468e348bde40"
TEMP_HTML = os.path.join(ROOT_DIR, "temp_preview_s4.html")

BASE_TEMPLATE = """<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Preview Opciones Slide 4</title>
  <link rel="stylesheet" href="styles.css?v=9999">
</head>
<body>
  <main id="presentation-viewport">
    <div id="slides-stage">
      {SLIDE_CONTENT}
    </div>
  </main>
  <script src="app.js?v=9999"></script>
</body>
</html>"""

# ==============================================================================
# OPCION A: EDITORIAL INSTITUCIONAL (CONTINUIDAD CON LA PORTADA)
# ==============================================================================
CONTENT_A = """
<section class="slide s-cover active" id="slide-preview-4a">
  <!-- Silueta oficial de la Torre del Reloj como en la portada -->
  <img src="assets/image1.png" alt="Torre" class="s1-tower-bg" style="opacity: 0.22;">

  <!-- Contenido principal -->
  <div style="position: absolute; left: 5.7%; top: 28%; max-width: 1250px; z-index: 5;">
    
    <div style="display: flex; align-items: center; gap: 18px; margin-bottom: 24px;">
      <div style="width: 50px; height: 6px; background-color: var(--c-red-accent);"></div>
      <span style="font-family: var(--font-mono); font-size: 26px; font-weight: 700; color: var(--c-gold); letter-spacing: 2px;">
        01 &middot; PRIMER BLOQUE TEMÁTICO
      </span>
    </div>

    <h1 style="font-family: var(--font-sans); font-size: 76px; font-weight: 800; color: #FFFFFF; line-height: 1.15; margin-bottom: 24px;">
      Contexto y Problema Rural
    </h1>

    <p style="font-family: var(--font-sans); font-size: 32px; line-height: 1.4; color: rgba(255, 255, 255, 0.85); margin: 0; max-width: 1000px;">
      La brecha de conectividad en escuelas y la dependencia de servicios en la nube.
    </p>

  </div>

  <!-- Pie institucional sutil -->
  <div style="position: absolute; left: 5.7%; bottom: 6%; font-family: var(--font-mono); font-size: 22px; color: rgba(255, 255, 255, 0.5); letter-spacing: 1.5px; z-index: 5;">
    VI CONGRESO CARTAGENA &middot; 2026
  </div>
</section>
"""

# ==============================================================================
# OPCION B: ULTRA-MINIMALISTA (NUMERO MONUMENTAL + TITULO PURO)
# ==============================================================================
CONTENT_B = """
<section class="slide s-cover active" id="slide-preview-4b">
  <!-- Fondo limpio y elegante -->
  <div style="position: absolute; left: 5.7%; top: 24%; max-width: 1400px; z-index: 5;">
    
    <div style="display: flex; align-items: center; gap: 28px; margin-bottom: 20px;">
      <span style="font-family: var(--font-sans); font-size: 130px; font-weight: 800; color: var(--c-gold); line-height: 1;">
        01
      </span>
      <div style="width: 100px; height: 8px; background-color: var(--c-red-accent);"></div>
    </div>

    <h1 style="font-family: var(--font-sans); font-size: 82px; font-weight: 800; color: #FFFFFF; line-height: 1.12; margin: 0;">
      Contexto y Problema Rural
    </h1>

  </div>

  <!-- Pie sutil -->
  <div style="position: absolute; left: 5.7%; bottom: 6%; font-family: var(--font-mono); font-size: 22px; color: rgba(255, 255, 255, 0.5); letter-spacing: 1.5px; z-index: 5;">
    LOHACEMOSXTIC.COM &middot; SLM OFFLINE
  </div>
</section>
"""

# ==============================================================================
# OPCION C: CON INDICADOR DE RUTA (PASO 1 DE 4 ACTIVO)
# ==============================================================================
CONTENT_C = """
<section class="slide s-cover active" id="slide-preview-4c">
  <!-- Silueta sutil derecha -->
  <img src="assets/image1.png" alt="Torre" class="s1-tower-bg" style="opacity: 0.16;">

  <!-- Contenido central -->
  <div style="position: absolute; left: 5.7%; top: 24%; max-width: 1300px; z-index: 5;">
    
    <div style="display: flex; align-items: center; gap: 16px; margin-bottom: 20px;">
      <div style="width: 44px; height: 6px; background-color: var(--c-red-accent);"></div>
      <span style="font-family: var(--font-mono); font-size: 24px; font-weight: 700; color: var(--c-gold); letter-spacing: 2px;">
        FASE 1 DE 4
      </span>
    </div>

    <h1 style="font-family: var(--font-sans); font-size: 74px; font-weight: 800; color: #FFFFFF; line-height: 1.15; margin-bottom: 20px;">
      Contexto y Problema Rural
    </h1>

    <p style="font-family: var(--font-sans); font-size: 30px; line-height: 1.4; color: rgba(255, 255, 255, 0.85); margin: 0;">
      Brecha de conectividad y necesidad de tutoría local sin internet.
    </p>

  </div>

  <!-- Mini-Roadmap en la parte inferior -->
  <div style="position: absolute; left: 5.7%; bottom: 8%; width: 88.5%; display: flex; gap: 20px; z-index: 5;">
    
    <!-- Paso 1: Activo -->
    <div style="flex: 1; border-top: 4px solid var(--c-gold); padding-top: 14px;">
      <div style="font-family: var(--font-mono); font-size: 18px; font-weight: 700; color: var(--c-gold); margin-bottom: 4px;">01 &middot; ACTIVO</div>
      <div style="font-family: var(--font-sans); font-size: 22px; font-weight: 700; color: #FFFFFF;">Contexto Rural</div>
    </div>

    <!-- Paso 2: Pendiente -->
    <div style="flex: 1; border-top: 4px solid rgba(255,255,255,0.2); padding-top: 14px;">
      <div style="font-family: var(--font-mono); font-size: 18px; font-weight: 700; color: rgba(255,255,255,0.4); margin-bottom: 4px;">02</div>
      <div style="font-family: var(--font-sans); font-size: 22px; font-weight: 600; color: rgba(255,255,255,0.4);">Metodología RAG</div>
    </div>

    <!-- Paso 3: Pendiente -->
    <div style="flex: 1; border-top: 4px solid rgba(255,255,255,0.2); padding-top: 14px;">
      <div style="font-family: var(--font-mono); font-size: 18px; font-weight: 700; color: rgba(255,255,255,0.4); margin-bottom: 4px;">03</div>
      <div style="font-family: var(--font-sans); font-size: 22px; font-weight: 600; color: rgba(255,255,255,0.4);">Resultados</div>
    </div>

    <!-- Paso 4: Pendiente -->
    <div style="flex: 1; border-top: 4px solid rgba(255,255,255,0.2); padding-top: 14px;">
      <div style="font-family: var(--font-mono); font-size: 18px; font-weight: 700; color: rgba(255,255,255,0.4); margin-bottom: 4px;">04</div>
      <div style="font-family: var(--font-sans); font-size: 22px; font-weight: 600; color: rgba(255,255,255,0.4);">Conclusiones</div>
    </div>

  </div>
</section>
"""

options = [
    ("opcion_a", CONTENT_A, "slide_04_opcion_a.png"),
    ("opcion_b", CONTENT_B, "slide_04_opcion_b.png"),
    ("opcion_c", CONTENT_C, "slide_04_opcion_c.png"),
]

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page(viewport={"width": 1920, "height": 1080})

    for name, content, out_file in options:
        full_html = BASE_TEMPLATE.replace("{SLIDE_CONTENT}", content)
        with open(TEMP_HTML, "w", encoding="utf-8") as f:
            f.write(full_html)
        
        page.goto(f"file:///{TEMP_HTML.replace(os.sep, '/')}")
        page.wait_for_load_state("networkidle")
        page.wait_for_timeout(350)
        
        dest_path = os.path.join(ARTIFACT_DIR, out_file)
        page.screenshot(path=dest_path)
        print(f"Captured {name} -> {dest_path}")

    browser.close()

if os.path.exists(TEMP_HTML):
    os.remove(TEMP_HTML)

print("Todas las opciones de Slide 4 fueron capturadas con exito.")
