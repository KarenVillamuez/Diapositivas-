# -*- coding: utf-8 -*-
import os
from playwright.sync_api import sync_playwright

output_dir = r"C:\Users\ASUS\.gemini\antigravity-ide\brain\a6624504-511c-4b9d-bc9a-468e348bde40"
os.makedirs(output_dir, exist_ok=True)

ROWS_HTML = '''
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
'''

# Ribbon Variant R1: Cinta Cápsula con Badge Sólido Vino (#FAF2F3 + border-radius 8px)
RIBBON_R1 = '''
    <div style="background: #FAF2F3; border: 1.5px solid #E6CCD1; border-radius: 8px; padding: 18px 34px; display: flex; align-items: center; gap: 26px;">
      <div style="background: var(--c-wine-primary); color: #FFFFFF; font-family: var(--font-mono); font-size: 15px; font-weight: 800; letter-spacing: 1.2px; padding: 8px 18px; border-radius: 5px; white-space: nowrap; flex-shrink: 0;">
        TESIS DEFENDIDA
      </div>
      <div style="font-family: var(--font-sans); font-size: 27px; color: #110103; line-height: 1.35; font-weight: 600;">
        <strong>Democratizar la IA educativa rural</strong> mediante hardware común, sin transferir jamás la <strong>soberanía pedagógica</strong> a los algoritmos.
      </div>
    </div>
'''

# Ribbon Variant R2: Cinta Editorial con Etiqueta Tipográfica y Separador Vertical Fino (sin badge sólido)
RIBBON_R2 = '''
    <div style="background: #FAF2F3; border: 1.5px solid #E6CCD1; border-radius: 8px; padding: 18px 34px; display: flex; align-items: center; gap: 28px;">
      <div style="display: flex; flex-direction: column; align-items: flex-start; white-space: nowrap; flex-shrink: 0;">
        <span style="font-family: var(--font-mono); font-size: 13px; font-weight: 800; color: var(--c-wine-primary); letter-spacing: 1.5px;">APORTE CENTRAL</span>
        <span style="font-family: var(--font-sans); font-size: 24px; font-weight: 900; color: #110103; line-height: 1.1; margin-top: 2px;">Tesis Defendida</span>
      </div>
      <div style="width: 2px; height: 42px; background: #D8B8BE; flex-shrink: 0;"></div>
      <div style="font-family: var(--font-sans); font-size: 27px; color: #110103; line-height: 1.35; font-weight: 600;">
        <strong>Democratizar la IA educativa rural</strong> mediante hardware común, sin transferir jamás la <strong>soberanía pedagógica</strong> a los algoritmos.
      </div>
    </div>
'''

# Ribbon Variant R3: Cinta con Acento de Borde Superior Vino (Subtle Top Bar)
RIBBON_R3 = '''
    <div style="background: #FAF5F5; border-top: 4px solid var(--c-wine-primary); border-left: 1px solid #E2D2D2; border-right: 1px solid #E2D2D2; border-bottom: 1px solid #E2D2D2; border-radius: 0 0 6px 6px; padding: 18px 34px; display: flex; align-items: center; gap: 26px;">
      <div style="background: var(--c-wine-primary); color: #FFFFFF; font-family: var(--font-mono); font-size: 14px; font-weight: 800; letter-spacing: 1.2px; padding: 7px 16px; border-radius: 4px; white-space: nowrap; flex-shrink: 0;">
        TESIS DEFENDIDA
      </div>
      <div style="font-family: var(--font-sans); font-size: 27px; color: #110103; line-height: 1.35; font-weight: 600;">
        <strong>Democratizar la IA educativa rural</strong> mediante hardware común, sin transferir jamás la <strong>soberanía pedagógica</strong> a los algoritmos.
      </div>
    </div>
'''

def build_html(ribbon):
    return f'''
  <div class="slide-content-area" style="top: 175px; height: 720px; justify-content: space-between;">
    <h2 class="s-lead-question" style="font-size: 38px; font-weight: 800; margin: 0; line-height: 1.2; color: #2C0509;">
      Tres lecciones para la adopción real de tutores de IA en aulas desconectadas
    </h2>

    <div style="display: flex; flex-direction: column; gap: 18px; flex: 1; margin-top: 16px; margin-bottom: 18px;">
      {ROWS_HTML}
    </div>

    {ribbon}
  </div>
'''

HTML_PAGE = '''<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <title>Slide 18 Ribbon Variants</title>
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
    variants = [
        ("slide18_r1_badge_solido", build_html(RIBBON_R1)),
        ("slide18_r2_etiqueta_tipografica", build_html(RIBBON_R2)),
        ("slide18_r3_borde_superior", build_html(RIBBON_R3)),
    ]

    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(viewport={"width": 1920, "height": 1080})

        for name, content in variants:
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
