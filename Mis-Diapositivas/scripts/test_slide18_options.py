# -*- coding: utf-8 -*-
import os
from playwright.sync_api import sync_playwright

output_dir = r"C:\Users\ASUS\.gemini\antigravity-ide\brain\a6624504-511c-4b9d-bc9a-468e348bde40"
os.makedirs(output_dir, exist_ok=True)

# ===========================================================================
# OPCIÓN A: Tríptico de 3 Pilares Verticales Limpios + Banner Aporte Inferior
# ===========================================================================
CONTENT_OPCION_A = '''
  <div class="slide-content-area" style="top: 175px; height: 720px; justify-content: space-between;">
    <h2 class="s-lead-question" style="font-size: 38px; font-weight: 800; margin: 0; line-height: 1.2; color: #2C0509;">
      Tres lecciones para la adopción real de tutores de IA en aulas desconectadas
    </h2>

    <div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 26px; flex: 1; margin-top: 16px; margin-bottom: 20px;">
      
      <!-- Pilar 1: Factibilidad Técnica -->
      <div style="background: #FAF5F5; border-top: 8px solid var(--c-wine-primary); padding: 28px 30px; display: flex; flex-direction: column; justify-content: space-between;">
        <div>
          <div style="font-family: var(--font-mono); font-size: 15px; font-weight: 800; color: var(--c-wine-primary); letter-spacing: 1.5px; margin-bottom: 6px;">
            01 · FACTIBILIDAD TÉCNICA
          </div>
          <div style="font-family: var(--font-sans); font-size: 32px; font-weight: 900; color: #110103; margin-bottom: 16px;">
            RAG en CPU Escolar
          </div>
          <div style="border-left: 3px solid var(--c-wine-primary); padding-left: 16px; margin-bottom: 18px;">
            <div style="font-family: var(--font-mono); font-size: 40px; font-weight: 900; color: var(--c-wine-primary); line-height: 1;">100% OFFLINE</div>
            <div style="font-family: var(--font-mono); font-size: 13px; font-weight: 800; color: #5D4A4D; margin-top: 4px; letter-spacing: 0.5px;">PORTABLE EN MEMORIA USB</div>
          </div>
          <div style="font-family: var(--font-sans); font-size: 24px; color: #222; line-height: 1.4; font-weight: 600;">
            Opera a <strong>1.9 tokens/s</strong> en Core i5 básico. Cierra de forma tangible la brecha tecnológica sin requerir GPU ni conexión a internet.
          </div>
        </div>
      </div>

      <!-- Pilar 2: Rigor Metodológico -->
      <div style="background: #FAF5F5; border-top: 8px solid #B38600; padding: 28px 30px; display: flex; flex-direction: column; justify-content: space-between;">
        <div>
          <div style="font-family: var(--font-mono); font-size: 15px; font-weight: 800; color: #8A6700; letter-spacing: 1.5px; margin-bottom: 6px;">
            02 · RIGOR METODOLÓGICO
          </div>
          <div style="font-family: var(--font-sans); font-size: 32px; font-weight: 900; color: #110103; margin-bottom: 16px;">
            Exigencia de Réplicas
          </div>
          <div style="border-left: 3px solid #B38600; padding-left: 16px; margin-bottom: 18px;">
            <div style="font-family: var(--font-mono); font-size: 40px; font-weight: 900; color: #B38600; line-height: 1;">≥ 4 SEMILLAS</div>
            <div style="font-family: var(--font-mono); font-size: 13px; font-weight: 800; color: #5D4A4D; margin-top: 4px; letter-spacing: 0.5px;">CONTROL DE VARIANZA SLM</div>
          </div>
          <div style="font-family: var(--font-sans); font-size: 24px; color: #222; line-height: 1.4; font-weight: 600;">
            Una corrida única carece de validez científica. La <strong>alta sensibilidad estocástica</strong> de los modelos compactos exige promediar múltiples ejecuciones.
          </div>
        </div>
      </div>

      <!-- Pilar 3: Soberanía Pedagógica -->
      <div style="background: #FAF5F5; border-top: 8px solid var(--c-red-accent); padding: 28px 30px; display: flex; flex-direction: column; justify-content: space-between;">
        <div>
          <div style="font-family: var(--font-mono); font-size: 15px; font-weight: 800; color: var(--c-red-accent); letter-spacing: 1.5px; margin-bottom: 6px;">
            03 · SOBERANÍA DOCENTE
          </div>
          <div style="font-family: var(--font-sans); font-size: 32px; font-weight: 900; color: #110103; margin-bottom: 16px;">
            Criterio Humano Central
          </div>
          <div style="border-left: 3px solid var(--c-red-accent); padding-left: 16px; margin-bottom: 18px;">
            <div style="font-family: var(--font-mono); font-size: 40px; font-weight: 900; color: var(--c-red-accent); line-height: 1;">κ = -0.429</div>
            <div style="font-family: var(--font-mono); font-size: 13px; font-weight: 800; color: #5D4A4D; margin-top: 4px; letter-spacing: 0.5px;">DESACUERDO INTER-EVALUADOR</div>
          </div>
          <div style="font-family: var(--font-sans); font-size: 24px; color: #222; line-height: 1.4; font-weight: 600;">
            Las métricas de similitud no miden pedagogía. El <strong>profesor de aula debe validar y calibrar</strong> los modelos antes de su uso real con estudiantes.
          </div>
        </div>
      </div>

    </div>

    <!-- Banner Aporte Principal -->
    <div style="background: #FAF5F5; border-left: 6px solid var(--c-red-accent); padding: 18px 28px; display: flex; align-items: center; gap: 16px;">
      <span style="font-family: var(--font-mono); font-size: 15px; font-weight: 900; color: var(--c-red-accent); letter-spacing: 1px; white-space: nowrap;">
        APORTE PRINCIPAL:
      </span>
      <span style="font-family: var(--font-sans); font-size: 25px; color: #110103; line-height: 1.35; font-weight: 600;">
        Demostrar que la IA generativa puede operar de forma <strong>autónoma en el aula rural desconectada</strong>, siempre que su despliegue esté subordinado al juicio docente.
      </span>
    </div>
  </div>
'''

