# -*- coding: utf-8 -*-
import os
from playwright.sync_api import sync_playwright

# Plantilla base para slide 9
base_header = '''<!-- ====================================================================
     SLIDE 09: 02 · METODOLOGÍA / BANCO CURRICULAR
     ==================================================================== -->
<section class="slide s-white" id="slide-9">
  <header class="slide-header">
    <div class="sh-left">
      <span class="sh-red-bar"></span>
      <span class="sh-category">02 &middot; METODOLOG&Iacute;A &middot; BANCO CURRICULAR</span>
    </div>
    <img src="assets/image6.png" alt="#LoxTIC" class="sh-loxtic">
  </header>
  <div class="sh-divider"></div>

  <div class="slide-content-area" style="justify-content: center; padding-top: 10px; padding-bottom: 20px;">
    <h2 class="s-lead-question" style="font-size: 46px; font-weight: 800; margin-bottom: 28px; line-height: 1.2;">
      Banco de evaluaci&oacute;n: 14 preguntas dise&ntilde;adas para el aula rural
    </h2>
'''

base_footer = '''
  </div>

  <div class="slide-footer-rule"></div>
  <footer class="slide-footer">
    <span class="sf-left">VI CONGRESO CARTAGENA &middot; 2026</span>
    <span class="sf-right">LOHACEMOSXTIC.COM &middot; SLM OFFLINE</span>
  </footer>
</section>
'''

# -------------------------------------------------------------------------
# OPCIÓN A: TABLA EDITORIAL LIMPIA (Sin artefactos de paper, tildes corregidas, alto contraste)
# -------------------------------------------------------------------------
opcion_a_content = '''
    <div style="background: #FFFFFF; border: 2px solid var(--c-wine-primary); overflow: hidden;">
      <table style="width: 100%; border-collapse: collapse; font-family: var(--font-sans); text-align: left;">
        <thead>
          <tr style="background: var(--c-wine-primary); color: #FFFFFF;">
            <th style="padding: 16px 24px; font-family: var(--font-mono); font-size: 20px; font-weight: 700; letter-spacing: 1px; width: 22%;">COMPETENCIA</th>
            <th style="padding: 16px 20px; font-family: var(--font-mono); font-size: 20px; font-weight: 700; letter-spacing: 1px; width: 14%; text-align: center;">C&Oacute;DIGOS</th>
            <th style="padding: 16px 20px; font-family: var(--font-mono); font-size: 20px; font-weight: 700; letter-spacing: 1px; width: 18%; text-align: center;">P&Aacute;GINAS</th>
            <th style="padding: 16px 24px; font-family: var(--font-mono); font-size: 20px; font-weight: 700; letter-spacing: 1px; width: 46%;">PROP&Oacute;SITO PEDAG&Oacute;GICO</th>
          </tr>
        </thead>
        <tbody>
          <tr style="background: #FFFFFF; border-bottom: 1px solid var(--c-border-subtle);">
            <td style="padding: 18px 24px; font-size: 25px; font-weight: 800; color: #110103;">Grammar</td>
            <td style="padding: 18px 20px; font-size: 24px; font-family: var(--font-mono); font-weight: 700; color: var(--c-wine-primary); text-align: center;">G1 &ndash; G4</td>
            <td style="padding: 18px 20px; font-size: 24px; font-family: var(--font-mono); color: #444444; text-align: center;">191 &ndash; 235</td>
            <td style="padding: 18px 24px; font-size: 24px; color: #110103; line-height: 1.35;">4 preguntas sobre reglas gramaticales y tiempos verbales.</td>
          </tr>
          <tr style="background: #FAF5F5; border-bottom: 1px solid var(--c-border-subtle);">
            <td style="padding: 18px 24px; font-size: 25px; font-weight: 800; color: #110103;">Vocabulary</td>
            <td style="padding: 18px 20px; font-size: 24px; font-family: var(--font-mono); font-weight: 700; color: var(--c-wine-primary); text-align: center;">V1 &ndash; V3</td>
            <td style="padding: 18px 20px; font-size: 24px; font-family: var(--font-mono); color: #444444; text-align: center;">36 &ndash; 150</td>
            <td style="padding: 18px 24px; font-size: 24px; color: #110103; line-height: 1.35;">3 preguntas de definici&oacute;n y uso en contexto formal.</td>
          </tr>
          <tr style="background: #FFFFFF; border-bottom: 1px solid var(--c-border-subtle);">
            <td style="padding: 18px 24px; font-size: 25px; font-weight: 800; color: #110103;">Writing</td>
            <td style="padding: 18px 20px; font-size: 24px; font-family: var(--font-mono); font-weight: 700; color: var(--c-wine-primary); text-align: center;">W1 &ndash; W3</td>
            <td style="padding: 18px 20px; font-size: 24px; font-family: var(--font-mono); color: #444444; text-align: center;">68 &ndash; 138</td>
            <td style="padding: 18px 24px; font-size: 24px; color: #110103; line-height: 1.35;">3 preguntas sobre estructura de p&aacute;rrafos y coherencia.</td>
          </tr>
          <tr style="background: #FAF5F5; border-bottom: 2px solid var(--c-red-accent);">
            <td style="padding: 18px 24px; font-size: 25px; font-weight: 800; color: #110103;">Reading</td>
            <td style="padding: 18px 20px; font-size: 24px; font-family: var(--font-mono); font-weight: 700; color: var(--c-wine-primary); text-align: center;">R1 &ndash; R2</td>
            <td style="padding: 18px 20px; font-size: 24px; font-family: var(--font-mono); color: #444444; text-align: center;">15 &ndash; 60</td>
            <td style="padding: 18px 24px; font-size: 24px; color: #110103; line-height: 1.35;">2 preguntas de comprensi&oacute;n e inferencia textual.</td>
          </tr>
          <tr style="background: #FFF2F2;">
            <td style="padding: 20px 24px; font-size: 25px; font-weight: 800; color: var(--c-red-accent);">
              <span style="display: inline-block; background: var(--c-red-accent); color: #FFFFFF; font-size: 14px; font-family: var(--font-mono); padding: 2px 8px; margin-right: 8px; border-radius: 3px;">SONDA</span>
              Fuera de alcance
            </td>
            <td style="padding: 20px 20px; font-size: 25px; font-family: var(--font-mono); font-weight: 800; color: var(--c-red-accent); text-align: center;">F1 &ndash; F2</td>
            <td style="padding: 20px 20px; font-size: 23px; font-weight: 700; color: var(--c-red-accent); text-align: center;">Ausente en libro</td>
            <td style="padding: 20px 24px; font-size: 24px; color: #110103; line-height: 1.35;">
              <strong style="color: var(--c-red-accent);">2 sondas de rechazo:</strong> Auditan si el modelo inventa informaci&oacute;n o se abstiene con honestidad.
            </td>
          </tr>
        </tbody>
      </table>
    </div>
    <div style="margin-top: 14px; font-family: var(--font-mono); font-size: 19px; color: var(--c-wine-primary); font-weight: 700;">
      TOTAL: 12 PREGUNTAS CURRICULARES + 2 SONDAS DE RECHAZO (LIBRO COLLEGE ESL WRITERS)
    </div>
'''

