# -*- coding: utf-8 -*-
import os
from playwright.sync_api import sync_playwright

output_dir = r"C:\Users\ASUS\.gemini\antigravity-ide\brain\a6624504-511c-4b9d-bc9a-468e348bde40"
os.makedirs(output_dir, exist_ok=True)

# ===========================================================================
# OPCIÓN D1: Díptico Vertical Flat Continuo (CERO cajas anidadas)
# ===========================================================================
CONTENT_D1 = '''
    <h2 class="s-lead-question" style="font-size: 38px; font-weight: 800; margin: 0; line-height: 1.2; color: #2C0509;">
      Apego al material fuente no es aprendizaje: guía para auditar y desplegar tutores
    </h2>

    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 36px; flex: 1; align-items: stretch; margin-top: 10px;">
      
      <!-- COLUMNA 1: ADVERTENCIA METODOLÓGICA (Bloque continuo sin cajas internas) -->
      <div style="background: #FAF5F5; border-top: 8px solid var(--c-red-accent); padding: 32px 36px; display: flex; flex-direction: column; justify-content: space-between;">
        <div>
          <div style="font-family: var(--font-mono); font-size: 19px; font-weight: 800; color: var(--c-red-accent); letter-spacing: 1.5px; margin-bottom: 8px;">
            01 · ADVERTENCIA METODOLÓGICA
          </div>
          <h3 style="font-family: var(--font-sans); font-size: 34px; font-weight: 800; color: #110103; margin-bottom: 24px;">
            La Falacia de la Nota Agregada
          </h3>

          <div style="display: flex; flex-direction: column; gap: 22px;">
            <div style="display: flex; gap: 16px; align-items: flex-start;">
              <div style="width: 10px; height: 10px; border-radius: 50%; background: var(--c-red-accent); margin-top: 10px; flex-shrink: 0;"></div>
              <div>
                <div style="font-family: var(--font-sans); font-size: 24px; font-weight: 800; color: #110103;">
                  Apego textual &ne; Calidad pedagógica
                </div>
                <div style="font-family: var(--font-sans); font-size: 21px; color: #5D4A4D; line-height: 1.4; margin-top: 4px;">
                  El benchmark mide similitud léxica con el libro fuente, no comprensión ni apropiación del estudiante.
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
                  Respuestas vacías o evasivas superan 0.70 por longitud y coseno, ocultando riesgos graves.
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
                  Obligatorio desglosar relevancia, grounding y tasa de rechazo por separado.
                </div>
              </div>
            </div>
          </div>
        </div>

        <!-- Regla de oro al pie -->
        <div style="border-top: 2px solid #EAE0E1; padding-top: 18px; margin-top: 24px; display: flex; align-items: baseline; gap: 10px;">
          <span style="font-family: var(--font-mono); font-size: 19px; font-weight: 800; color: var(--c-red-accent); white-space: nowrap;">REGLA DE ORO:</span>
          <span style="font-family: var(--font-sans); font-size: 21px; font-weight: 700; color: #110103;">
            Prohibido certificar tutores de IA con un único promedio cuantitativo global.
          </span>
        </div>
      </div>

      <!-- COLUMNA 2: MATRIZ DE DECISIÓN (Totalmente abierta, sin cajetines blancos) -->
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
            
            <!-- Perfil Qwen (Abierto, con barra lateral y sin recuadro interno) -->
            <div style="border-left: 6px solid var(--c-wine-primary); padding-left: 20px;">
              <div style="display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 6px;">
                <span style="font-family: var(--font-sans); font-size: 25px; font-weight: 800; color: var(--c-wine-primary);">
                  Qwen2.5-3B &rarr; Autoestudio Autónomo
                </span>
                <span style="font-family: var(--font-mono); font-size: 19px; font-weight: 900; color: var(--c-wine-primary);">
                  85.7% Rechazo
                </span>
              </div>
              <div style="font-family: var(--font-sans); font-size: 21px; color: #5D4A4D; line-height: 1.45;">
                <strong>Sin docente en sala:</strong> Prima la certeza. Es preferible que el tutor declare no saber antes que inducir al alumno a un error conceptual no supervisado.
              </div>
            </div>

            <!-- Divisor limpio entre modelos -->
            <div style="width: 100%; height: 1.5px; background: #EAE0E1;"></div>

            <!-- Perfil Phi (Abierto, con barra lateral y sin recuadro interno) -->
            <div style="border-left: 6px solid var(--c-red-accent); padding-left: 20px;">
              <div style="display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 6px;">
                <span style="font-family: var(--font-sans); font-size: 25px; font-weight: 800; color: var(--c-red-accent);">
                  Phi-4-mini &rarr; Aula con Docente
                </span>
                <span style="font-family: var(--font-mono); font-size: 19px; font-weight: 900; color: var(--c-red-accent);">
                  0.0% Bloqueos
                </span>
              </div>
              <div style="font-family: var(--font-sans); font-size: 21px; color: #5D4A4D; line-height: 1.45;">
                <strong>Con docente en sala:</strong> Prima la fluidez. El tutor dinamiza la sesión sin frenos y el profesor está presente para corregir cualquier desvío en tiempo real.
              </div>
            </div>

          </div>
        </div>

        <!-- Criterio final al pie -->
        <div style="border-top: 2px solid #EAE0E1; padding-top: 18px; margin-top: 24px; display: flex; align-items: baseline; gap: 10px;">
          <span style="font-family: var(--font-mono); font-size: 19px; font-weight: 800; color: var(--c-wine-primary); white-space: nowrap;">CONCLUSIÓN:</span>
          <span style="font-family: var(--font-sans); font-size: 21px; font-weight: 700; color: #110103;">
            El entorno escolar y la presencia docente definen el modelo, no el benchmark.
          </span>
        </div>
      </div>

    </div>
'''

