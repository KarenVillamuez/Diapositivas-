# -*- coding: utf-8 -*-
import os
from playwright.sync_api import sync_playwright

output_dir = r"C:\Users\ASUS\.gemini\antigravity-ide\brain\a6624504-511c-4b9d-bc9a-468e348bde40"
os.makedirs(output_dir, exist_ok=True)

# ===========================================================================
# D3-C1: Simetría de Badges + Texto Gigante (28px) + Cero Viudas
# ===========================================================================
CONTENT_PERFECT_1 = '''
    <h2 class="s-lead-question" style="font-size: 38px; font-weight: 800; margin: 0; line-height: 1.2; color: #2C0509;">
      Apego al texto no es aprendizaje: criterios para auditar y desplegar tutores
    </h2>

    <div style="display: grid; grid-template-columns: 1fr 1fr; grid-template-rows: 1fr 1fr; gap: 26px; flex: 1; margin-top: 14px;">
      
      <!-- Cuadrante 1: Diagnóstico -->
      <div style="background: #FAF5F5; border-top: 8px solid var(--c-red-accent); padding: 28px 36px; display: flex; flex-direction: column; justify-content: center;">
        <div style="display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 8px;">
          <span style="font-family: var(--font-mono); font-size: 19px; font-weight: 800; color: var(--c-red-accent); letter-spacing: 1.5px;">
            01 · DIAGNÓSTICO METODOLÓGICO
          </span>
          <span style="font-family: var(--font-mono); font-size: 22px; font-weight: 900; color: var(--c-red-accent);">
            0.795 Engañoso
          </span>
        </div>
        <div style="font-family: var(--font-sans); font-size: 34px; font-weight: 900; color: #110103; margin-bottom: 12px;">
          Apego &ne; Aprendizaje
        </div>
        <div style="font-family: var(--font-sans); font-size: 28px; color: #110103; line-height: 1.35; font-weight: 600;">
          El puntaje agregado mide copia literal del libro de texto, no comprensión ni apropiación del estudiante.
        </div>
      </div>

      <!-- Cuadrante 2: Auditoría -->
      <div style="background: #FAF5F5; border-top: 8px solid #B38600; padding: 28px 36px; display: flex; flex-direction: column; justify-content: center;">
        <div style="display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 8px;">
          <span style="font-family: var(--font-mono); font-size: 19px; font-weight: 800; color: #B38600; letter-spacing: 1.5px;">
            02 · PROTOCOLO DE AUDITORÍA
          </span>
          <span style="font-family: var(--font-mono); font-size: 22px; font-weight: 900; color: #B38600;">
            3 Dimensiones
          </span>
        </div>
        <div style="font-family: var(--font-sans); font-size: 34px; font-weight: 900; color: #110103; margin-bottom: 12px;">
          Auditoría Desglosada
        </div>
        <div style="font-family: var(--font-sans); font-size: 28px; color: #110103; line-height: 1.35; font-weight: 600;">
          <strong style="color: #B38600;">Prohibido promedio único:</strong> evaluar por separado recuperación, fidelidad contextual y rechazo.
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
        <div style="font-family: var(--font-sans); font-size: 28px; color: #110103; line-height: 1.35; font-weight: 600;">
          <strong>Sin profesor:</strong> Prima la <strong style="color: var(--c-wine-primary);">certeza absoluta</strong>. Preferible admitir desconocimiento antes que alucinar.
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
        <div style="font-family: var(--font-sans); font-size: 28px; color: #110103; line-height: 1.35; font-weight: 600;">
          <strong>Con profesor:</strong> Prima la <strong style="color: var(--c-red-accent);">fluidez total</strong>. No frena la clase y el docente corrige en tiempo real.
        </div>
      </div>

    </div>
'''

