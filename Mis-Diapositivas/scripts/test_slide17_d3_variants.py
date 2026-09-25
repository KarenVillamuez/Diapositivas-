# -*- coding: utf-8 -*-
import os
from playwright.sync_api import sync_playwright

output_dir = r"C:\Users\ASUS\.gemini\antigravity-ide\brain\a6624504-511c-4b9d-bc9a-468e348bde40"
os.makedirs(output_dir, exist_ok=True)

# ===========================================================================
# D3-A: Texto Mínimo + Fuente Grande (26px / 28px) en los 4 Cuadrantes
# ===========================================================================
CONTENT_D3_A = '''
    <h2 class="s-lead-question" style="font-size: 40px; font-weight: 800; margin: 0; line-height: 1.2; color: #2C0509;">
      Apego al material fuente no es aprendizaje: guía para auditar y desplegar tutores
    </h2>

    <div style="display: grid; grid-template-columns: 1fr 1fr; grid-template-rows: 1fr 1fr; gap: 24px; flex: 1; margin-top: 10px;">
      
      <!-- Cuadrante 1: Diagnóstico -->
      <div style="background: #FAF5F5; border-top: 8px solid var(--c-red-accent); padding: 26px 32px; display: flex; flex-direction: column; justify-content: space-between;">
        <div>
          <div style="font-family: var(--font-mono); font-size: 19px; font-weight: 800; color: var(--c-red-accent); letter-spacing: 1.5px; margin-bottom: 6px;">
            01 · DIAGNÓSTICO METODOLÓGICO
          </div>
          <div style="font-family: var(--font-sans); font-size: 32px; font-weight: 900; color: #110103; margin-bottom: 14px;">
            La Falacia de la Nota Agregada
          </div>
          <div style="font-family: var(--font-sans); font-size: 26px; color: #110103; line-height: 1.4;">
            <strong style="color: var(--c-red-accent);">Apego &ne; Aprendizaje:</strong> El índice <span style="font-family: var(--font-mono); font-weight: 800;">0.795</span> mide similitud con el libro, no comprensión del estudiante.
          </div>
        </div>
        <div style="font-family: var(--font-mono); font-size: 20px; font-weight: 800; color: var(--c-red-accent);">
          &bull; Respuestas vacías superan 0.70
        </div>
      </div>

      <!-- Cuadrante 2: Auditoría -->
      <div style="background: #FAF5F5; border-top: 8px solid #B38600; padding: 26px 32px; display: flex; flex-direction: column; justify-content: space-between;">
        <div>
          <div style="font-family: var(--font-mono); font-size: 19px; font-weight: 800; color: #B38600; letter-spacing: 1.5px; margin-bottom: 6px;">
            02 · PROTOCOLO DE AUDITORÍA
          </div>
          <div style="font-family: var(--font-sans); font-size: 32px; font-weight: 900; color: #110103; margin-bottom: 14px;">
            Desglose por Componentes
          </div>
          <div style="font-family: var(--font-sans); font-size: 26px; color: #110103; line-height: 1.4;">
            <strong style="color: #B38600;">Prohibido promedio único:</strong> Auditar obligatoriamente por separado <em>grounding</em>, <em>relevance</em> y <em>rechazo</em>.
          </div>
        </div>
        <div style="font-family: var(--font-mono); font-size: 20px; font-weight: 800; color: #B38600;">
          &bull; Tres dimensiones independientes
        </div>
      </div>

      <!-- Cuadrante 3: Qwen -->
      <div style="background: #FAF5F5; border-top: 8px solid var(--c-wine-primary); padding: 26px 32px; display: flex; flex-direction: column; justify-content: space-between;">
        <div>
          <div style="display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 6px;">
            <span style="font-family: var(--font-mono); font-size: 19px; font-weight: 800; color: var(--c-wine-primary); letter-spacing: 1.5px;">
              03 · DESPLIEGUE AUTÓNOMO
            </span>
            <span style="font-family: var(--font-mono); font-size: 22px; font-weight: 900; color: var(--c-wine-primary);">
              85.7% Rechazo
            </span>
          </div>
          <div style="font-family: var(--font-sans); font-size: 32px; font-weight: 900; color: var(--c-wine-primary); margin-bottom: 14px;">
            Qwen2.5-3B &rarr; Autoestudio
          </div>
          <div style="font-family: var(--font-sans); font-size: 26px; color: #110103; line-height: 1.4;">
            <strong>Sin docente en sala:</strong> Prima la <strong style="color: var(--c-wine-primary);">certeza absoluta</strong>. Es preferible admitir desconocimiento antes que alucinar.
          </div>
        </div>
        <div style="font-family: var(--font-mono); font-size: 20px; font-weight: 800; color: var(--c-wine-primary);">
          &bull; Cautela máxima frente a trampas
        </div>
      </div>

      <!-- Cuadrante 4: Phi -->
      <div style="background: #FAF5F5; border-top: 8px solid var(--c-red-accent); padding: 26px 32px; display: flex; flex-direction: column; justify-content: space-between;">
        <div>
          <div style="display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 6px;">
            <span style="font-family: var(--font-mono); font-size: 19px; font-weight: 800; color: var(--c-red-accent); letter-spacing: 1.5px;">
              04 · DESPLIEGUE ASISTIDO
            </span>
            <span style="font-family: var(--font-mono); font-size: 22px; font-weight: 900; color: var(--c-red-accent);">
              0.0% Bloqueos
            </span>
          </div>
          <div style="font-family: var(--font-sans); font-size: 32px; font-weight: 900; color: var(--c-red-accent); margin-bottom: 14px;">
            Phi-4-mini &rarr; Aula con Docente
          </div>
          <div style="font-family: var(--font-sans); font-size: 26px; color: #110103; line-height: 1.4;">
            <strong>Con docente en sala:</strong> Prima la <strong style="color: var(--c-red-accent);">fluidez total</strong>. El modelo no frena la clase y el profesor corrige desvíos.
          </div>
        </div>
        <div style="font-family: var(--font-mono); font-size: 20px; font-weight: 800; color: var(--c-red-accent);">
          &bull; Dinamismo con supervisión humana
        </div>
      </div>

    </div>
'''

