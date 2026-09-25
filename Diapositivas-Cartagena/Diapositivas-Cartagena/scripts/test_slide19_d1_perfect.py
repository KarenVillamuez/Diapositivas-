# -*- coding: utf-8 -*-
import os
from playwright.sync_api import sync_playwright

output_dir = r"C:\Users\ASUS\.gemini\antigravity-ide\brain\a6624504-511c-4b9d-bc9a-468e348bde40"
os.makedirs(output_dir, exist_ok=True)

PANEL_LEFT = '''
      <!-- Panel 1: RAG y Evaluación Automatizada -->
      <div style="background: #FAF5F5; border-top: 6px solid var(--c-wine-primary); padding: 24px 30px; display: flex; flex-direction: column; justify-content: space-between;">
        <div style="display: flex; align-items: center; justify-content: space-between; border-bottom: 2px solid #EAE0E1; padding-bottom: 8px;">
          <span style="font-family: var(--font-mono); font-size: 16px; font-weight: 800; color: var(--c-wine-primary); letter-spacing: 1.5px;">
            01 · RAG Y EVALUACIÓN AUTOMATIZADA
          </span>
          <span style="font-family: var(--font-mono); font-size: 13px; font-weight: 800; color: #5D4A4D; background: #EAE0E1; padding: 2px 8px;">
            3 FUENTES
          </span>
        </div>

        <!-- Ref 1: Lewis -->
        <div style="padding-bottom: 12px; border-bottom: 1px solid #E8DCDE;">
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 3px;">
            <span style="font-family: var(--font-mono); font-size: 13px; font-weight: 800; color: var(--c-wine-primary); letter-spacing: 1px;">RAG FUNDACIONAL</span>
            <span style="font-family: var(--font-mono); font-size: 13px; font-weight: 800; color: #5D4A4D;">NeurIPS 2020</span>
          </div>
          <div style="font-family: var(--font-sans); font-size: 23px; font-weight: 800; color: #110103; margin-bottom: 2px;">
            Lewis, P., Perez, E., Piktus, A., et al. (2020)
          </div>
          <div style="font-family: var(--font-sans); font-size: 21px; color: #222; line-height: 1.35; font-weight: 500;">
            Retrieval-augmented generation for knowledge-intensive NLP tasks. <em>Advances in Neural Information Processing Systems</em>, 33, 9459–9474.
          </div>
        </div>

        <!-- Ref 2: Es (RAGAs) -->
        <div style="padding-bottom: 12px; border-bottom: 1px solid #E8DCDE;">
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 3px;">
            <span style="font-family: var(--font-mono); font-size: 13px; font-weight: 800; color: var(--c-wine-primary); letter-spacing: 1px;">EVALUACIÓN MÉTRICA</span>
            <span style="font-family: var(--font-mono); font-size: 13px; font-weight: 800; color: #5D4A4D;">EACL 2024</span>
          </div>
          <div style="font-family: var(--font-sans); font-size: 23px; font-weight: 800; color: #110103; margin-bottom: 2px;">
            Es, S., James, J., Espinosa-Anke, L., &amp; Schockaert, S. (2024)
          </div>
          <div style="font-family: var(--font-sans); font-size: 21px; color: #222; line-height: 1.35; font-weight: 500;">
            RAGAs: Automated evaluation of retrieval augmented generation. <em>Proceedings of the 18th Conference of the EACL: System Demonstrations</em>, 150–158.
          </div>
        </div>

        <!-- Ref 3: Nogueira -->
        <div>
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 3px;">
            <span style="font-family: var(--font-mono); font-size: 13px; font-weight: 800; color: var(--c-wine-primary); letter-spacing: 1px;">REORDENAMIENTO CROSS-ENCODER</span>
            <span style="font-family: var(--font-mono); font-size: 13px; font-weight: 800; color: #5D4A4D;">arXiv:1901.04085</span>
          </div>
          <div style="font-family: var(--font-sans); font-size: 23px; font-weight: 800; color: #110103; margin-bottom: 2px;">
            Nogueira, R., &amp; Cho, K. (2019)
          </div>
          <div style="font-family: var(--font-sans); font-size: 21px; color: #222; line-height: 1.35; font-weight: 500;">
            Passage re-ranking with BERT. <em>arXiv preprint arXiv:1901.04085</em>. Módulo de re-clasificación semántica para top-k pasajes en hardware común.
          </div>
        </div>
      </div>
'''

