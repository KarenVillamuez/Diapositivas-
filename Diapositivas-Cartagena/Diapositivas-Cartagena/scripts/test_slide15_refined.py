# -*- coding: utf-8 -*-
import os
from playwright.sync_api import sync_playwright

output_dir = r"C:\Users\ASUS\.gemini\antigravity-ide\brain\a6624504-511c-4b9d-bc9a-468e348bde40"
os.makedirs(output_dir, exist_ok=True)

# SVG Slopegraph refined
SVG_SLOPEGRAPH_REFINED = '''
<svg viewBox="0 0 740 350" style="width: 100%; height: auto; font-family: var(--font-sans);">
  <!-- Guías horizontales discretas -->
  <line x1="170" y1="60" x2="570" y2="60" stroke="#EAE0E1" stroke-width="1.5" stroke-dasharray="4 4" />
  <line x1="170" y1="120" x2="570" y2="120" stroke="#EAE0E1" stroke-width="1.5" stroke-dasharray="4 4" />
  <line x1="170" y1="180" x2="570" y2="180" stroke="#EAE0E1" stroke-width="1.5" stroke-dasharray="4 4" />
  <line x1="170" y1="240" x2="570" y2="240" stroke="#EAE0E1" stroke-width="1.5" stroke-dasharray="4 4" />
  <line x1="170" y1="300" x2="570" y2="300" stroke="#EAE0E1" stroke-width="1.5" stroke-dasharray="4 4" />

  <!-- Ejes de docentes -->
  <line x1="200" y1="42" x2="200" y2="315" stroke="#460811" stroke-width="3.5" />
  <line x1="540" y1="42" x2="540" y2="315" stroke="#C9101B" stroke-width="3.5" />

  <!-- Cabeceras de docentes con medias -->
  <text x="200" y="20" font-size="22" font-weight="800" fill="#460811" text-anchor="middle">Docente 1</text>
  <text x="200" y="38" font-size="16" font-weight="700" fill="#460811" text-anchor="middle" font-family="var(--font-mono)">MEDIA: 3.33</text>

  <text x="540" y="20" font-size="22" font-weight="800" fill="#C9101B" text-anchor="middle">Docente 2</text>
  <text x="540" y="38" font-size="16" font-weight="700" fill="#C9101B" text-anchor="middle" font-family="var(--font-mono)">MEDIA: 1.93</text>

  <!-- Escalas 1.0 a 5.0 -->
  <text x="180" y="65" font-size="17" fill="#8D7A7D" text-anchor="end" font-weight="700" font-family="var(--font-mono)">5.0</text>
  <text x="180" y="125" font-size="17" fill="#8D7A7D" text-anchor="end" font-weight="700" font-family="var(--font-mono)">4.0</text>
  <text x="180" y="185" font-size="17" fill="#8D7A7D" text-anchor="end" font-weight="700" font-family="var(--font-mono)">3.0</text>
  <text x="180" y="245" font-size="17" fill="#8D7A7D" text-anchor="end" font-weight="700" font-family="var(--font-mono)">2.0</text>
  <text x="180" y="305" font-size="17" fill="#8D7A7D" text-anchor="end" font-weight="700" font-family="var(--font-mono)">1.0</text>

  <text x="560" y="65" font-size="17" fill="#8D7A7D" font-weight="700" font-family="var(--font-mono)">5.0</text>
  <text x="560" y="125" font-size="17" fill="#8D7A7D" font-weight="700" font-family="var(--font-mono)">4.0</text>
  <text x="560" y="185" font-size="17" fill="#8D7A7D" font-weight="700" font-family="var(--font-mono)">3.0</text>
  <text x="560" y="245" font-size="17" fill="#8D7A7D" font-weight="700" font-family="var(--font-mono)">2.0</text>
  <text x="560" y="305" font-size="17" fill="#8D7A7D" font-weight="700" font-family="var(--font-mono)">1.0</text>

  <!-- 10 LÍNEAS REALES TABLA 4 -->
  <!-- Neutras (Gris suave 2px) -->
  <line x1="200" y1="180" x2="540" y2="260" stroke="#8D7A7D" stroke-width="2.5" opacity="0.45" />
  <line x1="200" y1="180" x2="540" y2="300" stroke="#8D7A7D" stroke-width="2.5" opacity="0.45" />
  <line x1="200" y1="120" x2="540" y2="280" stroke="#8D7A7D" stroke-width="2.5" opacity="0.45" />
  <line x1="200" y1="160" x2="540" y2="180" stroke="#8D7A7D" stroke-width="2.5" opacity="0.45" />

  <!-- Aprobadas Docente 1 (Vino 3.5px) -->
  <line x1="200" y1="140" x2="540" y2="280" stroke="#460811" stroke-width="3.5" opacity="0.9" />
  <line x1="200" y1="160" x2="540" y2="300" stroke="#460811" stroke-width="3.5" opacity="0.9" />
  <line x1="200" y1="120" x2="540" y2="300" stroke="#460811" stroke-width="4.5" opacity="0.95" />

  <!-- Aprobadas Docente 2 (Rojo 3.5px) -->
  <line x1="200" y1="180" x2="540" y2="220" stroke="#C9101B" stroke-width="3.5" opacity="0.9" />
  <line x1="200" y1="180" x2="540" y2="160" stroke="#C9101B" stroke-width="3.5" opacity="0.9" />
  <line x1="200" y1="180" x2="540" y2="160" stroke="#C9101B" stroke-width="3.5" opacity="0.9" />

  <!-- Puntos Docente 1 -->
  <circle cx="200" cy="120" r="7" fill="#460811" />
  <circle cx="200" cy="140" r="6" fill="#460811" />
  <circle cx="200" cy="160" r="6" fill="#460811" />
  <circle cx="200" cy="180" r="8" fill="#460811" />

  <!-- Puntos Docente 2 -->
  <circle cx="540" cy="160" r="7" fill="#C9101B" />
  <circle cx="540" cy="180" r="6" fill="#8D7A7D" />
  <circle cx="540" cy="220" r="6" fill="#C9101B" />
  <circle cx="540" cy="260" r="6" fill="#8D7A7D" />
  <circle cx="540" cy="280" r="7" fill="#460811" />
  <circle cx="540" cy="300" r="8" fill="#C9101B" />
</svg>
'''

