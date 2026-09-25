# -*- coding: utf-8 -*-
import os
from playwright.sync_api import sync_playwright

output_dir = r"C:\Users\ASUS\.gemini\antigravity-ide\brain\a6624504-511c-4b9d-bc9a-468e348bde40"
os.makedirs(output_dir, exist_ok=True)

# ===========================================================================
# OPCIÓN A: Díptico Vertical Equilibrado (2 Columnas Robustas de Altura Completa)
# ===========================================================================
CONTENT_A = '''
    <h2 class="s-lead-question" style="font-size: 38px; font-weight: 800; margin: 0; line-height: 1.2; color: #2C0509;">
      Apego al material fuente no es aprendizaje: guía para auditar y desplegar tutores
    </h2>

    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 36px; flex: 1; align-items: stretch; margin-top: 10px;">
      
      <!-- COLUMNA 1: LA FALACIA METODOLÓGICA -->
      <div style="background: #FAF5F5; border-top: 8px solid var(--c-red-accent); padding: 32px 36px; display: flex; flex-direction: column; justify-content: space-between;">
        <div>
          <div style="font-family: var(--font-mono); font-size: 19px; font-weight: 800; color: var(--c-red-accent); letter-spacing: 1.5px; margin-bottom: 8px;">
            01 · ADVERTENCIA METODOLÓGICA
          </div>
          <h3 style="font-family: var(--font-sans); font-size: 34px; font-weight: 800; color: #110103; margin-bottom: 24px;">
            La Falacia de la Nota Agregada
          </h3>

          <div style="display: flex; flex-direction: column; gap: 20px;">
            <div style="display: flex; gap: 16px; align-items: flex-start;">
              <div style="width: 10px; height: 10px; border-radius: 50%; background: var(--c-red-accent); margin-top: 10px; flex-shrink: 0;"></div>
              <div>
                <div style="font-family: var(--font-sans); font-size: 24px; font-weight: 800; color: #110103;">
                  Apego textual &ne; Calidad pedagógica
                </div>
                <div style="font-family: var(--font-sans); font-size: 21px; color: #5D4A4D; line-height: 1.4; margin-top: 4px;">
                  El indicador mide cercanía literal con el libro de texto, no comprensión ni desarrollo cognitivo del estudiante.
                </div>
              </div>
            </div>

            <div style="display: flex; gap: 16px; align-items: flex-start;">
              <div style="width: 10px; height: 10px; border-radius: 50%; background: var(--c-red-accent); margin-top: 10px; flex-shrink: 0;"></div>
              <div>
                <div style="font-family: var(--font-sans); font-size: 24px; font-weight: 800; color: #110103;">
                  Efecto de enmascaramiento
                </div>
                <div style="font-family: var(--font-sans); font-size: 21px; color: #5D4A4D; line-height: 1.4; margin-top: 4px;">
                  Respuestas evasivas superan 0.70 por inercia matemática, ocultando alucinaciones y sesgos graves.
                </div>
              </div>
            </div>

            <div style="display: flex; gap: 16px; align-items: flex-start;">
              <div style="width: 10px; height: 10px; border-radius: 50%; background: var(--c-red-accent); margin-top: 10px; flex-shrink: 0;"></div>
              <div>
                <div style="font-family: var(--font-sans); font-size: 24px; font-weight: 800; color: #110103;">
                  Auditoría por componentes
                </div>
                <div style="font-family: var(--font-sans); font-size: 21px; color: #5D4A4D; line-height: 1.4; margin-top: 4px;">
                  Obligatorio desglosar recuperación (relevance), respuesta (grounding) y tasa de rechazo por separado.
                </div>
              </div>
            </div>
          </div>
        </div>

        <!-- Regla de oro al pie -->
        <div style="border-top: 2px solid #EAE0E1; padding-top: 18px; margin-top: 24px; display: flex; align-items: baseline; gap: 10px;">
          <span style="font-family: var(--font-mono); font-size: 19px; font-weight: 800; color: var(--c-red-accent); white-space: nowrap;">REGLA DE ORO:</span>
          <span style="font-family: var(--font-sans); font-size: 21px; font-weight: 700; color: #110103;">
            Prohibido certificar tutores de IA mediante un único promedio cuantitativo global.
          </span>
        </div>
      </div>

      <!-- COLUMNA 2: MATRIZ DE DECISIÓN SEGÚN RIESGO -->
      <div style="background: #FAF5F5; border-top: 8px solid var(--c-wine-primary); padding: 32px 36px; display: flex; flex-direction: column; justify-content: space-between;">
        <div>
          <div style="display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 8px;">
            <span style="font-family: var(--font-mono); font-size: 19px; font-weight: 800; color: var(--c-wine-primary); letter-spacing: 1.5px;">
              02 · MATRIZ SEGÚN RIESGO
            </span>
            <span style="font-family: var(--font-mono); font-size: 18px; font-weight: 700; color: #B38600;">
              Contexto > Benchmark
            </span>
          </div>
          <h3 style="font-family: var(--font-sans); font-size: 34px; font-weight: 800; color: #110103; margin-bottom: 24px;">
            ¿Cuál Modelo Desplegar?
          </h3>

          <div style="display: flex; flex-direction: column; gap: 24px;">
            
            <!-- Perfil Qwen -->
            <div style="background: #FFFFFF; border-left: 8px solid var(--c-wine-primary); padding: 20px 24px;">
              <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 6px;">
                <span style="font-family: var(--font-sans); font-size: 24px; font-weight: 800; color: var(--c-wine-primary);">
                  Qwen2.5-3B · Autoestudio Autónomo
                </span>
                <span style="font-family: var(--font-mono); font-size: 18px; font-weight: 800; color: var(--c-wine-primary); background: #FAF5F5; padding: 4px 10px;">
                  85.7% Rechazo
                </span>
              </div>
              <div style="font-family: var(--font-sans); font-size: 21px; color: #5D4A4D; line-height: 1.4;">
                <strong>Sin docente en sala:</strong> Prima la certeza. Es preferible que el tutor declare no saber antes que inducir al alumno a un error conceptual no supervisado.
              </div>
            </div>

            <!-- Perfil Phi -->
            <div style="background: #FFFFFF; border-left: 8px solid var(--c-red-accent); padding: 20px 24px;">
              <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 6px;">
                <span style="font-family: var(--font-sans); font-size: 24px; font-weight: 800; color: var(--c-red-accent);">
                  Phi-4-mini · Aula Asistida con Docente
                </span>
                <span style="font-family: var(--font-mono); font-size: 18px; font-weight: 800; color: var(--c-red-accent); background: #FAF5F5; padding: 4px 10px;">
                  0.0% Bloqueos
                </span>
              </div>
              <div style="font-family: var(--font-sans); font-size: 21px; color: #5D4A4D; line-height: 1.4;">
                <strong>Con docente en sala:</strong> Prima la fluidez. El tutor jamás frena la dinámica del grupo y el profesor está presente para corregir cualquier alucinación.
              </div>
            </div>

          </div>
        </div>

        <!-- Criterio final al pie -->
        <div style="border-top: 2px solid #EAE0E1; padding-top: 18px; margin-top: 24px; display: flex; align-items: baseline; gap: 10px;">
          <span style="font-family: var(--font-mono); font-size: 19px; font-weight: 800; color: var(--c-wine-primary); white-space: nowrap;">CONCLUSIÓN:</span>
          <span style="font-family: var(--font-sans); font-size: 21px; font-weight: 700; color: #110103;">
            El modelo no se elige por puntaje sintético, sino por la presencia o ausencia de supervisión humana.
          </span>
        </div>
      </div>

    </div>
'''

