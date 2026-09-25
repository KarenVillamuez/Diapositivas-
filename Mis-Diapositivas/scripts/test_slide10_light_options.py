# -*- coding: utf-8 -*-
import os
from playwright.sync_api import sync_playwright

title_text = "Dise&ntilde;o factorial: evaluaci&oacute;n sistem&aacute;tica de b&uacute;squeda, inferencia y varianza"

base_header = f'''<!-- ====================================================================
     SLIDE 10: 02 · METODOLOGÍA / MATRIZ EXPERIMENTAL
     ==================================================================== -->
<section class="slide s-white" id="slide-10">
  <header class="slide-header">
    <div class="sh-left">
      <span class="sh-red-bar"></span>
      <span class="sh-category">02 &middot; METODOLOG&Iacute;A &middot; MATRIZ EXPERIMENTAL</span>
    </div>
    <img src="assets/image6.png" alt="#LoxTIC" class="sh-loxtic">
  </header>
  <div class="sh-divider"></div>

  <div class="slide-content-area" style="justify-content: flex-start; padding-top: 10px; padding-bottom: 20px;">
    <h2 class="s-lead-question" style="font-size: 38px; font-weight: 800; margin-bottom: 20px; line-height: 1.25;">
      {title_text}
    </h2>

    <!-- Banner Superior Centrado Blanco Neutro -->
    <div style="background: #FFFFFF; border: 2px solid #2C0509; padding: 14px 24px; display: flex; align-items: center; justify-content: space-around; margin-bottom: 22px;">
      <!-- Columna 1: 196 -->
      <div style="flex: 1; text-align: center; display: flex; flex-direction: column; align-items: center; justify-content: center;">
        <div style="display: flex; align-items: baseline; justify-content: center; gap: 14px;">
          <span style="font-family: var(--font-mono); font-size: 50px; font-weight: 800; color: var(--c-wine-primary); line-height: 1;">196</span>
          <span style="font-family: var(--font-sans); font-size: 22px; font-weight: 800; color: #110103; letter-spacing: 0.5px;">COMBINACIONES BASE &Uacute;NICAS</span>
        </div>
        <div style="font-family: var(--font-sans); font-size: 19px; color: #555555; font-weight: 600; margin-top: 4px;">
          14 preguntas &times; 7 esquemas RAG &times; 2 modelos SLM
        </div>
      </div>

      <!-- Divisor Vertical Neutro -->
      <div style="width: 2px; height: 50px; background: #D5C8C9; flex-shrink: 0;"></div>

      <!-- Columna 2: 784 -->
      <div style="flex: 1; text-align: center; display: flex; flex-direction: column; align-items: center; justify-content: center;">
        <div style="display: flex; align-items: baseline; justify-content: center; gap: 14px;">
          <span style="font-family: var(--font-mono); font-size: 50px; font-weight: 800; color: var(--c-red-accent); line-height: 1;">784</span>
          <span style="font-family: var(--font-sans); font-size: 22px; font-weight: 800; color: #110103; letter-spacing: 0.5px;">INFERENCIAS AUDITADAS</span>
        </div>
        <div style="font-family: var(--font-sans); font-size: 19px; color: #555555; font-weight: 600; margin-top: 4px;">
          196 combinaciones &times; 4 r&eacute;plicas estoc&aacute;sticas independientes
        </div>
      </div>
    </div>
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

# -------------------------------------------------------------------------
# OPCIÓN D3: EDITORIAL ULTRA-LIMPIA (Sin cuadros anidados, parámetros en monospace destacado)
# -------------------------------------------------------------------------
opcion_d3_content = '''
    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 20px; flex-grow: 1;">
      
      <!-- Cuadrante 1: Léxica (Vinotinto) -->
      <div style="background: #FAF5F5; border: 2px solid var(--c-wine-primary); padding: 24px 30px; display: flex; flex-direction: column; justify-content: space-between;">
        <div>
          <div style="font-family: var(--font-mono); font-size: 17px; font-weight: 800; color: var(--c-wine-primary); letter-spacing: 1px; margin-bottom: 6px;">
            RECUPERACI&Oacute;N L&Eacute;XICA
          </div>
          <div style="font-family: var(--font-sans); font-size: 30px; font-weight: 800; color: #110103; margin-bottom: 12px;">
            6 Esquemas BM25
          </div>
          <div style="font-family: var(--font-mono); font-size: 22px; font-weight: 800; color: var(--c-wine-primary); margin-bottom: 10px;">
            top-k: 3 &ndash; 10 &nbsp;&bull;&nbsp; Temp: 0.1 &ndash; 0.7
          </div>
        </div>
        <div style="font-family: var(--font-sans); font-size: 22px; color: #110103; font-weight: 600; line-height: 1.35;">
          B&uacute;squeda exacta de t&eacute;rminos y palabras clave del libro.
        </div>
      </div>

      <!-- Cuadrante 2: Semántica (Azul Petróleo) -->
      <div style="background: #F0F9FF; border: 2px solid #0284C7; padding: 24px 30px; display: flex; flex-direction: column; justify-content: space-between;">
        <div>
          <div style="font-family: var(--font-mono); font-size: 17px; font-weight: 800; color: #0369A1; letter-spacing: 1px; margin-bottom: 6px;">
            RECUPERACI&Oacute;N SEM&Aacute;NTICA
          </div>
          <div style="font-family: var(--font-sans); font-size: 30px; font-weight: 800; color: #110103; margin-bottom: 12px;">
            1 Esquema Denso (Vectorial)
          </div>
          <div style="font-family: var(--font-mono); font-size: 22px; font-weight: 800; color: #0369A1; margin-bottom: 10px;">
            Embeddings MiniLM &nbsp;&bull;&nbsp; Temp: 0.30 fija
          </div>
        </div>
        <div style="font-family: var(--font-sans); font-size: 22px; color: #110103; font-weight: 600; line-height: 1.35;">
          Captura proximidad conceptual y significado contextual.
        </div>
      </div>

      <!-- Cuadrante 3: Control Estocástico (Ámbar) -->
      <div style="background: #FFFDF0; border: 2px solid #D97706; padding: 24px 30px; display: flex; flex-direction: column; justify-content: space-between;">
        <div>
          <div style="font-family: var(--font-mono); font-size: 17px; font-weight: 800; color: #B45309; letter-spacing: 1px; margin-bottom: 6px;">
            CONTROL ESTOC&Aacute;STICO
          </div>
          <div style="font-family: var(--font-sans); font-size: 30px; font-weight: 800; color: #110103; margin-bottom: 12px;">
            4 Semillas de R&eacute;plica
          </div>
          <div style="font-family: var(--font-mono); font-size: 22px; font-weight: 800; color: #B45309; margin-bottom: 10px;">
            Semillas: 42 &middot; 7 &middot; 123 &middot; 2026
          </div>
        </div>
        <div style="font-family: var(--font-sans); font-size: 22px; color: #110103; font-weight: 600; line-height: 1.35;">
          Auditor&iacute;a de dispersi&oacute;n: descarta sesgo de corrida &uacute;nica.
        </div>
      </div>

      <!-- Cuadrante 4: Auditoría Científica (Rojo) -->
      <div style="background: #FFF5F5; border: 2px solid var(--c-red-accent); padding: 24px 30px; display: flex; flex-direction: column; justify-content: space-between;">
        <div>
          <div style="font-family: var(--font-mono); font-size: 17px; font-weight: 800; color: var(--c-red-accent); letter-spacing: 1px; margin-bottom: 6px;">
            AUDITOR&Iacute;A CIENT&Iacute;FICA
          </div>
          <div style="font-family: var(--font-sans); font-size: 30px; font-weight: 800; color: #110103; margin-bottom: 12px;">
            Doble M&eacute;trica de Fidelidad
          </div>
          <div style="font-family: var(--font-mono); font-size: 22px; font-weight: 800; color: var(--c-red-accent); margin-bottom: 10px;">
            Apego L&eacute;xico &nbsp;+&nbsp; Similitud Sem&aacute;ntica
          </div>
        </div>
        <div style="font-family: var(--font-sans); font-size: 22px; color: #110103; font-weight: 600; line-height: 1.35;">
          Contraste ciego frente al pasaje curricular original.
        </div>
      </div>

    </div>
