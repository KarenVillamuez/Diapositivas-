# -*- coding: utf-8 -*-
import os
from playwright.sync_api import sync_playwright

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
    <h2 class="s-lead-question" style="font-size: 46px; font-weight: 800; margin-bottom: 26px; line-height: 1.2;">
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

# Tabla compartida con la columna PÁGINAS en negro puro #110103, font-size 26px bold, y "Ausente en libro" en #900C13 badge
table_html = '''
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
          <!-- Fila 1: Grammar -->
          <tr style="background: #FFFFFF; border-bottom: 1px solid var(--c-border-subtle);">
            <td style="padding: 18px 24px; font-size: 25px; font-weight: 800; color: #110103;">Grammar</td>
            <td style="padding: 18px 20px; font-size: 25px; font-family: var(--font-mono); font-weight: 700; color: var(--c-wine-primary); text-align: center;">G1 &ndash; G4</td>
            <td style="padding: 18px 20px; font-size: 26px; font-family: var(--font-sans); font-weight: 800; color: #110103; text-align: center;">191 &ndash; 235</td>
            <td style="padding: 18px 24px; font-size: 24px; color: #110103; line-height: 1.35;">4 preguntas sobre reglas gramaticales y tiempos verbales.</td>
          </tr>
          <!-- Fila 2: Vocabulary -->
          <tr style="background: #FAF5F5; border-bottom: 1px solid var(--c-border-subtle);">
            <td style="padding: 18px 24px; font-size: 25px; font-weight: 800; color: #110103;">Vocabulary</td>
            <td style="padding: 18px 20px; font-size: 25px; font-family: var(--font-mono); font-weight: 700; color: var(--c-wine-primary); text-align: center;">V1 &ndash; V3</td>
            <td style="padding: 18px 20px; font-size: 26px; font-family: var(--font-sans); font-weight: 800; color: #110103; text-align: center;">36 &ndash; 150</td>
            <td style="padding: 18px 24px; font-size: 24px; color: #110103; line-height: 1.35;">3 preguntas de definici&oacute;n y uso en contexto formal.</td>
          </tr>
          <!-- Fila 3: Writing -->
          <tr style="background: #FFFFFF; border-bottom: 1px solid var(--c-border-subtle);">
            <td style="padding: 18px 24px; font-size: 25px; font-weight: 800; color: #110103;">Writing</td>
            <td style="padding: 18px 20px; font-size: 25px; font-family: var(--font-mono); font-weight: 700; color: var(--c-wine-primary); text-align: center;">W1 &ndash; W3</td>
            <td style="padding: 18px 20px; font-size: 26px; font-family: var(--font-sans); font-weight: 800; color: #110103; text-align: center;">68 &ndash; 138</td>
            <td style="padding: 18px 24px; font-size: 24px; color: #110103; line-height: 1.35;">3 preguntas sobre estructura de p&aacute;rrafos y coherencia.</td>
          </tr>
          <!-- Fila 4: Reading -->
          <tr style="background: #FAF5F5; border-bottom: 2px solid var(--c-red-accent);">
            <td style="padding: 18px 24px; font-size: 25px; font-weight: 800; color: #110103;">Reading</td>
            <td style="padding: 18px 20px; font-size: 25px; font-family: var(--font-mono); font-weight: 700; color: var(--c-wine-primary); text-align: center;">R1 &ndash; R2</td>
            <td style="padding: 18px 20px; font-size: 26px; font-family: var(--font-sans); font-weight: 800; color: #110103; text-align: center;">15 &ndash; 60</td>
            <td style="padding: 18px 24px; font-size: 24px; color: #110103; line-height: 1.35;">2 preguntas de comprensi&oacute;n e inferencia textual.</td>
          </tr>
          <!-- Fila 5: Sondas de Rechazo -->
          <tr style="background: #FFF2F2;">
            <td style="padding: 20px 24px; font-size: 25px; font-weight: 800; color: var(--c-red-accent);">
              <span style="display: inline-block; background: var(--c-red-accent); color: #FFFFFF; font-size: 15px; font-family: var(--font-mono); font-weight: 800; padding: 3px 8px; margin-right: 8px; border-radius: 3px;">SONDA</span>
              Fuera de alcance
            </td>
            <td style="padding: 20px 20px; font-size: 25px; font-family: var(--font-mono); font-weight: 800; color: var(--c-red-accent); text-align: center;">F1 &ndash; F2</td>
            <td style="padding: 20px 20px; text-align: center;">
              <span style="display: inline-block; background: #FFE4E6; border: 1.5px solid var(--c-red-accent); color: #900C13; font-family: var(--font-sans); font-size: 22px; font-weight: 800; padding: 4px 12px; border-radius: 4px;">Ausente en libro</span>
            </td>
            <td style="padding: 20px 24px; font-size: 24px; color: #110103; line-height: 1.35;">
              <strong style="color: var(--c-red-accent);">2 sondas de rechazo:</strong> Auditan si el modelo inventa informaci&oacute;n o se abstiene con honestidad.
            </td>
          </tr>
        </tbody>
      </table>
    </div>
'''

# VARIANTE 1: Línea tipográfica limpia de alto impacto (26px)
v1_bottom = '''
    <div style="margin-top: 22px; font-family: var(--font-sans); font-size: 26px; color: #110103; font-weight: 800; display: flex; align-items: center; justify-content: space-between;">
      <div>
        <span style="color: var(--c-wine-primary); letter-spacing: 0.5px;">TOTAL: 14 &Iacute;TEMS DE EVALUACI&Oacute;N</span>
      </div>
      <div style="font-size: 24px; font-weight: 700; color: #110103;">
        <span style="color: var(--c-wine-primary); font-weight: 800;">12 Curriculares</span> (Libro College ESL Writers) &nbsp;&bull;&nbsp; <span style="color: var(--c-red-accent); font-weight: 800;">2 Sondas de Rechazo</span>
      </div>
    </div>
'''

# VARIANTE 2: Barra banner estilizada (Background #FAF5F5 con borde 2px wine)
v2_bottom = '''
    <div style="margin-top: 20px; background: #FAF5F5; border: 2px solid var(--c-wine-primary); padding: 14px 28px; display: flex; align-items: center; justify-content: space-between;">
      <div style="font-family: var(--font-sans); font-size: 26px; font-weight: 800; color: var(--c-wine-primary);">
        TOTAL: 14 &Iacute;TEMS DE EVALUACI&Oacute;N
      </div>
      <div style="font-family: var(--font-sans); font-size: 24px; font-weight: 700; color: #110103;">
        <span style="color: var(--c-wine-primary); font-weight: 800;">12 Curriculares</span> (Libro College ESL Writers) &nbsp;&bull;&nbsp; <span style="color: var(--c-red-accent); font-weight: 800;">2 Sondas de Rechazo</span>
      </div>
    </div>
'''

options = {
    "slide_09_v1_linea.png": table_html + v1_bottom,
    "slide_09_v2_banner.png": table_html + v2_bottom,
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

print("Variations captured.")
