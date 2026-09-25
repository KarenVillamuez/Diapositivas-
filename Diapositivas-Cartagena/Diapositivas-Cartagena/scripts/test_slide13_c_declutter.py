# -*- coding: utf-8 -*-
"""
Generación de las 3 opciones declutter refinadas para Slide 13:
- C1: Gráfica Hero Centralizada Arriba (Full Width) + 2 Tarjetas K2.2 Abajo (La estructura aprobada del Slide 12)
- C2: Gráfica a la Izquierda (60%) + 2 Tarjetas a la Derecha (40%) (Distribución en 2 columnas despejada)
- C4: Gráfica Hero Arriba + Cinta Resumen Horizontal de 3 Métricas Abajo
"""
import os
from playwright.sync_api import sync_playwright

output_dir = r"C:\Users\ASUS\.gemini\antigravity-ide\brain\a6624504-511c-4b9d-bc9a-468e348bde40"
os.makedirs(output_dir, exist_ok=True)

def get_wide_chart_svg():
    x_coords = [
        (160, "G1", [(75, 115, 95), (80, 120, 100)]),
        (280, "G2", [(35, 145, 85), (60, 215, 138)]),
        (400, "G3", [(45, 68, 55), (55, 130, 85)]),
        (520, "G4", [(50, 82, 65), (60, 115, 80)]),
        (640, "V1", [(105, 185, 145), (85, 88, 86)]),
        (760, "V2", [(70, 125, 92), (75, 120, 95)]),
        (880, "V3", [(80, 140, 110), (75, 160, 115)]),
        (1000, "W1", [(25, 175, 95), (55, 110, 78)]),
        (1120, "W2", [(35, 95, 65), (45, 105, 72)]),
        (1240, "W3", [(70, 115, 95), (65, 130, 98)]),
        (1360, "R1", [(60, 75, 68), (65, 85, 76)]),
        (1480, "R2", [(110, 155, 135), (100, 195, 142)]),
    ]
    
    items_svg = ""
    for xc, label, (m1, m2) in x_coords:
        items_svg += f'''
        <!-- {label} -->
        <line x1="{xc - 12}" y1="{m1[0]}" x2="{xc - 12}" y2="{m1[1]}" stroke="#460811" stroke-width="5.5" stroke-linecap="round" />
        <circle cx="{xc - 12}" cy="{m1[2]}" r="8.5" fill="#460811" />
        
        <line x1="{xc + 12}" y1="{m2[0]}" x2="{xc + 12}" y2="{m2[1]}" stroke="#C9101B" stroke-width="5.5" stroke-linecap="round" />
        <circle cx="{xc + 12}" cy="{m2[2]}" r="8.5" fill="#C9101B" />
        
        <text x="{xc}" y="278" font-size="24" font-weight="800" fill="#2C0509" text-anchor="middle">{label}</text>
        '''
    
    return f'''
    <svg viewBox="0 0 1560 300" style="width: 100%; height: auto; font-family: var(--font-sans);">
      <!-- Eje Y -->
      <line x1="80" y1="25" x2="1530" y2="25" stroke="#E2D6D8" stroke-dasharray="4,4" />
      <text x="35" y="32" font-size="20" fill="#5D4A4D" font-weight="700">0.90</text>
      
      <line x1="80" y1="95" x2="1530" y2="95" stroke="#E2D6D8" stroke-dasharray="4,4" />
      <text x="35" y="102" font-size="20" fill="#5D4A4D" font-weight="700">0.80</text>

      <line x1="80" y1="165" x2="1530" y2="165" stroke="#E2D6D8" stroke-dasharray="4,4" />
      <text x="35" y="172" font-size="20" fill="#5D4A4D" font-weight="700">0.70</text>

      <line x1="80" y1="235" x2="1530" y2="235" stroke="#2C0509" stroke-width="2.5" />
      <text x="35" y="242" font-size="20" fill="#5D4A4D" font-weight="700">0.60</text>

      {items_svg}
    </svg>
    '''

