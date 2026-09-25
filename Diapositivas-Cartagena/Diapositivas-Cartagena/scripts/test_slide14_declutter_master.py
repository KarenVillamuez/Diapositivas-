# -*- coding: utf-8 -*-
"""
Generación de 3 variantes maestras para Slide 14:
Solución radical al feedback del usuario:
- "esta sobre cargada de cosas" -> Erradicación de textos secundarios, etiquetas redundantes y notas narrativas.
- "me gustan las barras de porcentajes" -> Barras protagonistas, gruesas (28-32px), números mono colosales (44-48px).
- "mucho espacio muerto" -> Distribución milimétrica en el lienzo (Y=200 a Y=850), sin huecos vacíos dentro de tarjetas ni franjas desiertas.
"""
import os
from playwright.sync_api import sync_playwright

output_dir = r"C:\Users\ASUS\.gemini\antigravity-ide\brain\a6624504-511c-4b9d-bc9a-468e348bde40"
os.makedirs(output_dir, exist_ok=True)

# =============================================================================
# VARIANTE 1: Díptico Vertical Heroico + Franja de Síntesis Inferior (Opción V)
# =============================================================================
HTML_VAR_1 = '''
<section class="slide s-white active" id="slide-14-clean-v">
  <header class="slide-header">
    <div class="sh-left">
      <span class="sh-red-bar"></span>
      <span class="sh-category">03 · RESULTADOS · MODOS DE FALLO ASIMÉTRICOS</span>
    </div>
    <img src="http://localhost:8085/assets/image6.png" alt="#LoxTIC" class="sh-loxtic">
  </header>
  <div class="sh-divider"></div>

  <div class="slide-content-area" style="justify-content: space-between; padding: 16px 0 8px 0; height: calc(100% - 32px);">
    
    <!-- TÍTULO -->
    <h2 class="s-lead-question" style="font-size: 40px; font-weight: 800; margin: 0; line-height: 1.2; color: #2C0509;">
      Alucinación frente a sobre-rechazo: cómo fallan dos modelos con la misma nota
    </h2>

    <!-- DÍPTICO DE COLUMNAS -->
    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 36px; margin: 18px 0 16px 0;">
      
      <!-- MODELO 1: PHI-4-MINI -->
      <div style="background: #FAF5F5; border-top: 8px solid var(--c-wine-primary); padding: 28px 32px; display: flex; flex-direction: column; gap: 26px;">
        <!-- Cabecera de modelo -->
        <div style="display: flex; justify-content: space-between; align-items: baseline; border-bottom: 2px solid #EAE0E1; padding-bottom: 12px;">
          <div>
            <div style="font-family: var(--font-sans); font-size: 38px; font-weight: 800; color: #2C0509; line-height: 1.1;">
              Phi-4-mini <span style="font-size: 24px; font-weight: 600; color: #5D4A4D;">(3.8B)</span>
            </div>
            <div style="font-family: var(--font-mono); font-size: 19px; font-weight: 700; color: var(--c-wine-primary); letter-spacing: 1px; margin-top: 4px;">
              PERFIL PERMISIVO · Q = 0.8030
            </div>
          </div>
          <div style="text-align: right;">
            <span style="font-family: var(--font-sans); font-size: 22px; font-weight: 800; color: var(--c-wine-primary); background: #F0E6E8; padding: 6px 14px;">
              Aula Asistida
            </span>
          </div>
        </div>

        <!-- Métrica 1: Sondas trampa -->
        <div>
          <div style="display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 8px;">
            <span style="font-family: var(--font-sans); font-size: 23px; font-weight: 700; color: #2C0509;">
              Rechazo en 14 sondas trampa:
            </span>
            <span style="font-family: var(--font-mono); font-size: 42px; font-weight: 800; color: var(--c-red-accent); line-height: 1;">
              28.6% <span style="font-size: 22px; font-weight: 700; color: #5D4A4D;">(4/14)</span>
            </span>
          </div>
          <!-- Barra gruesa 30px -->
          <div style="background: #EAE0E1; height: 30px; width: 100%; margin-bottom: 8px;">
            <div style="width: 28.6%; background: var(--c-red-accent); height: 100%;"></div>
          </div>
          <div style="font-family: var(--font-sans); font-size: 21px; color: var(--c-red-accent); font-weight: 700;">
            Alucina en 10 casos fuera del libro escolar.
          </div>
        </div>

        <!-- Métrica 2: Falso rechazo -->
        <div>
          <div style="display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 8px;">
            <span style="font-family: var(--font-sans); font-size: 23px; font-weight: 700; color: #2C0509;">
              Falso rechazo en 84 consultas válidas:
            </span>
            <span style="font-family: var(--font-mono); font-size: 42px; font-weight: 800; color: var(--c-wine-primary); line-height: 1;">
              0.0% <span style="font-size: 22px; font-weight: 700; color: #5D4A4D;">(0/84)</span>
            </span>
          </div>
          <!-- Barra gruesa 30px -->
          <div style="background: #EAE0E1; height: 30px; width: 100%; margin-bottom: 8px;">
            <div style="width: 0%; background: var(--c-wine-primary); height: 100%;"></div>
          </div>
          <div style="font-family: var(--font-sans); font-size: 21px; color: var(--c-wine-primary); font-weight: 700;">
            Fluidez total; jamás bloquea al estudiante.
          </div>
        </div>
      </div>

      <!-- MODELO 2: QWEN2.5-3B -->
      <div style="background: #FAF5F5; border-top: 8px solid var(--c-red-accent); padding: 28px 32px; display: flex; flex-direction: column; gap: 26px;">
        <!-- Cabecera de modelo -->
        <div style="display: flex; justify-content: space-between; align-items: baseline; border-bottom: 2px solid #EAE0E1; padding-bottom: 12px;">
          <div>
            <div style="font-family: var(--font-sans); font-size: 38px; font-weight: 800; color: #2C0509; line-height: 1.1;">
              Qwen2.5-3B <span style="font-size: 24px; font-weight: 600; color: #5D4A4D;">(3.1B)</span>
            </div>
            <div style="font-family: var(--font-mono); font-size: 19px; font-weight: 700; color: var(--c-red-accent); letter-spacing: 1px; margin-top: 4px;">
              PERFIL CONSERVADOR · Q = 0.8010
            </div>
          </div>
          <div style="text-align: right;">
            <span style="font-family: var(--font-sans); font-size: 22px; font-weight: 800; color: var(--c-red-accent); background: #FDE8E9; padding: 6px 14px;">
              Autoestudio
            </span>
          </div>
        </div>

        <!-- Métrica 1: Sondas trampa -->
        <div>
          <div style="display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 8px;">
            <span style="font-family: var(--font-sans); font-size: 23px; font-weight: 700; color: #2C0509;">
              Rechazo en 14 sondas trampa:
            </span>
            <span style="font-family: var(--font-mono); font-size: 42px; font-weight: 800; color: var(--c-wine-primary); line-height: 1;">
              85.7% <span style="font-size: 22px; font-weight: 700; color: #5D4A4D;">(12/14)</span>
            </span>
          </div>
          <!-- Barra gruesa 30px -->
          <div style="background: #EAE0E1; height: 30px; width: 100%; margin-bottom: 8px;">
            <div style="width: 85.7%; background: var(--c-wine-primary); height: 100%;"></div>
          </div>
          <div style="font-family: var(--font-sans); font-size: 21px; color: var(--c-wine-primary); font-weight: 700;">
            Filtro riguroso frente a preguntas trampa.
          </div>
        </div>

        <!-- Métrica 2: Falso rechazo -->
        <div>
          <div style="display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 8px;">
            <span style="font-family: var(--font-sans); font-size: 23px; font-weight: 700; color: #2C0509;">
              Falso rechazo en 84 consultas válidas:
            </span>
            <span style="font-family: var(--font-mono); font-size: 42px; font-weight: 800; color: var(--c-red-accent); line-height: 1;">
              7.1% <span style="font-size: 22px; font-weight: 700; color: #5D4A4D;">(6/84)</span>
            </span>
          </div>
          <!-- Barra gruesa 30px -->
          <div style="background: #EAE0E1; height: 30px; width: 100%; margin-bottom: 8px;">
            <div style="width: 25%; background: var(--c-red-accent); height: 100%;"></div>
          </div>
          <div style="font-family: var(--font-sans); font-size: 21px; color: var(--c-red-accent); font-weight: 700;">
            Sobre-rechazo; bloquea consultas legítimas.
          </div>
        </div>
      </div>

    </div>

    <!-- FRANJA DE SÍNTESIS INFERIOR: Erradica el espacio muerto y cierra el mensaje -->
    <div style="background: #FAF5F5; border: 2px solid var(--c-wine-primary); padding: 16px 28px; display: flex; align-items: center; justify-content: space-between;">
      <div style="display: flex; align-items: center; gap: 16px;">
        <span style="font-family: var(--font-mono); font-size: 20px; font-weight: 800; color: var(--c-wine-primary); letter-spacing: 1.5px;">
          CONCLUSIÓN CLAVE:
        </span>
        <span style="font-family: var(--font-sans); font-size: 23px; font-weight: 700; color: #110103;">
          La misma nota global (0.80) oculta riesgos pedagógicos opuestos según el rol del docente.
        </span>
      </div>
      <div style="font-family: var(--font-mono); font-size: 20px; font-weight: 700; color: #5D4A4D;">
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
# VARIANTE 2: Panorámica de 2 Filas Horizontales con Llenado Armónico (Opción H)
# =============================================================================
HTML_VAR_2 = '''
<section class="slide s-white active" id="slide-14-clean-h">
  <header class="slide-header">
    <div class="sh-left">
      <span class="sh-red-bar"></span>
      <span class="sh-category">03 · RESULTADOS · MODOS DE FALLO ASIMÉTRICOS</span>
    </div>
    <img src="http://localhost:8085/assets/image6.png" alt="#LoxTIC" class="sh-loxtic">
  </header>
  <div class="sh-divider"></div>

  <div class="slide-content-area" style="justify-content: space-between; padding: 18px 0 10px 0; height: calc(100% - 36px);">
    
    <!-- TÍTULO -->
    <h2 class="s-lead-question" style="font-size: 40px; font-weight: 800; margin: 0; line-height: 1.2; color: #2C0509;">
      Alucinación frente a sobre-rechazo: cómo fallan dos modelos con la misma nota
    </h2>

    <!-- FILA 1: PHI-4-MINI (HORIZONTAL EXPANDIDO) -->
    <div style="background: #FAF5F5; border-left: 10px solid var(--c-wine-primary); padding: 28px 36px; display: grid; grid-template-columns: 420px 1fr 1fr; gap: 48px; align-items: center;">
      <!-- Identidad y Rol -->
      <div style="border-right: 2px solid #EAE0E1; padding-right: 32px;">
        <div style="font-family: var(--font-mono); font-size: 19px; font-weight: 700; color: var(--c-wine-primary); letter-spacing: 1.5px; margin-bottom: 4px;">
          PERFIL PERMISIVO · Q = 0.8030
        </div>
        <div style="font-family: var(--font-sans); font-size: 42px; font-weight: 800; color: #2C0509; line-height: 1.1; margin-bottom: 8px;">
          Phi-4-mini <span style="font-size: 26px; font-weight: 600; color: #5D4A4D;">3.8B</span>
        </div>
        <div style="font-family: var(--font-sans); font-size: 23px; font-weight: 700; color: #110103;">
          <strong style="color: var(--c-wine-primary);">Aula asistida:</strong> con docente que guía.
        </div>
      </div>

      <!-- Barra 1: Sondas trampa -->
      <div>
        <div style="display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 8px;">
          <span style="font-family: var(--font-sans); font-size: 23px; font-weight: 700; color: #2C0509;">Rechazo en trampas (14):</span>
          <span style="font-family: var(--font-mono); font-size: 42px; font-weight: 800; color: var(--c-red-accent); line-height: 1;">28.6%</span>
        </div>
        <div style="background: #EAE0E1; height: 28px; width: 100%; margin-bottom: 8px;">
          <div style="width: 28.6%; background: var(--c-red-accent); height: 100%;"></div>
        </div>
        <div style="font-family: var(--font-sans); font-size: 21px; color: var(--c-red-accent); font-weight: 700;">
          Alucina en 10 casos fuera de libro.
        </div>
      </div>

      <!-- Barra 2: Consultas válidas -->
      <div>
        <div style="display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 8px;">
          <span style="font-family: var(--font-sans); font-size: 23px; font-weight: 700; color: #2C0509;">Falso rechazo (84 válidas):</span>
          <span style="font-family: var(--font-mono); font-size: 42px; font-weight: 800; color: var(--c-wine-primary); line-height: 1;">0.0%</span>
        </div>
        <div style="background: #EAE0E1; height: 28px; width: 100%; margin-bottom: 8px;">
          <div style="width: 0%; background: var(--c-wine-primary); height: 100%;"></div>
        </div>
        <div style="font-family: var(--font-sans); font-size: 21px; color: var(--c-wine-primary); font-weight: 700;">
          Fluidez total; jamás frena al alumno.
        </div>
      </div>
    </div>

    <!-- FILA 2: QWEN2.5-3B (HORIZONTAL EXPANDIDO) -->
    <div style="background: #FAF5F5; border-left: 10px solid var(--c-red-accent); padding: 28px 36px; display: grid; grid-template-columns: 420px 1fr 1fr; gap: 48px; align-items: center;">
      <!-- Identidad y Rol -->
      <div style="border-right: 2px solid #EAE0E1; padding-right: 32px;">
        <div style="font-family: var(--font-mono); font-size: 19px; font-weight: 700; color: var(--c-red-accent); letter-spacing: 1.5px; margin-bottom: 4px;">
          PERFIL CONSERVADOR · Q = 0.8010
        </div>
        <div style="font-family: var(--font-sans); font-size: 42px; font-weight: 800; color: #2C0509; line-height: 1.1; margin-bottom: 8px;">
          Qwen2.5-3B <span style="font-size: 26px; font-weight: 600; color: #5D4A4D;">3.1B</span>
        </div>
        <div style="font-family: var(--font-sans); font-size: 23px; font-weight: 700; color: #110103;">
          <strong style="color: var(--c-red-accent);">Autoestudio:</strong> sin profesor presente.
        </div>
      </div>

      <!-- Barra 1: Sondas trampa -->
      <div>
        <div style="display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 8px;">
          <span style="font-family: var(--font-sans); font-size: 23px; font-weight: 700; color: #2C0509;">Rechazo en trampas (14):</span>
          <span style="font-family: var(--font-mono); font-size: 42px; font-weight: 800; color: var(--c-wine-primary); line-height: 1;">85.7%</span>
        </div>
        <div style="background: #EAE0E1; height: 28px; width: 100%; margin-bottom: 8px;">
          <div style="width: 85.7%; background: var(--c-wine-primary); height: 100%;"></div>
        </div>
        <div style="font-family: var(--font-sans); font-size: 21px; color: var(--c-wine-primary); font-weight: 700;">
          Filtro riguroso frente a trampas.
        </div>
      </div>

      <!-- Barra 2: Consultas válidas -->
      <div>
        <div style="display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 8px;">
          <span style="font-family: var(--font-sans); font-size: 23px; font-weight: 700; color: #2C0509;">Falso rechazo (84 válidas):</span>
          <span style="font-family: var(--font-mono); font-size: 42px; font-weight: 800; color: var(--c-red-accent); line-height: 1;">7.1%</span>
        </div>
        <div style="background: #EAE0E1; height: 28px; width: 100%; margin-bottom: 8px;">
          <div style="width: 25%; background: var(--c-red-accent); height: 100%;"></div>
        </div>
        <div style="font-family: var(--font-sans); font-size: 21px; color: var(--c-red-accent); font-weight: 700;">
          Sobre-rechazo por cautela extrema.
        </div>
      </div>
    </div>

    <!-- LÍNEA SUTIL DE FUENTE -->
    <div style="display: flex; justify-content: space-between; font-family: var(--font-mono); font-size: 20px; color: #5D4A4D; padding: 0 4px;">
      <span>Tabla 3 del paper: Evaluación sobre 14 preguntas curriculares y 2 sondas fuera de dominio (×4 semillas).</span>
      <span style="font-weight: 700; color: var(--c-wine-primary);">LHXT26 EXPERIMENTAL</span>
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
# VARIANTE 3: Cara a Cara por Prueba (Barras Apiladas Directamente) (Opción C)
# =============================================================================
HTML_VAR_3 = '''
<section class="slide s-white active" id="slide-14-clean-c">
  <header class="slide-header">
    <div class="sh-left">
      <span class="sh-red-bar"></span>
      <span class="sh-category">03 · RESULTADOS · MODOS DE FALLO ASIMÉTRICOS</span>
    </div>
    <img src="http://localhost:8085/assets/image6.png" alt="#LoxTIC" class="sh-loxtic">
  </header>
  <div class="sh-divider"></div>

  <div class="slide-content-area" style="justify-content: space-between; padding: 16px 0 8px 0; height: calc(100% - 32px);">
    
    <!-- TÍTULO -->
    <h2 class="s-lead-question" style="font-size: 40px; font-weight: 800; margin: 0; line-height: 1.2; color: #2C0509;">
      Alucinación frente a sobre-rechazo: cómo fallan dos modelos con la misma nota
    </h2>

    <!-- DOS COLUMNAS POR PRUEBA: Permite ver las barras una debajo de otra -->
    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 36px; margin: 18px 0 16px 0;">
      
      <!-- COLUMNA 1: SONDAS TRAMPA (RECHAZO CERTERO) -->
      <div style="background: #FAF5F5; border-top: 8px solid var(--c-wine-primary); padding: 28px 32px; display: flex; flex-direction: column; gap: 24px;">
        <div>
          <div style="font-family: var(--font-mono); font-size: 19px; font-weight: 800; color: var(--c-wine-primary); letter-spacing: 1px; margin-bottom: 4px;">
            PRUEBA 1 · 14 SONDAS TRAMPA
          </div>
          <div style="font-family: var(--font-sans); font-size: 34px; font-weight: 800; color: #2C0509;">
            Rechazo Certero <span style="font-size: 22px; font-weight: 600; color: #5D4A4D;">(Preguntas fuera de libro)</span>
          </div>
        </div>

        <!-- Barra Phi-4 -->
        <div>
          <div style="display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 6px;">
            <span style="font-family: var(--font-sans); font-size: 24px; font-weight: 800; color: #2C0509;">
              Phi-4-mini (3.8B)
            </span>
            <span style="font-family: var(--font-mono); font-size: 38px; font-weight: 800; color: var(--c-red-accent); line-height: 1;">
              28.6% <span style="font-size: 20px; font-weight: 700; color: #5D4A4D;">(4/14)</span>
            </span>
          </div>
          <div style="background: #EAE0E1; height: 28px; width: 100%; margin-bottom: 6px;">
            <div style="width: 28.6%; background: var(--c-red-accent); height: 100%;"></div>
          </div>
          <div style="font-family: var(--font-sans); font-size: 21px; color: var(--c-red-accent); font-weight: 700;">
            Alucina en 10 casos; inventa datos con alta fluidez.
          </div>
        </div>

        <!-- Barra Qwen2.5 -->
        <div>
          <div style="display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 6px;">
            <span style="font-family: var(--font-sans); font-size: 24px; font-weight: 800; color: #2C0509;">
              Qwen2.5-3B (3.1B)
            </span>
            <span style="font-family: var(--font-mono); font-size: 38px; font-weight: 800; color: var(--c-wine-primary); line-height: 1;">
              85.7% <span style="font-size: 20px; font-weight: 700; color: #5D4A4D;">(12/14)</span>
            </span>
          </div>
          <div style="background: #EAE0E1; height: 28px; width: 100%; margin-bottom: 6px;">
            <div style="width: 85.7%; background: var(--c-wine-primary); height: 100%;"></div>
          </div>
          <div style="font-family: var(--font-sans); font-size: 21px; color: var(--c-wine-primary); font-weight: 700;">
            Filtro riguroso; frena el 85.7% de trampas.
          </div>
        </div>
      </div>

      <!-- COLUMNA 2: CONSULTAS CURRICULARES (FALSO RECHAZO) -->
      <div style="background: #FAF5F5; border-top: 8px solid var(--c-red-accent); padding: 28px 32px; display: flex; flex-direction: column; gap: 24px;">
        <div>
          <div style="font-family: var(--font-mono); font-size: 19px; font-weight: 800; color: var(--c-red-accent); letter-spacing: 1px; margin-bottom: 4px;">
            PRUEBA 2 · 84 CONSULTAS VÁLIDAS
          </div>
          <div style="font-family: var(--font-sans); font-size: 34px; font-weight: 800; color: #2C0509;">
            Falso Rechazo <span style="font-size: 22px; font-weight: 600; color: #5D4A4D;">(Preguntas curriculares legítimas)</span>
          </div>
        </div>

        <!-- Barra Phi-4 -->
        <div>
          <div style="display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 6px;">
            <span style="font-family: var(--font-sans); font-size: 24px; font-weight: 800; color: #2C0509;">
              Phi-4-mini (3.8B)
            </span>
            <span style="font-family: var(--font-mono); font-size: 38px; font-weight: 800; color: var(--c-wine-primary); line-height: 1;">
              0.0% <span style="font-size: 20px; font-weight: 700; color: #5D4A4D;">(0/84)</span>
            </span>
          </div>
          <div style="background: #EAE0E1; height: 28px; width: 100%; margin-bottom: 6px;">
            <div style="width: 0%; background: var(--c-wine-primary); height: 100%;"></div>
          </div>
          <div style="font-family: var(--font-sans); font-size: 21px; color: var(--c-wine-primary); font-weight: 700;">
            Fluidez total; jamás bloquea una duda válida.
          </div>
        </div>

        <!-- Barra Qwen2.5 -->
        <div>
          <div style="display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 6px;">
            <span style="font-family: var(--font-sans); font-size: 24px; font-weight: 800; color: #2C0509;">
              Qwen2.5-3B (3.1B)
            </span>
            <span style="font-family: var(--font-mono); font-size: 38px; font-weight: 800; color: var(--c-red-accent); line-height: 1;">
              7.1% <span style="font-size: 20px; font-weight: 700; color: #5D4A4D;">(6/84)</span>
            </span>
          </div>
          <div style="background: #EAE0E1; height: 28px; width: 100%; margin-bottom: 6px;">
            <div style="width: 25%; background: var(--c-red-accent); height: 100%;"></div>
          </div>
          <div style="font-family: var(--font-sans); font-size: 21px; color: var(--c-red-accent); font-weight: 700;">
            Sobre-rechazo; bloquea a 6 alumnos con dudas legítimas.
          </div>
        </div>
      </div>

    </div>

    <!-- FRANJA DE SÍNTESIS INFERIOR -->
    <div style="background: #FAF5F5; border: 2px solid var(--c-wine-primary); padding: 16px 28px; display: flex; align-items: center; justify-content: space-between;">
      <div style="display: flex; align-items: center; gap: 16px;">
        <span style="font-family: var(--font-mono); font-size: 20px; font-weight: 800; color: var(--c-wine-primary); letter-spacing: 1.5px;">
          CONCLUSIÓN:
        </span>
        <span style="font-family: var(--font-sans); font-size: 23px; font-weight: 700; color: #110103;">
          Phi-4 prioriza fluidez (ideal con docente); Qwen prioriza seguridad (ideal en autoestudio).
        </span>
      </div>
      <div style="font-family: var(--font-mono); font-size: 20px; font-weight: 700; color: #5D4A4D;">
        Tabla 3
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
  <title>Slide 14 Declutter Master</title>
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
        ('slide_14_clean_v.html', 'slide_14_clean_v.png', HTML_VAR_1),
        ('slide_14_clean_h.html', 'slide_14_clean_h.png', HTML_VAR_2),
        ('slide_14_clean_c.html', 'slide_14_clean_c.png', HTML_VAR_3),
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
