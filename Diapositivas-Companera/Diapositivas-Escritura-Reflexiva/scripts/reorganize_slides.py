# -*- coding: utf-8 -*-
"""
Reorganización de diapositivas para insertar la Slide 03 (Roadmap en 4 Actos)
y consolidar la validación de 3 perfiles en la Slide 17, manteniendo exactamente 20 diapositivas.
"""
import os
import re

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
slides_dir = os.path.join(base_dir, 'slides')
backup_dir = os.path.join(base_dir, 'slides_backup')

# 1. Slide 03 content (Roadmap)
slide_03_content = '''<!-- ====================================================================
     SLIDE 03: ESTRUCTURA DE LA PONENCIA (ROADMAP EN 4 ACTOS)
     ==================================================================== -->
<section class="slide s-white" id="slide-3" data-notes="Presentar el mapa de navegación de la ponencia en 20 segundos: 'La exposición sigue un recorrido en cuatro momentos: primero, el conflicto de la delegación acrítica; segundo, el diseño metodológico de la guía conversacional; tercero, la verificación del modelo en tres perfiles de escritor; y cuarto, los límites reconocidos y la ruta hacia el aula real.'">
  
  <header class="slide-header">
    <div class="sh-left">
      <span class="sh-red-bar"></span>
      <span class="sh-category">ESTRUCTURA DE LA PONENCIA</span>
    </div>
    <img src="assets/image6.png" alt="#LoxTIC" class="sh-loxtic">
  </header>
  <div class="sh-divider"></div>

  <div class="slide-content-area" style="justify-content: center; padding-top: 20px; padding-bottom: 25px;">
    
    <div>
      <h2 class="s-lead-question" style="margin-bottom: 34px; font-size: 48px; font-weight: 800; line-height: 1.22; color: #2C0509;">
        Ruta de la Presentaci&oacute;n
      </h2>
    </div>

    <div style="display: flex; gap: 28px; max-width: 1650px; align-items: stretch;">
      
      <!-- Paso 01: Contexto y Problema -->
      <div style="flex: 1; background: #FAF5F5; border-top: 8px solid var(--c-wine-primary); border-left: 1px solid var(--c-border-subtle); border-right: 1px solid var(--c-border-subtle); border-bottom: 1px solid var(--c-border-subtle); padding: 44px 30px; display: flex; flex-direction: column; justify-content: space-between; min-height: 400px; position: relative; overflow: hidden;">
        
        <div style="position: absolute; right: -10px; bottom: -20px; opacity: 0.08; color: var(--c-wine-primary); transform: rotate(6deg); pointer-events: none; z-index: 0;">
          <svg width="240" height="240" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
            <path d="M10.29 3.86L1.82 18a2 2 0 0 0 1.71 3h16.94a2 2 0 0 0 1.71-3L13.71 3.86a2 2 0 0 0-3.42 0z"/>
            <line x1="12" y1="9" x2="12" y2="13"/>
            <line x1="12" y1="17" x2="12.01" y2="17"/>
          </svg>
        </div>

        <div style="position: relative; z-index: 1;">
          <div style="font-family: var(--font-mono); font-size: 76px; font-weight: 900; color: var(--c-wine-primary); line-height: 1; margin-bottom: 20px;">
            01
          </div>
          <div style="width: 48px; height: 4px; background: var(--c-wine-primary); margin-bottom: 20px;"></div>
          
          <h3 style="font-family: var(--font-sans); font-size: 32px; font-weight: 800; color: var(--c-text-dark); line-height: 1.25; margin: 0 0 12px 0;">
            Contexto y Problema
          </h3>
          <p style="font-family: var(--font-sans); font-size: 22px; color: #110103; line-height: 1.35; margin: 0; font-weight: 500;">
            Tensi&oacute;n entre la <strong>delegaci&oacute;n acr&iacute;tica</strong> y el desaprovechamiento formativo de la IA.
          </p>
        </div>

        <div style="border-top: 1.5px solid var(--c-border-subtle); padding-top: 14px; position: relative; z-index: 1;">
          <span style="font-family: var(--font-mono); font-size: 16px; font-weight: 800; color: var(--c-wine-primary); letter-spacing: 1px;">
            EL CONFLICTO
          </span>
        </div>
      </div>

      <!-- Paso 02: Metodología y Diseño -->
      <div style="flex: 1; background: #FAF5F5; border-top: 8px solid #8B263E; border-left: 1px solid var(--c-border-subtle); border-right: 1px solid var(--c-border-subtle); border-bottom: 1px solid var(--c-border-subtle); padding: 44px 30px; display: flex; flex-direction: column; justify-content: space-between; min-height: 400px; position: relative; overflow: hidden;">
        
        <div style="position: absolute; right: -10px; bottom: -20px; opacity: 0.08; color: #8B263E; transform: rotate(-6deg); pointer-events: none; z-index: 0;">
          <svg width="240" height="240" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
            <polygon points="12 2 2 7 12 12 22 7 12 2"/>
            <polyline points="2 17 12 22 22 17"/>
            <polyline points="2 12 12 17 22 12"/>
          </svg>
        </div>

        <div style="position: relative; z-index: 1;">
          <div style="font-family: var(--font-mono); font-size: 76px; font-weight: 900; color: #8B263E; line-height: 1; margin-bottom: 20px;">
            02
          </div>
          <div style="width: 48px; height: 4px; background: #8B263E; margin-bottom: 20px;"></div>
          
          <h3 style="font-family: var(--font-sans); font-size: 32px; font-weight: 800; color: var(--c-text-dark); line-height: 1.25; margin: 0 0 12px 0;">
            Metodolog&iacute;a y Dise&ntilde;o
          </h3>
          <p style="font-family: var(--font-sans); font-size: 22px; color: #110103; line-height: 1.35; margin: 0; font-weight: 500;">
            Articulaci&oacute;n de <strong>Flower &amp; Hayes con Sch&ouml;n</strong> y reglas en Markdown (.md).
          </p>
        </div>

        <div style="border-top: 1.5px solid var(--c-border-subtle); padding-top: 14px; position: relative; z-index: 1;">
          <span style="font-family: var(--font-mono); font-size: 16px; font-weight: 800; color: #8B263E; letter-spacing: 1px;">
            EL ENFOQUE DBR
          </span>
        </div>
      </div>

      <!-- Paso 03: Resultados y Evidencia -->
      <div style="flex: 1; background: #FAF5F5; border-top: 8px solid var(--c-red-accent); border-left: 1px solid var(--c-border-subtle); border-right: 1px solid var(--c-border-subtle); border-bottom: 1px solid var(--c-border-subtle); padding: 44px 30px; display: flex; flex-direction: column; justify-content: space-between; min-height: 400px; position: relative; overflow: hidden;">
        
        <div style="position: absolute; right: -10px; bottom: -20px; opacity: 0.08; color: var(--c-red-accent); transform: rotate(6deg); pointer-events: none; z-index: 0;">
          <svg width="240" height="240" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
            <polyline points="22 12 18 12 15 21 9 3 6 12 2 12"/>
          </svg>
        </div>

        <div style="position: relative; z-index: 1;">
          <div style="font-family: var(--font-mono); font-size: 76px; font-weight: 900; color: var(--c-red-accent); line-height: 1; margin-bottom: 20px;">
            03
          </div>
          <div style="width: 48px; height: 4px; background: var(--c-red-accent); margin-bottom: 20px;"></div>
          
          <h3 style="font-family: var(--font-sans); font-size: 32px; font-weight: 800; color: var(--c-text-dark); line-height: 1.25; margin: 0 0 12px 0;">
            Resultados y Evidencia
          </h3>
          <p style="font-family: var(--font-sans); font-size: 22px; color: #110103; line-height: 1.35; margin: 0; font-weight: 500;">
            Modelos de proceso, compuertas l&oacute;gicas y <strong>simulaci&oacute;n en 3 perfiles</strong>.
          </p>
        </div>

        <div style="border-top: 1.5px solid var(--c-border-subtle); padding-top: 14px; position: relative; z-index: 1;">
          <span style="font-family: var(--font-mono); font-size: 16px; font-weight: 800; color: var(--c-red-accent); letter-spacing: 1px;">
            LA PRUEBA
          </span>
        </div>
      </div>

      <!-- Paso 04: Discusión y Conclusiones -->
      <div style="flex: 1; background: #FAF5F5; border-top: 8px solid var(--c-gold); border-left: 1px solid var(--c-border-subtle); border-right: 1px solid var(--c-border-subtle); border-bottom: 1px solid var(--c-border-subtle); padding: 44px 30px; display: flex; flex-direction: column; justify-content: space-between; min-height: 400px; position: relative; overflow: hidden;">
        
        <div style="position: absolute; right: -10px; bottom: -20px; opacity: 0.08; color: #9A7200; transform: rotate(-6deg); pointer-events: none; z-index: 0;">
          <svg width="240" height="240" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
            <circle cx="12" cy="12" r="10"/>
            <polygon points="16.24 7.76 14.12 14.12 7.76 16.24 9.88 9.88 16.24 7.76"/>
          </svg>
        </div>

        <div style="position: relative; z-index: 1;">
          <div style="font-family: var(--font-mono); font-size: 76px; font-weight: 900; color: #9A7200; line-height: 1; margin-bottom: 20px;">
            04
          </div>
          <div style="width: 48px; height: 4px; background: var(--c-gold); margin-bottom: 20px;"></div>
          
          <h3 style="font-family: var(--font-sans); font-size: 32px; font-weight: 800; color: var(--c-text-dark); line-height: 1.25; margin: 0 0 12px 0;">
            Discusi&oacute;n y Cierre
          </h3>
          <p style="font-family: var(--font-sans); font-size: 22px; color: #110103; line-height: 1.35; margin: 0; font-weight: 500;">
            Aportes metodol&oacute;gicos, l&iacute;mites reconocidos y <strong>ruta hacia el aula real</strong>.
          </p>
        </div>

        <div style="border-top: 1.5px solid var(--c-border-subtle); padding-top: 14px; position: relative; z-index: 1;">
          <span style="font-family: var(--font-mono); font-size: 16px; font-weight: 800; color: #9A7200; letter-spacing: 1px;">
            LA PROPUESTA
          </span>
        </div>
      </div>

    </div>

  </div>

  <div class="slide-footer-rule"></div>
  <footer class="slide-footer">
    <span class="sf-left">VI CONGRESO INTERNACIONAL &middot; CARTAGENA 2026</span>
    <span class="sf-right">ESCRITURA REFLEXIVA ASISTIDA POR IA</span>
  </footer>

</section>
'''

