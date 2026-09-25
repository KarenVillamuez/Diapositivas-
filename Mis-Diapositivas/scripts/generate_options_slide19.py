# -*- coding: utf-8 -*-
import os
from playwright.sync_api import sync_playwright

output_dir = r"C:\Users\ASUS\.gemini\antigravity-ide\brain\a6624504-511c-4b9d-bc9a-468e348bde40"
os.makedirs(output_dir, exist_ok=True)

# ==============================================================================
# CONTENIDOS Y REFERENCIAS APA VII
# ==============================================================================

# ==============================================================================
# OPCIÓN A: Dos Paneles Editoriales Estructurados con Borde Superior y Separadores
# ==============================================================================
CONTENT_OPCION_A = '''
  <div class="slide-content-area" style="top: 175px; height: 720px; justify-content: space-between;">
    <h2 class="s-lead-question" style="font-size: 38px; font-weight: 800; margin: 0; line-height: 1.2; color: #2C0509;">
      Referencias Bibliográficas Clave (Norma APA VII)
    </h2>

    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 32px; flex: 1; margin-top: 16px; margin-bottom: 16px;">
      
      <!-- Panel 1: RAG y Evaluación Automatizada -->
      <div style="background: #FAF5F5; border-top: 6px solid var(--c-wine-primary); padding: 24px 28px; display: flex; flex-direction: column; justify-content: space-between;">
        <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 14px; border-bottom: 2px solid #EAE0E1; padding-bottom: 10px;">
          <span style="font-family: var(--font-mono); font-size: 16px; font-weight: 800; color: var(--c-wine-primary); letter-spacing: 1.5px;">
            01 · RAG Y EVALUACIÓN AUTOMATIZADA
          </span>
          <span style="font-family: var(--font-mono); font-size: 14px; font-weight: 700; color: #5D4A4D;">3 CITAS</span>
        </div>

        <!-- Ref 1: Lewis -->
        <div style="padding-bottom: 14px; border-bottom: 1px solid #E8DCDE;">
          <div style="display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 4px;">
            <span style="font-family: var(--font-sans); font-size: 24px; font-weight: 800; color: #110103;">Lewis, P., Perez, E., Piktus, A., et al. (2020)</span>
            <span style="font-family: var(--font-mono); font-size: 13px; font-weight: 800; color: var(--c-wine-primary); background: #F0E6E8; padding: 2px 8px;">NeurIPS 2020</span>
          </div>
          <div style="font-family: var(--font-sans); font-size: 21px; color: #222; line-height: 1.35; font-weight: 500;">
            Retrieval-augmented generation for knowledge-intensive NLP tasks. <em>Advances in Neural Information Processing Systems</em>, 33, 9459–9474.
          </div>
        </div>

        <!-- Ref 2: Es (RAGAs) -->
        <div style="padding-bottom: 14px; border-bottom: 1px solid #E8DCDE;">
          <div style="display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 4px;">
            <span style="font-family: var(--font-sans); font-size: 24px; font-weight: 800; color: #110103;">Es, S., James, J., Espinosa-Anke, L., &amp; Schockaert, S. (2024)</span>
            <span style="font-family: var(--font-mono); font-size: 13px; font-weight: 800; color: var(--c-wine-primary); background: #F0E6E8; padding: 2px 8px;">EACL 2024</span>
          </div>
          <div style="font-family: var(--font-sans); font-size: 21px; color: #222; line-height: 1.35; font-weight: 500;">
            RAGAs: Automated evaluation of retrieval augmented generation. <em>Proceedings of the 18th Conference of the EACL: System Demonstrations</em>, 150–158.
          </div>
        </div>

        <!-- Ref 3: Nogueira -->
        <div>
          <div style="display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 4px;">
            <span style="font-family: var(--font-sans); font-size: 24px; font-weight: 800; color: #110103;">Nogueira, R., &amp; Cho, K. (2019)</span>
            <span style="font-family: var(--font-mono); font-size: 13px; font-weight: 800; color: #5D4A4D; background: #EAE0E1; padding: 2px 8px;">arXiv:1901.04085</span>
          </div>
          <div style="font-family: var(--font-sans); font-size: 21px; color: #222; line-height: 1.35; font-weight: 500;">
            Passage re-ranking with BERT. <em>arXiv preprint arXiv:1901.04085</em>. Fundamento del módulo Cross-Encoder de reordenamiento semántico.
          </div>
        </div>
      </div>

      <!-- Panel 2: Modelos SLM y Artículo Base -->
      <div style="background: #FAF5F5; border-top: 6px solid var(--c-red-accent); padding: 24px 28px; display: flex; flex-direction: column; justify-content: space-between;">
        <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 14px; border-bottom: 2px solid #EAE0E1; padding-bottom: 10px;">
          <span style="font-family: var(--font-mono); font-size: 16px; font-weight: 800; color: var(--c-red-accent); letter-spacing: 1.5px;">
            02 · MODELOS SLM Y ARTÍCULO BASE
          </span>
          <span style="font-family: var(--font-mono); font-size: 14px; font-weight: 700; color: #5D4A4D;">3 CITAS</span>
        </div>

        <!-- Ref 4: Muñoz-Gómez (Paper Base) -->
        <div style="padding-bottom: 14px; border-bottom: 1px solid #E8DCDE;">
          <div style="display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 4px;">
            <span style="font-family: var(--font-sans); font-size: 24px; font-weight: 800; color: #110103;">Muñoz-Gómez, Y., Hoyos-Cerón, F., &amp; Caiza, J. (2026)</span>
            <span style="font-family: var(--font-mono); font-size: 13px; font-weight: 800; color: #785A00; background: #FFF3C4; padding: 2px 8px; border: 1px solid #F5C21B;">ARTÍCULO BASE</span>
          </div>
          <div style="font-family: var(--font-sans); font-size: 21px; color: #222; line-height: 1.35; font-weight: 500;">
            Portable RAG for offline tutoring: A benchmark on rural school hardware. <em>Revista Entramado</em>, 22(2), 1–19. DOI: 10.18041/1900-3803.
          </div>
        </div>

        <!-- Ref 5: Abouelenin (Phi-4-mini) -->
        <div style="padding-bottom: 14px; border-bottom: 1px solid #E8DCDE;">
          <div style="display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 4px;">
            <span style="font-family: var(--font-sans); font-size: 24px; font-weight: 800; color: #110103;">Abouelenin, A., et al. [Microsoft Research] (2025)</span>
            <span style="font-family: var(--font-mono); font-size: 13px; font-weight: 800; color: var(--c-red-accent); background: #FDE8E8; padding: 2px 8px;">arXiv:2503.01743</span>
          </div>
          <div style="font-family: var(--font-sans); font-size: 21px; color: #222; line-height: 1.35; font-weight: 500;">
            Phi-4-mini technical report: Compact and capable multimodal reasoning. <em>arXiv preprint arXiv:2503.01743</em>.
          </div>
        </div>

        <!-- Ref 6: Yang (Qwen2.5) -->
        <div>
          <div style="display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 4px;">
            <span style="font-family: var(--font-sans); font-size: 24px; font-weight: 800; color: #110103;">Yang, A., et al. [Qwen Team] (2024)</span>
            <span style="font-family: var(--font-mono); font-size: 13px; font-weight: 800; color: var(--c-wine-primary); background: #F0E6E8; padding: 2px 8px;">arXiv:2412.15115</span>
          </div>
          <div style="font-family: var(--font-sans); font-size: 21px; color: #222; line-height: 1.35; font-weight: 500;">
            Qwen2.5 technical report. <em>arXiv preprint arXiv:2412.15115</em>. Arquitectura transformer de parámetros densos (3.1B evaluado).
          </div>
        </div>
      </div>

    </div>

    <!-- Banner Institucional de Cierre -->
    <div style="background: #FAF5F5; border-top: 3px solid var(--c-wine-primary); border-bottom: 3px solid var(--c-wine-primary); padding: 14px 28px; display: flex; align-items: center; justify-content: space-between;">
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

# ==============================================================================
# OPCIÓN B: Fichas Bibliográficas con Tarjetas Individuales (Grid 2x3 Plano)
# ==============================================================================
CONTENT_OPCION_B = '''
  <div class="slide-content-area" style="top: 175px; height: 720px; justify-content: space-between;">
    <div style="display: flex; justify-content: space-between; align-items: baseline;">
      <h2 class="s-lead-question" style="font-size: 38px; font-weight: 800; margin: 0; line-height: 1.2; color: #2C0509;">
        Referencias Bibliográficas Clave
      </h2>
      <div style="font-family: var(--font-mono); font-size: 16px; font-weight: 800; color: var(--c-wine-primary); letter-spacing: 1px;">
        ESTÁNDAR APA 7.ª EDICIÓN
      </div>
    </div>

    <!-- Grid 2x3 de Fichas Planas -->
    <div style="display: grid; grid-template-columns: 1fr 1fr; grid-template-rows: repeat(3, 1fr); gap: 16px; flex: 1; margin-top: 14px; margin-bottom: 14px;">
      
      <!-- Ficha 1 -->
      <div style="background: #FAF5F5; border-left: 6px solid var(--c-wine-primary); padding: 14px 22px; display: flex; flex-direction: column; justify-content: center;">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 3px;">
          <span style="font-family: var(--font-mono); font-size: 12px; font-weight: 800; color: var(--c-wine-primary); letter-spacing: 1px;">RAG FUNDACIONAL</span>
          <span style="font-family: var(--font-mono); font-size: 13px; font-weight: 800; color: #5D4A4D;">NeurIPS 2020</span>
        </div>
        <div style="font-family: var(--font-sans); font-size: 23px; font-weight: 800; color: #110103; margin-bottom: 2px;">
          Lewis, P., Perez, E., Piktus, A., et al. (2020)
        </div>
        <div style="font-family: var(--font-sans); font-size: 20px; color: #333; line-height: 1.3;">
          Retrieval-augmented generation for knowledge-intensive NLP tasks. <em>NeurIPS</em>, 33, 9459–9474.
        </div>
      </div>

      <!-- Ficha 2 -->
      <div style="background: #FAF5F5; border-left: 6px solid #B38600; padding: 14px 22px; display: flex; flex-direction: column; justify-content: center;">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 3px;">
          <span style="font-family: var(--font-mono); font-size: 12px; font-weight: 800; color: #8A6700; letter-spacing: 1px;">ARTÍCULO PRINCIPAL</span>
          <span style="font-family: var(--font-mono); font-size: 13px; font-weight: 800; color: #8A6700; background: #FFF3C4; padding: 1px 6px;">ENTRAMADO 2026</span>
        </div>
        <div style="font-family: var(--font-sans); font-size: 23px; font-weight: 800; color: #110103; margin-bottom: 2px;">
          Muñoz-Gómez, Y., Hoyos-Cerón, F., &amp; Caiza, J. (2026)
        </div>
        <div style="font-family: var(--font-sans); font-size: 20px; color: #333; line-height: 1.3;">
          Portable RAG for offline tutoring: A benchmark on rural school hardware. <em>Revista Entramado</em>, 22(2).
        </div>
      </div>

      <!-- Ficha 3 -->
      <div style="background: #FAF5F5; border-left: 6px solid var(--c-wine-primary); padding: 14px 22px; display: flex; flex-direction: column; justify-content: center;">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 3px;">
          <span style="font-family: var(--font-mono); font-size: 12px; font-weight: 800; color: var(--c-wine-primary); letter-spacing: 1px;">MÉTRICAS AUTOMATIZADAS</span>
          <span style="font-family: var(--font-mono); font-size: 13px; font-weight: 800; color: #5D4A4D;">EACL 2024</span>
        </div>
        <div style="font-family: var(--font-sans); font-size: 23px; font-weight: 800; color: #110103; margin-bottom: 2px;">
          Es, S., James, J., Espinosa-Anke, L., &amp; Schockaert, S. (2024)
        </div>
        <div style="font-family: var(--font-sans); font-size: 20px; color: #333; line-height: 1.3;">
          RAGAs: Automated evaluation of retrieval augmented generation. <em>EACL System Demos</em>, 150–158.
        </div>
      </div>

      <!-- Ficha 4 -->
      <div style="background: #FAF5F5; border-left: 6px solid var(--c-red-accent); padding: 14px 22px; display: flex; flex-direction: column; justify-content: center;">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 3px;">
          <span style="font-family: var(--font-mono); font-size: 12px; font-weight: 800; color: var(--c-red-accent); letter-spacing: 1px;">SLM EVALUADO · PHI</span>
          <span style="font-family: var(--font-mono); font-size: 13px; font-weight: 800; color: var(--c-red-accent);">arXiv 2025</span>
        </div>
        <div style="font-family: var(--font-sans); font-size: 23px; font-weight: 800; color: #110103; margin-bottom: 2px;">
          Abouelenin, A., et al. [Microsoft] (2025)
        </div>
        <div style="font-family: var(--font-sans); font-size: 20px; color: #333; line-height: 1.3;">
          Phi-4-mini technical report: Compact multimodal reasoning. <em>arXiv:2503.01743</em>.
        </div>
      </div>

      <!-- Ficha 5 -->
      <div style="background: #FAF5F5; border-left: 6px solid var(--c-wine-primary); padding: 14px 22px; display: flex; flex-direction: column; justify-content: center;">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 3px;">
          <span style="font-family: var(--font-mono); font-size: 12px; font-weight: 800; color: var(--c-wine-primary); letter-spacing: 1px;">REORDENAMIENTO</span>
          <span style="font-family: var(--font-mono); font-size: 13px; font-weight: 800; color: #5D4A4D;">arXiv 2019</span>
        </div>
        <div style="font-family: var(--font-sans); font-size: 23px; font-weight: 800; color: #110103; margin-bottom: 2px;">
          Nogueira, R., &amp; Cho, K. (2019)
        </div>
        <div style="font-family: var(--font-sans); font-size: 20px; color: #333; line-height: 1.3;">
          Passage re-ranking with BERT. <em>arXiv:1901.04085</em>. Cross-Encoder para top-k pasajes.
        </div>
      </div>

      <!-- Ficha 6 -->
      <div style="background: #FAF5F5; border-left: 6px solid var(--c-wine-primary); padding: 14px 22px; display: flex; flex-direction: column; justify-content: center;">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 3px;">
          <span style="font-family: var(--font-mono); font-size: 12px; font-weight: 800; color: var(--c-wine-primary); letter-spacing: 1px;">SLM EVALUADO · QWEN</span>
          <span style="font-family: var(--font-mono); font-size: 13px; font-weight: 800; color: var(--c-wine-primary);">arXiv 2024</span>
        </div>
        <div style="font-family: var(--font-sans); font-size: 23px; font-weight: 800; color: #110103; margin-bottom: 2px;">
          Yang, A., et al. [Qwen Team] (2024)
        </div>
        <div style="font-family: var(--font-sans); font-size: 20px; color: #333; line-height: 1.3;">
          Qwen2.5 technical report. <em>arXiv:2412.15115</em>. Modelo denso de 3.1B parámetros.
        </div>
      </div>

    </div>

    <!-- Banner Base -->
    <div style="background: #FAF2F3; border: 1.5px solid #E2CCD1; padding: 14px 28px; display: flex; align-items: center; justify-content: space-between;">
      <span style="font-family: var(--font-sans); font-size: 22px; font-weight: 600; color: #110103;">
        Investigación presentada en el <strong>VI Congreso Internacional de Investigación Interdisciplinar</strong> (Cartagena 2026).
      </span>
      <span style="font-family: var(--font-mono); font-size: 15px; font-weight: 800; color: var(--c-wine-primary);">
        REPOSITORIO: LOHACEMOSXTIC.COM
      </span>
    </div>
  </div>
