# -*- coding: utf-8 -*-
import os
from playwright.sync_api import sync_playwright

output_dir = r"C:\Users\ASUS\.gemini\antigravity-ide\brain\a6624504-511c-4b9d-bc9a-468e348bde40"
os.makedirs(output_dir, exist_ok=True)

# ===========================================================================
# OPCIÓN A: "Foco Jerárquico 1 + 2" (Banner de Hallazgo + 2 Vías de Despliegue)
# Sin cajas dentro de cajas. Foco inmediato: Tesis arriba, 2 opciones abajo.
# ===========================================================================
CONTENT_A = '''
    <h2 class="s-lead-question" style="font-size: 38px; font-weight: 800; margin: 0; line-height: 1.2; color: #2C0509;">
      Apego al texto no es aprendizaje: criterios para auditar y desplegar tutores
    </h2>

    <div style="display: flex; flex-direction: column; gap: 22px; flex: 1; margin-top: 14px;">
      
      <!-- BANNER DE FOCO PRINCIPAL: LA TESIS METODOLÓGICA -->
      <div style="background: #FAF5F5; border-left: 8px solid var(--c-wine-primary); padding: 22px 36px; display: flex; align-items: center; justify-content: space-between; gap: 30px;">
        <div style="flex: 1;">
          <div style="font-family: var(--font-mono); font-size: 18px; font-weight: 800; color: var(--c-wine-primary); letter-spacing: 1.5px; margin-bottom: 6px;">
            CRITERIO DE AUDITORÍA · LA FALACIA DEL PROMEDIO
          </div>
          <div style="font-family: var(--font-sans); font-size: 28px; color: #110103; font-weight: 700; line-height: 1.3;">
            El puntaje agregado (0.795) encubre fallos críticos. <strong style="color: var(--c-red-accent);">Prohibido promedio único:</strong> auditar fidelidad y rechazo por separado.
          </div>
        </div>
        <div style="text-align: right; border-left: 2px solid #E2D9D9; padding-left: 28px; min-width: 200px;">
          <div style="font-family: var(--font-mono); font-size: 38px; font-weight: 900; color: var(--c-red-accent); line-height: 1;">0.795</div>
          <div style="font-family: var(--font-sans); font-size: 16px; font-weight: 800; color: #5D4A4D; margin-top: 4px;">APEGO ENGAÑOSO</div>
        </div>
      </div>

      <!-- DOS COLUMNAS DE DESPLIEGUE (CERO CAJAS ANIDADAS, NÚMEROS HEROICOS) -->
      <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 26px; flex: 1;">
        
        <!-- Tarjeta 1: Autoestudio (Qwen) -->
        <div style="background: #FAF5F5; border-top: 8px solid var(--c-wine-primary); padding: 30px 36px; display: flex; flex-direction: column; justify-content: space-between;">
          <div>
            <div style="font-family: var(--font-mono); font-size: 18px; font-weight: 800; color: var(--c-wine-primary); letter-spacing: 1.5px; margin-bottom: 8px;">
              ESCENARIO A · AUTOESTUDIO
            </div>
            <div style="font-family: var(--font-sans); font-size: 38px; font-weight: 900; color: var(--c-wine-primary); margin-bottom: 12px;">
              Qwen2.5-3B
            </div>
            <div style="font-family: var(--font-sans); font-size: 28px; color: #110103; line-height: 1.35; font-weight: 600;">
              <strong>Sin docente:</strong> Prima la <strong style="color: var(--c-wine-primary);">certeza absoluta</strong>. Preferible admitir desconocimiento antes que inventar.
            </div>
          </div>
          
          <div style="display: flex; align-items: baseline; gap: 14px; border-top: 2px solid #E2D9D9; padding-top: 16px; margin-top: 16px;">
            <span style="font-family: var(--font-mono); font-size: 46px; font-weight: 900; color: var(--c-wine-primary); line-height: 1;">85.7%</span>
            <span style="font-family: var(--font-sans); font-size: 20px; font-weight: 800; color: #5D4A4D;">Rechazo certero ante preguntas trampa</span>
          </div>
        </div>

        <!-- Tarjeta 2: Aula Asistida (Phi) -->
        <div style="background: #FAF5F5; border-top: 8px solid var(--c-red-accent); padding: 30px 36px; display: flex; flex-direction: column; justify-content: space-between;">
          <div>
            <div style="font-family: var(--font-mono); font-size: 18px; font-weight: 800; color: var(--c-red-accent); letter-spacing: 1.5px; margin-bottom: 8px;">
              ESCENARIO B · AULA CON DOCENTE
            </div>
            <div style="font-family: var(--font-sans); font-size: 38px; font-weight: 900; color: var(--c-red-accent); margin-bottom: 12px;">
              Phi-4-mini
            </div>
            <div style="font-family: var(--font-sans); font-size: 28px; color: #110103; line-height: 1.35; font-weight: 600;">
              <strong>Con docente:</strong> Prima la <strong style="color: var(--c-red-accent);">fluidez total</strong>. Dinamiza la clase y el profesor corrige en vivo.
            </div>
          </div>

          <div style="display: flex; align-items: baseline; gap: 14px; border-top: 2px solid #E2D9D9; padding-top: 16px; margin-top: 16px;">
            <span style="font-family: var(--font-mono); font-size: 46px; font-weight: 900; color: var(--c-red-accent); line-height: 1;">0.0%</span>
            <span style="font-family: var(--font-sans); font-size: 20px; font-weight: 800; color: #5D4A4D;">Bloqueos innecesarios al diálogo</span>
          </div>
        </div>

      </div>

    </div>
'''

