# -*- coding: utf-8 -*-
"""
Genera y captura las 3 opciones de diseño para Slide 2
para que el usuario pueda compararlas visualmente.
"""
import os
from playwright.sync_api import sync_playwright

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ARTIFACT_DIR = r"C:\Users\ASUS\.gemini\antigravity-ide\brain\a6624504-511c-4b9d-bc9a-468e348bde40"
TEMP_HTML = os.path.join(ROOT_DIR, "temp_preview.html")

BASE_TEMPLATE = """<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Preview Opciones Slide 2</title>
  <link rel="stylesheet" href="styles.css?v=99">
</head>
<body>
  <main id="presentation-viewport">
    <div id="slides-stage">
      {SLIDE_CONTENT}
    </div>
  </main>
  <script src="app.js?v=99"></script>
</body>
</html>"""

# ==============================================================================
# OPCIÓN A: TRÍPTICO EN 3 COLUMNAS HORIZONTALES
# ==============================================================================
CONTENT_A = """
<section class="slide s-white active" id="slide-preview-a">
  <header class="slide-header">
    <div class="sh-left">
      <span class="sh-red-bar"></span>
      <span class="sh-category">RESUMEN EJECUTIVO</span>
    </div>
    <img src="assets/image6.png" alt="#LoxTIC" class="sh-loxtic">
  </header>
  <div class="sh-divider"></div>

  <div class="slide-content-area" style="justify-content: center; padding-top: 15px; padding-bottom: 15px;">
    <h2 class="s-lead-question" style="margin-bottom: 24px; font-size: 38px;">
      ¿Puede existir tutoría con Inteligencia Artificial donde ni siquiera llega internet?
    </h2>

    <div class="s6-blocks-row" style="margin-top: 0; margin-bottom: 20px; gap: 32px; align-items: stretch; flex-grow: 1;">
      
      <!-- Columna 1 -->
      <div class="s6-block s6-block-wine" style="padding: 28px 28px; display: flex; flex-direction: column; justify-content: space-between;">
        <div>
          <div class="s6-block-tag">01 &middot; EL PROBLEMA</div>
          <h3 class="s6-block-title" style="font-size: 32px; margin-bottom: 16px;">Brecha y Exclusión</h3>
          
          <div class="metric-box-large" style="margin-bottom: 20px;">
            <span class="metric-digit-huge" style="font-size: 56px;">58.6%</span>
            <span class="metric-unit-sub" style="font-size: 20px; line-height: 1.3;">Hogares rurales en Colombia sin acceso a internet (DANE)</span>
          </div>

          <p style="font-family: var(--font-sans); font-size: 23px; line-height: 1.45; color: var(--c-gray-text); margin: 0;">
            Los tutores comerciales de IA exigen conectividad continua y suscripciones en dólares, dejando fuera a las aulas donde más se necesita el refuerzo educativo.
          </p>
        </div>

        <div style="border-top: 1px solid var(--c-border-subtle); padding-top: 14px; margin-top: 20px; font-family: var(--font-sans); font-size: 21px; font-weight: 700; color: var(--c-wine-primary);">
          Desafío: Inaccesibilidad rural
        </div>
      </div>

      <!-- Columna 2 -->
      <div class="s6-block s6-block-red" style="padding: 28px 28px; display: flex; flex-direction: column; justify-content: space-between;">
        <div>
          <div class="s6-block-tag" style="color: var(--c-red-accent);">02 &middot; LA PROPUESTA</div>
          <h3 class="s6-block-title" style="font-size: 32px; margin-bottom: 16px;">Tutor Offline en USB</h3>
          
          <div class="metric-box-large" style="margin-bottom: 20px;">
            <span class="metric-digit-huge highlight-red" style="font-size: 56px;">100%</span>
            <span class="metric-unit-sub" style="font-size: 20px; line-height: 1.3;">Offline &middot; Inferencia en PC escolar común sin GPU</span>
          </div>

          <p style="font-family: var(--font-sans); font-size: 23px; line-height: 1.45; color: var(--c-gray-text); margin: 0;">
            Arquitectura RAG con modelos compactos (Phi-4-mini y Qwen2.5-3B) cuantizados a 4 bits, ejecutados directamente desde una memoria USB a 1.9 tokens/s.
          </p>
        </div>

        <div style="border-top: 1px solid var(--c-border-subtle); padding-top: 14px; margin-top: 20px; font-family: var(--font-sans); font-size: 21px; font-weight: 700; color: var(--c-red-accent);">
          Solución: Autonomía y costo cero
        </div>
      </div>

      <!-- Columna 3 -->
      <div class="s6-block s6-block-gold" style="padding: 28px 28px; display: flex; flex-direction: column; justify-content: space-between;">
        <div>
          <div class="s6-block-tag" style="color: #9A7200;">03 &middot; EL HALLAZGO</div>
          <h3 class="s6-block-title" style="font-size: 32px; margin-bottom: 16px;">El Falso Empate</h3>
          
          <div class="metric-box-large" style="margin-bottom: 20px;">
            <span class="metric-digit-huge" style="font-size: 56px; color: #9A7200;">0.795</span>
            <span class="metric-unit-sub" style="font-size: 20px; line-height: 1.3;">Misma nota automática pero conductas opuestas</span>
          </div>

          <p style="font-family: var(--font-sans); font-size: 23px; line-height: 1.45; color: var(--c-gray-text); margin: 0;">
            La métrica oculta que Phi-4 alucina y Qwen sobre-rechaza; los docentes discrepan (&kappa; = -0.429), demostrando que el índice premia texto, no pedagogía.
          </p>
        </div>

        <div style="border-top: 1px solid var(--c-border-subtle); padding-top: 14px; margin-top: 20px; font-family: var(--font-sans); font-size: 21px; font-weight: 700; color: #9A7200;">
          Veredicto: Métrica ciega a la calidad
        </div>
      </div>

    </div>

    <!-- Fila inferior -->
    <div style="font-family: var(--font-sans); font-size: 22px; color: var(--c-gray-text); border-top: 1.5px solid var(--c-border-subtle); padding-top: 12px; display: flex; justify-content: space-between; align-items: center; flex-shrink: 0;">
      <span><strong style="color: var(--c-wine-primary);">Propósito de la ponencia:</strong> Demostrar la viabilidad del tutor offline y exponer los sesgos de la evaluación algorítmica antes de llevar la IA al aula.</span>
      <span style="color: var(--c-gray-muted); font-size: 20px;">LHXT26 &middot; CARTAGENA 2026</span>
    </div>
  </div>

  <div class="slide-footer-rule"></div>
  <footer class="slide-footer">
    <span class="sf-left">VI CONGRESO CARTAGENA · 2026</span>
    <span class="sf-right">OPCIÓN A: TRÍPTICO EN 3 COLUMNAS</span>
  </footer>
</section>
"""

