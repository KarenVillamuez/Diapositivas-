# -*- coding: utf-8 -*-
"""
Genera y captura las 3 opciones de diseño para el Slide 7:
(02 · Metodología / Pipeline RAG en Hardware de Aula)
"""
import os
from playwright.sync_api import sync_playwright

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ARTIFACT_DIR = r"C:\Users\ASUS\.gemini\antigravity-ide\brain\a6624504-511c-4b9d-bc9a-468e348bde40"
TEMP_HTML = os.path.join(ROOT_DIR, "temp_preview_s7.html")

BASE_TEMPLATE = """<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Preview Opciones Slide 7</title>
  <link rel="stylesheet" href="styles.css?v=9999">
</head>
<body>
  <main id="presentation-viewport">
    <div id="slides-stage">
      {SLIDE_CONTENT}
    </div>
  </main>
</body>
</html>"""

# ==============================================================================
# OPCION A: 4 COLUMNAS CONTINUAS (ESTILO SLIDE 3 Y SLIDE 5 LIMPIO)
# ==============================================================================
CONTENT_A = """
<section class="slide s-white active" id="slide-preview-7a">
  <header class="slide-header">
    <div class="sh-left">
      <span class="sh-red-bar"></span>
      <span class="sh-category">02 &middot; METODOLOG&Iacute;A &middot; PIPELINE RAG LOCAL</span>
    </div>
    <img src="assets/image6.png" alt="#LoxTIC" class="sh-loxtic">
  </header>
  <div class="sh-divider"></div>

  <div class="slide-content-area" style="justify-content: center; padding-top: 10px; padding-bottom: 20px;">
    <h2 class="s-lead-question" style="font-size: 46px; font-weight: 800; margin-bottom: 34px; line-height: 1.2;">
      Cuatro etapas para garantizar respuestas precisas en la CPU del aula
    </h2>

    <div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 24px; align-items: stretch;">
      
      <!-- Etapa 1: Corpus -->
      <div style="background: var(--c-pink-bg); border-top: 8px solid var(--c-wine-primary); padding: 40px 30px; display: flex; flex-direction: column;">
        <div style="font-family: var(--font-mono); font-size: 19px; font-weight: 700; color: var(--c-wine-primary); letter-spacing: 2px; margin-bottom: 12px;">
          ETAPA 01
        </div>
        <h3 style="font-family: var(--font-sans); font-size: 32px; font-weight: 700; color: var(--c-wine-dark); margin-bottom: 20px;">
          Corpus
        </h3>
        <div style="font-family: var(--font-sans); font-size: 60px; font-weight: 800; color: var(--c-wine-primary); line-height: 1; margin-bottom: 22px;">
          339
        </div>
        <p style="font-family: var(--font-sans); font-size: 26px; color: var(--c-text-dark); line-height: 1.45; margin: 0;">
          Trozos curriculares del libro <em>College ESL Writers</em> (&le; 512 palabras).
        </p>
      </div>

      <!-- Etapa 2: Búsqueda -->
      <div style="background: var(--c-pink-bg); border-top: 8px solid var(--c-wine-primary); padding: 40px 30px; display: flex; flex-direction: column;">
        <div style="font-family: var(--font-mono); font-size: 19px; font-weight: 700; color: var(--c-wine-primary); letter-spacing: 2px; margin-bottom: 12px;">
          ETAPA 02
        </div>
        <h3 style="font-family: var(--font-sans); font-size: 32px; font-weight: 700; color: var(--c-wine-dark); margin-bottom: 20px;">
          B&uacute;squeda
        </h3>
        <div style="font-family: var(--font-sans); font-size: 60px; font-weight: 800; color: var(--c-wine-primary); line-height: 1; margin-bottom: 22px;">
          H&iacute;brida
        </div>
        <p style="font-family: var(--font-sans); font-size: 26px; color: var(--c-text-dark); line-height: 1.45; margin: 0;">
          Fusi&oacute;n RRF: <strong>60% vectorial</strong> denso + <strong>40% l&eacute;xico</strong> BM25.
        </p>
      </div>

      <!-- Etapa 3: Reranker -->
      <div style="background: var(--c-pink-bg); border-top: 8px solid var(--c-red-accent); padding: 40px 30px; display: flex; flex-direction: column;">
        <div style="font-family: var(--font-mono); font-size: 19px; font-weight: 700; color: var(--c-red-accent); letter-spacing: 2px; margin-bottom: 12px;">
          ETAPA 03
        </div>
        <h3 style="font-family: var(--font-sans); font-size: 32px; font-weight: 700; color: var(--c-wine-dark); margin-bottom: 20px;">
          Reranker
        </h3>
        <div style="font-family: var(--font-sans); font-size: 60px; font-weight: 800; color: var(--c-red-accent); line-height: 1; margin-bottom: 22px;">
          Top-K
        </div>
        <p style="font-family: var(--font-sans); font-size: 26px; color: var(--c-text-dark); line-height: 1.45; margin: 0;">
          Cross-Encoder <strong>MiniLM</strong> para reordenar y filtrar ruido conceptual.
        </p>
      </div>

      <!-- Etapa 4: Inferencia -->
      <div style="background: var(--c-pink-bg); border-top: 8px solid var(--c-gold); padding: 40px 30px; display: flex; flex-direction: column;">
        <div style="font-family: var(--font-mono); font-size: 19px; font-weight: 700; color: #9A7200; letter-spacing: 2px; margin-bottom: 12px;">
          ETAPA 04
        </div>
        <h3 style="font-family: var(--font-sans); font-size: 32px; font-weight: 700; color: var(--c-wine-dark); margin-bottom: 20px;">
          Inferencia
        </h3>
        <div style="font-family: var(--font-sans); font-size: 60px; font-weight: 800; color: #9A7200; line-height: 1; margin-bottom: 22px;">
          1.9 tok/s
        </div>
        <p style="font-family: var(--font-sans); font-size: 26px; color: var(--c-text-dark); line-height: 1.45; margin: 0;">
          Motor <strong>llama.cpp</strong> en CPU de aula sin GPU a costo cero.
        </p>
      </div>

    </div>
  </div>

  <div class="slide-footer-rule"></div>
  <footer class="slide-footer">
    <span class="sf-left">VI CONGRESO CARTAGENA &middot; 2026</span>
    <span class="sf-right">LOHACEMOSXTIC.COM &middot; SLM OFFLINE</span>
  </footer>
</section>
"""

