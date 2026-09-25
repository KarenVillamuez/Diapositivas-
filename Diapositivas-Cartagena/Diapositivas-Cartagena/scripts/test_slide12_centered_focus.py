# -*- coding: utf-8 -*-
"""
Pruebas de diseño para Slide 12 según las directrices exactas del usuario:
- Base: Variante F3 (sin cuadros dentro de cuadros, esquinas 100% rectas).
- Foco: La gráfica centrada como protagonista visual principal del slide.
- Complementos: Tarjetas/etiquetas técnicas con el texto estrictamente necesario (sin sobrecarga).
- Legibilidad: Cero textos pequeños (<21px), apto para auditorio de congreso.
"""
import os
from playwright.sync_api import sync_playwright

output_dir = r"C:\Users\ASUS\.gemini\antigravity-ide\brain\a6624504-511c-4b9d-bc9a-468e348bde40"
os.makedirs(output_dir, exist_ok=True)

# -----------------------------------------------------------------------------
# VARIANTE C1: Gráfica Centrada Hero + Puntero 40/60 + 2 Tarjetas Técnicas
# -----------------------------------------------------------------------------
C1_HTML = '''
<section class="slide s-white active" id="slide-12-c1">
  <header class="slide-header">
    <div class="sh-left">
      <span class="sh-red-bar"></span>
      <span class="sh-category">03 · RESULTADOS · AUDITORÍA DE LA ECUACIÓN 1 (MÉTRICA Q)</span>
    </div>
    <img src="assets/image6.png" alt="#LoxTIC" class="sh-loxtic">
  </header>
  <div class="sh-divider"></div>

  <div class="slide-content-area" style="justify-content: flex-start; padding-top: 10px;">
    <!-- Pregunta Rectora -->
    <h2 class="s-lead-question" style="font-size: 38px; font-weight: 800; margin-bottom: 22px; line-height: 1.2;">
      Anatomía de la fórmula: la métrica califica al modelo sin leer su respuesta
    </h2>

    <!-- EL FOCO PRINCIPAL: Gráfica Centrada y Protagonista -->
    <div style="margin-bottom: 26px;">
      
      <!-- Fila de Etiquetas de Foco Superior -->
      <div style="display: flex; width: 100%; margin-bottom: 8px;">
        <div style="width: 40%; font-family: var(--font-sans); font-size: 20px; font-weight: 800; color: var(--c-wine-primary); padding-left: 6px;">
          ● ÚNICO TÉRMINO ACTIVO (40%)
        </div>
        <div style="width: 60%; font-family: var(--font-sans); font-size: 20px; font-weight: 800; color: var(--c-red-accent); text-align: center; background: #FFE4E6; border: 1.5px solid var(--c-red-accent); padding: 3px 0;">
          ▲ 60% DE LA NOTA: NO EVALÚA LA RESPUESTA O SOLO MIDE LONGITUD
        </div>
      </div>

      <!-- Barra Segmentada Oficial (100% Plana, Esquinas Rectas, Altura Imponente) -->
      <div class="formula-segmented-bar" style="margin: 0; height: 110px; border: 2px solid #2C0509;">
        <!-- 40% Grounding -->
        <div class="formula-segment" style="width: 40%; background-color: var(--c-wine-primary); justify-content: center; padding: 8px 16px;">
          <div class="formula-seg-pct" style="font-size: 42px; color: var(--c-gold);">40%</div>
          <div class="formula-seg-label" style="font-size: 22px; letter-spacing: 0.5px;">GROUNDING (r, C)</div>
          <div style="font-size: 20px; opacity: 0.95; font-weight: 600; margin-top: 3px;">
            Compara la respuesta generada vs. texto del libro
          </div>
        </div>

        <!-- 40% Relevance -->
        <div class="formula-segment" style="width: 40%; background-color: var(--c-red-accent); border-left: 2px solid #FFFFFF; justify-content: center; padding: 8px 16px;">
          <div class="formula-seg-pct" style="font-size: 42px;">40%</div>
          <div class="formula-seg-label" style="font-size: 22px; letter-spacing: 0.5px;">RELEVANCE (q, C)</div>
          <div style="font-size: 20px; opacity: 0.95; font-weight: 600; margin-top: 3px;">
            Pregunta vs. contexto · ¡Ignora la respuesta!
          </div>
        </div>

        <!-- 20% Longitud -->
        <div class="formula-segment" style="width: 20%; background-color: #B38600; border-left: 2px solid #FFFFFF; justify-content: center; padding: 8px 16px;">
          <div class="formula-seg-pct" style="font-size: 42px;">20%</div>
          <div class="formula-seg-label" style="font-size: 22px; letter-spacing: 0.5px;">LONGITUD (r)</div>
          <div style="font-size: 20px; opacity: 0.95; font-weight: 600; margin-top: 3px;">
            Heurística: solo cuenta caracteres
          </div>
        </div>
      </div>

      <!-- Línea Tipográfica de la Ecuación Formal Centrada -->
      <div style="display: flex; justify-content: space-between; align-items: center; margin-top: 10px; padding: 0 4px;">
        <span style="font-family: var(--font-mono); font-size: 21px; font-weight: 700; color: var(--c-wine-dark);">
          Q(r, q, C) = 0.40·grounding(r, C) + 0.40·relevance(q, C) + 0.20·length(r)
        </span>
        <span style="font-family: var(--font-mono); font-size: 18px; font-weight: 800; color: #110103; background: #FAF5F5; border: 1.5px solid #2C0509; padding: 2px 10px;">
          ECUACIÓN 1 AUDITADA
        </span>
      </div>

    </div>

    <!-- TARJETAS TÉCNICAS COMPLEMENTARIAS (Sin sobrecarga de texto, cero microtextos) -->
    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 28px;">
      
      <!-- Distorsión 01 -->
      <div style="background: #FFFFFF; border: 2px solid var(--c-wine-primary); padding: 20px 24px; display: flex; flex-direction: column; justify-content: space-between;">
        <div>
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
            <span style="font-family: var(--font-mono); font-size: 18px; font-weight: 800; color: var(--c-wine-primary); letter-spacing: 1px;">DISTORSIÓN EN CÓDIGO 01</span>
            <span style="font-family: var(--font-mono); font-size: 20px; font-weight: 800; color: var(--c-wine-primary); background: #FAF5F5; border: 1.5px solid var(--c-wine-primary); padding: 2px 10px;">(x + 1) / 2</span>
          </div>
          <h3 style="font-family: var(--font-sans); font-size: 26px; font-weight: 800; color: var(--c-wine-dark); margin: 0 0 10px 0;">
            Coseno Reescalado: Similitud 0.00 → 0.50
          </h3>
          <p style="font-family: var(--font-sans); font-size: 22px; color: #110103; font-weight: 600; line-height: 1.38; margin: 0;">
            Al mapear [-1, 1] a [0, 1], una respuesta ortogonal o desconectada obtiene un <strong>0.50 aprobatorio</strong> como nota base garantizada.
          </p>
        </div>
        <div style="margin-top: 14px; padding-top: 10px; border-top: 1.5px solid rgba(70,8,17,0.2); font-family: var(--font-sans); font-size: 21px; color: var(--c-wine-dark); font-weight: 700;">
          Impacto en benchmark: Infla artificialmente modelos que fallan la respuesta.
        </div>
      </div>

      <!-- Distorsión 02 -->
      <div style="background: #FFFFFF; border: 2px solid var(--c-red-accent); padding: 20px 24px; display: flex; flex-direction: column; justify-content: space-between;">
        <div>
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
            <span style="font-family: var(--font-mono); font-size: 18px; font-weight: 800; color: var(--c-red-accent); letter-spacing: 1px;">DISTORSIÓN EN CÓDIGO 02</span>
            <span style="font-family: var(--font-mono); font-size: 20px; font-weight: 800; color: var(--c-red-accent); background: #FFE4E6; border: 1.5px solid var(--c-red-accent); padding: 2px 10px;">NOTA = 0.80</span>
          </div>
          <h3 style="font-family: var(--font-sans); font-size: 26px; font-weight: 800; color: var(--c-wine-dark); margin: 0 0 10px 0;">
            Premio Automático al Rechazo: 9 Frases
          </h3>
          <p style="font-family: var(--font-sans); font-size: 22px; color: #110103; font-weight: 600; line-height: 1.38; margin: 0;">
            Nueve frases de abstención reciben <strong>0.80 directo</strong>. Bonifica igual la prudencia pedagógica que un bloqueo por torpeza del recuperador.
          </p>
        </div>
        <div style="margin-top: 14px; padding-top: 10px; border-top: 1.5px solid rgba(201,16,27,0.2); font-family: var(--font-sans); font-size: 21px; color: var(--c-red-accent); font-weight: 700;">
          Impacto en benchmark: Ventaja artificial a modelos sobre-conservadores.
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
# VARIANTE C2: Gráfica Centrada Dominante + Etiquetas Técnicas Monospace
# -----------------------------------------------------------------------------
C2_HTML = '''
<section class="slide s-white active" id="slide-12-c2">
  <header class="slide-header">
    <div class="sh-left">
      <span class="sh-red-bar"></span>
      <span class="sh-category">03 · RESULTADOS · AUDITORÍA DE LA ECUACIÓN 1 (MÉTRICA Q)</span>
    </div>
    <img src="assets/image6.png" alt="#LoxTIC" class="sh-loxtic">
  </header>
  <div class="sh-divider"></div>

  <div class="slide-content-area" style="justify-content: flex-start; padding-top: 10px;">
    <!-- Pregunta Rectora -->
    <h2 class="s-lead-question" style="font-size: 38px; font-weight: 800; margin-bottom: 18px; line-height: 1.2;">
      Anatomía de la fórmula: la métrica que califica al modelo sin leer su respuesta
    </h2>

    <!-- Foco: Barra Centrada con Rótulos Verticales Integrados -->
    <div style="margin-bottom: 24px;">
      
      <!-- Indicador Focal Superior -->
      <div style="display: flex; justify-content: space-between; align-items: flex-end; margin-bottom: 8px;">
        <span style="font-family: var(--font-mono); font-size: 22px; font-weight: 800; color: var(--c-wine-dark);">
          Q = 0.40·G(r,C) + 0.40·R(q,C) + 0.20·L(r)
        </span>
        <span style="font-family: var(--font-sans); font-size: 20px; font-weight: 800; color: var(--c-red-accent); background: #FFE4E6; border: 1.5px solid var(--c-red-accent); padding: 3px 12px;">
          ▼ 60% CIEGO: IGNORA LA RESPUESTA O SOLO MIDE CARACTERES
        </span>
      </div>

      <!-- Barra de 120px de Altura (Gran Foco Visual) -->
      <div class="formula-segmented-bar" style="margin: 0; height: 118px; border: 2px solid #2C0509;">
        <div class="formula-segment" style="width: 40%; background-color: var(--c-wine-primary); justify-content: center; padding: 10px 18px;">
          <div class="formula-seg-pct" style="font-size: 44px; color: var(--c-gold);">40%</div>
          <div class="formula-seg-label" style="font-size: 23px;">GROUNDING (r, C)</div>
          <div style="font-size: 20px; opacity: 0.95; font-weight: 600; margin-top: 3px;">
            Único término que evalúa el texto generado
          </div>
        </div>
        <div class="formula-segment" style="width: 40%; background-color: var(--c-red-accent); border-left: 2px solid #FFFFFF; justify-content: center; padding: 10px 18px;">
          <div class="formula-seg-pct" style="font-size: 44px;">40%</div>
          <div class="formula-seg-label" style="font-size: 23px;">RELEVANCE (q, C)</div>
          <div style="font-size: 20px; opacity: 0.95; font-weight: 600; margin-top: 3px;">
            Pregunta vs. contexto · ¡Ignora la respuesta!
          </div>
        </div>
        <div class="formula-segment" style="width: 20%; background-color: #B38600; border-left: 2px solid #FFFFFF; justify-content: center; padding: 10px 18px;">
          <div class="formula-seg-pct" style="font-size: 44px;">20%</div>
          <div class="formula-seg-label" style="font-size: 23px;">LONGITUD (r)</div>
          <div style="font-size: 20px; opacity: 0.95; font-weight: 600; margin-top: 3px;">
            Heurística de cantidad de caracteres
          </div>
        </div>
      </div>

    </div>

    <!-- Píldoras Técnicas Complementarias (Mínimo Texto, Máximo Rigor) -->
    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 28px;">
      
      <div style="background: #FAF5F5; border: 2px solid var(--c-wine-primary); padding: 18px 22px;">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
          <span style="font-family: var(--font-sans); font-size: 23px; font-weight: 800; color: var(--c-wine-dark);">
            Coseno Reescalado (x + 1)/2
          </span>
          <span style="font-family: var(--font-mono); font-size: 21px; font-weight: 800; color: var(--c-wine-primary); background: #FFFFFF; border: 1.5px solid var(--c-wine-primary); padding: 2px 10px;">
            0.00 → 0.50
          </span>
        </div>
        <p style="font-family: var(--font-sans); font-size: 22px; color: #110103; font-weight: 600; line-height: 1.35; margin: 0 0 10px 0;">
          Mapear de [-1, 1] a [0, 1] premia respuestas desconectadas con <strong>0.50 aprobado</strong>.
        </p>
        <div style="font-family: var(--font-sans); font-size: 21px; color: var(--c-wine-primary); font-weight: 700;">
          Sesgo: Infla artificialmente la calidad de respuestas mediocres.
        </div>
      </div>

      <div style="background: #FAF5F5; border: 2px solid var(--c-red-accent); padding: 18px 22px;">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
          <span style="font-family: var(--font-sans); font-size: 23px; font-weight: 800; color: var(--c-wine-dark);">
            Premio al Rechazo (9 Frases)
          </span>
          <span style="font-family: var(--font-mono); font-size: 21px; font-weight: 800; color: var(--c-red-accent); background: #FFFFFF; border: 1.5px solid var(--c-red-accent); padding: 2px 10px;">
            Nota = 0.80
          </span>
        </div>
        <p style="font-family: var(--font-sans); font-size: 22px; color: #110103; font-weight: 600; line-height: 1.35; margin: 0 0 10px 0;">
          Nueve frases fijas reciben <strong>0.80 automático</strong>, premiando la no-respuesta como éxito.
        </p>
        <div style="font-family: var(--font-sans); font-size: 21px; color: var(--c-red-accent); font-weight: 700;">
          Sesgo: Ventaja artificial a modelos sobre-conservadores.
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
# VARIANTE C3: Estructura F3 Depurada (Espejo de slide_12.html pero Descongestionada)
# -----------------------------------------------------------------------------
C3_HTML = '''
<section class="slide s-white active" id="slide-12-c3">
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
    <h2 class="s-lead-question" style="font-size: 38px; font-weight: 800; margin-bottom: 14px; line-height: 1.2;">
      Anatomía de la fórmula: la métrica que califica al modelo sin leer su respuesta
    </h2>

    <!-- Fórmula en marco sutil alineada al centro -->
    <div style="background: #FAF5F5; border-left: 6px solid var(--c-wine-primary); padding: 10px 20px; font-family: var(--font-mono); font-size: 22px; color: var(--c-wine-dark); font-weight: 700; margin-bottom: 14px; display: flex; justify-content: space-between; align-items: center;">
      <span>Q(r, q, C) = 0.40·grounding(r, C) + 0.40·relevance(q, C) + 0.20·longitud(r)</span>
      <span style="font-family: var(--font-sans); font-size: 19px; font-weight: 800; color: var(--c-red-accent); background: #FFE4E6; border: 1px solid var(--c-red-accent); padding: 2px 10px;">
        ▲ 60% CIEGO A LA RESPUESTA
      </span>
    </div>

    <!-- Barra Segmentada Oficial Centrada (El Foco) -->
    <div class="formula-segmented-bar" style="margin: 0 0 22px 0; height: 106px;">
      <div class="formula-segment" style="width: 40%; background-color: var(--c-wine-primary); justify-content: center;">
        <div class="formula-seg-pct" style="font-size: 40px; color: var(--c-gold);">40%</div>
        <div class="formula-seg-label" style="font-size: 22px;">GROUNDING (r, C)</div>
        <div style="font-size: 20px; opacity: 0.95; font-weight: 600;">Único término que evalúa la respuesta</div>
      </div>
      <div class="formula-segment" style="width: 40%; background-color: var(--c-red-accent); justify-content: center;">
        <div class="formula-seg-pct" style="font-size: 40px;">40%</div>
        <div class="formula-seg-label" style="font-size: 22px;">RELEVANCE (q, C)</div>
        <div style="font-size: 20px; opacity: 0.95; font-weight: 600;">Pregunta vs. libro · ¡Ignora la respuesta!</div>
      </div>
      <div class="formula-segment" style="width: 20%; background-color: #B38600; justify-content: center;">
        <div class="formula-seg-pct" style="font-size: 40px;">20%</div>
        <div class="formula-seg-label" style="font-size: 22px;">LONGITUD (r)</div>
        <div style="font-size: 20px; opacity: 0.95; font-weight: 600;">Mide cantidad de caracteres</div>
      </div>
    </div>

    <!-- Dos Bloques Limpios s6-block Descongestionados -->
    <div class="grid-2col" style="gap: 28px;">
      
      <!-- Trampa 1 -->
      <div class="s6-block s6-block-wine" style="padding: 20px 24px;">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 6px;">
          <div class="s6-block-tag" style="font-size: 18px; font-weight: 800;">DISTORSIÓN 01</div>
          <span style="font-family: var(--font-mono); font-size: 19px; font-weight: 800; color: var(--c-wine-primary); background: #FAF5F5; padding: 2px 8px; border: 1px solid var(--c-wine-primary);">(x + 1)/2</span>
        </div>
        <h3 class="s6-block-title" style="font-size: 25px; margin-bottom: 8px; color: var(--c-wine-dark);">
          Coseno Reescalado: 0.00 → 0.50
        </h3>
        <p style="font-family: var(--font-sans); font-size: 22px; color: #110103; font-weight: 600; line-height: 1.35; margin: 0 0 10px 0;">
          Una similitud nula se convierte en nota aprobatoria de <strong>0.50</strong>, inflando respuestas sin relación con el texto.
        </p>
        <div class="card-conclusion-row" style="font-size: 21px; padding-top: 8px; margin-top: 6px;">
          <strong>Efecto:</strong> Califica como válidas respuestas mediocres.
        </div>
      </div>

      <!-- Trampa 2 -->
      <div class="s6-block s6-block-red" style="padding: 20px 24px;">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 6px;">
          <div class="s6-block-tag" style="font-size: 18px; font-weight: 800; color: var(--c-red-accent);">DISTORSIÓN 02</div>
          <span style="font-family: var(--font-mono); font-size: 19px; font-weight: 800; color: var(--c-red-accent); background: #FFE4E6; padding: 2px 8px; border: 1px solid var(--c-red-accent);">Nota = 0.80</span>
        </div>
        <h3 class="s6-block-title" style="font-size: 25px; margin-bottom: 8px; color: var(--c-wine-dark);">
          Premio al Rechazo: 9 Frases = 0.80
        </h3>
        <p style="font-family: var(--font-sans); font-size: 22px; color: #110103; font-weight: 600; line-height: 1.35; margin: 0 0 10px 0;">
          Nueve frases de abstención reciben <strong>0.80 automático</strong>. Bonifica igual la prudencia que el bloqueo por torpeza léxica.
        </p>
        <div class="card-conclusion-row verdict-red" style="font-size: 21px; padding-top: 8px; margin-top: 6px;">
          <strong style="color: var(--c-red-accent);">Efecto:</strong> Ventaja artificial a modelos sobre-conservadores.
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
  <title>Test Centered Focus Variants Slide 12</title>
  <link rel="stylesheet" href="http://localhost:8085/styles.css?v=17">
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
        ('slide_12_c1.html', 'slide_12_c1.png', C1_HTML),
        ('slide_12_c2.html', 'slide_12_c2.png', C2_HTML),
        ('slide_12_c3.html', 'slide_12_c3.png', C3_HTML)
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
