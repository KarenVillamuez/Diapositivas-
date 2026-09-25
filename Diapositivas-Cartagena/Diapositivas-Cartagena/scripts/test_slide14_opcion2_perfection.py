# -*- coding: utf-8 -*-
"""
Perfeccionamiento de las 3 Variantes de Opción 2 para Slide 14:
- VARIANTE 2-V: Díptico Vertical Heroico con Barras Gruesas de 32px + Franja de Síntesis Inferior.
- VARIANTE 2-H: Díptico Panorámico de 2 Filas con Barras Horizontales Anchas y Proporción Editorial.
- VARIANTE 2-C: Díptico Vertical con Bloques Métricos de 56px y Altura Natural (sin huecos).
"""
import os
from playwright.sync_api import sync_playwright

output_dir = r"C:\Users\ASUS\.gemini\antigravity-ide\brain\a6624504-511c-4b9d-bc9a-468e348bde40"
os.makedirs(output_dir, exist_ok=True)

# =============================================================================
# VARIANTE 2-V: Díptico Vertical + Franja Inferior (Todo contenido entre Y=170 y Y=870)
# =============================================================================
HTML_VAR_2V = '''
<section class="slide s-white active" id="slide-14-2v">
  <header class="slide-header">
    <div class="sh-left">
      <span class="sh-red-bar"></span>
      <span class="sh-category">03 · RESULTADOS · MODOS DE FALLO ASIMÉTRICOS</span>
    </div>
    <img src="http://localhost:8085/assets/image6.png" alt="#LoxTIC" class="sh-loxtic">
  </header>
  <div class="sh-divider"></div>

  <!-- Contenedor ajustado a altura real (720px) sin overflow -->
  <div class="slide-content-area" style="top: 175px; height: 720px; justify-content: flex-start; gap: 20px;">
    
    <!-- TÍTULO -->
    <h2 class="s-lead-question" style="font-size: 38px; font-weight: 800; margin: 0; line-height: 1.2; color: #2C0509;">
      Alucinación frente a sobre-rechazo: cómo fallan dos modelos con la misma nota
    </h2>

    <!-- GRID DE 2 COLUMNAS (ALTO NATURAL ~460px) -->
    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 36px;">
      
      <!-- PHI-4-MINI -->
      <div style="background: #FAF5F5; border-top: 8px solid var(--c-wine-primary); padding: 26px 32px; display: flex; flex-direction: column; gap: 22px;">
        <!-- Cabecera -->
        <div style="display: flex; justify-content: space-between; align-items: baseline; border-bottom: 2px solid #EAE0E1; padding-bottom: 10px;">
          <div>
            <div style="font-family: var(--font-sans); font-size: 36px; font-weight: 800; color: #2C0509; line-height: 1.1;">
              Phi-4-mini <span style="font-size: 24px; font-weight: 600; color: #5D4A4D;">(3.8B)</span>
            </div>
            <div style="font-family: var(--font-mono); font-size: 18px; font-weight: 700; color: var(--c-wine-primary); letter-spacing: 1px; margin-top: 3px;">
              PERFIL PERMISIVO · Q = 0.8030
            </div>
          </div>
          <span style="font-family: var(--font-sans); font-size: 20px; font-weight: 800; color: var(--c-wine-primary); background: #F0E6E8; padding: 4px 12px;">
            Aula Asistida
          </span>
        </div>

        <!-- Métrica 1 -->
        <div>
          <div style="display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 6px;">
            <span style="font-family: var(--font-sans); font-size: 22px; font-weight: 700; color: #2C0509;">
              Rechazo en 14 sondas trampa:
            </span>
            <span style="font-family: var(--font-mono); font-size: 38px; font-weight: 800; color: var(--c-red-accent); line-height: 1;">
              28.6% <span style="font-size: 20px; font-weight: 700; color: #5D4A4D;">(4/14)</span>
            </span>
          </div>
          <div style="background: #EAE0E1; height: 26px; width: 100%; margin-bottom: 6px;">
            <div style="width: 28.6%; background: var(--c-red-accent); height: 100%;"></div>
          </div>
          <div style="font-family: var(--font-sans); font-size: 20px; color: var(--c-red-accent); font-weight: 700;">
            Alucina en 10 casos fuera del libro escolar.
          </div>
        </div>

        <!-- Métrica 2 -->
        <div>
          <div style="display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 6px;">
            <span style="font-family: var(--font-sans); font-size: 22px; font-weight: 700; color: #2C0509;">
              Falso rechazo en 84 consultas válidas:
            </span>
            <span style="font-family: var(--font-mono); font-size: 38px; font-weight: 800; color: var(--c-wine-primary); line-height: 1;">
              0.0% <span style="font-size: 20px; font-weight: 700; color: #5D4A4D;">(0/84)</span>
            </span>
          </div>
          <div style="background: #EAE0E1; height: 26px; width: 100%; margin-bottom: 6px;">
            <div style="width: 0%; background: var(--c-wine-primary); height: 100%;"></div>
          </div>
          <div style="font-family: var(--font-sans); font-size: 20px; color: var(--c-wine-primary); font-weight: 700;">
            Fluidez total; jamás bloquea al estudiante.
          </div>
        </div>

        <!-- Remate pedagógico -->
        <div style="border-top: 1px solid #EAE0E1; padding-top: 10px; font-family: var(--font-sans); font-size: 20px; color: #110103; font-weight: 600;">
          <strong style="color: var(--c-wine-primary);">Uso recomendado:</strong> Docente activo en clase que modera y rectifica alucinaciones.
        </div>
      </div>

      <!-- QWEN2.5-3B -->
      <div style="background: #FAF5F5; border-top: 8px solid var(--c-red-accent); padding: 26px 32px; display: flex; flex-direction: column; gap: 22px;">
        <!-- Cabecera -->
        <div style="display: flex; justify-content: space-between; align-items: baseline; border-bottom: 2px solid #EAE0E1; padding-bottom: 10px;">
          <div>
            <div style="font-family: var(--font-sans); font-size: 36px; font-weight: 800; color: #2C0509; line-height: 1.1;">
              Qwen2.5-3B <span style="font-size: 24px; font-weight: 600; color: #5D4A4D;">(3.1B)</span>
            </div>
            <div style="font-family: var(--font-mono); font-size: 18px; font-weight: 700; color: var(--c-red-accent); letter-spacing: 1px; margin-top: 3px;">
              PERFIL CONSERVADOR · Q = 0.8010
            </div>
          </div>
          <span style="font-family: var(--font-sans); font-size: 20px; font-weight: 800; color: var(--c-red-accent); background: #FDE8E9; padding: 4px 12px;">
            Autoestudio
          </span>
        </div>

        <!-- Métrica 1 -->
        <div>
          <div style="display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 6px;">
            <span style="font-family: var(--font-sans); font-size: 22px; font-weight: 700; color: #2C0509;">
              Rechazo en 14 sondas trampa:
            </span>
            <span style="font-family: var(--font-mono); font-size: 38px; font-weight: 800; color: var(--c-wine-primary); line-height: 1;">
              85.7% <span style="font-size: 20px; font-weight: 700; color: #5D4A4D;">(12/14)</span>
            </span>
          </div>
          <div style="background: #EAE0E1; height: 26px; width: 100%; margin-bottom: 6px;">
            <div style="width: 85.7%; background: var(--c-wine-primary); height: 100%;"></div>
          </div>
          <div style="font-family: var(--font-sans); font-size: 20px; color: var(--c-wine-primary); font-weight: 700;">
            Filtro riguroso frente a preguntas trampa.
          </div>
        </div>

        <!-- Métrica 2 -->
        <div>
          <div style="display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 6px;">
            <span style="font-family: var(--font-sans); font-size: 22px; font-weight: 700; color: #2C0509;">
              Falso rechazo en 84 consultas válidas:
            </span>
            <span style="font-family: var(--font-mono); font-size: 38px; font-weight: 800; color: var(--c-red-accent); line-height: 1;">
              7.1% <span style="font-size: 20px; font-weight: 700; color: #5D4A4D;">(6/84)</span>
            </span>
          </div>
          <div style="background: #EAE0E1; height: 26px; width: 100%; margin-bottom: 6px;">
            <div style="width: 25%; background: var(--c-red-accent); height: 100%;"></div>
          </div>
          <div style="font-family: var(--font-sans); font-size: 20px; color: var(--c-red-accent); font-weight: 700;">
            Sobre-rechazo; bloquea consultas legítimas.
          </div>
        </div>

        <!-- Remate pedagógico -->
        <div style="border-top: 1px solid #EAE0E1; padding-top: 10px; font-family: var(--font-sans); font-size: 20px; color: #110103; font-weight: 600;">
          <strong style="color: var(--c-red-accent);">Uso recomendado:</strong> Autoestudio sin profesor donde prima no inducir al error al alumno.
        </div>
      </div>

    </div>

    <!-- FRANJA DE SÍNTESIS INFERIOR: Ancla visual a Y=840px -->
    <div style="background: #FAF5F5; border: 2px solid var(--c-wine-primary); padding: 14px 28px; display: flex; align-items: center; justify-content: space-between;">
      <div style="display: flex; align-items: center; gap: 14px;">
        <span style="font-family: var(--font-mono); font-size: 20px; font-weight: 800; color: var(--c-wine-primary); letter-spacing: 1.5px;">
          CONCLUSIÓN:
        </span>
        <span style="font-family: var(--font-sans); font-size: 22px; font-weight: 700; color: #110103;">
          La misma nota global (0.80) oculta riesgos asimétricos: la elección depende del rol del docente.
        </span>
      </div>
      <div style="font-family: var(--font-mono); font-size: 19px; font-weight: 700; color: #5D4A4D;">
        Tabla 3 del paper
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

# =============================================================================
# VARIANTE 2-H: Díptico Panorámico de 2 Filas Horizontales (Proporción Perfecta)
# =============================================================================
HTML_VAR_2H = '''
<section class="slide s-white active" id="slide-14-2h">
  <header class="slide-header">
    <div class="sh-left">
      <span class="sh-red-bar"></span>
      <span class="sh-category">03 · RESULTADOS · MODOS DE FALLO ASIMÉTRICOS</span>
    </div>
    <img src="http://localhost:8085/assets/image6.png" alt="#LoxTIC" class="sh-loxtic">
  </header>
  <div class="sh-divider"></div>

  <!-- Contenedor ajustado a altura real (720px) sin overflow -->
  <div class="slide-content-area" style="top: 175px; height: 720px; justify-content: flex-start; gap: 20px;">
    
    <!-- TÍTULO -->
    <h2 class="s-lead-question" style="font-size: 38px; font-weight: 800; margin: 0; line-height: 1.2; color: #2C0509;">
      Alucinación frente a sobre-rechazo: cómo fallan dos modelos con la misma nota
    </h2>

    <!-- FILA 1: PHI-4-MINI (HORIZONTAL) -->
    <div style="background: #FAF5F5; border-left: 10px solid var(--c-wine-primary); padding: 22px 34px; display: grid; grid-template-columns: 400px 1fr 1fr; gap: 40px; align-items: center;">
      <!-- Identidad y Rol -->
      <div style="border-right: 2px solid #EAE0E1; padding-right: 28px;">
        <div style="font-family: var(--font-mono); font-size: 18px; font-weight: 700; color: var(--c-wine-primary); letter-spacing: 1.5px; margin-bottom: 2px;">
          PERFIL PERMISIVO · Q = 0.8030
        </div>
        <div style="font-family: var(--font-sans); font-size: 38px; font-weight: 800; color: #2C0509; line-height: 1.1; margin-bottom: 6px;">
          Phi-4-mini <span style="font-size: 24px; font-weight: 600; color: #5D4A4D;">3.8B</span>
        </div>
        <div style="font-family: var(--font-sans); font-size: 21px; font-weight: 700; color: #110103;">
          <strong style="color: var(--c-wine-primary);">Aula asistida:</strong> con docente activo.
        </div>
      </div>

      <!-- Barra 1: Sondas trampa -->
      <div>
        <div style="display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 6px;">
          <span style="font-family: var(--font-sans); font-size: 21px; font-weight: 700; color: #2C0509;">Rechazo en trampas (14):</span>
          <span style="font-family: var(--font-mono); font-size: 38px; font-weight: 800; color: var(--c-red-accent); line-height: 1;">28.6%</span>
        </div>
        <div style="background: #EAE0E1; height: 26px; width: 100%; margin-bottom: 6px;">
          <div style="width: 28.6%; background: var(--c-red-accent); height: 100%;"></div>
        </div>
        <div style="font-family: var(--font-sans); font-size: 20px; color: var(--c-red-accent); font-weight: 700;">
          Alucina en 10 casos fuera del libro.
        </div>
      </div>

      <!-- Barra 2: Consultas válidas -->
      <div>
        <div style="display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 6px;">
          <span style="font-family: var(--font-sans); font-size: 21px; font-weight: 700; color: #2C0509;">Falso rechazo (84 válidas):</span>
          <span style="font-family: var(--font-mono); font-size: 38px; font-weight: 800; color: var(--c-wine-primary); line-height: 1;">0.0%</span>
        </div>
        <div style="background: #EAE0E1; height: 26px; width: 100%; margin-bottom: 6px;">
          <div style="width: 0%; background: var(--c-wine-primary); height: 100%;"></div>
        </div>
        <div style="font-family: var(--font-sans); font-size: 20px; color: var(--c-wine-primary); font-weight: 700;">
          Fluidez total; jamás frena al alumno.
        </div>
      </div>
    </div>

    <!-- FILA 2: QWEN2.5-3B (HORIZONTAL) -->
    <div style="background: #FAF5F5; border-left: 10px solid var(--c-red-accent); padding: 22px 34px; display: grid; grid-template-columns: 400px 1fr 1fr; gap: 40px; align-items: center;">
      <!-- Identidad y Rol -->
      <div style="border-right: 2px solid #EAE0E1; padding-right: 28px;">
        <div style="font-family: var(--font-mono); font-size: 18px; font-weight: 700; color: var(--c-red-accent); letter-spacing: 1.5px; margin-bottom: 2px;">
          PERFIL CONSERVADOR · Q = 0.8010
        </div>
        <div style="font-family: var(--font-sans); font-size: 38px; font-weight: 800; color: #2C0509; line-height: 1.1; margin-bottom: 6px;">
          Qwen2.5-3B <span style="font-size: 24px; font-weight: 600; color: #5D4A4D;">3.1B</span>
        </div>
        <div style="font-family: var(--font-sans); font-size: 21px; font-weight: 700; color: #110103;">
          <strong style="color: var(--c-red-accent);">Autoestudio:</strong> sin docente presente.
        </div>
      </div>

      <!-- Barra 1: Sondas trampa -->
      <div>
        <div style="display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 6px;">
          <span style="font-family: var(--font-sans); font-size: 21px; font-weight: 700; color: #2C0509;">Rechazo en trampas (14):</span>
          <span style="font-family: var(--font-mono); font-size: 38px; font-weight: 800; color: var(--c-wine-primary); line-height: 1;">85.7%</span>
        </div>
        <div style="background: #EAE0E1; height: 26px; width: 100%; margin-bottom: 6px;">
          <div style="width: 85.7%; background: var(--c-wine-primary); height: 100%;"></div>
        </div>
        <div style="font-family: var(--font-sans); font-size: 20px; color: var(--c-wine-primary); font-weight: 700;">
          Filtro riguroso frente a trampas.
        </div>
      </div>

      <!-- Barra 2: Consultas válidas -->
      <div>
        <div style="display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 6px;">
          <span style="font-family: var(--font-sans); font-size: 21px; font-weight: 700; color: #2C0509;">Falso rechazo (84 válidas):</span>
          <span style="font-family: var(--font-mono); font-size: 38px; font-weight: 800; color: var(--c-red-accent); line-height: 1;">7.1%</span>
        </div>
        <div style="background: #EAE0E1; height: 26px; width: 100%; margin-bottom: 6px;">
          <div style="width: 25%; background: var(--c-red-accent); height: 100%;"></div>
        </div>
        <div style="font-family: var(--font-sans); font-size: 20px; color: var(--c-red-accent); font-weight: 700;">
          Sobre-rechazo por cautela extrema.
        </div>
      </div>
    </div>

    <!-- REMATE EDITORIAL INFERIOR -->
    <div style="display: flex; justify-content: space-between; align-items: center; border-top: 1px solid #EAE0E1; padding-top: 14px; margin-top: 4px;">
      <span style="font-family: var(--font-sans); font-size: 21px; font-weight: 700; color: #110103;">
        <strong style="color: var(--c-wine-primary);">Conclusión pedagógica:</strong> Modelos con idéntica nota numérica exigen entornos de despliegue completamente distintos.
      </span>
      <span style="font-family: var(--font-mono); font-size: 19px; font-weight: 700; color: #5D4A4D;">
        Tabla 3 del paper (×4 semillas)
      </span>
    </div>

  </div>

  <div class="slide-footer-rule"></div>
  <footer class="slide-footer">
    <span class="sf-left">VI CONGRESO CARTAGENA · 2026</span>
    <span class="sf-right">LOHACEMOSXTIC.COM · SLM OFFLINE</span>
  </footer>
