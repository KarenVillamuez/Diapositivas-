# -*- coding: utf-8 -*-
import os
from playwright.sync_api import sync_playwright

output_dir = r"C:\Users\ASUS\.gemini\antigravity-ide\brain\a6624504-511c-4b9d-bc9a-468e348bde40"
os.makedirs(output_dir, exist_ok=True)

# Test 3 variations of the perfectly aligned banner:
# Variant B-Aligned-1: Warm wine background (#F4E8EA), left border 8px wine, matching 290px grid
# Variant B-Aligned-2: Soft rose tint (#F9EFF1), matching 290px grid with pill badge
# Variant B-Aligned-3: Clean card with double border and wine badge

def create_slide(banner_bg, banner_border_left, banner_left_content, banner_border_div):
    return f'''
  <div class="slide-content-area" style="top: 175px; height: 720px; justify-content: space-between;">
    <h2 class="s-lead-question" style="font-size: 38px; font-weight: 800; margin: 0; line-height: 1.2; color: #2C0509;">
      Tres lecciones para la adopción real de tutores de IA en aulas desconectadas
    </h2>

    <div style="display: flex; flex-direction: column; gap: 16px; flex: 1; margin-top: 16px; margin-bottom: 16px;">
      
      <!-- Fila 1: Factibilidad Técnica -->
      <div style="background: #FAF5F5; border-left: 8px solid var(--c-wine-primary); padding: 22px 36px; display: grid; grid-template-columns: 290px 1fr; gap: 32px; align-items: center; flex: 1;">
        <div style="border-right: 2px solid #E2D2D2; padding-right: 24px; text-align: center;">
          <div style="font-family: var(--font-mono); font-size: 15px; font-weight: 800; color: var(--c-wine-primary); letter-spacing: 1.5px; margin-bottom: 2px;">
            01 · FACTIBILIDAD
          </div>
          <div style="font-family: var(--font-mono); font-size: 56px; font-weight: 900; color: var(--c-wine-primary); line-height: 1;">
            100%
          </div>
          <div style="font-family: var(--font-mono); font-size: 14px; font-weight: 800; color: #5D4A4D; margin-top: 4px; letter-spacing: 0.5px;">
            USB OFFLINE SIN GPU
          </div>
        </div>
        <div>
          <div style="font-family: var(--font-sans); font-size: 32px; font-weight: 900; color: #110103; margin-bottom: 6px;">
            Hardware Escolar Común (CPU sin GPU)
          </div>
          <div style="font-family: var(--font-sans); font-size: 27px; color: #222; line-height: 1.35; font-weight: 600;">
            RAG portátil que genera <strong>1.9 tokens/s</strong> en un Core i5 de aula, cerrando la brecha rural sin requerir internet ni pagos en la nube.
          </div>
        </div>
      </div>

      <!-- Fila 2: Rigor Metodológico -->
      <div style="background: #FAF5F5; border-left: 8px solid #B38600; padding: 22px 36px; display: grid; grid-template-columns: 290px 1fr; gap: 32px; align-items: center; flex: 1;">
        <div style="border-right: 2px solid #E2D2D2; padding-right: 24px; text-align: center;">
          <div style="font-family: var(--font-mono); font-size: 15px; font-weight: 800; color: #8A6700; letter-spacing: 1.5px; margin-bottom: 2px;">
            02 · METODOLOGÍA
          </div>
          <div style="font-family: var(--font-mono); font-size: 56px; font-weight: 900; color: #B38600; line-height: 1;">
            ≥ 4
          </div>
          <div style="font-family: var(--font-mono); font-size: 14px; font-weight: 800; color: #5D4A4D; margin-top: 4px; letter-spacing: 0.5px;">
            RÉPLICAS ESTOCÁSTICAS
          </div>
        </div>
        <div>
          <div style="font-family: var(--font-sans); font-size: 32px; font-weight: 900; color: #110103; margin-bottom: 6px;">
            Control de Variabilidad Estocástica
          </div>
          <div style="font-family: var(--font-sans); font-size: 27px; color: #222; line-height: 1.35; font-weight: 600;">
            Una sola corrida carece de validez científica. La <strong>alta dispersión de los SLM</strong> exige semillas múltiples como nuevo estándar.
          </div>
        </div>
      </div>

      <!-- Fila 3: Soberanía Pedagógica -->
      <div style="background: #FAF5F5; border-left: 8px solid var(--c-red-accent); padding: 22px 36px; display: grid; grid-template-columns: 290px 1fr; gap: 32px; align-items: center; flex: 1;">
        <div style="border-right: 2px solid #E2D2D2; padding-right: 24px; text-align: center;">
          <div style="font-family: var(--font-mono); font-size: 15px; font-weight: 800; color: var(--c-red-accent); letter-spacing: 1.5px; margin-bottom: 2px;">
            03 · DOCENCIA
          </div>
          <div style="font-family: var(--font-mono); font-size: 42px; font-weight: 900; color: var(--c-red-accent); line-height: 1; letter-spacing: -0.5px; white-space: nowrap;">
            κ = -0.429
          </div>
          <div style="font-family: var(--font-mono); font-size: 14px; font-weight: 800; color: #5D4A4D; margin-top: 4px; letter-spacing: 0.5px;">
            DESACUERDO EN AULA
          </div>
        </div>
        <div>
          <div style="font-family: var(--font-sans); font-size: 32px; font-weight: 900; color: #110103; margin-bottom: 6px;">
            El Docente en el Centro del Diseño
          </div>
          <div style="font-family: var(--font-sans); font-size: 27px; color: #222; line-height: 1.35; font-weight: 600;">
            El algoritmo mide apego textual, no pedagogía. La <strong>calibración por profesores en contexto real</strong> es insustituible para evitar falsedades.
          </div>
        </div>
      </div>

    </div>

    <!-- Banner Tesis Defendida con perfecta alineación geométrica -->
    <div style="background: {banner_bg}; border-left: 8px solid {banner_border_left}; padding: 18px 36px; display: grid; grid-template-columns: 290px 1fr; gap: 32px; align-items: center; border-radius: 2px; border-top: 1px solid rgba(107, 29, 47, 0.12); border-right: 1px solid rgba(107, 29, 47, 0.12); border-bottom: 1px solid rgba(107, 29, 47, 0.12);">
      <div style="border-right: 2px solid {banner_border_div}; padding-right: 24px; text-align: center;">
        {banner_left_content}
      </div>
      <div style="font-family: var(--font-sans); font-size: 27px; color: #110103; line-height: 1.35; font-weight: 700;">
        Democratizar la IA educativa rural mediante hardware común, sin transferir jamás la soberanía pedagógica a los algoritmos.
      </div>
    </div>
  </div>
'''

