# -*- coding: utf-8 -*-
"""
Genera y captura 3 variantes refinadas de la Opción B para el Slide 5:
Eliminando "cuadros dentro de cuadros" y equilibrando los espacios vacíos.
"""
import os
from playwright.sync_api import sync_playwright

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ARTIFACT_DIR = r"C:\Users\ASUS\.gemini\antigravity-ide\brain\a6624504-511c-4b9d-bc9a-468e348bde40"
TEMP_HTML = os.path.join(ROOT_DIR, "temp_preview_s5_b.html")

BASE_TEMPLATE = """<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Preview Variantes B Slide 5</title>
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

# ==============================================================================
# VARIANTE B1: 3 COLUMNAS PURAS Y CONTINUAS (CERO CAJAS ANIDADAS, FLUJO ORGÁNICO)
# ==============================================================================
CONTENT_B1 = """
<section class="slide s-white active" id="slide-preview-5-b1">
  <header class="slide-header">
    <div class="sh-left">
      <span class="sh-red-bar"></span>
      <span class="sh-category">01 &middot; CONTEXTO Y PROBLEMA RURAL</span>
    </div>
    <img src="assets/image6.png" alt="#LoxTIC" class="sh-loxtic">
  </header>
  <div class="sh-divider"></div>

  <div class="slide-content-area" style="justify-content: flex-start; padding-top: 15px;">
    <h2 class="s-lead-question" style="font-size: 46px; font-weight: 800; margin-bottom: 30px; line-height: 1.2;">
      De la brecha de conectividad a las preguntas que guiaron el benchmark
    </h2>

    <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 32px; flex-grow: 1; align-items: stretch;">
      
      <!-- Columna 1: La Brecha -->
      <div style="background: var(--c-pink-bg); border-top: 8px solid var(--c-wine-primary); padding: 36px 32px; display: flex; flex-direction: column; justify-content: space-between;">
        <div>
          <div style="font-family: var(--font-mono); font-size: 19px; font-weight: 700; color: var(--c-wine-primary); letter-spacing: 2px; margin-bottom: 12px;">
            01 &middot; LA REALIDAD
          </div>
          <h3 style="font-family: var(--font-sans); font-size: 32px; font-weight: 700; color: var(--c-wine-dark); margin-bottom: 20px;">
            La Brecha Rural
          </h3>
          <div style="font-family: var(--font-sans); font-size: 64px; font-weight: 800; color: var(--c-wine-primary); line-height: 1; margin-bottom: 18px;">
            58.6%
          </div>
          <p style="font-family: var(--font-sans); font-size: 25px; color: var(--c-text-dark); line-height: 1.45; margin: 0;">
            Hogares rurales en Colombia <strong>sin acceso a internet</strong> (DANE 2024).
          </p>
        </div>

        <div style="padding-top: 24px; border-top: 2px solid var(--c-border-subtle);">
          <p style="font-family: var(--font-sans); font-size: 24px; color: var(--c-gray-text); line-height: 1.4; margin: 0;">
            Las APIs comerciales en la nube son inviables en el aula rural por costos y falta de red fija.
          </p>
        </div>
      </div>

      <!-- Columna 2: Pregunta 1 -->
      <div style="background: var(--c-pink-bg); border-top: 8px solid var(--c-red-accent); padding: 36px 32px; display: flex; flex-direction: column; justify-content: space-between;">
        <div>
          <div style="font-family: var(--font-mono); font-size: 19px; font-weight: 700; color: var(--c-red-accent); letter-spacing: 2px; margin-bottom: 12px;">
            02 &middot; PREGUNTA 1
          </div>
          <h3 style="font-family: var(--font-sans); font-size: 32px; font-weight: 700; color: var(--c-wine-dark); margin-bottom: 20px;">
            Elecci&oacute;n de Modelo
          </h3>
          <div style="font-family: var(--font-sans); font-size: 64px; font-weight: 800; color: var(--c-red-accent); line-height: 1; margin-bottom: 18px;">
            SLM
          </div>
          <p style="font-family: var(--font-sans); font-size: 25px; color: var(--c-text-dark); line-height: 1.45; margin: 0;">
            &iquest;Cu&aacute;l modelo compacto ofrece <strong>fluidez y rigor</strong> en una CPU escolar est&aacute;ndar?
          </p>
        </div>

        <div style="padding-top: 24px; border-top: 2px solid var(--c-border-subtle);">
          <p style="font-family: var(--font-sans); font-size: 24px; color: var(--c-gray-text); line-height: 1.4; margin: 0;">
            Operaci&oacute;n 100% aut&oacute;noma en equipos del aula, sin requerir inversi&oacute;n en servidores externos.
          </p>
        </div>
      </div>

      <!-- Columna 3: Pregunta 2 -->
      <div style="background: var(--c-pink-bg); border-top: 8px solid var(--c-gold); padding: 36px 32px; display: flex; flex-direction: column; justify-content: space-between;">
        <div>
          <div style="font-family: var(--font-mono); font-size: 19px; font-weight: 700; color: #9A7200; letter-spacing: 2px; margin-bottom: 12px;">
            03 &middot; PREGUNTA 2
          </div>
          <h3 style="font-family: var(--font-sans); font-size: 32px; font-weight: 700; color: var(--c-wine-dark); margin-bottom: 20px;">
            Auditor&iacute;a y Rigor
          </h3>
          <div style="font-family: var(--font-sans); font-size: 64px; font-weight: 800; color: #9A7200; line-height: 1; margin-bottom: 18px;">
            Offline
          </div>
          <p style="font-family: var(--font-sans); font-size: 25px; color: var(--c-text-dark); line-height: 1.45; margin: 0;">
            &iquest;C&oacute;mo evaluar la <strong>calidad pedag&oacute;gica</strong> sin evaluadores humanos en cada sesi&oacute;n?
          </p>
        </div>

        <div style="padding-top: 24px; border-top: 2px solid var(--c-border-subtle);">
          <p style="font-family: var(--font-sans); font-size: 24px; color: var(--c-gray-text); line-height: 1.4; margin: 0;">
            Un benchmark cuantitativo y reproducible para auditar alucinaciones antes del despliegue.
          </p>
        </div>
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