</section>
'''

# =============================================================================
# VARIANTE 2-M: Díptico Vertical Monumental con Grandes Cifras (56px) y Distribución Equilibrada
# =============================================================================
HTML_VAR_2M = '''
<section class="slide s-white active" id="slide-14-2m">
  <header class="slide-header">
    <div class="sh-left">
      <span class="sh-red-bar"></span>
      <span class="sh-category">03 · RESULTADOS · MODOS DE FALLO ASIMÉTRICOS</span>
    </div>
    <img src="http://localhost:8085/assets/image6.png" alt="#LoxTIC" class="sh-loxtic">
  </header>
  <div class="sh-divider"></div>

  <!-- Contenedor ajustado a altura real (720px) sin overflow -->
  <div class="slide-content-area" style="top: 175px; height: 720px; justify-content: flex-start; gap: 20px;">
    
    <!-- TÍTULO -->
    <h2 class="s-lead-question" style="font-size: 38px; font-weight: 800; margin: 0; line-height: 1.2; color: #2C0509;">
      Alucinación frente a sobre-rechazo: cómo fallan dos modelos con la misma nota
    </h2>

    <!-- GRID DE 2 COLUMNAS AMPLIAS -->
    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 36px; flex: 1;">
      
      <!-- PHI-4-MINI -->
      <div style="background: #FAF5F5; border-top: 8px solid var(--c-wine-primary); padding: 32px 36px; display: flex; flex-direction: column; justify-content: space-between;">
        
        <div>
          <!-- Cabecera -->
          <div style="display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 4px;">
            <span style="font-family: var(--font-mono); font-size: 19px; font-weight: 800; color: var(--c-wine-primary); letter-spacing: 1.5px;">
              PERFIL PERMISIVO · Q = 0.8030
            </span>
            <span style="font-family: var(--font-sans); font-size: 19px; font-weight: 800; color: var(--c-wine-primary); background: #F0E6E8; padding: 4px 10px;">
              AULA ASISTIDA
            </span>
          </div>
          <div style="font-family: var(--font-sans); font-size: 40px; font-weight: 800; color: #2C0509; margin-bottom: 28px;">
            Phi-4-mini <span style="font-size: 26px; font-weight: 600; color: #5D4A4D;">(3.8B)</span>
          </div>

          <!-- Métrica 1 -->
          <div style="margin-bottom: 28px;">
            <div style="display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 8px;">
              <span style="font-family: var(--font-sans); font-size: 23px; font-weight: 700; color: #2C0509;">
                Rechazo en 14 sondas trampa:
              </span>
              <span style="font-family: var(--font-mono); font-size: 44px; font-weight: 800; color: var(--c-red-accent); line-height: 1;">
                28.6% <span style="font-size: 22px; font-weight: 700; color: #5D4A4D;">(4/14)</span>
              </span>
            </div>
            <!-- Barra monumental 32px -->
            <div style="background: #EAE0E1; height: 30px; width: 100%; margin-bottom: 8px;">
              <div style="width: 28.6%; background: var(--c-red-accent); height: 100%;"></div>
            </div>
            <div style="font-family: var(--font-sans); font-size: 21px; color: var(--c-red-accent); font-weight: 700;">
              Alucina en 10 casos fuera del libro escolar.
            </div>
          </div>

          <!-- Métrica 2 -->
          <div>
            <div style="display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 8px;">
              <span style="font-family: var(--font-sans); font-size: 23px; font-weight: 700; color: #2C0509;">
                Falso rechazo en 84 consultas válidas:
              </span>
              <span style="font-family: var(--font-mono); font-size: 44px; font-weight: 800; color: var(--c-wine-primary); line-height: 1;">
                0.0% <span style="font-size: 22px; font-weight: 700; color: #5D4A4D;">(0/84)</span>
              </span>
            </div>
            <!-- Barra monumental 32px -->
            <div style="background: #EAE0E1; height: 30px; width: 100%; margin-bottom: 8px;">
              <div style="width: 0%; background: var(--c-wine-primary); height: 100%;"></div>
            </div>
            <div style="font-family: var(--font-sans); font-size: 21px; color: var(--c-wine-primary); font-weight: 700;">
              Fluidez total; jamás bloquea al estudiante.
            </div>
          </div>
        </div>

        <!-- Remate integrado -->
        <div style="border-top: 2px solid #EAE0E1; padding-top: 16px; margin-top: 14px;">
          <div style="font-family: var(--font-sans); font-size: 22px; font-weight: 700; color: #110103;">
            <strong style="color: var(--c-wine-primary);">Uso recomendado:</strong> Docente activo en clase que modera y rectifica alucinaciones.
          </div>
        </div>

      </div>

      <!-- QWEN2.5-3B -->
      <div style="background: #FAF5F5; border-top: 8px solid var(--c-red-accent); padding: 32px 36px; display: flex; flex-direction: column; justify-content: space-between;">
        
        <div>
          <!-- Cabecera -->
          <div style="display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 4px;">
            <span style="font-family: var(--font-mono); font-size: 19px; font-weight: 800; color: var(--c-red-accent); letter-spacing: 1.5px;">
              PERFIL CONSERVADOR · Q = 0.8010
            </span>
            <span style="font-family: var(--font-sans); font-size: 19px; font-weight: 800; color: var(--c-red-accent); background: #FDE8E9; padding: 4px 10px;">
              AUTOESTUDIO
            </span>
          </div>
          <div style="font-family: var(--font-sans); font-size: 40px; font-weight: 800; color: #2C0509; margin-bottom: 28px;">
            Qwen2.5-3B <span style="font-size: 26px; font-weight: 600; color: #5D4A4D;">(3.1B)</span>
          </div>

          <!-- Métrica 1 -->
          <div style="margin-bottom: 28px;">
            <div style="display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 8px;">
              <span style="font-family: var(--font-sans); font-size: 23px; font-weight: 700; color: #2C0509;">
                Rechazo en 14 sondas trampa:
              </span>
              <span style="font-family: var(--font-mono); font-size: 44px; font-weight: 800; color: var(--c-wine-primary); line-height: 1;">
                85.7% <span style="font-size: 22px; font-weight: 700; color: #5D4A4D;">(12/14)</span>
              </span>
            </div>
            <!-- Barra monumental 32px -->
            <div style="background: #EAE0E1; height: 30px; width: 100%; margin-bottom: 8px;">
              <div style="width: 85.7%; background: var(--c-wine-primary); height: 100%;"></div>
            </div>
            <div style="font-family: var(--font-sans); font-size: 21px; color: var(--c-wine-primary); font-weight: 700;">
              Filtro riguroso frente a preguntas trampa.
            </div>
          </div>

          <!-- Métrica 2 -->
          <div>
            <div style="display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 8px;">
              <span style="font-family: var(--font-sans); font-size: 23px; font-weight: 700; color: #2C0509;">
                Falso rechazo en 84 consultas válidas:
              </span>
              <span style="font-family: var(--font-mono); font-size: 44px; font-weight: 800; color: var(--c-red-accent); line-height: 1;">
                7.1% <span style="font-size: 22px; font-weight: 700; color: #5D4A4D;">(6/84)</span>
              </span>
            </div>
            <!-- Barra monumental 32px -->
            <div style="background: #EAE0E1; height: 30px; width: 100%; margin-bottom: 8px;">
              <div style="width: 25%; background: var(--c-red-accent); height: 100%;"></div>
            </div>
            <div style="font-family: var(--font-sans); font-size: 21px; color: var(--c-red-accent); font-weight: 700;">
              Sobre-rechazo; bloquea consultas legítimas.
            </div>
          </div>
        </div>

        <!-- Remate integrado -->
        <div style="border-top: 2px solid #EAE0E1; padding-top: 16px; margin-top: 14px;">
          <div style="font-family: var(--font-sans); font-size: 22px; font-weight: 700; color: #110103;">
            <strong style="color: var(--c-red-accent);">Uso recomendado:</strong> Autoestudio sin profesor donde prima no inducir al error al alumno.
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
  <title>Slide 14 Perfection</title>
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
    variants = [
        ('slide_14_2v.html', 'slide_14_2v.png', HTML_VAR_2V),
        ('slide_14_2h.html', 'slide_14_2h.png', HTML_VAR_2H),
        ('slide_14_2m.html', 'slide_14_2m.png', HTML_VAR_2M),
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
            page.wait_for_timeout(400)
            page.screenshot(path=png_path)
            print(f"Captured: {png_name}")

        browser.close()

if __name__ == '__main__':
    main()
