# -*- coding: utf-8 -*-
"""
Pruebas de descongestión y jerarquía visual para Slide 12.
Resuelve la queja del usuario:
1. Usa el estilo de barra con esquinas rectas de slide_12.html (sin border-radius que choque con el estilo).
2. Crea un foco principal inequívoco en el que fijarse (el 60% ciego / puntero de fig1_ecuacion_terminos.png).
3. Elimina la sobrecarga: retira la fórmula gris duplicada y descongestiona los textos inferiores.
"""
import os
from playwright.sync_api import sync_playwright

output_dir = r"C:\Users\ASUS\.gemini\antigravity-ide\brain\a6624504-511c-4b9d-bc9a-468e348bde40"
os.makedirs(output_dir, exist_ok=True)

# -----------------------------------------------------------------------------
# VARIANTE 1: Hero Barra Segmentada con Puntero de Alerta (Inspirado en Fig 1)
# -----------------------------------------------------------------------------
VARIANTE_1_HTML = '''
<section class="slide s-white active" id="slide-12-v1">
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
    <h2 class="s-lead-question" style="font-size: 38px; font-weight: 800; margin-bottom: 24px; line-height: 1.2;">
      Anatomía de la fórmula: el 60% de la calificación ignora la respuesta del modelo
    </h2>

    <!-- BLOQUE HERO PRINCIPAL: La Barra Segmentada de la Figura 1 (Esquinas rectas, 100% plano) -->
    <div style="background: #FAF5F5; border: 2px solid var(--c-wine-primary); padding: 20px 24px; margin-bottom: 26px;">
      
      <!-- Fila superior: Llamado de atención focal sobre el 60% -->
      <div style="display: flex; justify-content: space-between; align-items: flex-end; margin-bottom: 10px;">
        <span style="font-family: var(--font-mono); font-size: 21px; font-weight: 700; color: var(--c-wine-dark);">
          Q(r, q, C) = 0.40·grounding + 0.40·relevance + 0.20·longitud
        </span>
        <span style="font-family: var(--font-sans); font-size: 20px; font-weight: 800; color: var(--c-red-accent); display: flex; align-items: center; gap: 6px;">
          <span>▼</span> ¡El 60% de la nota final es ciego al contenido de la respuesta!
        </span>
      </div>

      <!-- Barra Segmentada Oficial (Esquinas Rectas) -->
      <div style="display: flex; width: 100%; height: 96px; border: 1.5px solid #2C0509;">
        <!-- 40% Grounding -->
        <div style="width: 40%; background-color: var(--c-wine-primary); color: #FFFFFF; display: flex; flex-direction: column; align-items: center; justify-content: center; padding: 6px 12px; text-align: center;">
          <div style="font-family: var(--font-mono); font-size: 36px; font-weight: 800; line-height: 1; color: var(--c-gold);">40%</div>
          <div style="font-family: var(--font-sans); font-size: 21px; font-weight: 700; letter-spacing: 0.5px; margin-top: 4px;">GROUNDING (r, C)</div>
          <div style="font-family: var(--font-sans); font-size: 19px; opacity: 0.95; font-weight: 600;">Único término que evalúa la respuesta generada</div>
        </div>

        <!-- 40% Relevance -->
        <div style="width: 40%; background-color: var(--c-red-accent); color: #FFFFFF; display: flex; flex-direction: column; align-items: center; justify-content: center; padding: 6px 12px; text-align: center; border-left: 2px solid #FFFFFF;">
          <div style="font-family: var(--font-mono); font-size: 36px; font-weight: 800; line-height: 1;">40%</div>
          <div style="font-family: var(--font-sans); font-size: 21px; font-weight: 700; letter-spacing: 0.5px; margin-top: 4px;">RELEVANCE (q, C)</div>
          <div style="font-family: var(--font-sans); font-size: 19px; opacity: 0.95; font-weight: 600;">Pregunta vs. contexto · ¡Ignora la respuesta!</div>
        </div>

        <!-- 20% Longitud -->
        <div style="width: 20%; background-color: #B38600; color: #FFFFFF; display: flex; flex-direction: column; align-items: center; justify-content: center; padding: 6px 12px; text-align: center; border-left: 2px solid #FFFFFF;">
          <div style="font-family: var(--font-mono); font-size: 36px; font-weight: 800; line-height: 1;">20%</div>
          <div style="font-family: var(--font-sans); font-size: 21px; font-weight: 700; letter-spacing: 0.5px; margin-top: 4px;">LONGITUD (r)</div>
          <div style="font-family: var(--font-sans); font-size: 19px; opacity: 0.95; font-weight: 600;">Conteo de caracteres</div>
        </div>
      </div>

    </div>

    <!-- SEGUNDO BLOQUE: Dos Distorsiones de Código (Descongestionadas y con Foco Claro) -->
    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 28px;">
      
      <!-- Trampa 1 -->
      <div style="background: #FFFFFF; border: 2px solid var(--c-wine-primary); padding: 22px 24px; display: flex; flex-direction: column; justify-content: space-between;">
        <div>
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px;">
            <span style="font-family: var(--font-mono); font-size: 18px; font-weight: 800; color: var(--c-wine-primary); letter-spacing: 1px;">DISTORSIÓN EN CÓDIGO 01</span>
            <span style="font-family: var(--font-mono); font-size: 20px; font-weight: 800; color: var(--c-wine-primary); background: #FAF5F5; border: 1.5px solid var(--c-wine-primary); padding: 2px 10px;">(x + 1) / 2</span>
          </div>
          <h3 style="font-family: var(--font-sans); font-size: 26px; font-weight: 800; color: var(--c-wine-dark); margin: 0 0 10px 0;">
            Coseno Reescalado Artificialmente
          </h3>
          <p style="font-family: var(--font-sans); font-size: 22px; color: #110103; font-weight: 600; line-height: 1.35; margin: 0;">
            Una similitud nula (<strong>0.00</strong>) se transforma matemáticamente en <strong>0.50</strong>. Cualquier respuesta desconectada parte con medio punto aprobado garantizado.
          </p>
        </div>
        <div style="margin-top: 14px; padding-top: 10px; border-top: 1.5px solid rgba(70,8,17,0.2); font-family: var(--font-sans); font-size: 21px; color: var(--c-wine-dark); font-weight: 700;">
          Efecto: Califica como válidas respuestas mediocres.
        </div>
      </div>

      <!-- Trampa 2 -->
      <div style="background: #FFFFFF; border: 2px solid var(--c-red-accent); padding: 22px 24px; display: flex; flex-direction: column; justify-content: space-between;">
        <div>
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px;">
            <span style="font-family: var(--font-mono); font-size: 18px; font-weight: 800; color: var(--c-red-accent); letter-spacing: 1px;">DISTORSIÓN EN CÓDIGO 02</span>
            <span style="font-family: var(--font-mono); font-size: 20px; font-weight: 800; color: var(--c-red-accent); background: #FFE4E6; border: 1.5px solid var(--c-red-accent); padding: 2px 10px;">NOTA = 0.80</span>
          </div>
          <h3 style="font-family: var(--font-sans); font-size: 26px; font-weight: 800; color: var(--c-wine-dark); margin: 0 0 10px 0;">
            Bonificación Fija al Rechazo
          </h3>
          <p style="font-family: var(--font-sans); font-size: 22px; color: #110103; font-weight: 600; line-height: 1.35; margin: 0;">
            Nueve frases de abstención reciben una nota automática de <strong>0.80</strong>. Bonifica igual la prudencia legítima que un fallo por bloqueo léxico.
          </p>
        </div>
        <div style="margin-top: 14px; padding-top: 10px; border-top: 1.5px solid rgba(201,16,27,0.2); font-family: var(--font-sans); font-size: 21px; color: var(--c-red-accent); font-weight: 700;">
          Efecto: Ventaja artificial a modelos sobre-conservadores.
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
# VARIANTE 2: Barra Integrada Directa (Sin marco exterior) + Tarjetas Clarísimas
# -----------------------------------------------------------------------------
VARIANTE_2_HTML = '''
<section class="slide s-white active" id="slide-12-v2">
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
      Anatomía de la fórmula: la métrica que califica al modelo sin leer su respuesta
    </h2>

    <!-- Barra de Puntero Superior que focaliza la atención -->
    <div style="display: flex; width: 100%; margin-bottom: 6px;">
      <div style="width: 40%; font-family: var(--font-sans); font-size: 19px; font-weight: 800; color: var(--c-wine-primary); padding-left: 4px;">
        ● ÚNICO TÉRMINO ACTIVO (40%)
      </div>
      <div style="width: 60%; font-family: var(--font-sans); font-size: 20px; font-weight: 800; color: var(--c-red-accent); text-align: center; background: #FFE4E6; border: 1.5px solid var(--c-red-accent); padding: 4px 0;">
        ▲ 60% DE LA CALIFICACIÓN NO EVALÚA LA RESPUESTA DEL MODELO
      </div>
    </div>

    <!-- Barra Segmentada Oficial (Esquinas 100% Rectas) -->
    <div class="formula-segmented-bar" style="margin: 0 0 28px 0; height: 96px; border: 2px solid #2C0509;">
      <div class="formula-segment" style="width: 40%; background-color: var(--c-wine-primary);">
        <div class="formula-seg-pct" style="color: var(--c-gold); font-size: 38px;">40%</div>
        <div class="formula-seg-label" style="font-size: 21px;">GROUNDING (r, C)</div>
        <div style="font-size: 18px; opacity: 0.95; font-weight: 600;">Compara la respuesta generada con el libro</div>
      </div>
      <div class="formula-segment" style="width: 40%; background-color: var(--c-red-accent); border-left: 2px solid #FFFFFF;">
        <div class="formula-seg-pct" style="font-size: 38px;">40%</div>
        <div class="formula-seg-label" style="font-size: 21px;">RELEVANCE (q, C)</div>
        <div style="font-size: 18px; opacity: 0.95; font-weight: 600;">Pregunta vs. contexto · ¡Ignora la respuesta!</div>
      </div>
      <div class="formula-segment" style="width: 20%; background-color: #B38600; border-left: 2px solid #FFFFFF;">
        <div class="formula-seg-pct" style="font-size: 38px;">20%</div>
        <div class="formula-seg-label" style="font-size: 21px;">LONGITUD (r)</div>
        <div style="font-size: 18px; opacity: 0.95; font-weight: 600;">Solo cuenta cantidad de caracteres</div>
      </div>
    </div>

    <!-- Dos Trampas de Código: Esquinas Rectas, Estilo Plano Puro -->
    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 28px;">
      
      <!-- Trampa 1 -->
      <div style="background: #FAF5F5; border: 2px solid var(--c-wine-primary); padding: 22px 26px; display: flex; flex-direction: column; justify-content: space-between;">
        <div>
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
            <span style="font-family: var(--font-mono); font-size: 18px; font-weight: 800; color: var(--c-wine-primary); letter-spacing: 1px;">DISTORSIÓN EN CÓDIGO 01</span>
            <span style="font-family: var(--font-mono); font-size: 20px; font-weight: 800; color: var(--c-wine-primary); background: #FFFFFF; border: 1.5px solid var(--c-wine-primary); padding: 2px 10px;">(x + 1) / 2</span>
          </div>
          <h3 style="font-family: var(--font-sans); font-size: 26px; font-weight: 800; color: var(--c-wine-dark); margin: 0 0 12px 0;">
            Coseno Reescalado: Similitud 0.00 → 0.50
          </h3>
          <p style="font-family: var(--font-sans); font-size: 22px; color: #110103; font-weight: 600; line-height: 1.4; margin: 0;">
            Al transformar el rango [-1, 1] a [0, 1], cualquier respuesta desconectada o incoherente obtiene automáticamente un <strong>0.50 aprobatorio</strong> como nota base garantizada.
          </p>
        </div>
        <div style="margin-top: 14px; padding-top: 10px; border-top: 1.5px solid rgba(70,8,17,0.2); font-family: var(--font-sans); font-size: 21px; color: var(--c-wine-dark); font-weight: 700;">
          Efecto: Respuestas mediocres son calificadas como válidas.
        </div>
      </div>

      <!-- Trampa 2 -->
      <div style="background: #FAF5F5; border: 2px solid var(--c-red-accent); padding: 22px 26px; display: flex; flex-direction: column; justify-content: space-between;">
        <div>
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
            <span style="font-family: var(--font-mono); font-size: 18px; font-weight: 800; color: var(--c-red-accent); letter-spacing: 1px;">DISTORSIÓN EN CÓDIGO 02</span>
            <span style="font-family: var(--font-mono); font-size: 20px; font-weight: 800; color: var(--c-red-accent); background: #FFFFFF; border: 1.5px solid var(--c-red-accent); padding: 2px 10px;">NOTA = 0.80</span>
          </div>
          <h3 style="font-family: var(--font-sans); font-size: 26px; font-weight: 800; color: var(--c-wine-dark); margin: 0 0 12px 0;">
            Premio Fijo al Rechazo: 9 Frases = 0.80
          </h3>
          <p style="font-family: var(--font-sans); font-size: 22px; color: #110103; font-weight: 600; line-height: 1.4; margin: 0;">
            Nueve frases literales de abstención otorgan nota fija inmediata de <strong>0.80</strong>. Bonifica idéntico la abstención legítima que el fallo por torpeza del buscador.
          </p>
        </div>
        <div style="margin-top: 14px; padding-top: 10px; border-top: 1.5px solid rgba(201,16,27,0.2); font-family: var(--font-sans); font-size: 21px; color: var(--c-red-accent); font-weight: 700;">
          Efecto: Ventaja artificial a modelos sobre-conservadores.
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
# VARIANTE 3: Foco Extremo en la Ecuación 1 (Hero Centralizado con Cifras Rectoras)
# -----------------------------------------------------------------------------
VARIANTE_3_HTML = '''
<section class="slide s-white active" id="slide-12-v3">
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
    <h2 class="s-lead-question" style="font-size: 38px; font-weight: 800; margin-bottom: 18px; line-height: 1.2;">
      Anatomía de la fórmula: el 60% de la calificación ignora la respuesta del modelo
    </h2>

    <!-- Banner Panorámico Superior con el Gran Mensaje Focal -->
    <div style="background: #FFFFFF; border: 2px solid #2C0509; padding: 14px 24px; display: flex; align-items: center; justify-content: space-between; margin-bottom: 20px;">
      <div style="display: flex; align-items: baseline; gap: 14px;">
        <span style="font-family: var(--font-mono); font-size: 48px; font-weight: 800; color: var(--c-red-accent); line-height: 1;">60%</span>
        <span style="font-family: var(--font-sans); font-size: 23px; font-weight: 800; color: #110103;">
          DE LA NOTA ES INDEPENDIENTE DE LA RESPUESTA
        </span>
      </div>
      <div style="font-family: var(--font-mono); font-size: 20px; font-weight: 700; color: var(--c-wine-primary); background: #FAF5F5; padding: 4px 14px; border: 1.5px solid var(--c-wine-primary);">
        Q = 0.40·G + 0.40·R + 0.20·L
      </div>
    </div>

    <!-- Barra Segmentada Oficial (Esquinas 100% Rectas) -->
    <div class="formula-segmented-bar" style="margin: 0 0 24px 0; height: 96px; border: 2px solid #2C0509;">
      <div class="formula-segment" style="width: 40%; background-color: var(--c-wine-primary);">
        <div class="formula-seg-pct" style="color: var(--c-gold); font-size: 36px;">40%</div>
        <div class="formula-seg-label" style="font-size: 21px;">GROUNDING (r, C)</div>
        <div style="font-size: 18px; opacity: 0.95; font-weight: 600;">Único término que evalúa la respuesta</div>
      </div>
      <div class="formula-segment" style="width: 40%; background-color: var(--c-red-accent); border-left: 2px solid #FFFFFF;">
        <div class="formula-seg-pct" style="font-size: 36px;">40%</div>
        <div class="formula-seg-label" style="font-size: 21px;">RELEVANCE (q, C)</div>
        <div style="font-size: 18px; opacity: 0.95; font-weight: 600;">Pregunta vs. contexto · ¡Ignora la respuesta!</div>
      </div>
      <div class="formula-segment" style="width: 20%; background-color: #B38600; border-left: 2px solid #FFFFFF;">
        <div class="formula-seg-pct" style="font-size: 36px;">20%</div>
        <div class="formula-seg-label" style="font-size: 21px;">LONGITUD (r)</div>
        <div style="font-size: 18px; opacity: 0.95; font-weight: 600;">Mide cantidad de caracteres</div>
      </div>
    </div>

    <!-- Fila Inferior de Alertas: Dos Paneles Compactos y Contundentes -->
    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 24px;">
      <div style="background: #FAF5F5; border: 2px solid var(--c-wine-primary); padding: 18px 22px;">
        <div style="display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 6px;">
          <span style="font-family: var(--font-sans); font-size: 22px; font-weight: 800; color: var(--c-wine-dark);">
            Coseno Reescalado (x + 1)/2
          </span>
          <span style="font-family: var(--font-mono); font-size: 20px; font-weight: 800; color: var(--c-wine-primary);">
            0.00 → 0.50
          </span>
        </div>
        <div style="font-family: var(--font-sans); font-size: 21px; color: #110103; font-weight: 600; line-height: 1.35;">
          Una similitud nula se convierte en nota aprobatoria de <strong>0.50</strong>, inflando respuestas sin sentido.
        </div>
      </div>

      <div style="background: #FAF5F5; border: 2px solid var(--c-red-accent); padding: 18px 22px;">
        <div style="display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 6px;">
          <span style="font-family: var(--font-sans); font-size: 22px; font-weight: 800; color: var(--c-wine-dark);">
            Bonificación Fija al Rechazo
          </span>
          <span style="font-family: var(--font-mono); font-size: 20px; font-weight: 800; color: var(--c-red-accent);">
            Nota = 0.80
          </span>
        </div>
        <div style="font-family: var(--font-sans); font-size: 21px; color: #110103; font-weight: 600; line-height: 1.35;">
          Nueve frases fijas reciben <strong>0.80 automático</strong>, dando ventaja artificial a modelos que no arriesgan.
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
  <title>Test Slide 12 Declutter</title>
  <link rel="stylesheet" href="http://localhost:8085/styles.css?v=15">
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
        ('slide_12_v1.html', 'slide_12_v1.png', VARIANTE_1_HTML),
        ('slide_12_v2.html', 'slide_12_v2.png', VARIANTE_2_HTML),
        ('slide_12_v3.html', 'slide_12_v3.png', VARIANTE_3_HTML)
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