# ==============================================================================
# OPCION B: DIAGRAMA DE FLUJO SECUENCIAL (PIPELINE STEPPER CON CONECTORES)
# ==============================================================================
CONTENT_B = """
<section class="slide s-white active" id="slide-preview-7b">
  <header class="slide-header">
    <div class="sh-left">
      <span class="sh-red-bar"></span>
      <span class="sh-category">02 &middot; METODOLOG&Iacute;A &middot; PIPELINE RAG LOCAL</span>
    </div>
    <img src="assets/image6.png" alt="#LoxTIC" class="sh-loxtic">
  </header>
  <div class="sh-divider"></div>

  <div class="slide-content-area" style="justify-content: center; padding-top: 10px; padding-bottom: 20px;">
    <h2 class="s-lead-question" style="font-size: 46px; font-weight: 800; margin-bottom: 34px; line-height: 1.2;">
      Flujo secuencial del pipeline RAG: de la consulta a la generaci&oacute;n
    </h2>

    <div style="display: flex; flex-direction: column; gap: 24px;">
      
      <!-- Fila de Proceso Conectado -->
      <div style="display: flex; align-items: stretch; gap: 16px;">
        
        <!-- Paso 1 -->
        <div style="flex: 1; background: #FAF5F5; border-left: 6px solid var(--c-wine-primary); padding: 24px 22px;">
          <div style="font-family: var(--font-mono); font-size: 18px; font-weight: 700; color: var(--c-wine-primary); margin-bottom: 6px;">
            PASO 01
          </div>
          <div style="font-family: var(--font-sans); font-size: 26px; font-weight: 800; color: var(--c-text-dark); margin-bottom: 8px;">
            Corpus Curricular
          </div>
          <div style="font-family: var(--font-sans); font-size: 23px; color: var(--c-gray-text); line-height: 1.35;">
            Libro abierto <em>College ESL</em>: 339 trozos indexados (&le; 512 palabras).
          </div>
        </div>

        <div style="display: flex; align-items: center; justify-content: center; font-size: 28px; color: var(--c-wine-primary); font-weight: 800;">&rarr;</div>

        <!-- Paso 2 -->
        <div style="flex: 1; background: #FAF5F5; border-left: 6px solid var(--c-wine-primary); padding: 24px 22px;">
          <div style="font-family: var(--font-mono); font-size: 18px; font-weight: 700; color: var(--c-wine-primary); margin-bottom: 6px;">
            PASO 02
          </div>
          <div style="font-family: var(--font-sans); font-size: 26px; font-weight: 800; color: var(--c-text-dark); margin-bottom: 8px;">
            B&uacute;squeda H&iacute;brida
          </div>
          <div style="font-family: var(--font-sans); font-size: 23px; color: var(--c-gray-text); line-height: 1.35;">
            Fusi&oacute;n RRF (60% denso + 40% BM25) con expansi&oacute;n l&eacute;xica multi-query.
          </div>
        </div>

        <div style="display: flex; align-items: center; justify-content: center; font-size: 28px; color: var(--c-red-accent); font-weight: 800;">&rarr;</div>

        <!-- Paso 3 -->
        <div style="flex: 1; background: #FAF5F5; border-left: 6px solid var(--c-red-accent); padding: 24px 22px;">
          <div style="font-family: var(--font-mono); font-size: 18px; font-weight: 700; color: var(--c-red-accent); margin-bottom: 6px;">
            PASO 03
          </div>
          <div style="font-family: var(--font-sans); font-size: 26px; font-weight: 800; color: var(--c-text-dark); margin-bottom: 8px;">
            Reranker Neuronal
          </div>
          <div style="font-family: var(--font-sans); font-size: 23px; color: var(--c-gray-text); line-height: 1.35;">
            Cross-Encoder <em>MiniLM</em>: reordena y suprime ruido antes de la CPU.
          </div>
        </div>

        <div style="display: flex; align-items: center; justify-content: center; font-size: 28px; color: #9A7200; font-weight: 800;">&rarr;</div>

        <!-- Paso 4 -->
        <div style="flex: 1; background: #FAF5F5; border-left: 6px solid var(--c-gold); padding: 24px 22px;">
          <div style="font-family: var(--font-mono); font-size: 18px; font-weight: 700; color: #9A7200; margin-bottom: 6px;">
            PASO 04
          </div>
          <div style="font-family: var(--font-sans); font-size: 26px; font-weight: 800; color: var(--c-text-dark); margin-bottom: 8px;">
            Inferencia Local
          </div>
          <div style="font-family: var(--font-sans); font-size: 23px; color: var(--c-gray-text); line-height: 1.35;">
            Motor <code>llama.cpp</code> a 1.9 tok/s en CPU est&aacute;ndar sin GPU.
          </div>
        </div>

      </div>

      <!-- Tarjeta Panorámica de Principio Técnico -->
      <div style="background: #FAF5F5; border-left: 8px solid var(--c-wine-primary); padding: 24px 34px; display: flex; align-items: center; gap: 32px;">
        <div style="flex: 0 0 200px; text-align: center;">
          <div style="font-family: var(--font-sans); font-size: 52px; font-weight: 800; color: var(--c-wine-primary); line-height: 1;">
            100%
          </div>
          <div style="font-family: var(--font-mono); font-size: 16px; font-weight: 700; color: var(--c-gray-text); margin-top: 4px;">
            LOCAL / USB
          </div>
        </div>
        <div style="width: 2px; height: 75px; background: var(--c-border-subtle); flex-shrink: 0;"></div>
        <div style="flex: 1;">
          <div style="font-family: var(--font-sans); font-size: 26px; font-weight: 700; color: var(--c-text-dark); margin-bottom: 6px;">
            Principio Operativo: Cero Dependencia de Servidores
          </div>
          <p style="font-family: var(--font-sans); font-size: 24px; color: var(--c-gray-text); line-height: 1.4; margin: 0;">
            Todo el pipeline (b&uacute;squeda, re-ranking e inferencia del modelo SLM) se ejecuta en la <strong>memoria RAM del computador del aula</strong> sin enviar un solo byte a la nube.
          </p>
        </div>
      </div>

    </div>
  </div>

  <div class="slide-footer-rule"></div>
  <footer class="slide-footer">
    <span class="sf-left">VI CONGRESO CARTAGENA &middot; 2026</span>
    <span class="sf-right">LOHACEMOSXTIC.COM &middot; SLM OFFLINE</span>
  </footer>
</section>
"""