# ==============================================================================
# OPCIÓN B: FILAS EDITORIALES CON BARRAS LATERALES Y SEPARADORES
# ==============================================================================
CONTENT_B = """
<section class="slide s-white active" id="slide-preview-b">
  <header class="slide-header">
    <div class="sh-left">
      <span class="sh-red-bar"></span>
      <span class="sh-category">RESUMEN EJECUTIVO</span>
    </div>
    <img src="assets/image6.png" alt="#LoxTIC" class="sh-loxtic">
  </header>
  <div class="sh-divider"></div>

  <div class="slide-content-area" style="justify-content: center; padding-top: 15px; padding-bottom: 20px;">
    <h2 class="s-lead-question" style="margin-bottom: 30px; font-size: 38px;">
      ¿Puede existir tutoría con Inteligencia Artificial donde ni siquiera llega internet?
    </h2>

    <div style="display: flex; flex-direction: column; gap: 24px; max-width: 1650px;">
      
      <!-- Fila 1: Problema -->
      <div style="display: flex; align-items: center; gap: 36px; padding: 18px 24px; background: #FAF5F5; border-left: 6px solid var(--c-wine-primary);">
        <div style="min-width: 170px;">
          <div style="font-family: var(--font-mono); font-size: 20px; font-weight: 700; color: var(--c-wine-primary); letter-spacing: 1.5px;">01 &middot; PROBLEMA</div>
          <div style="font-family: var(--font-sans); font-size: 50px; font-weight: 700; color: var(--c-text-dark); line-height: 1;">58.6%</div>
          <div style="font-family: var(--font-sans); font-size: 17px; color: var(--c-gray-muted);">Desconexión rural</div>
        </div>
        <div style="width: 1.5px; height: 75px; background: var(--c-border-subtle);"></div>
        <div style="flex: 1;">
          <h3 style="font-family: var(--font-sans); font-size: 28px; font-weight: 700; color: var(--c-text-dark); margin-bottom: 6px;">Exclusión por Dependencia de Nube</h3>
          <p style="font-family: var(--font-sans); font-size: 23px; line-height: 1.4; color: var(--c-gray-text); margin: 0;">
            Los tutores comerciales de IA exigen internet de alta velocidad y pagos recurrentes en dólares, marginando a más de la mitad de las escuelas del país.
          </p>
        </div>
      </div>

      <!-- Fila 2: Propuesta -->
      <div style="display: flex; align-items: center; gap: 36px; padding: 18px 24px; background: #FAF5F5; border-left: 6px solid var(--c-red-accent);">
        <div style="min-width: 170px;">
          <div style="font-family: var(--font-mono); font-size: 20px; font-weight: 700; color: var(--c-red-accent); letter-spacing: 1.5px;">02 &middot; PROPUESTA</div>
          <div style="font-family: var(--font-sans); font-size: 50px; font-weight: 700; color: var(--c-red-accent); line-height: 1;">100%</div>
          <div style="font-family: var(--font-sans); font-size: 17px; color: var(--c-gray-muted);">Offline en USB</div>
        </div>
        <div style="width: 1.5px; height: 75px; background: var(--c-border-subtle);"></div>
        <div style="flex: 1;">
          <h3 style="font-family: var(--font-sans); font-size: 28px; font-weight: 700; color: var(--c-text-dark); margin-bottom: 6px;">Tutor RAG Portátil en Computador Escolar</h3>
          <p style="font-family: var(--font-sans); font-size: 23px; line-height: 1.4; color: var(--c-gray-text); margin: 0;">
            Modelos compactos (Phi-4-mini y Qwen2.5-3B) cuantizados a 4 bits, ejecutados de forma nativa en CPU Intel Core i5 común (sin GPU) a 1.9 tokens/s.
          </p>
        </div>
      </div>

      <!-- Fila 3: Hallazgo -->
      <div style="display: flex; align-items: center; gap: 36px; padding: 18px 24px; background: #FAF5F5; border-left: 6px solid var(--c-gold);">
        <div style="min-width: 170px;">
          <div style="font-family: var(--font-mono); font-size: 20px; font-weight: 700; color: #9A7200; letter-spacing: 1.5px;">03 &middot; HALLAZGO</div>
          <div style="font-family: var(--font-sans); font-size: 50px; font-weight: 700; color: #9A7200; line-height: 1;">0.795</div>
          <div style="font-family: var(--font-sans); font-size: 17px; color: var(--c-gray-muted);">Falso empate</div>
        </div>
        <div style="width: 1.5px; height: 75px; background: var(--c-border-subtle);"></div>
        <div style="flex: 1;">
          <h3 style="font-family: var(--font-sans); font-size: 28px; font-weight: 700; color: var(--c-text-dark); margin-bottom: 6px;">Falso Empate y Desacuerdo Docente (&kappa; = -0.429)</h3>
          <p style="font-family: var(--font-sans); font-size: 23px; line-height: 1.4; color: var(--c-gray-text); margin: 0;">
            La métrica automática oculta que Phi-4 alucina y Qwen bloquea; los profesores discrepan fuertemente, evidenciando que el índice premia texto, no pedagogía.
          </p>
        </div>
      </div>

    </div>

    <!-- Fila inferior -->
    <div style="font-family: var(--font-sans); font-size: 22px; color: var(--c-gray-text); border-top: 1.5px solid var(--c-border-subtle); padding-top: 14px; margin-top: 25px; display: flex; justify-content: space-between; align-items: center;">
      <span><strong style="color: var(--c-wine-primary);">Propósito de la ponencia:</strong> Demostrar la viabilidad del tutor offline y exponer los sesgos de la evaluación algorítmica antes de llevar la IA al aula.</span>
      <span style="color: var(--c-gray-muted); font-size: 20px;">LHXT26 &middot; CARTAGENA 2026</span>
    </div>
  </div>

  <div class="slide-footer-rule"></div>
  <footer class="slide-footer">
    <span class="sf-left">VI CONGRESO CARTAGENA · 2026</span>
    <span class="sf-right">OPCIÓN B: FILAS EDITORIALES CON BARRAS LATERALES</span>
  </footer>
</section>
"""

