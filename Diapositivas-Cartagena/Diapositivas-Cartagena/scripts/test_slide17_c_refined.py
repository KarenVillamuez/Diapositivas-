# -*- coding: utf-8 -*-
import os
from playwright.sync_api import sync_playwright

output_dir = r"C:\Users\ASUS\.gemini\antigravity-ide\brain\a6624504-511c-4b9d-bc9a-468e348bde40"
os.makedirs(output_dir, exist_ok=True)

# ===========================================================================
# C-V1: Fila Inferior con Métrica Monumental al Pie (52px)
# Las 4 tarjetas tienen una métrica gigante que es IMPOSIBLE de pasar por alto.
# ===========================================================================
CONTENT_CV1 = '''
    <h2 class="s-lead-question" style="font-size: 38px; font-weight: 800; margin: 0; line-height: 1.2; color: #2C0509;">
      Apego al texto no es aprendizaje: criterios para auditar y desplegar tutores
    </h2>

    <div style="display: grid; grid-template-columns: 1fr 1fr; grid-template-rows: 1fr 1fr; gap: 24px; flex: 1; margin-top: 14px;">
      
      <!-- C1: El Diagnóstico Crítico (Rojo Alerta) -->
      <div style="background: #FAF5F5; border-top: 8px solid var(--c-red-accent); padding: 24px 32px; display: flex; flex-direction: column; justify-content: space-between;">
        <div>
          <div style="font-family: var(--font-mono); font-size: 17px; font-weight: 800; color: var(--c-red-accent); letter-spacing: 1.5px; margin-bottom: 6px;">
            01 · ALERTA METODOLÓGICA
          </div>
          <div style="font-family: var(--font-sans); font-size: 32px; font-weight: 900; color: var(--c-red-accent); margin-bottom: 8px;">
            La Falacia del Promedio
          </div>
          <div style="font-family: var(--font-sans); font-size: 24px; color: #110103; line-height: 1.35; font-weight: 600;">
            El puntaje global mide copia textual del libro, pero encubre que el modelo inventa cuando no sabe.
          </div>
        </div>
        <div style="display: flex; align-items: baseline; gap: 14px; border-top: 2px solid #E5D5D5; padding-top: 12px; margin-top: 10px;">
          <span style="font-family: var(--font-mono); font-size: 48px; font-weight: 900; color: var(--c-red-accent); line-height: 1;">0.795</span>
          <span style="font-family: var(--font-sans); font-size: 19px; font-weight: 800; color: #5D4A4D;">Apego engañoso (no predice aprendizaje)</span>
        </div>
      </div>

      <!-- C2: La Regla Metodológica (Vino Institucional) -->
      <div style="background: #FAF5F5; border-top: 8px solid var(--c-wine-primary); padding: 24px 32px; display: flex; flex-direction: column; justify-content: space-between;">
        <div>
          <div style="font-family: var(--font-mono); font-size: 17px; font-weight: 800; color: var(--c-wine-primary); letter-spacing: 1.5px; margin-bottom: 6px;">
            02 · PROTOCOLO DE EVALUACIÓN
          </div>
          <div style="font-family: var(--font-sans); font-size: 32px; font-weight: 900; color: var(--c-wine-primary); margin-bottom: 8px;">
            Auditoría Desglosada
          </div>
          <div style="font-family: var(--font-sans); font-size: 24px; color: #110103; line-height: 1.35; font-weight: 600;">
            <strong>Prohibido calificar con un solo número:</strong> es obligatorio medir recuperación, fidelidad y rechazo por separado.
          </div>
        </div>
        <div style="display: flex; align-items: baseline; gap: 14px; border-top: 2px solid #E5D5D5; padding-top: 12px; margin-top: 10px;">
          <span style="font-family: var(--font-mono); font-size: 48px; font-weight: 900; color: var(--c-wine-primary); line-height: 1;">3</span>
          <span style="font-family: var(--font-sans); font-size: 19px; font-weight: 800; color: #5D4A4D;">Dimensiones obligatorias independientes</span>
        </div>
      </div>

      <!-- C3: Qwen2.5-3B (Vino de Certeza) -->
      <div style="background: #FAF5F5; border-top: 8px solid var(--c-wine-primary); padding: 24px 32px; display: flex; flex-direction: column; justify-content: space-between;">
        <div>
          <div style="font-family: var(--font-mono); font-size: 17px; font-weight: 800; color: var(--c-wine-primary); letter-spacing: 1.5px; margin-bottom: 6px;">
            03 · AUTOESTUDIO SIN DOCENTE
          </div>
          <div style="font-family: var(--font-sans); font-size: 32px; font-weight: 900; color: var(--c-wine-primary); margin-bottom: 8px;">
            Qwen2.5-3B: Prioridad Certeza
          </div>
          <div style="font-family: var(--font-sans); font-size: 24px; color: #110103; line-height: 1.35; font-weight: 600;">
            Sin profesor que supervise, inventar una respuesta confunde al alumno. Es preferible admitir no saber.
          </div>
        </div>
        <div style="display: flex; align-items: baseline; gap: 14px; border-top: 2px solid #E5D5D5; padding-top: 12px; margin-top: 10px;">
          <span style="font-family: var(--font-mono); font-size: 52px; font-weight: 900; color: var(--c-wine-primary); line-height: 1;">85.7%</span>
          <span style="font-family: var(--font-sans); font-size: 19px; font-weight: 800; color: #110103;">Rechazo certero ante preguntas trampa</span>
        </div>
      </div>

      <!-- C4: Phi-4-mini (Rojo de Fluidez y Acción) -->
      <div style="background: #FAF5F5; border-top: 8px solid var(--c-red-accent); padding: 24px 32px; display: flex; flex-direction: column; justify-content: space-between;">
        <div>
          <div style="font-family: var(--font-mono); font-size: 17px; font-weight: 800; color: var(--c-red-accent); letter-spacing: 1.5px; margin-bottom: 6px;">
            04 · AULA ASISTIDA CON DOCENTE
          </div>
          <div style="font-family: var(--font-sans); font-size: 32px; font-weight: 900; color: var(--c-red-accent); margin-bottom: 8px;">
            Phi-4-mini: Prioridad Fluidez
          </div>
          <div style="font-family: var(--font-sans); font-size: 24px; color: #110103; line-height: 1.35; font-weight: 600;">
            Con profesor en el aula, no interrumpe el ritmo pedagógico y el docente modera y corrige en vivo.
          </div>
        </div>
        <div style="display: flex; align-items: baseline; gap: 14px; border-top: 2px solid #E5D5D5; padding-top: 12px; margin-top: 10px;">
          <span style="font-family: var(--font-mono); font-size: 52px; font-weight: 900; color: var(--c-red-accent); line-height: 1;">0.0%</span>
          <span style="font-family: var(--font-sans); font-size: 19px; font-weight: 800; color: #110103;">Bloqueos innecesarios al estudiante</span>
        </div>
      </div>

    </div>
'''