# ===========================================================================
# OPCIÓN B: "Bifurcación Monumental de Despliegue" (2 Grandes Bloques con Foco Extremo)
# El foco es la toma de decisiones. Cero distracciones.
# ===========================================================================
CONTENT_B = '''
    <!-- TÍTULO CON SUBRAYADO EDITORIAL -->
    <div style="display: flex; justify-content: space-between; align-items: flex-end; padding-bottom: 12px; border-bottom: 2px solid #E2D9D9;">
      <div>
        <h2 class="s-lead-question" style="font-size: 38px; font-weight: 800; margin: 0; line-height: 1.2; color: #2C0509;">
          ¿Qué tutor desplegar según la supervisión pedagógica?
        </h2>
        <div style="font-family: var(--font-sans); font-size: 22px; color: #5D4A4D; margin-top: 6px; font-weight: 600;">
          El puntaje agregado (0.795) encubre fallos críticos: el modelo ideal depende del rol docente.
        </div>
      </div>
      <div style="background: #FBEAEA; border: 2px solid var(--c-red-accent); padding: 8px 18px; text-align: center; border-radius: 2px;">
        <span style="font-family: var(--font-mono); font-size: 16px; font-weight: 800; color: var(--c-red-accent); letter-spacing: 1px;">
          APEGO &ne; APRENDIZAJE
        </span>
      </div>
    </div>

    <!-- DOS GRANDES BLOQUES MONUMENTALES -->
    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 32px; flex: 1; margin-top: 18px;">
      
      <!-- Bloque Qwen -->
      <div style="background: #FAF5F5; border-top: 10px solid var(--c-wine-primary); padding: 36px 42px; display: flex; flex-direction: column; justify-content: space-between;">
        <div>
          <div style="font-family: var(--font-mono); font-size: 19px; font-weight: 800; color: var(--c-wine-primary); letter-spacing: 1.5px; margin-bottom: 8px;">
            01 · AUTOESTUDIO SIN DOCENTE
          </div>
          <div style="font-family: var(--font-sans); font-size: 42px; font-weight: 900; color: var(--c-wine-primary); margin-bottom: 14px;">
            Qwen2.5-3B
          </div>
          <div style="font-family: var(--font-sans); font-size: 28px; color: #110103; line-height: 1.4; font-weight: 600;">
            <strong>Prioridad: Certeza.</strong> Al no haber docente, inventar una respuesta deseduca. Es preferible admitir no saber antes que alucinar.
          </div>
        </div>

        <div style="display: flex; align-items: baseline; gap: 16px; border-top: 2px solid #E2D9D9; padding-top: 18px;">
          <span style="font-family: var(--font-mono); font-size: 54px; font-weight: 900; color: var(--c-wine-primary); line-height: 1;">85.7%</span>
          <span style="font-family: var(--font-sans); font-size: 22px; font-weight: 800; color: #5D4A4D;">Rechazo certero en preguntas fuera de contexto</span>
        </div>
      </div>

      <!-- Bloque Phi -->
      <div style="background: #FAF5F5; border-top: 10px solid var(--c-red-accent); padding: 36px 42px; display: flex; flex-direction: column; justify-content: space-between;">
        <div>
          <div style="font-family: var(--font-mono); font-size: 19px; font-weight: 800; color: var(--c-red-accent); letter-spacing: 1.5px; margin-bottom: 8px;">
            02 · AULA CON DOCENTE
          </div>
          <div style="font-family: var(--font-sans); font-size: 42px; font-weight: 900; color: var(--c-red-accent); margin-bottom: 14px;">
            Phi-4-mini
          </div>
          <div style="font-family: var(--font-sans); font-size: 28px; color: #110103; line-height: 1.4; font-weight: 600;">
            <strong>Prioridad: Fluidez.</strong> En clase, no interrumpe el ritmo del aula. El profesor modera y corrige imprecisiones en tiempo real.
          </div>
        </div>

        <div style="display: flex; align-items: baseline; gap: 16px; border-top: 2px solid #E2D9D9; padding-top: 18px;">
          <span style="font-family: var(--font-mono); font-size: 54px; font-weight: 900; color: var(--c-red-accent); line-height: 1;">0.0%</span>
          <span style="font-family: var(--font-sans); font-size: 22px; font-weight: 800; color: #5D4A4D;">Bloqueos al diálogo durante la sesión</span>
        </div>
      </div>

    </div>
'''