# ===========================================================================
# OPCIÓN B: 3 Filas Horizontales Editoriales (Patrón Slide 2 Opción B)
# ===========================================================================
CONTENT_OPCION_B = '''
  <div class="slide-content-area" style="top: 175px; height: 720px; justify-content: space-between;">
    <h2 class="s-lead-question" style="font-size: 38px; font-weight: 800; margin: 0; line-height: 1.2; color: #2C0509;">
      Tres lecciones para la adopción real de tutores de IA en aulas desconectadas
    </h2>

    <div style="display: flex; flex-direction: column; gap: 18px; flex: 1; margin-top: 16px; margin-bottom: 16px;">
      
      <!-- Fila 1: Factibilidad Técnica -->
      <div style="background: #FAF5F5; border-left: 8px solid var(--c-wine-primary); padding: 22px 36px; display: grid; grid-template-columns: 260px 1fr; gap: 32px; align-items: center; flex: 1;">
        <div style="border-right: 2px solid #E2D2D2; padding-right: 24px; text-align: center;">
          <div style="font-family: var(--font-mono); font-size: 14px; font-weight: 800; color: var(--c-wine-primary); letter-spacing: 1.5px; margin-bottom: 2px;">
            01 · FACTIBILIDAD
          </div>
          <div style="font-family: var(--font-mono); font-size: 50px; font-weight: 900; color: var(--c-wine-primary); line-height: 1;">
            100%
          </div>
          <div style="font-family: var(--font-mono); font-size: 13px; font-weight: 800; color: #5D4A4D; margin-top: 4px; letter-spacing: 0.5px;">
            USB OFFLINE
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
      <div style="background: #FAF5F5; border-left: 8px solid #B38600; padding: 22px 36px; display: grid; grid-template-columns: 260px 1fr; gap: 32px; align-items: center; flex: 1;">
        <div style="border-right: 2px solid #E2D2D2; padding-right: 24px; text-align: center;">
          <div style="font-family: var(--font-mono); font-size: 14px; font-weight: 800; color: #8A6700; letter-spacing: 1.5px; margin-bottom: 2px;">
            02 · METODOLOGÍA
          </div>
          <div style="font-family: var(--font-mono); font-size: 50px; font-weight: 900; color: #B38600; line-height: 1;">
            ≥ 4
          </div>
          <div style="font-family: var(--font-mono); font-size: 13px; font-weight: 800; color: #5D4A4D; margin-top: 4px; letter-spacing: 0.5px;">
            RÉPLICAS SLM
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
      <div style="background: #FAF5F5; border-left: 8px solid var(--c-red-accent); padding: 22px 36px; display: grid; grid-template-columns: 260px 1fr; gap: 32px; align-items: center; flex: 1;">
        <div style="border-right: 2px solid #E2D2D2; padding-right: 24px; text-align: center;">
          <div style="font-family: var(--font-mono); font-size: 14px; font-weight: 800; color: var(--c-red-accent); letter-spacing: 1.5px; margin-bottom: 2px;">
            03 · PEDAGOGÍA
          </div>
          <div style="font-family: var(--font-mono); font-size: 46px; font-weight: 900; color: var(--c-red-accent); line-height: 1;">
            Humano
          </div>
          <div style="font-family: var(--font-mono); font-size: 13px; font-weight: 800; color: #5D4A4D; margin-top: 4px; letter-spacing: 0.5px;">
            CRITERIO DOCENTE
          </div>
        </div>
        <div>
          <div style="font-family: var(--font-sans); font-size: 30px; font-weight: 900; color: #110103; margin-bottom: 6px;">
            El Docente en el Centro del Diseño
          </div>
          <div style="font-family: var(--font-sans); font-size: 26px; color: #222; line-height: 1.35; font-weight: 600;">
            El desacuerdo inter-evaluador (<strong>κ = -0.429</strong>) demuestra que el algoritmo no juzga pedagogía; los profesores deben calibrar antes de desplegar.
          </div>
        </div>
      </div>

    </div>

    <!-- Banner Aporte Inferior -->
    <div style="background: #FAF5F5; border-left: 6px solid var(--c-wine-primary); padding: 16px 28px; display: flex; align-items: center; gap: 16px;">
      <span style="font-family: var(--font-mono); font-size: 15px; font-weight: 900; color: var(--c-wine-primary); letter-spacing: 1px; white-space: nowrap;">
        APORTE CENTRAL:
      </span>
      <span style="font-family: var(--font-sans); font-size: 24px; color: #110103; line-height: 1.35; font-weight: 600;">
        Democratizar la IA educativa en zonas desconectadas mediante software libre, sin transferir soberanía didáctica a los algoritmos.
      </span>
    </div>
  </div>
'''

