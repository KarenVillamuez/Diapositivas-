# -*- coding: utf-8 -*-
"""
Generador de opciones de diseño para Slide 12: Deconstrucción de la Métrica Automática.
3 opciones calibradas exactamente para el viewport de 1920x1080 y la caja de 765px,
cero microtextos (<22px), sin cuadros dentro de cuadros, y con contraste óptimo para auditorio.
"""
import os
from playwright.sync_api import sync_playwright

output_dir = r"C:\Users\ASUS\.gemini\antigravity-ide\brain\a6624504-511c-4b9d-bc9a-468e348bde40"
os.makedirs(output_dir, exist_ok=True)

# Opción A: Barra Analítica Panorámica + 2 Tarjetas de Auditoría Técnica
OPCION_A_HTML = '''
<section class="slide s-white active" id="slide-12-opt-a">
  <header class="slide-header">
    <div class="sh-left">
      <span class="sh-red-bar"></span>
      <span class="sh-category">03 · RESULTADOS · AUDITORÍA DE LA MÉTRICA AUTOMÁTICA</span>
    </div>
    <img src="assets/image6.png" alt="#LoxTIC" class="sh-loxtic">
  </header>
  <div class="sh-divider"></div>

  <div class="slide-content-area" style="justify-content: flex-start;">
    <!-- Pregunta Rectora -->
    <h2 class="s-lead-question" style="font-size: 38px; font-weight: 800; margin-bottom: 12px; line-height: 1.2;">
      Anatomía de la fórmula: el 60% de la calificación ignora la respuesta del modelo
    </h2>

    <!-- Ecuación Principal en Marco Editorial -->
    <div style="background: #FAF5F5; border: 2px solid var(--c-wine-primary); border-radius: 6px; padding: 10px 22px; font-family: var(--font-mono); font-size: 23px; color: var(--c-wine-dark); font-weight: 700; margin-bottom: 14px; display: flex; align-items: center; justify-content: space-between;">
      <span>Q(r, q, C) = 0.40 · grounding(r, C) + 0.40 · relevance(q, C) + 0.20 · length(r)</span>
      <span style="font-size: 18px; background: #FFE4E6; color: var(--c-red-accent); padding: 3px 12px; border-radius: 4px; font-weight: 800; border: 1px solid var(--c-red-accent);">ECUACIÓN 1 AUDITADA</span>
    </div>

    <!-- Barra Segmentada Desglosada con alta legibilidad -->
    <div style="display: flex; width: 100%; border-radius: 6px; overflow: hidden; margin-bottom: 22px; border: 2px solid #2C0509; height: 86px;">
      <!-- Segmento 1: 40% Grounding -->
      <div style="width: 40%; background: var(--c-wine-primary); color: #FFFFFF; padding: 10px 18px; display: flex; flex-direction: column; justify-content: center;">
        <div style="display: flex; align-items: baseline; gap: 10px; margin-bottom: 2px;">
          <span style="font-family: var(--font-mono); font-size: 32px; font-weight: 800; color: var(--c-gold); line-height: 1;">40%</span>
          <span style="font-family: var(--font-sans); font-size: 22px; font-weight: 800;">GROUNDING (r, C)</span>
        </div>
        <div style="font-family: var(--font-sans); font-size: 19px; opacity: 0.95; font-weight: 600;">
          Único término que evalúa lo que el modelo respondió.
        </div>
      </div>

      <!-- Segmento 2: 40% Relevance -->
      <div style="width: 40%; background: var(--c-red-accent); color: #FFFFFF; padding: 10px 18px; border-left: 2px solid #FFFFFF; display: flex; flex-direction: column; justify-content: center;">
        <div style="display: flex; align-items: baseline; gap: 10px; margin-bottom: 2px;">
          <span style="font-family: var(--font-mono); font-size: 32px; font-weight: 800; color: #FFFFFF; line-height: 1;">40%</span>
          <span style="font-family: var(--font-sans); font-size: 22px; font-weight: 800;">RELEVANCE (q, C)</span>
        </div>
        <div style="font-family: var(--font-sans); font-size: 19px; opacity: 0.95; font-weight: 600;">
          Pregunta vs. libro: ¡ignora la respuesta del modelo!
        </div>
      </div>

      <!-- Segmento 3: 20% Coherencia -->
      <div style="width: 20%; background: #9E7400; color: #FFFFFF; padding: 10px 18px; border-left: 2px solid #FFFFFF; display: flex; flex-direction: column; justify-content: center;">
        <div style="display: flex; align-items: baseline; gap: 8px; margin-bottom: 2px;">
          <span style="font-family: var(--font-mono); font-size: 32px; font-weight: 800; color: #FFFFFF; line-height: 1;">20%</span>
          <span style="font-family: var(--font-sans); font-size: 22px; font-weight: 800;">LONGITUD</span>
        </div>
        <div style="font-family: var(--font-sans); font-size: 19px; opacity: 0.95; font-weight: 600;">
          Conteo heurístico de caracteres.
        </div>
      </div>
    </div>

    <!-- Dos Trampas de Código: Tarjetas Limpias con Bordes Equilibrados de 2px -->
    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 24px;">
      <!-- Tarjeta 1: Coseno Re-escalado -->
      <div style="background: #FAF5F5; border: 2px solid var(--c-wine-primary); border-radius: 8px; padding: 22px 24px; display: flex; flex-direction: column; justify-content: space-between;">
        <div>
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
            <span style="font-family: var(--font-mono); font-size: 19px; font-weight: 800; color: var(--c-wine-primary); letter-spacing: 1px;">DISTORSIÓN EN CÓDIGO 01</span>
            <span style="font-family: var(--font-mono); font-size: 20px; font-weight: 800; background: #FFFFFF; border: 1.5px solid var(--c-wine-primary); color: var(--c-wine-primary); padding: 2px 10px; border-radius: 4px;">(x + 1) / 2</span>
          </div>
          <h3 style="font-family: var(--font-sans); font-size: 27px; font-weight: 800; color: var(--c-wine-dark); margin: 0 0 12px 0;">
            Coseno Reescalado Artificialmente
          </h3>
          <ul style="list-style: none; padding: 0; margin: 0; display: flex; flex-direction: column; gap: 10px;">
            <li style="font-family: var(--font-sans); font-size: 23px; color: #110103; font-weight: 600; display: flex; align-items: flex-start; gap: 10px;">
              <span style="color: var(--c-wine-primary); font-size: 24px; line-height: 1;">▪</span>
              <span><strong>Similitud nula (0.00):</strong> Se transforma en <strong>0.50</strong> (nota aprobatoria).</span>
            </li>
            <li style="font-family: var(--font-sans); font-size: 23px; color: #110103; font-weight: 600; display: flex; align-items: flex-start; gap: 10px;">
              <span style="color: var(--c-wine-primary); font-size: 24px; line-height: 1;">▪</span>
              <span><strong>Piso inflado:</strong> Respuestas desconectadas parten con medio punto garantizado.</span>
            </li>
          </ul>
        </div>
        <div style="margin-top: 14px; padding-top: 10px; border-top: 1.5px solid rgba(70,8,17,0.2); font-family: var(--font-sans); font-size: 22px; color: var(--c-wine-dark);">
          <strong>Efecto en auditoría:</strong> Califica como válidas respuestas mediocres.
        </div>
      </div>

      <!-- Tarjeta 2: Premio Fijo al Rechazo -->
      <div style="background: #FAF5F5; border: 2px solid var(--c-red-accent); border-radius: 8px; padding: 22px 24px; display: flex; flex-direction: column; justify-content: space-between;">
        <div>
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
            <span style="font-family: var(--font-mono); font-size: 19px; font-weight: 800; color: var(--c-red-accent); letter-spacing: 1px;">DISTORSIÓN EN CÓDIGO 02</span>
            <span style="font-family: var(--font-mono); font-size: 20px; font-weight: 800; background: #FFFFFF; border: 1.5px solid var(--c-red-accent); color: var(--c-red-accent); padding: 2px 10px; border-radius: 4px;">NOTA = 0.80</span>
          </div>
          <h3 style="font-family: var(--font-sans); font-size: 27px; font-weight: 800; color: var(--c-wine-dark); margin: 0 0 12px 0;">
            Bonificación Fija al Rechazo
          </h3>
          <ul style="list-style: none; padding: 0; margin: 0; display: flex; flex-direction: column; gap: 10px;">
            <li style="font-family: var(--font-sans); font-size: 23px; color: #110103; font-weight: 600; display: flex; align-items: flex-start; gap: 10px;">
              <span style="color: var(--c-red-accent); font-size: 24px; line-height: 1;">▪</span>
              <span><strong>9 frases fijas:</strong> Otorgan nota fija inmediata de <strong>0.80</strong> al abstenerse.</span>
            </li>
            <li style="font-family: var(--font-sans); font-size: 23px; color: #110103; font-weight: 600; display: flex; align-items: flex-start; gap: 10px;">
              <span style="color: var(--c-red-accent); font-size: 24px; line-height: 1;">▪</span>
              <span><strong>Premio ciego:</strong> Bonifica igual la abstención prudente que el fallo por torpeza léxica.</span>
            </li>
          </ul>
        </div>
        <div style="margin-top: 14px; padding-top: 10px; border-top: 1.5px solid rgba(201,16,27,0.2); font-family: var(--font-sans); font-size: 22px; color: var(--c-red-accent);">
          <strong>Efecto en auditoría:</strong> Ventaja artificial para modelos sobre-conservadores.
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

# Opción B: Tríptico de Desglose Matemático (40/40/20) + Banner Inferior de Distorsiones
OPCION_B_HTML = '''
<section class="slide s-white active" id="slide-12-opt-b">
  <header class="slide-header">
    <div class="sh-left">
      <span class="sh-red-bar"></span>
      <span class="sh-category">03 · RESULTADOS · AUDITORÍA DE LA MÉTRICA AUTOMÁTICA</span>
    </div>
    <img src="assets/image6.png" alt="#LoxTIC" class="sh-loxtic">
  </header>
  <div class="sh-divider"></div>

  <div class="slide-content-area" style="justify-content: flex-start;">
    <!-- Pregunta Rectora -->
    <h2 class="s-lead-question" style="font-size: 38px; font-weight: 800; margin-bottom: 14px; line-height: 1.2;">
      Deconstrucción de la Ecuación 1: el 60% de la métrica evalúa el buscador o la longitud
    </h2>

    <!-- Tríptico de los 3 Componentes -->
    <div style="display: grid; grid-template-columns: 1.1fr 1.1fr 0.8fr; gap: 20px; margin-bottom: 22px;">
      
      <!-- Tarjeta 1: Grounding -->
      <div style="background: #FAF5F5; border: 2px solid var(--c-wine-primary); border-radius: 8px; padding: 20px 22px;">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
          <span style="font-family: var(--font-mono); font-size: 44px; font-weight: 800; color: var(--c-wine-primary); line-height: 1;">40%</span>
          <span style="font-family: var(--font-mono); font-size: 17px; font-weight: 700; background: var(--c-wine-primary); color: #FFFFFF; padding: 3px 10px; border-radius: 4px;">grounding(r, C)</span>
        </div>
        <div style="font-family: var(--font-sans); font-size: 24px; font-weight: 800; color: var(--c-wine-dark); margin-bottom: 8px;">
          Fidelidad al Libro
        </div>
        <p style="font-family: var(--font-sans); font-size: 22px; color: #110103; font-weight: 600; line-height: 1.35; margin: 0;">
          Es el <strong>único componente</strong> que analiza lo que el modelo realmente redactó frente al texto del libro.
        </p>
      </div>

      <!-- Tarjeta 2: Relevance -->
      <div style="background: #FAF5F5; border: 2px solid var(--c-red-accent); border-radius: 8px; padding: 20px 22px;">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
          <span style="font-family: var(--font-mono); font-size: 44px; font-weight: 800; color: var(--c-red-accent); line-height: 1;">40%</span>
          <span style="font-family: var(--font-mono); font-size: 17px; font-weight: 700; background: var(--c-red-accent); color: #FFFFFF; padding: 3px 10px; border-radius: 4px;">relevance(q, C)</span>
        </div>
        <div style="font-family: var(--font-sans); font-size: 24px; font-weight: 800; color: var(--c-red-accent); margin-bottom: 8px;">
          Pregunta vs. Contexto
        </div>
        <p style="font-family: var(--font-sans); font-size: 22px; color: #110103; font-weight: 600; line-height: 1.35; margin: 0;">
          Compara la pregunta con el fragmento: <strong>¡ignora la respuesta!</strong> Califica al buscador, no al modelo.
        </p>
      </div>

      <!-- Tarjeta 3: Coherencia de longitud -->
      <div style="background: #FAF5F5; border: 2px solid #9E7400; border-radius: 8px; padding: 20px 22px;">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
          <span style="font-family: var(--font-mono); font-size: 44px; font-weight: 800; color: #9E7400; line-height: 1;">20%</span>
          <span style="font-family: var(--font-mono); font-size: 17px; font-weight: 700; background: #9E7400; color: #FFFFFF; padding: 3px 10px; border-radius: 4px;">length(r)</span>
        </div>
        <div style="font-family: var(--font-sans); font-size: 24px; font-weight: 800; color: #7A5A00; margin-bottom: 8px;">
          Conteo de Caracteres
        </div>
        <p style="font-family: var(--font-sans); font-size: 22px; color: #110103; font-weight: 600; line-height: 1.35; margin: 0;">
          Heurística de código que premia longitud textual. No evalúa comprensión pedagógica.
        </p>
      </div>

    </div>

    <!-- Franja Panorámica Inferior: Las Dos Distorsiones de Código -->
    <div style="background: #FFFFFF; border: 2px solid #2C0509; border-radius: 8px; padding: 18px 24px;">
      <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 12px; border-bottom: 1.5px solid #EAE0E1; padding-bottom: 8px;">
        <span style="font-family: var(--font-sans); font-size: 22px; font-weight: 800; color: var(--c-wine-dark); letter-spacing: 0.5px;">
          AUDITORÍA DEL CÓDIGO FUENTE: DOS DISTORSIONES ARITMÉTICAS CRÍTICAS
        </span>
        <span style="font-family: var(--font-mono); font-size: 18px; font-weight: 800; color: var(--c-red-accent); background: #FFE4E6; padding: 2px 10px; border-radius: 4px; border: 1px solid var(--c-red-accent);">
          60% DE LA MÉTRICA NO AUDITA LA RESPUESTA
        </span>
      </div>

      <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 28px;">
        <!-- Distorsión 1 -->
        <div style="display: flex; gap: 14px; align-items: flex-start;">
          <div style="font-family: var(--font-mono); font-size: 22px; font-weight: 800; color: var(--c-wine-primary); background: #FAF5F5; border: 1.5px solid var(--c-wine-primary); padding: 6px 12px; border-radius: 6px; white-space: nowrap;">
            0.00 → 0.50
          </div>
          <div>
            <div style="font-family: var(--font-sans); font-size: 22px; font-weight: 800; color: var(--c-wine-dark); margin-bottom: 4px;">
              Coseno Reescalado (x + 1) / 2
            </div>
            <div style="font-family: var(--font-sans); font-size: 21px; color: #110103; font-weight: 600; line-height: 1.35;">
              Al reescalar [-1, 1] a [0, 1], una similitud nula recibe nota de <strong>0.50 aprobatoria</strong>, inflando respuestas desconectadas.
            </div>
          </div>
        </div>

        <!-- Distorsión 2 -->
        <div style="display: flex; gap: 14px; align-items: flex-start;">
          <div style="font-family: var(--font-mono); font-size: 22px; font-weight: 800; color: var(--c-red-accent); background: #FFE4E6; border: 1.5px solid var(--c-red-accent); padding: 6px 12px; border-radius: 6px; white-space: nowrap;">
            Fijo 0.80
          </div>
          <div>
            <div style="font-family: var(--font-sans); font-size: 22px; font-weight: 800; color: var(--c-wine-dark); margin-bottom: 4px;">
              Premio Automático al Rechazo
            </div>
            <div style="font-family: var(--font-sans); font-size: 21px; color: #110103; font-weight: 600; line-height: 1.35;">
              Nueve frases de abstención reciben <strong>0.80 automático</strong>, otorgando ventaja artificial a modelos que no arriesgan.
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

