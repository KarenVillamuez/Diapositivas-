# -*- coding: utf-8 -*-
import os
from playwright.sync_api import sync_playwright

output_dir = r"C:\Users\ASUS\.gemini\antigravity-ide\brain\a6624504-511c-4b9d-bc9a-468e348bde40"
os.makedirs(output_dir, exist_ok=True)

# ===========================================================================
# OPCIÓN A: Tríptico de 3 Pilares Verticales (Editorial Proporcionado)
# ===========================================================================
CONTENT_OPCION_A = '''
  <div class="slide-content-area" style="top: 175px; height: 720px; justify-content: space-between;">
    <h2 class="s-lead-question" style="font-size: 38px; font-weight: 800; margin: 0; line-height: 1.2; color: #2C0509;">
      Tres lecciones para la adopción real de tutores de IA en aulas desconectadas
    </h2>

    <div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 26px; flex: 1; margin-top: 16px; margin-bottom: 20px;">
      
      <!-- Pilar 1: Factibilidad Técnica -->
      <div style="background: #FAF5F5; border-top: 8px solid var(--c-wine-primary); padding: 32px 30px; display: flex; flex-direction: column; justify-content: space-between;">
        <div>
          <div style="font-family: var(--font-mono); font-size: 15px; font-weight: 800; color: var(--c-wine-primary); letter-spacing: 1.5px; margin-bottom: 6px;">
            01 · FACTIBILIDAD TÉCNICA
          </div>
          <div style="font-family: var(--font-sans); font-size: 34px; font-weight: 900; color: #110103; margin-bottom: 18px;">
            RAG en CPU Escolar
          </div>
          <div style="font-family: var(--font-mono); font-size: 54px; font-weight: 900; color: var(--c-wine-primary); line-height: 1; margin-bottom: 6px;">
            100%
          </div>
          <div style="font-family: var(--font-mono); font-size: 13px; font-weight: 800; color: #5D4A4D; letter-spacing: 1px; margin-bottom: 20px;">
            PORTABLE EN USB SIN GPU
          </div>
          <div style="font-family: var(--font-sans); font-size: 25px; color: #110103; line-height: 1.38; font-weight: 600;">
            Genera <strong>1.9 tokens/s</strong> en un Core i5 común. Cierra de forma tangible la brecha tecnológica sin requerir internet ni costos de nube.
          </div>
        </div>
        <div style="border-top: 2px solid #E2D2D2; padding-top: 14px; font-family: var(--font-mono); font-size: 13px; font-weight: 800; color: var(--c-wine-primary); letter-spacing: 0.5px;">
          APORTE: DEMOCRATIZACIÓN OFFLINE
        </div>
      </div>

      <!-- Pilar 2: Rigor Metodológico -->
      <div style="background: #FAF5F5; border-top: 8px solid #B38600; padding: 32px 30px; display: flex; flex-direction: column; justify-content: space-between;">
        <div>
          <div style="font-family: var(--font-mono); font-size: 15px; font-weight: 800; color: #8A6700; letter-spacing: 1.5px; margin-bottom: 6px;">
            02 · RIGOR METODOLÓGICO
          </div>
          <div style="font-family: var(--font-sans); font-size: 34px; font-weight: 900; color: #110103; margin-bottom: 18px;">
            Exigencia de Réplicas
          </div>
          <div style="font-family: var(--font-mono); font-size: 54px; font-weight: 900; color: #B38600; line-height: 1; margin-bottom: 6px;">
            ≥ 4
          </div>
          <div style="font-family: var(--font-mono); font-size: 13px; font-weight: 800; color: #5D4A4D; letter-spacing: 1px; margin-bottom: 20px;">
            SEMILLAS ESTOCÁSTICAS
          </div>
          <div style="font-family: var(--font-sans); font-size: 25px; color: #110103; line-height: 1.38; font-weight: 600;">
            Una sola corrida carece de validez científica. La <strong>alta variabilidad de los SLM</strong> exige promediar múltiples ejecuciones.
          </div>
        </div>
        <div style="border-top: 2px solid #E2D2D2; padding-top: 14px; font-family: var(--font-mono); font-size: 13px; font-weight: 800; color: #8A6700; letter-spacing: 0.5px;">
          APORTE: NUEVO PROTOCOLO SLM
        </div>
      </div>

      <!-- Pilar 3: Soberanía Pedagógica -->
      <div style="background: #FAF5F5; border-top: 8px solid var(--c-red-accent); padding: 32px 30px; display: flex; flex-direction: column; justify-content: space-between;">
        <div>
          <div style="font-family: var(--font-mono); font-size: 15px; font-weight: 800; color: var(--c-red-accent); letter-spacing: 1.5px; margin-bottom: 6px;">
            03 · SOBERANÍA DOCENTE
          </div>
          <div style="font-family: var(--font-sans); font-size: 34px; font-weight: 900; color: #110103; margin-bottom: 18px;">
            Criterio Humano Central
          </div>
          <div style="font-family: var(--font-mono); font-size: 48px; font-weight: 900; color: var(--c-red-accent); line-height: 1; margin-bottom: 6px; letter-spacing: -1px;">
            κ = -0.429
          </div>
          <div style="font-family: var(--font-mono); font-size: 13px; font-weight: 800; color: #5D4A4D; letter-spacing: 1px; margin-bottom: 20px;">
            DESACUERDO INTER-DOCENTE
          </div>
          <div style="font-family: var(--font-sans); font-size: 25px; color: #110103; line-height: 1.38; font-weight: 600;">
            El algoritmo premia copiar, no aprender. El <strong>profesor de aula debe validar y calibrar</strong> los modelos antes de su despliegue real.
          </div>
        </div>
        <div style="border-top: 2px solid #E2D2D2; padding-top: 14px; font-family: var(--font-mono); font-size: 13px; font-weight: 800; color: var(--c-red-accent); letter-spacing: 0.5px;">
          APORTE: AUDITORÍA EN AULA
        </div>
      </div>

    </div>

    <!-- Banner Aporte Principal -->
    <div style="background: #FAF5F5; border-left: 6px solid var(--c-red-accent); padding: 18px 28px; display: flex; align-items: center; gap: 18px;">
      <span style="font-family: var(--font-mono); font-size: 15px; font-weight: 900; color: var(--c-red-accent); letter-spacing: 1px; white-space: nowrap;">
        TESIS DEFENDIDA:
      </span>
      <span style="font-family: var(--font-sans); font-size: 25px; color: #110103; line-height: 1.35; font-weight: 600;">
        La tecnología portátil resuelve la <strong>desconexión rural</strong>, pero solo el juicio pedagógico del docente garantiza una <strong>educación rigurosa</strong>.
      </span>
    </div>
  </div>
'''