def get_col_chart_svg():
    x_coords = [
        (115, "G1", [(75, 115, 95), (80, 120, 100)]),
        (168, "G2", [(35, 145, 85), (60, 215, 138)]),
        (221, "G3", [(45, 68, 55), (55, 130, 85)]),
        (274, "G4", [(50, 82, 65), (60, 115, 80)]),
        (327, "V1", [(105, 185, 145), (85, 88, 86)]),
        (380, "V2", [(70, 125, 92), (75, 120, 95)]),
        (433, "V3", [(80, 140, 110), (75, 160, 115)]),
        (486, "W1", [(25, 175, 95), (55, 110, 78)]),
        (539, "W2", [(35, 95, 65), (45, 105, 72)]),
        (592, "W3", [(70, 115, 95), (65, 130, 98)]),
        (645, "R1", [(60, 75, 68), (65, 85, 76)]),
        (698, "R2", [(110, 155, 135), (100, 195, 142)]),
    ]
    items_svg = ""
    for xc, label, (m1, m2) in x_coords:
        items_svg += f'''
        <line x1="{xc - 7}" y1="{m1[0]}" x2="{xc - 7}" y2="{m1[1]}" stroke="#460811" stroke-width="4.5" stroke-linecap="round" />
        <circle cx="{xc - 7}" cy="{m1[2]}" r="6.5" fill="#460811" />
        
        <line x1="{xc + 7}" y1="{m2[0]}" x2="{xc + 7}" y2="{m2[1]}" stroke="#C9101B" stroke-width="4.5" stroke-linecap="round" />
        <circle cx="{xc + 7}" cy="{m2[2]}" r="6.5" fill="#C9101B" />
        
        <text x="{xc}" y="262" font-size="19" font-weight="800" fill="#2C0509" text-anchor="middle">{label}</text>
        '''
    return f'''
    <svg viewBox="0 0 760 285" style="width: 100%; height: auto; font-family: var(--font-sans);">
      <line x1="75" y1="25" x2="735" y2="25" stroke="#E2D6D8" stroke-dasharray="3,3" />
      <text x="35" y="32" font-size="18" fill="#5D4A4D" font-weight="700">0.90</text>
      
      <line x1="75" y1="95" x2="735" y2="95" stroke="#E2D6D8" stroke-dasharray="3,3" />
      <text x="35" y="102" font-size="18" fill="#5D4A4D" font-weight="700">0.80</text>

      <line x1="75" y1="165" x2="735" y2="165" stroke="#E2D6D8" stroke-dasharray="3,3" />
      <text x="35" y="172" font-size="18" fill="#5D4A4D" font-weight="700">0.70</text>

      <line x1="75" y1="235" x2="735" y2="235" stroke="#2C0509" stroke-width="2.5" />
      <text x="35" y="242" font-size="18" fill="#5D4A4D" font-weight="700">0.60</text>

      {items_svg}
    </svg>
    '''

