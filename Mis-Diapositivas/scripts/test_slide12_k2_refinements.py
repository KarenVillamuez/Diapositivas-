# -*- coding: utf-8 -*-
"""
Afinamientos y mejoras sobre K2 para Slide 12:
- Variante K2-A: Tarjetas con 2 líneas técnicas concisas (Mecanismo + Efecto benchmark),
  fondo #FAF5F5, badges uniformes y balance vertical perfecto.
- Variante K2-B: Píldoras horizontales con mayor presencia, etiquetas balanceadas arriba (40% vs 60%)
  y fórmula formal.
- Variante K2-C: Máxima simplicidad con tipografía ampliada (24px) y distribución vertical expandida.
"""
import os
from playwright.sync_api import sync_playwright

output_dir = r"C:\Users\ASUS\.gemini\antigravity-ide\brain\a6624504-511c-4b9d-bc9a-468e348bde40"
os.makedirs(output_dir, exist_ok=True)

# -----------------------------------------------------------------------------
# VARIANTE K2-A: Balance Técnico Completo (Mecanismo + Efecto)
# -----------------------------------------------------------------------------
K2_A_HTML = '''
<section class="slide s-white active" id="slide-12-k2-a">
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

    <!-- EL FOCO PRINCIPAL: Gráfica Centrada (124px de altura) -->
    <div>
      
      <!-- Fila superior: Contraste de las dos zonas (40% vs 60%) -->
      <div style="display: flex; width: 100%; margin-bottom: 8px; align-items: flex-end;">
        <div style="width: 40%; font-family: var(--font-sans); font-size: 20px; font-weight: 800; color: var(--c-wine-primary); padding-left: 4px;">
          ● 40% EVALÚA LA RESPUESTA GENERADA
        </div>
        <div style="width: 60%; font-family: var(--font-sans); font-size: 20px; font-weight: 800; color: var(--c-red-accent); text-align: center; background: #FFE4E6; border: 1.5px solid var(--c-red-accent); padding: 4px 0;">
          ▼ ¡EL 60% DE LA NOTA ES CIEGO AL CONTENIDO DE LA RESPUESTA!
        </div>
      </div>

      <!-- Barra Segmentada Oficial (124px de alto, esquinas rectas) -->
      <div class="formula-segmented-bar" style="margin: 0; height: 124px; border: 2px solid #2C0509;">
        <!-- 40% Grounding -->
        <div class="formula-segment" style="width: 40%; background-color: var(--c-wine-primary); justify-content: center; padding: 10px 18px;">
          <div class="formula-seg-pct" style="font-size: 46px; color: var(--c-gold); line-height: 1;">40%</div>
          <div class="formula-seg-label" style="font-size: 23px; letter-spacing: 0.5px; margin-top: 4px;">GROUNDING (r, C)</div>
          <div style="font-size: 20px; opacity: 0.95; font-weight: 600; margin-top: 3px;">
            Único término que compara respuesta vs. libro
          </div>
        </div>

        <!-- 40% Relevance -->
        <div class="formula-segment" style="width: 40%; background-color: var(--c-red-accent); border-left: 2px solid #FFFFFF; justify-content: center; padding: 10px 18px;">
          <div class="formula-seg-pct" style="font-size: 46px; line-height: 1;">40%</div>
          <div class="formula-seg-label" style="font-size: 23px; letter-spacing: 0.5px; margin-top: 4px;">RELEVANCE (q, C)</div>
          <div style="font-size: 20px; opacity: 0.95; font-weight: 600; margin-top: 3px;">
            Pregunta vs. contexto · ¡Ignora la respuesta!
          </div>
        </div>

        <!-- 20% Longitud -->
        <div class="formula-segment" style="width: 20%; background-color: #B38600; border-left: 2px solid #FFFFFF; justify-content: center; padding: 10px 18px;">
          <div class="formula-seg-pct" style="font-size: 46px; line-height: 1;">20%</div>
          <div class="formula-seg-label" style="font-size: 23px; letter-spacing: 0.5px; margin-top: 4px;">LONGITUD (r)</div>
          <div style="font-size: 20px; opacity: 0.95; font-weight: 600; margin-top: 3px;">
            Conteo de caracteres
          </div>
        </div>
      </div>

      <!-- Fórmula formal compacta justo debajo de la barra -->
      <div style="font-family: var(--font-mono); font-size: 20px; font-weight: 700; color: #555555; margin-top: 8px; text-align: center;">
        Q(r, q, C) = 0.40·grounding(r, C) + 0.40·relevance(q, C) + 0.20·length(r)
      </div>

    </div>

    <!-- TARJETAS COMPLEMENTARIAS: Con Mecanismo + Efecto Benchmark (Fondo #FAF5F5) -->
    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 28px;">
      
      <!-- Distorsión 01 -->
      <div style="background: #FAF5F5; border: 2px solid var(--c-wine-primary); padding: 18px 22px; display: flex; align-items: center; gap: 18px;">
        <div style="font-family: var(--font-mono); font-size: 24px; font-weight: 800; color: var(--c-wine-primary); background: #FFFFFF; border: 1.5px solid var(--c-wine-primary); padding: 12px 14px; white-space: nowrap; text-align: center; min-width: 130px;">
          0.00 → 0.50
        </div>
        <div>
          <div style="font-family: var(--font-sans); font-size: 23px; font-weight: 800; color: var(--c-wine-dark); margin-bottom: 4px;">
            Coseno Reescalado: (x + 1)/2
          </div>
          <div style="font-family: var(--font-sans); font-size: 21px; color: #110103; font-weight: 600; line-height: 1.35;">
            Una similitud nula se convierte en nota aprobatoria de <strong>0.50</strong>, inflando respuestas sin relación con el libro.
          </div>
        </div>
      </div>

      <!-- Distorsión 02 -->
      <div style="background: #FAF5F5; border: 2px solid var(--c-red-accent); padding: 18px 22px; display: flex; align-items: center; gap: 18px;">
        <div style="font-family: var(--font-mono); font-size: 24px; font-weight: 800; color: var(--c-red-accent); background: #FFFFFF; border: 1.5px solid var(--c-red-accent); padding: 12px 14px; white-space: nowrap; text-align: center; min-width: 130px;">
          Nota = 0.80
        </div>
        <div>
          <div style="font-family: var(--font-sans); font-size: 23px; font-weight: 800; color: var(--c-wine-dark); margin-bottom: 4px;">
            Premio al Rechazo (9 Frases)
          </div>
          <div style="font-family: var(--font-sans); font-size: 21px; color: #110103; font-weight: 600; line-height: 1.35;">
            Nueve frases fijas reciben <strong>0.80 automático</strong>, dando ventaja artificial a modelos sobre-conservadores.
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
# VARIANTE K2-B: Píldoras Horizontales Limpias con Fondo Blanco y Borde Robusto
# -----------------------------------------------------------------------------
K2_B_HTML = '''
<section class="slide s-white active" id="slide-12-k2-b">
  <header class="slide-header">
    <div class="sh-left">
      <span class="sh-red-bar"></span>
      <span class="sh-category">03 · RESULTADOS · AUDITORÍA DE LA ECUACIÓN 1 (MÉTRICA Q)</span>
    </div>
    <img src="assets/image6.png" alt="#LoxTIC" class="sh-loxtic">
  </header>
  <div class="sh-divider"></div>

  <!-- Contenedor Centrado Verticalmente -->
  <div class="slide-content-area" style="justify-content: center; gap: 40px; padding: 0;">
    
    <!-- Título Principal -->
    <h2 class="s-lead-question" style="font-size: 38px; font-weight: 800; margin: 0; line-height: 1.2;">
      Anatomía de la fórmula: la métrica califica al modelo sin leer su respuesta
    </h2>

    <!-- EL FOCO PRINCIPAL: Gráfica Centrada (130px de altura) -->
    <div>
      
      <!-- Fila superior -->
      <div style="display: flex; width: 100%; margin-bottom: 8px; align-items: flex-end;">
        <div style="width: 40%; font-family: var(--font-mono); font-size: 22px; font-weight: 700; color: var(--c-wine-primary); padding-left: 4px;">
          Q(r, q, C) = 0.40·G + 0.40·R + 0.20·L
        </div>
        <div style="width: 60%; font-family: var(--font-sans); font-size: 21px; font-weight: 800; color: var(--c-red-accent); text-align: center; background: #FFE4E6; border: 1.5px solid var(--c-red-accent); padding: 4px 0;">
          ▼ ¡EL 60% DE LA NOTA NO EVALÚA EL CONTENIDO DE LA RESPUESTA!
        </div>
      </div>

      <!-- Barra Segmentada Oficial (130px de alto) -->
      <div class="formula-segmented-bar" style="margin: 0; height: 130px; border: 2.5px solid #2C0509;">
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

    <!-- TARJETAS PÍLDORA HORIZONTALES (Con remate de impacto) -->
    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 28px;">
      
      <!-- Píldora 1 -->
      <div style="background: #FFFFFF; border: 2px solid var(--c-wine-primary); padding: 18px 22px; display: flex; align-items: center; gap: 20px;">
        <div style="font-family: var(--font-mono); font-size: 24px; font-weight: 800; color: var(--c-wine-primary); background: #FAF5F5; border: 1.5px solid var(--c-wine-primary); padding: 12px 14px; white-space: nowrap; text-align: center; min-width: 130px;">
          0.00 → 0.50
        </div>
        <div>
          <div style="font-family: var(--font-sans); font-size: 23px; font-weight: 800; color: var(--c-wine-dark); margin-bottom: 2px;">
            Coseno Reescalado (x + 1)/2
          </div>
          <div style="font-family: var(--font-sans); font-size: 21px; color: #110103; font-weight: 600; line-height: 1.3;">
            Respuestas desconectadas del libro obtienen <strong>0.50 aprobado</strong> como nota base garantizada.
          </div>
        </div>
      </div>

      <!-- Píldora 2 -->
      <div style="background: #FFFFFF; border: 2px solid var(--c-red-accent); padding: 18px 22px; display: flex; align-items: center; gap: 20px;">
        <div style="font-family: var(--font-mono); font-size: 24px; font-weight: 800; color: var(--c-red-accent); background: #FFE4E6; border: 1.5px solid var(--c-red-accent); padding: 12px 14px; white-space: nowrap; text-align: center; min-width: 130px;">
          Nota = 0.80
        </div>
        <div>
          <div style="font-family: var(--font-sans); font-size: 23px; font-weight: 800; color: var(--c-wine-dark); margin-bottom: 2px;">
            Premio al Rechazo (9 Frases)
          </div>
          <div style="font-family: var(--font-sans); font-size: 21px; color: #110103; font-weight: 600; line-height: 1.3;">
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
# VARIANTE K2-C: Tarjetas con Estructura de 2 Columnas Verticales Claras
# -----------------------------------------------------------------------------
K2_C_HTML = '''
<section class="slide s-white active" id="slide-12-k2-c">
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

    <!-- EL FOCO PRINCIPAL: Gráfica Centrada (124px de altura) -->
    <div>
      
      <!-- Fila superior -->
      <div style="display: flex; width: 100%; margin-bottom: 8px; align-items: flex-end;">
        <div style="width: 40%; font-family: var(--font-mono); font-size: 22px; font-weight: 700; color: var(--c-wine-primary); padding-left: 4px;">
          Q(r, q, C) = 0.40·G + 0.40·R + 0.20·L
        </div>
        <div style="width: 60%; font-family: var(--font-sans); font-size: 21px; font-weight: 800; color: var(--c-red-accent); text-align: center; background: #FFE4E6; border: 1.5px solid var(--c-red-accent); padding: 4px 0;">
          ▼ ¡EL 60% DE LA NOTA NO EVALÚA EL CONTENIDO DE LA RESPUESTA!
        </div>
      </div>

      <!-- Barra Segmentada Oficial (124px de alto) -->
      <div class="formula-segmented-bar" style="margin: 0; height: 124px; border: 2px solid #2C0509;">
        <div class="formula-segment" style="width: 40%; background-color: var(--c-wine-primary); justify-content: center; padding: 10px 18px;">
          <div class="formula-seg-pct" style="font-size: 46px; color: var(--c-gold); line-height: 1;">40%</div>
          <div class="formula-seg-label" style="font-size: 23px; letter-spacing: 0.5px; margin-top: 4px;">GROUNDING (r, C)</div>
          <div style="font-size: 20px; opacity: 0.95; font-weight: 600; margin-top: 3px;">
            Único término que evalúa la respuesta generada
          </div>
        </div>

        <div class="formula-segment" style="width: 40%; background-color: var(--c-red-accent); border-left: 2px solid #FFFFFF; justify-content: center; padding: 10px 18px;">
          <div class="formula-seg-pct" style="font-size: 46px; line-height: 1;">40%</div>
          <div class="formula-seg-label" style="font-size: 23px; letter-spacing: 0.5px; margin-top: 4px;">RELEVANCE (q, C)</div>
          <div style="font-size: 20px; opacity: 0.95; font-weight: 600; margin-top: 3px;">
            Pregunta vs. contexto · ¡Ignora la respuesta!
          </div>
        </div>

        <div class="formula-segment" style="width: 20%; background-color: #B38600; border-left: 2px solid #FFFFFF; justify-content: center; padding: 10px 18px;">
          <div class="formula-seg-pct" style="font-size: 46px; line-height: 1;">20%</div>
          <div class="formula-seg-label" style="font-size: 23px; letter-spacing: 0.5px; margin-top: 4px;">LONGITUD (r)</div>
          <div style="font-size: 20px; opacity: 0.95; font-weight: 600; margin-top: 3px;">
            Conteo de caracteres
          </div>
        </div>
      </div>

    </div>

    <!-- TARJETAS CON BADGE ARRIBA A LA DERECHA Y FONDO BLANCO PURO -->
    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 28px;">
      
      <!-- Distorsión 01 -->
      <div style="background: #FFFFFF; border: 2px solid var(--c-wine-primary); padding: 18px 22px;">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
          <span style="font-family: var(--font-sans); font-size: 23px; font-weight: 800; color: var(--c-wine-dark);">
            Coseno Reescalado: (x + 1)/2
          </span>
          <span style="font-family: var(--font-mono); font-size: 21px; font-weight: 800; color: var(--c-wine-primary); background: #FAF5F5; border: 1.5px solid var(--c-wine-primary); padding: 2px 10px;">
            0.00 → 0.50
          </span>
        </div>
        <div style="font-family: var(--font-sans); font-size: 22px; color: #110103; font-weight: 600; line-height: 1.35;">
          Una similitud nula se convierte en nota de <strong>0.50 aprobatorio</strong>, inflando respuestas desconectadas del libro.
        </div>
      </div>

      <!-- Distorsión 02 -->
      <div style="background: #FFFFFF; border: 2px solid var(--c-red-accent); padding: 18px 22px;">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
          <span style="font-family: var(--font-sans); font-size: 23px; font-weight: 800; color: var(--c-wine-dark);">
            Premio al Rechazo: 9 Frases
          </span>
          <span style="font-family: var(--font-mono); font-size: 21px; font-weight: 800; color: var(--c-red-accent); background: #FFE4E6; border: 1.5px solid var(--c-red-accent); padding: 2px 10px;">
            Nota = 0.80
          </span>
        </div>
        <div style="font-family: var(--font-sans); font-size: 22px; color: #110103; font-weight: 600; line-height: 1.35;">
          Nueve frases fijas de abstención reciben <strong>0.80 automático</strong>, dando ventaja artificial a modelos que no arriesgan.
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
  <title>Test K2 Refinements</title>
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
    test_files = [
        ('slide_12_k2_a.html', 'slide_12_k2_a.png', K2_A_HTML),
        ('slide_12_k2_b.html', 'slide_12_k2_b.png', K2_B_HTML),
        ('slide_12_k2_c.html', 'slide_12_k2_c.png', K2_C_HTML)
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
