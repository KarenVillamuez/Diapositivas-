# -*- coding: utf-8 -*-
import os
from playwright.sync_api import sync_playwright

title_text = "Dise&ntilde;o factorial: evaluaci&oacute;n sistem&aacute;tica de b&uacute;squeda, inferencia y varianza"

# Base header con título más pequeño (38px en vez de 46px)
def get_header(banner_style):
    return f'''<!-- ====================================================================
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

    <!-- Banner Superior Centrado con Estilo Neutro -->
    <div style="{banner_style}">
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

      <!-- Divisor Vertical Neutro -->
      <div style="width: 2px; height: 52px; background: #D5C8C9; flex-shrink: 0;"></div>

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

# 4 Cuadrantes con la paleta A1 aprobada (Vino, Azul, Ámbar, Rojo)
cards_content = '''
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

# Variantes de estilo para el Banner Superior:
# Opción 1: Fondo Blanco Puro con Borde Neutral Grafito (#8D7A7D / #B0A0A3)
b1_style = "background: #FFFFFF; border: 2px solid #9E8D90; padding: 16px 24px; display: flex; align-items: center; justify-content: space-around; margin-bottom: 22px;"

# Opción 2: Fondo Blanco Puro con Borde Carbón Profundo (#2C0509 / #110103)
b2_style = "background: #FFFFFF; border: 2px solid #2C0509; padding: 16px 24px; display: flex; align-items: center; justify-content: space-around; margin-bottom: 22px;"

# Opción 3: Fondo Gris Neutro Muy Claro (#F8F8F9) con Borde Sutil (#D0D0D5)
b3_style = "background: #F8F8FA; border: 2px solid #CBD5E1; padding: 16px 24px; display: flex; align-items: center; justify-content: space-around; margin-bottom: 22px;"

variations = {
    "slide_10_banner_blanco_grafito.png": b1_style,
    "slide_10_banner_blanco_carbon.png": b2_style,
    "slide_10_banner_gris_neutro.png": b3_style,
}

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page(viewport={"width": 1920, "height": 1080})

    for img_name, b_style in variations.items():
        full_html = get_header(b_style) + cards_content + base_footer
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

print("All banner variations captured.")
