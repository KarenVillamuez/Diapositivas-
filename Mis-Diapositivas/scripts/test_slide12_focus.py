# -*- coding: utf-8 -*-
"""
Generación de 3 variantes con esquinas rectas (estilo nativo slide_12.html),
foco principal evidente (Figura 1 / 60% ciego) y descongestión de elementos.
"""
import os
from playwright.sync_api import sync_playwright

output_dir = r"C:\Users\ASUS\.gemini\antigravity-ide\brain\a6624504-511c-4b9d-bc9a-468e348bde40"
os.makedirs(output_dir, exist_ok=True)

# -----------------------------------------------------------------------------
# VARIANTE F1: Puntero Directo Figura 1 sobre la Barra Recta Oficial
# -----------------------------------------------------------------------------
F1_HTML = '''
<section class="slide s-white active" id="slide-12-f1">
  <header class="slide-header">
    <div class="sh-left">
      <span class="sh-red-bar"></span>
      <span class="sh-category">03 · RESULTADOS · AUDITORÍA DE LA MÉTRICA AUTOMÁTICA</span>
    </div>
    <img src="assets/image6.png" alt="#LoxTIC" class="sh-loxtic">
  </header>
  <div class="sh-divider"></div>

  <div class="slide-content-area" style="justify-content: flex-start; padding-top: 10px;">
    <!-- Pregunta Rectora concisa -->
    <h2 class="s-lead-question" style="font-size: 38px; font-weight: 800; margin-bottom: 24px; line-height: 1.2;">
      Anatomía de la fórmula: la métrica califica al modelo sin leer su respuesta
    </h2>

    <!-- ZONA FOCAL HERO: Recreación fiel de la Figura 1 del paper (Esquinas 100% rectas) -->
    <div style="margin-bottom: 30px;">
      
      <!-- Puntero Superior Idéntico a Figura 1 del paper -->
      <div style="display: flex; width: 100%; margin-bottom: 8px;">
        <div style="width: 40%; font-family: var(--font-mono); font-size: 19px; font-weight: 700; color: var(--c-wine-primary); padding-left: 6px;">
          Q = 0.40·G + 0.40·R + 0.20·L
        </div>
        <div style="width: 60%; display: flex; align-items: center; justify-content: center; gap: 8px; font-family: var(--font-sans); font-size: 21px; font-weight: 800; color: var(--c-red-accent);">
          <span style="font-size: 24px; line-height: 1;">▼</span> ¡Aquí la respuesta del modelo NO es un dato de entrada! (60% ciego)
        </div>
      </div>

      <!-- Barra Segmentada Oficial (100% plana, esquinas rectas) -->
      <div class="formula-segmented-bar" style="margin: 0; height: 105px; border: 2px solid #2C0509;">
        <!-- 40% Grounding -->
        <div class="formula-segment" style="width: 40%; background-color: var(--c-wine-primary); justify-content: center;">
          <div class="formula-seg-pct" style="font-size: 40px; color: var(--c-gold);">40%</div>
          <div class="formula-seg-label" style="font-size: 22px;">GROUNDING (r, C)</div>
          <div style="font-size: 19px; opacity: 0.95; font-weight: 600; margin-top: 2px;">
            Único término que compara la respuesta con el libro
          </div>
        </div>

        <!-- 40% Relevance -->
        <div class="formula-segment" style="width: 40%; background-color: var(--c-red-accent); border-left: 2px solid #FFFFFF; justify-content: center;">
          <div class="formula-seg-pct" style="font-size: 40px;">40%</div>
          <div class="formula-seg-label" style="font-size: 22px;">RELEVANCE (q, C)</div>
          <div style="font-size: 19px; opacity: 0.95; font-weight: 600; margin-top: 2px;">
            Pregunta vs. contexto · ¡Ignora totalmente la respuesta!
          </div>
        </div>

        <!-- 20% Longitud -->
        <div class="formula-segment" style="width: 20%; background-color: #B38600; border-left: 2px solid #FFFFFF; justify-content: center;">
          <div class="formula-seg-pct" style="font-size: 40px;">20%</div>
          <div class="formula-seg-label" style="font-size: 22px;">LONGITUD (r)</div>
          <div style="font-size: 19px; opacity: 0.95; font-weight: 600; margin-top: 2px;">
            Solo mide cantidad de caracteres
          </div>
        </div>
      </div>

    </div>

    <!-- ZONA SECUNDARIA DESCONGESTIONADA: Dos Distorsiones de Código (Sin cajas dentro de cajas) -->
    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 30px;">
      
      <!-- Distorsión 01 -->
      <div style="background: #FFFFFF; border: 2px solid var(--c-wine-primary); padding: 22px 24px; display: flex; flex-direction: column; justify-content: space-between;">
        <div>
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px;">
            <span style="font-family: var(--font-mono); font-size: 18px; font-weight: 800; color: var(--c-wine-primary); letter-spacing: 1px;">DISTORSIÓN EN CÓDIGO 01</span>
            <span style="font-family: var(--font-mono); font-size: 20px; font-weight: 800; color: var(--c-wine-primary); background: #FAF5F5; border: 1.5px solid var(--c-wine-primary); padding: 2px 10px;">(x + 1) / 2</span>
          </div>
          <h3 style="font-family: var(--font-sans); font-size: 27px; font-weight: 800; color: var(--c-wine-dark); margin: 0 0 10px 0;">
            Coseno Reescalado: Similitud 0.00 → 0.50
          </h3>
          <p style="font-family: var(--font-sans); font-size: 22px; color: #110103; font-weight: 600; line-height: 1.4; margin: 0;">
            Al transformar el rango [-1, 1] a [0, 1], una similitud nula se convierte en nota aprobatoria de <strong>0.50</strong>, inflando respuestas desconectadas del libro.
          </p>
        </div>
        <div style="margin-top: 14px; padding-top: 10px; border-top: 1.5px solid rgba(70,8,17,0.2); font-family: var(--font-sans); font-size: 21px; color: var(--c-wine-dark); font-weight: 700;">
          Efecto: Califica como válidas respuestas vacías o incoherentes.
        </div>
      </div>

      <!-- Distorsión 02 -->
      <div style="background: #FFFFFF; border: 2px solid var(--c-red-accent); padding: 22px 24px; display: flex; flex-direction: column; justify-content: space-between;">
        <div>
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px;">
            <span style="font-family: var(--font-mono); font-size: 18px; font-weight: 800; color: var(--c-red-accent); letter-spacing: 1px;">DISTORSIÓN EN CÓDIGO 02</span>
            <span style="font-family: var(--font-mono); font-size: 20px; font-weight: 800; color: var(--c-red-accent); background: #FFE4E6; border: 1.5px solid var(--c-red-accent); padding: 2px 10px;">NOTA = 0.80</span>
          </div>
          <h3 style="font-family: var(--font-sans); font-size: 27px; font-weight: 800; color: var(--c-wine-dark); margin: 0 0 10px 0;">
            Premio Fijo al Rechazo: 9 Frases = 0.80
          </h3>
          <p style="font-family: var(--font-sans); font-size: 22px; color: #110103; font-weight: 600; line-height: 1.4; margin: 0;">
            Nueve frases literales de abstención reciben nota automática de <strong>0.80</strong>. Bonifica idéntico la abstención legítima que el fallo por torpeza del buscador.
          </p>
        </div>
        <div style="margin-top: 14px; padding-top: 10px; border-top: 1.5px solid rgba(201,16,27,0.2); font-family: var(--font-sans); font-size: 21px; color: var(--c-red-accent); font-weight: 700;">
          Efecto: Ventaja artificial sistemática a modelos sobre-conservadores.
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
# VARIANTE F2: El 60% Ciego como Cifra Rectora Superior + Barra Integrada
# -----------------------------------------------------------------------------
F2_HTML = '''
<section class="slide s-white active" id="slide-12-f2">
  <header class="slide-header">
    <div class="sh-left">
      <span class="sh-red-bar"></span>
      <span class="sh-category">03 · RESULTADOS · AUDITORÍA DE LA MÉTRICA AUTOMÁTICA</span>
    </div>
    <img src="assets/image6.png" alt="#LoxTIC" class="sh-loxtic">
  </header>
  <div class="sh-divider"></div>

  <div class="slide-content-area" style="justify-content: flex-start; padding-top: 10px;">
    <!-- Título Principal -->
    <h2 class="s-lead-question" style="font-size: 38px; font-weight: 800; margin-bottom: 20px; line-height: 1.2;">
      Anatomía de la fórmula: el 60% de la calificación ignora la respuesta del modelo
    </h2>

    <!-- BANNER HERO CENTRAL: Gran Contraste de Ponderación (Esquinas 100% Rectas) -->
    <div style="background: #FAF5F5; border: 2px solid #2C0509; padding: 16px 24px; margin-bottom: 26px;">
      
      <div style="display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 12px;">
        <div style="font-family: var(--font-sans); font-size: 22px; font-weight: 800; color: var(--c-wine-dark);">
          DECONSTRUCCIÓN DE LA ECUACIÓN 1 (MÉTRICA DE CALIDAD Q)
        </div>
        <div style="font-family: var(--font-mono); font-size: 20px; font-weight: 700; color: var(--c-wine-primary);">
          Q = 0.40·grounding + 0.40·relevance + 0.20·longitud
        </div>
      </div>

      <!-- Barra Segmentada Oficial (100% plana) -->
      <div class="formula-segmented-bar" style="margin: 0; height: 96px; border: 1.5px solid #2C0509;">
        <div class="formula-segment" style="width: 40%; background-color: var(--c-wine-primary); justify-content: center;">
          <div class="formula-seg-pct" style="font-size: 38px; color: var(--c-gold);">40%</div>
          <div class="formula-seg-label" style="font-size: 21px;">GROUNDING (r, C)</div>
          <div style="font-size: 18px; opacity: 0.95; font-weight: 600;">Único término que evalúa la respuesta</div>
        </div>
        <div class="formula-segment" style="width: 40%; background-color: var(--c-red-accent); border-left: 2px solid #FFFFFF; justify-content: center;">
          <div class="formula-seg-pct" style="font-size: 38px;">40%</div>
          <div class="formula-seg-label" style="font-size: 21px;">RELEVANCE (q, C)</div>
          <div style="font-size: 18px; opacity: 0.95; font-weight: 600;">Pregunta vs. contexto · ¡Ignora la respuesta!</div>
        </div>
        <div class="formula-segment" style="width: 20%; background-color: #B38600; border-left: 2px solid #FFFFFF; justify-content: center;">
          <div class="formula-seg-pct" style="font-size: 38px;">20%</div>
          <div class="formula-seg-label" style="font-size: 21px;">LONGITUD (r)</div>
          <div style="font-size: 18px; opacity: 0.95; font-weight: 600;">Solo cuenta cantidad de caracteres</div>
        </div>
      </div>

      <!-- Línea de Conclusión Inmediata del Hero -->
      <div style="margin-top: 10px; display: flex; justify-content: space-between; align-items: center; font-family: var(--font-sans); font-size: 20px; font-weight: 700;">
        <span style="color: var(--c-wine-primary);">● 40% Evalúa fidelidad semántica</span>
        <span style="color: var(--c-red-accent); background: #FFE4E6; border: 1px solid var(--c-red-accent); padding: 2px 10px;">
          ▲ 60% de la nota califica al buscador o premia la longitud
        </span>
      </div>

    </div>

    <!-- PANELES INFERIORES: Las dos trampas aritméticas -->
    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 28px;">
      <div style="background: #FFFFFF; border: 2px solid var(--c-wine-primary); padding: 20px 24px;">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
          <span style="font-family: var(--font-mono); font-size: 18px; font-weight: 800; color: var(--c-wine-primary);">TRAMPA 01</span>
          <span style="font-family: var(--font-mono); font-size: 19px; font-weight: 800; color: var(--c-wine-primary); background: #FAF5F5; padding: 2px 8px; border: 1px solid var(--c-wine-primary);">(x + 1) / 2</span>
        </div>
        <h3 style="font-family: var(--font-sans); font-size: 25px; font-weight: 800; color: var(--c-wine-dark); margin: 0 0 8px 0;">
          Coseno Reescalado: 0.00 → 0.50
        </h3>
        <p style="font-family: var(--font-sans); font-size: 21px; color: #110103; font-weight: 600; line-height: 1.35; margin: 0;">
          Reescalar de [-1, 1] a [0, 1] otorga <strong>0.50 aprobatorio</strong> a cualquier respuesta desconectada, inflando artificialmente el piso de notas.
        </p>
      </div>

      <div style="background: #FFFFFF; border: 2px solid var(--c-red-accent); padding: 20px 24px;">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
          <span style="font-family: var(--font-mono); font-size: 18px; font-weight: 800; color: var(--c-red-accent);">TRAMPA 02</span>
          <span style="font-family: var(--font-mono); font-size: 19px; font-weight: 800; color: var(--c-red-accent); background: #FFE4E6; padding: 2px 8px; border: 1px solid var(--c-red-accent);">Nota Fija = 0.80</span>
        </div>
        <h3 style="font-family: var(--font-sans); font-size: 25px; font-weight: 800; color: var(--c-wine-dark); margin: 0 0 8px 0;">
          Premio Automático al Rechazo
        </h3>
        <p style="font-family: var(--font-sans); font-size: 21px; color: #110103; font-weight: 600; line-height: 1.35; margin: 0;">
          Nueve frases fijas de abstención reciben <strong>0.80 automático</strong>, dando una ventaja artificial a modelos sobre-conservadores que rehúyen responder.
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
# VARIANTE F3: Evolución Directa de slide_12.html con Foco Visual y Descongestión
# -----------------------------------------------------------------------------
F3_HTML = '''
<section class="slide s-white active" id="slide-12-f3">
  <header class="slide-header">
    <div class="sh-left">
      <span class="sh-red-bar"></span>
      <span class="sh-category">03 · RESULTADOS · DECONSTRUCCIÓN DE LA ECUACIÓN 1</span>
    </div>
    <img src="assets/image6.png" alt="#LoxTIC" class="sh-loxtic">
  </header>
  <div class="sh-divider"></div>

  <div class="slide-content-area" style="justify-content: flex-start; padding-top: 10px;">
    <!-- Título Principal -->
    <h2 class="s-lead-question" style="font-size: 38px; font-weight: 800; margin-bottom: 16px; line-height: 1.2;">
      Anatomía de la fórmula: la métrica que califica al modelo sin leer su respuesta
    </h2>

    <!-- Fila Focal de la Ecuación con el foco del 60% integrado -->
    <div style="background: #FAF5F5; border-left: 6px solid var(--c-wine-primary); padding: 12px 20px; font-family: var(--font-mono); font-size: 22px; color: var(--c-wine-dark); font-weight: 700; margin-bottom: 16px; display: flex; justify-content: space-between; align-items: center;">
      <span>Q(r, q, C) = 0.40·grounding(r, C) + 0.40·relevance(q, C) + 0.20·longitud(r)</span>
      <span style="font-family: var(--font-sans); font-size: 19px; font-weight: 800; color: var(--c-red-accent); background: #FFE4E6; padding: 2px 10px;">
        ▲ 60% CIEGO A LA RESPUESTA
      </span>
    </div>

    <!-- Barra Segmentada Oficial (Idéntica a slide_12.html original, esquinas 100% rectas, sin microtextos) -->
    <div class="formula-segmented-bar" style="margin: 0 0 24px 0; height: 100px;">
      <div class="formula-segment" style="width: 40%; background-color: var(--c-wine-primary); justify-content: center;">
        <div class="formula-seg-pct" style="font-size: 38px; color: var(--c-gold);">40%</div>
        <div class="formula-seg-label" style="font-size: 21px;">GROUNDING (r, C)</div>
        <div style="font-size: 18px; opacity: 0.95; font-weight: 600;">Único término que lee la respuesta del modelo</div>
      </div>
      <div class="formula-segment" style="width: 40%; background-color: var(--c-red-accent); justify-content: center;">
        <div class="formula-seg-pct" style="font-size: 38px;">40%</div>
        <div class="formula-seg-label" style="font-size: 21px;">RELEVANCE (q, C)</div>
        <div style="font-size: 18px; opacity: 0.95; font-weight: 600;">Pregunta vs. contexto · ¡Ignora la respuesta!</div>
      </div>
      <div class="formula-segment" style="width: 20%; background-color: #B38600; justify-content: center;">
        <div class="formula-seg-pct" style="font-size: 38px;">20%</div>
        <div class="formula-seg-label" style="font-size: 21px;">LONGITUD (r)</div>
        <div style="font-size: 18px; opacity: 0.95; font-weight: 600;">Solo mide cantidad de caracteres</div>
      </div>
    </div>

    <!-- Dos Trampas de Código: versión descongestionada sin cajas anidadas -->
    <div class="grid-2col" style="gap: 28px; flex-grow: 1;">
      
      <!-- Trampa 1 -->
      <div class="s6-block s6-block-wine" style="padding: 22px 26px; display: flex; flex-direction: column; justify-content: space-between;">
        <div>
          <div class="s6-block-tag" style="font-size: 18px; font-weight: 800; margin-bottom: 8px;">TRAMPA DE CÓDIGO 01</div>
          <h3 class="s6-block-title" style="font-size: 27px; margin-bottom: 12px; color: var(--c-wine-dark);">
            Coseno Reescalado: (x + 1)/2
          </h3>
          <ul class="card-bullet-list" style="gap: 10px;">
            <li class="card-bullet-item" style="font-size: 22px; color: #110103;">
              <span class="bullet-dot bullet-dot-wine"></span>
              <span><strong>Similitud nula (0.00):</strong> Se transforma en <strong>0.50</strong> (nota aprobatoria).</span>
            </li>
            <li class="card-bullet-item" style="font-size: 22px; color: #110103;">
              <span class="bullet-dot bullet-dot-wine"></span>
              <span><strong>Distorsión artificial:</strong> Respuestas mediocres parten con medio punto garantizado.</span>
            </li>
          </ul>
        </div>
        <div class="card-conclusion-row" style="font-size: 21px; margin-top: 14px;">
          <strong>Efecto:</strong> Califica como válidas respuestas desconectadas del libro.
        </div>
      </div>

      <!-- Trampa 2 -->
      <div class="s6-block s6-block-red" style="padding: 22px 26px; display: flex; flex-direction: column; justify-content: space-between;">
        <div>
          <div class="s6-block-tag" style="font-size: 18px; font-weight: 800; color: var(--c-red-accent); margin-bottom: 8px;">TRAMPA DE CÓDIGO 02</div>
          <h3 class="s6-block-title" style="font-size: 27px; margin-bottom: 12px; color: var(--c-wine-dark);">
            Premio Fijo al Rechazo (0.80)
          </h3>
          <ul class="card-bullet-list" style="gap: 10px;">
            <li class="card-bullet-item" style="font-size: 22px; color: #110103;">
              <span class="bullet-dot"></span>
              <span><strong>9 frases fijas:</strong> Otorgan nota fija automática de <strong>0.80</strong> al abstenerse.</span>
            </li>
            <li class="card-bullet-item" style="font-size: 22px; color: #110103;">
              <span class="bullet-dot"></span>
              <span><strong>Premio ciego:</strong> Bonifica igual la abstención prudente que un fallo por bloqueo léxico.</span>
            </li>
          </ul>
        </div>
        <div class="card-conclusion-row verdict-red" style="font-size: 21px; margin-top: 14px;">
          <strong style="color: var(--c-red-accent);">Efecto:</strong> Ventaja artificial sistemática a modelos sobre-conservadores.
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
  <title>Test Focus Variants Slide 12</title>
  <link rel="stylesheet" href="http://localhost:8085/styles.css?v=16">
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
        ('slide_12_f1.html', 'slide_12_f1.png', F1_HTML),
        ('slide_12_f2.html', 'slide_12_f2.png', F2_HTML),
        ('slide_12_f3.html', 'slide_12_f3.png', F3_HTML)
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