# ==============================================================================
# OPCION C: 2 GRANDES BLOQUES ESTRUCTURALES (PREPARACIÓN VS TIEMPO REAL)
# ==============================================================================
CONTENT_C = """
<section class="slide s-white active" id="slide-preview-7c">
  <header class="slide-header">
    <div class="sh-left">
      <span class="sh-red-bar"></span>
      <span class="sh-category">02 &middot; METODOLOG&Iacute;A &middot; PIPELINE RAG LOCAL</span>
    </div>
    <img src="assets/image6.png" alt="#LoxTIC" class="sh-loxtic">
  </header>
  <div class="sh-divider"></div>

  <div class="slide-content-area" style="justify-content: center; padding-top: 10px; padding-bottom: 20px;">
    <h2 class="s-lead-question" style="font-size: 46px; font-weight: 800; margin-bottom: 34px; line-height: 1.2;">
      Arquitectura del sistema: preparaci&oacute;n del corpus y respuesta en tiempo real
    </h2>

    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 36px; align-items: stretch;">
      
      <!-- Bloque Izquierdo: Fase Preparatoria (Offline / Previo) -->
      <div style="background: var(--c-pink-bg); border-top: 8px solid var(--c-wine-primary); padding: 36px 36px; display: flex; flex-direction: column; justify-content: space-between;">
        <div>
          <div style="font-family: var(--font-mono); font-size: 19px; font-weight: 700; color: var(--c-wine-primary); letter-spacing: 2px; margin-bottom: 10px;">
            FASE A &middot; BASE CURRICULAR PREVIA
          </div>
          <h3 style="font-family: var(--font-sans); font-size: 32px; font-weight: 700; color: var(--c-wine-dark); margin-bottom: 24px;">
            Corpus y Representaci&oacute;n
          </h3>

          <div style="display: flex; flex-direction: column; gap: 20px;">
            <div>
              <div style="font-family: var(--font-sans); font-size: 26px; font-weight: 700; color: var(--c-text-dark); margin-bottom: 4px;">
                1. Ingesta del Libro Abierto (ESL)
              </div>
              <p style="font-family: var(--font-sans); font-size: 24px; color: var(--c-gray-text); line-height: 1.4; margin: 0;">
                299 p&aacute;ginas procesadas y segmentadas en <strong>339 trozos</strong> pedag&oacute;gicos (&le; 512 palabras).
              </p>
            </div>

            <div>
              <div style="font-family: var(--font-sans); font-size: 26px; font-weight: 700; color: var(--c-text-dark); margin-bottom: 4px;">
                2. Doble Indexaci&oacute;n Offline
              </div>
              <p style="font-family: var(--font-sans); font-size: 24px; color: var(--c-gray-text); line-height: 1.4; margin: 0;">
                &Iacute;ndice vectorial denso (sem&aacute;ntica) + &Iacute;ndice BM25 (palabras exactas) precargados en USB.
              </p>
            </div>
          </div>
        </div>

        <div style="padding-top: 18px; border-top: 2px solid var(--c-border-subtle); font-family: var(--font-sans); font-size: 23px; color: var(--c-wine-primary); font-weight: 700;">
          Resultado: Base de conocimiento 100% portable y verificada.
        </div>
      </div>

      <!-- Bloque Derecho: Fase Interactiva (En el Aula) -->
      <div style="background: var(--c-pink-bg); border-top: 8px solid var(--c-red-accent); padding: 36px 36px; display: flex; flex-direction: column; justify-content: space-between;">
        <div>
          <div style="font-family: var(--font-mono); font-size: 19px; font-weight: 700; color: var(--c-red-accent); letter-spacing: 2px; margin-bottom: 10px;">
            FASE B &middot; INTERACCI&Oacute;N EN EL AULA
          </div>
          <h3 style="font-family: var(--font-sans); font-size: 32px; font-weight: 700; color: var(--c-wine-dark); margin-bottom: 24px;">
            Recuperaci&oacute;n e Inferencia
          </h3>

          <div style="display: flex; flex-direction: column; gap: 20px;">
            <div>
              <div style="font-family: var(--font-sans); font-size: 26px; font-weight: 700; color: var(--c-text-dark); margin-bottom: 4px;">
                3. B&uacute;squeda H&iacute;brida y Re-ranking
              </div>
              <p style="font-family: var(--font-sans); font-size: 24px; color: var(--c-gray-text); line-height: 1.4; margin: 0;">
                Fusi&oacute;n RRF (60/40) y filtro neuronal <strong>Cross-Encoder</strong> para eliminar ruido conceptual.
              </p>
            </div>

            <div>
              <div style="font-family: var(--font-sans); font-size: 26px; font-weight: 700; color: var(--c-text-dark); margin-bottom: 4px;">
                4. Generaci&oacute;n en CPU de Aula
              </div>
              <p style="font-family: var(--font-sans); font-size: 24px; color: var(--c-gray-text); line-height: 1.4; margin: 0;">
                Motor <strong>llama.cpp</strong> respondiendo a <strong>1.9 tokens/s</strong> en hardware existente.
              </p>
            </div>
          </div>
        </div>

        <div style="padding-top: 18px; border-top: 2px solid var(--c-border-subtle); font-family: var(--font-sans); font-size: 23px; color: var(--c-red-accent); font-weight: 700;">
          Resultado: Tutor interactivo inmediato sin requerir internet.
        </div>
      </div>

    </div>
  </div>

  <div class="slide-footer-rule"></div>
  <footer class="slide-footer">
    <span class="sf-left">VI CONGRESO CARTAGENA &middot; 2026</span>
    <span class="sf-right">LOHACEMOSXTIC.COM &middot; SLM OFFLINE</span>
  </footer>
</section>
"""

OPTIONS = [
    ("slide_07_opcion_a.png", CONTENT_A),
    ("slide_07_opcion_b.png", CONTENT_B),
    ("slide_07_opcion_c.png", CONTENT_C),
]

def generate_and_capture():
    print("Iniciando generación de capturas para Slide 7...")
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(viewport={"width": 1920, "height": 1080})

        for img_name, content in OPTIONS:
            full_html = BASE_TEMPLATE.format(SLIDE_CONTENT=content)
            with open(TEMP_HTML, "w", encoding="utf-8") as f:
                f.write(full_html)

            page.goto("http://localhost:8085/temp_preview_s7.html", wait_until="networkidle")
            page.wait_for_timeout(600)

            out_path_root = os.path.join(ROOT_DIR, img_name)
            out_path_artifact = os.path.join(ARTIFACT_DIR, img_name)

            page.screenshot(path=out_path_root)
            page.screenshot(path=out_path_artifact)
            print(f"-> Captura guardada: {img_name}")

        browser.close()

    if os.path.exists(TEMP_HTML):
        os.remove(TEMP_HTML)
    print("Completado.")

if __name__ == "__main__":
    generate_and_capture()