# ===========================================================================
# OPCIÓN D2: Díptico Panorámico Horizontal (16:9 con Franja Editorial P2)
# ===========================================================================
CONTENT_D2 = '''
    <h2 class="s-lead-question" style="font-size: 38px; font-weight: 800; margin: 0; line-height: 1.2; color: #2C0509;">
      Apego al material fuente no es aprendizaje: guía para auditar y desplegar tutores
    </h2>

    <div style="display: flex; flex-direction: column; justify-content: space-between; flex: 1; margin-top: 10px; gap: 20px;">
      
      <!-- FILA SUPERIOR: LA FALACIA DE LA NOTA AGREGADA (Franja en 3 columnas) -->
      <div style="background: #FAF5F5; border-left: 10px solid var(--c-red-accent); padding: 22px 28px;">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 14px;">
          <span style="font-family: var(--font-mono); font-size: 19px; font-weight: 800; color: var(--c-red-accent); letter-spacing: 1.5px;">
            01 · ADVERTENCIA METODOLÓGICA · LA FALACIA DE LA NOTA AGREGADA
          </span>
          <span style="font-family: var(--font-mono); font-size: 18px; font-weight: 700; color: #110103;">
            Índice 0.795 &ne; Calidad Real
          </span>
        </div>

        <div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 28px;">
          <div style="border-right: 1.5px solid #EAE0E1; padding-right: 20px;">
            <div style="font-family: var(--font-sans); font-size: 22px; font-weight: 800; color: #110103;">
              Apego &ne; Aprendizaje
            </div>
            <div style="font-family: var(--font-sans); font-size: 19px; color: #5D4A4D; margin-top: 4px; line-height: 1.35;">
              Mide similitud léxica con el libro fuente, no ganancia cognitiva real del alumno.
            </div>
          </div>

          <div style="border-right: 1.5px solid #EAE0E1; padding-right: 20px;">
            <div style="font-family: var(--font-sans); font-size: 22px; font-weight: 800; color: #110103;">
              Enmascaramiento
            </div>
            <div style="font-family: var(--font-sans); font-size: 19px; color: #5D4A4D; margin-top: 4px; line-height: 1.35;">
              Respuestas vacías logran 0.70 por coseno y longitud, ocultando alucinaciones.
            </div>
          </div>

          <div>
            <div style="font-family: var(--font-sans); font-size: 22px; font-weight: 800; color: #110103;">
              Auditoría Separada
            </div>
            <div style="font-family: var(--font-sans); font-size: 19px; color: #5D4A4D; margin-top: 4px; line-height: 1.35;">
              Obligatorio desglosar relevancia, grounding y tasa de rechazo por separado.
            </div>
          </div>
        </div>
      </div>

      <!-- FILA MEDIA: MATRIZ DE ELECCIÓN SEGÚN ENTORNO -->
      <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 24px; flex: 1;">
        
        <!-- Bloque Qwen -->
        <div style="background: #FAF5F5; border-left: 10px solid var(--c-wine-primary); padding: 24px 28px; display: flex; flex-direction: column; justify-content: space-between;">
          <div>
            <div style="display: flex; justify-content: space-between; align-items: baseline;">
              <span style="font-family: var(--font-sans); font-size: 26px; font-weight: 800; color: var(--c-wine-primary);">
                Qwen2.5-3B
              </span>
              <span style="font-family: var(--font-mono); font-size: 22px; font-weight: 900; color: var(--c-wine-primary);">
                85.7% Rechazo
              </span>
            </div>
            <div style="font-family: var(--font-sans); font-size: 23px; font-weight: 800; color: #110103; margin-top: 6px;">
              Entorno: Autoestudio Autónomo
            </div>
            <div style="font-family: var(--font-sans); font-size: 21px; color: #5D4A4D; line-height: 1.45; margin-top: 10px;">
              Cuando el alumno trabaja solo sin docente. Prima la <strong>certeza absoluta</strong>: preferible admitir desconocimiento antes que alucinar.
            </div>
          </div>
          <div style="font-family: var(--font-mono); font-size: 18px; font-weight: 700; color: var(--c-wine-primary); margin-top: 12px;">
            &bull; Perfil: Prudente / Cautela máxima
          </div>
        </div>

        <!-- Bloque Phi -->
        <div style="background: #FAF5F5; border-left: 10px solid var(--c-red-accent); padding: 24px 28px; display: flex; flex-direction: column; justify-content: space-between;">
          <div>
            <div style="display: flex; justify-content: space-between; align-items: baseline;">
              <span style="font-family: var(--font-sans); font-size: 26px; font-weight: 800; color: var(--c-red-accent);">
                Phi-4-mini
              </span>
              <span style="font-family: var(--font-mono); font-size: 22px; font-weight: 900; color: var(--c-red-accent);">
                0.0% Bloqueos
              </span>
            </div>
            <div style="font-family: var(--font-sans); font-size: 23px; font-weight: 800; color: #110103; margin-top: 6px;">
              Entorno: Aula Asistida con Docente
            </div>
            <div style="font-family: var(--font-sans); font-size: 21px; color: #5D4A4D; line-height: 1.45; margin-top: 10px;">
              Cuando hay profesor en sala guiando la clase. Prima la <strong>fluidez y dinamismo</strong>: el modelo nunca frena y el docente corrige desvíos.
            </div>
          </div>
          <div style="font-family: var(--font-mono); font-size: 18px; font-weight: 700; color: var(--c-red-accent); margin-top: 12px;">
            &bull; Perfil: Fluido / Requiere supervisión activa
          </div>
        </div>

      </div>

      <!-- FILA INFERIOR: REMATE EDITORIAL TIPO P2 -->
      <div style="background: #FAF5F5; border-top: 3.5px solid var(--c-wine-primary); border-bottom: 3.5px solid var(--c-wine-primary); padding: 14px 24px; display: flex; justify-content: space-between; align-items: center;">
        <div style="display: flex; align-items: center; gap: 14px;">
          <span style="font-family: var(--font-mono); font-size: 19px; font-weight: 800; color: var(--c-wine-primary); letter-spacing: 1.5px; white-space: nowrap;">
            CRITERIO DE ADOPCIÓN:
          </span>
          <span style="font-family: var(--font-sans); font-size: 23px; font-weight: 700; color: #110103; white-space: nowrap;">
            El modelo no lo define la nota del benchmark, sino la presencia o ausencia de supervisión docente.
          </span>
        </div>
        <span style="font-family: var(--font-mono); font-size: 19px; font-weight: 700; color: #5D4A4D; white-space: nowrap; margin-left: 20px;">
          Discusión del paper
        </span>
      </div>

    </div>
'''

