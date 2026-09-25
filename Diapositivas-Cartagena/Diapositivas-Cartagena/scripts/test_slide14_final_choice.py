# -*- coding: utf-8 -*-
"""
Comparación de enfoques para resolver el problema de sobrecarga y espacio muerto:
- Enfoque H: 2 Paneles Horizontales (Phi-4-mini arriba / Qwen2.5-3B abajo).
- Enfoque V1: 2 Columnas con Barras Gruesas de 28px y Espaciado Uniforme (sin huecos).
- Enfoque V2: 2 Columnas Compactas con Altura Natural y Proporción Aurea.
"""
import os
from playwright.sync_api import sync_playwright

output_dir = r"C:\Users\ASUS\.gemini\antigravity-ide\brain\a6624504-511c-4b9d-bc9a-468e348bde40"
os.makedirs(output_dir, exist_ok=True)

# -----------------------------------------------------------------------------
# ENFOQUE H: 2 Paneles Horizontales (Aprovecha el 16:9, Cero Espacio Muerto)
# -----------------------------------------------------------------------------
HTML_ENFOQUE_H = '''
<section class="slide s-white active" id="slide-14-h">
  <header class="slide-header">
    <div class="sh-left">
      <span class="sh-red-bar"></span>
      <span class="sh-category">03 · RESULTADOS · MODOS DE FALLO ASIMÉTRICOS</span>
    </div>
    <img src="http://localhost:8085/assets/image6.png" alt="#LoxTIC" class="sh-loxtic">
  </header>
  <div class="sh-divider"></div>

  <div class="slide-content-area" style="justify-content: center; gap: 24px;">
    
    <h2 class="s-lead-question" style="font-size: 38px; font-weight: 800; margin: 0; line-height: 1.2; color: var(--c-text-dark);">
      Alucinación frente a sobre-rechazo: cómo fallan dos modelos con la misma nota
    </h2>

    <!-- PANEL 1: PHI-4-MINI (HORIZONTAL) -->
    <div style="background: var(--c-pink-bg); border-left: 8px solid var(--c-wine-primary); padding: 26px 36px; display: grid; grid-template-columns: 380px 1fr 1fr; gap: 40px; align-items: center;">
      <!-- Identidad -->
      <div style="border-right: 2px solid var(--c-border-subtle); padding-right: 28px;">
        <div style="display: flex; justify-content: space-between; align-items: baseline;">
          <span style="font-family: var(--font-mono); font-size: 19px; font-weight: 700; color: var(--c-wine-primary); letter-spacing: 1.5px;">PERFIL PERMISIVO</span>
          <span style="font-family: var(--font-mono); font-size: 20px; font-weight: 700; color: var(--c-wine-dark);">Q = 0.8030</span>
        </div>
        <div style="font-family: var(--font-sans); font-size: 36px; font-weight: 800; color: var(--c-text-dark); margin: 4px 0 8px 0;">
          Phi-4-mini <span style="font-size: 22px; font-weight: 600; color: var(--c-gray-text);">3.8B</span>
        </div>
        <div style="font-family: var(--font-sans); font-size: 22px; font-weight: 700; color: #110103;">
          <strong style="color: var(--c-wine-primary);">Aula asistida:</strong> con docente activo.
        </div>
      </div>

      <!-- Barra 1: Sondas trampa -->
      <div>
        <div style="display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 8px;">
          <span style="font-family: var(--font-sans); font-size: 22px; font-weight: 700; color: var(--c-text-dark);">Rechazo en trampas (14):</span>
          <span style="font-family: var(--font-mono); font-size: 36px; font-weight: 800; color: var(--c-red-accent);">28.6%</span>
        </div>
        <div style="background: var(--c-border-subtle); height: 22px; width: 100%; margin-bottom: 8px;">
          <div style="width: 28.6%; background: var(--c-red-accent); height: 100%;"></div>
        </div>
        <div style="font-family: var(--font-sans); font-size: 21px; color: var(--c-red-accent); font-weight: 700;">
          Alucina en 10 casos fuera de libro.
        </div>
      </div>

      <!-- Barra 2: Consultas válidas -->
      <div>
        <div style="display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 8px;">
          <span style="font-family: var(--font-sans); font-size: 22px; font-weight: 700; color: var(--c-text-dark);">Falso rechazo (84 válidas):</span>
          <span style="font-family: var(--font-mono); font-size: 36px; font-weight: 800; color: var(--c-wine-primary);">0.0%</span>
        </div>
        <div style="background: var(--c-border-subtle); height: 22px; width: 100%; margin-bottom: 8px;">
          <div style="width: 0%; background: var(--c-wine-primary); height: 100%;"></div>
        </div>
        <div style="font-family: var(--font-sans); font-size: 21px; color: var(--c-wine-primary); font-weight: 700;">
          Fluidez total; jamás frena al alumno.
        </div>
      </div>
    </div>

    <!-- PANEL 2: QWEN2.5-3B (HORIZONTAL) -->
    <div style="background: var(--c-pink-bg); border-left: 8px solid var(--c-red-accent); padding: 26px 36px; display: grid; grid-template-columns: 380px 1fr 1fr; gap: 40px; align-items: center;">
      <!-- Identidad -->
      <div style="border-right: 2px solid var(--c-border-subtle); padding-right: 28px;">
        <div style="display: flex; justify-content: space-between; align-items: baseline;">
          <span style="font-family: var(--font-mono); font-size: 19px; font-weight: 700; color: var(--c-red-accent); letter-spacing: 1.5px;">PERFIL CONSERVADOR</span>
          <span style="font-family: var(--font-mono); font-size: 20px; font-weight: 700; color: var(--c-wine-dark);">Q = 0.8010</span>
        </div>
        <div style="font-family: var(--font-sans); font-size: 36px; font-weight: 800; color: var(--c-text-dark); margin: 4px 0 8px 0;">
          Qwen2.5-3B <span style="font-size: 22px; font-weight: 600; color: var(--c-gray-text);">3.1B</span>
        </div>
        <div style="font-family: var(--font-sans); font-size: 22px; font-weight: 700; color: #110103;">
          <strong style="color: var(--c-red-accent);">Autoestudio:</strong> sin docente presente.
        </div>
      </div>

      <!-- Barra 1: Sondas trampa -->
      <div>
        <div style="display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 8px;">
          <span style="font-family: var(--font-sans); font-size: 22px; font-weight: 700; color: var(--c-text-dark);">Rechazo en trampas (14):</span>
          <span style="font-family: var(--font-mono); font-size: 36px; font-weight: 800; color: var(--c-wine-primary);">85.7%</span>
        </div>
        <div style="background: var(--c-border-subtle); height: 22px; width: 100%; margin-bottom: 8px;">
          <div style="width: 85.7%; background: var(--c-wine-primary); height: 100%;"></div>
        </div>
        <div style="font-family: var(--font-sans); font-size: 21px; color: var(--c-wine-primary); font-weight: 700;">
          Filtro riguroso frente a trampas.
        </div>
      </div>

      <!-- Barra 2: Consultas válidas -->
      <div>
        <div style="display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 8px;">
          <span style="font-family: var(--font-sans); font-size: 22px; font-weight: 700; color: var(--c-text-dark);">Falso rechazo (84 válidas):</span>
          <span style="font-family: var(--font-mono); font-size: 36px; font-weight: 800; color: var(--c-red-accent);">7.1%</span>
        </div>
        <div style="background: var(--c-border-subtle); height: 22px; width: 100%; margin-bottom: 8px;">
          <div style="width: 25%; background: var(--c-red-accent); height: 100%;"></div>
        </div>
        <div style="font-family: var(--font-sans); font-size: 21px; color: var(--c-red-accent); font-weight: 700;">
          Sobre-rechazo por cautela extrema.
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
'''

