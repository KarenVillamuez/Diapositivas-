# -*- coding: utf-8 -*-
import os
from playwright.sync_api import sync_playwright

output_dir = r"C:\Users\ASUS\.gemini\antigravity-ide\brain\a6624504-511c-4b9d-bc9a-468e348bde40"
os.makedirs(output_dir, exist_ok=True)

# Título ajustado a 37px (1 sola línea limpia) o 2 líneas balanceadas
HTML_TITLE_1L = '''
<section class="slide s-white active" id="slide-14-3m-1l">
  <header class="slide-header">
    <div class="sh-left">
      <span class="sh-red-bar"></span>
      <span class="sh-category">03 · RESULTADOS · MODOS DE FALLO ASIMÉTRICOS</span>
    </div>
    <img src="http://localhost:8085/assets/image6.png" alt="#LoxTIC" class="sh-loxtic">
  </header>
  <div class="sh-divider"></div>

  <div class="slide-content-area" style="justify-content: flex-start;">
    
    <h2 class="s-lead-question" style="font-size: 38px; font-weight: 800; margin-bottom: 22px; line-height: 1.2; color: var(--c-text-dark); white-space: nowrap;">
      Alucinación frente a sobre-rechazo: cómo fallan dos modelos con la misma nota
    </h2>

    <!-- GRID DÍPTICO 2 COLUMNAS -->
    <div class="grid-2col" style="gap: 36px; align-items: stretch; height: 650px;">
      
      <!-- COLUMNA 1: PHI-4-MINI (PERFIL PERMISIVO) -->
      <div style="background: var(--c-pink-bg); border-top: 8px solid var(--c-wine-primary); padding: 24px 30px; display: flex; flex-direction: column; justify-content: space-between; box-sizing: border-box;">
        
        <div>
          <!-- Cabecera de Columna -->
          <div style="display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 6px;">
            <span style="font-family: var(--font-mono); font-size: 20px; font-weight: 700; color: var(--c-wine-primary); letter-spacing: 2px;">
              PERFIL PERMISIVO · FLUIDEZ
            </span>
            <span style="font-family: var(--font-mono); font-size: 24px; font-weight: 800; color: var(--c-wine-dark);">
              NOTA Q = 0.8030
            </span>
          </div>

          <div style="font-family: var(--font-sans); font-size: 36px; font-weight: 800; color: var(--c-text-dark); margin-bottom: 20px;">
            Phi-4-mini <span style="font-size: 24px; font-weight: 600; color: var(--c-gray-text);">(3.8B · Microsoft)</span>
          </div>

          <!-- Métrica 1: Sondas Trampa -->
          <div style="margin-bottom: 18px;">
            <div style="display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 5px;">
              <span style="font-family: var(--font-sans); font-size: 22px; font-weight: 700; color: var(--c-text-dark);">
                Rechazo certero (14 sondas trampa):
              </span>
              <span style="font-family: var(--font-mono); font-size: 34px; font-weight: 800; color: var(--c-red-accent);">
                28.6% <span style="font-size: 19px; font-weight: 700; color: var(--c-gray-text);">(4/14)</span>
              </span>
            </div>
            <div style="background: var(--c-border-subtle); height: 12px; width: 100%; margin-bottom: 6px;">
              <div style="width: 28.6%; background: var(--c-red-accent); height: 100%;"></div>
            </div>
            <div style="font-family: var(--font-sans); font-size: 21px; color: var(--c-red-accent); font-weight: 700;">
              Alucina en 10 casos fuera del libro de texto.
            </div>
          </div>

          <!-- Métrica 2: Consultas Válidas -->
          <div style="margin-bottom: 18px;">
            <div style="display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 5px;">
              <span style="font-family: var(--font-sans); font-size: 22px; font-weight: 700; color: var(--c-text-dark);">
                Falso rechazo (84 consultas válidas):
              </span>
              <span style="font-family: var(--font-mono); font-size: 34px; font-weight: 800; color: var(--c-wine-primary);">
                0.0% <span style="font-size: 19px; font-weight: 700; color: var(--c-gray-text);">(0/84)</span>
              </span>
            </div>
            <div style="background: var(--c-border-subtle); height: 12px; width: 100%; margin-bottom: 6px;">
              <div style="width: 0%; background: var(--c-wine-primary); height: 100%;"></div>
            </div>
            <div style="font-family: var(--font-sans); font-size: 21px; color: var(--c-wine-primary); font-weight: 700;">
              Fluidez total; jamás bloquea preguntas curriculares.
            </div>
          </div>

          <!-- Métrica 3: Fallback Global -->
          <div style="margin-bottom: 10px;">
            <div style="display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 5px;">
              <span style="font-family: var(--font-sans); font-size: 22px; font-weight: 700; color: var(--c-text-dark);">
                Tasa de repliegue / silencio global:
              </span>
              <span style="font-family: var(--font-mono); font-size: 34px; font-weight: 800; color: var(--c-wine-dark);">
                4.1% <span style="font-size: 19px; font-weight: 700; color: var(--c-gray-text);">(4/98)</span>
              </span>
            </div>
            <div style="background: var(--c-border-subtle); height: 12px; width: 100%; margin-bottom: 6px;">
              <div style="width: 4.1%; background: var(--c-wine-dark); height: 100%;"></div>
            </div>
            <div style="font-family: var(--font-sans); font-size: 21px; color: var(--c-gray-text); font-weight: 600;">
              Casi nunca se silencia; responde siempre arriesgando error.
            </div>
          </div>

        </div>

        <!-- Veredicto Pedagógico Dignificado -->
        <div class="card-conclusion-row" style="margin-top: 10px; padding-top: 14px;">
          <div style="font-family: var(--font-mono); font-size: 19px; font-weight: 700; color: var(--c-wine-primary); letter-spacing: 1.5px; margin-bottom: 4px; text-transform: uppercase;">
            Veredicto Pedagógico
          </div>
          <div style="font-family: var(--font-sans); font-size: 23px; font-weight: 700; color: #110103; line-height: 1.35;">
            Aula asistida: el docente modera y corrige alucinaciones, aprovechando una conversación sin trabas.
          </div>
        </div>

      </div>

      <!-- COLUMNA 2: QWEN2.5-3B (PERFIL CONSERVADOR) -->
      <div style="background: var(--c-pink-bg); border-top: 8px solid var(--c-red-accent); padding: 24px 30px; display: flex; flex-direction: column; justify-content: space-between; box-sizing: border-box;">
        
        <div>
          <!-- Cabecera de Columna -->
          <div style="display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 6px;">
            <span style="font-family: var(--font-mono); font-size: 20px; font-weight: 700; color: var(--c-red-accent); letter-spacing: 2px;">
              PERFIL CONSERVADOR · SEGURIDAD
            </span>
            <span style="font-family: var(--font-mono); font-size: 24px; font-weight: 800; color: var(--c-wine-dark);">
              NOTA Q = 0.8010
            </span>
          </div>

          <div style="font-family: var(--font-sans); font-size: 36px; font-weight: 800; color: var(--c-text-dark); margin-bottom: 20px;">
            Qwen2.5-3B <span style="font-size: 24px; font-weight: 600; color: var(--c-gray-text);">(3.1B · Alibaba)</span>
          </div>

          <!-- Métrica 1: Sondas Trampa -->
          <div style="margin-bottom: 18px;">
            <div style="display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 5px;">
              <span style="font-family: var(--font-sans); font-size: 22px; font-weight: 700; color: var(--c-text-dark);">
                Rechazo certero (14 sondas trampa):
              </span>
              <span style="font-family: var(--font-mono); font-size: 34px; font-weight: 800; color: var(--c-wine-primary);">
                85.7% <span style="font-size: 19px; font-weight: 700; color: var(--c-gray-text);">(12/14)</span>
              </span>
            </div>
            <div style="background: var(--c-border-subtle); height: 12px; width: 100%; margin-bottom: 6px;">
              <div style="width: 85.7%; background: var(--c-wine-primary); height: 100%;"></div>
            </div>
            <div style="font-family: var(--font-sans); font-size: 21px; color: var(--c-wine-primary); font-weight: 700;">
              Filtro estricto; bloquea preguntas fuera del libro.
            </div>
          </div>

          <!-- Métrica 2: Consultas Válidas -->
          <div style="margin-bottom: 18px;">
            <div style="display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 5px;">
              <span style="font-family: var(--font-sans); font-size: 22px; font-weight: 700; color: var(--c-text-dark);">
                Falso rechazo (84 consultas válidas):
              </span>
              <span style="font-family: var(--font-mono); font-size: 34px; font-weight: 800; color: var(--c-red-accent);">
                7.1% <span style="font-size: 19px; font-weight: 700; color: var(--c-gray-text);">(6/84)</span>
              </span>
            </div>
            <div style="background: var(--c-border-subtle); height: 12px; width: 100%; margin-bottom: 6px;">
              <div style="width: 25%; background: var(--c-red-accent); height: 100%;"></div>
            </div>
            <div style="font-family: var(--font-sans); font-size: 21px; color: var(--c-red-accent); font-weight: 700;">
              Sobre-rechazo; bloquea al alumno en consultas válidas.
            </div>
          </div>

          <!-- Métrica 3: Fallback Global -->
          <div style="margin-bottom: 10px;">
            <div style="display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 5px;">
              <span style="font-family: var(--font-sans); font-size: 22px; font-weight: 700; color: var(--c-text-dark);">
                Tasa de repliegue / silencio global:
              </span>
              <span style="font-family: var(--font-mono); font-size: 34px; font-weight: 800; color: var(--c-wine-dark);">
                18.4% <span style="font-size: 19px; font-weight: 700; color: var(--c-gray-text);">(18/98)</span>
              </span>
            </div>
            <div style="background: var(--c-border-subtle); height: 12px; width: 100%; margin-bottom: 6px;">
              <div style="width: 18.4%; background: var(--c-wine-dark); height: 100%;"></div>
            </div>
            <div style="font-family: var(--font-sans); font-size: 21px; color: var(--c-gray-text); font-weight: 600;">
              Repliegue frecuente; 4.5× más cauto ante la duda.
            </div>
          </div>

        </div>

        <!-- Veredicto Pedagógico Dignificado -->
        <div class="card-conclusion-row verdict-red" style="margin-top: 10px; padding-top: 14px;">
          <div style="font-family: var(--font-mono); font-size: 19px; font-weight: 700; color: var(--c-red-accent); letter-spacing: 1.5px; margin-bottom: 4px; text-transform: uppercase;">
            Veredicto Pedagógico
          </div>
          <div style="font-family: var(--font-sans); font-size: 23px; font-weight: 700; color: #110103; line-height: 1.35;">
            Autoestudio: sin docente, prima la certeza absoluta de no inducir al error al alumno autónomo.
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
  <title>Test Slide 14 Opcion 2 1-Line Title</title>
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
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(viewport={"width": 1920, "height": 1080})

        html_path = os.path.join(output_dir, 'slide_14_v2_clean.html')
        png_path = os.path.join(output_dir, 'slide_14_v2_clean.png')

        with open(html_path, 'w', encoding='utf-8') as f:
            f.write(HTML_WRAPPER.format(content=HTML_TITLE_1L))

        page.goto(f"file:///{html_path.replace(os.sep, '/')}")
        page.wait_for_timeout(400)
        page.screenshot(path=png_path)
        print("Captured: slide_14_v2_clean.png")

        browser.close()

if __name__ == '__main__':
    main()