'''

# ==============================================================================
# OPCIÓN C: Formato Editorial Abierto con Sangría Francesa Clásica y Marco Ligero
# ==============================================================================
CONTENT_OPCION_C = '''
  <div class="slide-content-area" style="top: 175px; height: 720px; justify-content: space-between;">
    <h2 class="s-lead-question" style="font-size: 38px; font-weight: 800; margin: 0; line-height: 1.2; color: #2C0509;">
      Referencias Bibliográficas Clave (Norma APA VII)
    </h2>

    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 40px; flex: 1; margin-top: 18px; margin-bottom: 18px;">
      
      <!-- Columna 1 -->
      <div style="display: flex; flex-direction: column; justify-content: space-between; border-right: 2px solid #E2D2D2; padding-right: 30px;">
        <div style="font-family: var(--font-mono); font-size: 18px; font-weight: 800; color: var(--c-wine-primary); letter-spacing: 1.5px; border-bottom: 2px solid var(--c-wine-primary); padding-bottom: 8px; margin-bottom: 12px;">
          RAG Y EVALUACIÓN AUTOMATIZADA
        </div>

        <div style="padding-left: 28px; text-indent: -28px; font-family: var(--font-sans); font-size: 22px; color: #110103; line-height: 1.45;">
          <strong>Lewis, P., Perez, E., Piktus, A., et al. (2020).</strong> Retrieval-augmented generation for knowledge-intensive NLP tasks. <em>Advances in Neural Information Processing Systems</em>, 33, 9459–9474.
        </div>

        <div style="padding-left: 28px; text-indent: -28px; font-family: var(--font-sans); font-size: 22px; color: #110103; line-height: 1.45;">
          <strong>Es, S., James, J., Espinosa-Anke, L., &amp; Schockaert, S. (2024).</strong> RAGAs: Automated evaluation of retrieval augmented generation. <em>Proceedings of the 18th Conference of the EACL: System Demonstrations</em>, 150–158.
        </div>

        <div style="padding-left: 28px; text-indent: -28px; font-family: var(--font-sans); font-size: 22px; color: #110103; line-height: 1.45;">
          <strong>Nogueira, R., &amp; Cho, K. (2019).</strong> Passage re-ranking with BERT. <em>arXiv preprint arXiv:1901.04085</em>.
        </div>
      </div>

      <!-- Columna 2 -->
      <div style="display: flex; flex-direction: column; justify-content: space-between;">
        <div style="font-family: var(--font-mono); font-size: 18px; font-weight: 800; color: var(--c-red-accent); letter-spacing: 1.5px; border-bottom: 2px solid var(--c-red-accent); padding-bottom: 8px; margin-bottom: 12px;">
          MODELOS SLM Y ARTÍCULO BASE
        </div>

        <div style="background: #FFF9E6; border: 1.5px solid #F5C21B; padding: 14px 16px; margin-bottom: 4px;">
          <div style="font-family: var(--font-mono); font-size: 12px; font-weight: 800; color: #8A6700; margin-bottom: 4px; letter-spacing: 1px;">
            ★ ARTÍCULO BASE DEL BENCHMARK
          </div>
          <div style="padding-left: 28px; text-indent: -28px; font-family: var(--font-sans); font-size: 22px; color: #110103; line-height: 1.45;">
            <strong>Muñoz-Gómez, Y., Hoyos-Cerón, F., &amp; Caiza, J. (2026).</strong> Portable RAG for offline tutoring: A benchmark on rural school hardware. <em>Revista Entramado</em>, 22(2), 1–19.
          </div>
        </div>

        <div style="padding-left: 28px; text-indent: -28px; font-family: var(--font-sans); font-size: 22px; color: #110103; line-height: 1.45;">
          <strong>Abouelenin, A., et al. (2025).</strong> Phi-4-mini technical report: Compact and capable multimodal reasoning. <em>arXiv preprint arXiv:2503.01743</em>.
        </div>

        <div style="padding-left: 28px; text-indent: -28px; font-family: var(--font-sans); font-size: 22px; color: #110103; line-height: 1.45;">
          <strong>Yang, A., et al. (2024).</strong> Qwen2.5 technical report. <em>arXiv preprint arXiv:2412.15115</em>.
        </div>
      </div>

    </div>

    <!-- Remate Doble Regla -->
    <div style="background: #FAF5F5; border-top: 3.5px solid var(--c-wine-primary); border-bottom: 3.5px solid var(--c-wine-primary); padding: 14px 28px; display: flex; align-items: center; justify-content: space-between;">
      <span style="font-family: var(--font-sans); font-size: 22px; font-weight: 600; color: #110103;">
        Investigación presentada en el <strong>VI Congreso Internacional de Investigación Interdisciplinar</strong> · Cartagena 2026
      </span>
      <span style="font-family: var(--font-mono); font-size: 15px; font-weight: 800; color: var(--c-wine-primary);">
        LOHACEMOSXTIC.COM
      </span>
    </div>
  </div>
'''

HTML_PAGE = '''<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <title>Slide 19 Options</title>
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
    options = [
        ("slide19_opcion_a_paneles_estructurados", CONTENT_OPCION_A),
        ("slide19_opcion_b_grid_fichas", CONTENT_OPCION_B),
        ("slide19_opcion_c_sangria_francesa", CONTENT_OPCION_C),
    ]

    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(viewport={"width": 1920, "height": 1080})

        for name, content in options:
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