# ==============================================================================
# VARIANTE B2: 3 FILAS HORIZONTALES (ESTILO SLIDE 2 - AMPLITUD Y CONTINUIDAD)
# ==============================================================================
CONTENT_B2 = """
<section class="slide s-white active" id="slide-preview-5-b2">
  <header class="slide-header">
    <div class="sh-left">
      <span class="sh-red-bar"></span>
      <span class="sh-category">01 &middot; CONTEXTO Y PROBLEMA RURAL</span>
    </div>
    <img src="assets/image6.png" alt="#LoxTIC" class="sh-loxtic">
  </header>
  <div class="sh-divider"></div>

  <div class="slide-content-area" style="justify-content: center; padding-top: 15px; padding-bottom: 15px;">
    <h2 class="s-lead-question" style="font-size: 46px; font-weight: 800; margin-bottom: 26px; line-height: 1.2;">
      De la brecha de conectividad a las preguntas que guiaron el benchmark
    </h2>

    <div style="display: flex; flex-direction: column; gap: 20px;">
      
      <!-- Fila 1: La Brecha -->
      <div style="background-color: var(--c-pink-bg); border-left: 8px solid var(--c-wine-primary); padding: 22px 32px; display: flex; align-items: center; gap: 36px;">
        <div style="flex: 0 0 240px; width: 240px; text-align: center;">
          <div style="font-family: var(--font-sans); font-size: 64px; font-weight: 800; color: var(--c-wine-primary); line-height: 1;">
            58.6%
          </div>
          <div style="font-family: var(--font-mono); font-size: 18px; font-weight: 700; color: var(--c-gray-text); margin-top: 6px; letter-spacing: 1px;">
            DANE 2024
          </div>
        </div>
        <div style="width: 2px; height: 85px; background-color: var(--c-line-rule); opacity: 0.6; flex-shrink: 0;"></div>
        <div style="flex: 1;">
          <h3 style="font-family: var(--font-sans); font-size: 30px; font-weight: 700; color: var(--c-text-dark); margin-bottom: 8px;">
            La Brecha Rural de Conectividad
          </h3>
          <p style="font-family: var(--font-sans); font-size: 25px; color: var(--c-gray-text); line-height: 1.4; margin: 0;">
            M&aacute;s de la mitad de los hogares rurales en Colombia no tienen internet. <strong>Las APIs comerciales en la nube excluyen al aula rural</strong> por costos y falta de red fija.
          </p>
        </div>
      </div>

      <!-- Fila 2: Pregunta 1 -->
      <div style="background-color: var(--c-pink-bg); border-left: 8px solid var(--c-red-accent); padding: 22px 32px; display: flex; align-items: center; gap: 36px;">
        <div style="flex: 0 0 240px; width: 240px; text-align: center;">
          <div style="font-family: var(--font-sans); font-size: 64px; font-weight: 800; color: var(--c-red-accent); line-height: 1;">
            SLM
          </div>
          <div style="font-family: var(--font-mono); font-size: 18px; font-weight: 700; color: var(--c-red-accent); margin-top: 6px; letter-spacing: 1px;">
            PREGUNTA 1
          </div>
        </div>
        <div style="width: 2px; height: 85px; background-color: var(--c-line-rule); opacity: 0.6; flex-shrink: 0;"></div>
        <div style="flex: 1;">
          <h3 style="font-family: var(--font-sans); font-size: 30px; font-weight: 700; color: var(--c-text-dark); margin-bottom: 8px;">
            Selecci&oacute;n y Viabilidad de Hardware
          </h3>
          <p style="font-family: var(--font-sans); font-size: 25px; color: var(--c-gray-text); line-height: 1.4; margin: 0;">
            &iquest;Cu&aacute;l modelo compacto ofrece el mejor balance entre <strong>rigor conceptual y velocidad</strong> ejecut&aacute;ndose aut&oacute;nomo en la CPU est&aacute;ndar de la escuela?
          </p>
        </div>
      </div>

      <!-- Fila 3: Pregunta 2 -->
      <div style="background-color: var(--c-pink-bg); border-left: 8px solid var(--c-gold); padding: 22px 32px; display: flex; align-items: center; gap: 36px;">
        <div style="flex: 0 0 240px; width: 240px; text-align: center;">
          <div style="font-family: var(--font-sans); font-size: 64px; font-weight: 800; color: #9A7200; line-height: 1;">
            Offline
          </div>
          <div style="font-family: var(--font-mono); font-size: 18px; font-weight: 700; color: #9A7200; margin-top: 6px; letter-spacing: 1px;">
            PREGUNTA 2
          </div>
        </div>
        <div style="width: 2px; height: 85px; background-color: var(--c-line-rule); opacity: 0.6; flex-shrink: 0;"></div>
        <div style="flex: 1;">
          <h3 style="font-family: var(--font-sans); font-size: 30px; font-weight: 700; color: var(--c-text-dark); margin-bottom: 8px;">
            Auditor&iacute;a y Evaluaci&oacute;n de Calidad
          </h3>
          <p style="font-family: var(--font-sans); font-size: 25px; color: var(--c-gray-text); line-height: 1.4; margin: 0;">
            &iquest;C&oacute;mo calificar la <strong>calidad pedag&oacute;gica</strong> y detectar alucinaciones con rigor metodol&oacute;gico sin evaluadores humanos en cada sesi&oacute;n?
          </p>
        </div>
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

# ==============================================================================
# VARIANTE B3: 3 COLUMNAS INTEGRADAS CON GRAN PRESENCIA (BALANCE PERFECTO)
# ==============================================================================
CONTENT_B3 = """
<section class="slide s-white active" id="slide-preview-5-b3">
  <header class="slide-header">
    <div class="sh-left">
      <span class="sh-red-bar"></span>
      <span class="sh-category">01 &middot; CONTEXTO Y PROBLEMA RURAL</span>
    </div>
    <img src="assets/image6.png" alt="#LoxTIC" class="sh-loxtic">
  </header>
  <div class="sh-divider"></div>

  <div class="slide-content-area" style="justify-content: flex-start; padding-top: 15px;">
    <h2 class="s-lead-question" style="font-size: 46px; font-weight: 800; margin-bottom: 28px; line-height: 1.2;">
      De la brecha de conectividad a las preguntas que guiaron el benchmark
    </h2>

    <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 30px; flex-grow: 1; align-items: stretch;">
      
      <!-- Tarjeta 1: La Brecha -->
      <div style="background: var(--c-pink-bg); border-top: 8px solid var(--c-wine-primary); padding: 38px 34px; display: flex; flex-direction: column;">
        <div style="font-family: var(--font-mono); font-size: 19px; font-weight: 700; color: var(--c-wine-primary); letter-spacing: 2px; margin-bottom: 12px;">
          01 &middot; EL CONTEXTO
        </div>
        <h3 style="font-family: var(--font-sans); font-size: 32px; font-weight: 700; color: var(--c-wine-dark); margin-bottom: 24px;">
          Brecha Rural
        </h3>
        <div style="font-family: var(--font-sans); font-size: 68px; font-weight: 800; color: var(--c-wine-primary); line-height: 1; margin-bottom: 20px;">
          58.6%
        </div>
        <p style="font-family: var(--font-sans); font-size: 26px; color: var(--c-text-dark); line-height: 1.4; margin-bottom: 20px;">
          Hogares rurales en Colombia <strong>sin acceso a internet</strong> (DANE 2024).
        </p>
        <p style="font-family: var(--font-sans); font-size: 24px; color: var(--c-gray-text); line-height: 1.45; margin-top: auto;">
          La dependencia de la nube comercial excluye donde m&aacute;s se necesita tutor&iacute;a de ingl&eacute;s.
        </p>
      </div>

      <!-- Tarjeta 2: Pregunta 1 -->
      <div style="background: var(--c-pink-bg); border-top: 8px solid var(--c-red-accent); padding: 38px 34px; display: flex; flex-direction: column;">
        <div style="font-family: var(--font-mono); font-size: 19px; font-weight: 700; color: var(--c-red-accent); letter-spacing: 2px; margin-bottom: 12px;">
          02 &middot; PREGUNTA 1
        </div>
        <h3 style="font-family: var(--font-sans); font-size: 32px; font-weight: 700; color: var(--c-wine-dark); margin-bottom: 24px;">
          Elecci&oacute;n de Modelo
        </h3>
        <div style="font-family: var(--font-sans); font-size: 68px; font-weight: 800; color: var(--c-red-accent); line-height: 1; margin-bottom: 20px;">
          SLM
        </div>
        <p style="font-family: var(--font-sans); font-size: 26px; color: var(--c-text-dark); line-height: 1.4; margin-bottom: 20px;">
          &iquest;Cu&aacute;l modelo ofrece <strong>fluidez y precisi&oacute;n</strong> en una CPU escolar b&aacute;sica?
        </p>
        <p style="font-family: var(--font-sans); font-size: 24px; color: var(--c-gray-text); line-height: 1.45; margin-top: auto;">
          Modelos compactos (3B a 8B) capaces de operar en hardware existente sin inversi&oacute;n adicional.
        </p>
      </div>

      <!-- Tarjeta 3: Pregunta 2 -->
      <div style="background: var(--c-pink-bg); border-top: 8px solid var(--c-gold); padding: 38px 34px; display: flex; flex-direction: column;">
        <div style="font-family: var(--font-mono); font-size: 19px; font-weight: 700; color: #9A7200; letter-spacing: 2px; margin-bottom: 12px;">
          03 &middot; PREGUNTA 2
        </div>
        <h3 style="font-family: var(--font-sans); font-size: 32px; font-weight: 700; color: var(--c-wine-dark); margin-bottom: 24px;">
          Auditor&iacute;a de Calidad
        </h3>
        <div style="font-family: var(--font-sans); font-size: 68px; font-weight: 800; color: #9A7200; line-height: 1; margin-bottom: 20px;">
          Offline
        </div>
        <p style="font-family: var(--font-sans); font-size: 26px; color: var(--c-text-dark); line-height: 1.4; margin-bottom: 20px;">
          &iquest;C&oacute;mo auditar y calificar las respuestas <strong>sin depender de internet</strong>?
        </p>
        <p style="font-family: var(--font-sans); font-size: 24px; color: var(--c-gray-text); line-height: 1.45; margin-top: auto;">
          Un protocolo ciego y cuantitativo para verificar que el tutor no invente explicaciones err&oacute;neas.
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

OPTIONS = [
    ("slide_05_variante_b1.png", CONTENT_B1),
    ("slide_05_variante_b2.png", CONTENT_B2),
    ("slide_05_variante_b3.png", CONTENT_B3),
]

def generate_and_capture():
    print("Iniciando generación de capturas para variantes de Opción B (Slide 5)...")
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(viewport={"width": 1920, "height": 1080})

        for img_name, content in OPTIONS:
            full_html = BASE_TEMPLATE.format(SLIDE_CONTENT=content)
            with open(TEMP_HTML, "w", encoding="utf-8") as f:
                f.write(full_html)

            page.goto("http://localhost:8085/temp_preview_s5_b.html", wait_until="networkidle")
            page.wait_for_timeout(600)

            out_path_root = os.path.join(ROOT_DIR, img_name)
            out_path_artifact = os.path.join(ARTIFACT_DIR, img_name)

            page.screenshot(path=out_path_root)
            page.screenshot(path=out_path_artifact)
            print(f"-> Captura guardada: {img_name}")

        browser.close()

    if os.path.exists(TEMP_HTML):
        os.remove(TEMP_HTML)
    print("Completado.")

if __name__ == "__main__":
    generate_and_capture()