# 2. Slide 17 content (Merged Figura 5 + 3 Hallazgos)
slide_17_content = '''<!-- ====================================================================
     SLIDE 17: 03 · RESULTADOS / VALIDACIÓN PRÁCTICA Y HALLAZGOS (FIGURA 5)
     ==================================================================== -->
<section class="slide s-white" id="slide-17" data-notes="Probamos la guía con tres perfiles de escritor: novato, competente y experto. En los tres casos se verificó consistencia lógica interna absoluta sin desvíos de rol, 0% de texto ajeno generado por el bot y adaptabilidad plena al ritmo de cada usuario. La Figura 5 resume los caminos recorridos y la evidencia de no sustitución.">
  
  <header class="slide-header">
    <div class="sh-left">
      <span class="sh-red-bar"></span>
      <span class="sh-category">03 &middot; RESULTADOS &middot; VALIDACI&Oacute;N Y EVIDENCIA</span>
    </div>
    <img src="assets/image6.png" alt="#LoxTIC" class="sh-loxtic">
  </header>
  <div class="sh-divider"></div>

  <div class="slide-content-area" style="justify-content: space-between; padding-top: 16px; padding-bottom: 16px;">
    
    <div>
      <h2 class="s-lead-question" style="font-size: 44px; font-weight: 800; color: #2C0509; margin-bottom: 6px; line-height: 1.2;">
        Validaci&oacute;n pr&aacute;ctica: simulaci&oacute;n en tres perfiles y hallazgos clave
      </h2>
      <div style="font-family: var(--font-sans); font-size: 24px; color: var(--c-gray-text); font-weight: 600;">
        Figura 5: Recorridos diferenciados en novato, competente y experto; y m&eacute;tricas de consistencia comprobadas.
      </div>
    </div>

    <!-- Layout Dividido: Figura 5 a la izquierda (60%) + 3 Métricas a la derecha (40%) -->
    <div style="display: grid; grid-template-columns: 1.2fr 0.8fr; gap: 32px; flex: 1; align-items: stretch; margin-top: 12px; margin-bottom: 12px;">
      
      <!-- Columna Izquierda: Figura 5 en Marco Editorial Plano -->
      <div style="border: 2px solid var(--c-wine-primary); background: #FFFFFF; display: flex; flex-direction: column; justify-content: space-between;">
        <div style="background: var(--c-wine-primary); padding: 8px 18px; display: flex; justify-content: space-between; align-items: center; flex-shrink: 0;">
          <span style="font-family: var(--font-mono); font-size: 16px; font-weight: 800; color: #FFFFFF; letter-spacing: 1px;">
            FIGURA 5 &middot; SIMULACI&Oacute;N CON TRES NIVELES DE ESCRITOR
          </span>
          <span style="font-family: var(--font-sans); font-size: 16px; color: var(--c-gold); font-weight: 700;">
            Novato &middot; Competente &middot; Experto
          </span>
        </div>
        <div style="flex: 1; display: flex; align-items: center; justify-content: center; padding: 12px; background: #FFFFFF; overflow: hidden;">
          <img src="assets/figura_5.png" alt="Figura 5: Validación práctica en 3 perfiles" style="max-width: 100%; max-height: 100%; object-fit: contain;">
        </div>
        <div style="background: #FAF5F5; border-top: 1px solid var(--c-border-subtle); padding: 8px 16px; display: flex; justify-content: space-between; font-family: var(--font-mono); font-size: 17px; color: #4A3B3D; font-weight: 700;">
          <span>Verificaci&oacute;n en entorno LLM controlado cargando la gu&iacute;a .md</span>
          <span style="color: var(--c-wine-primary);">Fuente: Autores.</span>
        </div>
      </div>

      <!-- Columna Derecha: 3 Métricas y Hallazgos Heroicos -->
      <div style="display: flex; flex-direction: column; gap: 16px; justify-content: space-between;">
        
        <!-- Hallazgo 1: 100% -->
        <div style="flex: 1; background: #FAF5F5; border-left: 8px solid var(--c-wine-primary); border-top: 1px solid var(--c-border-subtle); border-right: 1px solid var(--c-border-subtle); border-bottom: 1px solid var(--c-border-subtle); padding: 18px 22px; display: flex; flex-direction: column; justify-content: center;">
          <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 4px;">
            <span style="font-family: var(--font-mono); font-size: 40px; font-weight: 900; color: var(--c-wine-primary); line-height: 1;">100%</span>
            <span style="font-family: var(--font-mono); font-size: 14px; font-weight: 800; color: var(--c-wine-primary); background: #EAE0E1; padding: 2px 10px;">CONSISTENCIA</span>
          </div>
          <div style="font-family: var(--font-sans); font-size: 22px; font-weight: 800; color: var(--c-wine-dark); margin-bottom: 4px;">Gobernanza L&oacute;gica Total</div>
          <div style="font-family: var(--font-sans); font-size: 19px; color: #110103; line-height: 1.35;">Cumplimiento estricto de compuertas l&oacute;gicas, transiciones y silencios sin desv&iacute;o de rol.</div>
        </div>

        <!-- Hallazgo 2: 0% -->
        <div style="flex: 1; background: #FAF5F5; border-left: 8px solid var(--c-red-accent); border-top: 1px solid var(--c-border-subtle); border-right: 1px solid var(--c-border-subtle); border-bottom: 1px solid var(--c-border-subtle); padding: 18px 22px; display: flex; flex-direction: column; justify-content: center;">
          <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 4px;">
            <span style="font-family: var(--font-mono); font-size: 40px; font-weight: 900; color: var(--c-red-accent); line-height: 1;">0%</span>
            <span style="font-family: var(--font-mono); font-size: 14px; font-weight: 800; color: var(--c-red-accent); background: #FDE8E9; padding: 2px 10px;">NO SUSTITUCI&Oacute;N</span>
          </div>
          <div style="font-family: var(--font-sans); font-size: 22px; font-weight: 800; color: var(--c-wine-dark); margin-bottom: 4px;">Texto Ajeno Generado</div>
          <div style="font-family: var(--font-sans); font-size: 19px; color: #110103; line-height: 1.35;">El modelo nunca redact&oacute; ni una sola frase por el autor; la voz autoral permaneci&oacute; intacta.</div>
        </div>

        <!-- Hallazgo 3: 3 / 3 -->
        <div style="flex: 1; background: #FAF5F5; border-left: 8px solid var(--c-gold); border-top: 1px solid var(--c-border-subtle); border-right: 1px solid var(--c-border-subtle); border-bottom: 1px solid var(--c-border-subtle); padding: 18px 22px; display: flex; flex-direction: column; justify-content: center;">
          <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 4px;">
            <span style="font-family: var(--font-mono); font-size: 40px; font-weight: 900; color: #9A7200; line-height: 1;">3 / 3</span>
            <span style="font-family: var(--font-mono); font-size: 14px; font-weight: 800; color: #9A7200; background: #FAF0D8; padding: 2px 10px;">ADAPTABILIDAD</span>
          </div>
          <div style="font-family: var(--font-sans); font-size: 22px; font-weight: 800; color: var(--c-wine-dark); margin-bottom: 4px;">Perfiles Validados</div>
          <div style="font-family: var(--font-sans); font-size: 19px; color: #110103; line-height: 1.35;">Desde el novato (gu&iacute;a completa) hasta el experto (recorrido acotado), el modelo se adapt&oacute; plenamente.</div>
        </div>

      </div>

    </div>

    <!-- Doble Regla Editorial Remate -->
    <div style="background: #FAF5F5; border-top: 3.5px solid var(--c-wine-primary); border-bottom: 3.5px solid var(--c-wine-primary); padding: 14px 30px; display: flex; align-items: center; justify-content: space-between;">
      <div style="display: flex; align-items: center; gap: 20px;">
        <span style="font-family: var(--font-mono); font-size: 16px; font-weight: 800; color: var(--c-wine-primary); letter-spacing: 1.5px; flex-shrink: 0;">
          BALANCE DE LA VALIDACI&Oacute;N:
        </span>
        <span style="font-family: var(--font-sans); font-size: 21px; font-weight: 700; color: #110103;">
          El andamiaje conversacional es t&eacute;cnicamente viable, consistente y preserva la soberan&iacute;a reflexiva del escritor.
        </span>
      </div>
    </div>

  </div>

  <div class="slide-footer-rule"></div>
  <footer class="slide-footer">
    <span class="sf-left">VI CONGRESO INTERNACIONAL &middot; CARTAGENA 2026</span>
    <span class="sf-right">ESCRITURA REFLEXIVA ASISTIDA POR IA &middot; ACTO 03</span>
  </footer>

</section>
'''

def run():
    # Shift old slide_03 to slide_15 to new slide_04 to slide_16
    for i in range(15, 2, -1):
        src = os.path.join(backup_dir, f'slide_{i:02d}.html')
        dst = os.path.join(slides_dir, f'slide_{i+1:02d}.html')
        with open(src, 'r', encoding='utf-8') as f:
            content = f.read()
        content = re.sub(r'id="slide-\d+"', f'id="slide-{i+1}"', content)
        content = re.sub(r'SLIDE \d+:', f'SLIDE {i+1:02d}:', content)
        with open(dst, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f'Shifted slide_{i:02d} -> slide_{i+1:02d}')

    # Write slide_03 (Roadmap)
    with open(os.path.join(slides_dir, 'slide_03.html'), 'w', encoding='utf-8') as f:
        f.write(slide_03_content)
    print('Created slide_03.html (Roadmap)')

    # Write slide_17 (Merged)
    with open(os.path.join(slides_dir, 'slide_17.html'), 'w', encoding='utf-8') as f:
        f.write(slide_17_content)
    print('Created slide_17.html (Merged Figura 5 + Métricas)')

    print('Reorganización completada con éxito!')

if __name__ == '__main__':
    run()
