# -*- coding: utf-8 -*-
import os
from playwright.sync_api import sync_playwright

output_dir = r"C:\Users\ASUS\.gemini\antigravity-ide\brain\a6624504-511c-4b9d-bc9a-468e348bde40"
os.makedirs(output_dir, exist_ok=True)

# Base 3 lessons (Rows 1, 2, 3) - unchanged, these are the 3 clear lessons:
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

# Treatment 1: Cinta Horizontal con Badge Vino + Borde Completo Delicado (Cero border-left, Cero columna 290px)
# Visualmente es una "cinta resumen" que abraza las 3 lecciones.
BANNER_T1 = '''
    <div style="background: #FAF2F3; border: 1.5px solid #E6CCD1; border-radius: 8px; padding: 16px 32px; display: flex; align-items: center; gap: 24px;">
      <div style="background: var(--c-wine-primary); color: #FFFFFF; font-family: var(--font-mono); font-size: 14px; font-weight: 800; letter-spacing: 1.2px; padding: 8px 18px; border-radius: 5px; white-space: nowrap;">
        TESIS DEFENDIDA
      </div>
      <div style="font-family: var(--font-sans); font-size: 26px; color: #110103; line-height: 1.35; font-weight: 600;">
        <strong>Democratizar la IA educativa rural</strong> mediante hardware común, sin transferir jamás la <strong>soberanía pedagógica</strong> a los algoritmos.
      </div>
    </div>
'''

# Treatment 2: Franja Editorial Abierta con Línea Superior (Swiss Quote style)
# Sin caja cerrada ni border-left: una regla horizontal que separa las 3 lecciones de la tesis global.
BANNER_T2 = '''
    <div style="border-top: 2.5px solid #D8B8BE; padding-top: 16px; padding-bottom: 4px; padding-left: 10px; padding-right: 10px; display: flex; align-items: baseline; gap: 24px;">
      <div style="font-family: var(--font-mono); font-size: 16px; font-weight: 900; color: var(--c-wine-primary); letter-spacing: 1.5px; white-space: nowrap;">
        TESIS DEFENDIDA ·
      </div>
      <div style="font-family: var(--font-sans); font-size: 27px; color: #110103; line-height: 1.35; font-weight: 600;">
        <strong>Democratizar la IA educativa rural</strong> mediante hardware común, sin transferir jamás la <strong>soberanía pedagógica</strong> a los algoritmos.
      </div>
    </div>
'''

# Treatment 3: Cintillo de Conclusión con Acento Superior (Borde Arriba Vino 4px, fondo suave, sin bordes laterales)
BANNER_T3 = '''
    <div style="background: #F8ECEE; border-top: 4px solid var(--c-wine-primary); padding: 18px 34px; display: flex; align-items: center; gap: 24px; border-radius: 0 0 6px 6px;">
      <div style="display: flex; flex-direction: column; align-items: flex-start; white-space: nowrap;">
        <span style="font-family: var(--font-mono); font-size: 13px; font-weight: 800; color: #6E5357; letter-spacing: 1px;">SÍNTESIS DE LA PONENCIA</span>
        <span style="font-family: var(--font-sans); font-size: 22px; font-weight: 900; color: var(--c-wine-primary); margin-top: 2px;">Tesis Defendida</span>
      </div>
      <div style="width: 2px; height: 42px; background: #D8B8BE;"></div>
      <div style="font-family: var(--font-sans); font-size: 26px; color: #110103; line-height: 1.35; font-weight: 600;">
        <strong>Democratizar la IA educativa rural</strong> mediante hardware común, sin transferir jamás la <strong>soberanía pedagógica</strong> a los algoritmos.
      </div>
    </div>
'''

# Treatment 4: Placa Elegante con Borde Dorado Superior (El estándar del oro de conclusiones)
BANNER_T4 = '''
    <div style="background: #FAF7EF; border-top: 4px solid #B38600; border-radius: 0 0 6px 6px; padding: 18px 34px; display: flex; align-items: center; gap: 24px;">
      <div style="background: #B38600; color: #FFFFFF; font-family: var(--font-mono); font-size: 14px; font-weight: 900; letter-spacing: 1px; padding: 6px 16px; border-radius: 4px; white-space: nowrap;">
        APORTE CENTRAL
      </div>
      <div style="font-family: var(--font-sans); font-size: 26px; color: #110103; line-height: 1.35; font-weight: 600;">
        <strong>Democratizar la IA educativa rural</strong> mediante hardware común, sin transferir jamás la <strong>soberanía pedagógica</strong> a los algoritmos.
      </div>
    </div>
'''

def build_full_html(banner_html):
    return f'''
  <div class="slide-content-area" style="top: 175px; height: 720px; justify-content: space-between;">
    <h2 class="s-lead-question" style="font-size: 38px; font-weight: 800; margin: 0; line-height: 1.2; color: #2C0509;">
      Tres lecciones para la adopción real de tutores de IA en aulas desconectadas
    </h2>

    <div style="display: flex; flex-direction: column; gap: 18px; flex: 1; margin-top: 16px; margin-bottom: 18px;">
      {ROWS_HTML}
    </div>

    {banner_html}
  </div>
'''

HTML_PAGE = '''<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <title>Slide 18 Distinct Thesis Treatments</title>
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
        ("slide18_t1_cintabadge", build_full_html(BANNER_T1)),
        ("slide18_t2_reglaabierta", build_full_html(BANNER_T2)),
        ("slide18_t3_bordesuperior", build_full_html(BANNER_T3)),
        ("slide18_t4_oroplaca", build_full_html(BANNER_T4)),
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
