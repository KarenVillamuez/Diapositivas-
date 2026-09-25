# -*- coding: utf-8 -*-
"""
Script para generar las variantes definitivas de Slide 12 combinando:
1. Punteros de K2.4 (cuidando tamaños de texto >= 23px-25px, alto contraste).
2. Distribución horizontal de tarjetas de K2.2 (columna métrica a la izquierda + texto a la derecha).
3. SIN fondos oscuros con letras claras en tarjetas ni punteros (fondo claro con texto oscuro y nítido).
4. Solución definitiva al bug de flex-shrink/overflow: columnas laterales con ancho explícito (flex: 0 0 210px) y padding holgado.
"""
import os
from playwright.sync_api import sync_playwright

output_dir = r"C:\Users\ASUS\.gemini\antigravity-ide\brain\a6624504-511c-4b9d-bc9a-468e348bde40"
os.makedirs(output_dir, exist_ok=True)

# -----------------------------------------------------------------------------
# VARIANTE P1: Columna lateral en tono suave (#FAF0F2 / #FFF0F4) con texto oscuro
# -----------------------------------------------------------------------------
P1_HTML = '''
<section class="slide s-white active" id="slide-12-p1">
  <header class="slide-header">
    <div class="sh-left">
      <span class="sh-red-bar"></span>
      <span class="sh-category">03 · RESULTADOS · AUDITORÍA DE LA ECUACIÓN 1 (MÉTRICA Q)</span>
    </div>
    <img src="assets/image6.png" alt="#LoxTIC" class="sh-loxtic">
  </header>
  <div class="sh-divider"></div>

  <!-- Contenedor con distribución vertical natural y equilibrada -->
  <div class="slide-content-area" style="justify-content: space-between; padding: 14px 0 6px 0;">
    
    <!-- Título Principal -->
    <h2 class="s-lead-question" style="font-size: 38px; font-weight: 800; margin: 0; line-height: 1.2;">
      Anatomía de la fórmula: la métrica califica al modelo sin leer su respuesta
    </h2>

    <!-- ZONA HERO CENTRAL: Punteros K2.4 + Barra Segmentada -->
    <div>
      
      <!-- Punteros K2.4 con textos grandes, fondo blanco y alto contraste -->
      <div style="display: flex; width: 100%; margin-bottom: 10px; align-items: flex-end;">
        <!-- Puntero Grounding (40%) -->
        <div style="width: 40%; font-family: var(--font-mono); font-size: 23px; font-weight: 800; color: var(--c-wine-dark); padding-left: 6px;">
          Q = 0.40·G + 0.40·R + 0.20·L
        </div>

        <!-- Puntero Relevance (40%) -->
        <div style="width: 40%; font-family: var(--font-sans); font-size: 24px; font-weight: 800; color: var(--c-red-accent); text-align: center; line-height: 1.2;">
          <span style="font-size: 26px;">▼</span> ¡La respuesta NO entra aquí! (40%)
        </div>

        <!-- Puntero Longitud (20%) -->
        <div style="width: 20%; font-family: var(--font-sans); font-size: 23px; font-weight: 800; color: #7A5000; text-align: center; line-height: 1.2;">
          <span style="font-size: 26px;">▼</span> Solo caracteres (20%)
        </div>
      </div>

      <!-- Barra Segmentada Oficial (142px de alto, esquinas rectas) -->
      <div class="formula-segmented-bar" style="margin: 0; height: 142px; border: 2.5px solid #2C0509;">
        <!-- 40% Grounding -->
        <div class="formula-segment" style="width: 40%; background-color: var(--c-wine-primary); justify-content: center; padding: 12px 20px;">
          <div class="formula-seg-pct" style="font-size: 52px; color: var(--c-gold); line-height: 1;">40%</div>
          <div class="formula-seg-label" style="font-size: 24px; letter-spacing: 0.5px; margin-top: 5px;">GROUNDING (r, C)</div>
          <div style="font-size: 21px; opacity: 0.95; font-weight: 600; margin-top: 4px;">
            Único término que evalúa la respuesta generada
          </div>
        </div>

        <!-- 40% Relevance -->
        <div class="formula-segment" style="width: 40%; background-color: var(--c-red-accent); border-left: 2.5px solid #FFFFFF; justify-content: center; padding: 12px 20px;">
          <div class="formula-seg-pct" style="font-size: 52px; line-height: 1;">40%</div>
          <div class="formula-seg-label" style="font-size: 24px; letter-spacing: 0.5px; margin-top: 5px;">RELEVANCE (q, C)</div>
          <div style="font-size: 21px; opacity: 0.95; font-weight: 600; margin-top: 4px;">
            Pregunta vs. contexto · ¡Ignora la respuesta!
          </div>
        </div>

        <!-- 20% Longitud -->
        <div class="formula-segment" style="width: 20%; background-color: #B38600; border-left: 2.5px solid #FFFFFF; justify-content: center; padding: 12px 20px;">
          <div class="formula-seg-pct" style="font-size: 52px; line-height: 1;">20%</div>
          <div class="formula-seg-label" style="font-size: 24px; letter-spacing: 0.5px; margin-top: 5px;">LONGITUD (r)</div>
          <div style="font-size: 21px; opacity: 0.95; font-weight: 600; margin-top: 4px;">
            Conteo de caracteres
          </div>
        </div>
      </div>

      <!-- Fórmula formal compacta debajo de la barra -->
      <div style="font-family: var(--font-mono); font-size: 20px; font-weight: 700; color: #555555; margin-top: 8px; text-align: center;">
        Q(r, q, C) = 0.40·grounding(r, C) + 0.40·relevance(q, C) + 0.20·length(r)
      </div>

    </div>

    <!-- TARJETAS CON DISTRIBUCIÓN K2.2: FONDO CLARO CON TEXTO OSCURO DE ALTO CONTRASTE -->
    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 28px;">
      
      <!-- Tarjeta 1: Coseno Reescalado -->
      <div style="background: #FFFFFF; border: 2.5px solid var(--c-wine-primary); display: flex; align-items: stretch;">
        <!-- Columna lateral integrada: Fondo suave vino (#FAF0F2), texto vino oscuro de 26px -->
        <div style="flex: 0 0 215px; background: #FAF0F2; border-right: 2.5px solid var(--c-wine-primary); color: var(--c-wine-dark); font-family: var(--font-mono); font-size: 26px; font-weight: 800; display: flex; align-items: center; justify-content: center; white-space: nowrap; padding: 14px 10px;">
          0.00 → 0.50
        </div>
        <!-- Contenido principal: Título 24px + Frase técnica 22px -->
        <div style="flex: 1; padding: 16px 22px; display: flex; flex-direction: column; justify-content: center;">
          <div style="font-family: var(--font-sans); font-size: 24px; font-weight: 800; color: var(--c-wine-dark); margin-bottom: 3px;">
            Coseno Reescalado: (x + 1)/2
          </div>
          <div style="font-family: var(--font-sans); font-size: 22px; color: #110103; font-weight: 600; line-height: 1.35;">
            Respuestas desconectadas del libro obtienen <strong>0.50 aprobado</strong> como piso garantizado.
          </div>
        </div>
      </div>

      <!-- Tarjeta 2: Premio al Rechazo -->
      <div style="background: #FFFFFF; border: 2.5px solid var(--c-red-accent); display: flex; align-items: stretch;">
        <!-- Columna lateral integrada: Fondo suave rojo (#FFF0F4), texto rojo oscuro de 26px -->
        <div style="flex: 0 0 215px; background: #FFF0F4; border-right: 2.5px solid var(--c-red-accent); color: var(--c-red-accent); font-family: var(--font-mono); font-size: 26px; font-weight: 800; display: flex; align-items: center; justify-content: center; white-space: nowrap; padding: 14px 10px;">
          Nota = 0.80
        </div>
        <!-- Contenido principal: Título 24px + Frase técnica 22px -->
        <div style="flex: 1; padding: 16px 22px; display: flex; flex-direction: column; justify-content: center;">
          <div style="font-family: var(--font-sans); font-size: 24px; font-weight: 800; color: var(--c-wine-dark); margin-bottom: 3px;">
            Premio al Rechazo (9 Frases)
          </div>
          <div style="font-family: var(--font-sans); font-size: 22px; color: #110103; font-weight: 600; line-height: 1.35;">
            Nueve frases fijas reciben <strong>0.80 directo</strong>, premiando a modelos que rehúyen responder.
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
# VARIANTE P2: Columna lateral en blanco puro (#FFFFFF) con fondo general #FAF5F5
# -----------------------------------------------------------------------------
P2_HTML = '''
<section class="slide s-white active" id="slide-12-p2">
  <header class="slide-header">
    <div class="sh-left">
      <span class="sh-red-bar"></span>
      <span class="sh-category">03 · RESULTADOS · AUDITORÍA DE LA ECUACIÓN 1 (MÉTRICA Q)</span>
    </div>
    <img src="assets/image6.png" alt="#LoxTIC" class="sh-loxtic">
  </header>
  <div class="sh-divider"></div>

  <div class="slide-content-area" style="justify-content: space-between; padding: 14px 0 6px 0;">
    
    <h2 class="s-lead-question" style="font-size: 38px; font-weight: 800; margin: 0; line-height: 1.2;">
      Anatomía de la fórmula: la métrica califica al modelo sin leer su respuesta
    </h2>

    <div>
      <!-- Punteros K2.4 con etiquetas descriptivas completas -->
      <div style="display: flex; width: 100%; margin-bottom: 10px; align-items: flex-end;">
        <div style="width: 40%; font-family: var(--font-sans); font-size: 23px; font-weight: 800; color: var(--c-wine-dark); padding-left: 6px;">
          ● 40% Evalúa fidelidad semántica
        </div>

        <div style="width: 40%; font-family: var(--font-sans); font-size: 24px; font-weight: 800; color: var(--c-red-accent); text-align: center;">
          ▼ ¡Aquí la respuesta NO es dato de entrada!
        </div>

        <div style="width: 20%; font-family: var(--font-sans); font-size: 23px; font-weight: 800; color: #7A5000; text-align: center;">
          ▼ Solo caracteres
        </div>
      </div>

      <!-- Barra Segmentada Oficial (142px) -->
      <div class="formula-segmented-bar" style="margin: 0; height: 142px; border: 2.5px solid #2C0509;">
        <div class="formula-segment" style="width: 40%; background-color: var(--c-wine-primary); justify-content: center; padding: 12px 20px;">
          <div class="formula-seg-pct" style="font-size: 52px; color: var(--c-gold); line-height: 1;">40%</div>
          <div class="formula-seg-label" style="font-size: 24px; letter-spacing: 0.5px; margin-top: 5px;">GROUNDING (r, C)</div>
          <div style="font-size: 21px; opacity: 0.95; font-weight: 600; margin-top: 4px;">
            Único término que evalúa la respuesta generada
          </div>
        </div>

        <div class="formula-segment" style="width: 40%; background-color: var(--c-red-accent); border-left: 2.5px solid #FFFFFF; justify-content: center; padding: 12px 20px;">
          <div class="formula-seg-pct" style="font-size: 52px; line-height: 1;">40%</div>
          <div class="formula-seg-label" style="font-size: 24px; letter-spacing: 0.5px; margin-top: 5px;">RELEVANCE (q, C)</div>
          <div style="font-size: 21px; opacity: 0.95; font-weight: 600; margin-top: 4px;">
            Pregunta vs. contexto · ¡Ignora la respuesta!
          </div>
        </div>

        <div class="formula-segment" style="width: 20%; background-color: #B38600; border-left: 2.5px solid #FFFFFF; justify-content: center; padding: 12px 20px;">
          <div class="formula-seg-pct" style="font-size: 52px; line-height: 1;">20%</div>
          <div class="formula-seg-label" style="font-size: 24px; letter-spacing: 0.5px; margin-top: 5px;">LONGITUD (r)</div>
          <div style="font-size: 21px; opacity: 0.95; font-weight: 600; margin-top: 4px;">
            Conteo de caracteres
          </div>
        </div>
      </div>

      <div style="font-family: var(--font-mono); font-size: 20px; font-weight: 700; color: #555555; margin-top: 8px; text-align: center;">
        Q(r, q, C) = 0.40·grounding(r, C) + 0.40·relevance(q, C) + 0.20·length(r)
      </div>
    </div>

    <!-- TARJETAS K2.2 CON FONDO GENERAL #FAF5F5 Y COLUMNA BLANCA -->
    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 28px;">
      
      <!-- Tarjeta 1 -->
      <div style="background: #FAF5F5; border: 2.5px solid var(--c-wine-primary); display: flex; align-items: stretch;">
        <div style="flex: 0 0 215px; background: #FFFFFF; border-right: 2.5px solid var(--c-wine-primary); color: var(--c-wine-primary); font-family: var(--font-mono); font-size: 26px; font-weight: 800; display: flex; align-items: center; justify-content: center; white-space: nowrap; padding: 14px 10px;">
          0.00 → 0.50
        </div>
        <div style="flex: 1; padding: 16px 22px; display: flex; flex-direction: column; justify-content: center;">
          <div style="font-family: var(--font-sans); font-size: 24px; font-weight: 800; color: var(--c-wine-dark); margin-bottom: 3px;">
            Coseno Reescalado: (x + 1)/2
          </div>
          <div style="font-family: var(--font-sans); font-size: 22px; color: #110103; font-weight: 600; line-height: 1.35;">
            Respuestas desconectadas del libro obtienen <strong>0.50 aprobado</strong> como piso garantizado.
          </div>
        </div>
      </div>

      <!-- Tarjeta 2 -->
      <div style="background: #FAF5F5; border: 2.5px solid var(--c-red-accent); display: flex; align-items: stretch;">
        <div style="flex: 0 0 215px; background: #FFFFFF; border-right: 2.5px solid var(--c-red-accent); color: var(--c-red-accent); font-family: var(--font-mono); font-size: 26px; font-weight: 800; display: flex; align-items: center; justify-content: center; white-space: nowrap; padding: 14px 10px;">
          Nota = 0.80
        </div>
        <div style="flex: 1; padding: 16px 22px; display: flex; flex-direction: column; justify-content: center;">
          <div style="font-family: var(--font-sans); font-size: 24px; font-weight: 800; color: var(--c-wine-dark); margin-bottom: 3px;">
            Premio al Rechazo (9 Frases)
          </div>
          <div style="font-family: var(--font-sans); font-size: 22px; color: #110103; font-weight: 600; line-height: 1.35;">
            Nueve frases fijas reciben <strong>0.80 directo</strong>, premiando a modelos que rehúyen responder.
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
# VARIANTE P3: Punteros idénticos a Figura 1 del paper + Barra 148px
# -----------------------------------------------------------------------------
P3_HTML = '''
<section class="slide s-white active" id="slide-12-p3">
  <header class="slide-header">
    <div class="sh-left">
      <span class="sh-red-bar"></span>
      <span class="sh-category">03 · RESULTADOS · AUDITORÍA DE LA ECUACIÓN 1 (MÉTRICA Q)</span>
    </div>
    <img src="assets/image6.png" alt="#LoxTIC" class="sh-loxtic">
  </header>
  <div class="sh-divider"></div>

  <div class="slide-content-area" style="justify-content: space-between; padding: 14px 0 6px 0;">
    
    <h2 class="s-lead-question" style="font-size: 38px; font-weight: 800; margin: 0; line-height: 1.2;">
      Anatomía de la fórmula: la métrica califica al modelo sin leer su respuesta
    </h2>

    <div>
      <!-- Punteros K2.4 fieles a Figura 1 -->
      <div style="display: flex; width: 100%; margin-bottom: 10px; align-items: flex-end;">
        <div style="width: 40%; font-family: var(--font-mono); font-size: 23px; font-weight: 800; color: var(--c-wine-dark); padding-left: 6px;">
          Q = 0.40·G + 0.40·R + 0.20·L
        </div>

        <div style="width: 40%; font-family: var(--font-sans); font-size: 24px; font-weight: 800; color: var(--c-red-accent); text-align: center;">
          <span style="font-size: 26px;">▼</span> ¡Aquí la respuesta NO es un dato de entrada!
        </div>

        <div style="width: 20%; font-family: var(--font-sans); font-size: 23px; font-weight: 800; color: #7A5000; text-align: center;">
          <span style="font-size: 26px;">▼</span> Solo caracteres
        </div>
      </div>

      <!-- Barra Segmentada Oficial (148px) -->
      <div class="formula-segmented-bar" style="margin: 0; height: 148px; border: 2.5px solid #2C0509;">
        <div class="formula-segment" style="width: 40%; background-color: var(--c-wine-primary); justify-content: center; padding: 12px 20px;">
          <div class="formula-seg-pct" style="font-size: 54px; color: var(--c-gold); line-height: 1;">40%</div>
          <div class="formula-seg-label" style="font-size: 25px; letter-spacing: 0.5px; margin-top: 5px;">GROUNDING (r, C)</div>
          <div style="font-size: 21px; opacity: 0.95; font-weight: 600; margin-top: 4px;">
            Único término que evalúa la respuesta generada
          </div>
        </div>

        <div class="formula-segment" style="width: 40%; background-color: var(--c-red-accent); border-left: 2.5px solid #FFFFFF; justify-content: center; padding: 12px 20px;">
          <div class="formula-seg-pct" style="font-size: 54px; line-height: 1;">40%</div>
          <div class="formula-seg-label" style="font-size: 25px; letter-spacing: 0.5px; margin-top: 5px;">RELEVANCE (q, C)</div>
          <div style="font-size: 21px; opacity: 0.95; font-weight: 600; margin-top: 4px;">
            Pregunta vs. contexto · ¡Ignora la respuesta!
          </div>
        </div>

        <div class="formula-segment" style="width: 20%; background-color: #B38600; border-left: 2.5px solid #FFFFFF; justify-content: center; padding: 12px 20px;">
          <div class="formula-seg-pct" style="font-size: 54px; line-height: 1;">20%</div>
          <div class="formula-seg-label" style="font-size: 25px; letter-spacing: 0.5px; margin-top: 5px;">LONGITUD (r)</div>
          <div style="font-size: 21px; opacity: 0.95; font-weight: 600; margin-top: 4px;">
            Conteo de caracteres
          </div>
        </div>
      </div>

      <div style="font-family: var(--font-mono); font-size: 20px; font-weight: 700; color: #555555; margin-top: 8px; text-align: center;">
        Q(r, q, C) = 0.40·grounding(r, C) + 0.40·relevance(q, C) + 0.20·length(r)
      </div>
    </div>

    <!-- TARJETAS K2.2 CON FONDO BLANCO PURO Y BORDE SUAVE ENTRE COLUMNAS -->
    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 28px;">
      
      <!-- Tarjeta 1 -->
      <div style="background: #FFFFFF; border: 2.5px solid var(--c-wine-primary); display: flex; align-items: stretch;">
        <div style="flex: 0 0 215px; border-right: 2px solid rgba(70,8,17,0.25); color: var(--c-wine-primary); font-family: var(--font-mono); font-size: 26px; font-weight: 800; display: flex; align-items: center; justify-content: center; white-space: nowrap; padding: 14px 10px;">
          0.00 → 0.50
        </div>
        <div style="flex: 1; padding: 16px 22px; display: flex; flex-direction: column; justify-content: center;">
          <div style="font-family: var(--font-sans); font-size: 24px; font-weight: 800; color: var(--c-wine-dark); margin-bottom: 3px;">
            Coseno Reescalado: (x + 1)/2
          </div>
          <div style="font-family: var(--font-sans); font-size: 22px; color: #110103; font-weight: 600; line-height: 1.35;">
            Respuestas desconectadas del libro obtienen <strong>0.50 aprobado</strong> como piso garantizado.
          </div>
        </div>
      </div>

      <!-- Tarjeta 2 -->
      <div style="background: #FFFFFF; border: 2.5px solid var(--c-red-accent); display: flex; align-items: stretch;">
        <div style="flex: 0 0 215px; border-right: 2px solid rgba(201,16,27,0.25); color: var(--c-red-accent); font-family: var(--font-mono); font-size: 26px; font-weight: 800; display: flex; align-items: center; justify-content: center; white-space: nowrap; padding: 14px 10px;">
          Nota = 0.80
        </div>
        <div style="flex: 1; padding: 16px 22px; display: flex; flex-direction: column; justify-content: center;">
          <div style="font-family: var(--font-sans); font-size: 24px; font-weight: 800; color: var(--c-wine-dark); margin-bottom: 3px;">
            Premio al Rechazo (9 Frases)
          </div>
          <div style="font-family: var(--font-sans); font-size: 22px; color: #110103; font-weight: 600; line-height: 1.35;">
            Nueve frases fijas reciben <strong>0.80 directo</strong>, premiando a modelos que rehúyen responder.
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
  <title>Test Final K2 Combinations</title>
  <link rel="stylesheet" href="http://localhost:8085/styles.css?v=23">
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
        ('slide_12_p1.html', 'slide_12_p1.png', P1_HTML),
        ('slide_12_p2.html', 'slide_12_p2.png', P2_HTML),
        ('slide_12_p3.html', 'slide_12_p3.png', P3_HTML),
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
            page.wait_for_timeout(500)
            page.screenshot(path=png_path)
            print(f"Captured: {png_name}")

        browser.close()

if __name__ == '__main__':
    main()