# -----------------------------------------------------------------------------
# C1 POLISHED: Gráfica Hero Central Arriba + 2 Tarjetas K2.2 Abajo
# -----------------------------------------------------------------------------
VAR_C1_POLISHED = f'''
<section class="slide s-white active" id="slide-13-var-c1">
  <header class="slide-header">
    <div class="sh-left">
      <span class="sh-red-bar"></span>
      <span class="sh-category">03 · RESULTADOS · EL FALSO EMPATE ESTADÍSTICO</span>
    </div>
    <img src="http://localhost:8085/assets/image6.png" alt="#LoxTIC" class="sh-loxtic">
  </header>
  <div class="sh-divider"></div>

  <div class="slide-content-area" style="justify-content: space-between; padding: 14px 0 6px 0;">
    
    <h2 class="s-lead-question" style="font-size: 38px; font-weight: 800; margin: 0; line-height: 1.2;">
      La ilusión del 0.795: la variación por semilla supera la diferencia entre modelos
    </h2>

    <!-- HERO CENTRAL: Gráfica con máxima amplitud y respiro -->
    <div style="background: #FAF5F5; border: 2.5px solid var(--c-wine-primary); padding: 18px 28px 14px 28px;">
      <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px;">
        <div style="font-family: var(--font-sans); font-size: 24px; font-weight: 800; color: var(--c-wine-dark);">
          DISPERSIÓN EN 12 PREGUNTAS CURRICULARES (FIGURA 3 DEL PAPER)
        </div>
        <div style="display: flex; gap: 32px; font-family: var(--font-sans); font-size: 22px; font-weight: 800;">
          <span style="color: #460811; display: flex; align-items: center; gap: 8px;">
            <span style="display: inline-block; width: 16px; height: 16px; background: #460811; border-radius: 50%;"></span>
            Phi-4-mini
          </span>
          <span style="color: #C9101B; display: flex; align-items: center; gap: 8px;">
            <span style="display: inline-block; width: 16px; height: 16px; background: #C9101B; border-radius: 50%;"></span>
            Qwen2.5-3B
          </span>
        </div>
      </div>

      {get_wide_chart_svg()}
    </div>

    <!-- TARJETAS COMPLEMENTARIAS: Exacto Ritmo Slide 12 (Solo 2 tarjetas horizontales K2.2) -->
    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 28px;">
      
      <!-- Tarjeta 1: Wilcoxon -->
      <div style="background: #FAF5F5; border: 2.5px solid var(--c-wine-primary); display: flex; align-items: stretch;">
        <div style="flex: 0 0 215px; background: #FFFFFF; border-right: 2.5px solid var(--c-wine-primary); color: #460811; font-family: var(--font-mono); font-size: 28px; font-weight: 800; display: flex; flex-direction: column; align-items: center; justify-content: center; padding: 14px 10px;">
          <div>p = 0.569</div>
          <div style="font-size: 19px; color: #555555; font-weight: 700; margin-top: 4px;">W = 31.0</div>
        </div>
        <div style="flex: 1; padding: 16px 22px; display: flex; flex-direction: column; justify-content: center;">
          <div style="font-family: var(--font-sans); font-size: 24px; font-weight: 800; color: var(--c-wine-dark); margin-bottom: 3px;">
            Prueba de Wilcoxon: Empate Real
          </div>
          <div style="font-family: var(--font-sans); font-size: 22px; color: #110103; font-weight: 600; line-height: 1.35;">
            Diferencia global de apenas <strong>0.002</strong> (0.8030 vs 0.8010). Al ser p &gt; 0.05, no hay diferencia estadísticamente medible.
          </div>
        </div>
      </div>

      <!-- Tarjeta 2: Varianza Semillas -->
      <div style="background: #FAF5F5; border: 2.5px solid var(--c-red-accent); display: flex; align-items: stretch;">
        <div style="flex: 0 0 215px; background: #FFFFFF; border-right: 2.5px solid var(--c-red-accent); color: var(--c-red-accent); font-family: var(--font-mono); font-size: 34px; font-weight: 800; display: flex; flex-direction: column; align-items: center; justify-content: center; padding: 14px 10px;">
          <div>18.5×</div>
          <div style="font-size: 16px; color: var(--c-red-accent); font-weight: 800; letter-spacing: 0.5px; margin-top: 2px;">RUIDO &gt; SEÑAL</div>
        </div>
        <div style="flex: 1; padding: 16px 22px; display: flex; flex-direction: column; justify-content: center;">
          <div style="font-family: var(--font-sans); font-size: 24px; font-weight: 800; color: var(--c-wine-dark); margin-bottom: 3px;">
            Variación Estocástica Dominante
          </div>
          <div style="font-family: var(--font-sans); font-size: 22px; color: #110103; font-weight: 600; line-height: 1.35;">
            El ruido entre semillas (<strong>0.037</strong>) supera por 18.5 veces la brecha neta. <strong>Obligatorio evaluar con 4 semillas</strong>.
          </div>
        </div>
      </div>

    </div>

  </div>

  <div class="slide-footer-rule"></div>
  <footer class="slide-footer">
    <span class="sf-left">VI CONGRESO CARTAGENA · 2026</span>
    <span class="sf-right">LOHACEMOSXTIC.COM · SLM OFFLINE</span>
  </footer>
</section>
'''

