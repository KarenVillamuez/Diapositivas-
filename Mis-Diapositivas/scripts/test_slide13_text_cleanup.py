# -*- coding: utf-8 -*-
"""
Pruebas de limpieza y reducción de texto para Slide 13:
L1: Sintética y Directa (1 sola línea limpia por métrica, eliminando palabras redundantes)
L2: Ultra-Telegrafiada (Cifras protagonistas, frases de impacto instantáneo)
L3: Formato Balanceado (Cifra + Título descriptivo + 1 dato numérico clave)
"""
import os
from playwright.sync_api import sync_playwright

output_dir = r"C:\Users\ASUS\.gemini\antigravity-ide\brain\a6624504-511c-4b9d-bc9a-468e348bde40"
os.makedirs(output_dir, exist_ok=True)

def get_chart_box(title="SOLAPAMIENTO EN 12 PREGUNTAS CURRICULARES"):
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
        <line x1="{xc - 12}" y1="{m1[0]}" x2="{xc - 12}" y2="{m1[1]}" stroke="var(--c-wine-primary)" stroke-width="5.5" stroke-linecap="round" />
        <circle cx="{xc - 12}" cy="{m1[2]}" r="8.5" fill="var(--c-wine-primary)" />
        
        <line x1="{xc + 12}" y1="{m2[0]}" x2="{xc + 12}" y2="{m2[1]}" stroke="var(--c-red-accent)" stroke-width="5.5" stroke-linecap="round" />
        <circle cx="{xc + 12}" cy="{m2[2]}" r="8.5" fill="var(--c-red-accent)" />
        
        <text x="{xc}" y="278" font-size="24" font-weight="800" fill="#2C0509" text-anchor="middle">{label}</text>
        '''
    
    return f'''
    <div style="background: #FAF5F5; border: 2.5px solid var(--c-wine-primary); padding: 18px 28px 14px 28px;">
      <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px;">
        <div style="font-family: var(--font-sans); font-size: 24px; font-weight: 800; color: var(--c-wine-dark);">
          {title}
        </div>
        <div style="display: flex; gap: 32px; font-family: var(--font-sans); font-size: 22px; font-weight: 800;">
          <span style="color: var(--c-wine-primary); display: flex; align-items: center; gap: 8px;">
            <span style="display: inline-block; width: 16px; height: 16px; background: var(--c-wine-primary); border-radius: 50%;"></span>
            Phi-4-mini
          </span>
          <span style="color: var(--c-red-accent); display: flex; align-items: center; gap: 8px;">
            <span style="display: inline-block; width: 16px; height: 16px; background: var(--c-red-accent); border-radius: 50%;"></span>
            Qwen2.5-3B
          </span>
        </div>
      </div>

      <svg viewBox="0 0 1560 300" style="width: 100%; height: auto; font-family: var(--font-sans);">
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
    </div>
    '''

# -----------------------------------------------------------------------------
# OPCION L1: Sintética y Directa (1 sola frase por métrica, sin redundancias)
# -----------------------------------------------------------------------------
HTML_L1 = f'''
<section class="slide s-white active" id="slide-13-l1">
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

    {get_chart_box("SOLAPAMIENTO EN 12 PREGUNTAS CURRICULARES")}

    <!-- METRICAS L1: Sintéticas y sin texto de relleno -->
    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 48px; padding: 8px 12px;">
      
      <!-- Métrica 1 -->
      <div style="display: flex; gap: 22px; align-items: stretch;">
        <div style="width: 7px; background-color: var(--c-wine-primary); flex-shrink: 0;"></div>
        <div style="display: flex; flex-direction: column; justify-content: center;">
          <div style="display: flex; align-items: baseline; gap: 14px; margin-bottom: 2px;">
            <span style="font-family: var(--font-mono); font-size: 52px; font-weight: 800; color: var(--c-wine-primary); line-height: 1;">p = 0.569</span>
            <span style="font-family: var(--font-mono); font-size: 24px; font-weight: 700; color: #555555;">W = 31.0</span>
          </div>
          <div style="font-family: var(--font-sans); font-size: 25px; font-weight: 800; color: var(--c-wine-dark); margin-bottom: 3px;">
            Empate Estadístico Formal
          </div>
          <div style="font-family: var(--font-sans); font-size: 22px; color: #110103; font-weight: 600;">
            Brecha de solo <strong>0.002</strong> (0.8030 vs 0.8010) sin diferencia significativa.
          </div>
        </div>
      </div>

      <!-- Métrica 2 -->
      <div style="display: flex; gap: 22px; align-items: stretch;">
        <div style="width: 7px; background-color: var(--c-red-accent); flex-shrink: 0;"></div>
        <div style="display: flex; flex-direction: column; justify-content: center;">
          <div style="display: flex; align-items: baseline; gap: 14px; margin-bottom: 2px;">
            <span style="font-family: var(--font-mono); font-size: 52px; font-weight: 800; color: var(--c-red-accent); line-height: 1;">18.5×</span>
            <span style="font-family: var(--font-mono); font-size: 22px; font-weight: 800; color: var(--c-red-accent);">RUIDO &gt; SEÑAL</span>
          </div>
          <div style="font-family: var(--font-sans); font-size: 25px; font-weight: 800; color: var(--c-wine-dark); margin-bottom: 3px;">
            Varianza por Semilla
          </div>
          <div style="font-family: var(--font-sans); font-size: 22px; color: #110103; font-weight: 600;">
            El azar de semillas (<strong>0.037</strong>) domina el ranking: <strong>4 semillas obligatorias</strong>.
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
# OPCION L2: Ultra-Telegrafiada (Cifras grandes + Frases mínimas de impacto)
# -----------------------------------------------------------------------------
HTML_L2 = f'''
<section class="slide s-white active" id="slide-13-l2">
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

    {get_chart_box("SOLAPAMIENTO CURRICULAR (4 SEMILLAS)")}

    <!-- METRICAS L2: Ultra Telegrafiado -->
    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 48px; padding: 10px 14px;">
      
      <!-- Métrica 1 -->
      <div style="display: flex; gap: 20px; align-items: stretch;">
        <div style="width: 7px; background-color: var(--c-wine-primary); flex-shrink: 0;"></div>
        <div>
          <div style="font-family: var(--font-mono); font-size: 56px; font-weight: 800; color: var(--c-wine-primary); line-height: 1; margin-bottom: 6px;">
            p = 0.569
          </div>
          <div style="font-family: var(--font-sans); font-size: 26px; font-weight: 800; color: var(--c-wine-dark);">
            Empate Estadístico (Wilcoxon W = 31.0)
          </div>
          <div style="font-family: var(--font-sans); font-size: 23px; color: #110103; font-weight: 600; margin-top: 4px;">
            Diferencia neta de apenas <strong>0.002</strong>.
          </div>
        </div>
      </div>

      <!-- Métrica 2 -->
      <div style="display: flex; gap: 20px; align-items: stretch;">
        <div style="width: 7px; background-color: var(--c-red-accent); flex-shrink: 0;"></div>
        <div>
          <div style="font-family: var(--font-mono); font-size: 56px; font-weight: 800; color: var(--c-red-accent); line-height: 1; margin-bottom: 6px;">
            18.5×
          </div>
          <div style="font-family: var(--font-sans); font-size: 26px; font-weight: 800; color: var(--c-wine-dark);">
            Ruido Estocástico Dominante
          </div>
          <div style="font-family: var(--font-sans); font-size: 23px; color: #110103; font-weight: 600; margin-top: 4px;">
            Desviación de <strong>0.037</strong> (exige 4 semillas).
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
# OPCION L3: Balance Minimalista en 1 Sola Línea por Bloque
# -----------------------------------------------------------------------------
HTML_L3 = f'''
<section class="slide s-white active" id="slide-13-l3">
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

    {get_chart_box("DISPERSIÓN EN 12 PREGUNTAS CURRICULARES")}

    <!-- METRICAS L3: Bloque Horizontal Compacto y Cristalino -->
    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 48px; padding: 8px 14px;">
      
      <!-- Métrica 1 -->
      <div style="display: flex; gap: 20px; align-items: center;">
        <div style="width: 7px; height: 75px; background-color: var(--c-wine-primary); flex-shrink: 0;"></div>
        <div>
          <div style="display: flex; align-items: baseline; gap: 12px;">
            <span style="font-family: var(--font-mono); font-size: 52px; font-weight: 800; color: var(--c-wine-primary); line-height: 1;">p = 0.569</span>
            <span style="font-family: var(--font-sans); font-size: 25px; font-weight: 800; color: var(--c-wine-dark);">Empate Real</span>
          </div>
          <div style="font-family: var(--font-sans); font-size: 22px; color: #110103; font-weight: 600; margin-top: 5px;">
            Wilcoxon (W = 31.0) · Brecha neta de apenas <strong>0.002</strong>.
          </div>
        </div>
      </div>

      <!-- Métrica 2 -->
      <div style="display: flex; gap: 20px; align-items: center;">
        <div style="width: 7px; height: 75px; background-color: var(--c-red-accent); flex-shrink: 0;"></div>
        <div>
          <div style="display: flex; align-items: baseline; gap: 12px;">
            <span style="font-family: var(--font-mono); font-size: 52px; font-weight: 800; color: var(--c-red-accent); line-height: 1;">18.5×</span>
            <span style="font-family: var(--font-sans); font-size: 25px; font-weight: 800; color: var(--c-wine-dark);">Ruido Estocástico</span>
          </div>
          <div style="font-family: var(--font-sans); font-size: 22px; color: #110103; font-weight: 600; margin-top: 5px;">
            Desviación de <strong>0.037</strong> · Obligatorio evaluar con 4 semillas.
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
  <title>Test Slide 13 Cleanup</title>
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
        ('slide_13_l1.html', 'slide_13_l1.png', HTML_L1),
        ('slide_13_l2.html', 'slide_13_l2.png', HTML_L2),
        ('slide_13_l3.html', 'slide_13_l3.png', HTML_L3),
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