# ===========================================================================
# D3-C3: Ultra-Sintetizado + Tipografía Colosal (30px) + Máximo Impacto
# ===========================================================================
CONTENT_PERFECT_3 = '''
    <h2 class="s-lead-question" style="font-size: 38px; font-weight: 800; margin: 0; line-height: 1.2; color: #2C0509;">
      Apego al texto no es aprendizaje: criterios para auditar y desplegar tutores
    </h2>

    <div style="display: grid; grid-template-columns: 1fr 1fr; grid-template-rows: 1fr 1fr; gap: 26px; flex: 1; margin-top: 14px;">
      
      <!-- Cuadrante 1: Diagnóstico -->
      <div style="background: #FAF5F5; border-top: 8px solid var(--c-red-accent); padding: 30px 38px; display: flex; flex-direction: column; justify-content: center;">
        <div style="display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 10px;">
          <span style="font-family: var(--font-mono); font-size: 20px; font-weight: 800; color: var(--c-red-accent); letter-spacing: 1.5px;">
            01 · DIAGNÓSTICO
          </span>
          <span style="font-family: var(--font-mono); font-size: 24px; font-weight: 900; color: var(--c-red-accent);">
            0.795 Engañoso
          </span>
        </div>
        <div style="font-family: var(--font-sans); font-size: 36px; font-weight: 900; color: #110103; margin-bottom: 12px;">
          Apego &ne; Aprendizaje
        </div>
        <div style="font-family: var(--font-sans); font-size: 30px; color: #110103; line-height: 1.35; font-weight: 600;">
          El promedio mide copia del libro, no comprensión ni pedagogía real.
        </div>
      </div>

      <!-- Cuadrante 2: Auditoría -->
      <div style="background: #FAF5F5; border-top: 8px solid #B38600; padding: 30px 38px; display: flex; flex-direction: column; justify-content: center;">
        <div style="display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 10px;">
          <span style="font-family: var(--font-mono); font-size: 20px; font-weight: 800; color: #B38600; letter-spacing: 1.5px;">
            02 · PROTOCOLO
          </span>
          <span style="font-family: var(--font-mono); font-size: 24px; font-weight: 900; color: #B38600;">
            3 Dimensiones
          </span>
        </div>
        <div style="font-family: var(--font-sans); font-size: 36px; font-weight: 900; color: #110103; margin-bottom: 12px;">
          Auditoría Desglosada
        </div>
        <div style="font-family: var(--font-sans); font-size: 30px; color: #110103; line-height: 1.35; font-weight: 600;">
          <strong style="color: #B38600;">Prohibido promedio único:</strong> auditar recuperación, fidelidad y rechazo por separado.
        </div>
      </div>

      <!-- Cuadrante 3: Qwen -->
      <div style="background: #FAF5F5; border-top: 8px solid var(--c-wine-primary); padding: 30px 38px; display: flex; flex-direction: column; justify-content: center;">
        <div style="display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 10px;">
          <span style="font-family: var(--font-mono); font-size: 20px; font-weight: 800; color: var(--c-wine-primary); letter-spacing: 1.5px;">
            03 · QWEN2.5-3B
          </span>
          <span style="font-family: var(--font-mono); font-size: 24px; font-weight: 900; color: var(--c-wine-primary);">
            85.7% Rechazo
          </span>
        </div>
        <div style="font-family: var(--font-sans); font-size: 36px; font-weight: 900; color: var(--c-wine-primary); margin-bottom: 12px;">
          Autoestudio Autónomo
        </div>
        <div style="font-family: var(--font-sans); font-size: 30px; color: #110103; line-height: 1.35; font-weight: 600;">
          <strong>Sin profesor:</strong> Prima la <strong style="color: var(--c-wine-primary);">certeza</strong>. Mejor admitir no saber antes que inventar.
        </div>
      </div>

      <!-- Cuadrante 4: Phi -->
      <div style="background: #FAF5F5; border-top: 8px solid var(--c-red-accent); padding: 30px 38px; display: flex; flex-direction: column; justify-content: center;">
        <div style="display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 10px;">
          <span style="font-family: var(--font-mono); font-size: 20px; font-weight: 800; color: var(--c-red-accent); letter-spacing: 1.5px;">
            04 · PHI-4-MINI
          </span>
          <span style="font-family: var(--font-mono); font-size: 24px; font-weight: 900; color: var(--c-red-accent);">
            0.0% Bloqueos
          </span>
        </div>
        <div style="font-family: var(--font-sans); font-size: 36px; font-weight: 900; color: var(--c-red-accent); margin-bottom: 12px;">
          Aula con Docente
        </div>
        <div style="font-family: var(--font-sans); font-size: 30px; color: #110103; line-height: 1.35; font-weight: 600;">
          <strong>Con profesor:</strong> Prima la <strong style="color: var(--c-red-accent);">fluidez</strong>. Dinamiza el aula y el docente guía en vivo.
        </div>
      </div>

    </div>
'''