# ===========================================================================
# OPCIÓN B: Arquitectura Modular Horizontal (Banner Superior + Matriz Inferior)
# ===========================================================================
CONTENT_B = '''
    <h2 class="s-lead-question" style="font-size: 38px; font-weight: 800; margin: 0; line-height: 1.2; color: #2C0509;">
      Apego al material fuente no es aprendizaje: guía para auditar y desplegar tutores
    </h2>

    <div style="display: flex; flex-direction: column; justify-content: space-between; flex: 1; margin-top: 10px; gap: 20px;">
      
      <!-- BANNER SUPERIOR: LA FALACIA DE LA NOTA AGREGADA (Franja panorámica en 3 columnas) -->
      <div style="background: #FAF5F5; border-left: 10px solid var(--c-red-accent); padding: 22px 28px;">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 14px;">
          <span style="font-family: var(--font-mono); font-size: 19px; font-weight: 800; color: var(--c-red-accent); letter-spacing: 1.5px;">
            ADVERTENCIA METODOLÓGICA · LA FALACIA DE LA NOTA AGREGADA
          </span>
          <span style="font-family: var(--font-mono); font-size: 18px; font-weight: 700; color: #110103;">
            Índice 0.795 &ne; Calidad Real
          </span>
        </div>

        <div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 24px;">
          <div style="border-right: 1.5px solid #EAE0E1; padding-right: 20px;">
            <div style="font-family: var(--font-sans); font-size: 22px; font-weight: 800; color: #110103;">
              Apego &ne; Comprensión
            </div>
            <div style="font-family: var(--font-sans); font-size: 19px; color: #5D4A4D; margin-top: 4px; line-height: 1.35;">
              Mide similitud léxica con el libro, no ganancia pedagógica del alumno.
            </div>
          </div>

          <div style="border-right: 1.5px solid #EAE0E1; padding-right: 20px;">
            <div style="font-family: var(--font-sans); font-size: 22px; font-weight: 800; color: #110103;">
              Enmascaramiento
            </div>
            <div style="font-family: var(--font-sans); font-size: 19px; color: #5D4A4D; margin-top: 4px; line-height: 1.35;">
              Respuestas vacías superan 0.70, ocultando riesgos conceptuales.
            </div>
          </div>

          <div>
            <div style="font-family: var(--font-sans); font-size: 22px; font-weight: 800; color: #110103;">
              Auditoría Separada
            </div>
            <div style="font-family: var(--font-sans); font-size: 19px; color: #5D4A4D; margin-top: 4px; line-height: 1.35;">
              Obligatorio desglosar relevancia, grounding y tasa de rechazo.
            </div>
          </div>
        </div>
      </div>

      <!-- PARTE INFERIOR: MATRIZ DE ELECCIÓN EN 2 BLOQUES HERO -->
      <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 24px; flex: 1;">
        
        <!-- Bloque Qwen -->
        <div style="background: #FAF5F5; border-left: 10px solid var(--c-wine-primary); padding: 24px 28px; display: flex; flex-direction: column; justify-content: space-between;">
          <div>
            <div style="display: flex; justify-content: space-between; align-items: baseline;">
              <span style="font-family: var(--font-sans); font-size: 28px; font-weight: 800; color: var(--c-wine-primary);">
                Qwen2.5-3B
              </span>
              <span style="font-family: var(--font-mono); font-size: 22px; font-weight: 900; color: var(--c-wine-primary);">
                85.7% Rechazo
              </span>
            </div>
            <div style="font-family: var(--font-sans); font-size: 24px; font-weight: 800; color: #110103; margin-top: 6px;">
              Entorno: Autoestudio Autónomo
            </div>
            <div style="font-family: var(--font-sans); font-size: 21px; color: #5D4A4D; line-height: 1.45; margin-top: 10px;">
              Cuando el alumno trabaja solo en casa o biblioteca rural sin tutor. Prima la <strong>certeza absoluta</strong>: preferible admitir desconocimiento antes que alucinar.
            </div>
          </div>
          <div style="font-family: var(--font-mono); font-size: 18px; font-weight: 700; color: var(--c-wine-primary); margin-top: 14px;">
            &bull; Perfil: Prudente / Cautela máxima
          </div>
        </div>

        <!-- Bloque Phi -->
        <div style="background: #FAF5F5; border-left: 10px solid var(--c-red-accent); padding: 24px 28px; display: flex; flex-direction: column; justify-content: space-between;">
          <div>
            <div style="display: flex; justify-content: space-between; align-items: baseline;">
              <span style="font-family: var(--font-sans); font-size: 28px; font-weight: 800; color: var(--c-red-accent);">
                Phi-4-mini
              </span>
              <span style="font-family: var(--font-mono); font-size: 22px; font-weight: 900; color: var(--c-red-accent);">
                0.0% Bloqueos
              </span>
            </div>
            <div style="font-family: var(--font-sans); font-size: 24px; font-weight: 800; color: #110103; margin-top: 6px;">
              Entorno: Aula Asistida con Docente
            </div>
            <div style="font-family: var(--font-sans); font-size: 21px; color: #5D4A4D; line-height: 1.45; margin-top: 10px;">
              Cuando hay profesor en sala guiando la clase. Prima la <strong>fluidez y dinamismo</strong>: el modelo nunca se detiene y el docente supervisa y corrige desvíos.
            </div>
          </div>
          <div style="font-family: var(--font-mono); font-size: 18px; font-weight: 700; color: var(--c-red-accent); margin-top: 14px;">
            &bull; Perfil: Fluido / Requiere supervisión activa
          </div>
        </div>

      </div>

      <!-- REMATE EDITORIAL INFERIOR TIPO P2 -->
      <div style="background: #FAF5F5; border-top: 3.5px solid var(--c-wine-primary); border-bottom: 3.5px solid var(--c-wine-primary); padding: 12px 24px; display: flex; justify-content: space-between; align-items: center;">
        <span style="font-family: var(--font-sans); font-size: 22px; font-weight: 700; color: #110103;">
          <strong style="color: var(--c-wine-primary);">Directriz metodológica:</strong> El entorno escolar y la presencia docente definen el modelo, no el puntaje del benchmark.
        </span>
        <span style="font-family: var(--font-mono); font-size: 18px; font-weight: 700; color: #5D4A4D;">
          Discusión del paper
        </span>
      </div>

    </div>
'''

