# -*- coding: utf-8 -*-
import os
from playwright.sync_api import sync_playwright

# Título sin redundancia numérica (no repite 196 ni 784 que ya están en el banner)
new_title = "Dise&ntilde;o factorial: evaluaci&oacute;n sistem&aacute;tica de b&uacute;squeda, inferencia y varianza"

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
    <h2 class="s-lead-question" style="font-size: 46px; font-weight: 800; margin-bottom: 22px; line-height: 1.2;">
      {new_title}
    </h2>

    <!-- Banner Superior Centrado por Columna -->
    <div style="background: #FAF5F5; border: 2px solid var(--c-wine-primary); padding: 16px 24px; display: flex; align-items: center; justify-content: space-around; margin-bottom: 22px;">
      <!-- Columna 1: 196 -->
      <div style="flex: 1; text-align: center; display: flex; flex-direction: column; align-items: center; justify-content: center;">
        <div style="display: flex; align-items: baseline; justify-content: center; gap: 14px;">
          <span style="font-family: var(--font-mono); font-size: 52px; font-weight: 800; color: var(--c-wine-primary); line-height: 1;">196</span>
          <span style="font-family: var(--font-sans); font-size: 22px; font-weight: 800; color: #110103; letter-spacing: 0.5px;">COMBINACIONES BASE &Uacute;NICAS</span>
        </div>
        <div style="font-family: var(--font-sans); font-size: 19px; color: #555555; font-weight: 600; margin-top: 4px;">
          14 preguntas &times; 7 esquemas RAG &times; 2 modelos SLM
        </div>
      </div>

      <!-- Divisor Vertical -->
      <div style="width: 2px; height: 52px; background: var(--c-border-subtle); flex-shrink: 0;"></div>

      <!-- Columna 2: 784 -->
      <div style="flex: 1; text-align: center; display: flex; flex-direction: column; align-items: center; justify-content: center;">
        <div style="display: flex; align-items: baseline; justify-content: center; gap: 14px;">
          <span style="font-family: var(--font-mono); font-size: 52px; font-weight: 800; color: var(--c-red-accent); line-height: 1;">784</span>
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
# VARIANTE 1: 4 COLORES CON FONDOS TEMÁTICOS SUAVES (Vino, Azul Petróleo, Ámbar, Rojo)
# -------------------------------------------------------------------------
v1_cards = '''
    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 20px; flex-grow: 1;">
      
      <!-- Cuadrante 1: Léxica (Vinotinto) -->
      <div style="background: #FAF5F5; border: 2px solid var(--c-wine-primary); padding: 22px 28px; display: flex; flex-direction: column; justify-content: space-between;">
        <div>
          <div style="font-family: var(--font-mono); font-size: 17px; font-weight: 800; color: var(--c-wine-primary); letter-spacing: 1px; margin-bottom: 6px;">
            RECUPERACI&Oacute;N L&Eacute;XICA
          </div>
          <div style="font-family: var(--font-sans); font-size: 28px; font-weight: 800; color: #110103; margin-bottom: 8px;">
            6 Esquemas BM25
          </div>
          <p style="font-family: var(--font-sans); font-size: 22px; color: #110103; line-height: 1.35; margin: 0;">
            Variaci&oacute;n sistem&aacute;tica de <strong>temperatura (0.1 a 0.7)</strong> y profundidad de recuperaci&oacute;n <strong>top-k (3 a 10 trozos)</strong>.
          </p>
        </div>
        <div style="font-family: var(--font-mono); font-size: 17px; font-weight: 700; color: var(--c-wine-primary); margin-top: 10px;">
          B&uacute;squeda exacta de t&eacute;rminos y palabras clave
        </div>
      </div>

      <!-- Cuadrante 2: Semántica (Azul Petróleo / Slate AI) -->
      <div style="background: #F0F9FF; border: 2px solid #0284C7; padding: 22px 28px; display: flex; flex-direction: column; justify-content: space-between;">
        <div>
          <div style="font-family: var(--font-mono); font-size: 17px; font-weight: 800; color: #0369A1; letter-spacing: 1px; margin-bottom: 6px;">
            RECUPERACI&Oacute;N SEM&Aacute;NTICA
          </div>
          <div style="font-family: var(--font-sans); font-size: 28px; font-weight: 800; color: #110103; margin-bottom: 8px;">
            1 Esquema Denso (Vectorial)
          </div>
          <p style="font-family: var(--font-sans); font-size: 22px; color: #110103; line-height: 1.35; margin: 0;">
            Recuperaci&oacute;n por similitud de <strong>embeddings sem&aacute;nticos</strong> operando a temperatura est&aacute;ndar fija de <strong>0.30</strong>.
          </p>
        </div>
        <div style="font-family: var(--font-mono); font-size: 17px; font-weight: 700; color: #0369A1; margin-top: 10px;">
          Captura relaciones de significado y conceptos afines
        </div>
      </div>

      <!-- Cuadrante 3: Control Estocástico (Dorado Ocre / Ámbar) -->
      <div style="background: #FFFDF0; border: 2px solid #D97706; padding: 22px 28px; display: flex; flex-direction: column; justify-content: space-between;">
        <div>
          <div style="font-family: var(--font-mono); font-size: 17px; font-weight: 800; color: #B45309; letter-spacing: 1px; margin-bottom: 6px;">
            CONTROL ESTOC&Aacute;STICO
          </div>
          <div style="font-family: var(--font-sans); font-size: 28px; font-weight: 800; color: #110103; margin-bottom: 8px;">
            4 Semillas de R&eacute;plica
          </div>
          <p style="font-family: var(--font-sans); font-size: 22px; color: #110103; line-height: 1.35; margin: 0;">
            Ejecuci&oacute;n repetida bajo semillas aleatorias <strong>(42, 7, 123 y 2026)</strong> para medir dispersi&oacute;n real y estabilidad.
          </p>
        </div>
        <div style="font-family: var(--font-mono); font-size: 17px; font-weight: 700; color: #B45309; margin-top: 10px;">
          Evita conclusiones basadas en una corrida fortuita
        </div>
      </div>

      <!-- Cuadrante 4: Auditoría Científica (Rojo Acento) -->
      <div style="background: #FFF5F5; border: 2px solid var(--c-red-accent); padding: 22px 28px; display: flex; flex-direction: column; justify-content: space-between;">
        <div>
          <div style="font-family: var(--font-mono); font-size: 17px; font-weight: 800; color: var(--c-red-accent); letter-spacing: 1px; margin-bottom: 6px;">
            AUDITOR&Iacute;A CIENT&Iacute;FICA
          </div>
          <div style="font-family: var(--font-sans); font-size: 28px; font-weight: 800; color: #110103; margin-bottom: 8px;">
            Doble M&eacute;trica Autom&aacute;tica
          </div>
          <p style="font-family: var(--font-sans); font-size: 22px; color: #110103; line-height: 1.35; margin: 0;">
            Evaluaci&oacute;n cruzada: <strong>coincidencia l&eacute;xica directa</strong> versus <strong>alineaci&oacute;n sem&aacute;ntica</strong> con el libro de texto.
          </p>
        </div>
        <div style="font-family: var(--font-mono); font-size: 17px; font-weight: 700; color: var(--c-red-accent); margin-top: 10px;">
          Auditor&iacute;a objetiva de apego estricto al material
        </div>
      </div>

    </div>
'''

