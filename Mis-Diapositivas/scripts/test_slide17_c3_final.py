# -*- coding: utf-8 -*-
import os
from playwright.sync_api import sync_playwright

output_dir = r"C:\Users\ASUS\.gemini\antigravity-ide\brain\a6624504-511c-4b9d-bc9a-468e348bde40"
os.makedirs(output_dir, exist_ok=True)

# ===========================================================================
# A1: Natural Vertical Rhythm (Sin hueco central, Texto 27px, Números 64px)
# ===========================================================================
CONTENT_A1 = '''
    <h2 class="s-lead-question" style="font-size: 38px; font-weight: 800; margin: 0; line-height: 1.2; color: #2C0509;">
      Apego al texto no es aprendizaje: criterios para auditar y desplegar tutores
    </h2>

    <div style="display: grid; grid-template-columns: 1fr 1fr; grid-template-rows: 1fr 1fr; gap: 24px; flex: 1; margin-top: 14px;">
      
      <!-- C1 -->
      <div style="background: #FAF5F5; border-top: 8px solid #C51625; padding: 28px 36px; display: flex; flex-direction: column;">
        <div style="display: flex; justify-content: space-between; align-items: flex-start;">
          <div>
            <div style="font-family: var(--font-mono); font-size: 16px; font-weight: 800; color: #C51625; letter-spacing: 1.5px; margin-bottom: 4px;">
              01 · EL RIESGO OCULTO
            </div>
            <div style="font-family: var(--font-sans); font-size: 36px; font-weight: 900; color: #110103;">
              La Falacia del Promedio
            </div>
          </div>
          <div style="text-align: right;">
            <div style="font-family: var(--font-mono); font-size: 62px; font-weight: 900; color: #C51625; line-height: 0.95;">0.795</div>
            <div style="font-family: var(--font-mono); font-size: 14px; font-weight: 800; color: #C51625; letter-spacing: 1px; margin-top: 4px;">APEGO ENGAÑOSO</div>
          </div>
        </div>
        <div style="border-top: 2px solid #E5D5D5; margin: 14px 0 16px 0;"></div>
        <div style="font-family: var(--font-sans); font-size: 27px; color: #110103; line-height: 1.38; font-weight: 600;">
          El puntaje premia copiar del libro, pero da una falsa ilusión de éxito: encubre que el tutor inventa falsedades al quedarse sin datos.
        </div>
      </div>

      <!-- C2 -->
      <div style="background: #FAF5F5; border-top: 8px solid #4A3B3D; padding: 28px 36px; display: flex; flex-direction: column;">
        <div style="display: flex; justify-content: space-between; align-items: flex-start;">
          <div>
            <div style="font-family: var(--font-mono); font-size: 16px; font-weight: 800; color: #4A3B3D; letter-spacing: 1.5px; margin-bottom: 4px;">
              02 · EL ESTÁNDAR TÉCNICO
            </div>
            <div style="font-family: var(--font-sans); font-size: 36px; font-weight: 900; color: #110103;">
              Auditoría Desglosada
            </div>
          </div>
          <div style="text-align: right;">
            <div style="font-family: var(--font-mono); font-size: 62px; font-weight: 900; color: #4A3B3D; line-height: 0.95;">3</div>
            <div style="font-family: var(--font-mono); font-size: 14px; font-weight: 800; color: #4A3B3D; letter-spacing: 1px; margin-top: 4px;">DIMENSIONES</div>
          </div>
        </div>
        <div style="border-top: 2px solid #E5D5D5; margin: 14px 0 16px 0;"></div>
        <div style="font-family: var(--font-sans); font-size: 27px; color: #110103; line-height: 1.38; font-weight: 600;">
          <strong style="color: #4A3B3D;">Prohibido evaluar con nota única:</strong> es obligatorio medir por separado recuperación de fuentes, fidelidad contextual y rechazo.
        </div>
      </div>

      <!-- C3 -->
      <div style="background: #FAF5F5; border-top: 8px solid var(--c-wine-primary); padding: 28px 36px; display: flex; flex-direction: column;">
        <div style="display: flex; justify-content: space-between; align-items: flex-start;">
          <div>
            <div style="font-family: var(--font-mono); font-size: 16px; font-weight: 800; color: var(--c-wine-primary); letter-spacing: 1.5px; margin-bottom: 4px;">
              03 · AUTOESTUDIO SIN DOCENTE
            </div>
            <div style="font-family: var(--font-sans); font-size: 36px; font-weight: 900; color: var(--c-wine-primary);">
              Qwen2.5-3B: Certeza
            </div>
          </div>
          <div style="text-align: right;">
            <div style="font-family: var(--font-mono); font-size: 64px; font-weight: 900; color: var(--c-wine-primary); line-height: 0.95;">85.7%</div>
            <div style="font-family: var(--font-mono); font-size: 14px; font-weight: 800; color: var(--c-wine-primary); letter-spacing: 1px; margin-top: 4px;">RECHAZO CERTERO</div>
          </div>
        </div>
        <div style="border-top: 2px solid #E5D5D5; margin: 14px 0 16px 0;"></div>
        <div style="font-family: var(--font-sans); font-size: 27px; color: #110103; line-height: 1.38; font-weight: 600;">
          En soledad no hay profesor que supervise: alucinar destruye la confianza. Prima la certeza; es preferible admitir no saber antes que inventar.
        </div>
      </div>

      <!-- C4 -->
      <div style="background: #FAF5F5; border-top: 8px solid var(--c-red-accent); padding: 28px 36px; display: flex; flex-direction: column;">
        <div style="display: flex; justify-content: space-between; align-items: flex-start;">
          <div>
            <div style="font-family: var(--font-mono); font-size: 16px; font-weight: 800; color: var(--c-red-accent); letter-spacing: 1.5px; margin-bottom: 4px;">
              04 · AULA ASISTIDA CON DOCENTE
            </div>
            <div style="font-family: var(--font-sans); font-size: 36px; font-weight: 900; color: var(--c-red-accent);">
              Phi-4-mini: Fluidez
            </div>
          </div>
          <div style="text-align: right;">
            <div style="font-family: var(--font-mono); font-size: 64px; font-weight: 900; color: var(--c-red-accent); line-height: 0.95;">0.0%</div>
            <div style="font-family: var(--font-mono); font-size: 14px; font-weight: 800; color: var(--c-red-accent); letter-spacing: 1px; margin-top: 4px;">BLOQUEOS DIÁLOGO</div>
          </div>
        </div>
        <div style="border-top: 2px solid #E5D5D5; margin: 14px 0 16px 0;"></div>
        <div style="font-family: var(--font-sans); font-size: 27px; color: #110103; line-height: 1.38; font-weight: 600;">
          En clase interactiva prima el ritmo: dinamiza la sesión sin bloqueos innecesarios, y el docente modera y corrige imprecisiones en vivo.
        </div>
      </div>

    </div>
'''

