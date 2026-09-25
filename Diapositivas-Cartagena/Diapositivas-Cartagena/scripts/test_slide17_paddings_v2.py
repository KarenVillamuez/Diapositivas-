# -*- coding: utf-8 -*-
import os
from playwright.sync_api import sync_playwright

output_dir = r"C:\Users\ASUS\.gemini\antigravity-ide\brain\a6624504-511c-4b9d-bc9a-468e348bde40"
os.makedirs(output_dir, exist_ok=True)

# We will test 3 padding variations:
# V1: grid-template-columns: 1fr 240px; card padding 26px 36px; right col border-left with equal visual margins
# V2: grid-template-columns: 1fr auto; flex metric with explicit padding
# V3: grid-template-columns: 1fr 250px; font-size 58px; generous breathing room

def get_slide_html(col_spec, card_pad, metric_style, font_size_pct, font_size_num, label_size="13px"):
    return f'''
    <h2 class="s-lead-question" style="font-size: 38px; font-weight: 800; margin: 0; line-height: 1.2; color: #2C0509;">
      Apego al texto no es aprendizaje: criterios para auditar y desplegar tutores
    </h2>

    <div style="display: grid; grid-template-columns: 1fr 1fr; grid-template-rows: 1fr 1fr; gap: 24px; flex: 1; margin-top: 14px;">
      
      <!-- Cuadrante 1: Diagnóstico Metodológico (Rojo Alerta) -->
      <div style="background: #FAF5F5; border-top: 8px solid #C51625; padding: {card_pad}; display: grid; grid-template-columns: {col_spec}; gap: 28px; align-items: center;">
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
        <div style="{metric_style}">
          <div style="font-family: var(--font-mono); font-size: {font_size_pct}; font-weight: 900; color: #C51625; line-height: 1; letter-spacing: -1px;">0.795</div>
          <div style="font-family: var(--font-mono); font-size: {label_size}; font-weight: 800; color: #5D4A4D; margin-top: 8px; letter-spacing: 0.5px; white-space: nowrap;">APEGO ENGAÑOSO</div>
        </div>
      </div>

      <!-- Cuadrante 2: Protocolo de Evaluación (Gris Pizarra Neutral) -->
      <div style="background: #FAF5F5; border-top: 8px solid #4A3B3D; padding: {card_pad}; display: grid; grid-template-columns: {col_spec}; gap: 28px; align-items: center;">
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
        <div style="{metric_style}">
          <div style="font-family: var(--font-mono); font-size: {font_size_num}; font-weight: 900; color: #4A3B3D; line-height: 1;">3</div>
          <div style="font-family: var(--font-mono); font-size: {label_size}; font-weight: 800; color: #5D4A4D; margin-top: 8px; letter-spacing: 0.5px; white-space: nowrap;">DIMENSIONES</div>
        </div>
      </div>

      <!-- Cuadrante 3: Despliegue Autoestudio (Vino Institucional Qwen) -->
      <div style="background: #FAF5F5; border-top: 8px solid var(--c-wine-primary); padding: {card_pad}; display: grid; grid-template-columns: {col_spec}; gap: 28px; align-items: center;">
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
        <div style="{metric_style}">
          <div style="font-family: var(--font-mono); font-size: {font_size_pct}; font-weight: 900; color: var(--c-wine-primary); line-height: 1; letter-spacing: -1px;">85.7%</div>
          <div style="font-family: var(--font-mono); font-size: {label_size}; font-weight: 800; color: var(--c-wine-primary); margin-top: 8px; letter-spacing: 0.5px; white-space: nowrap;">RECHAZO CERTERO</div>
        </div>
      </div>

      <!-- Cuadrante 4: Despliegue Aula Asistida (Rojo Acento Phi) -->
      <div style="background: #FAF5F5; border-top: 8px solid var(--c-red-accent); padding: {card_pad}; display: grid; grid-template-columns: {col_spec}; gap: 28px; align-items: center;">
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
        <div style="{metric_style}">
          <div style="font-family: var(--font-mono); font-size: {font_size_pct}; font-weight: 900; color: var(--c-red-accent); line-height: 1; letter-spacing: -1px;">0.0%</div>
          <div style="font-family: var(--font-mono); font-size: {label_size}; font-weight: 800; color: var(--c-red-accent); margin-top: 8px; letter-spacing: 0.5px; white-space: nowrap;">BLOQUEOS DIÁLOGO</div>
        </div>
      </div>

    </div>
    '''

HTML_PAGE = '''<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <title>Padding Test Variations</title>
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
    variations = [
        # Option V1: 240px col, 58px font, border-left: 2px solid #E5D5D5, padding-left: 24px, padding-right: 0, card-padding: 26px 40px
        {
            "name": "var_paddings_v1",
            "col_spec": "1fr 230px",
            "card_pad": "26px 36px",
            "metric_style": "border-left: 2px solid #E5D5D5; padding-left: 20px; padding-right: 4px; text-align: center; display: flex; flex-direction: column; align-items: center; justify-content: center;",
            "font_size_pct": "56px",
            "font_size_num": "56px",
            "label_size": "13px"
        },
        # Option V2: 250px col, 58px font, perfectly balanced padding inside metric block
        {
            "name": "var_paddings_v2",
            "col_spec": "1fr 250px",
            "card_pad": "26px 34px",
            "metric_style": "border-left: 2px solid #E5D5D5; padding-left: 24px; padding-right: 10px; text-align: center; display: flex; flex-direction: column; align-items: center; justify-content: center;",
            "font_size_pct": "58px",
            "font_size_num": "58px",
            "label_size": "13px"
        },
        # Option V3: 260px col, card padding: 26px 32px, metric font 58px, letter-spacing -1.5px, generous margins all around
        {
            "name": "var_paddings_v3",
            "col_spec": "1fr 255px",
            "card_pad": "26px 32px",
            "metric_style": "border-left: 2px solid #E5D5D5; padding-left: 24px; text-align: center; display: flex; flex-direction: column; align-items: center; justify-content: center;",
            "font_size_pct": "58px",
            "font_size_num": "60px",
            "label_size": "13px"
        },
    ]

    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(viewport={"width": 1920, "height": 1080})

        for v in variations:
            content = get_slide_html(
                col_spec=v["col_spec"],
                card_pad=v["card_pad"],
                metric_style=v["metric_style"],
                font_size_pct=v["font_size_pct"],
                font_size_num=v["font_size_num"],
                label_size=v["label_size"]
            )
            html = HTML_PAGE.format(content=content)
            tmp_html = os.path.join(output_dir, f"{v['name']}.html")
            tmp_png = os.path.join(output_dir, f"{v['name']}.png")
            with open(tmp_html, "w", encoding="utf-8") as f:
                f.write(html)
            page.goto(f"file:///{tmp_html.replace(os.sep, '/')}")
            page.wait_for_timeout(350)
            page.screenshot(path=tmp_png)
            print(f"Generated {v['name']}.png")

        browser.close()

if __name__ == '__main__':
    main()