# ===========================================================================
# OPCIÓN C: 3 Tarjetas con Hero Closing Box en Vino Profundo
# ===========================================================================
CONTENT_OPCION_C = '''
  <div class="slide-content-area" style="top: 175px; height: 720px; justify-content: space-between;">
    <h2 class="s-lead-question" style="font-size: 38px; font-weight: 800; margin: 0; line-height: 1.2; color: #2C0509;">
      Tres lecciones para la adopción real de tutores de IA en aulas desconectadas
    </h2>

    <div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 24px; flex: 1; margin-top: 16px; margin-bottom: 20px;">
      
      <!-- Card 1 -->
      <div style="background: #FAF5F5; border-top: 8px solid var(--c-wine-primary); padding: 26px 28px; display: flex; flex-direction: column; justify-content: space-between;">
        <div>
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px;">
            <span style="font-family: var(--font-mono); font-size: 15px; font-weight: 800; color: var(--c-wine-primary); letter-spacing: 1.5px;">
              01 · HARDWARE
            </span>
            <span style="font-family: var(--font-mono); font-size: 22px; font-weight: 900; color: var(--c-wine-primary); background: #F0E6E8; padding: 4px 10px; border-radius: 4px;">
              100% USB
            </span>
          </div>
          <div style="font-family: var(--font-sans); font-size: 30px; font-weight: 900; color: #110103; margin-bottom: 12px;">
            RAG en CPU Común
          </div>
          <div style="font-family: var(--font-sans); font-size: 24px; color: #222; line-height: 1.4; font-weight: 600;">
            Ejecución a <strong>1.9 tokens/s</strong> en computadores básicos de aula. Factible, autónomo y sin costos recurrentes de conectividad.
          </div>
        </div>
        <div style="border-top: 1.5px solid #E2D2D2; padding-top: 12px; font-family: var(--font-mono); font-size: 13px; font-weight: 800; color: #5D4A4D;">
          IMPACTO: CIERRE DE BRECHA RURAL
        </div>
      </div>

      <!-- Card 2 -->
      <div style="background: #FAF5F5; border-top: 8px solid #B38600; padding: 26px 28px; display: flex; flex-direction: column; justify-content: space-between;">
        <div>
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px;">
            <span style="font-family: var(--font-mono); font-size: 15px; font-weight: 800; color: #8A6700; letter-spacing: 1.5px;">
              02 · MÉTODO
            </span>
            <span style="font-family: var(--font-mono); font-size: 22px; font-weight: 900; color: #8A6700; background: #F8F1DA; padding: 4px 10px; border-radius: 4px;">
              ≥ 4 SEMILLAS
            </span>
          </div>
          <div style="font-family: var(--font-sans); font-size: 30px; font-weight: 900; color: #110103; margin-bottom: 12px;">
            Exigencia de Réplicas
          </div>
          <div style="font-family: var(--font-sans); font-size: 24px; color: #222; line-height: 1.4; font-weight: 600;">
            Una sola corrida induce a error científico. Evaluar SLMs exige <strong>promediar múltiples semillas</strong> para captar su variabilidad intrínseca.
          </div>
        </div>
        <div style="border-top: 1.5px solid #E2D2D2; padding-top: 12px; font-family: var(--font-mono); font-size: 13px; font-weight: 800; color: #5D4A4D;">
          IMPACTO: ESTÁNDAR CIENTÍFICO SLM
        </div>
      </div>

      <!-- Card 3 -->
      <div style="background: #FAF5F5; border-top: 8px solid var(--c-red-accent); padding: 26px 28px; display: flex; flex-direction: column; justify-content: space-between;">
        <div>
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px;">
            <span style="font-family: var(--font-mono); font-size: 15px; font-weight: 800; color: var(--c-red-accent); letter-spacing: 1.5px;">
              03 · DOCENCIA
            </span>
            <span style="font-family: var(--font-mono); font-size: 22px; font-weight: 900; color: var(--c-red-accent); background: #FDE8E8; padding: 4px 10px; border-radius: 4px;">
              κ = -0.429
            </span>
          </div>
          <div style="font-family: var(--font-sans); font-size: 30px; font-weight: 900; color: #110103; margin-bottom: 12px;">
            Criterio Docente Central
          </div>
          <div style="font-family: var(--font-sans); font-size: 24px; color: #222; line-height: 1.4; font-weight: 600;">
            Los puntajes de similitud premian la copia textual. La adopción pedagógica exige <strong>auditoría humana en contexto real de aula</strong>.
          </div>
        </div>
        <div style="border-top: 1.5px solid #E2D2D2; padding-top: 12px; font-family: var(--font-mono); font-size: 13px; font-weight: 800; color: #5D4A4D;">
          IMPACTO: SOBERANÍA DIDÁCTICA
        </div>
      </div>

    </div>

    <!-- Hero Dark Closing Banner -->
    <div style="background: #2C0509; border-left: 8px solid var(--c-gold); padding: 20px 32px; display: flex; align-items: center; justify-content: space-between; border-radius: 4px;">
      <div>
        <div style="font-family: var(--font-mono); font-size: 13px; font-weight: 800; color: var(--c-gold); letter-spacing: 1.5px; margin-bottom: 4px;">
          CONCLUSIÓN DEFINITIVA DE LA INVESTIGACIÓN
        </div>
        <div style="font-family: var(--font-sans); font-size: 26px; color: #FFFFFF; font-weight: 700; line-height: 1.3;">
          La tecnología portátil resuelve el acceso rural; el criterio docente garantiza el aprendizaje.
        </div>
      </div>
      <div style="font-family: var(--font-mono); font-size: 15px; font-weight: 800; color: rgba(255,255,255,0.7); text-align: right; padding-left: 28px; border-left: 1px solid rgba(255,255,255,0.2); white-space: nowrap;">
        VI CONGRESO<br>CARTAGENA 2026
      </div>
    </div>
  </div>
'''

HTML_PAGE = '''<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <title>Options Slide 18</title>
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
        ("slide18_opcion_a", CONTENT_OPCION_A),
        ("slide18_opcion_b", CONTENT_OPCION_B),
        ("slide18_opcion_c", CONTENT_OPCION_C),
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
