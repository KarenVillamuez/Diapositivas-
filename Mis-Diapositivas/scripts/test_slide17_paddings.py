# -*- coding: utf-8 -*-
import os
from playwright.sync_api import sync_playwright

output_dir = r"C:\Users\ASUS\.gemini\antigravity-ide\brain\a6624504-511c-4b9d-bc9a-468e348bde40"
os.makedirs(output_dir, exist_ok=True)

# ===========================================================================
# Test Paddings Refinados para Slide 17
# ===========================================================================
CONTENT_PADDINGS_FIXED = '''
    <h2 class="s-lead-question" style="font-size: 38px; font-weight: 800; margin: 0; line-height: 1.2; color: #2C0509;">
      Apego al texto no es aprendizaje: criterios para auditar y desplegar tutores
    </h2>

    <div style="display: grid; grid-template-columns: 1fr 1fr; grid-template-rows: 1fr 1fr; gap: 24px; flex: 1; margin-top: 14px;">
      
      <!-- Cuadrante 1: Diagnóstico Metodológico (Rojo Alerta) -->
      <div style="background: #FAF5F5; border-top: 8px solid #C51625; padding: 26px 42px; display: grid; grid-template-columns: 1fr 220px; gap: 32px; align-items: center;">
        <div>
          <div style="font-family: var(--font-mono); font-size: 15px; font-weight: 800; color: #C51625; letter-spacing: 1.5px; margin-bottom: 4px;">
            01 · EL RIESGO OCULTO
          </div>
          <div style="font-family: var(--font-sans); font-size: 34px; font-weight: 900; color: #110103; margin-bottom: 10px;">
            La Falacia del Promedio
          </div>
          <div style="font-family: var(--font-sans); font-size: 26px; color: #110103; line-height: 1.35; font-weight: 600;">
            Mide copia del libro, no comprensión real ni capacidad pedagógica.
          </div>
        </div>
        <div style="border-left: 2.5px solid #E5D5D5; padding-left: 26px; text-align: center;">
          <div style="font-family: var(--font-mono); font-size: 60px; font-weight: 900; color: #C51625; line-height: 1;">0.795</div>
          <div style="font-family: var(--font-mono); font-size: 13px; font-weight: 800; color: #5D4A4D; margin-top: 6px; letter-spacing: 0.5px;">APEGO ENGAÑOSO</div>
        </div>
      </div>

      <!-- Cuadrante 2: Protocolo de Evaluación (Gris Pizarra Neutral) -->
      <div style="background: #FAF5F5; border-top: 8px solid #4A3B3D; padding: 26px 42px; display: grid; grid-template-columns: 1fr 220px; gap: 32px; align-items: center;">
        <div>
          <div style="font-family: var(--font-mono); font-size: 15px; font-weight: 800; color: #4A3B3D; letter-spacing: 1.5px; margin-bottom: 4px;">
            02 · EL ESTÁNDAR TÉCNICO
          </div>
          <div style="font-family: var(--font-sans); font-size: 34px; font-weight: 900; color: #110103; margin-bottom: 10px;">
            Auditoría Desglosada
          </div>
          <div style="font-family: var(--font-sans); font-size: 26px; color: #110103; line-height: 1.35; font-weight: 600;">
            <strong style="color: #4A3B3D;">Prohibido promedio único:</strong> auditar fidelidad y rechazo por separado.
          </div>
        </div>
        <div style="border-left: 2.5px solid #E5D5D5; padding-left: 26px; text-align: center;">
          <div style="font-family: var(--font-mono); font-size: 60px; font-weight: 900; color: #4A3B3D; line-height: 1;">3</div>
          <div style="font-family: var(--font-mono); font-size: 13px; font-weight: 800; color: #5D4A4D; margin-top: 6px; letter-spacing: 0.5px;">DIMENSIONES</div>
        </div>
      </div>

      <!-- Cuadrante 3: Despliegue Autoestudio (Vino Institucional Qwen) -->
      <div style="background: #FAF5F5; border-top: 8px solid var(--c-wine-primary); padding: 26px 42px; display: grid; grid-template-columns: 1fr 220px; gap: 32px; align-items: center;">
        <div>
          <div style="font-family: var(--font-mono); font-size: 15px; font-weight: 800; color: var(--c-wine-primary); letter-spacing: 1.5px; margin-bottom: 4px;">
            03 · AUTOESTUDIO SIN DOCENTE
          </div>
          <div style="font-family: var(--font-sans); font-size: 34px; font-weight: 900; color: var(--c-wine-primary); margin-bottom: 10px;">
            Qwen2.5-3B: Certeza
          </div>
          <div style="font-family: var(--font-sans); font-size: 26px; color: #110103; line-height: 1.35; font-weight: 600;">
            <strong>Sin profesor:</strong> preferible admitir no saber antes que inventar.
          </div>
        </div>
        <div style="border-left: 2.5px solid #E5D5D5; padding-left: 26px; text-align: center;">
          <div style="font-family: var(--font-mono); font-size: 62px; font-weight: 900; color: var(--c-wine-primary); line-height: 1;">85.7%</div>
          <div style="font-family: var(--font-mono); font-size: 13px; font-weight: 800; color: var(--c-wine-primary); margin-top: 6px; letter-spacing: 0.5px;">RECHAZO CERTERO</div>
        </div>
      </div>

      <!-- Cuadrante 4: Despliegue Aula Asistida (Rojo Acento Phi) -->
      <div style="background: #FAF5F5; border-top: 8px solid var(--c-red-accent); padding: 26px 42px; display: grid; grid-template-columns: 1fr 220px; gap: 32px; align-items: center;">
        <div>
          <div style="font-family: var(--font-mono); font-size: 15px; font-weight: 800; color: var(--c-red-accent); letter-spacing: 1.5px; margin-bottom: 4px;">
            04 · AULA ASISTIDA CON DOCENTE
          </div>
          <div style="font-family: var(--font-sans); font-size: 34px; font-weight: 900; color: var(--c-red-accent); margin-bottom: 10px;">
            Phi-4-mini: Fluidez
          </div>
          <div style="font-family: var(--font-sans); font-size: 26px; color: #110103; line-height: 1.35; font-weight: 600;">
            <strong>Con profesor:</strong> prima la fluidez y el docente corrige en vivo.
          </div>
        </div>
        <div style="border-left: 2.5px solid #E5D5D5; padding-left: 26px; text-align: center;">
          <div style="font-family: var(--font-mono); font-size: 62px; font-weight: 900; color: var(--c-red-accent); line-height: 1;">0.0%</div>
          <div style="font-family: var(--font-mono); font-size: 13px; font-weight: 800; color: var(--c-red-accent); margin-top: 6px; letter-spacing: 0.5px;">BLOQUEOS DIÁLOGO</div>
        </div>
      </div>

    </div>
'''

HTML_TEMPLATE = '''<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Test Slide 17 Padding Fix</title>
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

        html_path = os.path.join(output_dir, "slide_17_padding_test.html")
        png_path = os.path.join(output_dir, "slide_17_padding_test.png")

        full_html = HTML_TEMPLATE.format(content=CONTENT_PADDINGS_FIXED)
        with open(html_path, 'w', encoding='utf-8') as f:
            f.write(full_html)

        page.goto(f"file:///{html_path.replace(os.sep, '/')}")
        page.wait_for_timeout(400)
        page.screenshot(path=png_path)
        print("Captured: slide_17_padding_test.png")

        browser.close()

if __name__ == '__main__':
    main()