# ===========================================================================
# D3-C2: Con Franja de Remate Pedagógica al Pie (Tipo P2)
# ===========================================================================
CONTENT_PERFECT_2 = '''
    <h2 class="s-lead-question" style="font-size: 38px; font-weight: 800; margin: 0; line-height: 1.2; color: #2C0509;">
      Apego al texto no es aprendizaje: criterios para auditar y desplegar tutores
    </h2>

    <div style="display: flex; flex-direction: column; justify-content: space-between; flex: 1; margin-top: 10px; gap: 16px;">
      
      <!-- GRID 2x2 -->
      <div style="display: grid; grid-template-columns: 1fr 1fr; grid-template-rows: 1fr 1fr; gap: 20px; flex: 1;">
        
        <!-- Cuadrante 1 -->
        <div style="background: #FAF5F5; border-top: 6px solid var(--c-red-accent); padding: 22px 30px; display: flex; flex-direction: column; justify-content: center;">
          <div style="display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 6px;">
            <span style="font-family: var(--font-mono); font-size: 18px; font-weight: 800; color: var(--c-red-accent); letter-spacing: 1.5px;">
              01 · DIAGNÓSTICO
            </span>
            <span style="font-family: var(--font-mono); font-size: 20px; font-weight: 900; color: var(--c-red-accent);">
              0.795 Engañoso
            </span>
          </div>
          <div style="font-family: var(--font-sans); font-size: 30px; font-weight: 900; color: #110103; margin-bottom: 8px;">
            Apego &ne; Aprendizaje
          </div>
          <div style="font-family: var(--font-sans); font-size: 24px; color: #110103; line-height: 1.35; font-weight: 600;">
            El promedio mide copia del libro, no comprensión del estudiante.
          </div>
        </div>

        <!-- Cuadrante 2 -->
        <div style="background: #FAF5F5; border-top: 6px solid #B38600; padding: 22px 30px; display: flex; flex-direction: column; justify-content: center;">
          <div style="display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 6px;">
            <span style="font-family: var(--font-mono); font-size: 18px; font-weight: 800; color: #B38600; letter-spacing: 1.5px;">
              02 · PROTOCOLO
            </span>
            <span style="font-family: var(--font-mono); font-size: 20px; font-weight: 900; color: #B38600;">
              3 Dimensiones
            </span>
          </div>
          <div style="font-family: var(--font-sans); font-size: 30px; font-weight: 900; color: #110103; margin-bottom: 8px;">
            Auditoría Desglosada
          </div>
          <div style="font-family: var(--font-sans); font-size: 24px; color: #110103; line-height: 1.35; font-weight: 600;">
            <strong style="color: #B38600;">Prohibido promedio único:</strong> auditar recuperación, fidelidad y rechazo.
          </div>
        </div>

        <!-- Cuadrante 3 -->
        <div style="background: #FAF5F5; border-top: 6px solid var(--c-wine-primary); padding: 22px 30px; display: flex; flex-direction: column; justify-content: center;">
          <div style="display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 6px;">
            <span style="font-family: var(--font-mono); font-size: 18px; font-weight: 800; color: var(--c-wine-primary); letter-spacing: 1.5px;">
              03 · QWEN2.5-3B
            </span>
            <span style="font-family: var(--font-mono); font-size: 22px; font-weight: 900; color: var(--c-wine-primary);">
              85.7% Rechazo
            </span>
          </div>
          <div style="font-family: var(--font-sans); font-size: 30px; font-weight: 900; color: var(--c-wine-primary); margin-bottom: 8px;">
            Autoestudio Autónomo
          </div>
          <div style="font-family: var(--font-sans); font-size: 24px; color: #110103; line-height: 1.35; font-weight: 600;">
            <strong>Sin docente:</strong> Prima la <strong style="color: var(--c-wine-primary);">certeza</strong>. Preferible admitir ignorancia antes que alucinar.
          </div>
        </div>

        <!-- Cuadrante 4 -->
        <div style="background: #FAF5F5; border-top: 6px solid var(--c-red-accent); padding: 22px 30px; display: flex; flex-direction: column; justify-content: center;">
          <div style="display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 6px;">
            <span style="font-family: var(--font-mono); font-size: 18px; font-weight: 800; color: var(--c-red-accent); letter-spacing: 1.5px;">
              04 · PHI-4-MINI
            </span>
            <span style="font-family: var(--font-mono); font-size: 22px; font-weight: 900; color: var(--c-red-accent);">
              0.0% Bloqueos
            </span>
          </div>
          <div style="font-family: var(--font-sans); font-size: 30px; font-weight: 900; color: var(--c-red-accent); margin-bottom: 8px;">
            Aula con Docente
          </div>
          <div style="font-family: var(--font-sans); font-size: 24px; color: #110103; line-height: 1.35; font-weight: 600;">
            <strong>Con docente:</strong> Prima la <strong style="color: var(--c-red-accent);">fluidez</strong>. Dinamiza la sesión y el profesor corrige en vivo.
          </div>
        </div>

      </div>

      <!-- REMATE EDITORIAL INFERIOR TIPO P2 -->
      <div style="background: #FAF5F5; border-top: 3.5px solid var(--c-wine-primary); border-bottom: 3.5px solid var(--c-wine-primary); padding: 12px 24px; display: flex; justify-content: space-between; align-items: center;">
        <span style="font-family: var(--font-sans); font-size: 22px; font-weight: 700; color: #110103;">
          <strong style="color: var(--c-wine-primary);">Directriz metodológica:</strong> El entorno pedagógico y la supervisión definen el modelo, no el benchmark.
        </span>
        <span style="font-family: var(--font-mono); font-size: 18px; font-weight: 700; color: #5D4A4D;">
          Discusión del paper
        </span>
      </div>

    </div>
'''

HTML_TEMPLATE = '''<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Test Slide 17 Perfect D3</title>
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
    options = [
        ('slide_17_perfect_D3_1.html', 'slide_17_perfect_D3_1.png', CONTENT_PERFECT_1),
        ('slide_17_perfect_D3_2.html', 'slide_17_perfect_D3_2.png', CONTENT_PERFECT_2),
        ('slide_17_perfect_D3_3.html', 'slide_17_perfect_D3_3.png', CONTENT_PERFECT_3),
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
