# -*- coding: utf-8 -*-
"""
Variante C1.2: Refinamiento Ultra-Limpio de C1.
- Gráfica como HERO ABSOLUTO arriba: sin textos redundantes al pie del gráfico, barras y puntos más grandes y claros.
- Abajo: exactamente 2 tarjetas K2.2 con las dos verdades científicas clave (Wilcoxon p=0.569 y Ruido 18.5x).
"""
import os
from playwright.sync_api import sync_playwright

output_dir = r"C:\Users\ASUS\.gemini\antigravity-ide\brain\a6624504-511c-4b9d-bc9a-468e348bde40"
os.makedirs(output_dir, exist_ok=True)

def get_ultra_clean_chart_svg():
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

VAR_C1_2_HTML = f'''
<section class="slide s-white active" id="slide-13-var-c1-2">
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

    <!-- HERO CENTRAL: Gráfica como protagonista absoluto con máximo respiro -->
    <div style="background: #FAF5F5; border: 2.5px solid var(--c-wine-primary); padding: 18px 28px 12px 28px;">
      <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px;">
        <div style="font-family: var(--font-sans); font-size: 24px; font-weight: 800; color: var(--c-wine-dark);">
          DISPERSIÓN Y SOLAPAMIENTO POR PREGUNTA CURRICULAR (FIGURA 3 DEL PAPER)
        </div>
        <div style="display: flex; gap: 28px; font-family: var(--font-sans); font-size: 22px; font-weight: 800;">
          <span style="color: #460811; display: flex; align-items: center; gap: 8px;">
            <span style="display: inline-block; width: 16px; height: 16px; background: #460811; border-radius: 50%;"></span>
            Phi-4-mini (media ± σ)
          </span>
          <span style="color: #C9101B; display: flex; align-items: center; gap: 8px;">
            <span style="display: inline-block; width: 16px; height: 16px; background: #C9101B; border-radius: 50%;"></span>
            Qwen2.5-3B (media ± σ)
          </span>
        </div>
      </div>

      {get_ultra_clean_chart_svg()}
    </div>

    <!-- TARJETAS COMPLEMENTARIAS K2.2: Dos verdades científicas contundentes -->
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
    html_path = os.path.join(output_dir, 'slide_13_c1_2.html')
    png_path = os.path.join(output_dir, 'slide_13_c1_2.png')

    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(HTML_WRAPPER.format(content=VAR_C1_2_HTML))

    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(viewport={"width": 1920, "height": 1080})
        page.goto(f"file:///{html_path.replace(os.sep, '/')}")
        page.wait_for_timeout(400)
        page.screenshot(path=png_path)
        print("Captured: slide_13_c1_2.png")
        browser.close()

if __name__ == '__main__':
    main()
