# -*- coding: utf-8 -*-
import os
from playwright.sync_api import sync_playwright

output_dir = r"C:\Users\ASUS\.gemini\antigravity-ide\brain\a6624504-511c-4b9d-bc9a-468e348bde40"

# Compare:
# Test A: current divider height (auto on flex, ~82px)
# Test B: divider with height: 120px; align-self: center (clean vertical accent rule)
# Test C: divider with height: 140px

def build_card(border_color, cat_num, cat_title, card_title, body_text, metric_val, metric_label, div_height=None, font_sz="58px"):
    h_style = f"height: {div_height};" if div_height else ""
    return f'''
      <div style="background: #FAF5F5; border-top: 8px solid {border_color}; padding: 26px 36px; display: grid; grid-template-columns: 1fr 245px; gap: 28px; align-items: center;">
        <div>
          <div style="font-family: var(--font-mono); font-size: 15px; font-weight: 800; color: {border_color}; letter-spacing: 1.5px; margin-bottom: 4px;">
            {cat_num} · {cat_title}
          </div>
          <div style="font-family: var(--font-sans); font-size: 34px; font-weight: 900; color: #110103; margin-bottom: 10px;">
            {card_title}
          </div>
          <div style="font-family: var(--font-sans); font-size: 26px; color: #110103; line-height: 1.35; font-weight: 600;">
            {body_text}
          </div>
        </div>
        <div style="border-left: 2px solid #E2D2D2; padding-left: 24px; padding-right: 8px; text-align: center; display: flex; flex-direction: column; align-items: center; justify-content: center; {h_style}">
          <div style="font-family: var(--font-mono); font-size: {font_sz}; font-weight: 900; color: {border_color}; line-height: 1; letter-spacing: -1px;">{metric_val}</div>
          <div style="font-family: var(--font-mono); font-size: 13px; font-weight: 800; color: {border_color if '%' in metric_val else '#5D4A4D'}; margin-top: 8px; letter-spacing: 0.5px; white-space: nowrap;">{metric_label}</div>
        </div>
      </div>
    '''

def get_grid(div_h=None, font_sz="58px"):
    c1 = build_card("#C51625", "01", "EL RIESGO OCULTO", "La Falacia del Promedio", "Mide copia del libro, no comprensión real ni capacidad pedagógica.", "0.795", "APEGO ENGAÑOSO", div_h, font_sz)
    c2 = build_card("#4A3B3D", "02", "EL ESTÁNDAR TÉCNICO", "Auditoría Desglosada", "<strong style=\'color: #4A3B3D;\'>Prohibido promedio único:</strong> auditar fidelidad y rechazo por separado.", "3", "DIMENSIONES", div_h, font_sz)
    c3 = build_card("var(--c-wine-primary)", "03", "AUTOESTUDIO SIN DOCENTE", "Qwen2.5-3B: Certeza", "<strong>Sin profesor:</strong> preferible admitir no saber antes que inventar.", "85.7%", "RECHAZO CERTERO", div_h, font_sz)
    c4 = build_card("var(--c-red-accent)", "04", "AULA ASISTIDA CON DOCENTE", "Phi-4-mini: Fluidez", "<strong>Con profesor:</strong> prima la fluidez y el docente corrige en vivo.", "0.0%", "BLOQUEOS DIÁLOGO", div_h, font_sz)
    return f'''
    <h2 class="s-lead-question" style="font-size: 38px; font-weight: 800; margin: 0; line-height: 1.2; color: #2C0509;">
      Apego al texto no es aprendizaje: criterios para auditar y desplegar tutores
    </h2>
    <div style="display: grid; grid-template-columns: 1fr 1fr; grid-template-rows: 1fr 1fr; gap: 24px; flex: 1; margin-top: 14px;">
      {c1}
      {c2}
      {c3}
      {c4}
    </div>
    '''

HTML_PAGE = '''<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <title>Divider & Padding Tests</title>
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
    configs = [
        ("divider_auto_58px", None, "58px"),
        ("divider_130px_58px", "130px", "58px"),
        ("divider_auto_60px", None, "60px"),
    ]

    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(viewport={"width": 1920, "height": 1080})

        for name, div_h, font_sz in configs:
            content = get_grid(div_h, font_sz)
            html = HTML_PAGE.format(content=content)
            tmp_html = os.path.join(output_dir, f"{name}.html")
            tmp_png = os.path.join(output_dir, f"{name}.png")
            with open(tmp_html, "w", encoding="utf-8") as f:
                f.write(html)
            page.goto(f"file:///{tmp_html.replace(os.sep, '/')}")
            page.wait_for_timeout(350)
            page.screenshot(path=tmp_png)
            print(f"Generated {name}.png")

        browser.close()

if __name__ == '__main__':
    main()