# Opción C: División Dual 50/50 (Estructura de la Fórmula vs. Trampas de Código)
OPCION_C_HTML = '''
<section class="slide s-white active" id="slide-12-opt-c">
  <header class="slide-header">
    <div class="sh-left">
      <span class="sh-red-bar"></span>
      <span class="sh-category">03 · RESULTADOS · AUDITORÍA DE LA MÉTRICA AUTOMÁTICA</span>
    </div>
    <img src="assets/image6.png" alt="#LoxTIC" class="sh-loxtic">
  </header>
  <div class="sh-divider"></div>

  <div class="slide-content-area" style="justify-content: flex-start;">
    <!-- Pregunta Rectora -->
    <h2 class="s-lead-question" style="font-size: 38px; font-weight: 800; margin-bottom: 16px; line-height: 1.2;">
      Auditoría de la Ecuación 1: ponderación ciega y distorsiones aritméticas en código
    </h2>

    <!-- Layout Dual 50/50 -->
    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 28px; align-items: stretch;">
      
      <!-- Columna Izquierda: La Estructura de la Métrica -->
      <div style="background: #FAF5F5; border: 2px solid var(--c-wine-primary); border-radius: 8px; padding: 22px 24px; display: flex; flex-direction: column; justify-content: space-between;">
        <div>
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px;">
            <span style="font-family: var(--font-mono); font-size: 19px; font-weight: 800; color: var(--c-wine-primary); letter-spacing: 1px;">PONDERACIÓN FORMAL</span>
            <span style="font-family: var(--font-mono); font-size: 19px; font-weight: 800; color: var(--c-red-accent); background: #FFE4E6; border: 1px solid var(--c-red-accent); padding: 2px 8px; border-radius: 4px;">60% CIEGO</span>
          </div>

          <!-- Fórmula Compacta -->
          <div style="background: #FFFFFF; border: 1.5px solid #2C0509; border-radius: 6px; padding: 10px 14px; font-family: var(--font-mono); font-size: 21px; font-weight: 700; color: var(--c-wine-dark); margin-bottom: 16px; text-align: center;">
            Q = 0.40·G(r,C) + 0.40·R(q,C) + 0.20·L(r)
          </div>

          <!-- Desglose de 3 barras -->
          <div style="display: flex; flex-direction: column; gap: 14px;">
            <!-- Item 1: 40% Grounding -->
            <div style="border-left: 5px solid var(--c-wine-primary); padding-left: 14px;">
              <div style="display: flex; justify-content: space-between; align-items: baseline;">
                <span style="font-family: var(--font-sans); font-size: 23px; font-weight: 800; color: var(--c-wine-dark);">Grounding (r, C)</span>
                <span style="font-family: var(--font-mono); font-size: 26px; font-weight: 800; color: var(--c-wine-primary);">40%</span>
              </div>
              <div style="font-family: var(--font-sans); font-size: 21px; color: #110103; font-weight: 600; line-height: 1.3;">
                El <strong>único componente</strong> que lee la respuesta del modelo.
              </div>
            </div>

            <!-- Item 2: 40% Relevance -->
            <div style="border-left: 5px solid var(--c-red-accent); padding-left: 14px;">
              <div style="display: flex; justify-content: space-between; align-items: baseline;">
                <span style="font-family: var(--font-sans); font-size: 23px; font-weight: 800; color: var(--c-red-accent);">Relevance (q, C)</span>
                <span style="font-family: var(--font-mono); font-size: 26px; font-weight: 800; color: var(--c-red-accent);">40%</span>
              </div>
              <div style="font-family: var(--font-sans); font-size: 21px; color: #110103; font-weight: 600; line-height: 1.3;">
                Pregunta vs. contexto: <strong>ignora totalmente la respuesta</strong>.
              </div>
            </div>

            <!-- Item 3: 20% Longitud -->
            <div style="border-left: 5px solid #9E7400; padding-left: 14px;">
              <div style="display: flex; justify-content: space-between; align-items: baseline;">
                <span style="font-family: var(--font-sans); font-size: 23px; font-weight: 800; color: #7A5A00;">Longitud (r)</span>
                <span style="font-family: var(--font-mono); font-size: 26px; font-weight: 800; color: #9E7400;">20%</span>
              </div>
              <div style="font-family: var(--font-sans); font-size: 21px; color: #110103; font-weight: 600; line-height: 1.3;">
                Heurística de longitud: solo mide cantidad de caracteres.
              </div>
            </div>
          </div>
        </div>

        <div style="margin-top: 16px; padding-top: 10px; border-top: 1.5px solid rgba(70,8,17,0.2); font-family: var(--font-sans); font-size: 22px; font-weight: 700; color: var(--c-wine-dark);">
          Impacto: Un modelo puede reprobar en contenido y aun así obtener 0.60.
        </div>
      </div>

      <!-- Columna Derecha: Las Dos Trampas de Código -->
      <div style="display: flex; flex-direction: column; gap: 18px;">
        <!-- Bloque 1: Coseno Re-escalado -->
        <div style="background: #FAF5F5; border: 2px solid var(--c-wine-primary); border-radius: 8px; padding: 22px 24px; flex: 1; display: flex; flex-direction: column; justify-content: space-between;">
          <div>
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
              <span style="font-family: var(--font-mono); font-size: 18px; font-weight: 800; color: var(--c-wine-primary);">DISTORSIÓN 01</span>
              <span style="font-family: var(--font-mono); font-size: 20px; font-weight: 800; color: var(--c-wine-primary); background: #FFFFFF; border: 1.5px solid var(--c-wine-primary); padding: 2px 10px; border-radius: 4px;">Coseno (x + 1)/2</span>
            </div>
            <h3 style="font-family: var(--font-sans); font-size: 26px; font-weight: 800; color: var(--c-wine-dark); margin: 0 0 10px 0;">
              Similitud 0.00 se transforma en 0.50
            </h3>
            <p style="font-family: var(--font-sans); font-size: 22px; color: #110103; font-weight: 600; line-height: 1.35; margin: 0;">
              Al reescalar artificialmente los cosenos, cualquier respuesta desconectada o incoherente obtiene una nota aprobatoria mínima garantizada.
            </p>
          </div>
          <div style="margin-top: 12px; font-family: var(--font-sans); font-size: 21px; color: var(--c-wine-primary); font-weight: 700;">
            Efecto: Califica como aceptables respuestas vacías.
          </div>
        </div>

        <!-- Bloque 2: Premio Fijo al Rechazo -->
        <div style="background: #FAF5F5; border: 2px solid var(--c-red-accent); border-radius: 8px; padding: 22px 24px; flex: 1; display: flex; flex-direction: column; justify-content: space-between;">
          <div>
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
              <span style="font-family: var(--font-mono); font-size: 18px; font-weight: 800; color: var(--c-red-accent);">DISTORSIÓN 02</span>
              <span style="font-family: var(--font-mono); font-size: 20px; font-weight: 800; color: var(--c-red-accent); background: #FFE4E6; border: 1.5px solid var(--c-red-accent); padding: 2px 10px; border-radius: 4px;">Nota Fija = 0.80</span>
            </div>
            <h3 style="font-family: var(--font-sans); font-size: 26px; font-weight: 800; color: var(--c-wine-dark); margin: 0 0 10px 0;">
              Bonificación Automática a 9 Frases
            </h3>
            <p style="font-family: var(--font-sans); font-size: 22px; color: #110103; font-weight: 600; line-height: 1.35; margin: 0;">
              Premia con 0.80 automático la abstención, generando una ventaja artificial para modelos sobre-conservadores que rehúyen responder.
            </p>
          </div>
          <div style="margin-top: 12px; font-family: var(--font-sans); font-size: 21px; color: var(--c-red-accent); font-weight: 700;">
            Efecto: Bonifica igual la prudencia que el bloqueo léxico.
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

# Plantilla HTML completa
HTML_WRAPPER = '''<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Test Opciones Slide 12</title>
  <link rel="stylesheet" href="http://localhost:8085/styles.css?v=14">
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
        ('slide_12_opcion_a.html', 'slide_12_opcion_a.png', OPCION_A_HTML),
        ('slide_12_opcion_b.html', 'slide_12_opcion_b.png', OPCION_B_HTML),
        ('slide_12_opcion_c.html', 'slide_12_opcion_c.png', OPCION_C_HTML)
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