# ===========================================================================
# OPCIÓN B: 3 Filas Horizontales con Banner Luminoso (Estilo Slide 2)
# ===========================================================================
CONTENT_OPCION_B = '''
  <div class="slide-content-area" style="top: 175px; height: 720px; justify-content: space-between;">
    <h2 class="s-lead-question" style="font-size: 38px; font-weight: 800; margin: 0; line-height: 1.2; color: #2C0509;">
      Tres lecciones para la adopción real de tutores de IA en aulas desconectadas
    </h2>

    <div style="display: flex; flex-direction: column; gap: 16px; flex: 1; margin-top: 16px; margin-bottom: 16px;">
      
      <!-- Fila 1: Factibilidad Técnica -->
      <div style="background: #FAF5F5; border-left: 8px solid var(--c-wine-primary); padding: 22px 36px; display: grid; grid-template-columns: 280px 1fr; gap: 32px; align-items: center; flex: 1;">
        <div style="border-right: 2px solid #E2D2D2; padding-right: 24px; text-align: center;">
          <div style="font-family: var(--font-mono); font-size: 14px; font-weight: 800; color: var(--c-wine-primary); letter-spacing: 1.5px; margin-bottom: 2px;">
            01 · FACTIBILIDAD
          </div>
          <div style="font-family: var(--font-mono); font-size: 52px; font-weight: 900; color: var(--c-wine-primary); line-height: 1;">
            100%
          </div>
          <div style="font-family: var(--font-mono); font-size: 13px; font-weight: 800; color: #5D4A4D; margin-top: 4px; letter-spacing: 0.5px;">
            USB OFFLINE SIN GPU
          </div>
        </div>
        <div>
          <div style="font-family: var(--font-sans); font-size: 30px; font-weight: 900; color: #110103; margin-bottom: 6px;">
            Hardware Escolar Común (CPU sin GPU)
          </div>
          <div style="font-family: var(--font-sans); font-size: 26px; color: #222; line-height: 1.35; font-weight: 600;">
            RAG portátil que genera <strong>1.9 tokens/s</strong> en un Core i5 de aula, cerrando la brecha rural sin requerir internet ni pagos en servidores cloud.
          </div>
        </div>
      </div>

      <!-- Fila 2: Rigor Metodológico -->
      <div style="background: #FAF5F5; border-left: 8px solid #B38600; padding: 22px 36px; display: grid; grid-template-columns: 280px 1fr; gap: 32px; align-items: center; flex: 1;">
        <div style="border-right: 2px solid #E2D2D2; padding-right: 24px; text-align: center;">
          <div style="font-family: var(--font-mono); font-size: 14px; font-weight: 800; color: #8A6700; letter-spacing: 1.5px; margin-bottom: 2px;">
            02 · METODOLOGÍA
          </div>
          <div style="font-family: var(--font-mono); font-size: 52px; font-weight: 900; color: #B38600; line-height: 1;">
            ≥ 4
          </div>
          <div style="font-family: var(--font-mono); font-size: 13px; font-weight: 800; color: #5D4A4D; margin-top: 4px; letter-spacing: 0.5px;">
            RÉPLICAS ESTOCÁSTICAS
          </div>
        </div>
        <div>
          <div style="font-family: var(--font-sans); font-size: 30px; font-weight: 900; color: #110103; margin-bottom: 6px;">
            Control de Variabilidad Estocástica
          </div>
          <div style="font-family: var(--font-sans); font-size: 26px; color: #222; line-height: 1.35; font-weight: 600;">
            Una sola corrida carece de validez científica. La <strong>alta dispersión de los SLM</strong> exige semillas múltiples como nuevo estándar de reproducibilidad.
          </div>
        </div>
      </div>

      <!-- Fila 3: Soberanía Pedagógica -->
      <div style="background: #FAF5F5; border-left: 8px solid var(--c-red-accent); padding: 22px 36px; display: grid; grid-template-columns: 280px 1fr; gap: 32px; align-items: center; flex: 1;">
        <div style="border-right: 2px solid #E2D2D2; padding-right: 24px; text-align: center;">
          <div style="font-family: var(--font-mono); font-size: 14px; font-weight: 800; color: var(--c-red-accent); letter-spacing: 1.5px; margin-bottom: 2px;">
            03 · DOCENCIA
          </div>
          <div style="font-family: var(--font-mono); font-size: 40px; font-weight: 900; color: var(--c-red-accent); line-height: 1; letter-spacing: -0.5px; white-space: nowrap;">
            κ = -0.429
          </div>
          <div style="font-family: var(--font-mono); font-size: 13px; font-weight: 800; color: #5D4A4D; margin-top: 4px; letter-spacing: 0.5px;">
            DESACUERDO EN AULA
          </div>
        </div>
        <div>
          <div style="font-family: var(--font-sans); font-size: 30px; font-weight: 900; color: #110103; margin-bottom: 6px;">
            El Docente en el Centro del Diseño
          </div>
          <div style="font-family: var(--font-sans); font-size: 26px; color: #222; line-height: 1.35; font-weight: 600;">
            El algoritmo mide apego textual, no pedagogía. La <strong>calibración por profesores en contexto real</strong> es insustituible para evitar falsedades.
          </div>
        </div>
      </div>

    </div>

    <!-- Banner Aporte Inferior -->
    <div style="background: #FAF5F5; border-left: 6px solid var(--c-wine-primary); padding: 16px 28px; display: flex; align-items: center; gap: 16px;">
      <span style="font-family: var(--font-mono); font-size: 15px; font-weight: 900; color: var(--c-wine-primary); letter-spacing: 1px; white-space: nowrap;">
        TESIS DEFENDIDA:
      </span>
      <span style="font-family: var(--font-sans); font-size: 24px; color: #110103; line-height: 1.35; font-weight: 600;">
        Democratizar la IA educativa en zonas desconectadas mediante hardware común, sin transferir jamás la soberanía pedagógica a los algoritmos.
      </span>
    </div>
  </div>
'''

