# -*- coding: utf-8 -*-
import os
from playwright.sync_api import sync_playwright

base_header = '''<!-- ====================================================================
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
      Espacio de par&aacute;metros: 196 combinaciones y 784 inferencias registradas
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

# -------------------------------------------------------------------------
# OPCIÓN A: BANNER SUPERIOR DE MÉTRICAS + MATRIZ 2x2 EQUILIBRADA (Sin cajas anidadas)
# -------------------------------------------------------------------------
opcion_a_content = '''
    <!-- Barra Superior de Ecuación Factorial -->
    <div style="background: #FAF5F5; border: 2px solid var(--c-wine-primary); padding: 14px 28px; display: flex; align-items: center; justify-content: space-between; margin-bottom: 22px;">
      <div style="display: flex; align-items: baseline; gap: 16px;">
        <span style="font-family: var(--font-mono); font-size: 50px; font-weight: 800; color: var(--c-wine-primary); line-height: 1;">196</span>
        <div>
          <div style="font-family: var(--font-sans); font-size: 21px; font-weight: 800; color: #110103;">COMBINACIONES BASE &Uacute;NICAS</div>
          <div style="font-family: var(--font-sans); font-size: 18px; color: #555555; font-weight: 600;">14 preguntas &times; 7 esquemas RAG &times; 2 modelos SLM</div>
        </div>
      </div>

      <div style="width: 2px; height: 48px; background: var(--c-border-subtle);"></div>

      <div style="display: flex; align-items: baseline; gap: 16px;">
        <span style="font-family: var(--font-mono); font-size: 50px; font-weight: 800; color: var(--c-red-accent); line-height: 1;">784</span>
        <div>
          <div style="font-family: var(--font-sans); font-size: 21px; font-weight: 800; color: #110103;">INFERENCIAS AUDITADAS</div>
          <div style="font-family: var(--font-sans); font-size: 18px; color: #555555; font-weight: 600;">196 combinaciones &times; 4 r&eacute;plicas estoc&aacute;sticas independientes</div>
        </div>
      </div>
    </div>

    <!-- Cuadrícula 2x2 de Parámetros -->
    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 20px; flex-grow: 1;">
      
      <!-- Cuadrante 1: Configuración Léxica -->
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

      <!-- Cuadrante 2: Configuración Semántica -->
      <div style="background: #FAF5F5; border: 2px solid var(--c-wine-primary); padding: 22px 28px; display: flex; flex-direction: column; justify-content: space-between;">
        <div>
          <div style="font-family: var(--font-mono); font-size: 17px; font-weight: 800; color: var(--c-wine-primary); letter-spacing: 1px; margin-bottom: 6px;">
            RECUPERACI&Oacute;N SEM&Aacute;NTICA
          </div>
          <div style="font-family: var(--font-sans); font-size: 28px; font-weight: 800; color: #110103; margin-bottom: 8px;">
            1 Esquema Denso (Vectorial)
          </div>
          <p style="font-family: var(--font-sans); font-size: 22px; color: #110103; line-height: 1.35; margin: 0;">
            Recuperaci&oacute;n por similitud de <strong>embeddings sem&aacute;nticos</strong> operando a temperatura est&aacute;ndar fija de <strong>0.30</strong>.
          </p>
        </div>
        <div style="font-family: var(--font-mono); font-size: 17px; font-weight: 700; color: var(--c-wine-primary); margin-top: 10px;">
          Captura relaciones de significado y conceptos afines
        </div>
      </div>

      <!-- Cuadrante 3: Control Estocástico -->
      <div style="background: #FAF5F5; border: 2px solid var(--c-wine-primary); padding: 22px 28px; display: flex; flex-direction: column; justify-content: space-between;">
        <div>
          <div style="font-family: var(--font-mono); font-size: 17px; font-weight: 800; color: var(--c-wine-primary); letter-spacing: 1px; margin-bottom: 6px;">
            CONTROL ESTOC&Aacute;STICO
          </div>
          <div style="font-family: var(--font-sans); font-size: 28px; font-weight: 800; color: #110103; margin-bottom: 8px;">
            4 Semillas de R&eacute;plica
          </div>
          <p style="font-family: var(--font-sans); font-size: 22px; color: #110103; line-height: 1.35; margin: 0;">
            Ejecuci&oacute;n repetida bajo semillas aleatorias <strong>(42, 7, 123 y 2026)</strong> para medir dispersi&oacute;n real y estabilidad.
          </p>
        </div>
        <div style="font-family: var(--font-mono); font-size: 17px; font-weight: 700; color: var(--c-wine-primary); margin-top: 10px;">
          Evita conclusiones basadas en una corrida fortuita
        </div>
      </div>

      <!-- Cuadrante 4: Protocolo de Evaluación -->
      <div style="background: #FAF5F5; border: 2px solid var(--c-wine-primary); padding: 22px 28px; display: flex; flex-direction: column; justify-content: space-between;">
        <div>
          <div style="font-family: var(--font-mono); font-size: 17px; font-weight: 800; color: var(--c-wine-primary); letter-spacing: 1px; margin-bottom: 6px;">
            AUDITOR&Iacute;A CIENT&Iacute;FICA
          </div>
          <div style="font-family: var(--font-sans); font-size: 28px; font-weight: 800; color: #110103; margin-bottom: 8px;">
            Doble M&eacute;trica Autom&aacute;tica
          </div>
          <p style="font-family: var(--font-sans); font-size: 22px; color: #110103; line-height: 1.35; margin: 0;">
            Evaluaci&oacute;n cruzada: <strong>coincidencia l&eacute;xica directa</strong> versus <strong>alineaci&oacute;n sem&aacute;ntica</strong> con el libro de texto.
          </p>
        </div>
        <div style="font-family: var(--font-mono); font-size: 17px; font-weight: 700; color: var(--c-wine-primary); margin-top: 10px;">
          Auditor&iacute;a objetiva de apego estricto al material
        </div>
      </div>

    </div>