# ===========================================================================
# C-V2: Badges Monumentales de Alto Contraste (Placas de Color con Texto Blanco)
# Los porcentajes resaltan como botones o medallas visuales de inmediato.
# ===========================================================================
CONTENT_CV2 = '''
    <h2 class="s-lead-question" style="font-size: 38px; font-weight: 800; margin: 0; line-height: 1.2; color: #2C0509;">
      Apego al texto no es aprendizaje: criterios para auditar y desplegar tutores
    </h2>

    <div style="display: grid; grid-template-columns: 1fr 1fr; grid-template-rows: 1fr 1fr; gap: 24px; flex: 1; margin-top: 14px;">
      
      <!-- C1 -->
      <div style="background: #FAF5F5; border-left: 8px solid var(--c-red-accent); padding: 26px 32px; display: flex; flex-direction: column; justify-content: space-between;">
        <div style="display: flex; justify-content: space-between; align-items: flex-start; gap: 16px;">
          <div>
            <div style="font-family: var(--font-mono); font-size: 16px; font-weight: 800; color: var(--c-red-accent); letter-spacing: 1.5px; margin-bottom: 4px;">
              EL PROBLEMA
            </div>
            <div style="font-family: var(--font-sans); font-size: 30px; font-weight: 900; color: #110103;">
              La Falacia del Promedio
            </div>
          </div>
          <div style="background: #E52535; color: #FFFFFF; padding: 6px 14px; text-align: center; border-radius: 4px; white-space: nowrap;">
            <div style="font-family: var(--font-mono); font-size: 28px; font-weight: 900; line-height: 1;">0.795</div>
            <div style="font-family: var(--font-sans); font-size: 11px; font-weight: 800; letter-spacing: 1px;">ENGAÑOSO</div>
          </div>
        </div>
        <div style="font-family: var(--font-sans); font-size: 25px; color: #110103; line-height: 1.35; font-weight: 600; margin-top: 10px;">
          El puntaje agregado premia la copia literal del libro, pero encubre que el tutor inventa cuando no sabe.
        </div>
      </div>

      <!-- C2 -->
      <div style="background: #FAF5F5; border-left: 8px solid var(--c-wine-primary); padding: 26px 32px; display: flex; flex-direction: column; justify-content: space-between;">
        <div style="display: flex; justify-content: space-between; align-items: flex-start; gap: 16px;">
          <div>
            <div style="font-family: var(--font-mono); font-size: 16px; font-weight: 800; color: var(--c-wine-primary); letter-spacing: 1.5px; margin-bottom: 4px;">
              EL PROTOCOLO
            </div>
            <div style="font-family: var(--font-sans); font-size: 30px; font-weight: 900; color: #110103;">
              Auditoría Desglosada
            </div>
          </div>
          <div style="background: var(--c-wine-primary); color: #FFFFFF; padding: 6px 14px; text-align: center; border-radius: 4px; white-space: nowrap;">
            <div style="font-family: var(--font-mono); font-size: 28px; font-weight: 900; line-height: 1;">3 METRICAS</div>
            <div style="font-family: var(--font-sans); font-size: 11px; font-weight: 800; letter-spacing: 1px;">SEPARADAS</div>
          </div>
        </div>
        <div style="font-family: var(--font-sans); font-size: 25px; color: #110103; line-height: 1.35; font-weight: 600; margin-top: 10px;">
          <strong style="color: var(--c-wine-primary);">Prohibida la nota única:</strong> es obligatorio auditar recuperación, fidelidad contextual y rechazo por separado.
        </div>
      </div>

      <!-- C3 -->
      <div style="background: #FAF5F5; border-left: 8px solid var(--c-wine-primary); padding: 26px 32px; display: flex; flex-direction: column; justify-content: space-between;">
        <div style="display: flex; justify-content: space-between; align-items: flex-start; gap: 16px;">
          <div>
            <div style="font-family: var(--font-mono); font-size: 16px; font-weight: 800; color: var(--c-wine-primary); letter-spacing: 1.5px; margin-bottom: 4px;">
              DESPLIEGUE A · SIN DOCENTE
            </div>
            <div style="font-family: var(--font-sans); font-size: 30px; font-weight: 900; color: var(--c-wine-primary);">
              Autoestudio (Qwen2.5-3B)
            </div>
          </div>
          <div style="background: var(--c-wine-primary); color: #FFFFFF; padding: 8px 16px; text-align: center; border-radius: 4px; white-space: nowrap;">
            <div style="font-family: var(--font-mono); font-size: 34px; font-weight: 900; line-height: 1;">85.7%</div>
            <div style="font-family: var(--font-sans); font-size: 11px; font-weight: 800; letter-spacing: 1px;">RECHAZO</div>
          </div>
        </div>
        <div style="font-family: var(--font-sans); font-size: 25px; color: #110103; line-height: 1.35; font-weight: 600; margin-top: 10px;">
          <strong>Prioridad Certeza:</strong> Al no haber profesor, admitir ignorancia es pedagógico; inventar deseduca.
        </div>
      </div>

      <!-- C4 -->
      <div style="background: #FAF5F5; border-left: 8px solid var(--c-red-accent); padding: 26px 32px; display: flex; flex-direction: column; justify-content: space-between;">
        <div style="display: flex; justify-content: space-between; align-items: flex-start; gap: 16px;">
          <div>
            <div style="font-family: var(--font-mono); font-size: 16px; font-weight: 800; color: var(--c-red-accent); letter-spacing: 1.5px; margin-bottom: 4px;">
              DESPLIEGUE B · CON DOCENTE
            </div>
            <div style="font-family: var(--font-sans); font-size: 30px; font-weight: 900; color: var(--c-red-accent);">
              Aula Guiada (Phi-4-mini)
            </div>
          </div>
          <div style="background: #E52535; color: #FFFFFF; padding: 8px 16px; text-align: center; border-radius: 4px; white-space: nowrap;">
            <div style="font-family: var(--font-mono); font-size: 34px; font-weight: 900; line-height: 1;">0.0%</div>
            <div style="font-family: var(--font-sans); font-size: 11px; font-weight: 800; letter-spacing: 1px;">BLOQUEOS</div>
          </div>
        </div>
        <div style="font-family: var(--font-sans); font-size: 25px; color: #110103; line-height: 1.35; font-weight: 600; margin-top: 10px;">
          <strong>Prioridad Fluidez:</strong> No interrumpe la sesión y el docente modera y corrige imprecisiones en tiempo real.
        </div>
      </div>

    </div>
'''

