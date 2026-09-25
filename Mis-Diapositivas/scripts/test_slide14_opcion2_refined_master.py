# -*- coding: utf-8 -*-
"""
Comparativa definitiva de 3 variantes ultra-limpias de Opción 2:
- R1: Díptico Vertical + Franja de Síntesis Inferior (Barras 30px, cero espacio muerto, remate armónico).
- R2: Díptico Vertical Centrado sin franja (Cards más altas y generosas, barras 32px, números 46px, espaciado uniforme sin huecos).
- R3: Díptico Panorámico de 2 Filas (100% horizontal, barras de 30px, 0 roturas de texto, lectura fluida en 16:9).
"""
import os
from playwright.sync_api import sync_playwright

output_dir = r"C:\Users\ASUS\.gemini\antigravity-ide\brain\a6624504-511c-4b9d-bc9a-468e348bde40"
os.makedirs(output_dir, exist_ok=True)

# -----------------------------------------------------------------------------
# VARIANTE R1: Vertical con Franja Inferior de Síntesis
# -----------------------------------------------------------------------------
HTML_R1 = '''
<section class="slide s-white active" id="slide-14-r1">
  <header class="slide-header">
    <div class="sh-left">
      <span class="sh-red-bar"></span>
      <span class="sh-category">03 · RESULTADOS · MODOS DE FALLO ASIMÉTRICOS</span>
    </div>
    <img src="http://localhost:8085/assets/image6.png" alt="#LoxTIC" class="sh-loxtic">
  </header>
  <div class="sh-divider"></div>

  <div class="slide-content-area" style="top: 175px; height: 720px; justify-content: flex-start; gap: 20px;">
    
    <h2 class="s-lead-question" style="font-size: 38px; font-weight: 800; margin: 0; line-height: 1.2; color: #2C0509;">
      Alucinación frente a sobre-rechazo: cómo fallan dos modelos con la misma nota
    </h2>

    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 36px;">
      
      <!-- PHI-4-MINI -->
      <div style="background: #FAF5F5; border-top: 8px solid var(--c-wine-primary); padding: 26px 32px; display: flex; flex-direction: column; gap: 22px;">
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

        <div>
          <div style="display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 6px;">
            <span style="font-family: var(--font-sans); font-size: 22px; font-weight: 700; color: #2C0509;">
              Rechazo en 14 sondas trampa:
            </span>
            <span style="font-family: var(--font-mono); font-size: 40px; font-weight: 800; color: var(--c-red-accent); line-height: 1;">
              28.6% <span style="font-size: 20px; font-weight: 700; color: #5D4A4D;">(4/14)</span>
            </span>
          </div>
          <div style="background: #EAE0E1; height: 30px; width: 100%; margin-bottom: 6px;">
            <div style="width: 28.6%; background: var(--c-red-accent); height: 100%;"></div>
          </div>
          <div style="font-family: var(--font-sans); font-size: 20px; color: var(--c-red-accent); font-weight: 700;">
            Alucina en 10 casos fuera del libro escolar.
          </div>
        </div>

        <div>
          <div style="display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 6px;">
            <span style="font-family: var(--font-sans); font-size: 22px; font-weight: 700; color: #2C0509;">
              Falso rechazo en 84 consultas válidas:
            </span>
            <span style="font-family: var(--font-mono); font-size: 40px; font-weight: 800; color: var(--c-wine-primary); line-height: 1;">
              0.0% <span style="font-size: 20px; font-weight: 700; color: #5D4A4D;">(0/84)</span>
            </span>
          </div>
          <div style="background: #EAE0E1; height: 30px; width: 100%; margin-bottom: 6px;">
            <div style="width: 0%; background: var(--c-wine-primary); height: 100%;"></div>
          </div>
          <div style="font-family: var(--font-sans); font-size: 20px; color: var(--c-wine-primary); font-weight: 700;">
            Fluidez total; jamás bloquea al estudiante.
          </div>
        </div>

        <div style="border-top: 1px solid #EAE0E1; padding-top: 10px; font-family: var(--font-sans); font-size: 20px; color: #110103; font-weight: 600;">
          <strong style="color: var(--c-wine-primary);">Uso recomendado:</strong> Docente activo en clase que modera y rectifica alucinaciones.
        </div>
      </div>

      <!-- QWEN2.5-3B -->
      <div style="background: #FAF5F5; border-top: 8px solid var(--c-red-accent); padding: 26px 32px; display: flex; flex-direction: column; gap: 22px;">
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

        <div>
          <div style="display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 6px;">
            <span style="font-family: var(--font-sans); font-size: 22px; font-weight: 700; color: #2C0509;">
              Rechazo en 14 sondas trampa:
            </span>
            <span style="font-family: var(--font-mono); font-size: 40px; font-weight: 800; color: var(--c-wine-primary); line-height: 1;">
              85.7% <span style="font-size: 20px; font-weight: 700; color: #5D4A4D;">(12/14)</span>
            </span>
          </div>
          <div style="background: #EAE0E1; height: 30px; width: 100%; margin-bottom: 6px;">
            <div style="width: 85.7%; background: var(--c-wine-primary); height: 100%;"></div>
          </div>
          <div style="font-family: var(--font-sans); font-size: 20px; color: var(--c-wine-primary); font-weight: 700;">
            Filtro riguroso frente a preguntas trampa.
          </div>
        </div>

        <div>
          <div style="display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 6px;">
            <span style="font-family: var(--font-sans); font-size: 22px; font-weight: 700; color: #2C0509;">
              Falso rechazo en 84 consultas válidas:
            </span>
            <span style="font-family: var(--font-mono); font-size: 40px; font-weight: 800; color: var(--c-red-accent); line-height: 1;">
              7.1% <span style="font-size: 20px; font-weight: 700; color: #5D4A4D;">(6/84)</span>
            </span>
          </div>
          <div style="background: #EAE0E1; height: 30px; width: 100%; margin-bottom: 6px;">
            <div style="width: 25%; background: var(--c-red-accent); height: 100%;"></div>
          </div>
          <div style="font-family: var(--font-sans); font-size: 20px; color: var(--c-red-accent); font-weight: 700;">
            Sobre-rechazo; bloquea consultas legítimas.
          </div>
        </div>

        <div style="border-top: 1px solid #EAE0E1; padding-top: 10px; font-family: var(--font-sans); font-size: 20px; color: #110103; font-weight: 600;">
          <strong style="color: var(--c-red-accent);">Uso recomendado:</strong> Autoestudio sin profesor donde prima no inducir al error al alumno.
        </div>
      </div>

    </div>

    <!-- FRANJA INFERIOR -->
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

# -----------------------------------------------------------------------------
# VARIANTE R2: Vertical Centrado Puro sin Franja (Cards con relleno armonioso)
# -----------------------------------------------------------------------------
HTML_R2 = '''
<section class="slide s-white active" id="slide-14-r2">
  <header class="slide-header">
    <div class="sh-left">
      <span class="sh-red-bar"></span>
      <span class="sh-category">03 · RESULTADOS · MODOS DE FALLO ASIMÉTRICOS</span>
    </div>
    <img src="http://localhost:8085/assets/image6.png" alt="#LoxTIC" class="sh-loxtic">
  </header>
  <div class="sh-divider"></div>

  <div class="slide-content-area" style="top: 175px; height: 720px; justify-content: center; gap: 26px;">
    
    <h2 class="s-lead-question" style="font-size: 38px; font-weight: 800; margin: 0; line-height: 1.2; color: #2C0509;">
      Alucinación frente a sobre-rechazo: cómo fallan dos modelos con la misma nota
    </h2>

    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 36px;">
      
      <!-- PHI-4-MINI -->
      <div style="background: #FAF5F5; border-top: 8px solid var(--c-wine-primary); padding: 30px 34px; display: flex; flex-direction: column; gap: 28px;">
        <div style="display: flex; justify-content: space-between; align-items: baseline; border-bottom: 2px solid #EAE0E1; padding-bottom: 12px;">
          <div>
            <div style="font-family: var(--font-sans); font-size: 38px; font-weight: 800; color: #2C0509; line-height: 1.1;">
              Phi-4-mini <span style="font-size: 24px; font-weight: 600; color: #5D4A4D;">(3.8B)</span>
            </div>
            <div style="font-family: var(--font-mono); font-size: 19px; font-weight: 700; color: var(--c-wine-primary); letter-spacing: 1px; margin-top: 3px;">
              PERFIL PERMISIVO · Q = 0.8030
            </div>
          </div>
          <span style="font-family: var(--font-sans); font-size: 21px; font-weight: 800; color: var(--c-wine-primary); background: #F0E6E8; padding: 5px 14px;">
            Aula Asistida
          </span>
        </div>

        <div>
          <div style="display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 8px;">
            <span style="font-family: var(--font-sans); font-size: 23px; font-weight: 700; color: #2C0509;">
              Rechazo en 14 sondas trampa:
            </span>
            <span style="font-family: var(--font-mono); font-size: 42px; font-weight: 800; color: var(--c-red-accent); line-height: 1;">
              28.6% <span style="font-size: 22px; font-weight: 700; color: #5D4A4D;">(4/14)</span>
            </span>
          </div>
          <div style="background: #EAE0E1; height: 32px; width: 100%; margin-bottom: 8px;">
            <div style="width: 28.6%; background: var(--c-red-accent); height: 100%;"></div>
          </div>
          <div style="font-family: var(--font-sans); font-size: 21px; color: var(--c-red-accent); font-weight: 700;">
            Alucina en 10 casos fuera del libro escolar.
          </div>
        </div>

        <div>
          <div style="display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 8px;">
            <span style="font-family: var(--font-sans); font-size: 23px; font-weight: 700; color: #2C0509;">
              Falso rechazo en 84 consultas válidas:
            </span>
            <span style="font-family: var(--font-mono); font-size: 42px; font-weight: 800; color: var(--c-wine-primary); line-height: 1;">
              0.0% <span style="font-size: 22px; font-weight: 700; color: #5D4A4D;">(0/84)</span>
            </span>
          </div>
          <div style="background: #EAE0E1; height: 32px; width: 100%; margin-bottom: 8px;">
            <div style="width: 0%; background: var(--c-wine-primary); height: 100%;"></div>
          </div>
          <div style="font-family: var(--font-sans); font-size: 21px; color: var(--c-wine-primary); font-weight: 700;">
            Fluidez total; jamás bloquea al estudiante.
          </div>
        </div>

        <div style="border-top: 2px solid #EAE0E1; padding-top: 14px; font-family: var(--font-sans); font-size: 21px; color: #110103; font-weight: 600;">
          <strong style="color: var(--c-wine-primary);">Uso pedagógico:</strong> Docente activo en clase que modera y rectifica alucinaciones.
        </div>
      </div>

      <!-- QWEN2.5-3B -->
      <div style="background: #FAF5F5; border-top: 8px solid var(--c-red-accent); padding: 30px 34px; display: flex; flex-direction: column; gap: 28px;">
        <div style="display: flex; justify-content: space-between; align-items: baseline; border-bottom: 2px solid #EAE0E1; padding-bottom: 12px;">
          <div>
            <div style="font-family: var(--font-sans); font-size: 38px; font-weight: 800; color: #2C0509; line-height: 1.1;">
              Qwen2.5-3B <span style="font-size: 24px; font-weight: 600; color: #5D4A4D;">(3.1B)</span>
            </div>
            <div style="font-family: var(--font-mono); font-size: 19px; font-weight: 700; color: var(--c-red-accent); letter-spacing: 1px; margin-top: 3px;">
              PERFIL CONSERVADOR · Q = 0.8010
            </div>
          </div>
          <span style="font-family: var(--font-sans); font-size: 21px; font-weight: 800; color: var(--c-red-accent); background: #FDE8E9; padding: 5px 14px;">
            Autoestudio
          </span>
        </div>

        <div>
          <div style="display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 8px;">
            <span style="font-family: var(--font-sans); font-size: 23px; font-weight: 700; color: #2C0509;">
              Rechazo en 14 sondas trampa:
            </span>
            <span style="font-family: var(--font-mono); font-size: 42px; font-weight: 800; color: var(--c-wine-primary); line-height: 1;">
              85.7% <span style="font-size: 22px; font-weight: 700; color: #5D4A4D;">(12/14)</span>
            </span>
          </div>
          <div style="background: #EAE0E1; height: 32px; width: 100%; margin-bottom: 8px;">
            <div style="width: 85.7%; background: var(--c-wine-primary); height: 100%;"></div>
          </div>
          <div style="font-family: var(--font-sans); font-size: 21px; color: var(--c-wine-primary); font-weight: 700;">
            Filtro riguroso frente a preguntas trampa.
          </div>
        </div>

        <div>
          <div style="display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 8px;">
            <span style="font-family: var(--font-sans); font-size: 23px; font-weight: 700; color: #2C0509;">
              Falso rechazo en 84 consultas válidas:
            </span>
            <span style="font-family: var(--font-mono); font-size: 42px; font-weight: 800; color: var(--c-red-accent); line-height: 1;">
              7.1% <span style="font-size: 22px; font-weight: 700; color: #5D4A4D;">(6/84)</span>
            </span>
          </div>
          <div style="background: #EAE0E1; height: 32px; width: 100%; margin-bottom: 8px;">
            <div style="width: 25%; background: var(--c-red-accent); height: 100%;"></div>
          </div>
          <div style="font-family: var(--font-sans); font-size: 21px; color: var(--c-red-accent); font-weight: 700;">
            Sobre-rechazo; bloquea consultas legítimas.
          </div>
        </div>

        <div style="border-top: 2px solid #EAE0E1; padding-top: 14px; font-family: var(--font-sans); font-size: 21px; color: #110103; font-weight: 600;">
          <strong style="color: var(--c-red-accent);">Uso pedagógico:</strong> Autoestudio sin profesor donde prima no inducir al error al alumno.
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
# VARIANTE R3: Panorámico Horizontal 16:9 con Llenado Perfecto
# -----------------------------------------------------------------------------
HTML_R3 = '''
<section class="slide s-white active" id="slide-14-r3">
  <header class="slide-header">
    <div class="sh-left">
      <span class="sh-red-bar"></span>
      <span class="sh-category">03 · RESULTADOS · MODOS DE FALLO ASIMÉTRICOS</span>
    </div>
    <img src="http://localhost:8085/assets/image6.png" alt="#LoxTIC" class="sh-loxtic">
  </header>
  <div class="sh-divider"></div>

  <div class="slide-content-area" style="top: 175px; height: 720px; justify-content: center; gap: 26px;">
    
    <h2 class="s-lead-question" style="font-size: 38px; font-weight: 800; margin: 0; line-height: 1.2; color: #2C0509;">
      Alucinación frente a sobre-rechazo: cómo fallan dos modelos con la misma nota
    </h2>

    <!-- FILA 1: PHI-4-MINI -->
    <div style="background: #FAF5F5; border-left: 10px solid var(--c-wine-primary); padding: 26px 36px; display: grid; grid-template-columns: 460px 1fr 1fr; gap: 44px; align-items: center;">
      <div style="border-right: 2px solid #EAE0E1; padding-right: 32px;">
        <div style="font-family: var(--font-mono); font-size: 19px; font-weight: 700; color: var(--c-wine-primary); letter-spacing: 1.5px; margin-bottom: 2px;">
          PERFIL PERMISIVO · Q = 0.8030
        </div>
        <div style="font-family: var(--font-sans); font-size: 40px; font-weight: 800; color: #2C0509; line-height: 1.1; margin-bottom: 6px;">
          Phi-4-mini <span style="font-size: 26px; font-weight: 600; color: #5D4A4D;">3.8B</span>
        </div>
        <div style="font-family: var(--font-sans); font-size: 22px; font-weight: 700; color: #110103;">
          <strong style="color: var(--c-wine-primary);">Aula asistida:</strong> con docente activo.
        </div>
      </div>

      <div>
        <div style="display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 6px;">
          <span style="font-family: var(--font-sans); font-size: 22px; font-weight: 700; color: #2C0509;">Rechazo en trampas (14):</span>
          <span style="font-family: var(--font-mono); font-size: 40px; font-weight: 800; color: var(--c-red-accent); line-height: 1;">28.6%</span>
        </div>
        <div style="background: #EAE0E1; height: 30px; width: 100%; margin-bottom: 6px;">
          <div style="width: 28.6%; background: var(--c-red-accent); height: 100%;"></div>
        </div>
        <div style="font-family: var(--font-sans); font-size: 20px; color: var(--c-red-accent); font-weight: 700;">
          Alucina en 10 casos fuera del libro.
        </div>
      </div>

      <div>
        <div style="display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 6px;">
          <span style="font-family: var(--font-sans); font-size: 22px; font-weight: 700; color: #2C0509;">Falso rechazo (84 válidas):</span>
          <span style="font-family: var(--font-mono); font-size: 40px; font-weight: 800; color: var(--c-wine-primary); line-height: 1;">0.0%</span>
        </div>
        <div style="background: #EAE0E1; height: 30px; width: 100%; margin-bottom: 6px;">
          <div style="width: 0%; background: var(--c-wine-primary); height: 100%;"></div>
        </div>
        <div style="font-family: var(--font-sans); font-size: 20px; color: var(--c-wine-primary); font-weight: 700;">
          Fluidez total; jamás frena al alumno.
        </div>
      </div>
    </div>

    <!-- FILA 2: QWEN2.5-3B -->
    <div style="background: #FAF5F5; border-left: 10px solid var(--c-red-accent); padding: 26px 36px; display: grid; grid-template-columns: 460px 1fr 1fr; gap: 44px; align-items: center;">
      <div style="border-right: 2px solid #EAE0E1; padding-right: 32px;">
        <div style="font-family: var(--font-mono); font-size: 19px; font-weight: 700; color: var(--c-red-accent); letter-spacing: 1.5px; margin-bottom: 2px;">
          PERFIL CONSERVADOR · Q = 0.8010
        </div>
        <div style="font-family: var(--font-sans); font-size: 40px; font-weight: 800; color: #2C0509; line-height: 1.1; margin-bottom: 6px;">
          Qwen2.5-3B <span style="font-size: 26px; font-weight: 600; color: #5D4A4D;">3.1B</span>
        </div>
        <div style="font-family: var(--font-sans); font-size: 22px; font-weight: 700; color: #110103;">
          <strong style="color: var(--c-red-accent);">Autoestudio:</strong> sin docente presente.
        </div>
      </div>

      <div>
        <div style="display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 6px;">
          <span style="font-family: var(--font-sans); font-size: 22px; font-weight: 700; color: #2C0509;">Rechazo en trampas (14):</span>
          <span style="font-family: var(--font-mono); font-size: 40px; font-weight: 800; color: var(--c-wine-primary); line-height: 1;">85.7%</span>
        </div>
        <div style="background: #EAE0E1; height: 30px; width: 100%; margin-bottom: 6px;">
          <div style="width: 85.7%; background: var(--c-wine-primary); height: 100%;"></div>
        </div>
        <div style="font-family: var(--font-sans); font-size: 20px; color: var(--c-wine-primary); font-weight: 700;">
          Filtro riguroso frente a trampas.
        </div>
      </div>

      <div>
        <div style="display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 6px;">
          <span style="font-family: var(--font-sans); font-size: 22px; font-weight: 700; color: #2C0509;">Falso rechazo (84 válidas):</span>
          <span style="font-family: var(--font-mono); font-size: 40px; font-weight: 800; color: var(--c-red-accent); line-height: 1;">7.1%</span>
        </div>
        <div style="background: #EAE0E1; height: 30px; width: 100%; margin-bottom: 6px;">
          <div style="width: 25%; background: var(--c-red-accent); height: 100%;"></div>
        </div>
        <div style="font-family: var(--font-sans); font-size: 20px; color: var(--c-red-accent); font-weight: 700;">
          Sobre-rechazo por cautela extrema.
        </div>
      </div>
    </div>

    <!-- REMATE EDITORIAL INFERIOR -->
    <div style="display: flex; justify-content: space-between; align-items: center; border-top: 1px solid #EAE0E1; padding-top: 12px;">
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

HTML_WRAPPER = '''<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Slide 14 Refinements</title>
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
        ('slide_14_r1.html', 'slide_14_r1.png', HTML_R1),
        ('slide_14_r2.html', 'slide_14_r2.png', HTML_R2),
        ('slide_14_r3.html', 'slide_14_r3.png', HTML_R3),
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