HTML_TEMPLATE = '''<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Test Slide 17 A1</title>
  <link rel="stylesheet" href="http://localhost:8085/styles.css?v=33">
</head>
<body style="margin: 0; padding: 0; background: #0b0103;">

  <div id="presentation-viewport">
    <div id="slides-stage">
      <section class="slide s-white active">
        <header class="slide-header">
          <div class="sh-left">
            <span class="sh-red-bar"></span>
            <span class="sh-category">04 · DISCUSIÓN · GUÍA METODOLÓGICA DE ELECCIÓN</span>
          </div>
          <img src="http://localhost:8085/assets/image6.png" alt="#LoxTIC" class="sh-loxtic">
        </header>
        <div class="sh-divider"></div>

        <div class="slide-content-area" style="top: 175px; height: 720px; justify-content: space-between;">
          {content}
        </div>

        <div class="slide-footer-rule"></div>
        <footer class="slide-footer">
          <span class="sf-left">VI CONGRESO CARTAGENA · 2026</span>
          <span class="sf-right">LOHACEMOSXTIC.COM · SLM OFFLINE</span>
        </footer>
      </section>
    </div>
  </div>

</body>
</html>
'''

def main():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(viewport={"width": 1920, "height": 1080})

        html_path = os.path.join(output_dir, "slide_17_c3_perfect_final.html")
        png_path = os.path.join(output_dir, "slide_17_c3_perfect_final.png")

        full_html = HTML_TEMPLATE.format(content=CONTENT_A1)
        with open(html_path, 'w', encoding='utf-8') as f:
            f.write(full_html)

        page.goto(f"file:///{html_path.replace(os.sep, '/')}")
        page.wait_for_timeout(400)
        page.screenshot(path=png_path)
        print("Captured: slide_17_c3_perfect_final.png")

        browser.close()

if __name__ == '__main__':
    main()
