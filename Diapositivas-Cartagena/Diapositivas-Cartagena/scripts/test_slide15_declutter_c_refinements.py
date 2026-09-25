# -*- coding: utf-8 -*-
import os
from playwright.sync_api import sync_playwright

output_dir = r"C:\Users\ASUS\.gemini\antigravity-ide\brain\a6624504-511c-4b9d-bc9a-468e348bde40"
os.makedirs(output_dir, exist_ok=True)

# ---------------------------------------------------------------------------
# SVG 1: Slopegraph más amplio y verticalmente generoso (Alto 540)
# Ya que no hay franja superior ni nota editorial abajo, el gráfico puede crecer
# ---------------------------------------------------------------------------
def make_svg(show_micro_legend=False):
    # Escala 1.0 a 5.0 (y: 470 a 70 => dy = 400px => 100px/unidad)
    # y(5.0) = 70
    # y(4.0) = 170
    # y(3.67) = 203
    # y(3.33) = 237
    # y(3.00) = 270
    # y(2.33) = 337
    # y(1.67) = 403
    # y(1.33) = 437
    # y(1.00) = 470

    micro_legend = ''
    if show_micro_legend:
        micro_legend = '''
        <!-- Micro leyenda discreta y mínima -->
        <g transform="translate(420, 20)">
          <line x1="0" y1="0" x2="30" y2="0" stroke="#460811" stroke-width="4" />
          <text x="38" y="5" font-size="16" font-weight="700" fill="#460811">Docente 1</text>
          
          <line x1="150" y1="0" x2="180" y2="0" stroke="#C9101B" stroke-width="4" />
          <text x="188" y="5" font-size="16" font-weight="700" fill="#C9101B">Docente 2</text>

          <line x1="300" y1="0" x2="330" y2="0" stroke="#D2C5C7" stroke-width="2" />
          <text x="338" y="5" font-size="16" font-weight="600" fill="#8D7A7D">Sin aval</text>
        </g>
        '''

    return f'''
<svg viewBox="0 0 1140 540" style="width: 100%; height: auto; font-family: var(--font-sans);">
  {micro_legend}

  <!-- Rejilla horizontal sutil de fondo -->
  <line x1="200" y1="70" x2="900" y2="70" stroke="#EAE0E1" stroke-width="1.2" stroke-dasharray="4 4" />
  <line x1="200" y1="170" x2="900" y2="170" stroke="#EAE0E1" stroke-width="1.2" stroke-dasharray="4 4" />
  <line x1="200" y1="270" x2="900" y2="270" stroke="#EAE0E1" stroke-width="1.2" stroke-dasharray="4 4" />
  <line x1="200" y1="370" x2="900" y2="370" stroke="#EAE0E1" stroke-width="1.2" stroke-dasharray="4 4" />
  <line x1="200" y1="470" x2="900" y2="470" stroke="#EAE0E1" stroke-width="1.2" stroke-dasharray="4 4" />

  <!-- Ejes verticales de docentes -->
  <line x1="280" y1="60" x2="280" y2="480" stroke="#460811" stroke-width="4" />
  <line x1="820" y1="60" x2="820" y2="480" stroke="#C9101B" stroke-width="4" />

  <!-- Cabeceras de ejes con medias -->
  <text x="280" y="24" font-size="32" font-weight="900" fill="#460811" text-anchor="middle">Docente 1</text>
  <text x="280" y="50" font-size="20" font-weight="800" fill="#460811" text-anchor="middle" font-family="var(--font-mono)">MEDIA: 3.33</text>

  <text x="820" y="24" font-size="32" font-weight="900" fill="#C9101B" text-anchor="middle">Docente 2</text>
  <text x="820" y="50" font-size="20" font-weight="800" fill="#C9101B" text-anchor="middle" font-family="var(--font-mono)">MEDIA: 1.93</text>

  <!-- Escalas numéricas (1.0 a 5.0) -->
  <text x="250" y="78" font-size="22" fill="#A08D90" text-anchor="end" font-weight="700" font-family="var(--font-mono)">5.0</text>
  <text x="250" y="178" font-size="22" fill="#A08D90" text-anchor="end" font-weight="700" font-family="var(--font-mono)">4.0</text>
  <text x="250" y="278" font-size="22" fill="#A08D90" text-anchor="end" font-weight="700" font-family="var(--font-mono)">3.0</text>
  <text x="250" y="378" font-size="22" fill="#A08D90" text-anchor="end" font-weight="700" font-family="var(--font-mono)">2.0</text>
  <text x="250" y="478" font-size="22" fill="#A08D90" text-anchor="end" font-weight="700" font-family="var(--font-mono)">1.0</text>

  <text x="850" y="78" font-size="22" fill="#A08D90" font-weight="700" font-family="var(--font-mono)">5.0</text>
  <text x="850" y="178" font-size="22" fill="#A08D90" font-weight="700" font-family="var(--font-mono)">4.0</text>
  <text x="850" y="278" font-size="22" fill="#A08D90" font-weight="700" font-family="var(--font-mono)">3.0</text>
  <text x="850" y="378" font-size="22" fill="#A08D90" font-weight="700" font-family="var(--font-mono)">2.0</text>
  <text x="850" y="478" font-size="22" fill="#A08D90" font-weight="700" font-family="var(--font-mono)">1.0</text>

  <!-- LÍNEAS OPACADAS DE FONDO (4 Reprobadas por ambos docentes) -->
  <line x1="280" y1="270" x2="820" y2="403" stroke="#D8CBCD" stroke-width="2" opacity="0.4" />
  <line x1="280" y1="270" x2="820" y2="470" stroke="#D8CBCD" stroke-width="2" opacity="0.4" />
  <line x1="280" y1="170" x2="820" y2="437" stroke="#D8CBCD" stroke-width="2" opacity="0.4" />
  <line x1="280" y1="237" x2="820" y2="270" stroke="#D8CBCD" stroke-width="2" opacity="0.4" />

  <!-- LÍNEAS PROTAGONISTAS DOCENTE 1: Aprobadas por D1 (Vino 5px) que se desploman a 1.0 -->
  <line x1="280" y1="203" x2="820" y2="437" stroke="#460811" stroke-width="5" />
  <line x1="280" y1="237" x2="820" y2="470" stroke="#460811" stroke-width="5" />
  <line x1="280" y1="170" x2="820" y2="470" stroke="#460811" stroke-width="6.5" />

  <!-- LÍNEAS PROTAGONISTAS DOCENTE 2: Aprobadas por D2 (Rojo 5px) -->
  <line x1="280" y1="270" x2="820" y2="337" stroke="#C9101B" stroke-width="5" />
  <line x1="280" y1="270" x2="820" y2="237" stroke="#C9101B" stroke-width="5" />
  <line x1="280" y1="270" x2="820" y2="237" stroke="#C9101B" stroke-width="5" />

  <!-- Puntos destacados de las líneas clave -->
  <circle cx="280" cy="170" r="9" fill="#460811" />
  <circle cx="280" cy="203" r="8" fill="#460811" />
  <circle cx="280" cy="237" r="8" fill="#460811" />
  <circle cx="280" cy="270" r="9" fill="#460811" />

  <circle cx="820" cy="237" r="9.5" fill="#C9101B" />
  <circle cx="820" cy="337" r="8" fill="#C9101B" />
  <circle cx="820" cy="437" r="8" fill="#460811" />
  <circle cx="820" cy="470" r="10" fill="#460811" />
</svg>
'''