# -------------------------------------------------------------
# VARIANTE 1: Split Clásico Optimizado (Slopegraph + 3 Tarjetas de Métricas + Franja P2)
# -------------------------------------------------------------
CONTENT_V1 = f'''
    <h2 class="s-lead-question" style="font-size: 38px; font-weight: 800; margin: 0; line-height: 1.2; color: #2C0509;">
      La prueba docente: cuando los evaluadores humanos discrepan del algoritmo
    </h2>

    <div style="display: grid; grid-template-columns: 880px 1fr; gap: 36px; align-items: stretch;">
      
      <!-- Columna Izquierda: Slopegraph con Tarjeta Editorial -->
      <div style="background: #FAF5F5; border: 2px solid #EAE0E1; border-left: 10px solid var(--c-wine-primary); padding: 22px 28px; display: flex; flex-direction: column; justify-content: space-between;">
        <div style="display: flex; justify-content: space-between; align-items: center;">
          <span style="font-family: var(--font-mono); font-size: 18px; font-weight: 800; color: var(--c-wine-primary); letter-spacing: 1.5px;">
            FIGURA 4 DEL PAPER · DISPARIDAD ENTRE DOCENTES
          </span>
          <span style="font-family: var(--font-mono); font-size: 17px; font-weight: 700; color: #5D4A4D;">
            10 respuestas a ciegas
          </span>
        </div>

        {SVG_SLOPEGRAPH_REFINED}

        <!-- Leyenda cromática de líneas -->
        <div style="display: flex; justify-content: space-around; align-items: center; background: #FFFFFF; border: 1.5px solid #EAE0E1; padding: 10px 18px;">
          <div style="display: flex; align-items: center; gap: 10px;">
            <div style="width: 24px; height: 5px; background: var(--c-wine-primary);"></div>
            <span style="font-family: var(--font-sans); font-size: 18px; font-weight: 700; color: #110103;">Aprobó Docente 1 (3)</span>
          </div>
          <div style="display: flex; align-items: center; gap: 10px;">
            <div style="width: 24px; height: 5px; background: var(--c-red-accent);"></div>
            <span style="font-family: var(--font-sans); font-size: 18px; font-weight: 700; color: #110103;">Aprobó Docente 2 (3)</span>
          </div>
          <div style="display: flex; align-items: center; gap: 10px;">
            <div style="width: 24px; height: 3px; background: #8D7A7D;"></div>
            <span style="font-family: var(--font-sans); font-size: 18px; font-weight: 600; color: #5D4A4D;">Reprobadas por ambos (4)</span>
          </div>
        </div>
      </div>

      <!-- Columna Derecha: 3 Métricas Abiertas con Barra de Acento -->
      <div style="display: flex; flex-direction: column; justify-content: space-between; gap: 16px;">
        
        <!-- Métrica 1: Kappa -->
        <div style="background: #FAF5F5; border-left: 10px solid var(--c-red-accent); padding: 18px 24px;">
          <div style="display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 4px;">
            <span style="font-family: var(--font-mono); font-size: 46px; font-weight: 800; color: var(--c-red-accent); line-height: 1;">
              &kappa; = -0.429
            </span>
            <span style="font-family: var(--font-mono); font-size: 18px; font-weight: 800; color: #2C0509; letter-spacing: 1px;">
              DESACUERDO SEVERO
            </span>
          </div>
          <div style="font-family: var(--font-sans); font-size: 21px; color: #110103; font-weight: 600; line-height: 1.35;">
            <strong>Kappa de Cohen negativo:</strong> el grado de discrepancia entre los profesores supera lo esperable por azar.
          </div>
        </div>

        <!-- Métrica 2: Rho Spearman -->
        <div style="background: #FAF5F5; border-left: 10px solid var(--c-wine-primary); padding: 18px 24px;">
          <div style="display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 4px;">
            <span style="font-family: var(--font-mono); font-size: 46px; font-weight: 800; color: var(--c-wine-primary); line-height: 1;">
              &rho; = +0.14 y +0.26
            </span>
            <span style="font-family: var(--font-mono); font-size: 18px; font-weight: 800; color: #2C0509; letter-spacing: 1px;">
              CORRELACIÓN NULA
            </span>
          </div>
          <div style="font-family: var(--font-sans); font-size: 21px; color: #110103; font-weight: 600; line-height: 1.35;">
            Sin relación estadística (<span style="font-family: var(--font-mono); font-size: 19px; font-weight: 700;">p &gt; 0.40</span>) entre el puntaje algorítmico y el juicio humano.
          </div>
        </div>

        <!-- Métrica 3: 0 en común -->
        <div style="background: #FAF5F5; border-left: 10px solid #B38600; padding: 18px 24px;">
          <div style="display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 4px;">
            <span style="font-family: var(--font-mono); font-size: 46px; font-weight: 800; color: #B38600; line-height: 1;">
              0 en Común
            </span>
            <span style="font-family: var(--font-mono); font-size: 18px; font-weight: 800; color: #2C0509; letter-spacing: 1px;">
              USO EN AULA DIRECTO
            </span>
          </div>
          <div style="font-family: var(--font-sans); font-size: 21px; color: #110103; font-weight: 600; line-height: 1.35;">
            Cada docente aprobó 3 de 10 respuestas sin modificar; <strong>¡cero coincidencias compartidas!</strong>
          </div>
        </div>

      </div>
    </div>

    <!-- REMATE EDITORIAL INFERIOR TIPO P2 -->
    <div style="background: #FAF5F5; border-top: 3.5px solid var(--c-wine-primary); border-bottom: 3.5px solid var(--c-wine-primary); padding: 14px 24px; display: flex; justify-content: space-between; align-items: center;">
      <div style="display: flex; align-items: center; gap: 14px;">
        <span style="font-family: var(--font-mono); font-size: 19px; font-weight: 800; color: var(--c-wine-primary); letter-spacing: 1.5px; white-space: nowrap;">
          LECCIÓN DE CAMPO:
        </span>
        <span style="font-family: var(--font-sans); font-size: 23px; font-weight: 700; color: #110103; white-space: nowrap;">
          Un puntaje algorítmico alto no predice aceptación pedagógica ni garantiza consenso docente.
        </span>
      </div>
      <span style="font-family: var(--font-mono); font-size: 19px; font-weight: 700; color: #5D4A4D; white-space: nowrap; margin-left: 20px;">
        Tabla 4 del paper
      </span>
    </div>
'''

