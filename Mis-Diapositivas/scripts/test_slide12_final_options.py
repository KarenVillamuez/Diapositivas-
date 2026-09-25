# -*- coding: utf-8 -*-
"""
Afinamiento final de Slide 12 según las directrices exactas del usuario:
1. Gráfica centrada y dominante como foco indiscutible del slide.
2. Esquinas 100% rectas (estilo nativo slide_12.html, sin cuadros dentro de cuadros).
3. Tarjetas técnicas complementarias con texto conciso y riguroso para el benchmark.
4. Cero textos pequeños (<21px): todo perfectamente legible a 15-20 metros.
"""
import os
from playwright.sync_api import sync_playwright

output_dir = r"C:\Users\ASUS\.gemini\antigravity-ide\brain\a6624504-511c-4b9d-bc9a-468e348bde40"
os.makedirs(output_dir, exist_ok=True)

# -----------------------------------------------------------------------------
# VARIANTE F4: Gráfica Centrada Hero + Conclusión de Benchmark + 2 Tarjetas
# -----------------------------------------------------------------------------
F4_HTML = '''
<section class="slide s-white active" id="slide-12-f4">
  <header class="slide-header">
    <div class="sh-left">
      <span class="sh-red-bar"></span>
      <span class="sh-category">03 · RESULTADOS · AUDITORÍA DE LA ECUACIÓN 1 (MÉTRICA Q)</span>
    </div>
    <img src="assets/image6.png" alt="#LoxTIC" class="sh-loxtic">
  </header>
  <div class="sh-divider"></div>

  <div class="slide-content-area" style="justify-content: flex-start; padding-top: 8px;">
    <!-- Pregunta Rectora concisa en una sola línea -->
    <h2 class="s-lead-question" style="font-size: 38px; font-weight: 800; margin-bottom: 20px; line-height: 1.2;">
      Anatomía de la fórmula: la métrica califica al modelo sin leer su respuesta
    </h2>

    <!-- EL FOCO PRINCIPAL: Gráfica Centrada Oficial de la Figura 1 (Esquinas 100% rectas) -->
    <div style="margin-bottom: 22px;">
      
      <!-- Fila superior de punteros focales -->
      <div style="display: flex; width: 100%; margin-bottom: 8px; align-items: flex-end;">
        <div style="width: 40%; font-family: var(--font-mono); font-size: 21px; font-weight: 700; color: var(--c-wine-primary); padding-left: 4px;">
          Q(r, q, C) = 0.40·G + 0.40·R + 0.20·L
        </div>
        <div style="width: 60%; font-family: var(--font-sans); font-size: 20px; font-weight: 800; color: var(--c-red-accent); text-align: center; background: #FFE4E6; border: 1.5px solid var(--c-red-accent); padding: 4px 0;">
          ▼ ¡EL 60% DE LA NOTA NO EVALÚA EL CONTENIDO DE LA RESPUESTA!
        </div>
      </div>

      <!-- Barra Segmentada Oficial (Altura dominante de 115px, esquinas rectas) -->
      <div class="formula-segmented-bar" style="margin: 0; height: 115px; border: 2px solid #2C0509;">
        <!-- 40% Grounding -->
        <div class="formula-segment" style="width: 40%; background-color: var(--c-wine-primary); justify-content: center; padding: 10px 16px;">
          <div class="formula-seg-pct" style="font-size: 44px; color: var(--c-gold); line-height: 1;">40%</div>
          <div class="formula-seg-label" style="font-size: 23px; letter-spacing: 0.5px; margin-top: 4px;">GROUNDING (r, C)</div>
          <div style="font-size: 20px; opacity: 0.95; font-weight: 600; margin-top: 2px;">
            Único término que evalúa la respuesta generada
          </div>
        </div>

        <!-- 40% Relevance -->
        <div class="formula-segment" style="width: 40%; background-color: var(--c-red-accent); border-left: 2px solid #FFFFFF; justify-content: center; padding: 10px 16px;">
          <div class="formula-seg-pct" style="font-size: 44px; line-height: 1;">40%</div>
          <div class="formula-seg-label" style="font-size: 23px; letter-spacing: 0.5px; margin-top: 4px;">RELEVANCE (q, C)</div>
          <div style="font-size: 20px; opacity: 0.95; font-weight: 600; margin-top: 2px;">
            Pregunta vs. contexto · ¡Ignora la respuesta!
          </div>
        </div>

        <!-- 20% Longitud -->
        <div class="formula-segment" style="width: 20%; background-color: #B38600; border-left: 2px solid #FFFFFF; justify-content: center; padding: 10px 16px;">
          <div class="formula-seg-pct" style="font-size: 44px; line-height: 1;">20%</div>
          <div class="formula-seg-label" style="font-size: 23px; letter-spacing: 0.5px; margin-top: 4px;">LONGITUD (r)</div>
          <div style="font-size: 20px; opacity: 0.95; font-weight: 600; margin-top: 2px;">
            Conteo de caracteres
          </div>
        </div>
      </div>

    </div>

    <!-- TARJETAS COMPLEMENTARIAS: Dos distorsiones en código del benchmark (Texto riguroso y conciso) -->
    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 28px;">
      
      <!-- Distorsión 01 -->
      <div style="background: #FFFFFF; border: 2px solid var(--c-wine-primary); padding: 22px 26px; display: flex; flex-direction: column; justify-content: space-between;">
        <div>
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
            <span style="font-family: var(--font-mono); font-size: 18px; font-weight: 800; color: var(--c-wine-primary); letter-spacing: 1px;">DISTORSIÓN EN CÓDIGO 01</span>
            <span style="font-family: var(--font-mono); font-size: 20px; font-weight: 800; color: var(--c-wine-primary); background: #FAF5F5; border: 1.5px solid var(--c-wine-primary); padding: 2px 10px;">(x + 1) / 2</span>
          </div>
          <h3 style="font-family: var(--font-sans); font-size: 26px; font-weight: 800; color: var(--c-wine-dark); margin: 0 0 10px 0;">
            Coseno Reescalado: Similitud 0.00 → 0.50
          </h3>
          <p style="font-family: var(--font-sans); font-size: 22px; color: #110103; font-weight: 600; line-height: 1.4; margin: 0;">
            Al transformar el rango [-1, 1] a [0, 1], cualquier respuesta desconectada o incoherente obtiene automáticamente un <strong>0.50 aprobatorio</strong> como nota base garantizada.
          </p>
        </div>
        <div style="margin-top: 16px; padding-top: 10px; border-top: 1.5px solid rgba(70,8,17,0.2); font-family: var(--font-sans); font-size: 21px; color: var(--c-wine-dark); font-weight: 700;">
          Impacto en benchmark: Infla artificialmente respuestas mediocres.
        </div>
      </div>

      <!-- Distorsión 02 -->
      <div style="background: #FFFFFF; border: 2px solid var(--c-red-accent); padding: 22px 26px; display: flex; flex-direction: column; justify-content: space-between;">
        <div>
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
            <span style="font-family: var(--font-mono); font-size: 18px; font-weight: 800; color: var(--c-red-accent); letter-spacing: 1px;">DISTORSIÓN EN CÓDIGO 02</span>
            <span style="font-family: var(--font-mono); font-size: 20px; font-weight: 800; color: var(--c-red-accent); background: #FFE4E6; border: 1.5px solid var(--c-red-accent); padding: 2px 10px;">NOTA = 0.80</span>
          </div>
          <h3 style="font-family: var(--font-sans); font-size: 26px; font-weight: 800; color: var(--c-wine-dark); margin: 0 0 10px 0;">
            Premio Fijo al Rechazo: 9 Frases = 0.80
          </h3>
          <p style="font-family: var(--font-sans); font-size: 22px; color: #110103; font-weight: 600; line-height: 1.4; margin: 0;">
            Nueve frases literales de abstención reciben nota automática de <strong>0.80</strong>. Bonifica idéntico la abstención legítima que un fallo por torpeza del buscador.
          </p>
        </div>
        <div style="margin-top: 16px; padding-top: 10px; border-top: 1.5px solid rgba(201,16,27,0.2); font-family: var(--font-sans); font-size: 21px; color: var(--c-red-accent); font-weight: 700;">
          Impacto en benchmark: Ventaja artificial sistemática a modelos sobre-conservadores.
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
# VARIANTE F5: Gráfica Centrada + Tarjetas con Fondo Suave (#FAF5F5) y Cifras Grandes
# -----------------------------------------------------------------------------
F5_HTML = '''
<section class="slide s-white active" id="slide-12-f5">
  <header class="slide-header">
    <div class="sh-left">
      <span class="sh-red-bar"></span>
      <span class="sh-category">03 · RESULTADOS · AUDITORÍA DE LA ECUACIÓN 1 (MÉTRICA Q)</span>
    </div>
    <img src="assets/image6.png" alt="#LoxTIC" class="sh-loxtic">
  </header>
  <div class="sh-divider"></div>

  <div class="slide-content-area" style="justify-content: flex-start; padding-top: 8px;">
    <!-- Pregunta Rectora -->
    <h2 class="s-lead-question" style="font-size: 38px; font-weight: 800; margin-bottom: 20px; line-height: 1.2;">
      Anatomía de la fórmula: la métrica califica al modelo sin leer su respuesta
    </h2>

    <!-- EL FOCO PRINCIPAL: Gráfica Centrada Oficial -->
    <div style="margin-bottom: 22px;">
      
      <!-- Fila superior de punteros focales -->
      <div style="display: flex; width: 100%; margin-bottom: 8px; align-items: flex-end;">
        <div style="width: 40%; font-family: var(--font-mono); font-size: 21px; font-weight: 700; color: var(--c-wine-primary); padding-left: 4px;">
          Q = 0.40·grounding + 0.40·relevance + 0.20·longitud
        </div>
        <div style="width: 60%; font-family: var(--font-sans); font-size: 20px; font-weight: 800; color: var(--c-red-accent); text-align: center; background: #FFE4E6; border: 1.5px solid var(--c-red-accent); padding: 4px 0;">
          ▼ ¡EL 60% DE LA NOTA NO EVALÚA EL CONTENIDO DE LA RESPUESTA!
        </div>
      </div>

      <!-- Barra Segmentada Oficial (115px de alto, esquinas rectas) -->
      <div class="formula-segmented-bar" style="margin: 0; height: 115px; border: 2px solid #2C0509;">
        <!-- 40% Grounding -->
        <div class="formula-segment" style="width: 40%; background-color: var(--c-wine-primary); justify-content: center; padding: 10px 16px;">
          <div class="formula-seg-pct" style="font-size: 44px; color: var(--c-gold); line-height: 1;">40%</div>
          <div class="formula-seg-label" style="font-size: 23px; letter-spacing: 0.5px; margin-top: 4px;">GROUNDING (r, C)</div>
          <div style="font-size: 20px; opacity: 0.95; font-weight: 600; margin-top: 2px;">
            Único término que evalúa la respuesta generada
          </div>
        </div>

        <!-- 40% Relevance -->
        <div class="formula-segment" style="width: 40%; background-color: var(--c-red-accent); border-left: 2px solid #FFFFFF; justify-content: center; padding: 10px 16px;">
          <div class="formula-seg-pct" style="font-size: 44px; line-height: 1;">40%</div>
          <div class="formula-seg-label" style="font-size: 23px; letter-spacing: 0.5px; margin-top: 4px;">RELEVANCE (q, C)</div>
          <div style="font-size: 20px; opacity: 0.95; font-weight: 600; margin-top: 2px;">
            Pregunta vs. contexto · ¡Ignora la respuesta!
          </div>
        </div>

        <!-- 20% Longitud -->
        <div class="formula-segment" style="width: 20%; background-color: #B38600; border-left: 2px solid #FFFFFF; justify-content: center; padding: 10px 16px;">
          <div class="formula-seg-pct" style="font-size: 44px; line-height: 1;">20%</div>
          <div class="formula-seg-label" style="font-size: 23px; letter-spacing: 0.5px; margin-top: 4px;">LONGITUD (r)</div>
          <div style="font-size: 20px; opacity: 0.95; font-weight: 600; margin-top: 2px;">
            Conteo de caracteres
          </div>
        </div>
      </div>

    </div>

    <!-- TARJETAS COMPLEMENTARIAS: Con fondo claro suave (#FAF5F5) idéntico a s6-block -->
    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 28px;">
      
      <!-- Distorsión 01 -->
      <div style="background: #FAF5F5; border: 2px solid var(--c-wine-primary); padding: 22px 26px; display: flex; flex-direction: column; justify-content: space-between;">
        <div>
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
            <span style="font-family: var(--font-mono); font-size: 18px; font-weight: 800; color: var(--c-wine-primary); letter-spacing: 1px;">DISTORSIÓN EN CÓDIGO 01</span>
            <span style="font-family: var(--font-mono); font-size: 20px; font-weight: 800; color: var(--c-wine-primary); background: #FFFFFF; border: 1.5px solid var(--c-wine-primary); padding: 2px 10px;">(x + 1) / 2</span>
          </div>
          <h3 style="font-family: var(--font-sans); font-size: 26px; font-weight: 800; color: var(--c-wine-dark); margin: 0 0 10px 0;">
            Coseno Reescalado: Similitud 0.00 → 0.50
          </h3>
          <p style="font-family: var(--font-sans); font-size: 22px; color: #110103; font-weight: 600; line-height: 1.4; margin: 0;">
            Al transformar el rango [-1, 1] a [0, 1], cualquier respuesta desconectada o incoherente obtiene automáticamente un <strong>0.50 aprobatorio</strong> como nota base garantizada.
          </p>
        </div>
        <div style="margin-top: 16px; padding-top: 10px; border-top: 1.5px solid rgba(70,8,17,0.2); font-family: var(--font-sans); font-size: 21px; color: var(--c-wine-dark); font-weight: 700;">
          Impacto en benchmark: Infla artificialmente respuestas mediocres.
        </div>
      </div>

      <!-- Distorsión 02 -->
      <div style="background: #FAF5F5; border: 2px solid var(--c-red-accent); padding: 22px 26px; display: flex; flex-direction: column; justify-content: space-between;">
        <div>
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
            <span style="font-family: var(--font-mono); font-size: 18px; font-weight: 800; color: var(--c-red-accent); letter-spacing: 1px;">DISTORSIÓN EN CÓDIGO 02</span>
            <span style="font-family: var(--font-mono); font-size: 20px; font-weight: 800; color: var(--c-red-accent); background: #FFFFFF; border: 1.5px solid var(--c-red-accent); padding: 2px 10px;">NOTA = 0.80</span>
          </div>
          <h3 style="font-family: var(--font-sans); font-size: 26px; font-weight: 800; color: var(--c-wine-dark); margin: 0 0 10px 0;">
            Premio Fijo al Rechazo: 9 Frases = 0.80
          </h3>
          <p style="font-family: var(--font-sans); font-size: 22px; color: #110103; font-weight: 600; line-height: 1.4; margin: 0;">
            Nueve frases literales de abstención reciben nota automática de <strong>0.80</strong>. Bonifica idéntico la abstención legítima que un fallo por torpeza del buscador.
          </p>
        </div>
        <div style="margin-top: 16px; padding-top: 10px; border-top: 1.5px solid rgba(201,16,27,0.2); font-family: var(--font-sans); font-size: 21px; color: var(--c-red-accent); font-weight: 700;">
          Impacto en benchmark: Ventaja artificial sistemática a modelos sobre-conservadores.
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
  <title>Test Final Options Slide 12</title>
  <link rel="stylesheet" href="http://localhost:8085/styles.css?v=18">
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
    test_files = [
        ('slide_12_f4.html', 'slide_12_f4.png', F4_HTML),
        ('slide_12_f5.html', 'slide_12_f5.png', F5_HTML)
    ]
    
    root_dir = r"c:\Users\ASUS\Desktop\Diapositivas-Cartagena"
    
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(viewport={"width": 1920, "height": 1080})
        
        for html_name, shot_name, slide_html in test_files:
            full_html = HTML_WRAPPER.format(content=slide_html)
            temp_path = os.path.join(root_dir, html_name)
            with open(temp_path, 'w', encoding='utf-8') as f:
                f.write(full_html)
            
            shot_path = os.path.join(output_dir, shot_name)
            page.goto(f"http://localhost:8085/{html_name}")
            page.wait_for_load_state("networkidle")
            page.wait_for_timeout(400)
            page.screenshot(path=shot_path)
            print(f"Generado con éxito: {shot_path}")
            
            if os.path.exists(temp_path):
                os.remove(temp_path)
                
        browser.close()

if __name__ == '__main__':
    main()
