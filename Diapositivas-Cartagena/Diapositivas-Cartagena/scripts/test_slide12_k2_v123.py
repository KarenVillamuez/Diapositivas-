# -*- coding: utf-8 -*-
"""
Script para generar y capturar 3 refinamientos específicos de K2 para Slide 12:
- K2-V1: Hero Bar Taller (145px), sin cajas anidadas (header integrado sin 'cuadro dentro de cuadro'),
         distribución vertical balanceada sin vacíos gigantes.
- K2-V2: Tarjetas horizontales con bloque lateral integrado (full-height pill sin cuadro interior),
         indicador 40% vs 60% simétrico arriba de la barra.
- K2-V3: Ultra-limpio minimalista: tarjetas planas directas de 2 líneas (título + métrica en negrita y 1 frase),
         barra de 150px con protagonismo absoluto.
"""
import os
from playwright.sync_api import sync_playwright

output_dir = r"C:\Users\ASUS\.gemini\antigravity-ide\brain\a6624504-511c-4b9d-bc9a-468e348bde40"
os.makedirs(output_dir, exist_ok=True)

# -----------------------------------------------------------------------------
# VARIANTE K2-V1: Balance Perfecto, Barra Hero (145px), Sin Cajas Anidadas
# -----------------------------------------------------------------------------
K2_V1_HTML = '''
<section class="slide s-white active" id="slide-12-k2-v1">
  <header class="slide-header">
    <div class="sh-left">
      <span class="sh-red-bar"></span>
      <span class="sh-category">03 · RESULTADOS · AUDITORÍA DE LA ECUACIÓN 1 (MÉTRICA Q)</span>
    </div>
    <img src="assets/image6.png" alt="#LoxTIC" class="sh-loxtic">
  </header>
  <div class="sh-divider"></div>

  <!-- Contenedor con distribución vertical equilibrada -->
  <div class="slide-content-area" style="justify-content: space-between; padding: 18px 0 10px 0;">
    
    <!-- Título Principal -->
    <h2 class="s-lead-question" style="font-size: 38px; font-weight: 800; margin: 0; line-height: 1.2;">
      Anatomía de la fórmula: la métrica califica al modelo sin leer su respuesta
    </h2>

    <!-- ZONA HERO CENTRAL: La Barra de la Figura 1 (145px) -->
    <div>
      
      <!-- Fila superior: Indicadores 40% vs 60% -->
      <div style="display: flex; width: 100%; margin-bottom: 8px; align-items: flex-end;">
        <div style="width: 40%; font-family: var(--font-sans); font-size: 21px; font-weight: 800; color: var(--c-wine-primary); padding-left: 4px;">
          ● 40% EVALÚA LA RESPUESTA
        </div>
        <div style="width: 60%; font-family: var(--font-sans); font-size: 21px; font-weight: 800; color: var(--c-red-accent); text-align: center; background: #FFE4E6; border: 1.5px solid var(--c-red-accent); padding: 4px 0;">
          ▼ ¡EL 60% DE LA NOTA NO EVALÚA EL CONTENIDO DE LA RESPUESTA!
        </div>
      </div>

      <!-- Barra Segmentada Oficial (145px de alto, esquinas 100% rectas) -->
      <div class="formula-segmented-bar" style="margin: 0; height: 145px; border: 2.5px solid #2C0509;">
        <!-- 40% Grounding -->
        <div class="formula-segment" style="width: 40%; background-color: var(--c-wine-primary); justify-content: center; padding: 12px 20px;">
          <div class="formula-seg-pct" style="font-size: 52px; color: var(--c-gold); line-height: 1;">40%</div>
          <div class="formula-seg-label" style="font-size: 24px; letter-spacing: 0.5px; margin-top: 6px;">GROUNDING (r, C)</div>
          <div style="font-size: 21px; opacity: 0.95; font-weight: 600; margin-top: 4px;">
            Único término que evalúa la respuesta generada
          </div>
        </div>

        <!-- 40% Relevance -->
        <div class="formula-segment" style="width: 40%; background-color: var(--c-red-accent); border-left: 2.5px solid #FFFFFF; justify-content: center; padding: 12px 20px;">
          <div class="formula-seg-pct" style="font-size: 52px; line-height: 1;">40%</div>
          <div class="formula-seg-label" style="font-size: 24px; letter-spacing: 0.5px; margin-top: 6px;">RELEVANCE (q, C)</div>
          <div style="font-size: 21px; opacity: 0.95; font-weight: 600; margin-top: 4px;">
            Pregunta vs. contexto · ¡Ignora la respuesta!
          </div>
        </div>

        <!-- 20% Longitud -->
        <div class="formula-segment" style="width: 20%; background-color: #B38600; border-left: 2.5px solid #FFFFFF; justify-content: center; padding: 12px 20px;">
          <div class="formula-seg-pct" style="font-size: 52px; line-height: 1;">20%</div>
          <div class="formula-seg-label" style="font-size: 24px; letter-spacing: 0.5px; margin-top: 6px;">LONGITUD (r)</div>
          <div style="font-size: 21px; opacity: 0.95; font-weight: 600; margin-top: 4px;">
            Conteo de caracteres
          </div>
        </div>
      </div>

      <!-- Fórmula matemática discreta debajo de la barra -->
      <div style="font-family: var(--font-mono); font-size: 20px; font-weight: 700; color: #555555; margin-top: 8px; text-align: center;">
        Q(r, q, C) = 0.40·grounding(r, C) + 0.40·relevance(q, C) + 0.20·length(r)
      </div>

    </div>

    <!-- TARJETAS COMPLEMENTARIAS: Sin cuadros anidados, cabecera limpia -->
    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 28px;">
      
      <!-- Distorsión 01 -->
      <div style="background: #FAF5F5; border: 2px solid var(--c-wine-primary); padding: 18px 24px;">
        <div style="display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 6px;">
          <span style="font-family: var(--font-sans); font-size: 24px; font-weight: 800; color: var(--c-wine-dark);">
            Coseno Reescalado: (x + 1)/2
          </span>
          <span style="font-family: var(--font-mono); font-size: 24px; font-weight: 800; color: var(--c-wine-primary);">
            0.00 → 0.50
          </span>
        </div>
        <p style="font-family: var(--font-sans); font-size: 22px; color: #110103; font-weight: 600; line-height: 1.35; margin: 0;">
          Una similitud nula se convierte en nota aprobatoria de <strong>0.50</strong>, inflando respuestas desconectadas del libro.
        </p>
      </div>

      <!-- Distorsión 02 -->
      <div style="background: #FAF5F5; border: 2px solid var(--c-red-accent); padding: 18px 24px;">
        <div style="display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 6px;">
          <span style="font-family: var(--font-sans); font-size: 24px; font-weight: 800; color: var(--c-wine-dark);">
            Premio al Rechazo: 9 Frases
          </span>
          <span style="font-family: var(--font-mono); font-size: 24px; font-weight: 800; color: var(--c-red-accent);">
            Nota = 0.80
          </span>
        </div>
        <p style="font-family: var(--font-sans); font-size: 22px; color: #110103; font-weight: 600; line-height: 1.35; margin: 0;">
          Nueve frases fijas reciben <strong>0.80 automático</strong>, dando ventaja artificial a modelos que rehúyen responder.
        </p>
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
# VARIANTE K2-V2: Tarjetas Horizontales con Bloque de Color Integrado (Sin anidar)
# -----------------------------------------------------------------------------
K2_V2_HTML = '''
<section class="slide s-white active" id="slide-12-k2-v2">
  <header class="slide-header">
    <div class="sh-left">
      <span class="sh-red-bar"></span>
      <span class="sh-category">03 · RESULTADOS · AUDITORÍA DE LA ECUACIÓN 1 (MÉTRICA Q)</span>
    </div>
    <img src="assets/image6.png" alt="#LoxTIC" class="sh-loxtic">
  </header>
  <div class="sh-divider"></div>

  <!-- Contenedor Centrado Verticalmente -->
  <div class="slide-content-area" style="justify-content: center; gap: 36px; padding: 0;">
    
    <!-- Título Principal -->
    <h2 class="s-lead-question" style="font-size: 38px; font-weight: 800; margin: 0; line-height: 1.2;">
      Anatomía de la fórmula: la métrica califica al modelo sin leer su respuesta
    </h2>

    <!-- EL FOCO PRINCIPAL: Gráfica Centrada (135px de altura) -->
    <div>
      
      <!-- Fila superior de contraste -->
      <div style="display: flex; width: 100%; margin-bottom: 8px; align-items: flex-end;">
        <div style="width: 40%; font-family: var(--font-mono); font-size: 22px; font-weight: 700; color: var(--c-wine-primary); padding-left: 4px;">
          Q(r, q, C) = 0.40·G + 0.40·R + 0.20·L
        </div>
        <div style="width: 60%; font-family: var(--font-sans); font-size: 21px; font-weight: 800; color: var(--c-red-accent); text-align: center; background: #FFE4E6; border: 1.5px solid var(--c-red-accent); padding: 4px 0;">
          ▼ ¡EL 60% DE LA NOTA NO EVALÚA EL CONTENIDO DE LA RESPUESTA!
        </div>
      </div>

      <!-- Barra Segmentada Oficial (135px de alto) -->
      <div class="formula-segmented-bar" style="margin: 0; height: 135px; border: 2.5px solid #2C0509;">
        <!-- 40% Grounding -->
        <div class="formula-segment" style="width: 40%; background-color: var(--c-wine-primary); justify-content: center; padding: 10px 18px;">
          <div class="formula-seg-pct" style="font-size: 50px; color: var(--c-gold); line-height: 1;">40%</div>
          <div class="formula-seg-label" style="font-size: 24px; letter-spacing: 0.5px; margin-top: 4px;">GROUNDING (r, C)</div>
          <div style="font-size: 20px; opacity: 0.95; font-weight: 600; margin-top: 3px;">
            Único término que evalúa la respuesta generada
          </div>
        </div>

        <!-- 40% Relevance -->
        <div class="formula-segment" style="width: 40%; background-color: var(--c-red-accent); border-left: 2.5px solid #FFFFFF; justify-content: center; padding: 10px 18px;">
          <div class="formula-seg-pct" style="font-size: 50px; line-height: 1;">40%</div>
          <div class="formula-seg-label" style="font-size: 24px; letter-spacing: 0.5px; margin-top: 4px;">RELEVANCE (q, C)</div>
          <div style="font-size: 20px; opacity: 0.95; font-weight: 600; margin-top: 3px;">
            Pregunta vs. contexto · ¡Ignora la respuesta!
          </div>
        </div>

        <!-- 20% Longitud -->
        <div class="formula-segment" style="width: 20%; background-color: #B38600; border-left: 2.5px solid #FFFFFF; justify-content: center; padding: 10px 18px;">
          <div class="formula-seg-pct" style="font-size: 50px; line-height: 1;">20%</div>
          <div class="formula-seg-label" style="font-size: 24px; letter-spacing: 0.5px; margin-top: 4px;">LONGITUD (r)</div>
          <div style="font-size: 20px; opacity: 0.95; font-weight: 600; margin-top: 3px;">
            Conteo de caracteres
          </div>
        </div>
      </div>

    </div>

    <!-- TARJETAS CON COLUMNA LATERAL INTEGRADA (Sin cuadros anidados dentro del contenido) -->
    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 28px;">
      
      <!-- Píldora 1 -->
      <div style="background: #FFFFFF; border: 2px solid var(--c-wine-primary); display: flex; align-items: stretch;">
        <div style="background: var(--c-wine-primary); color: #FFFFFF; font-family: var(--font-mono); font-size: 24px; font-weight: 800; padding: 16px 18px; display: flex; align-items: center; justify-content: center; white-space: nowrap;">
          0.00 → 0.50
        </div>
        <div style="padding: 16px 20px; display: flex; flex-direction: column; justify-content: center;">
          <div style="font-family: var(--font-sans); font-size: 22px; font-weight: 800; color: var(--c-wine-dark); margin-bottom: 2px;">
            Coseno Reescalado (x + 1)/2
          </div>
          <div style="font-family: var(--font-sans); font-size: 21px; color: #110103; font-weight: 600; line-height: 1.3;">
            Respuestas desconectadas del libro obtienen 0.50 aprobado como base garantizada.
          </div>
        </div>
      </div>

      <!-- Píldora 2 -->
      <div style="background: #FFFFFF; border: 2px solid var(--c-red-accent); display: flex; align-items: stretch;">
        <div style="background: var(--c-red-accent); color: #FFFFFF; font-family: var(--font-mono); font-size: 24px; font-weight: 800; padding: 16px 18px; display: flex; align-items: center; justify-content: center; white-space: nowrap;">
          Nota = 0.80
        </div>
        <div style="padding: 16px 20px; display: flex; flex-direction: column; justify-content: center;">
          <div style="font-family: var(--font-sans); font-size: 22px; font-weight: 800; color: var(--c-wine-dark); margin-bottom: 2px;">
            Premio al Rechazo (9 Frases)
          </div>
          <div style="font-family: var(--font-sans); font-size: 21px; color: #110103; font-weight: 600; line-height: 1.3;">
            Nueve frases fijas reciben 0.80 directo, premiando a modelos que rehúyen responder.
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
# VARIANTE K2-V3: Ultra-Limpio, Barra Gigante (155px), Tarjetas Directas 1 Frase
# -----------------------------------------------------------------------------
K2_V3_HTML = '''
<section class="slide s-white active" id="slide-12-k2-v3">
  <header class="slide-header">
    <div class="sh-left">
      <span class="sh-red-bar"></span>
      <span class="sh-category">03 · RESULTADOS · AUDITORÍA DE LA ECUACIÓN 1 (MÉTRICA Q)</span>
    </div>
    <img src="assets/image6.png" alt="#LoxTIC" class="sh-loxtic">
  </header>
  <div class="sh-divider"></div>

  <!-- Contenedor Centrado Vertical con gap proporcionado -->
  <div class="slide-content-area" style="justify-content: center; gap: 32px; padding: 0;">
    
    <!-- Título Principal -->
    <h2 class="s-lead-question" style="font-size: 40px; font-weight: 800; margin: 0; line-height: 1.2;">
      Anatomía de la fórmula: la métrica califica al modelo sin leer su respuesta
    </h2>

    <!-- EL FOCO HERO MÁXIMO: Barra de 155px -->
    <div>
      
      <!-- Fila superior -->
      <div style="display: flex; width: 100%; margin-bottom: 10px; align-items: flex-end;">
        <div style="width: 40%; font-family: var(--font-sans); font-size: 22px; font-weight: 800; color: var(--c-wine-primary); padding-left: 4px;">
          ● 40% EVALÚA FIDELIDAD SEMÁNTICA
        </div>
        <div style="width: 60%; font-family: var(--font-sans); font-size: 22px; font-weight: 800; color: var(--c-red-accent); text-align: center; background: #FFE4E6; border: 1.5px solid var(--c-red-accent); padding: 5px 0;">
          ▼ ¡EL 60% DE LA NOTA NO EVALÚA EL CONTENIDO DE LA RESPUESTA!
        </div>
      </div>

      <!-- Barra Segmentada Oficial (155px de alto) -->
      <div class="formula-segmented-bar" style="margin: 0; height: 155px; border: 2.5px solid #2C0509;">
        <!-- 40% Grounding -->
        <div class="formula-segment" style="width: 40%; background-color: var(--c-wine-primary); justify-content: center; padding: 12px 20px;">
          <div class="formula-seg-pct" style="font-size: 56px; color: var(--c-gold); line-height: 1;">40%</div>
          <div class="formula-seg-label" style="font-size: 26px; letter-spacing: 0.5px; margin-top: 6px;">GROUNDING (r, C)</div>
          <div style="font-size: 22px; opacity: 0.95; font-weight: 600; margin-top: 4px;">
            Único término que evalúa la respuesta generada
          </div>
        </div>

        <!-- 40% Relevance -->
        <div class="formula-segment" style="width: 40%; background-color: var(--c-red-accent); border-left: 2.5px solid #FFFFFF; justify-content: center; padding: 12px 20px;">
          <div class="formula-seg-pct" style="font-size: 56px; line-height: 1;">40%</div>
          <div class="formula-seg-label" style="font-size: 26px; letter-spacing: 0.5px; margin-top: 6px;">RELEVANCE (q, C)</div>
          <div style="font-size: 22px; opacity: 0.95; font-weight: 600; margin-top: 4px;">
            Pregunta vs. contexto · ¡Ignora la respuesta!
          </div>
        </div>

        <!-- 20% Longitud -->
        <div class="formula-segment" style="width: 20%; background-color: #B38600; border-left: 2.5px solid #FFFFFF; justify-content: center; padding: 12px 20px;">
          <div class="formula-seg-pct" style="font-size: 56px; line-height: 1;">20%</div>
          <div class="formula-seg-label" style="font-size: 26px; letter-spacing: 0.5px; margin-top: 6px;">LONGITUD (r)</div>
          <div style="font-size: 22px; opacity: 0.95; font-weight: 600; margin-top: 4px;">
            Conteo de caracteres
          </div>
        </div>
      </div>

    </div>

    <!-- TARJETAS MINIMALISTAS: 1 sola línea de título + 1 línea de texto grande -->
    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 28px;">
      
      <!-- Distorsión 01 -->
      <div style="background: #FFFFFF; border: 2.5px solid var(--c-wine-primary); padding: 18px 24px;">
        <div style="font-family: var(--font-sans); font-size: 24px; font-weight: 800; color: var(--c-wine-primary); margin-bottom: 6px;">
          Coseno Reescalado (x + 1)/2 &nbsp;·&nbsp; <span style="font-family: var(--font-mono);">0.00 → 0.50</span>
        </div>
        <div style="font-family: var(--font-sans); font-size: 22px; color: #110103; font-weight: 600; line-height: 1.35;">
          Respuestas sin ninguna relación con el libro obtienen <strong>0.50 aprobatorio</strong> como nota garantizada.
        </div>
      </div>

      <!-- Distorsión 02 -->
      <div style="background: #FFFFFF; border: 2.5px solid var(--c-red-accent); padding: 18px 24px;">
        <div style="font-family: var(--font-sans); font-size: 24px; font-weight: 800; color: var(--c-red-accent); margin-bottom: 6px;">
          Premio al Rechazo &nbsp;·&nbsp; <span style="font-family: var(--font-mono);">9 Frases = 0.80</span>
        </div>
        <div style="font-family: var(--font-sans); font-size: 22px; color: #110103; font-weight: 600; line-height: 1.35;">
          Nueve frases fijas de abstención reciben <strong>0.80 automático</strong>, dando ventaja a modelos que no arriesgan.
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
  <title>Test K2 Refinements V1-V3</title>
  <link rel="stylesheet" href="http://localhost:8085/styles.css?v=20">
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
        ('slide_12_k2_v1.html', 'slide_12_k2_v1.png', K2_V1_HTML),
        ('slide_12_k2_v2.html', 'slide_12_k2_v2.png', K2_V2_HTML),
        ('slide_12_k2_v3.html', 'slide_12_k2_v3.png', K2_V3_HTML),
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