# -------------------------------------------------------------
# VARIANTE 2: Doble Columna Enfrentada (50/50 - Slopegraph Cuantitativo vs Matriz de Disparidad)
# -------------------------------------------------------------
CONTENT_V2 = f'''
    <h2 class="s-lead-question" style="font-size: 38px; font-weight: 800; margin: 0; line-height: 1.2; color: #2C0509;">
      La prueba docente: cuando los evaluadores humanos discrepan del algoritmo
    </h2>

    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 34px; align-items: stretch;">
      
      <!-- Lado 1: Slopegraph Cuantitativo -->
      <div style="background: #FAF5F5; border: 2px solid #EAE0E1; border-left: 10px solid var(--c-wine-primary); padding: 22px 28px; display: flex; flex-direction: column; justify-content: space-between;">
        <div style="display: flex; justify-content: space-between; align-items: center;">
          <span style="font-family: var(--font-mono); font-size: 18px; font-weight: 800; color: var(--c-wine-primary); letter-spacing: 1.5px;">
            CALIFICACIÓN CUANTITATIVA (1.0 A 5.0)
          </span>
          <span style="font-family: var(--font-mono); font-size: 16px; font-weight: 700; color: #5D4A4D;">
            Figura 4
          </span>
        </div>

        {SVG_SLOPEGRAPH_REFINED}

        <div style="background: #FFFFFF; border: 1.5px solid #EAE0E1; padding: 12px 18px; display: flex; justify-content: space-between; align-items: center;">
          <span style="font-family: var(--font-sans); font-size: 21px; font-weight: 700; color: #2C0509;">
            Caída drástica de media: <strong style="font-family: var(--font-mono); color: var(--c-red-accent); font-size: 26px;">3.33 &rarr; 1.93</strong>
          </span>
          <span style="font-family: var(--font-mono); font-size: 17px; font-weight: 700; color: #5D4A4D;">
            Disparidad de umbral
          </span>
        </div>
      </div>

      <!-- Lado 2: Matriz de Desacuerdo Cualitativo -->
      <div style="background: #FAF5F5; border: 2px solid #EAE0E1; border-left: 10px solid var(--c-red-accent); padding: 22px 28px; display: flex; flex-direction: column; justify-content: space-between;">
        <div style="display: flex; justify-content: space-between; align-items: center;">
          <span style="font-family: var(--font-mono); font-size: 18px; font-weight: 800; color: var(--c-red-accent); letter-spacing: 1.5px;">
            DECISIÓN CUALITATIVA DE APROBACIÓN
          </span>
          <span style="font-family: var(--font-mono); font-size: 16px; font-weight: 700; color: #5D4A4D;">
            Uso sin modificar
          </span>
        </div>

        <!-- Macro-cifra 0 / 10 -->
        <div style="background: #FFFFFF; border: 2px solid #EAE0E1; padding: 18px 24px; text-align: center;">
          <div style="font-family: var(--font-mono); font-size: 64px; font-weight: 900; color: var(--c-red-accent); line-height: 1;">
            0 / 10 Coincidencias
          </div>
          <div style="font-family: var(--font-sans); font-size: 22px; font-weight: 700; color: #110103; margin-top: 6px;">
            Cada docente aprobó 3 respuestas, pero en conjuntos 100% disjuntos.
          </div>
        </div>

        <!-- 2 Cajas de métricas de correlación -->
        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 16px;">
          <div style="background: #FFFFFF; border: 1.5px solid #EAE0E1; padding: 14px 18px;">
            <div style="font-family: var(--font-mono); font-size: 34px; font-weight: 800; color: var(--c-red-accent);">
              &kappa; = -0.429
            </div>
            <div style="font-family: var(--font-sans); font-size: 18px; font-weight: 800; color: #2C0509;">
              Desacuerdo severo
            </div>
            <div style="font-family: var(--font-sans); font-size: 16px; color: #5D4A4D; margin-top: 2px;">
              Kappa de Cohen negativo: discrepan más que el azar.
            </div>
          </div>

          <div style="background: #FFFFFF; border: 1.5px solid #EAE0E1; padding: 14px 18px;">
            <div style="font-family: var(--font-mono); font-size: 34px; font-weight: 800; color: var(--c-wine-primary);">
              &rho; &le; +0.26
            </div>
            <div style="font-family: var(--font-sans); font-size: 18px; font-weight: 800; color: #2C0509;">
              Correlación nula
            </div>
            <div style="font-family: var(--font-sans); font-size: 16px; color: #5D4A4D; margin-top: 2px;">
              Sin significancia con el algoritmo (<span style="font-family: var(--font-mono);">p &gt; 0.40</span>).
            </div>
          </div>
        </div>

      </div>

    </div>

    <!-- REMATE EDITORIAL INFERIOR TIPO P2 -->
    <div style="background: #FAF5F5; border-top: 3.5px solid var(--c-wine-primary); border-bottom: 3.5px solid var(--c-wine-primary); padding: 14px 24px; display: flex; justify-content: space-between; align-items: center;">
      <div style="display: flex; align-items: center; gap: 14px;">
        <span style="font-family: var(--font-mono); font-size: 19px; font-weight: 800; color: var(--c-wine-primary); letter-spacing: 1.5px; white-space: nowrap;">
          LECCIÓN DE CAMPO:
        </span>
        <span style="font-family: var(--font-sans); font-size: 23px; font-weight: 700; color: #110103; white-space: nowrap;">
          Un puntaje algorítmico alto no predice aceptación pedagógica ni garantiza consenso docente.
        </span>
      </div>
      <span style="font-family: var(--font-mono); font-size: 19px; font-weight: 700; color: #5D4A4D; white-space: nowrap; margin-left: 20px;">
        Tabla 4 del paper
      </span>
    </div>
'''

HTML_TEMPLATE = '''<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Test Slide 15 Refined Options</title>
  <link rel="stylesheet" href="http://localhost:8085/styles.css?v=26">
</head>
<body style="margin: 0; padding: 0; background: #0b0103;">

  <div id="presentation-viewport">
    <div id="slides-stage">
      <section class="slide s-white active">
        <header class="slide-header">
          <div class="sh-left">
            <span class="sh-red-bar"></span>
            <span class="sh-category">03 · RESULTADOS · EL CHOQUE CON EL CRITERIO DOCENTE</span>
          </div>
          <img src="http://localhost:8085/assets/image6.png" alt="#LoxTIC" class="sh-loxtic">
        </header>
        <div class="sh-divider"></div>

        <div class="slide-content-area" style="top: 175px; height: 720px; justify-content: center; gap: 24px;">
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
        ('slide_15_v1_split.html', 'slide_15_v1_split.png', CONTENT_V1),
        ('slide_15_v2_balanced.html', 'slide_15_v2_balanced.png', CONTENT_V2),
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