# ===========================================================================
# OPCIÓN C: 3 Filas Horizontales con Gran Banner Hero Dark Institucional
# ===========================================================================
CONTENT_OPCION_C = '''
  <div class="slide-content-area" style="top: 175px; height: 720px; justify-content: space-between;">
    <h2 class="s-lead-question" style="font-size: 38px; font-weight: 800; margin: 0; line-height: 1.2; color: #2C0509;">
      Tres lecciones para la adopción real de tutores de IA en aulas desconectadas
    </h2>

    <div style="display: flex; flex-direction: column; gap: 14px; flex: 1; margin-top: 14px; margin-bottom: 16px;">
      
      <!-- Fila 1: Factibilidad Técnica -->
      <div style="background: #FAF5F5; border-left: 8px solid var(--c-wine-primary); padding: 18px 34px; display: grid; grid-template-columns: 280px 1fr; gap: 30px; align-items: center; flex: 1;">
        <div style="border-right: 2px solid #E2D2D2; padding-right: 20px; text-align: center;">
          <div style="font-family: var(--font-mono); font-size: 13px; font-weight: 800; color: var(--c-wine-primary); letter-spacing: 1.5px; margin-bottom: 2px;">
            01 · FACTIBILIDAD
          </div>
          <div style="font-family: var(--font-mono); font-size: 48px; font-weight: 900; color: var(--c-wine-primary); line-height: 1;">
            100%
          </div>
          <div style="font-family: var(--font-mono); font-size: 12px; font-weight: 800; color: #5D4A4D; margin-top: 2px; letter-spacing: 0.5px;">
            USB OFFLINE SIN GPU
          </div>
        </div>
        <div>
          <div style="font-family: var(--font-sans); font-size: 28px; font-weight: 900; color: #110103; margin-bottom: 4px;">
            Hardware Escolar Común (CPU sin GPU)
          </div>
          <div style="font-family: var(--font-sans); font-size: 25px; color: #222; line-height: 1.35; font-weight: 600;">
            RAG portátil que genera <strong>1.9 tokens/s</strong> en un Core i5 de aula, cerrando la brecha rural sin requerir internet ni pagos en la nube.
          </div>
        </div>
      </div>

      <!-- Fila 2: Rigor Metodológico -->
      <div style="background: #FAF5F5; border-left: 8px solid #B38600; padding: 18px 34px; display: grid; grid-template-columns: 280px 1fr; gap: 30px; align-items: center; flex: 1;">
        <div style="border-right: 2px solid #E2D2D2; padding-right: 20px; text-align: center;">
          <div style="font-family: var(--font-mono); font-size: 13px; font-weight: 800; color: #8A6700; letter-spacing: 1.5px; margin-bottom: 2px;">
            02 · METODOLOGÍA
          </div>
          <div style="font-family: var(--font-mono); font-size: 48px; font-weight: 900; color: #B38600; line-height: 1;">
            ≥ 4
          </div>
          <div style="font-family: var(--font-mono); font-size: 12px; font-weight: 800; color: #5D4A4D; margin-top: 2px; letter-spacing: 0.5px;">
            RÉPLICAS ESTOCÁSTICAS
          </div>
        </div>
        <div>
          <div style="font-family: var(--font-sans); font-size: 28px; font-weight: 900; color: #110103; margin-bottom: 4px;">
            Control de Variabilidad Estocástica
          </div>
          <div style="font-family: var(--font-sans); font-size: 25px; color: #222; line-height: 1.35; font-weight: 600;">
            Una sola corrida carece de validez científica. La <strong>alta dispersión de los SLM</strong> exige semillas múltiples como nuevo estándar.
          </div>
        </div>
      </div>

      <!-- Fila 3: Soberanía Pedagógica -->
      <div style="background: #FAF5F5; border-left: 8px solid var(--c-red-accent); padding: 18px 34px; display: grid; grid-template-columns: 280px 1fr; gap: 30px; align-items: center; flex: 1;">
        <div style="border-right: 2px solid #E2D2D2; padding-right: 20px; text-align: center;">
          <div style="font-family: var(--font-mono); font-size: 13px; font-weight: 800; color: var(--c-red-accent); letter-spacing: 1.5px; margin-bottom: 2px;">
            03 · DOCENCIA
          </div>
          <div style="font-family: var(--font-mono); font-size: 38px; font-weight: 900; color: var(--c-red-accent); line-height: 1; letter-spacing: -0.5px; white-space: nowrap;">
            κ = -0.429
          </div>
          <div style="font-family: var(--font-mono); font-size: 12px; font-weight: 800; color: #5D4A4D; margin-top: 2px; letter-spacing: 0.5px;">
            DESACUERDO EN AULA
          </div>
        </div>
        <div>
          <div style="font-family: var(--font-sans); font-size: 28px; font-weight: 900; color: #110103; margin-bottom: 4px;">
            El Docente en el Centro del Diseño
          </div>
          <div style="font-family: var(--font-sans); font-size: 25px; color: #222; line-height: 1.35; font-weight: 600;">
            El algoritmo mide apego textual, no pedagogía. La <strong>calibración por profesores en contexto real</strong> es insustituible.
          </div>
        </div>
      </div>

    </div>

    <!-- Hero Dark Banner Institucional -->
    <div style="background: #2C0509; border-left: 8px solid var(--c-gold); padding: 18px 32px; display: flex; align-items: center; justify-content: space-between; border-radius: 4px;">
      <div>
        <div style="font-family: var(--font-mono); font-size: 13px; font-weight: 800; color: var(--c-gold); letter-spacing: 1.5px; margin-bottom: 3px;">
          CONCLUSIÓN DEFINITIVA DE LA INVESTIGACIÓN
        </div>
        <div style="font-family: var(--font-sans); font-size: 25px; color: #FFFFFF; font-weight: 700; line-height: 1.3;">
          La tecnología portátil resuelve el acceso rural; el criterio docente garantiza el aprendizaje.
        </div>
      </div>
      <div style="font-family: var(--font-mono); font-size: 14px; font-weight: 800; color: rgba(255,255,255,0.7); text-align: right; padding-left: 24px; border-left: 1px solid rgba(255,255,255,0.2); white-space: nowrap;">
        VI CONGRESO<br>CARTAGENA 2026
      </div>
    </div>
  </div>
'''

