# -*- coding: utf-8 -*-
import os
from playwright.sync_api import sync_playwright

output_dir = r"C:\Users\ASUS\.gemini\antigravity-ide\brain\a6624504-511c-4b9d-bc9a-468e348bde40"
os.makedirs(output_dir, exist_ok=True)

# ===========================================================================
# F1: Jerarquía 1 + 2 (Foco Diagnóstico Arriba + 2 Escenarios Abajo)
# ===========================================================================
CONTENT_F1 = '''
    <h2 class="s-lead-question" style="font-size: 38px; font-weight: 800; margin: 0; line-height: 1.2; color: #2C0509;">
      Apego al texto no es aprendizaje: criterios para auditar y desplegar tutores
    </h2>

    <div style="display: flex; flex-direction: column; gap: 20px; flex: 1; margin-top: 16px;">
      
      <!-- BLOQUE 1 (FOCO PRINCIPAL): DIAGNÓSTICO METODOLÓGICO -->
      <div style="background: #FAF5F5; border-left: 8px solid var(--c-red-accent); padding: 22px 32px; display: flex; align-items: center; justify-content: space-between; gap: 30px;">
        <div style="flex: 1;">
          <div style="font-family: var(--font-mono); font-size: 18px; font-weight: 800; color: var(--c-red-accent); letter-spacing: 1.5px; margin-bottom: 6px;">
            HALLAZGO CLAVE · LA FALACIA DEL PROMEDIO
          </div>
          <div style="font-family: var(--font-sans); font-size: 28px; color: #110103; font-weight: 700; line-height: 1.3;">
            El puntaje agregado (0.795) mide copia literal, no comprensión. <strong style="color: var(--c-red-accent);">Prohibido promedio único:</strong> auditar fidelidad y rechazo por separado.
          </div>
        </div>
        <div style="background: #FFFFFF; border: 2px solid #E2D9D9; padding: 14px 24px; text-align: center; border-radius: 4px; min-width: 170px;">
          <div style="font-family: var(--font-mono); font-size: 34px; font-weight: 900; color: var(--c-red-accent); line-height: 1;">0.795</div>
          <div style="font-family: var(--font-sans); font-size: 15px; font-weight: 800; color: #5D4A4D; margin-top: 4px; text-transform: uppercase;">Apego engañoso</div>
        </div>
      </div>

      <!-- BLOQUE 2: DOS RUTAS DE DESPLIEGUE CLARAS -->
      <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 24px; flex: 1;">
        
        <!-- Tarjeta Izquierda: Autoestudio -->
        <div style="background: #FAF5F5; border-top: 8px solid var(--c-wine-primary); padding: 30px 36px; display: flex; flex-direction: column; justify-content: space-between;">
          <div>
            <div style="display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 8px;">
              <span style="font-family: var(--font-mono); font-size: 18px; font-weight: 800; color: var(--c-wine-primary); letter-spacing: 1.5px;">
                ESCENARIO A · AUTOESTUDIO
              </span>
              <span style="font-family: var(--font-mono); font-size: 22px; font-weight: 900; color: var(--c-wine-primary);">
                Qwen2.5-3B
              </span>
            </div>
            <div style="font-family: var(--font-sans); font-size: 34px; font-weight: 900; color: var(--c-wine-primary); margin-bottom: 12px;">
              Sin docente: Certeza
            </div>
            <div style="font-family: var(--font-sans); font-size: 26px; color: #110103; line-height: 1.35; font-weight: 600;">
              En soledad, prima no desinformar. Preferible admitir desconocimiento antes que alucinar.
            </div>
          </div>
          
          <div style="background: #FFFFFF; border-left: 5px solid var(--c-wine-primary); padding: 12px 20px; display: flex; align-items: center; justify-content: space-between; margin-top: 14px;">
            <span style="font-family: var(--font-sans); font-size: 19px; font-weight: 800; color: #110103;">Tasa de rechazo certero:</span>
            <span style="font-family: var(--font-mono); font-size: 26px; font-weight: 900; color: var(--c-wine-primary);">85.7%</span>
          </div>
        </div>

        <!-- Tarjeta Derecha: Aula Asistida -->
        <div style="background: #FAF5F5; border-top: 8px solid var(--c-red-accent); padding: 30px 36px; display: flex; flex-direction: column; justify-content: space-between;">
          <div>
            <div style="display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 8px;">
              <span style="font-family: var(--font-mono); font-size: 18px; font-weight: 800; color: var(--c-red-accent); letter-spacing: 1.5px;">
                ESCENARIO B · AULA ASISTIDA
              </span>
              <span style="font-family: var(--font-mono); font-size: 22px; font-weight: 900; color: var(--c-red-accent);">
                Phi-4-mini
              </span>
            </div>
            <div style="font-family: var(--font-sans); font-size: 34px; font-weight: 900; color: var(--c-red-accent); margin-bottom: 12px;">
              Con docente: Fluidez
            </div>
            <div style="font-family: var(--font-sans); font-size: 26px; color: #110103; line-height: 1.35; font-weight: 600;">
              En clase, prima dinamizar. No interrumpe la sesión y el profesor corrige imprecisiones en vivo.
            </div>
          </div>

          <div style="background: #FFFFFF; border-left: 5px solid var(--c-red-accent); padding: 12px 20px; display: flex; align-items: center; justify-content: space-between; margin-top: 14px;">
            <span style="font-family: var(--font-sans); font-size: 19px; font-weight: 800; color: #110103;">Bloqueos al diálogo:</span>
            <span style="font-family: var(--font-mono); font-size: 26px; font-weight: 900; color: var(--c-red-accent);">0.0%</span>
          </div>
        </div>

      </div>

    </div>
'''