# ===========================================================================
# OPCIÓN D3: Matriz Editorial en 4 Bloques Cuadrantes (2x2 Abierto)
# ===========================================================================
CONTENT_D3 = '''
    <h2 class="s-lead-question" style="font-size: 38px; font-weight: 800; margin: 0; line-height: 1.2; color: #2C0509;">
      Apego al material fuente no es aprendizaje: guía para auditar y desplegar tutores
    </h2>

    <div style="display: grid; grid-template-columns: 1fr 1fr; grid-template-rows: 1fr 1fr; gap: 24px; flex: 1; margin-top: 10px;">
      
      <!-- Cuadrante 1: La Falacia -->
      <div style="background: #FAF5F5; border-top: 6px solid var(--c-red-accent); padding: 24px 28px; display: flex; flex-direction: column; justify-content: space-between;">
        <div>
          <div style="font-family: var(--font-mono); font-size: 17px; font-weight: 800; color: var(--c-red-accent); letter-spacing: 1px; margin-bottom: 4px;">
            01 · DIAGNÓSTICO METODOLÓGICO
          </div>
          <div style="font-family: var(--font-sans); font-size: 26px; font-weight: 800; color: #110103; margin-bottom: 8px;">
            La Falacia de la Nota Agregada
          </div>
          <div style="font-family: var(--font-sans); font-size: 20px; color: #5D4A4D; line-height: 1.4;">
            El promedio general de <strong>0.795</strong> encubre fallos críticos. Similitud léxica con el libro no garantiza comprensión pedagógica del estudiante.
          </div>
        </div>
        <div style="font-family: var(--font-mono); font-size: 17px; font-weight: 700; color: var(--c-red-accent);">
          &bull; Riesgo: Falsa sensación de precisión
        </div>
      </div>

      <!-- Cuadrante 2: La Auditoría -->
      <div style="background: #FAF5F5; border-top: 6px solid #B38600; padding: 24px 28px; display: flex; flex-direction: column; justify-content: space-between;">
        <div>
          <div style="font-family: var(--font-mono); font-size: 17px; font-weight: 800; color: #B38600; letter-spacing: 1px; margin-bottom: 4px;">
            02 · PROTOCOLO DE AUDITORÍA
          </div>
          <div style="font-family: var(--font-sans); font-size: 26px; font-weight: 800; color: #110103; margin-bottom: 8px;">
            Desglose por Componentes
          </div>
          <div style="font-family: var(--font-sans); font-size: 20px; color: #5D4A4D; line-height: 1.4;">
            Prohibido certificar con un único valor. Obligatorio auditar por separado: <strong>recuperación (relevance)</strong>, <strong>fidelidad (grounding)</strong> y <strong>tasa de rechazo</strong>.
          </div>
        </div>
        <div style="font-family: var(--font-mono); font-size: 17px; font-weight: 700; color: #B38600;">
          &bull; Norma: Evaluación multi-dimensional
        </div>
      </div>

      <!-- Cuadrante 3: Despliegue Qwen -->
      <div style="background: #FAF5F5; border-top: 6px solid var(--c-wine-primary); padding: 24px 28px; display: flex; flex-direction: column; justify-content: space-between;">
        <div>
          <div style="display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 4px;">
            <span style="font-family: var(--font-mono); font-size: 17px; font-weight: 800; color: var(--c-wine-primary); letter-spacing: 1px;">
              03 · DESPLIEGUE A
            </span>
            <span style="font-family: var(--font-mono); font-size: 18px; font-weight: 900; color: var(--c-wine-primary);">
              85.7% Rechazo
            </span>
          </div>
          <div style="font-family: var(--font-sans); font-size: 26px; font-weight: 800; color: var(--c-wine-primary); margin-bottom: 8px;">
            Qwen2.5-3B &rarr; Autoestudio Autónomo
          </div>
          <div style="font-family: var(--font-sans); font-size: 20px; color: #5D4A4D; line-height: 1.4;">
            <strong>Sin profesor:</strong> Prima la certeza absoluta. Preferible admitir desconocimiento antes que inducir a un error conceptual que nadie corregirá.
          </div>
        </div>
        <div style="font-family: var(--font-mono); font-size: 17px; font-weight: 700; color: var(--c-wine-primary);">
          &bull; Cautela máxima frente a sondas trampa
        </div>
      </div>

      <!-- Cuadrante 4: Despliegue Phi -->
      <div style="background: #FAF5F5; border-top: 6px solid var(--c-red-accent); padding: 24px 28px; display: flex; flex-direction: column; justify-content: space-between;">
        <div>
          <div style="display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 4px;">
            <span style="font-family: var(--font-mono); font-size: 17px; font-weight: 800; color: var(--c-red-accent); letter-spacing: 1px;">
              04 · DESPLIEGUE B
            </span>
            <span style="font-family: var(--font-mono); font-size: 18px; font-weight: 900; color: var(--c-red-accent);">
              0.0% Bloqueos
            </span>
          </div>
          <div style="font-family: var(--font-sans); font-size: 26px; font-weight: 800; color: var(--c-red-accent); margin-bottom: 8px;">
            Phi-4-mini &rarr; Aula con Docente
          </div>
          <div style="font-family: var(--font-sans); font-size: 20px; color: #5D4A4D; line-height: 1.4;">
            <strong>Con profesor:</strong> Prima la fluidez de sesión. El tutor jamás frena al grupo y el docente supervisa y orienta en tiempo real.
          </div>
        </div>
        <div style="font-family: var(--font-mono); font-size: 17px; font-weight: 700; color: var(--c-red-accent);">
          &bull; Fluidez interactiva supervisada
        </div>
      </div>

    </div>
'''

HTML_TEMPLATE = '''<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Test Slide 17 Master</title>
  <link rel="stylesheet" href="http://localhost:8085/styles.css?v=31">
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
        ('slide_17_master_D1.html', 'slide_17_master_D1.png', CONTENT_D1),
        ('slide_17_master_D2.html', 'slide_17_master_D2.png', CONTENT_D2),
        ('slide_17_master_D3.html', 'slide_17_master_D3.png', CONTENT_D3),
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
