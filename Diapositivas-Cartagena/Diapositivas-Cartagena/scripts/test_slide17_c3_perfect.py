# -*- coding: utf-8 -*-
import os
from playwright.sync_api import sync_playwright

output_dir = r"C:\Users\ASUS\.gemini\antigravity-ide\brain\a6624504-511c-4b9d-bc9a-468e348bde40"
os.makedirs(output_dir, exist_ok=True)

# ===========================================================================
# C3-V1: Cabecera Integrada (Título 36px Izq + Número 56px Der sin caja) + Texto 27px
# ===========================================================================
CONTENT_C3_V1 = '''
    <h2 class="s-lead-question" style="font-size: 38px; font-weight: 800; margin: 0; line-height: 1.2; color: #2C0509;">
      Apego al texto no es aprendizaje: criterios para auditar y desplegar tutores
    </h2>

    <div style="display: grid; grid-template-columns: 1fr 1fr; grid-template-rows: 1fr 1fr; gap: 24px; flex: 1; margin-top: 14px;">
      
      <!-- C1: La Falacia del Promedio -->
      <div style="background: #FAF5F5; border-top: 8px solid #C51625; padding: 28px 36px; display: flex; flex-direction: column; justify-content: space-between;">
        <div>
          <div style="display: flex; justify-content: space-between; align-items: flex-start;">
            <div>
              <div style="font-family: var(--font-mono); font-size: 16px; font-weight: 800; color: #C51625; letter-spacing: 1.5px; margin-bottom: 4px;">
                01 · EL RIESGO OCULTO
              </div>
              <div style="font-family: var(--font-sans); font-size: 35px; font-weight: 900; color: #110103;">
                La Falacia del Promedio
              </div>
            </div>
            <div style="text-align: right;">
              <div style="font-family: var(--font-mono); font-size: 54px; font-weight: 900; color: #C51625; line-height: 1;">0.795</div>
              <div style="font-family: var(--font-mono); font-size: 14px; font-weight: 800; color: #C51625; letter-spacing: 1px; margin-top: 2px;">APEGO ENGAÑOSO</div>
            </div>
          </div>
          <div style="border-top: 2px solid #E5D5D5; margin-top: 14px; margin-bottom: 14px;"></div>
        </div>
        <div style="font-family: var(--font-sans); font-size: 26px; color: #110103; line-height: 1.38; font-weight: 600;">
          El puntaje premia copiar del libro, pero encubre que el tutor inventa respuestas erróneas cuando no sabe.
        </div>
      </div>

      <!-- C2: Auditoría Desglosada -->
      <div style="background: #FAF5F5; border-top: 8px solid #4A3B3D; padding: 28px 36px; display: flex; flex-direction: column; justify-content: space-between;">
        <div>
          <div style="display: flex; justify-content: space-between; align-items: flex-start;">
            <div>
              <div style="font-family: var(--font-mono); font-size: 16px; font-weight: 800; color: #4A3B3D; letter-spacing: 1.5px; margin-bottom: 4px;">
                02 · EL ESTÁNDAR TÉCNICO
              </div>
              <div style="font-family: var(--font-sans); font-size: 35px; font-weight: 900; color: #110103;">
                Auditoría Desglosada
              </div>
            </div>
            <div style="text-align: right;">
              <div style="font-family: var(--font-mono); font-size: 54px; font-weight: 900; color: #4A3B3D; line-height: 1;">3</div>
              <div style="font-family: var(--font-mono); font-size: 14px; font-weight: 800; color: #4A3B3D; letter-spacing: 1px; margin-top: 2px;">DIMENSIONES</div>
            </div>
          </div>
          <div style="border-top: 2px solid #E5D5D5; margin-top: 14px; margin-bottom: 14px;"></div>
        </div>
        <div style="font-family: var(--font-sans); font-size: 26px; color: #110103; line-height: 1.38; font-weight: 600;">
          <strong style="color: #4A3B3D;">Prohibida la nota única:</strong> es obligatorio evaluar recuperación, fidelidad contextual y rechazo por separado.
        </div>
      </div>

      <!-- C3: Qwen2.5-3B -->
      <div style="background: #FAF5F5; border-top: 8px solid var(--c-wine-primary); padding: 28px 36px; display: flex; flex-direction: column; justify-content: space-between;">
        <div>
          <div style="display: flex; justify-content: space-between; align-items: flex-start;">
            <div>
              <div style="font-family: var(--font-mono); font-size: 16px; font-weight: 800; color: var(--c-wine-primary); letter-spacing: 1.5px; margin-bottom: 4px;">
                03 · AUTOESTUDIO SIN DOCENTE
              </div>
              <div style="font-family: var(--font-sans); font-size: 35px; font-weight: 900; color: var(--c-wine-primary);">
                Qwen2.5-3B: Certeza
              </div>
            </div>
            <div style="text-align: right;">
              <div style="font-family: var(--font-mono); font-size: 56px; font-weight: 900; color: var(--c-wine-primary); line-height: 1;">85.7%</div>
              <div style="font-family: var(--font-mono); font-size: 14px; font-weight: 800; color: var(--c-wine-primary); letter-spacing: 1px; margin-top: 2px;">RECHAZO CERTERO</div>
            </div>
          </div>
          <div style="border-top: 2px solid #E5D5D5; margin-top: 14px; margin-bottom: 14px;"></div>
        </div>
        <div style="font-family: var(--font-sans); font-size: 26px; color: #110103; line-height: 1.38; font-weight: 600;">
          En soledad no hay profesor que corrija. Admitir ignorancia es pedagógico; inventar deseduca al estudiante.
        </div>
      </div>

      <!-- C4: Phi-4-mini -->
      <div style="background: #FAF5F5; border-top: 8px solid var(--c-red-accent); padding: 28px 36px; display: flex; flex-direction: column; justify-content: space-between;">
        <div>
          <div style="display: flex; justify-content: space-between; align-items: flex-start;">
            <div>
              <div style="font-family: var(--font-mono); font-size: 16px; font-weight: 800; color: var(--c-red-accent); letter-spacing: 1.5px; margin-bottom: 4px;">
                04 · AULA ASISTIDA CON DOCENTE
              </div>
              <div style="font-family: var(--font-sans); font-size: 35px; font-weight: 900; color: var(--c-red-accent);">
                Phi-4-mini: Fluidez
              </div>
            </div>
            <div style="text-align: right;">
              <div style="font-family: var(--font-mono); font-size: 56px; font-weight: 900; color: var(--c-red-accent); line-height: 1;">0.0%</div>
              <div style="font-family: var(--font-mono); font-size: 14px; font-weight: 800; color: var(--c-red-accent); letter-spacing: 1px; margin-top: 2px;">BLOQUEOS DE DIÁLOGO</div>
            </div>
          </div>
          <div style="border-top: 2px solid #E5D5D5; margin-top: 14px; margin-bottom: 14px;"></div>
        </div>
        <div style="font-family: var(--font-sans); font-size: 26px; color: #110103; line-height: 1.38; font-weight: 600;">
          En clase interactiva prima mantener el ritmo: no frena al grupo y el docente modera y corrige en tiempo real.
        </div>
      </div>

    </div>
'''