'''

# -------------------------------------------------------------------------
# OPCIÓN B: DOS COLUMNAS EDITORIALES LIMPIAS (Sin cuadros anidados)
# -------------------------------------------------------------------------
opcion_b_content = '''
    <div style="display: flex; gap: 26px; align-items: stretch; flex-grow: 1;">
      
      <!-- Columna 1: El Espacio Factorial (196 Combinaciones) -->
      <div style="flex: 1.1; background: #FAF5F5; border: 2px solid var(--c-wine-primary); padding: 28px 32px; display: flex; flex-direction: column; justify-content: space-between;">
        <div>
          <div style="display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 8px;">
            <span style="font-family: var(--font-mono); font-size: 18px; font-weight: 800; color: var(--c-wine-primary); letter-spacing: 1px;">
              DIMENSI&Oacute;N FACTORIAL
            </span>
            <span style="font-family: var(--font-mono); font-size: 44px; font-weight: 800; color: var(--c-wine-primary); line-height: 1;">
              196
            </span>
          </div>
          
          <div style="font-family: var(--font-sans); font-size: 30px; font-weight: 800; color: #110103; margin-bottom: 16px;">
            Combinaciones Base &Uacute;nicas
          </div>
          
          <div style="width: 100%; height: 2px; background: var(--c-border-subtle); margin-bottom: 20px;"></div>
          
          <div style="display: flex; flex-direction: column; gap: 18px;">
            <div style="border-bottom: 1px solid var(--c-border-subtle); padding-bottom: 12px; display: flex; justify-content: space-between; align-items: center;">
              <div>
                <div style="font-family: var(--font-sans); font-size: 23px; font-weight: 800; color: #110103;">14 Preguntas</div>
                <div style="font-family: var(--font-sans); font-size: 19px; color: #555555;">Banco curricular de ciencias y lenguaje</div>
              </div>
              <span style="font-family: var(--font-mono); font-size: 19px; font-weight: 700; color: var(--c-wine-primary);">12 + 2 Sondas</span>
            </div>

            <div style="border-bottom: 1px solid var(--c-border-subtle); padding-bottom: 12px; display: flex; justify-content: space-between; align-items: center;">
              <div>
                <div style="font-family: var(--font-sans); font-size: 23px; font-weight: 800; color: #110103;">7 Esquemas RAG</div>
                <div style="font-family: var(--font-sans); font-size: 19px; color: #555555;">Par&aacute;metros top-k (3 a 10) y Temp (0.1 a 0.7)</div>
              </div>
              <span style="font-family: var(--font-mono); font-size: 19px; font-weight: 700; color: var(--c-wine-primary);">6 BM25 + 1 Denso</span>
            </div>

            <div style="padding-bottom: 4px; display: flex; justify-content: space-between; align-items: center;">
              <div>
                <div style="font-family: var(--font-sans); font-size: 23px; font-weight: 800; color: #110103;">2 Modelos SLM</div>
                <div style="font-family: var(--font-sans); font-size: 19px; color: #555555;">Cuantizaci&oacute;n GGUF Q4_K_M para CPU local</div>
              </div>
              <span style="font-family: var(--font-mono); font-size: 19px; font-weight: 700; color: var(--c-wine-primary);">Phi-4 &middot; Qwen2.5</span>
            </div>
          </div>
        </div>

        <div style="margin-top: 20px; padding-top: 14px; border-top: 2px dashed var(--c-border-subtle); font-family: var(--font-mono); font-size: 21px; font-weight: 800; color: var(--c-wine-primary); text-align: center;">
          14 PREGUNTAS &times; 7 ESQUEMAS &times; 2 MODELOS = 196
        </div>
      </div>

      <!-- Columna 2: Protocolo de Rigor y Réplicas (784 Inferencias) -->
      <div style="flex: 1; background: #FAF5F5; border: 2px solid var(--c-wine-primary); padding: 28px 32px; display: flex; flex-direction: column; justify-content: space-between;">
        <div>
          <div style="display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 8px;">
            <span style="font-family: var(--font-mono); font-size: 18px; font-weight: 800; color: var(--c-red-accent); letter-spacing: 1px;">
              RIGOR EXPERIMENTAL
            </span>
            <span style="font-family: var(--font-mono); font-size: 44px; font-weight: 800; color: var(--c-red-accent); line-height: 1;">
              784
            </span>
          </div>
          
          <div style="font-family: var(--font-sans); font-size: 30px; font-weight: 800; color: #110103; margin-bottom: 16px;">
            Inferencias Registradas
          </div>
          
          <div style="width: 100%; height: 2px; background: var(--c-border-subtle); margin-bottom: 20px;"></div>
          
          <div style="display: flex; flex-direction: column; gap: 18px;">
            <div style="border-bottom: 1px solid var(--c-border-subtle); padding-bottom: 12px;">
              <div style="font-family: var(--font-sans); font-size: 23px; font-weight: 800; color: #110103; margin-bottom: 4px;">
                4 Semillas Aleatorias de R&eacute;plica
              </div>
              <div style="font-family: var(--font-mono); font-size: 19px; color: var(--c-wine-primary); font-weight: 700; margin-bottom: 4px;">
                Semillas: 42 &middot; 7 &middot; 123 &middot; 2026
              </div>
              <div style="font-family: var(--font-sans); font-size: 19px; color: #555555; line-height: 1.35;">
                Auditan la dispersi&oacute;n estoc&aacute;stica para evitar conclusiones sesgadas por una corrida fortuita.
              </div>
            </div>

            <div style="padding-bottom: 4px;">
              <div style="font-family: var(--font-sans); font-size: 23px; font-weight: 800; color: #110103; margin-bottom: 4px;">
                Auditor&iacute;a de Fidelidad Curricular
              </div>
              <div style="font-family: var(--font-sans); font-size: 19px; color: #555555; line-height: 1.35;">
                Doble criterio autom&aacute;tico objetivo: solapamiento l&eacute;xico estricto y similitud sem&aacute;ntica con los pasajes del libro.
              </div>
            </div>
          </div>
        </div>

        <div style="margin-top: 20px; padding-top: 14px; border-top: 2px dashed var(--c-border-subtle); font-family: var(--font-mono); font-size: 21px; font-weight: 800; color: var(--c-red-accent); text-align: center;">
          196 COMBINACIONES &times; 4 SEMILLAS = 784 INFERENCIAS
        </div>
      </div>

    </div>