# -------------------------------------------------------------------------
# VARIANTE 2: BORDES Y TAGS DE 4 COLORES SOBRE FONDO CLARO UNIFICADO (#FAF5F5)
# -------------------------------------------------------------------------
v2_cards = '''
    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 20px; flex-grow: 1;">
      
      <!-- Cuadrante 1: Léxica (Vinotinto) -->
      <div style="background: #FAF5F5; border: 2.5px solid var(--c-wine-primary); padding: 22px 28px; display: flex; flex-direction: column; justify-content: space-between;">
        <div>
          <div style="font-family: var(--font-mono); font-size: 17px; font-weight: 800; color: var(--c-wine-primary); letter-spacing: 1px; margin-bottom: 6px;">
            RECUPERACI&Oacute;N L&Eacute;XICA
          </div>
          <div style="font-family: var(--font-sans); font-size: 28px; font-weight: 800; color: #110103; margin-bottom: 8px;">
            6 Esquemas BM25
          </div>
          <p style="font-family: var(--font-sans); font-size: 22px; color: #110103; line-height: 1.35; margin: 0;">
            Variaci&oacute;n sistem&aacute;tica de <strong>temperatura (0.1 a 0.7)</strong> y profundidad de recuperaci&oacute;n <strong>top-k (3 a 10 trozos)</strong>.
          </p>
        </div>
        <div style="font-family: var(--font-mono); font-size: 17px; font-weight: 700; color: var(--c-wine-primary); margin-top: 10px;">
          B&uacute;squeda exacta de t&eacute;rminos y palabras clave
        </div>
      </div>

      <!-- Cuadrante 2: Semántica (Azul Petróleo) -->
      <div style="background: #FAF5F5; border: 2.5px solid #0284C7; padding: 22px 28px; display: flex; flex-direction: column; justify-content: space-between;">
        <div>
          <div style="font-family: var(--font-mono); font-size: 17px; font-weight: 800; color: #0369A1; letter-spacing: 1px; margin-bottom: 6px;">
            RECUPERACI&Oacute;N SEM&Aacute;NTICA
          </div>
          <div style="font-family: var(--font-sans); font-size: 28px; font-weight: 800; color: #110103; margin-bottom: 8px;">
            1 Esquema Denso (Vectorial)
          </div>
          <p style="font-family: var(--font-sans); font-size: 22px; color: #110103; line-height: 1.35; margin: 0;">
            Recuperaci&oacute;n por similitud de <strong>embeddings sem&aacute;nticos</strong> operando a temperatura est&aacute;ndar fija de <strong>0.30</strong>.
          </p>
        </div>
        <div style="font-family: var(--font-mono); font-size: 17px; font-weight: 700; color: #0369A1; margin-top: 10px;">
          Captura relaciones de significado y conceptos afines
        </div>
      </div>

      <!-- Cuadrante 3: Control Estocástico (Dorado Ocre) -->
      <div style="background: #FAF5F5; border: 2.5px solid #D97706; padding: 22px 28px; display: flex; flex-direction: column; justify-content: space-between;">
        <div>
          <div style="font-family: var(--font-mono); font-size: 17px; font-weight: 800; color: #B45309; letter-spacing: 1px; margin-bottom: 6px;">
            CONTROL ESTOC&Aacute;STICO
          </div>
          <div style="font-family: var(--font-sans); font-size: 28px; font-weight: 800; color: #110103; margin-bottom: 8px;">
            4 Semillas de R&eacute;plica
          </div>
          <p style="font-family: var(--font-sans); font-size: 22px; color: #110103; line-height: 1.35; margin: 0;">
            Ejecuci&oacute;n repetida bajo semillas aleatorias <strong>(42, 7, 123 y 2026)</strong> para medir dispersi&oacute;n real y estabilidad.
          </p>
        </div>
        <div style="font-family: var(--font-mono); font-size: 17px; font-weight: 700; color: #B45309; margin-top: 10px;">
          Evita conclusiones basadas en una corrida fortuita
        </div>
      </div>

      <!-- Cuadrante 4: Auditoría Científica (Rojo Acento) -->
      <div style="background: #FAF5F5; border: 2.5px solid var(--c-red-accent); padding: 22px 28px; display: flex; flex-direction: column; justify-content: space-between;">
        <div>
          <div style="font-family: var(--font-mono); font-size: 17px; font-weight: 800; color: var(--c-red-accent); letter-spacing: 1px; margin-bottom: 6px;">
            AUDITOR&Iacute;A CIENT&Iacute;FICA
          </div>
          <div style="font-family: var(--font-sans); font-size: 28px; font-weight: 800; color: #110103; margin-bottom: 8px;">
            Doble M&eacute;trica Autom&aacute;tica
          </div>
          <p style="font-family: var(--font-sans); font-size: 22px; color: #110103; line-height: 1.35; margin: 0;">
            Evaluaci&oacute;n cruzada: <strong>coincidencia l&eacute;xica directa</strong> versus <strong>alineaci&oacute;n sem&aacute;ntica</strong> con el libro de texto.
          </p>
        </div>
        <div style="font-family: var(--font-mono); font-size: 17px; font-weight: 700; color: var(--c-red-accent); margin-top: 10px;">
          Auditor&iacute;a objetiva de apego estricto al material
        </div>
      </div>

    </div>
'''

options = {
    "slide_10_colores_fondos.png": v1_cards,
    "slide_10_colores_bordes.png": v2_cards,
}

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page(viewport={"width": 1920, "height": 1080})

    for img_name, cards_content in options.items():
        full_html = base_header + cards_content + base_footer
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

print("Color options for slide 10 generated.")