def build_right_panel(highlight_html):
    return f'''
      <!-- Panel 2: Modelos SLM y Artículo Base -->
      <div style="background: #FAF5F5; border-top: 6px solid var(--c-red-accent); padding: 24px 30px; display: flex; flex-direction: column; justify-content: space-between;">
        <div style="display: flex; align-items: center; justify-content: space-between; border-bottom: 2px solid #EAE0E1; padding-bottom: 8px; margin-bottom: 8px;">
          <span style="font-family: var(--font-mono); font-size: 16px; font-weight: 800; color: var(--c-red-accent); letter-spacing: 1.5px;">
            02 · MODELOS SLM Y ARTÍCULO BASE
          </span>
          <span style="font-family: var(--font-mono); font-size: 13px; font-weight: 800; color: #5D4A4D; background: #EAE0E1; padding: 2px 8px;">
            3 FUENTES
          </span>
        </div>

        {highlight_html}

        <!-- Ref 5: Abouelenin (Phi-4-mini) -->
        <div style="padding-bottom: 12px; border-bottom: 1px solid #E8DCDE;">
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 3px;">
            <span style="font-family: var(--font-mono); font-size: 13px; font-weight: 800; color: var(--c-red-accent); letter-spacing: 1px;">SLM EVALUADO · PHI</span>
            <span style="font-family: var(--font-mono); font-size: 13px; font-weight: 800; color: var(--c-red-accent);">arXiv:2503.01743</span>
          </div>
          <div style="font-family: var(--font-sans); font-size: 23px; font-weight: 800; color: #110103; margin-bottom: 2px;">
            Abouelenin, A., et al. [Microsoft Research] (2025)
          </div>
          <div style="font-family: var(--font-sans); font-size: 21px; color: #222; line-height: 1.35; font-weight: 500;">
            Phi-4-mini technical report: Compact and capable multimodal reasoning. <em>arXiv preprint arXiv:2503.01743</em>.
          </div>
        </div>

        <!-- Ref 6: Yang (Qwen2.5) -->
        <div>
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 3px;">
            <span style="font-family: var(--font-mono); font-size: 13px; font-weight: 800; color: var(--c-wine-primary); letter-spacing: 1px;">SLM EVALUADO · QWEN</span>
            <span style="font-family: var(--font-mono); font-size: 13px; font-weight: 800; color: var(--c-wine-primary);">arXiv:2412.15115</span>
          </div>
          <div style="font-family: var(--font-sans); font-size: 23px; font-weight: 800; color: #110103; margin-bottom: 2px;">
            Yang, A., et al. [Qwen Team] (2024)
          </div>
          <div style="font-family: var(--font-sans); font-size: 21px; color: #222; line-height: 1.35; font-weight: 500;">
            Qwen2.5 technical report. <em>arXiv preprint arXiv:2412.15115</em>. Arquitectura transformer densa (3.1B evaluado sin internet).
          </div>
        </div>
      </div>
'''

# D1-A: Fondo Dorado Oro Cálido (#FFFDF0), Borde Lateral 7px Oro Oscuro (#9E7700), Badge Doble
HL_D1A = '''
        <!-- Ref 4: Muñoz-Gómez (Paper Base) D1-A -->
        <div style="background: #FFFCEB; border-left: 7px solid #B38600; border-top: 1px solid #EFE4BF; border-right: 1px solid #EFE4BF; border-bottom: 1px solid #EFE4BF; padding: 13px 18px; margin-bottom: 8px;">
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 4px;">
            <div style="display: flex; align-items: center; gap: 8px;">
              <span style="background: #B38600; color: #FFFFFF; font-family: var(--font-mono); font-size: 12px; font-weight: 900; letter-spacing: 1px; padding: 3px 8px;">
                ★ ARTÍCULO BASE DEL BENCHMARK
              </span>
              <span style="font-family: var(--font-mono); font-size: 12px; font-weight: 800; color: #8A6700;">
                AUTORES DE LA INVESTIGACIÓN
              </span>
            </div>
            <span style="font-family: var(--font-mono); font-size: 13px; font-weight: 900; color: #8A6700; background: #FFF3C4; padding: 2px 8px; border: 1px solid #F5C21B;">
              REVISTA ENTRAMADO · 2026
            </span>
          </div>
          <div style="font-family: var(--font-sans); font-size: 24px; font-weight: 900; color: #110103; margin-bottom: 2px;">
            Muñoz-Gómez, Y., Hoyos-Cerón, F., &amp; Caiza, J. (2026)
          </div>
          <div style="font-family: var(--font-sans); font-size: 21px; color: #110103; line-height: 1.35; font-weight: 600;">
            Portable RAG for offline tutoring: A benchmark on rural school hardware. <strong style="color: #6B1D2F;">Revista Entramado</strong>, 22(2), 1–19. DOI: 10.18041/1900-3803.
          </div>
        </div>
'''