# -----------------------------------------------------------------------------
# ENFOQUE V1: 2 Columnas con Barras Gruesas Dominantes y Espaciado Armónico
# -----------------------------------------------------------------------------
HTML_ENFOQUE_V1 = '''
<section class="slide s-white active" id="slide-14-v1">
  <header class="slide-header">
    <div class="sh-left">
      <span class="sh-red-bar"></span>
      <span class="sh-category">03 · RESULTADOS · MODOS DE FALLO ASIMÉTRICOS</span>
    </div>
    <img src="http://localhost:8085/assets/image6.png" alt="#LoxTIC" class="sh-loxtic">
  </header>
  <div class="sh-divider"></div>

  <div class="slide-content-area" style="justify-content: center; gap: 24px;">
    
    <h2 class="s-lead-question" style="font-size: 38px; font-weight: 800; margin: 0; line-height: 1.2; color: var(--c-text-dark);">
      Alucinación frente a sobre-rechazo: cómo fallan dos modelos con la misma nota
    </h2>

    <div class="grid-2col" style="gap: 36px; align-items: stretch;">
      
      <!-- PHI-4-MINI -->
      <div style="background: var(--c-pink-bg); border-top: 8px solid var(--c-wine-primary); padding: 34px 38px; display: flex; flex-direction: column; justify-content: space-between; box-sizing: border-box;">
        <div>
          <!-- Cabecera -->
          <div style="display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 4px;">
            <span style="font-family: var(--font-mono); font-size: 21px; font-weight: 700; color: var(--c-wine-primary); letter-spacing: 2px;">
              PERFIL PERMISIVO
            </span>
            <span style="font-family: var(--font-mono); font-size: 24px; font-weight: 700; color: var(--c-wine-dark);">
              Q = 0.8030
            </span>
          </div>
          <div style="font-family: var(--font-sans); font-size: 38px; font-weight: 800; color: var(--c-text-dark); margin-bottom: 32px;">
            Phi-4-mini <span style="font-size: 24px; font-weight: 600; color: var(--c-gray-text);">(3.8B)</span>
          </div>

          <!-- Barra 1: Sondas trampa -->
          <div style="margin-bottom: 32px;">
            <div style="display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 8px;">
              <span style="font-family: var(--font-sans); font-size: 23px; font-weight: 700; color: var(--c-text-dark);">
                Rechazo en 14 sondas trampa:
              </span>
              <span style="font-family: var(--font-mono); font-size: 40px; font-weight: 800; color: var(--c-red-accent); line-height: 1;">
                28.6%
              </span>
            </div>
            <div style="background: var(--c-border-subtle); height: 26px; width: 100%; margin-bottom: 8px;">
              <div style="width: 28.6%; background: var(--c-red-accent); height: 100%;"></div>
            </div>
            <div style="font-family: var(--font-sans); font-size: 22px; color: var(--c-red-accent); font-weight: 700;">
              Alucina en 10 casos fuera del libro de texto.
            </div>
          </div>

          <!-- Barra 2: Consultas válidas -->
          <div style="margin-bottom: 24px;">
            <div style="display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 8px;">
              <span style="font-family: var(--font-sans); font-size: 23px; font-weight: 700; color: var(--c-text-dark);">
                Falso rechazo en 84 consultas válidas:
              </span>
              <span style="font-family: var(--font-mono); font-size: 40px; font-weight: 800; color: var(--c-wine-primary); line-height: 1;">
                0.0%
              </span>
            </div>
            <div style="background: var(--c-border-subtle); height: 26px; width: 100%; margin-bottom: 8px;">
              <div style="width: 0%; background: var(--c-wine-primary); height: 100%;"></div>
            </div>
            <div style="font-family: var(--font-sans); font-size: 22px; color: var(--c-wine-primary); font-weight: 700;">
              Fluidez total; jamás bloquea al estudiante.
            </div>
          </div>
        </div>

        <!-- Veredicto -->
        <div style="border-top: 2px solid var(--c-border-subtle); padding-top: 18px; margin-top: 10px;">
          <div style="font-family: var(--font-sans); font-size: 24px; font-weight: 700; color: #110103; line-height: 1.35;">
            <strong style="color: var(--c-wine-primary);">Aula asistida:</strong> interacción fluida con docente que supervisa.
          </div>
        </div>
      </div>

      <!-- QWEN2.5-3B -->
      <div style="background: var(--c-pink-bg); border-top: 8px solid var(--c-red-accent); padding: 34px 38px; display: flex; flex-direction: column; justify-content: space-between; box-sizing: border-box;">
        <div>
          <!-- Cabecera -->
          <div style="display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 4px;">
            <span style="font-family: var(--font-mono); font-size: 21px; font-weight: 700; color: var(--c-red-accent); letter-spacing: 2px;">
              PERFIL CONSERVADOR
            </span>
            <span style="font-family: var(--font-mono); font-size: 24px; font-weight: 700; color: var(--c-wine-dark);">
              Q = 0.8010
            </span>
          </div>
          <div style="font-family: var(--font-sans); font-size: 38px; font-weight: 800; color: var(--c-text-dark); margin-bottom: 32px;">
            Qwen2.5-3B <span style="font-size: 24px; font-weight: 600; color: var(--c-gray-text);">(3.1B)</span>
          </div>

          <!-- Barra 1: Sondas trampa -->
          <div style="margin-bottom: 32px;">
            <div style="display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 8px;">
              <span style="font-family: var(--font-sans); font-size: 23px; font-weight: 700; color: var(--c-text-dark);">
                Rechazo en 14 sondas trampa:
              </span>
              <span style="font-family: var(--font-mono); font-size: 40px; font-weight: 800; color: var(--c-wine-primary); line-height: 1;">
                85.7%
              </span>
            </div>
            <div style="background: var(--c-border-subtle); height: 26px; width: 100%; margin-bottom: 8px;">
              <div style="width: 85.7%; background: var(--c-wine-primary); height: 100%;"></div>
            </div>
            <div style="font-family: var(--font-sans); font-size: 22px; color: var(--c-wine-primary); font-weight: 700;">
              Filtro riguroso frente a preguntas trampa.
            </div>
          </div>

          <!-- Barra 2: Consultas válidas -->
          <div style="margin-bottom: 24px;">
            <div style="display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 8px;">
              <span style="font-family: var(--font-sans); font-size: 23px; font-weight: 700; color: var(--c-text-dark);">
                Falso rechazo en 84 consultas válidas:
              </span>
              <span style="font-family: var(--font-mono); font-size: 40px; font-weight: 800; color: var(--c-red-accent); line-height: 1;">
                7.1%
              </span>
            </div>
            <div style="background: var(--c-border-subtle); height: 26px; width: 100%; margin-bottom: 8px;">
              <div style="width: 25%; background: var(--c-red-accent); height: 100%;"></div>
            </div>
            <div style="font-family: var(--font-sans); font-size: 22px; color: var(--c-red-accent); font-weight: 700;">
              Sobre-rechazo; bloquea consultas válidas.
            </div>
          </div>
        </div>

        <!-- Veredicto -->
        <div style="border-top: 2px solid var(--c-border-subtle); padding-top: 18px; margin-top: 10px;">
          <div style="font-family: var(--font-sans); font-size: 24px; font-weight: 700; color: #110103; line-height: 1.35;">
            <strong style="color: var(--c-red-accent);">Autoestudio:</strong> sin docente; prima no inducir al error al alumno.
          </div>
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
'''

HTML_WRAPPER = '''<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Test Slide 14 Final Options</title>
  <link rel="stylesheet" href="http://localhost:8085/styles.css?v=26">
</head>
<body style="margin: 0; padding: 0; background: #0b0103;">

  <div id="presentation-viewport">
    <div id="slides-stage">
      {content}
    </div>
  </div>

</body>
</html>
'''

def main():
    variants = [
        ('slide_14_enfoque_h.html', 'slide_14_enfoque_h.png', HTML_ENFOQUE_H),
        ('slide_14_enfoque_v1.html', 'slide_14_enfoque_v1.png', HTML_ENFOQUE_V1),
    ]

    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(viewport={"width": 1920, "height": 1080})

        for html_name, png_name, content in variants:
            html_path = os.path.join(output_dir, html_name)
            png_path = os.path.join(output_dir, png_name)

            with open(html_path, 'w', encoding='utf-8') as f:
                f.write(HTML_WRAPPER.format(content=content))

            page.goto(f"file:///{html_path.replace(os.sep, '/')}")
            page.wait_for_timeout(400)
            page.screenshot(path=png_path)
            print(f"Captured: {png_name}")

        browser.close()

if __name__ == '__main__':
    main()