# ==============================================================================
# OPCIÓN C: FLUJO NARRATIVO ESCALONADO (ESCALERA CAUSA-EFECTO)
# ==============================================================================
CONTENT_C = """
<section class="slide s-white active" id="slide-preview-c">
  <header class="slide-header">
    <div class="sh-left">
      <span class="sh-red-bar"></span>
      <span class="sh-category">RESUMEN EJECUTIVO</span>
    </div>
    <img src="assets/image6.png" alt="#LoxTIC" class="sh-loxtic">
  </header>
  <div class="sh-divider"></div>

  <div class="slide-content-area" style="justify-content: center; padding-top: 10px; padding-bottom: 15px;">
    <h2 class="s-lead-question" style="margin-bottom: 24px; font-size: 38px;">
      ¿Puede existir tutoría con Inteligencia Artificial donde ni siquiera llega internet?
    </h2>

    <!-- Escalera de 3 Fases en Cascada -->
    <div style="display: flex; flex-direction: column; gap: 16px; max-width: 1650px; position: relative;">
      
      <!-- Paso 1: Arriba Izquierda -->
      <div style="width: 72%; padding: 20px 28px; background: #FAF5F5; border-top: 5px solid var(--c-wine-primary); display: flex; align-items: center; justify-content: space-between;">
        <div style="display: flex; align-items: center; gap: 20px;">
          <span style="font-family: var(--font-mono); font-size: 26px; font-weight: 700; color: var(--c-wine-primary);">PASO 01</span>
          <div>
            <div style="font-family: var(--font-sans); font-size: 28px; font-weight: 700; color: var(--c-text-dark);">El Punto de Partida: La Brecha Rural</div>
            <div style="font-family: var(--font-sans); font-size: 22px; color: var(--c-gray-text);">El 58.6% de hogares rurales colombianos no tiene conectividad para usar IA en la nube.</div>
          </div>
        </div>
        <div style="font-family: var(--font-sans); font-size: 44px; font-weight: 700; color: var(--c-wine-primary); margin-left: 20px;">58.6%</div>
      </div>

      <!-- Conector 1 -->
      <div style="margin-left: 18%; font-family: var(--font-mono); font-size: 20px; font-weight: 700; color: var(--c-red-accent); display: flex; align-items: center; gap: 10px;">
        <span>&#8628; RESPUESTA EXPERIMENTAL</span>
      </div>

      <!-- Paso 2: Centro -->
      <div style="width: 72%; margin-left: 14%; padding: 20px 28px; background: #FAF5F5; border-top: 5px solid var(--c-red-accent); display: flex; align-items: center; justify-content: space-between;">
        <div style="display: flex; align-items: center; gap: 20px;">
          <span style="font-family: var(--font-mono); font-size: 26px; font-weight: 700; color: var(--c-red-accent);">PASO 02</span>
          <div>
            <div style="font-family: var(--font-sans); font-size: 28px; font-weight: 700; color: var(--c-text-dark);">La Intervención: Tutor RAG Offline en USB</div>
            <div style="font-family: var(--font-sans); font-size: 22px; color: var(--c-gray-text);">Modelos compactos cuantizados (Phi-4 y Qwen2.5) en CPU escolar común a 1.9 t/s.</div>
          </div>
        </div>
        <div style="font-family: var(--font-sans); font-size: 44px; font-weight: 700; color: var(--c-red-accent); margin-left: 20px;">100%</div>
      </div>

      <!-- Conector 2 -->
      <div style="margin-left: 45%; font-family: var(--font-mono); font-size: 20px; font-weight: 700; color: #9A7200; display: flex; align-items: center; gap: 10px;">
        <span>&#8628; REVELACIÓN CRÍTICA</span>
      </div>

      <!-- Paso 3: Abajo Derecha -->
      <div style="width: 72%; margin-left: 28%; padding: 20px 28px; background: #FAF5F5; border-top: 5px solid var(--c-gold); display: flex; align-items: center; justify-content: space-between;">
        <div style="display: flex; align-items: center; gap: 20px;">
          <span style="font-family: var(--font-mono); font-size: 26px; font-weight: 700; color: #9A7200);">PASO 03</span>
          <div>
            <div style="font-family: var(--font-sans); font-size: 28px; font-weight: 700; color: var(--c-text-dark);">El Hallazgo: El Falso Empate Estadístico</div>
            <div style="font-family: var(--font-sans); font-size: 22px; color: var(--c-gray-text);">Empatan en 0.795 pero fallan de forma opuesta y los docentes discrepan (&kappa; = -0.429).</div>
          </div>
        </div>
        <div style="font-family: var(--font-sans); font-size: 44px; font-weight: 700; color: #9A7200; margin-left: 20px;">0.795</div>
      </div>

    </div>

    <!-- Fila inferior -->
    <div style="font-family: var(--font-sans); font-size: 22px; color: var(--c-gray-text); border-top: 1.5px solid var(--c-border-subtle); padding-top: 12px; margin-top: 18px; display: flex; justify-content: space-between; align-items: center;">
      <span><strong style="color: var(--c-wine-primary);">Propósito de la ponencia:</strong> Demostrar la viabilidad del tutor offline y exponer los sesgos de la evaluación algorítmica antes de llevar la IA al aula.</span>
      <span style="color: var(--c-gray-muted); font-size: 20px;">LHXT26 &middot; CARTAGENA 2026</span>
    </div>
  </div>

  <div class="slide-footer-rule"></div>
  <footer class="slide-footer">
    <span class="sf-left">VI CONGRESO CARTAGENA · 2026</span>
    <span class="sf-right">OPCIÓN C: FLUJO NARRATIVO ESCALONADO</span>
  </footer>
</section>
"""

options = [
    ("opcion_a.png", CONTENT_A),
    ("opcion_b.png", CONTENT_B),
    ("opcion_c.png", CONTENT_C),
]

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page(viewport={"width": 1920, "height": 1080})

    for img_name, content in options:
        full_html = BASE_TEMPLATE.replace("{SLIDE_CONTENT}", content)
        with open(TEMP_HTML, "w", encoding="utf-8") as f:
            f.write(full_html)
        
        # Load the temp file directly in playwright
        file_url = f"file:///{TEMP_HTML.replace(os.sep, '/')}"
        page.goto(file_url)
        page.wait_for_load_state("networkidle")
        page.wait_for_timeout(400)
        
        out_path = os.path.join(ARTIFACT_DIR, img_name)
        page.screenshot(path=out_path)
        print(f"Generada: {out_path}")

    browser.close()

if os.path.exists(TEMP_HTML):
    os.remove(TEMP_HTML)

print("Todas las opciones generadas con exito!")