# ===========================================================================
# OPCIÓN C: "Matriz D3 con Foco Puro" (2x2 Simplificada al Extremo: Cero Etiquetas)
# Mantiene la estructura cuadrante solicitada, pero con foco unificado y sin ruido.
# ===========================================================================
CONTENT_C = '''
    <h2 class="s-lead-question" style="font-size: 38px; font-weight: 800; margin: 0; line-height: 1.2; color: #2C0509;">
      Apego al texto no es aprendizaje: criterios para auditar y desplegar tutores
    </h2>

    <div style="display: grid; grid-template-columns: 1fr 1fr; grid-template-rows: 1fr 1fr; gap: 24px; flex: 1; margin-top: 16px;">
      
      <!-- C1 -->
      <div style="background: #FAF5F5; border-top: 8px solid var(--c-red-accent); padding: 28px 36px; display: flex; flex-direction: column; justify-content: center;">
        <div style="font-family: var(--font-sans); font-size: 34px; font-weight: 900; color: var(--c-red-accent); margin-bottom: 10px;">
          Apego &ne; Aprendizaje
        </div>
        <div style="font-family: var(--font-sans); font-size: 28px; color: #110103; line-height: 1.35; font-weight: 600;">
          El 0.795 agregado mide copia literal del libro, no comprensión del estudiante.
        </div>
      </div>

      <!-- C2 -->
      <div style="background: #FAF5F5; border-top: 8px solid #B38600; padding: 28px 36px; display: flex; flex-direction: column; justify-content: center;">
        <div style="font-family: var(--font-sans); font-size: 34px; font-weight: 900; color: #B38600; margin-bottom: 10px;">
          Auditoría Desglosada
        </div>
        <div style="font-family: var(--font-sans); font-size: 28px; color: #110103; line-height: 1.35; font-weight: 600;">
          <strong>Prohibido promedio único:</strong> auditar fidelidad contextual y rechazo por separado.
        </div>
      </div>

      <!-- C3 -->
      <div style="background: #FAF5F5; border-top: 8px solid var(--c-wine-primary); padding: 28px 36px; display: flex; flex-direction: column; justify-content: center;">
        <div style="display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 10px;">
          <div style="font-family: var(--font-sans); font-size: 34px; font-weight: 900; color: var(--c-wine-primary);">
            Autoestudio (Qwen)
          </div>
          <span style="font-family: var(--font-mono); font-size: 26px; font-weight: 900; color: var(--c-wine-primary);">
            85.7% Rechazo
          </span>
        </div>
        <div style="font-family: var(--font-sans); font-size: 28px; color: #110103; line-height: 1.35; font-weight: 600;">
          <strong>Sin docente:</strong> Prima la <strong>certeza</strong>. Mejor admitir ignorancia antes que alucinar.
        </div>
      </div>

      <!-- C4 -->
      <div style="background: #FAF5F5; border-top: 8px solid var(--c-red-accent); padding: 28px 36px; display: flex; flex-direction: column; justify-content: center;">
        <div style="display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 10px;">
          <div style="font-family: var(--font-sans); font-size: 34px; font-weight: 900; color: var(--c-red-accent);">
            Aula con Docente (Phi)
          </div>
          <span style="font-family: var(--font-mono); font-size: 26px; font-weight: 900; color: var(--c-red-accent);">
            0.0% Bloqueos
          </span>
        </div>
        <div style="font-family: var(--font-sans); font-size: 28px; color: #110103; line-height: 1.35; font-weight: 600;">
          <strong>Con docente:</strong> Prima la <strong>fluidez</strong>. Dinamiza la clase y el profesor corrige en vivo.
        </div>
      </div>

    </div>
'''

HTML_TEMPLATE = '''<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Test Slide 17 Ultimate Focus</title>
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
        ('slide_17_ultimate_A.html', 'slide_17_ultimate_A.png', CONTENT_A),
        ('slide_17_ultimate_B.html', 'slide_17_ultimate_B.png', CONTENT_B),
        ('slide_17_ultimate_C.html', 'slide_17_ultimate_C.png', CONTENT_C),
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