# ===========================================================================
# C3-V2: Flujo Vertical Equilibrado (Todo Grande, Rellenando la Tarjeta Completa)
# ===========================================================================
CONTENT_C3_V2 = '''
    <h2 class="s-lead-question" style="font-size: 38px; font-weight: 800; margin: 0; line-height: 1.2; color: #2C0509;">
      Apego al texto no es aprendizaje: criterios para auditar y desplegar tutores
    </h2>

    <div style="display: grid; grid-template-columns: 1fr 1fr; grid-template-rows: 1fr 1fr; gap: 24px; flex: 1; margin-top: 14px;">
      
      <!-- C1 -->
      <div style="background: #FAF5F5; border-top: 8px solid #C51625; padding: 26px 36px; display: flex; flex-direction: column; justify-content: space-around;">
        <div style="display: flex; justify-content: space-between; align-items: baseline;">
          <span style="font-family: var(--font-mono); font-size: 16px; font-weight: 800; color: #C51625; letter-spacing: 1.5px;">
            01 · EL RIESGO OCULTO
          </span>
          <span style="font-family: var(--font-mono); font-size: 46px; font-weight: 900; color: #C51625;">
            0.795
          </span>
        </div>
        <div style="font-family: var(--font-sans); font-size: 34px; font-weight: 900; color: #110103; margin: 4px 0 8px 0;">
          La Falacia del Promedio
        </div>
        <div style="font-family: var(--font-sans); font-size: 26px; color: #110103; line-height: 1.38; font-weight: 600;">
          Premia copiar palabras del libro, pero encubre que el tutor inventa falsedades al quedarse sin información.
        </div>
      </div>

      <!-- C2 -->
      <div style="background: #FAF5F5; border-top: 8px solid #4A3B3D; padding: 26px 36px; display: flex; flex-direction: column; justify-content: space-around;">
        <div style="display: flex; justify-content: space-between; align-items: baseline;">
          <span style="font-family: var(--font-mono); font-size: 16px; font-weight: 800; color: #4A3B3D; letter-spacing: 1.5px;">
            02 · EL ESTÁNDAR TÉCNICO
          </span>
          <span style="font-family: var(--font-mono); font-size: 46px; font-weight: 900; color: #4A3B3D;">
            3 Dimensiones
          </span>
        </div>
        <div style="font-family: var(--font-sans); font-size: 34px; font-weight: 900; color: #110103; margin: 4px 0 8px 0;">
          Auditoría Desglosada
        </div>
        <div style="font-family: var(--font-sans); font-size: 26px; color: #110103; line-height: 1.38; font-weight: 600;">
          <strong style="color: #4A3B3D;">Prohibida la nota única:</strong> es obligatorio evaluar recuperación, fidelidad contextual y rechazo por separado.
        </div>
      </div>

      <!-- C3 -->
      <div style="background: #FAF5F5; border-top: 8px solid var(--c-wine-primary); padding: 26px 36px; display: flex; flex-direction: column; justify-content: space-around;">
        <div style="display: flex; justify-content: space-between; align-items: baseline;">
          <span style="font-family: var(--font-mono); font-size: 16px; font-weight: 800; color: var(--c-wine-primary); letter-spacing: 1.5px;">
            03 · AUTOESTUDIO SIN DOCENTE
          </span>
          <span style="font-family: var(--font-mono); font-size: 52px; font-weight: 900; color: var(--c-wine-primary);">
            85.7% Rechazo
          </span>
        </div>
        <div style="font-family: var(--font-sans); font-size: 34px; font-weight: 900; color: var(--c-wine-primary); margin: 4px 0 8px 0;">
          Qwen2.5-3B: Certeza
        </div>
        <div style="font-family: var(--font-sans); font-size: 26px; color: #110103; line-height: 1.38; font-weight: 600;">
          En soledad no hay profesor que corrija. Admitir ignorancia es pedagógico; inventar deseduca al estudiante.
        </div>
      </div>

      <!-- C4 -->
      <div style="background: #FAF5F5; border-top: 8px solid var(--c-red-accent); padding: 26px 36px; display: flex; flex-direction: column; justify-content: space-around;">
        <div style="display: flex; justify-content: space-between; align-items: baseline;">
          <span style="font-family: var(--font-mono); font-size: 16px; font-weight: 800; color: var(--c-red-accent); letter-spacing: 1.5px;">
            04 · AULA ASISTIDA CON DOCENTE
          </span>
          <span style="font-family: var(--font-mono); font-size: 52px; font-weight: 900; color: var(--c-red-accent);">
            0.0% Bloqueos
          </span>
        </div>
        <div style="font-family: var(--font-sans); font-size: 34px; font-weight: 900; color: var(--c-red-accent); margin: 4px 0 8px 0;">
          Phi-4-mini: Fluidez
        </div>
        <div style="font-family: var(--font-sans); font-size: 26px; color: #110103; line-height: 1.38; font-weight: 600;">
          En clase interactiva prima mantener el ritmo: no frena al grupo y el docente modera y corrige en vivo.
        </div>
      </div>

    </div>
'''