# ===========================================================================
# D3-B: Cifras Rectoras Heroicas + Máxima Síntesis Telegráfica
# ===========================================================================
CONTENT_D3_B = '''
    <h2 class="s-lead-question" style="font-size: 40px; font-weight: 800; margin: 0; line-height: 1.2; color: #2C0509;">
      Apego al material fuente no es aprendizaje: guía para auditar y desplegar tutores
    </h2>

    <div style="display: grid; grid-template-columns: 1fr 1fr; grid-template-rows: 1fr 1fr; gap: 24px; flex: 1; margin-top: 10px;">
      
      <!-- Cuadrante 1: 0.795 -->
      <div style="background: #FAF5F5; border-left: 12px solid var(--c-red-accent); padding: 26px 32px; display: flex; align-items: center; gap: 28px;">
        <div style="font-family: var(--font-mono); font-size: 56px; font-weight: 900; color: var(--c-red-accent); line-height: 1; flex-shrink: 0; text-align: center;">
          0.795
        </div>
        <div style="width: 2px; height: 100px; background: #D5C8C9; flex-shrink: 0;"></div>
        <div>
          <div style="font-family: var(--font-mono); font-size: 18px; font-weight: 800; color: var(--c-red-accent); letter-spacing: 1px;">
            FALACIA METODOLÓGICA
          </div>
          <div style="font-family: var(--font-sans); font-size: 28px; font-weight: 900; color: #110103; margin-top: 4px;">
            Apego &ne; Aprendizaje
          </div>
          <div style="font-family: var(--font-sans); font-size: 23px; color: #5D4A4D; margin-top: 6px; line-height: 1.35;">
            Mide copia del libro, no comprensión. Respuestas vacías superan 0.70.
          </div>
        </div>
      </div>

      <!-- Cuadrante 2: 3 Ejes -->
      <div style="background: #FAF5F5; border-left: 12px solid #B38600; padding: 26px 32px; display: flex; align-items: center; gap: 28px;">
        <div style="font-family: var(--font-mono); font-size: 56px; font-weight: 900; color: #B38600; line-height: 1; flex-shrink: 0; text-align: center;">
          3 Ejes
        </div>
        <div style="width: 2px; height: 100px; background: #D5C8C9; flex-shrink: 0;"></div>
        <div>
          <div style="font-family: var(--font-mono); font-size: 18px; font-weight: 800; color: #B38600; letter-spacing: 1px;">
            AUDITORÍA MULTI-DIMENSIONAL
          </div>
          <div style="font-family: var(--font-sans); font-size: 28px; font-weight: 900; color: #110103; margin-top: 4px;">
            Desglose Obligatorio
          </div>
          <div style="font-family: var(--font-sans); font-size: 23px; color: #5D4A4D; margin-top: 6px; line-height: 1.35;">
            Prohibido promedio único: evaluar <em>grounding</em>, <em>relevance</em> y <em>rechazo</em>.
          </div>
        </div>
      </div>

      <!-- Cuadrante 3: 85.7% -->
      <div style="background: #FAF5F5; border-left: 12px solid var(--c-wine-primary); padding: 26px 32px; display: flex; align-items: center; gap: 28px;">
        <div style="font-family: var(--font-mono); font-size: 56px; font-weight: 900; color: var(--c-wine-primary); line-height: 1; flex-shrink: 0; text-align: center;">
          85.7%
        </div>
        <div style="width: 2px; height: 100px; background: #D5C8C9; flex-shrink: 0;"></div>
        <div>
          <div style="font-family: var(--font-mono); font-size: 18px; font-weight: 800; color: var(--c-wine-primary); letter-spacing: 1px;">
            QWEN2.5-3B &bull; AUTOESTUDIO
          </div>
          <div style="font-family: var(--font-sans); font-size: 28px; font-weight: 900; color: #110103; margin-top: 4px;">
            Certeza Absoluta
          </div>
          <div style="font-family: var(--font-sans); font-size: 23px; color: #5D4A4D; margin-top: 6px; line-height: 1.35;">
            Sin docente en sala: prefiere admitir desconocimiento antes que alucinar.
          </div>
        </div>
      </div>

      <!-- Cuadrante 4: 0.0% -->
      <div style="background: #FAF5F5; border-left: 12px solid var(--c-red-accent); padding: 26px 32px; display: flex; align-items: center; gap: 28px;">
        <div style="font-family: var(--font-mono); font-size: 56px; font-weight: 900; color: var(--c-red-accent); line-height: 1; flex-shrink: 0; text-align: center;">
          0.0%
        </div>
        <div style="width: 2px; height: 100px; background: #D5C8C9; flex-shrink: 0;"></div>
        <div>
          <div style="font-family: var(--font-mono); font-size: 18px; font-weight: 800; color: var(--c-red-accent); letter-spacing: 1px;">
            PHI-4-MINI &bull; AULA ASISTIDA
          </div>
          <div style="font-family: var(--font-sans); font-size: 28px; font-weight: 900; color: #110103; margin-top: 4px;">
            Fluidez Interactiva
          </div>
          <div style="font-family: var(--font-sans); font-size: 23px; color: #5D4A4D; margin-top: 6px; line-height: 1.35;">
            Con docente en sala: nunca frena la sesión; el profesor corrige desvíos.
          </div>
        </div>
      </div>

    </div>
'''