# D1-B: Fondo Suave Vinotinto (#FAF2F3), Borde Lateral 7px Vinotinto Institucional, Badge Sólido Vino + Oro
HL_D1B = '''
        <!-- Ref 4: Muñoz-Gómez (Paper Base) D1-B -->
        <div style="background: #FAF2F3; border-left: 7px solid var(--c-wine-primary); border-top: 1px solid #E8D0D5; border-right: 1px solid #E8D0D5; border-bottom: 1px solid #E8D0D5; padding: 13px 18px; margin-bottom: 8px;">
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 4px;">
            <div style="display: flex; align-items: center; gap: 8px;">
              <span style="background: var(--c-wine-primary); color: #FFFFFF; font-family: var(--font-mono); font-size: 12px; font-weight: 900; letter-spacing: 1px; padding: 3px 8px;">
                ★ ARTÍCULO BASE DEL BENCHMARK
              </span>
              <span style="font-family: var(--font-mono); font-size: 12px; font-weight: 800; color: var(--c-wine-primary);">
                COLMAYOR CAUCA
              </span>
            </div>
            <span style="font-family: var(--font-mono); font-size: 13px; font-weight: 900; color: var(--c-wine-primary); background: #F0E6E8; padding: 2px 8px; border: 1px solid #D8B8BE;">
              REVISTA ENTRAMADO · 2026
            </span>
          </div>
          <div style="font-family: var(--font-sans); font-size: 24px; font-weight: 900; color: var(--c-wine-primary); margin-bottom: 2px;">
            Muñoz-Gómez, Y., Hoyos-Cerón, F., &amp; Caiza, J. (2026)
          </div>
          <div style="font-family: var(--font-sans); font-size: 21px; color: #110103; line-height: 1.35; font-weight: 600;">
            Portable RAG for offline tutoring: A benchmark on rural school hardware. <strong style="color: var(--c-wine-primary);">Revista Entramado</strong>, 22(2), 1–19. DOI: 10.18041/1900-3803.
          </div>
        </div>
'''

def build_full_html(highlight):
    return f'''
  <div class="slide-content-area" style="top: 175px; height: 720px; justify-content: space-between;">
    <h2 class="s-lead-question" style="font-size: 38px; font-weight: 800; margin: 0; line-height: 1.2; color: #2C0509;">
      Referencias Bibliográficas Clave (Norma APA VII)
    </h2>

    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 32px; flex: 1; margin-top: 16px; margin-bottom: 16px;">
      {PANEL_LEFT}
      {build_right_panel(highlight)}
    </div>

    <!-- Banner Institucional de Cierre (Doble Regla Estilo Slide 14/18) -->
    <div style="background: #FAF5F5; border-top: 3.5px solid var(--c-wine-primary); border-bottom: 3.5px solid var(--c-wine-primary); padding: 14px 28px; display: flex; align-items: center; justify-content: space-between;">
      <div style="display: flex; align-items: center; gap: 16px;">
        <span style="font-family: var(--font-mono); font-size: 14px; font-weight: 800; color: var(--c-wine-primary); letter-spacing: 1.5px;">FILIACIÓN &amp; REPRODUCIBILIDAD:</span>
        <span style="font-family: var(--font-sans); font-size: 22px; font-weight: 600; color: #110103;">
          Artículo presentado en el VI Congreso Internacional de Investigación Interdisciplinar · Cartagena de Indias, 2026.
        </span>
      </div>
      <span style="font-family: var(--font-mono); font-size: 16px; font-weight: 800; color: var(--c-wine-primary); letter-spacing: 1px;">
        LOHACEMOSXTIC.COM
      </span>
    </div>
  </div>
'''

HTML_PAGE = '''<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <title>Slide 19 D1 Perfect</title>
  <link rel="stylesheet" href="http://localhost:8085/styles.css?v=33">
</head>
<body style="margin: 0; padding: 0; background: #0b0103;">
  <div id="presentation-viewport">
    <div id="slides-stage">
      <section class="slide s-white active">
        <header class="slide-header">
          <div class="sh-left">
            <span class="sh-red-bar"></span>
            <span class="sh-category">05 · REFERENCIAS · APA VII</span>
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
        ("slide19_d1a_dorado_perfeccionado", build_full_html(HL_D1A)),
        ("slide19_d1b_vino_perfeccionado", build_full_html(HL_D1B)),
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