# -------------------------------------------------------------
# VARIANTE C1: Pura, Ultra-Limpia, Cero Texto Extra
# Sin encabezado de Figura 4, sin nota editorial abajo, sin leyenda de texto
# -------------------------------------------------------------
CONTENT_C1 = f'''
    <h2 class="s-lead-question" style="font-size: 40px; font-weight: 800; margin: 0; line-height: 1.2; color: #2C0509;">
      La prueba docente: cuando los evaluadores humanos discrepan del algoritmo
    </h2>

    <div style="display: grid; grid-template-columns: 1180px 1fr; gap: 44px; align-items: center; flex: 1;">
      
      <!-- CONTENEDOR 100% LIBRE Y FLAT (Cero cajas, máxima respiración) -->
      <div style="display: flex; flex-direction: column; justify-content: center; height: 100%;">
        {make_svg(show_micro_legend=False)}
      </div>

      <!-- COLUMNA DERECHA: TEXTO MÍNIMO ABSOLUTO -->
      <div style="display: flex; flex-direction: column; justify-content: space-around; height: 100%; gap: 20px;">
        
        <!-- Métrica 1 -->
        <div style="background: #FAF5F5; border-left: 10px solid #B38600; padding: 26px 28px; display: flex; flex-direction: column; justify-content: center;">
          <div style="font-family: var(--font-mono); font-size: 68px; font-weight: 900; color: #B38600; line-height: 1;">
            0 / 10
          </div>
          <div style="font-family: var(--font-sans); font-size: 26px; font-weight: 800; color: #110103; margin-top: 8px;">
            Coincidencias en Aula
          </div>
          <div style="font-family: var(--font-sans); font-size: 20px; color: #5D4A4D; font-weight: 600; margin-top: 4px;">
            Aprobaciones 100% disjuntas.
          </div>
        </div>

        <!-- Métrica 2 -->
        <div style="background: #FAF5F5; border-left: 10px solid var(--c-red-accent); padding: 26px 28px; display: flex; flex-direction: column; justify-content: center;">
          <div style="font-family: var(--font-mono); font-size: 54px; font-weight: 900; color: var(--c-red-accent); line-height: 1;">
            &kappa; = -0.429
          </div>
          <div style="font-family: var(--font-sans); font-size: 26px; font-weight: 800; color: #110103; margin-top: 8px;">
            Desacuerdo Severo
          </div>
          <div style="font-family: var(--font-sans); font-size: 20px; color: #5D4A4D; font-weight: 600; margin-top: 4px;">
            Kappa de Cohen negativo.
          </div>
        </div>

        <!-- Métrica 3 -->
        <div style="background: #FAF5F5; border-left: 10px solid var(--c-wine-primary); padding: 26px 28px; display: flex; flex-direction: column; justify-content: center;">
          <div style="font-family: var(--font-mono); font-size: 48px; font-weight: 900; color: var(--c-wine-primary); line-height: 1;">
            &rho; &le; +0.26
          </div>
          <div style="font-family: var(--font-sans); font-size: 26px; font-weight: 800; color: #110103; margin-top: 8px;">
            Correlación Nula
          </div>
          <div style="font-family: var(--font-sans); font-size: 20px; color: #5D4A4D; font-weight: 600; margin-top: 4px;">
            Sin relación con el algoritmo.
          </div>
        </div>

      </div>
    </div>
'''