# ===========================================================================
# C-V3: Split Interno con Columna Numérica Heroica (60px) en cada Cuadrante
# El número es el ancla visual izquierdo/derecho en cada tarjeta.
# ===========================================================================
CONTENT_CV3 = '''
    <h2 class="s-lead-question" style="font-size: 38px; font-weight: 800; margin: 0; line-height: 1.2; color: #2C0509;">
      Apego al texto no es aprendizaje: criterios para auditar y desplegar tutores
    </h2>

    <div style="display: grid; grid-template-columns: 1fr 1fr; grid-template-rows: 1fr 1fr; gap: 24px; flex: 1; margin-top: 14px;">
      
      <!-- C1 -->
      <div style="background: #FAF5F5; border-top: 8px solid var(--c-red-accent); padding: 22px 28px; display: grid; grid-template-columns: 1fr 140px; gap: 20px; align-items: center;">
        <div>
          <div style="font-family: var(--font-mono); font-size: 16px; font-weight: 800; color: var(--c-red-accent); letter-spacing: 1.5px; margin-bottom: 4px;">
            01 · DIAGNÓSTICO
          </div>
          <div style="font-family: var(--font-sans); font-size: 30px; font-weight: 900; color: var(--c-red-accent); margin-bottom: 8px;">
            La Falacia del Promedio
          </div>
          <div style="font-family: var(--font-sans); font-size: 23px; color: #110103; line-height: 1.35; font-weight: 600;">
            Mide copia del texto base, pero encubre que el tutor inventa respuestas erróneas.
          </div>
        </div>
        <div style="text-align: center; border-left: 2px solid #E5D5D5; padding-left: 16px;">
          <div style="font-family: var(--font-mono); font-size: 46px; font-weight: 900; color: var(--c-red-accent); line-height: 1;">0.795</div>
          <div style="font-family: var(--font-sans); font-size: 14px; font-weight: 800; color: #5D4A4D; margin-top: 6px;">Engañoso</div>
        </div>
      </div>

      <!-- C2 -->
      <div style="background: #FAF5F5; border-top: 8px solid var(--c-wine-primary); padding: 22px 28px; display: grid; grid-template-columns: 1fr 140px; gap: 20px; align-items: center;">
        <div>
          <div style="font-family: var(--font-mono); font-size: 16px; font-weight: 800; color: var(--c-wine-primary); letter-spacing: 1.5px; margin-bottom: 4px;">
            02 · PROTOCOLO
          </div>
          <div style="font-family: var(--font-sans); font-size: 30px; font-weight: 900; color: var(--c-wine-primary); margin-bottom: 8px;">
            Auditoría Desglosada
          </div>
          <div style="font-family: var(--font-sans); font-size: 23px; color: #110103; line-height: 1.35; font-weight: 600;">
            <strong>Prohibida la nota única:</strong> calificar recuperación, fidelidad y rechazo por separado.
          </div>
        </div>
        <div style="text-align: center; border-left: 2px solid #E5D5D5; padding-left: 16px;">
          <div style="font-family: var(--font-mono); font-size: 46px; font-weight: 900; color: var(--c-wine-primary); line-height: 1;">3</div>
          <div style="font-family: var(--font-sans); font-size: 14px; font-weight: 800; color: #5D4A4D; margin-top: 6px;">Dimensiones</div>
        </div>
      </div>

      <!-- C3 -->
      <div style="background: #FAF5F5; border-top: 8px solid var(--c-wine-primary); padding: 22px 28px; display: grid; grid-template-columns: 1fr 160px; gap: 20px; align-items: center;">
        <div>
          <div style="font-family: var(--font-mono); font-size: 16px; font-weight: 800; color: var(--c-wine-primary); letter-spacing: 1.5px; margin-bottom: 4px;">
            03 · SIN DOCENTE
          </div>
          <div style="font-family: var(--font-sans); font-size: 30px; font-weight: 900; color: var(--c-wine-primary); margin-bottom: 8px;">
            Qwen2.5-3B: Certeza
          </div>
          <div style="font-family: var(--font-sans); font-size: 23px; color: #110103; line-height: 1.35; font-weight: 600;">
            En autoestudio no hay profesor que corrija. Admitir ignorancia evita enseñar falsedades.
          </div>
        </div>
        <div style="text-align: center; border-left: 2px solid #E5D5D5; padding-left: 16px;">
          <div style="font-family: var(--font-mono); font-size: 52px; font-weight: 900; color: var(--c-wine-primary); line-height: 1;">85.7%</div>
          <div style="font-family: var(--font-sans); font-size: 14px; font-weight: 800; color: var(--c-wine-primary); margin-top: 6px;">Rechazo Certero</div>
        </div>
      </div>

      <!-- C4 -->
      <div style="background: #FAF5F5; border-top: 8px solid var(--c-red-accent); padding: 22px 28px; display: grid; grid-template-columns: 1fr 160px; gap: 20px; align-items: center;">
        <div>
          <div style="font-family: var(--font-mono); font-size: 16px; font-weight: 800; color: var(--c-red-accent); letter-spacing: 1.5px; margin-bottom: 4px;">
            04 · CON DOCENTE
          </div>
          <div style="font-family: var(--font-sans); font-size: 30px; font-weight: 900; color: var(--c-red-accent); margin-bottom: 8px;">
            Phi-4-mini: Fluidez
          </div>
          <div style="font-family: var(--font-sans); font-size: 23px; color: #110103; line-height: 1.35; font-weight: 600;">
            En aula, dinamiza la clase sin interrupciones y el docente corrige imprecisiones en vivo.
          </div>
        </div>
        <div style="text-align: center; border-left: 2px solid #E5D5D5; padding-left: 16px;">
          <div style="font-family: var(--font-mono); font-size: 52px; font-weight: 900; color: var(--c-red-accent); line-height: 1;">0.0%</div>
          <div style="font-family: var(--font-sans); font-size: 14px; font-weight: 800; color: var(--c-red-accent); margin-top: 6px;">Bloqueos</div>
        </div>
      </div>

    </div>
'''

HTML_TEMPLATE = '''<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Test Slide 17 C Refined</title>
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
        ('slide_17_cv1.html', 'slide_17_cv1.png', CONTENT_CV1),
        ('slide_17_cv2.html', 'slide_17_cv2.png', CONTENT_CV2),
        ('slide_17_cv3.html', 'slide_17_cv3.png', CONTENT_CV3),
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