# ===========================================================================
# F2: Matriz 2x2 Despejada con Foco Visual Claro (Sin etiquetas redundantes)
# ===========================================================================
CONTENT_F2 = '''
    <h2 class="s-lead-question" style="font-size: 38px; font-weight: 800; margin: 0; line-height: 1.2; color: #2C0509;">
      Apego al texto no es aprendizaje: criterios para auditar y desplegar tutores
    </h2>

    <div style="display: grid; grid-template-columns: 1fr 1fr; grid-template-rows: 1fr 1fr; gap: 24px; flex: 1; margin-top: 16px;">
      
      <!-- Cuadrante 1: Diagnóstico -->
      <div style="background: #FAF5F5; border-left: 8px solid var(--c-red-accent); padding: 26px 36px; display: flex; flex-direction: column; justify-content: center;">
        <div style="font-family: var(--font-sans); font-size: 32px; font-weight: 900; color: var(--c-red-accent); margin-bottom: 10px;">
          1. Apego &ne; Aprendizaje
        </div>
        <div style="font-family: var(--font-sans); font-size: 28px; color: #110103; line-height: 1.35; font-weight: 600;">
          El puntaje de 0.795 mide copia del libro, no comprensión real del alumno.
        </div>
      </div>

      <!-- Cuadrante 2: Auditoría -->
      <div style="background: #FAF5F5; border-left: 8px solid #B38600; padding: 26px 36px; display: flex; flex-direction: column; justify-content: center;">
        <div style="font-family: var(--font-sans); font-size: 32px; font-weight: 900; color: #B38600; margin-bottom: 10px;">
          2. Auditoría Desglosada
        </div>
        <div style="font-family: var(--font-sans); font-size: 28px; color: #110103; line-height: 1.35; font-weight: 600;">
          <strong>Prohibido promedio único:</strong> calificar fidelidad y rechazo por separado.
        </div>
      </div>

      <!-- Cuadrante 3: Qwen (Foco de decisión) -->
      <div style="background: #F5EBEB; border-left: 8px solid var(--c-wine-primary); padding: 26px 36px; display: flex; flex-direction: column; justify-content: center;">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px;">
          <div style="font-family: var(--font-sans); font-size: 32px; font-weight: 900; color: var(--c-wine-primary);">
            3. Autoestudio (Qwen)
          </div>
          <span style="font-family: var(--font-mono); font-size: 24px; font-weight: 900; color: var(--c-wine-primary);">
            85.7% Rechazo
          </span>
        </div>
        <div style="font-family: var(--font-sans); font-size: 28px; color: #110103; line-height: 1.35; font-weight: 600;">
          <strong>Sin docente:</strong> Prima la <strong>certeza</strong>. Mejor admitir ignorancia que alucinar.
        </div>
      </div>

      <!-- Cuadrante 4: Phi (Foco de decisión) -->
      <div style="background: #FBEAEA; border-left: 8px solid var(--c-red-accent); padding: 26px 36px; display: flex; flex-direction: column; justify-content: center;">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px;">
          <div style="font-family: var(--font-sans); font-size: 32px; font-weight: 900; color: var(--c-red-accent);">
            4. Aula con Docente (Phi)
          </div>
          <span style="font-family: var(--font-mono); font-size: 24px; font-weight: 900; color: var(--c-red-accent);">
            0.0% Bloqueos
          </span>
        </div>
        <div style="font-family: var(--font-sans); font-size: 28px; color: #110103; line-height: 1.35; font-weight: 600;">
          <strong>Con docente:</strong> Prima la <strong>fluidez</strong>. Dinamiza la clase y el profesor corrige.
        </div>
      </div>

    </div>
'''