# -------------------------------------------------------------
# VARIANTE C2: Con Micro-Leyenda Discreta en el gráfico (sin texto largo de "aprobó")
# -------------------------------------------------------------
CONTENT_C2 = f'''
    <h2 class="s-lead-question" style="font-size: 40px; font-weight: 800; margin: 0; line-height: 1.2; color: #2C0509;">
      La prueba docente: cuando los evaluadores humanos discrepan del algoritmo
    </h2>

    <div style="display: grid; grid-template-columns: 1180px 1fr; gap: 44px; align-items: center; flex: 1;">
      
      <!-- CONTENEDOR 100% LIBRE Y FLAT -->
      <div style="display: flex; flex-direction: column; justify-content: center; height: 100%;">
        {make_svg(show_micro_legend=True)}
      </div>

      <!-- COLUMNA DERECHA: TEXTO MÍNIMO ABSOLUTO -->
      <div style="display: flex; flex-direction: column; justify-content: space-around; height: 100%; gap: 20px;">
        
        <!-- Métrica 1 -->
        <div style="background: #FAF5F5; border-left: 10px solid #B38600; padding: 26px 28px; display: flex; flex-direction: column; justify-content: center;">
          <div style="font-family: var(--font-mono); font-size: 68px; font-weight: 900; color: #B38600; line-height: 1;">
            0 / 10
          </div>
          <div style="font-family: var(--font-sans); font-size: 26px; font-weight: 800; color: #110103; margin-top: 8px;">
            Coincidencias en Aula
          </div>
          <div style="font-family: var(--font-sans); font-size: 20px; color: #5D4A4D; font-weight: 600; margin-top: 4px;">
            Aprobaciones 100% disjuntas.
          </div>
        </div>

        <!-- Métrica 2 -->
        <div style="background: #FAF5F5; border-left: 10px solid var(--c-red-accent); padding: 26px 28px; display: flex; flex-direction: column; justify-content: center;">
          <div style="font-family: var(--font-mono); font-size: 54px; font-weight: 900; color: var(--c-red-accent); line-height: 1;">
            &kappa; = -0.429
          </div>
          <div style="font-family: var(--font-sans); font-size: 26px; font-weight: 800; color: #110103; margin-top: 8px;">
            Desacuerdo Severo
          </div>
          <div style="font-family: var(--font-sans); font-size: 20px; color: #5D4A4D; font-weight: 600; margin-top: 4px;">
            Kappa de Cohen negativo.
          </div>
        </div>

        <!-- Métrica 3 -->
        <div style="background: #FAF5F5; border-left: 10px solid var(--c-wine-primary); padding: 26px 28px; display: flex; flex-direction: column; justify-content: center;">
          <div style="font-family: var(--font-mono); font-size: 48px; font-weight: 900; color: var(--c-wine-primary); line-height: 1;">
            &rho; &le; +0.26
          </div>
          <div style="font-family: var(--font-sans); font-size: 26px; font-weight: 800; color: #110103; margin-top: 8px;">
            Correlación Nula
          </div>
          <div style="font-family: var(--font-sans); font-size: 20px; color: #5D4A4D; font-weight: 600; margin-top: 4px;">
            Sin relación con el algoritmo.
          </div>
        </div>

      </div>
    </div>
'''

HTML_TEMPLATE = '''<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Test Slide 15 Declutter C</title>
  <link rel="stylesheet" href="http://localhost:8085/styles.css?v=28">
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
        ('slide_15_c1_pure.html', 'slide_15_c1_pure.png', CONTENT_C1),
        ('slide_15_c2_micro.html', 'slide_15_c2_micro.png', CONTENT_C2),
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