# ===========================================================================
# D3-C: Híbrido Editorial — Textos Ultra-Grandes (28px) en 2 Filas
# ===========================================================================
CONTENT_D3_C = '''
    <h2 class="s-lead-question" style="font-size: 40px; font-weight: 800; margin: 0; line-height: 1.2; color: #2C0509;">
      Apego al material fuente no es aprendizaje: guía para auditar y desplegar tutores
    </h2>

    <div style="display: grid; grid-template-columns: 1fr 1fr; grid-template-rows: 1fr 1fr; gap: 24px; flex: 1; margin-top: 10px;">
      
      <!-- Cuadrante 1: Diagnóstico -->
      <div style="background: #FAF5F5; border-top: 8px solid var(--c-red-accent); padding: 28px 36px; display: flex; flex-direction: column; justify-content: center;">
        <div style="font-family: var(--font-mono); font-size: 19px; font-weight: 800; color: var(--c-red-accent); letter-spacing: 1.5px; margin-bottom: 8px;">
          01 · LA FALACIA METODOLÓGICA
        </div>
        <div style="font-family: var(--font-sans); font-size: 34px; font-weight: 900; color: #110103; margin-bottom: 12px;">
          Apego &ne; Aprendizaje
        </div>
        <div style="font-family: var(--font-sans); font-size: 27px; color: #110103; line-height: 1.35; font-weight: 600;">
          El puntaje <span style="font-family: var(--font-mono); font-weight: 800; color: var(--c-red-accent);">0.795</span> mide copia literal del libro, no comprensión real del alumno.
        </div>
      </div>

      <!-- Cuadrante 2: Auditoría -->
      <div style="background: #FAF5F5; border-top: 8px solid #B38600; padding: 28px 36px; display: flex; flex-direction: column; justify-content: center;">
        <div style="font-family: var(--font-mono); font-size: 19px; font-weight: 800; color: #B38600; letter-spacing: 1.5px; margin-bottom: 8px;">
          02 · PROTOCOLO DE AUDITORÍA
        </div>
        <div style="font-family: var(--font-sans); font-size: 34px; font-weight: 900; color: #110103; margin-bottom: 12px;">
          Auditoría Desglosada
        </div>
        <div style="font-family: var(--font-sans); font-size: 27px; color: #110103; line-height: 1.35; font-weight: 600;">
          <strong style="color: #B38600;">Prohibido promedio único:</strong> evaluar por separado relevancia, fidelidad y rechazo.
        </div>
      </div>

      <!-- Cuadrante 3: Qwen -->
      <div style="background: #FAF5F5; border-top: 8px solid var(--c-wine-primary); padding: 28px 36px; display: flex; flex-direction: column; justify-content: center;">
        <div style="display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 8px;">
          <span style="font-family: var(--font-mono); font-size: 19px; font-weight: 800; color: var(--c-wine-primary); letter-spacing: 1.5px;">
            03 · QWEN2.5-3B
          </span>
          <span style="font-family: var(--font-mono); font-size: 24px; font-weight: 900; color: var(--c-wine-primary);">
            85.7% Rechazo
          </span>
        </div>
        <div style="font-family: var(--font-sans); font-size: 34px; font-weight: 900; color: var(--c-wine-primary); margin-bottom: 12px;">
          Autoestudio Autónomo
        </div>
        <div style="font-family: var(--font-sans); font-size: 27px; color: #110103; line-height: 1.35; font-weight: 600;">
          <strong>Sin profesor:</strong> Prima la <strong style="color: var(--c-wine-primary);">certeza</strong>. Preferible admitir desconocimiento antes que alucinar.
        </div>
      </div>

      <!-- Cuadrante 4: Phi -->
      <div style="background: #FAF5F5; border-top: 8px solid var(--c-red-accent); padding: 28px 36px; display: flex; flex-direction: column; justify-content: center;">
        <div style="display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 8px;">
          <span style="font-family: var(--font-mono); font-size: 19px; font-weight: 800; color: var(--c-red-accent); letter-spacing: 1.5px;">
            04 · PHI-4-MINI
          </span>
          <span style="font-family: var(--font-mono); font-size: 24px; font-weight: 900; color: var(--c-red-accent);">
            0.0% Bloqueos
          </span>
        </div>
        <div style="font-family: var(--font-sans); font-size: 34px; font-weight: 900; color: var(--c-red-accent); margin-bottom: 12px;">
          Aula Asistida con Docente
        </div>
        <div style="font-family: var(--font-sans); font-size: 27px; color: #110103; line-height: 1.35; font-weight: 600;">
          <strong>Con profesor:</strong> Prima la <strong style="color: var(--c-red-accent);">fluidez</strong>. No frena la clase y el docente corrige en tiempo real.
        </div>
      </div>

    </div>
'''

HTML_TEMPLATE = '''<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Test Slide 17 D3 Refinements</title>
  <link rel="stylesheet" href="http://localhost:8085/styles.css?v=32">
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
    options = [
        ('slide_17_d3_A.html', 'slide_17_d3_A.png', CONTENT_D3_A),
        ('slide_17_d3_B.html', 'slide_17_d3_B.png', CONTENT_D3_B),
        ('slide_17_d3_C.html', 'slide_17_d3_C.png', CONTENT_D3_C),
    ]

    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(viewport={"width": 1920, "height": 1080})

        for html_name, png_name, content in options:
            html_path = os.path.join(output_dir, html_name)
            png_path = os.path.join(output_dir, png_name)

            full_html = HTML_TEMPLATE.format(content=content)
            with open(html_path, 'w', encoding='utf-8') as f:
                f.write(full_html)

            page.goto(f"file:///{html_path.replace(os.sep, '/')}")
            page.wait_for_timeout(400)
            page.screenshot(path=png_path)
            print(f"Captured: {png_name}")

        browser.close()

if __name__ == '__main__':
    main()