# -------------------------------------------------------------------------
# OPCIÓN B: TRÍPTICO/MALLA CURRICULAR + TARJETA PANORÁMICA DE SONDAS (Recomendada)
# -------------------------------------------------------------------------
opcion_b_content = '''
    <div style="display: flex; flex-direction: column; gap: 20px;">
      
      <!-- Fila Superior: 4 Tarjetas Curriculares -->
      <div style="display: flex; gap: 16px; align-items: stretch;">
        
        <!-- Grammar -->
        <div style="flex: 1; background: #FAF5F5; border: 2px solid var(--c-wine-primary); padding: 22px 20px; display: flex; flex-direction: column;">
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 6px;">
            <span style="font-family: var(--font-mono); font-size: 18px; font-weight: 700; color: var(--c-wine-primary);">G1 &ndash; G4</span>
            <span style="font-family: var(--font-mono); font-size: 16px; font-weight: 700; color: #666666;">P&aacute;gs. 191&ndash;235</span>
          </div>
          <div style="font-family: var(--font-sans); font-size: 28px; font-weight: 800; color: #110103; margin-bottom: 10px;">
            Grammar
          </div>
          <div style="font-family: var(--font-sans); font-size: 23px; color: #110103; line-height: 1.35;">
            <strong>4 preguntas:</strong> Reglas gramaticales, tiempos verbales y auxiliares.
          </div>
        </div>

        <!-- Vocabulary -->
        <div style="flex: 1; background: #FAF5F5; border: 2px solid var(--c-wine-primary); padding: 22px 20px; display: flex; flex-direction: column;">
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 6px;">
            <span style="font-family: var(--font-mono); font-size: 18px; font-weight: 700; color: var(--c-wine-primary);">V1 &ndash; V3</span>
            <span style="font-family: var(--font-mono); font-size: 16px; font-weight: 700; color: #666666;">P&aacute;gs. 36&ndash;150</span>
          </div>
          <div style="font-family: var(--font-sans); font-size: 28px; font-weight: 800; color: #110103; margin-bottom: 10px;">
            Vocabulary
          </div>
          <div style="font-family: var(--font-sans); font-size: 23px; color: #110103; line-height: 1.35;">
            <strong>3 preguntas:</strong> Definici&oacute;n contextual, sin&oacute;nimos y uso formal.
          </div>
        </div>

        <!-- Writing -->
        <div style="flex: 1; background: #FAF5F5; border: 2px solid var(--c-wine-primary); padding: 22px 20px; display: flex; flex-direction: column;">
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 6px;">
            <span style="font-family: var(--font-mono); font-size: 18px; font-weight: 700; color: var(--c-wine-primary);">W1 &ndash; W3</span>
            <span style="font-family: var(--font-mono); font-size: 16px; font-weight: 700; color: #666666;">P&aacute;gs. 68&ndash;138</span>
          </div>
          <div style="font-family: var(--font-sans); font-size: 28px; font-weight: 800; color: #110103; margin-bottom: 10px;">
            Writing
          </div>
          <div style="font-family: var(--font-sans); font-size: 23px; color: #110103; line-height: 1.35;">
            <strong>3 preguntas:</strong> Estructura de p&aacute;rrafos, coherencia y conectores.
          </div>
        </div>

        <!-- Reading -->
        <div style="flex: 1; background: #FAF5F5; border: 2px solid var(--c-wine-primary); padding: 22px 20px; display: flex; flex-direction: column;">
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 6px;">
            <span style="font-family: var(--font-mono); font-size: 18px; font-weight: 700; color: var(--c-wine-primary);">R1 &ndash; R2</span>
            <span style="font-family: var(--font-mono); font-size: 16px; font-weight: 700; color: #666666;">P&aacute;gs. 15&ndash;60</span>
          </div>
          <div style="font-family: var(--font-sans); font-size: 28px; font-weight: 800; color: #110103; margin-bottom: 10px;">
            Reading
          </div>
          <div style="font-family: var(--font-sans); font-size: 23px; color: #110103; line-height: 1.35;">
            <strong>2 preguntas:</strong> Comprensi&oacute;n global e inferencia pedag&oacute;gica.
          </div>
        </div>

      </div>

      <!-- Tarjeta Panorámica Inferior: 2 Sondas de Rechazo -->
      <div style="background: #FFF2F2; border: 2px solid var(--c-red-accent); padding: 26px 36px; display: flex; align-items: center; gap: 36px;">
        <div style="flex: 0 0 230px; text-align: center;">
          <div style="font-family: var(--font-mono); font-size: 50px; font-weight: 800; color: var(--c-red-accent); line-height: 1;">
            F1 &ndash; F2
          </div>
          <div style="font-family: var(--font-mono); font-size: 17px; font-weight: 800; color: var(--c-red-accent); margin-top: 6px; letter-spacing: 1px;">
            SONDAS DE RECHAZO
          </div>
        </div>
        <div style="width: 2px; height: 90px; background: rgba(201, 16, 27, 0.25); flex-shrink: 0;"></div>
        <div style="flex: 1;">
          <div style="font-family: var(--font-sans); font-size: 28px; font-weight: 800; color: var(--c-red-accent); margin-bottom: 8px;">
            Auditor&iacute;a de Alucinaci&oacute;n: Ausentes en el Libro de Texto
          </div>
          <p style="font-family: var(--font-sans); font-size: 24px; color: #110103; line-height: 1.4; margin: 0;">
            Preguntas deliberadamente sin sustento curricular para auditar si el modelo local <strong>inventa informaci&oacute;n espuria</strong> o <strong>se abstiene con honestidad</strong> al carecer de evidencia en el RAG.
          </p>
        </div>
      </div>

    </div>
'''

