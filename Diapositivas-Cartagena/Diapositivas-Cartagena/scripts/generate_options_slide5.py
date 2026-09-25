# -*- coding: utf-8 -*-
"""
Genera y captura las 3 opciones de diseno para el Slide 5 (01 · Contexto y Problema Rural)
para que el usuario pueda compararlas visualmente.
"""
import os
from playwright.sync_api import sync_playwright

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ARTIFACT_DIR = r"C:\Users\ASUS\.gemini\antigravity-ide\brain\a6624504-511c-4b9d-bc9a-468e348bde40"
TEMP_HTML = os.path.join(ROOT_DIR, "temp_preview_s5.html")

BASE_TEMPLATE = """<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Preview Opciones Slide 5</title>
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
# OPCION A: DOS COLUMNAS EDITORIALES EQUILIBRADAS (REALIDAD VS PREGUNTAS)
# ==============================================================================
CONTENT_A = """
<section class="slide s-white active" id="slide-preview-5a">
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
      El dilema de la IA educativa: alta dependencia de la nube en escuelas sin internet
    </h2>

    <div style="display: grid; grid-template-columns: 1fr 1.15fr; gap: 36px; flex-grow: 1; align-items: stretch;">
      
      <!-- Columna Izquierda: La Realidad de la Brecha -->
      <div style="background: var(--c-pink-bg); border-top: 6px solid var(--c-wine-primary); padding: 32px 36px; display: flex; flex-direction: column; justify-content: space-between;">
        <div>
          <div style="font-family: var(--font-mono); font-size: 20px; font-weight: 700; color: var(--c-wine-primary); letter-spacing: 2px; margin-bottom: 12px;">
            01 &middot; REALIDAD DE CONECTIVIDAD
          </div>
          <h3 style="font-family: var(--font-sans); font-size: 32px; font-weight: 700; color: var(--c-wine-dark); margin-bottom: 24px;">
            La Brecha Rural
          </h3>

          <div style="display: flex; flex-direction: column; gap: 24px;">
            <!-- Metrica 1 -->
            <div style="display: flex; gap: 20px; align-items: flex-start;">
              <div style="width: 5px; height: 75px; background: var(--c-red-accent); flex-shrink: 0;"></div>
              <div>
                <div style="font-family: var(--font-sans); font-size: 58px; font-weight: 800; color: var(--c-red-accent); line-height: 1;">58.6%</div>
                <div style="font-family: var(--font-sans); font-size: 24px; color: var(--c-text-dark); margin-top: 6px; line-height: 1.3;">
                  Hogares rurales en Colombia <strong>sin acceso a internet</strong> (DANE 2024).
                </div>
              </div>
            </div>

            <!-- Metrica 2 -->
            <div style="display: flex; gap: 20px; align-items: flex-start;">
              <div style="width: 5px; height: 75px; background: var(--c-wine-primary); flex-shrink: 0;"></div>
              <div>
                <div style="font-family: var(--font-sans); font-size: 58px; font-weight: 800; color: var(--c-wine-primary); line-height: 1;">33.0%</div>
                <div style="font-family: var(--font-sans); font-size: 24px; color: var(--c-text-dark); margin-top: 6px; line-height: 1.3;">
                  Poblaci&oacute;n mundial completamente <strong>desconectada</strong> (ITU 2023).
                </div>
              </div>
            </div>
          </div>
        </div>

        <!-- Consecuencia pedagogica -->
        <div style="background: #FFFFFF; border-left: 5px solid var(--c-wine-primary); padding: 18px 20px; margin-top: 20px;">
          <div style="font-family: var(--font-sans); font-size: 24px; color: var(--c-gray-text); line-height: 1.4;">
            Las APIs comerciales en la nube exigen internet veloz y pagos recurrentes en d&oacute;lares, excluyendo al aula rural.
          </div>
        </div>
      </div>

      <!-- Columna Derecha: Las Dos Preguntas de Investigacion -->
      <div style="background: var(--c-pink-bg); border-top: 6px solid var(--c-red-accent); padding: 32px 36px; display: flex; flex-direction: column; justify-content: space-between;">
        <div>
          <div style="font-family: var(--font-mono); font-size: 20px; font-weight: 700; color: var(--c-red-accent); letter-spacing: 2px; margin-bottom: 12px;">
            FORMULACI&Oacute;N DEL PROBLEMA
          </div>
          <h3 style="font-family: var(--font-sans); font-size: 32px; font-weight: 700; color: var(--c-wine-dark); margin-bottom: 24px;">
            Dos Preguntas de Investigaci&oacute;n
          </h3>

          <!-- Pregunta 1 -->
          <div style="margin-bottom: 24px;">
            <div style="display: flex; align-items: center; gap: 12px; margin-bottom: 8px;">
              <span style="font-family: var(--font-mono); font-size: 24px; font-weight: 700; color: var(--c-wine-primary);">01.</span>
              <span style="font-family: var(--font-sans); font-size: 26px; font-weight: 700; color: var(--c-wine-primary);">Selecci&oacute;n de Modelo Compacto</span>
            </div>
            <p style="font-family: var(--font-sans); font-size: 24px; color: var(--c-text-dark); line-height: 1.4; margin: 0; padding-left: 36px;">
              &iquest;Cu&aacute;l modelo (SLM) ofrece el mejor balance entre rigor conceptual y velocidad en la CPU est&aacute;ndar de una escuela?
            </p>
          </div>

          <!-- Pregunta 2 -->
          <div>
            <div style="display: flex; align-items: center; gap: 12px; margin-bottom: 8px;">
              <span style="font-family: var(--font-mono); font-size: 24px; font-weight: 700; color: var(--c-red-accent);">02.</span>
              <span style="font-family: var(--font-sans); font-size: 26px; font-weight: 700; color: var(--c-red-accent);">Control y Evaluaci&oacute;n de Calidad</span>
            </div>
            <p style="font-family: var(--font-sans); font-size: 24px; color: var(--c-text-dark); line-height: 1.4; margin: 0; padding-left: 36px;">
              &iquest;C&oacute;mo auditar y calificar las respuestas pedag&oacute;gicas con rigor metodol&oacute;gico y sin depender de internet?
            </p>
          </div>
        </div>

        <!-- Meta de investigacion -->
        <div style="background: #FFFFFF; border-left: 5px solid var(--c-red-accent); padding: 18px 20px; margin-top: 20px;">
          <div style="font-family: var(--font-sans); font-size: 24px; color: var(--c-text-dark); line-height: 1.4;">
            <strong>Meta:</strong> Establecer un protocolo de evaluaci&oacute;n offline reproducible, ciego y con criterio pedag&oacute;gico.
          </div>
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
# OPCION B: TRÍPTICO DE 3 PANELES (CONTEXTO -> PREGUNTA 1 -> PREGUNTA 2)
# ==============================================================================
CONTENT_B = """
<section class="slide s-white active" id="slide-preview-5b">
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

    <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 28px; flex-grow: 1; align-items: stretch; margin-bottom: 20px;">
      
      <!-- Panel 1: Contexto Rural -->
      <div style="background: var(--c-pink-bg); border-top: 6px solid var(--c-wine-primary); padding: 28px 30px; display: flex; flex-direction: column; justify-content: space-between;">
        <div>
          <div style="font-family: var(--font-mono); font-size: 18px; font-weight: 700; color: var(--c-wine-primary); letter-spacing: 2px; margin-bottom: 10px;">
            01 &middot; LA REALIDAD
          </div>
          <h3 style="font-family: var(--font-sans); font-size: 28px; font-weight: 700; color: var(--c-wine-dark); margin-bottom: 18px;">
            Brecha Rural
          </h3>
          <div style="font-family: var(--font-sans); font-size: 58px; font-weight: 800; color: var(--c-wine-primary); line-height: 1; margin-bottom: 14px;">
            58.6%
          </div>
          <p style="font-family: var(--font-sans); font-size: 24px; color: var(--c-text-dark); line-height: 1.4; margin-bottom: 12px;">
            Hogares rurales en Colombia sin internet (DANE 2024).
          </p>
        </div>
        <div style="background: #FFFFFF; border-left: 4px solid var(--c-wine-primary); padding: 14px; font-family: var(--font-sans); font-size: 22px; color: var(--c-gray-text); line-height: 1.35;">
          Las APIs en la nube no son una opci&oacute;n factible para la escuela rural.
        </div>
      </div>

      <!-- Panel 2: Pregunta 1 -->
      <div style="background: var(--c-pink-bg); border-top: 6px solid var(--c-red-accent); padding: 28px 30px; display: flex; flex-direction: column; justify-content: space-between;">
        <div>
          <div style="font-family: var(--font-mono); font-size: 18px; font-weight: 700; color: var(--c-red-accent); letter-spacing: 2px; margin-bottom: 10px;">
            02 &middot; PREGUNTA 1
          </div>
          <h3 style="font-family: var(--font-sans); font-size: 28px; font-weight: 700; color: var(--c-wine-dark); margin-bottom: 18px;">
            Elecci&oacute;n de Modelo
          </h3>
          <div style="font-family: var(--font-sans); font-size: 58px; font-weight: 800; color: var(--c-red-accent); line-height: 1; margin-bottom: 14px;">
            SLM
          </div>
          <p style="font-family: var(--font-sans); font-size: 24px; color: var(--c-text-dark); line-height: 1.4; margin-bottom: 12px;">
            &iquest;Cu&aacute;l modelo compacto ofrece precisi&oacute;n y fluidez razonable en CPU escolar?
          </p>
        </div>
        <div style="background: #FFFFFF; border-left: 4px solid var(--c-red-accent); padding: 14px; font-family: var(--font-sans); font-size: 22px; color: var(--c-gray-text); line-height: 1.35;">
          Correr localmente en hardware existente sin inversi&oacute;n en servidores.
        </div>
      </div>

      <!-- Panel 3: Pregunta 2 -->
      <div style="background: var(--c-pink-bg); border-top: 6px solid var(--c-gold); padding: 28px 30px; display: flex; flex-direction: column; justify-content: space-between;">
        <div>
          <div style="font-family: var(--font-mono); font-size: 18px; font-weight: 700; color: #9A7200; letter-spacing: 2px; margin-bottom: 10px;">
            03 &middot; PREGUNTA 2
          </div>
          <h3 style="font-family: var(--font-sans); font-size: 28px; font-weight: 700; color: var(--c-wine-dark); margin-bottom: 18px;">
            Evaluaci&oacute;n Rigurosa
          </h3>
          <div style="font-family: var(--font-sans); font-size: 58px; font-weight: 800; color: #9A7200; line-height: 1; margin-bottom: 14px;">
            Offline
          </div>
          <p style="font-family: var(--font-sans); font-size: 24px; color: var(--c-text-dark); line-height: 1.4; margin-bottom: 12px;">
            &iquest;C&oacute;mo auditar si el modelo inventa respuestas antes de llevarlo a estudiantes?
          </p>
        </div>
        <div style="background: #FFFFFF; border-left: 4px solid var(--c-gold); padding: 14px; font-family: var(--font-sans); font-size: 22px; color: var(--c-gray-text); line-height: 1.35;">
          Evaluar con rigor cient&iacute;fico sin evaluadores humanos en cada sesi&oacute;n.
        </div>
      </div>

    </div>

    <!-- Barra Inferior de Proposito -->
    <div style="background: #FAF5F5; border-left: 6px solid var(--c-wine-primary); padding: 14px 24px; display: flex; align-items: center; justify-content: space-between;">
      <span style="font-family: var(--font-sans); font-size: 24px; color: var(--c-text-dark);">
        <strong>Prop&oacute;sito de la investigaci&oacute;n:</strong> Establecer un benchmark ciego y reproducible para validar tutores locales de ingl&eacute;s.
      </span>
      <span style="font-family: var(--font-mono); font-size: 20px; font-weight: 700; color: var(--c-wine-primary); letter-spacing: 1px;">
        BENCHMARK LOCAL
      </span>
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
# OPCION C: CONTRASTE HORIZONTAL (DATOS CLAVE IZQ + 2 FICHAS DE PREGUNTAS DER)
# ==============================================================================
CONTENT_C = """
<section class="slide s-white active" id="slide-preview-5c">
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
      &iquest;C&oacute;mo implementar tutor&iacute;a con IA donde no hay conexi&oacute;n a internet?
    </h2>

    <div style="display: grid; grid-template-columns: 0.95fr 1.25fr; gap: 36px; flex-grow: 1; align-items: stretch;">
      
      <!-- Columna Izquierda: Tarjeta de Contexto con Datos de Gran Escala -->
      <div style="background: #FAF5F5; border-left: 8px solid var(--c-wine-primary); padding: 34px 36px; display: flex; flex-direction: column; justify-content: space-between;">
        <div>
          <div style="font-family: var(--font-mono); font-size: 20px; font-weight: 700; color: var(--c-wine-primary); letter-spacing: 2px; margin-bottom: 12px;">
            EL ESCENARIO REAL
          </div>
          <h3 style="font-family: var(--font-sans); font-size: 32px; font-weight: 700; color: var(--c-wine-dark); margin-bottom: 26px;">
            La Brecha Rural
          </h3>

          <div style="margin-bottom: 24px;">
            <div style="font-family: var(--font-sans); font-size: 64px; font-weight: 800; color: var(--c-red-accent); line-height: 1;">
              58.6%
            </div>
            <div style="font-family: var(--font-sans); font-size: 24px; color: var(--c-text-dark); margin-top: 6px; line-height: 1.35;">
              Hogares rurales en Colombia <strong>sin acceso a internet</strong> (DANE 2024).
            </div>
          </div>

          <div>
            <div style="font-family: var(--font-sans); font-size: 48px; font-weight: 800; color: var(--c-wine-primary); line-height: 1;">
              33.0%
            </div>
            <div style="font-family: var(--font-sans); font-size: 24px; color: var(--c-text-dark); margin-top: 6px; line-height: 1.35;">
              Poblaci&oacute;n mundial completamente desconectada (ITU 2023).
            </div>
          </div>
        </div>

        <div style="padding-top: 20px; border-top: 1px solid var(--c-border-subtle); font-family: var(--font-sans); font-size: 24px; color: var(--c-gray-text); line-height: 1.4;">
          <strong>Dilema:</strong> La mayor&iacute;a de asistentes pedag&oacute;gicos requieren internet de fibra &oacute;ptica y suscripciones en d&oacute;lares.
        </div>
      </div>

      <!-- Columna Derecha: Dos Tarjetas Horizontales de Preguntas -->
      <div style="display: flex; flex-direction: column; gap: 20px; justify-content: space-between;">
        
        <!-- Tarjeta Pregunta 1 -->
        <div style="background: #FAF5F5; border-left: 8px solid var(--c-wine-primary); padding: 26px 30px; flex: 1; display: flex; flex-direction: column; justify-content: center;">
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px;">
            <span style="font-family: var(--font-mono); font-size: 20px; font-weight: 700; color: var(--c-wine-primary); letter-spacing: 1.5px;">
              PREGUNTA 1 &middot; HARDWARE Y MODELO
            </span>
          </div>
          <h4 style="font-family: var(--font-sans); font-size: 28px; font-weight: 700; color: var(--c-wine-dark); margin-bottom: 8px; line-height: 1.25;">
            &iquest;Cu&aacute;l modelo compacto ofrece el mejor balance entre rigor y velocidad en CPU escolar?
          </h4>
          <p style="font-family: var(--font-sans); font-size: 24px; color: var(--c-gray-text); line-height: 1.35; margin: 0;">
            Evaluaci&oacute;n de modelos SLM (3B a 8B) para operar 100% aut&oacute;nomos sin conexi&oacute;n ni GPU dedicada.
          </p>
        </div>

        <!-- Tarjeta Pregunta 2 -->
        <div style="background: #FAF5F5; border-left: 8px solid var(--c-red-accent); padding: 26px 30px; flex: 1; display: flex; flex-direction: column; justify-content: center;">
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px;">
            <span style="font-family: var(--font-mono); font-size: 20px; font-weight: 700; color: var(--c-red-accent); letter-spacing: 1.5px;">
              PREGUNTA 2 &middot; CONTROL DE CALIDAD
            </span>
          </div>
          <h4 style="font-family: var(--font-sans); font-size: 28px; font-weight: 700; color: var(--c-wine-dark); margin-bottom: 8px; line-height: 1.25;">
            &iquest;C&oacute;mo auditar y calificar las respuestas pedag&oacute;gicas antes de llevarlas al aula?
          </h4>
          <p style="font-family: var(--font-sans); font-size: 24px; color: var(--c-gray-text); line-height: 1.35; margin: 0;">
            Protocolo de evaluaci&oacute;n objetiva y ciega para detectar alucinaciones e incorrecciones gramaticales.
          </p>
        </div>

        <!-- Conclusor / Meta -->
        <div style="background: #FFFFFF; border-left: 5px solid var(--c-wine-primary); padding: 16px 22px; display: flex; align-items: center; box-shadow: none;">
          <div style="font-family: var(--font-sans); font-size: 24px; color: var(--c-text-dark); line-height: 1.35;">
            <strong>Meta:</strong> Un protocolo offline reproducible que eval&uacute;a y valida el modelo antes del aula.
          </div>
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

OPTIONS = [
    ("slide_05_opcion_a.png", CONTENT_A),
    ("slide_05_opcion_b.png", CONTENT_B),
    ("slide_05_opcion_c.png", CONTENT_C),
]

def generate_and_capture():
    print("Iniciando generación de capturas para Slide 5...")
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(viewport={"width": 1920, "height": 1080})

        for img_name, content in OPTIONS:
            full_html = BASE_TEMPLATE.format(SLIDE_CONTENT=content)
            with open(TEMP_HTML, "w", encoding="utf-8") as f:
                f.write(full_html)

            page.goto("http://localhost:8085/temp_preview_s5.html", wait_until="networkidle")
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