# ===========================================================================
# OPCION C: Enfoque Editorial Minimalista (Listado Limpio con Micro-Métricas)
# ===========================================================================
CONTENT_C = '''
    <h2 class="s-lead-question" style="font-size: 38px; font-weight: 800; margin: 0; line-height: 1.2; color: #2C0509;">
      Apego al material fuente no es aprendizaje: guía para auditar y desplegar tutores
    </h2>

    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 40px; flex: 1; align-items: stretch; margin-top: 10px;">
      
      <!-- COLUMNA 1: AUDITORÍA Y FALACIA -->
      <div style="display: flex; flex-direction: column; justify-content: space-between; padding: 10px 0;">
        <div>
          <div style="border-bottom: 2px solid var(--c-red-accent); padding-bottom: 8px; margin-bottom: 20px;">
            <span style="font-family: var(--font-mono); font-size: 20px; font-weight: 800; color: var(--c-red-accent); letter-spacing: 1.5px;">
              01 · ADVERTENCIA METODOLÓGICA
            </span>
          </div>
          <h3 style="font-family: var(--font-sans); font-size: 36px; font-weight: 800; color: #110103; margin-bottom: 20px;">
            La Falacia de la Nota Agregada
          </h3>

          <div style="display: flex; flex-direction: column; gap: 24px;">
            <div style="background: #FAF5F5; border-left: 8px solid var(--c-red-accent); padding: 18px 22px;">
              <div style="font-family: var(--font-sans); font-size: 23px; font-weight: 800; color: #110103;">
                Apego &ne; Aprendizaje
              </div>
              <div style="font-family: var(--font-sans); font-size: 20px; color: #5D4A4D; margin-top: 4px; line-height: 1.4;">
                Mide coincidencia con el libro fuente, no apropiación pedagógica.
              </div>
            </div>

            <div style="background: #FAF5F5; border-left: 8px solid var(--c-red-accent); padding: 18px 22px;">
              <div style="font-family: var(--font-sans); font-size: 23px; font-weight: 800; color: #110103;">
                Enmascaramiento Cuantitativo
              </div>
              <div style="font-family: var(--font-sans); font-size: 20px; color: #5D4A4D; margin-top: 4px; line-height: 1.4;">
                Respuestas vacías logran 0.70 por longitud y cosine similarity.
              </div>
            </div>

            <div style="background: #FAF5F5; border-left: 8px solid var(--c-red-accent); padding: 18px 22px;">
              <div style="font-family: var(--font-sans); font-size: 23px; font-weight: 800; color: #110103;">
                Auditoría Desglosada
              </div>
              <div style="font-family: var(--font-sans); font-size: 20px; color: #5D4A4D; margin-top: 4px; line-height: 1.4;">
                Evaluar obligatoriamente grounding, relevance y rechazos por separado.
              </div>
            </div>
          </div>
        </div>

        <div style="font-family: var(--font-sans); font-size: 20px; font-weight: 700; color: var(--c-red-accent); border-top: 1.5px solid #EAE0E1; padding-top: 14px;">
          Regla: Prohibido calificar tutores con un único promedio cuantitativo global.
        </div>
      </div>

      <!-- COLUMNA 2: MATRIZ DE ELECCIÓN -->
      <div style="display: flex; flex-direction: column; justify-content: space-between; padding: 10px 0;">
        <div>
          <div style="border-bottom: 2px solid var(--c-wine-primary); padding-bottom: 8px; margin-bottom: 20px;">
            <span style="font-family: var(--font-mono); font-size: 20px; font-weight: 800; color: var(--c-wine-primary); letter-spacing: 1.5px;">
              02 · MATRIZ SEGÚN RIESGO
            </span>
          </div>
          <h3 style="font-family: var(--font-sans); font-size: 36px; font-weight: 800; color: #110103; margin-bottom: 20px;">
            ¿Cuál Modelo Desplegar?
          </h3>

          <div style="display: flex; flex-direction: column; gap: 24px;">
            <div style="background: #FAF5F5; border-left: 8px solid var(--c-wine-primary); padding: 22px 24px;">
              <div style="display: flex; justify-content: space-between; align-items: baseline;">
                <span style="font-family: var(--font-sans); font-size: 25px; font-weight: 800; color: var(--c-wine-primary);">
                  Qwen2.5-3B
                </span>
                <span style="font-family: var(--font-mono); font-size: 20px; font-weight: 800; color: var(--c-wine-primary);">
                  Autoestudio Autónomo
                </span>
              </div>
              <div style="font-family: var(--font-sans); font-size: 21px; color: #5D4A4D; margin-top: 8px; line-height: 1.4;">
                <strong>85.7% de rechazo certero:</strong> Preferible no responder antes que alucinar. Ideal cuando el estudiante trabaja sin docente.
              </div>
            </div>

            <div style="background: #FAF5F5; border-left: 8px solid var(--c-red-accent); padding: 22px 24px;">
              <div style="display: flex; justify-content: space-between; align-items: baseline;">
                <span style="font-family: var(--font-sans); font-size: 25px; font-weight: 800; color: var(--c-red-accent);">
                  Phi-4-mini
                </span>
                <span style="font-family: var(--font-mono); font-size: 20px; font-weight: 800; color: var(--c-red-accent);">
                  Aula con Docente
                </span>
              </div>
              <div style="font-family: var(--font-sans); font-size: 21px; color: #5D4A4D; margin-top: 8px; line-height: 1.4;">
                <strong>0.0% de bloqueos (fluidez total):</strong> Nunca frena la sesión escolar. El profesor supervisa y corrige desviaciones conceptuales.
              </div>
            </div>
          </div>
        </div>

        <div style="font-family: var(--font-sans); font-size: 20px; font-weight: 700; color: var(--c-wine-primary); border-top: 1.5px solid #EAE0E1; padding-top: 14px;">
          Criterio: El entorno pedagógico define el modelo, no el puntaje del benchmark.
        </div>
      </div>

    </div>
'''

HTML_TEMPLATE = '''<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Test Slide 17 Options</title>
  <link rel="stylesheet" href="http://localhost:8085/styles.css?v=30">
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
        ('slide_17_opt_A.html', 'slide_17_opt_A.png', CONTENT_A),
        ('slide_17_opt_B.html', 'slide_17_opt_B.png', CONTENT_B),
        ('slide_17_opt_C.html', 'slide_17_opt_C.png', CONTENT_C),
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
