# -*- coding: utf-8 -*-
"""
Exploración de opciones de diseño para Slide 14: Modos de Fallo Asimétricos (Tabla 3 del paper).

Opción A: Comparativa Directa Modelo a Modelo (2 Columnas Hero: Phi-4-mini vs Qwen2.5-3B con datos de Tabla 3 integrados)
Opción B: Tabla 3 Estilizada y Balanceada (Izquierda 50%) + 2 Perfiles Pedagógicos (Derecha 50%)
Opción C: Tabla Comparativa Superior Ancha + 2 Veredictos Pedagógicos Inferiores (Estructura Hero Arriba + Base)
"""
import os
from playwright.sync_api import sync_playwright

output_dir = r"C:\Users\ASUS\.gemini\antigravity-ide\brain\a6624504-511c-4b9d-bc9a-468e348bde40"
os.makedirs(output_dir, exist_ok=True)

# -----------------------------------------------------------------------------
# OPCION A: Comparativa Directa Modelo a Modelo (2 Columnas Hero)
# -----------------------------------------------------------------------------
HTML_VAR_A = '''
<section class="slide s-white active" id="slide-14-var-a">
  <header class="slide-header">
    <div class="sh-left">
      <span class="sh-red-bar"></span>
      <span class="sh-category">03 · RESULTADOS · MODOS DE FALLO ASIMÉTRICOS</span>
    </div>
    <img src="http://localhost:8085/assets/image6.png" alt="#LoxTIC" class="sh-loxtic">
  </header>
  <div class="sh-divider"></div>

  <div class="slide-content-area" style="justify-content: space-between; padding: 14px 0 6px 0;">
    
    <h2 class="s-lead-question" style="font-size: 38px; font-weight: 800; margin: 0; line-height: 1.2;">
      Alucinación frente a Sobre-rechazo: cómo fallan dos modelos con la misma nota
    </h2>

    <!-- DOS COLUMNAS HERO: COMPARATIVA DIRECTA DE MODELOS -->
    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 32px; flex: 1; align-items: stretch; margin: 16px 0;">
      
      <!-- COLUMNA 1: PHI-4-MINI (PERFIL PERMISIVO) -->
      <div style="background: #FAF5F5; border: 2.5px solid var(--c-wine-primary); padding: 22px 26px; display: flex; flex-direction: column; justify-content: space-between;">
        <div>
          <!-- Cabecera de Modelo -->
          <div style="display: flex; justify-content: space-between; align-items: baseline; border-bottom: 2px solid rgba(70, 8, 17, 0.15); padding-bottom: 12px; margin-bottom: 16px;">
            <div>
              <span style="font-family: var(--font-mono); font-size: 19px; font-weight: 800; color: var(--c-wine-primary); letter-spacing: 1px;">
                PERFIL PERMISIVO
              </span>
              <div style="font-family: var(--font-sans); font-size: 32px; font-weight: 800; color: #110103; margin-top: 2px;">
                Phi-4-mini (3.8B)
              </div>
            </div>
            <div style="text-align: right;">
              <span style="font-family: var(--font-mono); font-size: 28px; font-weight: 800; color: var(--c-wine-primary);">
                Nota: 0.8030
              </span>
            </div>
          </div>

          <!-- Dos Métricas Clave de la Tabla 3 -->
          <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 16px; margin-bottom: 18px;">
            <div style="background: #FFFFFF; border-left: 5px solid #C9101B; padding: 12px 14px;">
              <div style="font-family: var(--font-mono); font-size: 32px; font-weight: 800; color: #C9101B; line-height: 1;">
                28.6%
              </div>
              <div style="font-family: var(--font-sans); font-size: 19px; font-weight: 800; color: #110103; margin-top: 4px;">
                Rechazo Certero (4/14)
              </div>
              <div style="font-family: var(--font-sans); font-size: 18px; color: #5D4A4D; margin-top: 2px;">
                Alucina en 10 sondas fuera de libro
              </div>
            </div>

            <div style="background: #FFFFFF; border-left: 5px solid #2E7D32; padding: 12px 14px;">
              <div style="font-family: var(--font-mono); font-size: 32px; font-weight: 800; color: #2E7D32; line-height: 1;">
                0.0%
              </div>
              <div style="font-family: var(--font-sans); font-size: 19px; font-weight: 800; color: #110103; margin-top: 4px;">
                Falsos Rechazos (0/84)
              </div>
              <div style="font-family: var(--font-sans); font-size: 18px; color: #5D4A4D; margin-top: 2px;">
                Jamás bloquea preguntas legítimas
              </div>
            </div>
          </div>

          <!-- Diagnóstico de Comportamiento -->
          <p style="font-family: var(--font-sans); font-size: 22px; color: #110103; font-weight: 600; line-height: 1.4; margin: 0 0 12px 0;">
            Prioriza responder siempre: ofrece <strong>fluidez conversacional total</strong>, pero inventa respuestas ante temas no vistos en el libro escolar.
          </p>
        </div>

        <!-- Veredicto de Uso Pedagógico -->
        <div style="background: #FFFFFF; border: 1.5px solid var(--c-wine-primary); padding: 12px 18px; display: flex; align-items: center; gap: 14px;">
          <span style="font-size: 26px;">👨‍🏫</span>
          <div>
            <div style="font-family: var(--font-sans); font-size: 18px; font-weight: 800; color: var(--c-wine-primary); letter-spacing: 0.5px;">
              RECOMENDACIÓN EN EL AULA
            </div>
            <div style="font-family: var(--font-sans); font-size: 21px; font-weight: 700; color: #110103;">
              Clase guiada con docente activo que modere y corrija.
            </div>
          </div>
        </div>
      </div>

      <!-- COLUMNA 2: QWEN2.5-3B (PERFIL CONSERVADOR) -->
      <div style="background: #FAF5F5; border: 2.5px solid var(--c-red-accent); padding: 22px 26px; display: flex; flex-direction: column; justify-content: space-between;">
        <div>
          <!-- Cabecera de Modelo -->
          <div style="display: flex; justify-content: space-between; align-items: baseline; border-bottom: 2px solid rgba(201, 16, 27, 0.15); padding-bottom: 12px; margin-bottom: 16px;">
            <div>
              <span style="font-family: var(--font-mono); font-size: 19px; font-weight: 800; color: var(--c-red-accent); letter-spacing: 1px;">
                PERFIL CONSERVADOR
              </span>
              <div style="font-family: var(--font-sans); font-size: 32px; font-weight: 800; color: #110103; margin-top: 2px;">
                Qwen2.5-3B (3.1B)
              </div>
            </div>
            <div style="text-align: right;">
              <span style="font-family: var(--font-mono); font-size: 28px; font-weight: 800; color: var(--c-red-accent);">
                Nota: 0.8010
              </span>
            </div>
          </div>

          <!-- Dos Métricas Clave de la Tabla 3 -->
          <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 16px; margin-bottom: 18px;">
            <div style="background: #FFFFFF; border-left: 5px solid #2E7D32; padding: 12px 14px;">
              <div style="font-family: var(--font-mono); font-size: 32px; font-weight: 800; color: #2E7D32; line-height: 1;">
                85.7%
              </div>
              <div style="font-family: var(--font-sans); font-size: 19px; font-weight: 800; color: #110103; margin-top: 4px;">
                Rechazo Certero (12/14)
              </div>
              <div style="font-family: var(--font-sans); font-size: 18px; color: #5D4A4D; margin-top: 2px;">
                Filtra con éxito sondas trampa
              </div>
            </div>

            <div style="background: #FFFFFF; border-left: 5px solid #C9101B; padding: 12px 14px;">
              <div style="font-family: var(--font-mono); font-size: 32px; font-weight: 800; color: #C9101B; line-height: 1;">
                7.1%
              </div>
              <div style="font-family: var(--font-sans); font-size: 19px; font-weight: 800; color: #110103; margin-top: 4px;">
                Falsos Rechazos (6/84)
              </div>
              <div style="font-family: var(--font-sans); font-size: 18px; color: #5D4A4D; margin-top: 2px;">
                Bloquea preguntas válidas por cautela
              </div>
            </div>
          </div>

          <!-- Diagnóstico de Comportamiento -->
          <p style="font-family: var(--font-sans); font-size: 22px; color: #110103; font-weight: 600; line-height: 1.4; margin: 0 0 12px 0;">
            Prioriza seguridad y rigor: <strong>bloquea con precisión</strong> lo que no conoce, pero a costa de frenar al alumno en preguntas válidas.
          </p>
        </div>

        <!-- Veredicto de Uso Pedagógico -->
        <div style="background: #FFFFFF; border: 1.5px solid var(--c-red-accent); padding: 12px 18px; display: flex; align-items: center; gap: 14px;">
          <span style="font-size: 26px;">📖</span>
          <div>
            <div style="font-family: var(--font-sans); font-size: 18px; font-weight: 800; color: var(--c-red-accent); letter-spacing: 0.5px;">
              RECOMENDACIÓN EN EL AULA
            </div>
            <div style="font-family: var(--font-sans); font-size: 21px; font-weight: 700; color: #110103;">
              Autoestudio solitario donde prima no enseñar errores.
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

# -----------------------------------------------------------------------------
# OPCION B: Tabla 3 Estilizada (50%) + Dos Perfiles (50%)
# -----------------------------------------------------------------------------
HTML_VAR_B = '''
<section class="slide s-white active" id="slide-14-var-b">
  <header class="slide-header">
    <div class="sh-left">
      <span class="sh-red-bar"></span>
      <span class="sh-category">03 · RESULTADOS · MODOS DE FALLO ASIMÉTRICOS</span>
    </div>
    <img src="http://localhost:8085/assets/image6.png" alt="#LoxTIC" class="sh-loxtic">
  </header>
  <div class="sh-divider"></div>

  <div class="slide-content-area" style="justify-content: space-between; padding: 14px 0 6px 0;">
    
    <h2 class="s-lead-question" style="font-size: 38px; font-weight: 800; margin: 0; line-height: 1.2;">
      Alucinación frente a Sobre-rechazo: cómo fallan dos modelos con la misma nota
    </h2>

    <div style="display: grid; grid-template-columns: 1.15fr 1fr; gap: 32px; flex: 1; align-items: stretch; margin: 16px 0;">
      
      <!-- IZQUIERDA: TABLA 3 FORMAL Y ROBUSTA -->
      <div style="background: #FAF5F5; border: 2.5px solid var(--c-wine-primary); padding: 22px 24px; display: flex; flex-direction: column; justify-content: space-between;">
        <div>
          <div style="display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 14px;">
            <span style="font-family: var(--font-sans); font-size: 24px; font-weight: 800; color: var(--c-wine-dark);">
              TABLA 3: AUDITORÍA DE FALLAS
            </span>
            <span style="font-family: var(--font-mono); font-size: 19px; font-weight: 700; color: #555;">
              14 SONDAS · 84 CURRICULARES
            </span>
          </div>

          <table style="width: 100%; border-collapse: collapse; font-family: var(--font-sans); text-align: center;">
            <thead>
              <tr style="background: var(--c-wine-primary); color: #FFFFFF;">
                <th style="padding: 14px 16px; font-family: var(--font-mono); font-size: 19px; font-weight: 700; text-align: left;">MODELO</th>
                <th style="padding: 14px 14px; font-family: var(--font-mono); font-size: 19px; font-weight: 700;">RECHAZO CERTERO<br><span style="font-size: 15px; font-weight: 400; opacity: 0.9;">Sondas fuera de libro</span></th>
                <th style="padding: 14px 14px; font-family: var(--font-mono); font-size: 19px; font-weight: 700;">FALSO RECHAZO<br><span style="font-size: 15px; font-weight: 400; opacity: 0.9;">Consultas válidas</span></th>
              </tr>
            </thead>
            <tbody>
              <!-- Phi-4-mini -->
              <tr style="background: #FFFFFF; border-bottom: 2px solid #E2D6D8;">
                <td style="padding: 20px 16px; font-size: 23px; font-weight: 800; color: #110103; text-align: left;">
                  Phi-4-mini<br><span style="font-size: 18px; font-family: var(--font-mono); color: #666; font-weight: 600;">(3.8B)</span>
                </td>
                <td style="padding: 20px 14px;">
                  <div style="font-family: var(--font-mono); font-size: 28px; font-weight: 800; color: #C9101B;">28.6%</div>
                  <div style="font-size: 18px; color: #C9101B; font-weight: 700;">4 / 14 (Alucina)</div>
                </td>
                <td style="padding: 20px 14px;">
                  <div style="font-family: var(--font-mono); font-size: 28px; font-weight: 800; color: #2E7D32;">0.0%</div>
                  <div style="font-size: 18px; color: #2E7D32; font-weight: 700;">0 / 84 (Fluido)</div>
                </td>
              </tr>
              <!-- Qwen2.5-3B -->
              <tr style="background: #FAF5F5;">
                <td style="padding: 20px 16px; font-size: 23px; font-weight: 800; color: #110103; text-align: left;">
                  Qwen2.5-3B<br><span style="font-size: 18px; font-family: var(--font-mono); color: #666; font-weight: 600;">(3.1B)</span>
                </td>
                <td style="padding: 20px 14px;">
                  <div style="font-family: var(--font-mono); font-size: 28px; font-weight: 800; color: #2E7D32;">85.7%</div>
                  <div style="font-size: 18px; color: #2E7D32; font-weight: 700;">12 / 14 (Seguro)</div>
                </td>
                <td style="padding: 20px 14px;">
                  <div style="font-family: var(--font-mono); font-size: 28px; font-weight: 800; color: #C9101B;">7.1%</div>
                  <div style="font-size: 18px; color: #C9101B; font-weight: 700;">6 / 84 (Bloquea)</div>
                </td>
              </tr>
            </tbody>
          </table>
        </div>

        <div style="border-top: 1.5px solid #E2D6D8; padding-top: 12px; font-family: var(--font-sans); font-size: 21px; color: #110103; font-weight: 600;">
          Ambos empatan en <strong>0.795 ~ 0.803</strong>, pero sus naturalezas de error son <strong>completamente opuestas</strong>.
        </div>
      </div>

      <!-- DERECHA: DOS BLOQUES DE PERFIL PEDAGÓGICO -->
      <div style="display: flex; flex-direction: column; gap: 20px; justify-content: space-between;">
        
        <!-- Bloque 1: Phi-4-mini -->
        <div style="background: #FAF5F5; border-left: 7px solid var(--c-wine-primary); border-top: 1px solid #E2D6D8; border-right: 1px solid #E2D6D8; border-bottom: 1px solid #E2D6D8; padding: 18px 22px; flex: 1; display: flex; flex-direction: column; justify-content: center;">
          <div style="display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 4px;">
            <span style="font-family: var(--font-sans); font-size: 24px; font-weight: 800; color: var(--c-wine-dark);">
              Phi-4-mini · Perfil Permisivo
            </span>
            <span style="font-family: var(--font-mono); font-size: 18px; font-weight: 800; color: var(--c-wine-primary);">
              FLUIDEZ TOTAL
            </span>
          </div>
          <div style="font-family: var(--font-sans); font-size: 21px; color: #110103; font-weight: 600; line-height: 1.35; margin-bottom: 8px;">
            Jamás interrumpe al alumno, pero inventa hechos cuando el libro no contiene la respuesta (10 alucinaciones).
          </div>
          <div style="font-family: var(--font-sans); font-size: 19px; color: var(--c-wine-primary); font-weight: 800;">
            👉 Ideal para: Aula guiada con docente presente para supervisar.
          </div>
        </div>

        <!-- Bloque 2: Qwen2.5-3B -->
        <div style="background: #FAF5F5; border-left: 7px solid var(--c-red-accent); border-top: 1px solid #E2D6D8; border-right: 1px solid #E2D6D8; border-bottom: 1px solid #E2D6D8; padding: 18px 22px; flex: 1; display: flex; flex-direction: column; justify-content: center;">
          <div style="display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 4px;">
            <span style="font-family: var(--font-sans); font-size: 24px; font-weight: 800; color: var(--c-wine-dark);">
              Qwen2.5-3B · Perfil Conservador
            </span>
            <span style="font-family: var(--font-mono); font-size: 18px; font-weight: 800; color: var(--c-red-accent);">
              SEGURIDAD ESTRICTA
            </span>
          </div>
          <div style="font-family: var(--font-sans); font-size: 21px; color: #110103; font-weight: 600; line-height: 1.35; margin-bottom: 8px;">
            Bloquea con rigor preguntas fuera de contexto (85.7%), pero descarta consultas válidas (7.1% falso rechazo).
          </div>
          <div style="font-family: var(--font-sans); font-size: 19px; color: var(--c-red-accent); font-weight: 800;">
            👉 Ideal para: Autoestudio individual donde prima la certeza factual.
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
# OPCION C: Tabla Hero Ancha Arriba + 2 Tarjetas Pedagógicas Abajo (Armonía 12 y 13)
# -----------------------------------------------------------------------------
HTML_VAR_C = '''
<section class="slide s-white active" id="slide-14-var-c">
  <header class="slide-header">
    <div class="sh-left">
      <span class="sh-red-bar"></span>
      <span class="sh-category">03 · RESULTADOS · MODOS DE FALLO ASIMÉTRICOS</span>
    </div>
    <img src="http://localhost:8085/assets/image6.png" alt="#LoxTIC" class="sh-loxtic">
  </header>
  <div class="sh-divider"></div>

  <div class="slide-content-area" style="justify-content: space-between; padding: 14px 0 6px 0;">
    
    <h2 class="s-lead-question" style="font-size: 38px; font-weight: 800; margin: 0; line-height: 1.2;">
      Alucinación frente a Sobre-rechazo: cómo fallan dos modelos con la misma nota
    </h2>

    <!-- HERO SUPERIOR: TABLA 3 EXTENDIDA -->
    <div style="background: #FAF5F5; border: 2.5px solid var(--c-wine-primary); padding: 18px 24px;">
      <div style="display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 12px;">
        <span style="font-family: var(--font-sans); font-size: 24px; font-weight: 800; color: var(--c-wine-dark);">
          TABLA 3 DEL PAPER: FALLAS EN SONDAS FUERA DE DOMINIO Y PREGUNTAS CURRICULARES
        </span>
        <span style="font-family: var(--font-mono); font-size: 19px; font-weight: 700; color: #555;">
          784 INFERENCIAS AUDITADAS
        </span>
      </div>

      <table style="width: 100%; border-collapse: collapse; font-family: var(--font-sans); text-align: center;">
        <thead>
          <tr style="background: var(--c-wine-primary); color: #FFFFFF;">
            <th style="padding: 12px 18px; font-family: var(--font-mono); font-size: 19px; font-weight: 700; text-align: left; width: 25%;">MODELO SLM</th>
            <th style="padding: 12px 18px; font-family: var(--font-mono); font-size: 19px; font-weight: 700; width: 25%;">RECHAZO CERTERO (F1/F2)<br><span style="font-size: 15px; font-weight: 400; opacity: 0.9;">14 sondas fuera de libro</span></th>
            <th style="padding: 12px 18px; font-family: var(--font-mono); font-size: 19px; font-weight: 700; width: 25%;">FALSO RECHAZO (VÁLIDAS)<br><span style="font-size: 15px; font-weight: 400; opacity: 0.9;">84 preguntas curriculares</span></th>
            <th style="padding: 12px 18px; font-family: var(--font-mono); font-size: 19px; font-weight: 700; width: 25%;">PERFIL RESULTANTE</th>
          </tr>
        </thead>
        <tbody>
          <!-- Phi-4-mini -->
          <tr style="background: #FFFFFF; border-bottom: 2px solid #E2D6D8;">
            <td style="padding: 16px 18px; font-size: 24px; font-weight: 800; color: #110103; text-align: left;">
              Phi-4-mini <span style="font-size: 18px; font-family: var(--font-mono); color: #666; font-weight: 600;">(3.8B)</span>
            </td>
            <td style="padding: 16px 18px;">
              <span style="font-family: var(--font-mono); font-size: 28px; font-weight: 800; color: #C9101B;">28.6%</span>
              <span style="font-size: 18px; color: #C9101B; font-weight: 700; display: block;">4/14 (Alucina 10 veces)</span>
            </td>
            <td style="padding: 16px 18px;">
              <span style="font-family: var(--font-mono); font-size: 28px; font-weight: 800; color: #2E7D32;">0.0%</span>
              <span style="font-size: 18px; color: #2E7D32; font-weight: 700; display: block;">0/84 (Fluidez total)</span>
            </td>
            <td style="padding: 16px 18px; font-size: 22px; font-weight: 800; color: var(--c-wine-primary);">
              Permisivo / Conversacional
            </td>
          </tr>
          <!-- Qwen2.5-3B -->
          <tr style="background: #FAF5F5;">
            <td style="padding: 16px 18px; font-size: 24px; font-weight: 800; color: #110103; text-align: left;">
              Qwen2.5-3B <span style="font-size: 18px; font-family: var(--font-mono); color: #666; font-weight: 600;">(3.1B)</span>
            </td>
            <td style="padding: 16px 18px;">
              <span style="font-family: var(--font-mono); font-size: 28px; font-weight: 800; color: #2E7D32;">85.7%</span>
              <span style="font-size: 18px; color: #2E7D32; font-weight: 700; display: block;">12/14 (Alta seguridad)</span>
            </td>
            <td style="padding: 16px 18px;">
              <span style="font-family: var(--font-mono); font-size: 28px; font-weight: 800; color: #C9101B;">7.1%</span>
              <span style="font-size: 18px; color: #C9101B; font-weight: 700; display: block;">6/84 (Sobre-rechazo)</span>
            </td>
            <td style="padding: 16px 18px; font-size: 22px; font-weight: 800; color: var(--c-red-accent);">
              Conservador / Estricto
            </td>
          </tr>
        </tbody>
      </table>
    </div>

    <!-- BASE: DOS VEREDICTOS PEDAGÓGICOS (ESTILO NATIVO PLANTILLA) -->
    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 40px; padding: 6px 10px;">
      
      <!-- Veredicto 1 -->
      <div style="display: flex; gap: 20px; align-items: center;">
        <div style="width: 7px; height: 80px; background-color: var(--c-wine-primary); flex-shrink: 0;"></div>
        <div>
          <div style="font-family: var(--font-sans); font-size: 24px; font-weight: 800; color: var(--c-wine-dark);">
            👨‍🏫 Aula Asistida: Phi-4-mini
          </div>
          <div style="font-family: var(--font-sans); font-size: 21px; color: #110103; font-weight: 600; line-height: 1.35; margin-top: 4px;">
            El docente modera la interacción y corrige alucinaciones, aprovechando la fluidez sin bloqueos falsos.
          </div>
        </div>
      </div>

      <!-- Veredicto 2 -->
      <div style="display: flex; gap: 20px; align-items: center;">
        <div style="width: 7px; height: 80px; background-color: var(--c-red-accent); flex-shrink: 0;"></div>
        <div>
          <div style="font-family: var(--font-sans); font-size: 24px; font-weight: 800; color: var(--c-wine-dark);">
            📖 Autoestudio: Qwen2.5-3B
          </div>
          <div style="font-family: var(--font-sans); font-size: 21px; color: #110103; font-weight: 600; line-height: 1.35; margin-top: 4px;">
            Sin profesor presente, prima no inducir al error al estudiante, asumiendo el costo del sobre-rechazo.
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
  <title>Test Slide 14 Variants</title>
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
        ('slide_14_var_a.html', 'slide_14_var_a.png', HTML_VAR_A),
        ('slide_14_var_b.html', 'slide_14_var_b.png', HTML_VAR_B),
        ('slide_14_var_c.html', 'slide_14_var_c.png', HTML_VAR_C),
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