HTML_PAGE = '''<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <title>Slide 18 Perfected Options</title>
  <link rel="stylesheet" href="http://localhost:8085/styles.css?v=33">
</head>
<body style="margin: 0; padding: 0; background: #0b0103;">
  <div id="presentation-viewport">
    <div id="slides-stage">
      <section class="slide s-white active">
        <header class="slide-header">
          <div class="sh-left">
            <span class="sh-red-bar"></span>
            <span class="sh-category">04 · CONCLUSIONES Y APORTES</span>
          </div>
          <img src="http://localhost:8085/assets/image6.png" alt="#LoxTIC" class="sh-loxtic">
        </header>
        <div class="sh-divider"></div>
        {content}
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
        ("slide18_final_a_triptico", CONTENT_OPCION_A),
        ("slide18_final_b_filas", CONTENT_OPCION_B),
        ("slide18_final_c_darkbanner", CONTENT_OPCION_C),
    ]

    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(viewport={"width": 1920, "height": 1080})

        for name, content in options:
            html = HTML_PAGE.format(content=content)
            tmp_html = os.path.join(output_dir, f"{name}.html")
            tmp_png = os.path.join(output_dir, f"{name}.png")
            with open(tmp_html, "w", encoding="utf-8") as f:
                f.write(html)
            page.goto(f"file:///{tmp_html.replace(os.sep, '/')}")
            page.wait_for_timeout(400)
            page.screenshot(path=tmp_png)
            print(f"Generated {name}.png")

        browser.close()

if __name__ == '__main__':
    main()
