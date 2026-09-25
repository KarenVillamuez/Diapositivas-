# -*- coding: utf-8 -*-
"""
Genera y captura las 3 opciones de diseño para el Slide 3 (Estructura de la Ponencia)
para que el usuario pueda compararlas visualmente.
"""
import os
from playwright.sync_api import sync_playwright

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ARTIFACT_DIR = r"C:\Users\ASUS\.gemini\antigravity-ide\brain\a6624504-511c-4b9d-bc9a-468e348bde40"
TEMP_HTML = os.path.join(ROOT_DIR, "temp_preview_s3.html")

BASE_TEMPLATE = """<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Preview Opciones Slide 3</title>
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
# OPCION A: 4 FILAS EDITORIALES CON BARRAS LATERALES (CONTINUIDAD SLIDE 2)
# ==============================================================================
CONTENT_A = """
<section class="slide s-white active" id="slide-preview-3a">
  <header class="slide-header">
    <div class="sh-left">
      <span class="sh-red-bar"></span>
      <span class="sh-category">ESTRUCTURA DE LA PONENCIA</span>
    </div>
    <img src="assets/image6.png" alt="#LoxTIC" class="sh-loxtic">
  </header>
  <div class="sh-divider"></div>

  <div class="slide-content-area" style="justify-content: center; padding-top: 15px; padding-bottom: 20px;">
    <h2 class="s-lead-question" style="margin-bottom: 28px; font-size: 38px;">
      Cuatro momentos para desmontar la evaluación de la IA educativa local
    </h2>

    <div style="display: flex; flex-direction: column; gap: 20px; max-width: 1650px;">
      
      <!-- Fila 1 -->
      <div style="display: flex; align-items: center; gap: 36px; padding: 20px 32px; background: #FAF5F5; border-left: 8px solid var(--c-wine-primary);">
        <div style="flex: 0 0 160px; width: 160px; text-align: center;">
          <div style="font-family: var(--font-sans); font-size: 56px; font-weight: 800; color: var(--c-wine-primary); line-height: 1;">01</div>
        </div>
        <div style="width: 2px; height: 64px; background: var(--c-border-subtle); flex-shrink: 0;"></div>
        <div style="flex: 1;">
          <h3 style="font-family: var(--font-sans); font-size: 28px; font-weight: 700; color: var(--c-text-dark); margin-bottom: 6px;">Contexto y Desafío Rural</h3>
          <p style="font-family: var(--font-sans); font-size: 24px; line-height: 1.4; color: var(--c-gray-text); margin: 0;">
            La brecha invisible del <strong>58.6% sin internet</strong> y la urgencia de tutoría local autónoma en memoria USB sin suscripciones en la nube.
          </p>
        </div>
      </div>

      <!-- Fila 2 -->
      <div style="display: flex; align-items: center; gap: 36px; padding: 20px 32px; background: #FAF5F5; border-left: 8px solid #8B263E;">
        <div style="flex: 0 0 160px; width: 160px; text-align: center;">
          <div style="font-family: var(--font-sans); font-size: 56px; font-weight: 800; color: #8B263E; line-height: 1;">02</div>
        </div>
        <div style="width: 2px; height: 64px; background: var(--c-border-subtle); flex-shrink: 0;"></div>
        <div style="flex: 1;">
          <h3 style="font-family: var(--font-sans); font-size: 28px; font-weight: 700; color: var(--c-text-dark); margin-bottom: 6px;">Metodología y Pipeline RAG</h3>
          <p style="font-family: var(--font-sans); font-size: 24px; line-height: 1.4; color: var(--c-gray-text); margin: 0;">
            Arquitectura en <strong>CPU estándar de aula (sin GPU)</strong>, banco curricular de <strong>14 preguntas</strong> y matriz de <strong>784 inferencias</strong> registradas.
          </p>
        </div>
      </div>

      <!-- Fila 3 -->
      <div style="display: flex; align-items: center; gap: 36px; padding: 20px 32px; background: #FAF5F5; border-left: 8px solid var(--c-red-accent);">
        <div style="flex: 0 0 160px; width: 160px; text-align: center;">
          <div style="font-family: var(--font-sans); font-size: 56px; font-weight: 800; color: var(--c-red-accent); line-height: 1;">03</div>
        </div>
        <div style="width: 2px; height: 64px; background: var(--c-border-subtle); flex-shrink: 0;"></div>
        <div style="flex: 1;">
          <h3 style="font-family: var(--font-sans); font-size: 28px; font-weight: 700; color: var(--c-text-dark); margin-bottom: 6px;">Resultados y el Falso Empate</h3>
          <p style="font-family: var(--font-sans); font-size: 24px; line-height: 1.4; color: var(--c-gray-text); margin: 0;">
            La ilusión métrica del <strong>0.795</strong>, modos de fallo asimétricos (<strong>alucinación vs. sobre-rechazo</strong>) y el choque con el criterio docente.
          </p>
        </div>
      </div>

      <!-- Fila 4 -->
      <div style="display: flex; align-items: center; gap: 36px; padding: 20px 32px; background: #FAF5F5; border-left: 8px solid var(--c-gold);">
        <div style="flex: 0 0 160px; width: 160px; text-align: center;">
          <div style="font-family: var(--font-sans); font-size: 56px; font-weight: 800; color: #9A7200; line-height: 1;">04</div>
        </div>
        <div style="width: 2px; height: 64px; background: var(--c-border-subtle); flex-shrink: 0;"></div>
        <div style="flex: 1;">
          <h3 style="font-family: var(--font-sans); font-size: 28px; font-weight: 700; color: var(--c-text-dark); margin-bottom: 6px;">Discusión y Conclusiones</h3>
          <p style="font-family: var(--font-sans); font-size: 24px; line-height: 1.4; color: var(--c-gray-text); margin: 0;">
            <strong>Matriz de riesgo institucional</strong> para adoptar tutores locales y directrices ético-técnicas para el aula real.
          </p>
        </div>
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
# OPCION B: CUADRANTE 2x2 (PANELES BALANCEADOS)
# ==============================================================================
CONTENT_B = """
<section class="slide s-white active" id="slide-preview-3b">
  <header class="slide-header">
    <div class="sh-left">
      <span class="sh-red-bar"></span>
      <span class="sh-category">ESTRUCTURA DE LA PONENCIA</span>
    </div>
    <img src="assets/image6.png" alt="#LoxTIC" class="sh-loxtic">
  </header>
  <div class="sh-divider"></div>

  <div class="slide-content-area" style="justify-content: center; padding-top: 15px; padding-bottom: 20px;">
    <h2 class="s-lead-question" style="margin-bottom: 28px; font-size: 38px;">
      Cuatro momentos para desmontar la evaluación de la IA educativa local
    </h2>

    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 26px; max-width: 1650px;">
      
      <!-- Cuadrante 01 -->
      <div style="background: #FAF5F5; border-top: 8px solid var(--c-wine-primary); padding: 28px 32px;">
        <div style="display: flex; align-items: center; gap: 20px; margin-bottom: 12px;">
          <span style="font-family: var(--font-sans); font-size: 46px; font-weight: 800; color: var(--c-wine-primary); line-height: 1;">01</span>
          <div style="width: 2px; height: 38px; background: var(--c-border-subtle);"></div>
          <h3 style="font-family: var(--font-sans); font-size: 28px; font-weight: 700; color: var(--c-text-dark); margin: 0;">Contexto y Desafío Rural</h3>
        </div>
        <p style="font-family: var(--font-sans); font-size: 24px; line-height: 1.45; color: var(--c-gray-text); margin: 0;">
          La brecha del <strong>58.6% sin internet</strong> y la urgencia de tutoría autónoma en USB sin requerir nube ni costo operativo.
        </p>
      </div>

      <!-- Cuadrante 02 -->
      <div style="background: #FAF5F5; border-top: 8px solid #8B263E; padding: 28px 32px;">
        <div style="display: flex; align-items: center; gap: 20px; margin-bottom: 12px;">
          <span style="font-family: var(--font-sans); font-size: 46px; font-weight: 800; color: #8B263E; line-height: 1;">02</span>
          <div style="width: 2px; height: 38px; background: var(--c-border-subtle);"></div>
          <h3 style="font-family: var(--font-sans); font-size: 28px; font-weight: 700; color: var(--c-text-dark); margin: 0;">Metodología y Pipeline RAG</h3>
        </div>
        <p style="font-family: var(--font-sans); font-size: 24px; line-height: 1.45; color: var(--c-gray-text); margin: 0;">
          Arquitectura en <strong>CPU estándar de aula (sin GPU)</strong>, banco curricular de <strong>14 preguntas</strong> y <strong>784 inferencias</strong> evaluadas.
        </p>
      </div>

      <!-- Cuadrante 03 -->
      <div style="background: #FAF5F5; border-top: 8px solid var(--c-red-accent); padding: 28px 32px;">
        <div style="display: flex; align-items: center; gap: 20px; margin-bottom: 12px;">
          <span style="font-family: var(--font-sans); font-size: 46px; font-weight: 800; color: var(--c-red-accent); line-height: 1;">03</span>
          <div style="width: 2px; height: 38px; background: var(--c-border-subtle);"></div>
          <h3 style="font-family: var(--font-sans); font-size: 28px; font-weight: 700; color: var(--c-text-dark); margin: 0;">Resultados y el Falso Empate</h3>
        </div>
        <p style="font-family: var(--font-sans); font-size: 24px; line-height: 1.45; color: var(--c-gray-text); margin: 0;">
          La ilusión del <strong>0.795</strong>, fallas asimétricas (<strong>alucinación vs. sobre-rechazo</strong>) y el choque con el criterio pedagógico docente.
        </p>
      </div>

      <!-- Cuadrante 04 -->
      <div style="background: #FAF5F5; border-top: 8px solid var(--c-gold); padding: 28px 32px;">
        <div style="display: flex; align-items: center; gap: 20px; margin-bottom: 12px;">
          <span style="font-family: var(--font-sans); font-size: 46px; font-weight: 800; color: #9A7200; line-height: 1;">04</span>
          <div style="width: 2px; height: 38px; background: var(--c-border-subtle);"></div>
          <h3 style="font-family: var(--font-sans); font-size: 28px; font-weight: 700; color: var(--c-text-dark); margin: 0;">Discusión y Conclusiones</h3>
        </div>
        <p style="font-family: var(--font-sans); font-size: 24px; line-height: 1.45; color: var(--c-gray-text); margin: 0;">
          <strong>Matriz de riesgo institucional</strong> para adopción de SLM y tres recomendaciones directas para llevar la IA al aula real.
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

# ==============================================================================
# OPCION C: ROADMAP HORIZONTAL EN 4 PASOS (FLUJO PROGRESIVO 01 -> 02 -> 03 -> 04)
# ==============================================================================
CONTENT_C = """
<section class="slide s-white active" id="slide-preview-3c">
  <header class="slide-header">
    <div class="sh-left">
      <span class="sh-red-bar"></span>
      <span class="sh-category">ESTRUCTURA DE LA PONENCIA</span>
    </div>
    <img src="assets/image6.png" alt="#LoxTIC" class="sh-loxtic">
  </header>
  <div class="sh-divider"></div>

  <div class="slide-content-area" style="justify-content: center; padding-top: 15px; padding-bottom: 20px;">
    <h2 class="s-lead-question" style="margin-bottom: 30px; font-size: 38px;">
      Cuatro momentos para desmontar la evaluación de la IA educativa local
    </h2>

    <div style="display: flex; gap: 24px; max-width: 1650px; align-items: stretch;">
      
      <!-- Paso 01 -->
      <div style="flex: 1; background: #FAF5F5; border-top: 8px solid var(--c-wine-primary); padding: 30px 24px; display: flex; flex-direction: column;">
        <div style="font-family: var(--font-sans); font-size: 52px; font-weight: 800; color: var(--c-wine-primary); line-height: 1; margin-bottom: 14px;">01</div>
        <h3 style="font-family: var(--font-sans); font-size: 26px; font-weight: 700; color: var(--c-text-dark); min-height: 64px; line-height: 1.25; margin-bottom: 14px;">
          Contexto y Desafío Rural
        </h3>
        <div style="width: 40px; height: 3px; background: var(--c-wine-primary); margin-bottom: 16px;"></div>
        <p style="font-family: var(--font-sans); font-size: 23px; line-height: 1.45; color: var(--c-gray-text); margin: 0;">
          Brecha de conectividad del <strong>58.6%</strong> y necesidad de tutoría en USB sin nube.
        </p>
      </div>

      <!-- Paso 02 -->
      <div style="flex: 1; background: #FAF5F5; border-top: 8px solid #8B263E; padding: 30px 24px; display: flex; flex-direction: column;">
        <div style="font-family: var(--font-sans); font-size: 52px; font-weight: 800; color: #8B263E; line-height: 1; margin-bottom: 14px;">02</div>
        <h3 style="font-family: var(--font-sans); font-size: 26px; font-weight: 700; color: var(--c-text-dark); min-height: 64px; line-height: 1.25; margin-bottom: 14px;">
          Metodología y Pipeline RAG
        </h3>
        <div style="width: 40px; height: 3px; background: #8B263E; margin-bottom: 16px;"></div>
        <p style="font-family: var(--font-sans); font-size: 23px; line-height: 1.45; color: var(--c-gray-text); margin: 0;">
          Ejecución en <strong>CPU de aula</strong>, banco de <strong>14 preguntas</strong> y <strong>784 inferencias</strong>.
        </p>
      </div>

      <!-- Paso 03 -->
      <div style="flex: 1; background: #FAF5F5; border-top: 8px solid var(--c-red-accent); padding: 30px 24px; display: flex; flex-direction: column;">
        <div style="font-family: var(--font-sans); font-size: 52px; font-weight: 800; color: var(--c-red-accent); line-height: 1; margin-bottom: 14px;">03</div>
        <h3 style="font-family: var(--font-sans); font-size: 26px; font-weight: 700; color: var(--c-text-dark); min-height: 64px; line-height: 1.25; margin-bottom: 14px;">
          Resultados y Falso Empate
        </h3>
        <div style="width: 40px; height: 3px; background: var(--c-red-accent); margin-bottom: 16px;"></div>
        <p style="font-family: var(--font-sans); font-size: 23px; line-height: 1.45; color: var(--c-gray-text); margin: 0;">
          Espejismo del <strong>0.795</strong>, fallas asimétricas y desacuerdo con el juicio docente.
        </p>
      </div>

      <!-- Paso 04 -->
      <div style="flex: 1; background: #FAF5F5; border-top: 8px solid var(--c-gold); padding: 30px 24px; display: flex; flex-direction: column;">
        <div style="font-family: var(--font-sans); font-size: 52px; font-weight: 800; color: #9A7200; line-height: 1; margin-bottom: 14px;">04</div>
        <h3 style="font-family: var(--font-sans); font-size: 26px; font-weight: 700; color: var(--c-text-dark); min-height: 64px; line-height: 1.25; margin-bottom: 14px;">
          Discusión y Conclusiones
        </h3>
        <div style="width: 40px; height: 3px; background: var(--c-gold); margin-bottom: 16px;"></div>
        <p style="font-family: var(--font-sans); font-size: 23px; line-height: 1.45; color: var(--c-gray-text); margin: 0;">
          <strong>Matriz de riesgo</strong> y directrices técnicas para llevar tutores offline al aula real.
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

options = [
    ("opcion_a", CONTENT_A, "slide_03_opcion_a.png"),
    ("opcion_b", CONTENT_B, "slide_03_opcion_b.png"),
    ("opcion_c", CONTENT_C, "slide_03_opcion_c.png"),
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

print("Todas las opciones de Slide 3 fueron generadas y capturadas con exito.")