'''

# -------------------------------------------------------------------------
# OPCIÓN D2: NÚMEROS GIGANTES 6 · 1 · 4 · 2
# -------------------------------------------------------------------------
opcion_d2_content = '''
    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 20px; flex-grow: 1;">
      
      <!-- Cuadrante 1: BM25 -->
      <div style="background: #FAF5F5; border: 2px solid var(--c-wine-primary); padding: 24px 28px; display: flex; align-items: center; gap: 24px;">
        <div style="font-family: var(--font-mono); font-size: 72px; font-weight: 800; color: var(--c-wine-primary); line-height: 1; flex-shrink: 0; width: 65px; text-align: center;">
          6
        </div>
        <div style="width: 2px; height: 80px; background: rgba(70, 8, 17, 0.2); flex-shrink: 0;"></div>
        <div>
          <div style="font-family: var(--font-sans); font-size: 28px; font-weight: 800; color: #110103; margin-bottom: 6px;">
            Esquemas BM25
          </div>
          <div style="font-family: var(--font-mono); font-size: 22px; font-weight: 700; color: var(--c-wine-primary);">
            top-k: 3 &ndash; 10 &nbsp;&bull;&nbsp; Temp: 0.1 &ndash; 0.7
          </div>
          <div style="font-family: var(--font-sans); font-size: 21px; color: #444444; margin-top: 4px; font-weight: 500;">
            Recuperaci&oacute;n l&eacute;xica por coincidencia exacta
          </div>
        </div>
      </div>

      <!-- Cuadrante 2: Denso -->
      <div style="background: #F0F9FF; border: 2px solid #0284C7; padding: 24px 28px; display: flex; align-items: center; gap: 24px;">
        <div style="font-family: var(--font-mono); font-size: 72px; font-weight: 800; color: #0284C7; line-height: 1; flex-shrink: 0; width: 65px; text-align: center;">
          1
        </div>
        <div style="width: 2px; height: 80px; background: rgba(2, 132, 199, 0.2); flex-shrink: 0;"></div>
        <div>
          <div style="font-family: var(--font-sans); font-size: 28px; font-weight: 800; color: #110103; margin-bottom: 6px;">
            Esquema Denso
          </div>
          <div style="font-family: var(--font-mono); font-size: 22px; font-weight: 700; color: #0369A1;">
            Embeddings &nbsp;&bull;&nbsp; Temp: 0.30 fija
          </div>
          <div style="font-family: var(--font-sans); font-size: 21px; color: #444444; margin-top: 4px; font-weight: 500;">
            Recuperaci&oacute;n vectorial sem&aacute;ntica
          </div>
        </div>
      </div>

      <!-- Cuadrante 3: Semillas -->
      <div style="background: #FFFDF0; border: 2px solid #D97706; padding: 24px 28px; display: flex; align-items: center; gap: 24px;">
        <div style="font-family: var(--font-mono); font-size: 72px; font-weight: 800; color: #D97706; line-height: 1; flex-shrink: 0; width: 65px; text-align: center;">
          4
        </div>
        <div style="width: 2px; height: 80px; background: rgba(217, 119, 6, 0.2); flex-shrink: 0;"></div>
        <div>
          <div style="font-family: var(--font-sans); font-size: 28px; font-weight: 800; color: #110103; margin-bottom: 6px;">
            Semillas de R&eacute;plica
          </div>
          <div style="font-family: var(--font-mono); font-size: 22px; font-weight: 700; color: #B45309;">
            42 &middot; 7 &middot; 123 &middot; 2026
          </div>
          <div style="font-family: var(--font-sans); font-size: 21px; color: #444444; margin-top: 4px; font-weight: 500;">
            Control estoc&aacute;stico y dispersi&oacute;n
          </div>
        </div>
      </div>

      <!-- Cuadrante 4: Métricas -->
      <div style="background: #FFF5F5; border: 2px solid var(--c-red-accent); padding: 24px 28px; display: flex; align-items: center; gap: 24px;">
        <div style="font-family: var(--font-mono); font-size: 72px; font-weight: 800; color: var(--c-red-accent); line-height: 1; flex-shrink: 0; width: 65px; text-align: center;">
          2
        </div>
        <div style="width: 2px; height: 80px; background: rgba(201, 16, 27, 0.2); flex-shrink: 0;"></div>
        <div>
          <div style="font-family: var(--font-sans); font-size: 28px; font-weight: 800; color: #110103; margin-bottom: 6px;">
            M&eacute;tricas de Auditor&iacute;a
          </div>
          <div style="font-family: var(--font-mono); font-size: 22px; font-weight: 700; color: var(--c-red-accent);">
            L&eacute;xica + Sem&aacute;ntica
          </div>
          <div style="font-family: var(--font-sans); font-size: 21px; color: #444444; margin-top: 4px; font-weight: 500;">
            Fidelidad estricta al libro de texto
          </div>
        </div>
      </div>

    </div>
'''

options = {
    "slide_10_opcion_d3_editorial.png": opcion_d3_content,
    "slide_10_opcion_d2_numeros.png": opcion_d2_content,
}

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page(viewport={"width": 1920, "height": 1080})

    for img_name, content in options.items():
        full_html = base_header + content + base_footer
        with open("slides/slide_10.html", "w", encoding="utf-8") as f:
            f.write(full_html)
        os.system("python scripts/build.py")
        page.goto(f"http://localhost:8085/?opt={img_name}#slide-10")
        page.wait_for_load_state("networkidle")
        page.evaluate('''
            const slides = document.querySelectorAll('.slide');
            slides.forEach((s, idx) => {
                if (idx === 9) s.classList.add('active');
                else s.classList.remove('active');
            });
        ''')
        page.wait_for_timeout(350)
        page.screenshot(path=img_name)
        print(f"Captured {img_name}")

    browser.close()

print("Options D3 and D2 generated.")