# ===========================================================================
# C3-V3: Columna Lateral Heroica Pura (Split 70% Texto / 30% Número Monumental 64px)
# Cero cajas: solo una línea divisoria vertical que ancla el número colosal.
# ===========================================================================
CONTENT_C3_V3 = '''
    <h2 class="s-lead-question" style="font-size: 38px; font-weight: 800; margin: 0; line-height: 1.2; color: #2C0509;">
      Apego al texto no es aprendizaje: criterios para auditar y desplegar tutores
    </h2>

    <div style="display: grid; grid-template-columns: 1fr 1fr; grid-template-rows: 1fr 1fr; gap: 24px; flex: 1; margin-top: 14px;">
      
      <!-- C1 -->
      <div style="background: #FAF5F5; border-top: 8px solid #C51625; padding: 26px 32px; display: grid; grid-template-columns: 1fr 190px; gap: 24px; align-items: center;">
        <div>
          <div style="font-family: var(--font-mono); font-size: 15px; font-weight: 800; color: #C51625; letter-spacing: 1.5px; margin-bottom: 4px;">
            01 · EL RIESGO OCULTO
          </div>
          <div style="font-family: var(--font-sans); font-size: 34px; font-weight: 900; color: #110103; margin-bottom: 10px;">
            La Falacia del Promedio
          </div>
          <div style="font-family: var(--font-sans); font-size: 24px; color: #110103; line-height: 1.38; font-weight: 600;">
            Premia copiar del libro, pero encubre que el tutor inventa falsedades cuando no sabe.
          </div>
        </div>
        <div style="border-left: 3px solid #E5D5D5; padding-left: 20px; text-align: center;">
          <div style="font-family: var(--font-mono); font-size: 56px; font-weight: 900; color: #C51625; line-height: 1;">0.795</div>
          <div style="font-family: var(--font-sans); font-size: 16px; font-weight: 800; color: #5D4A4D; margin-top: 6px;">Apego Engañoso</div>
        </div>
      </div>

      <!-- C2 -->
      <div style="background: #FAF5F5; border-top: 8px solid #4A3B3D; padding: 26px 32px; display: grid; grid-template-columns: 1fr 190px; gap: 24px; align-items: center;">
        <div>
          <div style="font-family: var(--font-mono); font-size: 15px; font-weight: 800; color: #4A3B3D; letter-spacing: 1.5px; margin-bottom: 4px;">
            02 · EL ESTÁNDAR TÉCNICO
          </div>
          <div style="font-family: var(--font-sans); font-size: 34px; font-weight: 900; color: #110103; margin-bottom: 10px;">
            Auditoría Desglosada
          </div>
          <div style="font-family: var(--font-sans); font-size: 24px; color: #110103; line-height: 1.38; font-weight: 600;">
            <strong style="color: #4A3B3D;">Prohibida la nota única:</strong> evaluar recuperación, fidelidad y rechazo por separado.
          </div>
        </div>
        <div style="border-left: 3px solid #E5D5D5; padding-left: 20px; text-align: center;">
          <div style="font-family: var(--font-mono); font-size: 56px; font-weight: 900; color: #4A3B3D; line-height: 1;">3</div>
          <div style="font-family: var(--font-sans); font-size: 16px; font-weight: 800; color: #5D4A4D; margin-top: 6px;">Dimensiones</div>
        </div>
      </div>

      <!-- C3 -->
      <div style="background: #FAF5F5; border-top: 8px solid var(--c-wine-primary); padding: 26px 32px; display: grid; grid-template-columns: 1fr 190px; gap: 24px; align-items: center;">
        <div>
          <div style="font-family: var(--font-mono); font-size: 15px; font-weight: 800; color: var(--c-wine-primary); letter-spacing: 1.5px; margin-bottom: 4px;">
            03 · AUTOESTUDIO SIN DOCENTE
          </div>
          <div style="font-family: var(--font-sans); font-size: 34px; font-weight: 900; color: var(--c-wine-primary); margin-bottom: 10px;">
            Qwen2.5-3B: Certeza
          </div>
          <div style="font-family: var(--font-sans); font-size: 24px; color: #110103; line-height: 1.38; font-weight: 600;">
            En soledad no hay profesor que corrija. Admitir ignorancia es pedagógico; inventar deseduca.
          </div>
        </div>
        <div style="border-left: 3px solid #E5D5D5; padding-left: 20px; text-align: center;">
          <div style="font-family: var(--font-mono); font-size: 60px; font-weight: 900; color: var(--c-wine-primary); line-height: 1;">85.7%</div>
          <div style="font-family: var(--font-sans); font-size: 16px; font-weight: 800; color: var(--c-wine-primary); margin-top: 6px;">Rechazo Certero</div>
        </div>
      </div>

      <!-- C4 -->
      <div style="background: #FAF5F5; border-top: 8px solid var(--c-red-accent); padding: 26px 32px; display: grid; grid-template-columns: 1fr 190px; gap: 24px; align-items: center;">
        <div>
          <div style="font-family: var(--font-mono); font-size: 15px; font-weight: 800; color: var(--c-red-accent); letter-spacing: 1.5px; margin-bottom: 4px;">
            04 · AULA ASISTIDA CON DOCENTE
          </div>
          <div style="font-family: var(--font-sans); font-size: 34px; font-weight: 900; color: var(--c-red-accent); margin-bottom: 10px;">
            Phi-4-mini: Fluidez
          </div>
          <div style="font-family: var(--font-sans); font-size: 24px; color: #110103; line-height: 1.38; font-weight: 600;">
            En clase prima no frenar el ritmo: interacción continua y el docente corrige en vivo.
          </div>
        </div>
        <div style="border-left: 3px solid #E5D5D5; padding-left: 20px; text-align: center;">
          <div style="font-family: var(--font-mono); font-size: 60px; font-weight: 900; color: var(--c-red-accent); line-height: 1;">0.0%</div>
          <div style="font-family: var(--font-sans); font-size: 16px; font-weight: 800; color: var(--c-red-accent); margin-top: 6px;">Bloqueos Diálogo</div>
        </div>
      </div>

    </div>
'''

HTML_TEMPLATE = '''<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Test Slide 17 C3 Perfected</title>
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
        ('slide_17_c3_v1.html', 'slide_17_c3_v1.png', CONTENT_C3_V1),
        ('slide_17_c3_v2.html', 'slide_17_c3_v2.png', CONTENT_C3_V2),
        ('slide_17_c3_v3.html', 'slide_17_c3_v3.png', CONTENT_C3_V3),
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