HTML_PAGE = '''<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <title>Slide 18 Alignment Tests</title>
  <link rel="stylesheet" href="http://localhost:8085/styles.css?v=33">
</head>
<body style="margin: 0; padding: 0; background: #0b0103;">
  <div id="presentation-viewport">
    <div id="slides-stage">
      <section class="slide s-white active">
        <header class="slide-header">
          <div class="sh-left">
            <span class="sh-red-bar"></span>
            <span class="sh-category">04 · CONCLUSIONES Y APORTES</span>
          </div>
          <img src="http://localhost:8085/assets/image6.png" alt="#LoxTIC" class="sh-loxtic">
        </header>
        <div class="sh-divider"></div>
        {content}
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
    left_content_1 = '''
      <div style="font-family: var(--font-mono); font-size: 15px; font-weight: 900; color: var(--c-wine-primary); letter-spacing: 1.5px; margin-bottom: 2px;">
        TESIS DEFENDIDA
      </div>
      <div style="font-family: var(--font-mono); font-size: 22px; font-weight: 900; color: #2C0509; letter-spacing: 0.5px;">
        APORTE CENTRAL
      </div>
    '''

    left_content_2 = '''
      <span style="background: var(--c-wine-primary); color: #FFFFFF; font-family: var(--font-mono); font-size: 15px; font-weight: 800; letter-spacing: 1px; padding: 8px 18px; border-radius: 4px; display: inline-block;">
        TESIS DEFENDIDA
      </span>
    '''

    left_content_3 = '''
      <div style="font-family: var(--font-mono); font-size: 16px; font-weight: 900; color: #C51625; letter-spacing: 1.5px; margin-bottom: 2px;">
        SÍNTESIS FINAL
      </div>
      <div style="font-family: var(--font-sans); font-size: 20px; font-weight: 800; color: #110103;">
        Tesis de la Ponencia
      </div>
    '''

    variations = [
        ("slide18_aligned_v1_vinosuave", create_slide("#F4E8EA", "var(--c-wine-primary)", left_content_1, "#D8B8BE")),
        ("slide18_aligned_v2_badgewine", create_slide("#FAF2F3", "var(--c-wine-primary)", left_content_2, "#E2C6CC")),
        ("slide18_aligned_v3_rojoacento", create_slide("#FDF6F6", "var(--c-red-accent)", left_content_3, "#E8D0D0")),
    ]

    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(viewport={"width": 1920, "height": 1080})

        for name, content in variations:
            html = HTML_PAGE.format(content=content)
            tmp_html = os.path.join(output_dir, f"{name}.html")
            tmp_png = os.path.join(output_dir, f"{name}.png")
            with open(tmp_html, "w", encoding="utf-8") as f:
                f.write(html)
            page.goto(f"file:///{tmp_html.replace(os.sep, '/')}")
            page.wait_for_timeout(400)
            page.screenshot(path=tmp_png)
            print(f"Generated {name}.png")

        browser.close()

if __name__ == '__main__':
    main()