# ===========================================================================
# F3: El Foco es la Decisión (2 Grandes Columnas Heroicas de Despliegue)
# ===========================================================================
CONTENT_F3 = '''
    <div style="display: flex; justify-content: space-between; align-items: baseline;">
      <h2 class="s-lead-question" style="font-size: 38px; font-weight: 800; margin: 0; line-height: 1.2; color: #2C0509;">
        ¿Qué tutor desplegar según la supervisión pedagógica?
      </h2>
      <span style="font-family: var(--font-mono); font-size: 18px; font-weight: 800; color: var(--c-red-accent); background: #FAF5F5; border: 1.5px solid var(--c-red-accent); padding: 6px 16px;">
        Apego 0.795 &ne; Aprendizaje
      </span>
    </div>

    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 32px; flex: 1; margin-top: 18px;">
      
      <!-- Gran Columna 1: Autoestudio -->
      <div style="background: #FAF5F5; border-top: 10px solid var(--c-wine-primary); padding: 36px 42px; display: flex; flex-direction: column; justify-content: space-between;">
        <div>
          <div style="font-family: var(--font-mono); font-size: 20px; font-weight: 800; color: var(--c-wine-primary); letter-spacing: 1.5px; margin-bottom: 8px;">
            ESCENARIO AUTÓNOMO · SIN DOCENTE
          </div>
          <div style="font-family: var(--font-sans); font-size: 42px; font-weight: 900; color: var(--c-wine-primary); line-height: 1.1; margin-bottom: 16px;">
            Qwen2.5-3B
          </div>
          
          <div style="font-family: var(--font-sans); font-size: 32px; font-weight: 800; color: #110103; margin-bottom: 12px;">
            Criterio: Certeza Absoluta
          </div>
          <div style="font-family: var(--font-sans); font-size: 28px; color: #110103; line-height: 1.35; font-weight: 600;">
            En soledad, alucinar rompe la confianza. Es preferible admitir no saber antes que inventar.
          </div>
        </div>

        <div style="display: flex; align-items: baseline; gap: 16px; border-top: 2px solid #E2D9D9; padding-top: 18px;">
          <span style="font-family: var(--font-mono); font-size: 52px; font-weight: 900; color: var(--c-wine-primary); line-height: 1;">85.7%</span>
          <span style="font-family: var(--font-sans); font-size: 22px; font-weight: 700; color: #5D4A4D;">Rechazo certero en preguntas trampa</span>
        </div>
      </div>

      <!-- Gran Columna 2: Aula Asistida -->
      <div style="background: #FAF5F5; border-top: 10px solid var(--c-red-accent); padding: 36px 42px; display: flex; flex-direction: column; justify-content: space-between;">
        <div>
          <div style="font-family: var(--font-mono); font-size: 20px; font-weight: 800; color: var(--c-red-accent); letter-spacing: 1.5px; margin-bottom: 8px;">
            ESCENARIO GRUPAL · CON DOCENTE
          </div>
          <div style="font-family: var(--font-sans); font-size: 42px; font-weight: 900; color: var(--c-red-accent); line-height: 1.1; margin-bottom: 16px;">
            Phi-4-mini
          </div>
          
          <div style="font-family: var(--font-sans); font-size: 32px; font-weight: 800; color: #110103; margin-bottom: 12px;">
            Criterio: Fluidez Interactiva
          </div>
          <div style="font-family: var(--font-sans); font-size: 28px; color: #110103; line-height: 1.35; font-weight: 600;">
            En clase, prima el ritmo pedagógico. No frena la sesión y el profesor corrige en tiempo real.
          </div>
        </div>

        <div style="display: flex; align-items: baseline; gap: 16px; border-top: 2px solid #E2D9D9; padding-top: 18px;">
          <span style="font-family: var(--font-mono); font-size: 52px; font-weight: 900; color: var(--c-red-accent); line-height: 1;">0.0%</span>
          <span style="font-family: var(--font-sans); font-size: 22px; font-weight: 700; color: #5D4A4D;">Bloqueos innecesarios al estudiante</span>
        </div>
      </div>

    </div>
'''

HTML_TEMPLATE = '''<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Test Slide 17 Focus Options</title>
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
        ('slide_17_focus_F1.html', 'slide_17_focus_F1.png', CONTENT_F1),
        ('slide_17_focus_F2.html', 'slide_17_focus_F2.png', CONTENT_F2),
        ('slide_17_focus_F3.html', 'slide_17_focus_F3.png', CONTENT_F3),
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