# -------------------------------------------------------------------------
# OPCIÓN C: DOS BLOQUES HORIZONTALES (12 Curriculares vs. 2 Sondas)
# -------------------------------------------------------------------------
opcion_c_content = '''
    <div style="display: flex; gap: 26px; align-items: stretch;">
      
      <!-- Bloque 1: 12 Preguntas Curriculares -->
      <div style="flex: 1.3; background: #FAF5F5; border: 2px solid var(--c-wine-primary); padding: 28px; display: flex; flex-direction: column; justify-content: space-between;">
        <div>
          <div style="display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 12px;">
            <div style="font-family: var(--font-sans); font-size: 32px; font-weight: 800; color: var(--c-wine-primary);">
              12 Preguntas Curriculares
            </div>
            <div style="font-family: var(--font-mono); font-size: 19px; font-weight: 700; color: #666666;">
              Libro College ESL
            </div>
          </div>
          <div style="width: 100%; height: 2px; background: var(--c-border-subtle); margin-bottom: 20px;"></div>
          
          <div style="display: flex; flex-direction: column; gap: 14px;">
            <div style="display: flex; justify-content: space-between; font-size: 24px;">
              <span style="font-weight: 700; color: #110103;">Grammar (G1&ndash;G4):</span>
              <span style="color: #444444;">Reglas y tiempos verbales (P&aacute;gs. 191&ndash;235)</span>
            </div>
            <div style="display: flex; justify-content: space-between; font-size: 24px;">
              <span style="font-weight: 700; color: #110103;">Vocabulary (V1&ndash;V3):</span>
              <span style="color: #444444;">Definici&oacute;n y contexto formal (P&aacute;gs. 36&ndash;150)</span>
            </div>
            <div style="display: flex; justify-content: space-between; font-size: 24px;">
              <span style="font-weight: 700; color: #110103;">Writing (W1&ndash;W3):</span>
              <span style="color: #444444;">Estructura de p&aacute;rrafos (P&aacute;gs. 68&ndash;138)</span>
            </div>
            <div style="display: flex; justify-content: space-between; font-size: 24px;">
              <span style="font-weight: 700; color: #110103;">Reading (R1&ndash;R2):</span>
              <span style="color: #444444;">Comprensi&oacute;n e inferencia (P&aacute;gs. 15&ndash;60)</span>
            </div>
          </div>
        </div>

        <div style="margin-top: 24px; padding-top: 14px; border-top: 1px dashed var(--c-border-subtle); font-family: var(--font-mono); font-size: 19px; color: var(--c-wine-primary); font-weight: 700;">
          OBJETIVO: Medir precisi&oacute;n pedag&oacute;gica en el contenido del curso.
        </div>
      </div>

      <!-- Bloque 2: 2 Sondas de Rechazo -->
      <div style="flex: 1; background: #FFF2F2; border: 2px solid var(--c-red-accent); padding: 28px; display: flex; flex-direction: column; justify-content: space-between;">
        <div>
          <div style="display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 12px;">
            <div style="font-family: var(--font-sans); font-size: 32px; font-weight: 800; color: var(--c-red-accent);">
              2 Sondas de Rechazo
            </div>
            <div style="font-family: var(--font-mono); font-size: 19px; font-weight: 800; color: var(--c-red-accent);">
              F1 &ndash; F2
            </div>
          </div>
          <div style="width: 100%; height: 2px; background: rgba(201, 16, 27, 0.25); margin-bottom: 20px;"></div>

          <div style="font-family: var(--font-mono); font-size: 20px; font-weight: 800; color: var(--c-red-accent); margin-bottom: 10px;">
            CONTENIDO AUSENTE EN EL LIBRO
          </div>
          <p style="font-family: var(--font-sans); font-size: 24px; color: #110103; line-height: 1.45; margin-bottom: 16px;">
            Dise&ntilde;adas intencionalmente para evaluar el <strong>control de alucinaciones</strong>:
          </p>
          <ul style="font-family: var(--font-sans); font-size: 23px; color: #110103; line-height: 1.4; padding-left: 24px; margin: 0;">
            <li style="margin-bottom: 8px;">&iquest;El modelo admite honestamente que no lo sabe?</li>
            <li>&iquest;O inventa informaci&oacute;n cre&iacute;ble pero falsa?</li>
          </ul>
        </div>

        <div style="margin-top: 24px; padding-top: 14px; border-top: 1px dashed rgba(201, 16, 27, 0.3); font-family: var(--font-mono); font-size: 19px; color: var(--c-red-accent); font-weight: 700;">
          OBJETIVO: Auditar la seguridad y abstenci&oacute;n del tutor.
        </div>
      </div>

    </div>
'''

options = {
    "slide_09_opcion_a.png": opcion_a_content,
    "slide_09_opcion_b.png": opcion_b_content,
    "slide_09_opcion_c.png": opcion_c_content,
}

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page(viewport={"width": 1920, "height": 1080})

    for img_name, content in options.items():
        full_html = base_header + content + base_footer
        with open("slides/slide_09.html", "w", encoding="utf-8") as f:
            f.write(full_html)
        os.system("python scripts/build.py")
        page.goto(f"http://localhost:8085/?opt={img_name}#slide-9")
        page.wait_for_load_state("networkidle")
        page.evaluate('''
            const slides = document.querySelectorAll('.slide');
            slides.forEach((s, idx) => {
                if (idx === 8) s.classList.add('active');
                else s.classList.remove('active');
            });
        ''')
        page.wait_for_timeout(350)
        page.screenshot(path=img_name)
        print(f"Captured {img_name}")

    browser.close()

print("All Slide 9 options rendered successfully.")
