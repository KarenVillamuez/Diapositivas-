# -*- coding: utf-8 -*-
"""
Exploración de variantes ultra-limpias para Slide 14 - OPCIÓN 2:
- Barras de porcentaje limpias y protagonistas.
- Reducción drástica de texto (cero redundancia, frases telegrafiadas).
- Erradicación total del espacio muerto (distribución armónica, sin huecos vacíos).
- Paleta institucional estricta (#460811, #C9101B, #2C0509, #110103, #FAF5F5).
- Cero emojis, cero cuadros dentro de cuadros.
"""
import os
from playwright.sync_api import sync_playwright

output_dir = r"C:\Users\ASUS\.gemini\antigravity-ide\brain\a6624504-511c-4b9d-bc9a-468e348bde40"
os.makedirs(output_dir, exist_ok=True)

# -----------------------------------------------------------------------------
# VARIANTE K1: Barras Integradas Grandes + Texto Sintético (Sin Huecos)
# -----------------------------------------------------------------------------
HTML_K1 = '''
<section class="slide s-white active" id="slide-14-k1">
  <header class="slide-header">
    <div class="sh-left">
      <span class="sh-red-bar"></span>
      <span class="sh-category">03 · RESULTADOS · MODOS DE FALLO ASIMÉTRICOS</span>
    </div>
    <img src="http://localhost:8085/assets/image6.png" alt="#LoxTIC" class="sh-loxtic">
  </header>
  <div class="sh-divider"></div>

  <div class="slide-content-area" style="justify-content: center; gap: 20px;">
    
    <h2 class="s-lead-question" style="font-size: 38px; font-weight: 800; margin: 0; line-height: 1.2; color: var(--c-text-dark);">
      Alucinación frente a sobre-rechazo: cómo fallan dos modelos con la misma nota
    </h2>

    <div class="grid-2col" style="gap: 36px; align-items: stretch;">
      
      <!-- PHI-4-MINI -->
      <div style="background: var(--c-pink-bg); border-top: 8px solid var(--c-wine-primary); padding: 32px 36px; display: flex; flex-direction: column; justify-content: space-between; min-height: 520px; box-sizing: border-box;">
        
        <div>
          <!-- Cabecera -->
          <div style="display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 6px;">
            <span style="font-family: var(--font-mono); font-size: 22px; font-weight: 700; color: var(--c-wine-primary); letter-spacing: 2px;">
              PERFIL PERMISIVO
            </span>
            <span style="font-family: var(--font-mono); font-size: 24px; font-weight: 700; color: var(--c-wine-dark);">
              Q = 0.8030
            </span>
          </div>
          <div style="font-family: var(--font-sans); font-size: 38px; font-weight: 800; color: var(--c-text-dark); margin-bottom: 32px;">
            Phi-4-mini <span style="font-size: 24px; font-weight: 600; color: var(--c-gray-text);">(3.8B)</span>
          </div>

          <!-- Métrica 1 -->
          <div style="margin-bottom: 30px;">
            <div style="display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 8px;">
              <span style="font-family: var(--font-sans); font-size: 24px; font-weight: 800; color: var(--c-text-dark);">
                Sondas trampa (14 fuera de libro)
              </span>
              <span style="font-family: var(--font-mono); font-size: 36px; font-weight: 800; color: var(--c-red-accent);">
                28.6% <span style="font-size: 20px; font-weight: 700; color: var(--c-gray-text);">rechazo</span>
              </span>
            </div>
            <div style="background: var(--c-border-subtle); height: 20px; width: 100%; margin-bottom: 8px;">
              <div style="width: 28.6%; background: var(--c-red-accent); height: 100%;"></div>
            </div>
            <div style="font-family: var(--font-sans); font-size: 22px; color: var(--c-red-accent); font-weight: 700;">
              Alucina en 10 casos inventando respuestas sin base.
            </div>
          </div>

          <!-- Métrica 2 -->
          <div style="margin-bottom: 24px;">
            <div style="display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 8px;">
              <span style="font-family: var(--font-sans); font-size: 24px; font-weight: 800; color: var(--c-text-dark);">
                Consultas válidas (84 del currículo)
              </span>
              <span style="font-family: var(--font-mono); font-size: 36px; font-weight: 800; color: var(--c-wine-primary);">
                0.0% <span style="font-size: 20px; font-weight: 700; color: var(--c-gray-text);">bloqueo</span>
              </span>
            </div>
            <div style="background: var(--c-border-subtle); height: 20px; width: 100%; margin-bottom: 8px;">
              <div style="width: 0%; background: var(--c-wine-primary); height: 100%;"></div>
            </div>
            <div style="font-family: var(--font-sans); font-size: 22px; color: var(--c-wine-primary); font-weight: 700;">
              Fluidez total; jamás interrumpe a un estudiante.
            </div>
          </div>
        </div>

        <!-- Veredicto -->
        <div style="border-top: 2px solid var(--c-border-subtle); padding-top: 18px;">
          <div style="font-family: var(--font-mono); font-size: 19px; font-weight: 700; color: var(--c-wine-primary); letter-spacing: 1.5px; margin-bottom: 4px;">
            VEREDICTO PEDAGÓGICO
          </div>
          <div style="font-family: var(--font-sans); font-size: 24px; font-weight: 700; color: #110103; line-height: 1.35;">
            Aula asistida: interacción fluida donde el docente corrige las alucinaciones.
          </div>
        </div>

      </div>

      <!-- QWEN2.5-3B -->
      <div style="background: var(--c-pink-bg); border-top: 8px solid var(--c-red-accent); padding: 32px 36px; display: flex; flex-direction: column; justify-content: space-between; min-height: 520px; box-sizing: border-box;">
        
        <div>
          <!-- Cabecera -->
          <div style="display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 6px;">
            <span style="font-family: var(--font-mono); font-size: 22px; font-weight: 700; color: var(--c-red-accent); letter-spacing: 2px;">
              PERFIL CONSERVADOR
            </span>
            <span style="font-family: var(--font-mono); font-size: 24px; font-weight: 700; color: var(--c-wine-dark);">
              Q = 0.8010
            </span>
          </div>
          <div style="font-family: var(--font-sans); font-size: 38px; font-weight: 800; color: var(--c-text-dark); margin-bottom: 32px;">
            Qwen2.5-3B <span style="font-size: 24px; font-weight: 600; color: var(--c-gray-text);">(3.1B)</span>
          </div>

          <!-- Métrica 1 -->
          <div style="margin-bottom: 30px;">
            <div style="display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 8px;">
              <span style="font-family: var(--font-sans); font-size: 24px; font-weight: 800; color: var(--c-text-dark);">
                Sondas trampa (14 fuera de libro)
              </span>
              <span style="font-family: var(--font-mono); font-size: 36px; font-weight: 800; color: var(--c-wine-primary);">
                85.7% <span style="font-size: 20px; font-weight: 700; color: var(--c-gray-text);">rechazo</span>
              </span>
            </div>
            <div style="background: var(--c-border-subtle); height: 20px; width: 100%; margin-bottom: 8px;">
              <div style="width: 85.7%; background: var(--c-wine-primary); height: 100%;"></div>
            </div>
            <div style="font-family: var(--font-sans); font-size: 22px; color: var(--c-wine-primary); font-weight: 700;">
              Filtro riguroso; bloquea con éxito preguntas trampa.
            </div>
          </div>

          <!-- Métrica 2 -->
          <div style="margin-bottom: 24px;">
            <div style="display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 8px;">
              <span style="font-family: var(--font-sans); font-size: 24px; font-weight: 800; color: var(--c-text-dark);">
                Consultas válidas (84 del currículo)
              </span>
              <span style="font-family: var(--font-mono); font-size: 36px; font-weight: 800; color: var(--c-red-accent);">
                7.1% <span style="font-size: 20px; font-weight: 700; color: var(--c-gray-text);">bloqueo</span>
              </span>
            </div>
            <div style="background: var(--c-border-subtle); height: 20px; width: 100%; margin-bottom: 8px;">
              <div style="width: 25%; background: var(--c-red-accent); height: 100%;"></div>
            </div>
            <div style="font-family: var(--font-sans); font-size: 22px; color: var(--c-red-accent); font-weight: 700;">
              Sobre-rechazo; silencia consultas legítimas por cautela.
            </div>
          </div>
        </div>

        <!-- Veredicto -->
        <div style="border-top: 2px solid var(--c-border-subtle); padding-top: 18px;">
          <div style="font-family: var(--font-mono); font-size: 19px; font-weight: 700; color: var(--c-red-accent); letter-spacing: 1.5px; margin-bottom: 4px;">
            VEREDICTO PEDAGÓGICO
          </div>
          <div style="font-family: var(--font-sans); font-size: 24px; font-weight: 700; color: #110103; line-height: 1.35;">
            Autoestudio: sin docente, prima la certeza de no inducir al error al alumno.
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
# VARIANTE K2: Formato Ultra-Sintético (Métricas Hero + Barra Inline)
# -----------------------------------------------------------------------------
HTML_K2 = '''
<section class="slide s-white active" id="slide-14-k2">
  <header class="slide-header">
    <div class="sh-left">
      <span class="sh-red-bar"></span>
      <span class="sh-category">03 · RESULTADOS · MODOS DE FALLO ASIMÉTRICOS</span>
    </div>
    <img src="http://localhost:8085/assets/image6.png" alt="#LoxTIC" class="sh-loxtic">
  </header>
  <div class="sh-divider"></div>

  <div class="slide-content-area" style="justify-content: center; gap: 24px;">
    
    <h2 class="s-lead-question" style="font-size: 38px; font-weight: 800; margin: 0; line-height: 1.2; color: var(--c-text-dark);">
      Alucinación frente a sobre-rechazo: cómo fallan dos modelos con la misma nota
    </h2>

    <div class="grid-2col" style="gap: 40px; align-items: stretch;">
      
      <!-- PHI-4-MINI -->
      <div style="background: var(--c-pink-bg); border-top: 8px solid var(--c-wine-primary); padding: 36px 38px; display: flex; flex-direction: column; justify-content: space-between; min-height: 520px; box-sizing: border-box;">
        
        <div>
          <!-- Cabecera -->
          <div style="display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 4px;">
            <span style="font-family: var(--font-mono); font-size: 22px; font-weight: 700; color: var(--c-wine-primary); letter-spacing: 2px;">
              PERFIL PERMISIVO
            </span>
            <span style="font-family: var(--font-mono); font-size: 26px; font-weight: 800; color: var(--c-wine-dark);">
              Q = 0.8030
            </span>
          </div>
          <div style="font-family: var(--font-sans); font-size: 40px; font-weight: 800; color: var(--c-text-dark); margin-bottom: 34px;">
            Phi-4-mini <span style="font-size: 26px; font-weight: 600; color: var(--c-gray-text);">(3.8B)</span>
          </div>

          <!-- Métrica 1 -->
          <div style="margin-bottom: 28px;">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px;">
              <span style="font-family: var(--font-sans); font-size: 24px; font-weight: 700; color: var(--c-text-dark);">
                Rechazo en trampas (14):
              </span>
              <span style="font-family: var(--font-mono); font-size: 42px; font-weight: 800; color: var(--c-red-accent);">
                28.6%
              </span>
            </div>
            <div style="background: var(--c-border-subtle); height: 18px; width: 100%; margin-bottom: 8px;">
              <div style="width: 28.6%; background: var(--c-red-accent); height: 100%;"></div>
            </div>
            <div style="font-family: var(--font-sans); font-size: 22px; color: var(--c-red-accent); font-weight: 700;">
              Alucina en 10 casos fuera del libro.
            </div>
          </div>

          <!-- Métrica 2 -->
          <div style="margin-bottom: 20px;">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px;">
              <span style="font-family: var(--font-sans); font-size: 24px; font-weight: 700; color: var(--c-text-dark);">
                Bloqueo en válidas (84):
              </span>
              <span style="font-family: var(--font-mono); font-size: 42px; font-weight: 800; color: var(--c-wine-primary);">
                0.0%
              </span>
            </div>
            <div style="background: var(--c-border-subtle); height: 18px; width: 100%; margin-bottom: 8px;">
              <div style="width: 0%; background: var(--c-wine-primary); height: 100%;"></div>
            </div>
            <div style="font-family: var(--font-sans); font-size: 22px; color: var(--c-wine-primary); font-weight: 700;">
              Fluidez total; jamás frena al alumno.
            </div>
          </div>
        </div>

        <!-- Veredicto -->
        <div style="border-top: 2px solid var(--c-border-subtle); padding-top: 18px;">
          <div style="font-family: var(--font-sans); font-size: 24px; font-weight: 700; color: #110103; line-height: 1.35;">
            <strong style="color: var(--c-wine-primary);">Aula asistida:</strong> interacción fluida; el docente en clase modera y corrige alucinaciones.
          </div>
        </div>

      </div>

      <!-- QWEN2.5-3B -->
      <div style="background: var(--c-pink-bg); border-top: 8px solid var(--c-red-accent); padding: 36px 38px; display: flex; flex-direction: column; justify-content: space-between; min-height: 520px; box-sizing: border-box;">
        
        <div>
          <!-- Cabecera -->
          <div style="display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 4px;">
            <span style="font-family: var(--font-mono); font-size: 22px; font-weight: 700; color: var(--c-red-accent); letter-spacing: 2px;">
              PERFIL CONSERVADOR
            </span>
            <span style="font-family: var(--font-mono); font-size: 26px; font-weight: 800; color: var(--c-wine-dark);">
              Q = 0.8010
            </span>
          </div>
          <div style="font-family: var(--font-sans); font-size: 40px; font-weight: 800; color: var(--c-text-dark); margin-bottom: 34px;">
            Qwen2.5-3B <span style="font-size: 26px; font-weight: 600; color: var(--c-gray-text);">(3.1B)</span>
          </div>

          <!-- Métrica 1 -->
          <div style="margin-bottom: 28px;">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px;">
              <span style="font-family: var(--font-sans); font-size: 24px; font-weight: 700; color: var(--c-text-dark);">
                Rechazo en trampas (14):
              </span>
              <span style="font-family: var(--font-mono); font-size: 42px; font-weight: 800; color: var(--c-wine-primary);">
                85.7%
              </span>
            </div>
            <div style="background: var(--c-border-subtle); height: 18px; width: 100%; margin-bottom: 8px;">
              <div style="width: 85.7%; background: var(--c-wine-primary); height: 100%;"></div>
            </div>
            <div style="font-family: var(--font-sans); font-size: 22px; color: var(--c-wine-primary); font-weight: 700;">
              Filtro riguroso frente a preguntas trampa.
            </div>
          </div>

          <!-- Métrica 2 -->
          <div style="margin-bottom: 20px;">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px;">
              <span style="font-family: var(--font-sans); font-size: 24px; font-weight: 700; color: var(--c-text-dark);">
                Bloqueo en válidas (84):
              </span>
              <span style="font-family: var(--font-mono); font-size: 42px; font-weight: 800; color: var(--c-red-accent);">
                7.1%
              </span>
            </div>
            <div style="background: var(--c-border-subtle); height: 18px; width: 100%; margin-bottom: 8px;">
              <div style="width: 25%; background: var(--c-red-accent); height: 100%;"></div>
            </div>
            <div style="font-family: var(--font-sans); font-size: 22px; color: var(--c-red-accent); font-weight: 700;">
              Sobre-rechazo por cautela extrema.
            </div>
          </div>
        </div>

        <!-- Veredicto -->
        <div style="border-top: 2px solid var(--c-border-subtle); padding-top: 18px;">
          <div style="font-family: var(--font-sans); font-size: 24px; font-weight: 700; color: #110103; line-height: 1.35;">
            <strong style="color: var(--c-red-accent);">Autoestudio:</strong> sin docente presente; prima la certeza absoluta de no inducir al error.
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
# VARIANTE K3: Díptico con Tarjetas Nativas Espaciadas + Barra Inferior de Síntesis
# -----------------------------------------------------------------------------
HTML_K3 = '''
<section class="slide s-white active" id="slide-14-k3">
  <header class="slide-header">
    <div class="sh-left">
      <span class="sh-red-bar"></span>
      <span class="sh-category">03 · RESULTADOS · MODOS DE FALLO ASIMÉTRICOS</span>
    </div>
    <img src="http://localhost:8085/assets/image6.png" alt="#LoxTIC" class="sh-loxtic">
  </header>
  <div class="sh-divider"></div>

  <div class="slide-content-area" style="justify-content: space-between; padding: 6px 0 10px 0;">
    
    <h2 class="s-lead-question" style="font-size: 38px; font-weight: 800; margin: 0; line-height: 1.2; color: var(--c-text-dark);">
      Alucinación frente a sobre-rechazo: cómo fallan dos modelos con la misma nota
    </h2>

    <div class="grid-2col" style="gap: 36px; align-items: stretch; flex: 1; margin: 18px 0 16px 0;">
      
      <!-- PHI-4-MINI -->
      <div style="background: var(--c-pink-bg); border-top: 8px solid var(--c-wine-primary); padding: 28px 34px; display: flex; flex-direction: column; justify-content: space-between; box-sizing: border-box;">
        <div>
          <div style="display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 4px;">
            <span style="font-family: var(--font-mono); font-size: 21px; font-weight: 700; color: var(--c-wine-primary); letter-spacing: 2px;">
              PERFIL PERMISIVO
            </span>
            <span style="font-family: var(--font-mono); font-size: 24px; font-weight: 800; color: var(--c-wine-dark);">
              Q = 0.8030
            </span>
          </div>
          <div style="font-family: var(--font-sans); font-size: 36px; font-weight: 800; color: var(--c-text-dark); margin-bottom: 28px;">
            Phi-4-mini (3.8B)
          </div>

          <!-- Métrica 1 -->
          <div style="margin-bottom: 24px;">
            <div style="display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 6px;">
              <span style="font-family: var(--font-sans); font-size: 23px; font-weight: 700; color: var(--c-text-dark);">
                Rechazo en trampas (14 fuera de libro):
              </span>
              <span style="font-family: var(--font-mono); font-size: 38px; font-weight: 800; color: var(--c-red-accent);">
                28.6%
              </span>
            </div>
            <div style="background: var(--c-border-subtle); height: 16px; width: 100%; margin-bottom: 6px;">
              <div style="width: 28.6%; background: var(--c-red-accent); height: 100%;"></div>
            </div>
            <div style="font-family: var(--font-sans); font-size: 21px; color: var(--c-red-accent); font-weight: 700;">
              Alucina en 10 casos fuera del libro.
            </div>
          </div>

          <!-- Métrica 2 -->
          <div style="margin-bottom: 16px;">
            <div style="display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 6px;">
              <span style="font-family: var(--font-sans); font-size: 23px; font-weight: 700; color: var(--c-text-dark);">
                Bloqueo en válidas (84 curriculares):
              </span>
              <span style="font-family: var(--font-mono); font-size: 38px; font-weight: 800; color: var(--c-wine-primary);">
                0.0%
              </span>
            </div>
            <div style="background: var(--c-border-subtle); height: 16px; width: 100%; margin-bottom: 6px;">
              <div style="width: 0%; background: var(--c-wine-primary); height: 100%;"></div>
            </div>
            <div style="font-family: var(--font-sans); font-size: 21px; color: var(--c-wine-primary); font-weight: 700;">
              Fluidez total; jamás frena al alumno.
            </div>
          </div>
        </div>

        <div style="border-top: 1.5px solid var(--c-border-subtle); padding-top: 14px; font-family: var(--font-sans); font-size: 23px; font-weight: 700; color: #110103; line-height: 1.35;">
          <strong style="color: var(--c-wine-primary);">Aula asistida:</strong> interacción fluida guiada por docente activo.
        </div>
      </div>

      <!-- QWEN2.5-3B -->
      <div style="background: var(--c-pink-bg); border-top: 8px solid var(--c-red-accent); padding: 28px 34px; display: flex; flex-direction: column; justify-content: space-between; box-sizing: border-box;">
        <div>
          <div style="display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 4px;">
            <span style="font-family: var(--font-mono); font-size: 21px; font-weight: 700; color: var(--c-red-accent); letter-spacing: 2px;">
              PERFIL CONSERVADOR
            </span>
            <span style="font-family: var(--font-mono); font-size: 24px; font-weight: 800; color: var(--c-wine-dark);">
              Q = 0.8010
            </span>
          </div>
          <div style="font-family: var(--font-sans); font-size: 36px; font-weight: 800; color: var(--c-text-dark); margin-bottom: 28px;">
            Qwen2.5-3B (3.1B)
          </div>

          <!-- Métrica 1 -->
          <div style="margin-bottom: 24px;">
            <div style="display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 6px;">
              <span style="font-family: var(--font-sans); font-size: 23px; font-weight: 700; color: var(--c-text-dark);">
                Rechazo en trampas (14 fuera de libro):
              </span>
              <span style="font-family: var(--font-mono); font-size: 38px; font-weight: 800; color: var(--c-wine-primary);">
                85.7%
              </span>
            </div>
            <div style="background: var(--c-border-subtle); height: 16px; width: 100%; margin-bottom: 6px;">
              <div style="width: 85.7%; background: var(--c-wine-primary); height: 100%;"></div>
            </div>
            <div style="font-family: var(--font-sans); font-size: 21px; color: var(--c-wine-primary); font-weight: 700;">
              Filtro riguroso frente a preguntas trampa.
            </div>
          </div>

          <!-- Métrica 2 -->
          <div style="margin-bottom: 16px;">
            <div style="display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 6px;">
              <span style="font-family: var(--font-sans); font-size: 23px; font-weight: 700; color: var(--c-text-dark);">
                Bloqueo en válidas (84 curriculares):
              </span>
              <span style="font-family: var(--font-mono); font-size: 38px; font-weight: 800; color: var(--c-red-accent);">
                7.1%
              </span>
            </div>
            <div style="background: var(--c-border-subtle); height: 16px; width: 100%; margin-bottom: 6px;">
              <div style="width: 25%; background: var(--c-red-accent); height: 100%;"></div>
            </div>
            <div style="font-family: var(--font-sans); font-size: 21px; color: var(--c-red-accent); font-weight: 700;">
              Sobre-rechazo por cautela extrema.
            </div>
          </div>
        </div>

        <div style="border-top: 1.5px solid var(--c-border-subtle); padding-top: 14px; font-family: var(--font-sans); font-size: 23px; font-weight: 700; color: #110103; line-height: 1.35;">
          <strong style="color: var(--c-red-accent);">Autoestudio:</strong> sin docente; prima no inducir al error al alumno.
        </div>
      </div>

    </div>

    <!-- SÍNTESIS PEDAGÓGICA AL PIE (OCUPA EL ESPACIO INFERIOR NATURALMENTE) -->
    <div style="background: #FFFFFF; border: 1.5px solid var(--c-wine-primary); padding: 14px 24px; display: flex; justify-content: space-between; align-items: center;">
      <span style="font-family: var(--font-sans); font-size: 22px; font-weight: 700; color: var(--c-text-dark);">
        Tesis pedagógica: la nota idéntica (~0.80) oculta riesgos opuestos en el aula.
      </span>
      <span style="font-family: var(--font-mono); font-size: 20px; font-weight: 700; color: var(--c-wine-primary);">
        TABLA 3 DEL PAPER
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
  <title>Test Slide 14 Clean Opcion 2</title>
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
        ('slide_14_k1.html', 'slide_14_k1.png', HTML_K1),
        ('slide_14_k2.html', 'slide_14_k2.png', HTML_K2),
        ('slide_14_k3.html', 'slide_14_k3.png', HTML_K3),
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