'''

# -------------------------------------------------------------------------
# OPCIÓN C: TRÍPTICO DE 3 PILARES TÉCNICOS + BARRA INFERIOR DE TOTALES
# -------------------------------------------------------------------------
opcion_c_content = '''
    <div style="display: flex; gap: 20px; align-items: stretch; flex-grow: 1; margin-bottom: 22px;">
      
      <!-- Pilar 1: Búsqueda y RAG -->
      <div style="flex: 1; background: #FAF5F5; border: 2px solid var(--c-wine-primary); padding: 26px 24px; display: flex; flex-direction: column; justify-content: space-between;">
        <div>
          <div style="font-family: var(--font-mono); font-size: 16px; font-weight: 800; color: var(--c-wine-primary); letter-spacing: 1px; margin-bottom: 6px;">
            PILAR 01 &middot; RECUPERACI&Oacute;N
          </div>
          <div style="font-family: var(--font-sans); font-size: 28px; font-weight: 800; color: #110103; margin-bottom: 14px;">
            7 Esquemas RAG
          </div>
          <ul style="font-family: var(--font-sans); font-size: 21px; color: #110103; line-height: 1.45; padding-left: 20px; margin: 0;">
            <li style="margin-bottom: 10px;"><strong>6 BM25 L&eacute;xicos:</strong> Temperaturas de 0.1 a 0.7; top-k de 3 a 10 fragmentos.</li>
            <li><strong>1 Denso Sem&aacute;ntico:</strong> Embeddings vectoriales a temperatura fija 0.30.</li>
          </ul>
        </div>
        <div style="font-family: var(--font-mono); font-size: 16px; font-weight: 700; color: var(--c-wine-primary); padding-top: 10px; border-top: 1px dashed var(--c-border-subtle);">
          Explora l&eacute;xico vs. sem&aacute;ntica
        </div>
      </div>

      <!-- Pilar 2: Modelos SLM Locales -->
      <div style="flex: 1; background: #FAF5F5; border: 2px solid var(--c-wine-primary); padding: 26px 24px; display: flex; flex-direction: column; justify-content: space-between;">
        <div>
          <div style="font-family: var(--font-mono); font-size: 16px; font-weight: 800; color: var(--c-wine-primary); letter-spacing: 1px; margin-bottom: 6px;">
            PILAR 02 &middot; GENERACI&Oacute;N
          </div>
          <div style="font-family: var(--font-sans); font-size: 28px; font-weight: 800; color: #110103; margin-bottom: 14px;">
            2 Modelos SLM
          </div>
          <ul style="font-family: var(--font-sans); font-size: 21px; color: #110103; line-height: 1.45; padding-left: 20px; margin: 0;">
            <li style="margin-bottom: 10px;"><strong>Phi-4-mini-instruct:</strong> 3.8B par&aacute;metros en cuantizaci&oacute;n GGUF Q4_K_M.</li>
            <li><strong>Qwen2.5-3B-Instruct:</strong> 3.0B par&aacute;metros en cuantizaci&oacute;n GGUF Q4_K_M.</li>
          </ul>
        </div>
        <div style="font-family: var(--font-mono); font-size: 16px; font-weight: 700; color: var(--c-wine-primary); padding-top: 10px; border-top: 1px dashed var(--c-border-subtle);">
          Inferencia &le; 3.8 GB RAM en CPU
        </div>
      </div>

      <!-- Pilar 3: Control Estocástico -->
      <div style="flex: 1; background: #FAF5F5; border: 2px solid var(--c-wine-primary); padding: 26px 24px; display: flex; flex-direction: column; justify-content: space-between;">
        <div>
          <div style="font-family: var(--font-mono); font-size: 16px; font-weight: 800; color: var(--c-wine-primary); letter-spacing: 1px; margin-bottom: 6px;">
            PILAR 03 &middot; CONTROL
          </div>
          <div style="font-family: var(--font-sans); font-size: 28px; font-weight: 800; color: #110103; margin-bottom: 14px;">
            4 Semillas Aleatorias
          </div>
          <ul style="font-family: var(--font-sans); font-size: 21px; color: #110103; line-height: 1.45; padding-left: 20px; margin: 0;">
            <li style="margin-bottom: 10px;">Semillas: <strong>42, 7, 123 y 2026</strong>.</li>
            <li style="margin-bottom: 10px;">Mide dispersi&oacute;n y reproducibilidad estricta.</li>
            <li>Doble m&eacute;trica: apego l&eacute;xico y coherencia sem&aacute;ntica.</li>
          </ul>
        </div>
        <div style="font-family: var(--font-mono); font-size: 16px; font-weight: 700; color: var(--c-wine-primary); padding-top: 10px; border-top: 1px dashed var(--c-border-subtle);">
          Cero sesgo de corrida &uacute;nica
        </div>
      </div>

    </div>

    <!-- Barra Inferior de Totales en Línea Abierta -->
    <div style="font-family: var(--font-sans); font-size: 25px; color: #110103; font-weight: 800; display: flex; align-items: center; justify-content: space-between;">
      <div>
        <span style="color: var(--c-wine-primary);">196 COMBINACIONES BASE:</span> 14 Preguntas &times; 7 Esquemas &times; 2 Modelos
      </div>
      <div>
        <span style="color: var(--c-red-accent);">784 INFERENCIAS:</span> 196 Combinaciones &times; 4 Semillas de r&eacute;plica
      </div>
    </div>
'''

options = {
    "slide_10_opcion_a.png": opcion_a_content,
    "slide_10_opcion_b.png": opcion_b_content,
    "slide_10_opcion_c.png": opcion_c_content,
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

print("All Slide 10 options regenerated successfully.")