# -----------------------------------------------------------------------------
# C2 POLISHED: Gráfica Izquierda 60% + 2 Tarjetas Derecha 40%
# -----------------------------------------------------------------------------
VAR_C2_POLISHED = f'''
<section class="slide s-white active" id="slide-13-var-c2">
  <header class="slide-header">
    <div class="sh-left">
      <span class="sh-red-bar"></span>
      <span class="sh-category">03 · RESULTADOS · EL FALSO EMPATE ESTADÍSTICO</span>
    </div>
    <img src="http://localhost:8085/assets/image6.png" alt="#LoxTIC" class="sh-loxtic">
  </header>
  <div class="sh-divider"></div>

  <div class="slide-content-area" style="justify-content: space-between; padding: 14px 0 6px 0;">
    
    <h2 class="s-lead-question" style="font-size: 38px; font-weight: 800; margin: 0; line-height: 1.2;">
      La ilusión del 0.795: la variación por semilla supera la diferencia entre modelos
    </h2>

    <div style="display: grid; grid-template-columns: 1.45fr 1fr; gap: 32px; flex: 1; align-items: stretch; margin: 18px 0;">
      
      <!-- HERO IZQUIERDO -->
      <div style="background: #FAF5F5; border: 2.5px solid var(--c-wine-primary); padding: 22px 24px; display: flex; flex-direction: column; justify-content: space-between;">
        <div>
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px;">
            <span style="font-family: var(--font-sans); font-size: 23px; font-weight: 800; color: var(--c-wine-dark);">
              SOLAPAMIENTO EN 12 PREGUNTAS (FIGURA 3)
            </span>
            <div style="display: flex; gap: 20px; font-family: var(--font-sans); font-size: 20px; font-weight: 800;">
              <span style="color: #460811;">● Phi-4-mini</span>
              <span style="color: #C9101B;">● Qwen2.5-3B</span>
            </div>
          </div>

          {get_col_chart_svg()}
        </div>

        <div style="border-top: 1.5px solid #E2D6D8; padding-top: 10px; font-family: var(--font-sans); font-size: 21px; color: #110103; font-weight: 600; line-height: 1.35;">
          Las barras de dispersión se cruzan en casi todas las preguntas: <strong style="color: #460811;">no hay modelo dominante</strong>.
        </div>
      </div>

      <!-- DERECHA: Solo 2 Tarjetas Verticales K2.2 -->
      <div style="display: flex; flex-direction: column; gap: 20px; justify-content: space-between;">
        
        <div style="background: #FAF5F5; border: 2.5px solid var(--c-wine-primary); flex: 1; display: flex; align-items: stretch;">
          <div style="flex: 0 0 160px; background: #FFFFFF; border-right: 2.5px solid var(--c-wine-primary); color: #460811; font-family: var(--font-mono); font-size: 26px; font-weight: 800; display: flex; flex-direction: column; align-items: center; justify-content: center; padding: 12px 8px;">
            <div>p = 0.569</div>
            <div style="font-size: 18px; color: #555; font-weight: 700; margin-top: 4px;">W = 31.0</div>
          </div>
          <div style="flex: 1; padding: 18px 22px; display: flex; flex-direction: column; justify-content: center;">
            <div style="font-family: var(--font-sans); font-size: 24px; font-weight: 800; color: var(--c-wine-dark); margin-bottom: 4px;">
              Prueba de Wilcoxon
            </div>
            <div style="font-family: var(--font-sans); font-size: 21px; color: #110103; font-weight: 600; line-height: 1.35;">
              Diferencia neta de apenas <strong>0.002</strong> (0.8030 vs 0.8010). Al ser p &gt; 0.05, se confirma un <strong>empate estadístico formal</strong>.
            </div>
          </div>
        </div>

        <div style="background: #FAF5F5; border: 2.5px solid var(--c-red-accent); flex: 1; display: flex; align-items: stretch;">
          <div style="flex: 0 0 160px; background: #FFFFFF; border-right: 2.5px solid var(--c-red-accent); color: var(--c-red-accent); font-family: var(--font-mono); font-size: 34px; font-weight: 800; display: flex; flex-direction: column; align-items: center; justify-content: center; padding: 12px 8px;">
            <div>18.5×</div>
            <div style="font-size: 15px; color: var(--c-red-accent); font-weight: 800; margin-top: 2px;">RUIDO &gt; SEÑAL</div>
          </div>
          <div style="flex: 1; padding: 18px 22px; display: flex; flex-direction: column; justify-content: center;">
            <div style="font-family: var(--font-sans); font-size: 24px; font-weight: 800; color: var(--c-wine-dark); margin-bottom: 4px;">
              Varianza por Semilla
            </div>
            <div style="font-family: var(--font-sans); font-size: 21px; color: #110103; font-weight: 600; line-height: 1.35;">
              La desviación entre semillas (<strong>0.037</strong>) es 18.5× mayor que la brecha neta. <strong>Obligatorio evaluar con 4 semillas</strong>.
            </div>
          </div>
        </div>

      </div>

    </div>

  </div>

  <div class="slide-footer-rule"></div>
  <footer class="slide-footer">
    <span class="sf-left">VI CONGRESO CARTAGENA · 2026</span>
    <span class="sf-right">LOHACEMOSXTIC.COM · SLM OFFLINE</span>
  </footer>
</section>
'''

HTML_WRAPPER = '''<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Test Slide 13 Decluttered</title>
  <link rel="stylesheet" href="http://localhost:8085/styles.css?v=26">
</head>
<body style="margin: 0; padding: 0; background: #0b0103;">

  <div id="presentation-viewport">
    <div id="slides-stage">
      {content}
    </div>
  </div>

</body>
</html>
'''

def main():
    variants = [
        ('slide_13_c1_polished.html', 'slide_13_c1_polished.png', VAR_C1_POLISHED),
        ('slide_13_c2_polished.html', 'slide_13_c2_polished.png', VAR_C2_POLISHED),
    ]

    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(viewport={"width": 1920, "height": 1080})

        for html_name, png_name, content in variants:
            html_path = os.path.join(output_dir, html_name)
            png_path = os.path.join(output_dir, png_name)

            with open(html_path, 'w', encoding='utf-8') as f:
                f.write(HTML_WRAPPER.format(content=content))

            page.goto(f"file:///{html_path.replace(os.sep, '/')}")
            page.wait_for_timeout(400)
            page.screenshot(path=png_path)
            print(f"Captured: {png_name}")

        browser.close()

if __name__ == '__main__':
    main()
