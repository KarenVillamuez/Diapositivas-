# -*- coding: utf-8 -*-
import os
from playwright.sync_api import sync_playwright

output_dir = r"C:\Users\ASUS\.gemini\antigravity-ide\brain\a6624504-511c-4b9d-bc9a-468e348bde40"
os.makedirs(output_dir, exist_ok=True)

# -----------------------------------------------------------------------------
# OPCION 1: Hero Superior Tabla Visual con Barras + Base con 2 Veredictos (Horizontal)
# -----------------------------------------------------------------------------
HTML_OPT1 = '''
<section class="slide s-white active" id="slide-14-opt1">
  <header class="slide-header">
    <div class="sh-left">
      <span class="sh-red-bar"></span>
      <span class="sh-category">03 · RESULTADOS · MODOS DE FALLO ASIMÉTRICOS</span>
    </div>
    <img src="http://localhost:8085/assets/image6.png" alt="#LoxTIC" class="sh-loxtic">
  </header>
  <div class="sh-divider"></div>

  <div class="slide-content-area" style="justify-content: space-between; padding: 14px 0 8px 0;">
    
    <h2 class="s-lead-question" style="font-size: 38px; font-weight: 800; margin: 0; line-height: 1.2;">
      Alucinación frente a Sobre-rechazo: cómo fallan dos modelos con la misma nota
    </h2>

    <!-- HERO SUPERIOR: TABLA 3 INFOGRÁFICA -->
    <div style="background: #FAF5F5; border: 2.5px solid var(--c-wine-primary); padding: 22px 28px;">
      <div style="display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 14px;">
        <span style="font-family: var(--font-sans); font-size: 24px; font-weight: 800; color: var(--c-wine-dark);">
          TABLA 3: AUDITORÍA EXPERIMENTAL DE FALLAS (784 INFERENCIAS)
        </span>
        <span style="font-family: var(--font-mono); font-size: 19px; font-weight: 700; color: #555;">
          14 SONDAS TRAMPA · 84 CONSULTAS CURRICULARES
        </span>
      </div>

      <table style="width: 100%; border-collapse: collapse; font-family: var(--font-sans);">
        <thead>
          <tr style="background: var(--c-wine-primary); color: #FFFFFF;">
            <th style="padding: 14px 20px; font-family: var(--font-mono); font-size: 19px; font-weight: 700; text-align: left; width: 24%;">MODELO SLM</th>
            <th style="padding: 14px 20px; font-family: var(--font-mono); font-size: 19px; font-weight: 700; text-align: left; width: 38%;">
              RECHAZO CERTERO (14 SONDAS TRAMPA)<br>
              <span style="font-size: 15px; font-weight: 400; opacity: 0.9;">Debe detectar y rechazar temas fuera del libro</span>
            </th>
            <th style="padding: 14px 20px; font-family: var(--font-mono); font-size: 19px; font-weight: 700; text-align: left; width: 38%;">
              FALSO RECHAZO (84 CONSULTAS VÁLIDAS)<br>
              <span style="font-size: 15px; font-weight: 400; opacity: 0.9;">Nunca debe bloquear preguntas legítimas</span>
            </th>
          </tr>
        </thead>
        <tbody>
          <!-- Phi-4-mini -->
          <tr style="background: #FFFFFF; border-bottom: 2px solid #E2D6D8;">
            <td style="padding: 20px 20px; text-align: left;">
              <div style="font-size: 26px; font-weight: 800; color: #110103;">Phi-4-mini</div>
              <div style="font-family: var(--font-mono); font-size: 19px; color: var(--c-wine-primary); font-weight: 700; margin-top: 3px;">Nota: 0.8030 · 3.8B</div>
            </td>
            <td style="padding: 20px 20px;">
              <div style="display: flex; align-items: center; gap: 14px;">
                <span style="font-family: var(--font-mono); font-size: 32px; font-weight: 800; color: #C9101B; width: 95px;">28.6%</span>
                <div style="flex: 1; background: #EAE0E1; height: 18px; border-radius: 2px; overflow: hidden;">
                  <div style="width: 28.6%; background: #C9101B; height: 100%;"></div>
                </div>
              </div>
              <div style="font-size: 18px; color: #C9101B; font-weight: 700; margin-top: 6px;">
                ⚠️ 4/14 rechazadas · Alucina e inventa en 10 casos
              </div>
            </td>
            <td style="padding: 20px 20px;">
              <div style="display: flex; align-items: center; gap: 14px;">
                <span style="font-family: var(--font-mono); font-size: 32px; font-weight: 800; color: #2E7D32; width: 95px;">0.0%</span>
                <div style="flex: 1; background: #EAE0E1; height: 18px; border-radius: 2px; overflow: hidden;">
                  <div style="width: 0%; background: #2E7D32; height: 100%;"></div>
                </div>
              </div>
              <div style="font-size: 18px; color: #2E7D32; font-weight: 700; margin-top: 6px;">
                ✅ 0/84 bloqueadas · Fluidez conversacional total
              </div>
            </td>
          </tr>
          <!-- Qwen2.5-3B -->
          <tr style="background: #FAF5F5;">
            <td style="padding: 20px 20px; text-align: left;">
              <div style="font-size: 26px; font-weight: 800; color: #110103;">Qwen2.5-3B</div>
              <div style="font-family: var(--font-mono); font-size: 19px; color: var(--c-red-accent); font-weight: 700; margin-top: 3px;">Nota: 0.8010 · 3.1B</div>
            </td>
            <td style="padding: 20px 20px;">
              <div style="display: flex; align-items: center; gap: 14px;">
                <span style="font-family: var(--font-mono); font-size: 32px; font-weight: 800; color: #2E7D32; width: 95px;">85.7%</span>
                <div style="flex: 1; background: #EAE0E1; height: 18px; border-radius: 2px; overflow: hidden;">
                  <div style="width: 85.7%; background: #2E7D32; height: 100%;"></div>
                </div>
              </div>
              <div style="font-size: 18px; color: #2E7D32; font-weight: 700; margin-top: 6px;">
                ✅ 12/14 rechazadas · Alta seguridad y filtro estricto
              </div>
            </td>
            <td style="padding: 20px 20px;">
              <div style="display: flex; align-items: center; gap: 14px;">
                <span style="font-family: var(--font-mono); font-size: 32px; font-weight: 800; color: #C9101B; width: 95px;">7.1%</span>
                <div style="flex: 1; background: #EAE0E1; height: 18px; border-radius: 2px; overflow: hidden;">
                  <div style="width: 25%; background: #C9101B; height: 100%;"></div>
                </div>
              </div>
              <div style="font-size: 18px; color: #C9101B; font-weight: 700; margin-top: 6px;">
                ⚠️ 6/84 bloqueadas · Sobre-rechazo en consultas válidas
              </div>
            </td>
          </tr>
        </tbody>
      </table>
    </div>

    <!-- BASE: DOS VEREDICTOS PEDAGÓGICOS EN CAJAS LIMPIAS ESTILO PLANTILLA -->
    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 36px;">
      
      <!-- Veredicto 1: Phi-4-mini -->
      <div style="background: #FAF5F5; border-left: 7px solid var(--c-wine-primary); padding: 18px 24px;">
        <div style="display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 6px;">
          <span style="font-family: var(--font-sans); font-size: 24px; font-weight: 800; color: var(--c-wine-dark);">
            Aula Asistida: Phi-4-mini
          </span>
          <span style="font-family: var(--font-mono); font-size: 18px; font-weight: 800; color: var(--c-wine-primary);">
            FLUIDEZ
          </span>
        </div>
        <div style="font-family: var(--font-sans); font-size: 21px; color: #110103; font-weight: 600; line-height: 1.35;">
          Docente activo en aula supervisa y corrige posibles alucinaciones, aprovechando la fluidez sin fricción.
        </div>
      </div>

      <!-- Veredicto 2: Qwen2.5-3B -->
      <div style="background: #FAF5F5; border-left: 7px solid var(--c-red-accent); padding: 18px 24px;">
        <div style="display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 6px;">
          <span style="font-family: var(--font-sans); font-size: 24px; font-weight: 800; color: var(--c-wine-dark);">
            Autoestudio: Qwen2.5-3B
          </span>
          <span style="font-family: var(--font-mono); font-size: 18px; font-weight: 800; color: var(--c-red-accent);">
            SEGURIDAD
          </span>
        </div>
        <div style="font-family: var(--font-sans); font-size: 21px; color: #110103; font-weight: 600; line-height: 1.35;">
          Sin profesor presente, prima la certeza factual de no engañar al alumno, tolerando bloqueos ocasionales.
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
# OPCION 2: Díptico Comparativo Modelo a Modelo (2 Grandes Columnas Verticales)
# -----------------------------------------------------------------------------
HTML_OPT2 = '''
<section class="slide s-white active" id="slide-14-opt2">
  <header class="slide-header">
    <div class="sh-left">
      <span class="sh-red-bar"></span>
      <span class="sh-category">03 · RESULTADOS · MODOS DE FALLO ASIMÉTRICOS</span>
    </div>
    <img src="http://localhost:8085/assets/image6.png" alt="#LoxTIC" class="sh-loxtic">
  </header>
  <div class="sh-divider"></div>

  <div class="slide-content-area" style="justify-content: space-between; padding: 14px 0 8px 0;">
    
    <h2 class="s-lead-question" style="font-size: 38px; font-weight: 800; margin: 0; line-height: 1.2;">
      Alucinación frente a Sobre-rechazo: cómo fallan dos modelos con la misma nota
    </h2>

    <!-- DOS GRANDES COLUMNAS DÍPTICO -->
    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 36px; flex: 1; align-items: stretch; margin: 16px 0;">
      
      <!-- MODELO 1: PHI-4-MINI -->
      <div style="background: #FAF5F5; border-top: 8px solid var(--c-wine-primary); padding: 26px 30px; display: flex; flex-direction: column; justify-content: space-between;">
        <div>
          <div style="display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 6px;">
            <span style="font-family: var(--font-mono); font-size: 20px; font-weight: 800; color: var(--c-wine-primary); letter-spacing: 1.5px;">
              PERFIL PERMISIVO · FLUIDEZ
            </span>
            <span style="font-family: var(--font-mono); font-size: 22px; font-weight: 700; color: #555;">
              NOTA: 0.8030
            </span>
          </div>
          <div style="font-family: var(--font-sans); font-size: 34px; font-weight: 800; color: #110103; margin-bottom: 24px;">
            Phi-4-mini (3.8B)
          </div>

          <!-- Métrica 1 -->
          <div style="margin-bottom: 22px;">
            <div style="display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 6px;">
              <span style="font-family: var(--font-sans); font-size: 21px; font-weight: 700; color: #110103;">
                Rechazo certero (14 sondas trampa):
              </span>
              <span style="font-family: var(--font-mono); font-size: 30px; font-weight: 800; color: #C9101B;">
                28.6% <span style="font-size: 19px; font-weight: 600;">(4/14)</span>
              </span>
            </div>
            <div style="background: #EAE0E1; height: 14px; border-radius: 2px; overflow: hidden; margin-bottom: 6px;">
              <div style="width: 28.6%; background: #C9101B; height: 100%;"></div>
            </div>
            <div style="font-family: var(--font-sans); font-size: 19px; color: #C9101B; font-weight: 700;">
              ⚠️ Alucina en 10 casos fuera del libro de texto.
            </div>
          </div>

          <!-- Métrica 2 -->
          <div style="margin-bottom: 20px;">
            <div style="display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 6px;">
              <span style="font-family: var(--font-sans); font-size: 21px; font-weight: 700; color: #110103;">
                Falso rechazo (84 consultas válidas):
              </span>
              <span style="font-family: var(--font-mono); font-size: 30px; font-weight: 800; color: #2E7D32;">
                0.0% <span style="font-size: 19px; font-weight: 600;">(0/84)</span>
              </span>
            </div>
            <div style="background: #EAE0E1; height: 14px; border-radius: 2px; overflow: hidden; margin-bottom: 6px;">
              <div style="width: 0%; background: #2E7D32; height: 100%;"></div>
            </div>
            <div style="font-family: var(--font-sans); font-size: 19px; color: #2E7D32; font-weight: 700;">
              ✅ Fluidez total; jamás bloquea una pregunta válida.
            </div>
          </div>
        </div>

        <!-- Recomendación Base -->
        <div style="border-top: 2px solid #E2D6D8; padding-top: 16px;">
          <div style="font-family: var(--font-mono); font-size: 18px; font-weight: 800; color: var(--c-wine-primary); letter-spacing: 1px; margin-bottom: 4px;">
            VEREDICTO PEDAGÓGICO
          </div>
          <div style="font-family: var(--font-sans); font-size: 22px; font-weight: 700; color: #110103; line-height: 1.35;">
            Aula asistida: profesor modera y corrige posibles alucinaciones aprovechando la fluidez.
          </div>
        </div>
      </div>

      <!-- MODELO 2: QWEN2.5-3B -->
      <div style="background: #FAF5F5; border-top: 8px solid var(--c-red-accent); padding: 26px 30px; display: flex; flex-direction: column; justify-content: space-between;">
        <div>
          <div style="display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 6px;">
            <span style="font-family: var(--font-mono); font-size: 20px; font-weight: 800; color: var(--c-red-accent); letter-spacing: 1.5px;">
              PERFIL CONSERVADOR · SEGURIDAD
            </span>
            <span style="font-family: var(--font-mono); font-size: 22px; font-weight: 700; color: #555;">
              NOTA: 0.8010
            </span>
          </div>
          <div style="font-family: var(--font-sans); font-size: 34px; font-weight: 800; color: #110103; margin-bottom: 24px;">
            Qwen2.5-3B (3.1B)
          </div>

          <!-- Métrica 1 -->
          <div style="margin-bottom: 22px;">
            <div style="display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 6px;">
              <span style="font-family: var(--font-sans); font-size: 21px; font-weight: 700; color: #110103;">
                Rechazo certero (14 sondas trampa):
              </span>
              <span style="font-family: var(--font-mono); font-size: 30px; font-weight: 800; color: #2E7D32;">
                85.7% <span style="font-size: 19px; font-weight: 600;">(12/14)</span>
              </span>
            </div>
            <div style="background: #EAE0E1; height: 14px; border-radius: 2px; overflow: hidden; margin-bottom: 6px;">
              <div style="width: 85.7%; background: #2E7D32; height: 100%;"></div>
            </div>
            <div style="font-family: var(--font-sans); font-size: 19px; color: #2E7D32; font-weight: 700;">
              ✅ Filtro estricto; detecta y frena preguntas fuera de libro.
            </div>
          </div>

          <!-- Métrica 2 -->
          <div style="margin-bottom: 20px;">
            <div style="display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 6px;">
              <span style="font-family: var(--font-sans); font-size: 21px; font-weight: 700; color: #110103;">
                Falso rechazo (84 consultas válidas):
              </span>
              <span style="font-family: var(--font-mono); font-size: 30px; font-weight: 800; color: #C9101B;">
                7.1% <span style="font-size: 19px; font-weight: 600;">(6/84)</span>
              </span>
            </div>
            <div style="background: #EAE0E1; height: 14px; border-radius: 2px; overflow: hidden; margin-bottom: 6px;">
              <div style="width: 25%; background: #C9101B; height: 100%;"></div>
            </div>
            <div style="font-family: var(--font-sans); font-size: 19px; color: #C9101B; font-weight: 700;">
              ⚠️ Sobre-rechazo; bloquea al alumno en consultas legítimas.
            </div>
          </div>
        </div>

        <!-- Recomendación Base -->
        <div style="border-top: 2px solid #E2D6D8; padding-top: 16px;">
          <div style="font-family: var(--font-mono); font-size: 18px; font-weight: 800; color: var(--c-red-accent); letter-spacing: 1px; margin-bottom: 4px;">
            VEREDICTO PEDAGÓGICO
          </div>
          <div style="font-family: var(--font-sans); font-size: 22px; font-weight: 700; color: #110103; line-height: 1.35;">
            Autoestudio individual: sin docente, prima la certeza absoluta de no inducir al error.
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
# OPCION 3: 2 Columnas Balanceadas (Tabla 3 Completa + Perfiles a la Derecha)
# -----------------------------------------------------------------------------
HTML_OPT3 = '''
<section class="slide s-white active" id="slide-14-opt3">
  <header class="slide-header">
    <div class="sh-left">
      <span class="sh-red-bar"></span>
      <span class="sh-category">03 · RESULTADOS · MODOS DE FALLO ASIMÉTRICOS</span>
    </div>
    <img src="http://localhost:8085/assets/image6.png" alt="#LoxTIC" class="sh-loxtic">
  </header>
  <div class="sh-divider"></div>

  <div class="slide-content-area" style="justify-content: space-between; padding: 14px 0 8px 0;">
    
    <h2 class="s-lead-question" style="font-size: 38px; font-weight: 800; margin: 0; line-height: 1.2;">
      Alucinación frente a Sobre-rechazo: cómo fallan dos modelos con la misma nota
    </h2>

    <div style="display: grid; grid-template-columns: 1.2fr 1fr; gap: 32px; flex: 1; align-items: stretch; margin: 16px 0;">
      
      <!-- IZQUIERDA: TABLA 3 COMPLETA DEL PAPER -->
      <div style="background: #FAF5F5; border: 2.5px solid var(--c-wine-primary); padding: 22px 24px; display: flex; flex-direction: column; justify-content: space-between;">
        <div>
          <div style="display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 14px;">
            <span style="font-family: var(--font-sans); font-size: 22px; font-weight: 800; color: var(--c-wine-dark);">
              TABLA 3: AUDITORÍA DE FALLAS
            </span>
            <span style="font-family: var(--font-mono); font-size: 18px; font-weight: 700; color: #555;">
              784 INFERENCIAS
            </span>
          </div>

          <table style="width: 100%; border-collapse: collapse; font-family: var(--font-sans); text-align: center;">
            <thead>
              <tr style="background: var(--c-wine-primary); color: #FFFFFF;">
                <th style="padding: 12px 10px; font-family: var(--font-mono); font-size: 17px; font-weight: 700; text-align: left;">MODELO</th>
                <th style="padding: 12px 8px; font-family: var(--font-mono); font-size: 17px; font-weight: 700;">RECHAZO CERTERO<br><span style="font-size: 14px; font-weight: 400; opacity: 0.9;">14 sondas</span></th>
                <th style="padding: 12px 8px; font-family: var(--font-mono); font-size: 17px; font-weight: 700;">FALSO RECHAZO<br><span style="font-size: 14px; font-weight: 400; opacity: 0.9;">84 válidas</span></th>
                <th style="padding: 12px 8px; font-family: var(--font-mono); font-size: 17px; font-weight: 700;">FALLBACK TOTAL<br><span style="font-size: 14px; font-weight: 400; opacity: 0.9;">98 consultas</span></th>
              </tr>
            </thead>
            <tbody>
              <tr style="background: #FFFFFF; border-bottom: 2px solid #E2D6D8;">
                <td style="padding: 18px 10px; text-align: left;">
                  <div style="font-size: 22px; font-weight: 800; color: #110103;">Phi-4-mini</div>
                  <div style="font-family: var(--font-mono); font-size: 17px; color: var(--c-wine-primary); font-weight: 700;">3.8B · Q: 0.8030</div>
                </td>
                <td style="padding: 18px 8px;">
                  <div style="font-family: var(--font-mono); font-size: 26px; font-weight: 800; color: #C9101B;">28.6%</div>
                  <div style="font-size: 16px; color: #C9101B; font-weight: 700;">4/14 (Alucina)</div>
                </td>
                <td style="padding: 18px 8px;">
                  <div style="font-family: var(--font-mono); font-size: 26px; font-weight: 800; color: #2E7D32;">0.0%</div>
                  <div style="font-size: 16px; color: #2E7D32; font-weight: 700;">0/84 (Fluido)</div>
                </td>
                <td style="padding: 18px 8px;">
                  <div style="font-family: var(--font-mono); font-size: 26px; font-weight: 800; color: #110103;">4.1%</div>
                  <div style="font-size: 16px; color: #555; font-weight: 700;">4/98</div>
                </td>
              </tr>
              <tr style="background: #FAF5F5;">
                <td style="padding: 18px 10px; text-align: left;">
                  <div style="font-size: 22px; font-weight: 800; color: #110103;">Qwen2.5-3B</div>
                  <div style="font-family: var(--font-mono); font-size: 17px; color: var(--c-red-accent); font-weight: 700;">3.1B · Q: 0.8010</div>
                </td>
                <td style="padding: 18px 8px;">
                  <div style="font-family: var(--font-mono); font-size: 26px; font-weight: 800; color: #2E7D32;">85.7%</div>
                  <div style="font-size: 16px; color: #2E7D32; font-weight: 700;">12/14 (Seguro)</div>
                </td>
                <td style="padding: 18px 8px;">
                  <div style="font-family: var(--font-mono); font-size: 26px; font-weight: 800; color: #C9101B;">7.1%</div>
                  <div style="font-size: 16px; color: #C9101B; font-weight: 700;">6/84 (Bloquea)</div>
                </td>
                <td style="padding: 18px 8px;">
                  <div style="font-family: var(--font-mono); font-size: 26px; font-weight: 800; color: #110103;">18.4%</div>
                  <div style="font-size: 16px; color: #555; font-weight: 700;">18/98</div>
                </td>
              </tr>
            </tbody>
          </table>
        </div>

        <div style="border-top: 1.5px solid #E2D6D8; padding-top: 12px; font-family: var(--font-sans); font-size: 20px; color: #110103; font-weight: 600; line-height: 1.35;">
          Misma nota global (~0.80), pero perfiles de fallo <strong>diametralmente opuestos</strong>: alucinación vs. sobre-rechazo.
        </div>
      </div>

      <!-- DERECHA: DOS TARJETAS LIMPIAS ESTILO PLANTILLA -->
      <div style="display: flex; flex-direction: column; gap: 20px; justify-content: space-between;">
        
        <!-- Tarjeta 1: Phi-4-mini -->
        <div style="background: #FAF5F5; border-left: 7px solid var(--c-wine-primary); padding: 22px 26px; flex: 1; display: flex; flex-direction: column; justify-content: center;">
          <div style="display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 6px;">
            <span style="font-family: var(--font-sans); font-size: 24px; font-weight: 800; color: var(--c-wine-dark);">
              Phi-4-mini · Perfil Permisivo
            </span>
            <span style="font-family: var(--font-mono); font-size: 18px; font-weight: 800; color: var(--c-wine-primary);">
              FLUIDEZ
            </span>
          </div>
          <div style="font-family: var(--font-sans); font-size: 21px; color: #110103; font-weight: 600; line-height: 1.35; margin-bottom: 10px;">
            Jamás bloquea al alumno en clase, pero inventa respuestas verosímiles ante temas fuera del libro.
          </div>
          <div style="font-family: var(--font-sans); font-size: 21px; color: var(--c-wine-primary); font-weight: 800;">
            👨‍🏫 Aula asistida: docente modera y corrige.
          </div>
        </div>

        <!-- Tarjeta 2: Qwen2.5-3B -->
        <div style="background: #FAF5F5; border-left: 7px solid var(--c-red-accent); padding: 22px 26px; flex: 1; display: flex; flex-direction: column; justify-content: center;">
          <div style="display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 6px;">
            <span style="font-family: var(--font-sans); font-size: 24px; font-weight: 800; color: var(--c-wine-dark);">
              Qwen2.5-3B · Perfil Conservador
            </span>
            <span style="font-family: var(--font-mono); font-size: 18px; font-weight: 800; color: var(--c-red-accent);">
              SEGURIDAD
            </span>
          </div>
          <div style="font-family: var(--font-sans); font-size: 21px; color: #110103; font-weight: 600; line-height: 1.35; margin-bottom: 10px;">
            Filtra preguntas trampa con 85.7% de éxito, aunque rechaza consultas válidas por cautela extrema.
          </div>
          <div style="font-family: var(--font-sans); font-size: 21px; color: var(--c-red-accent); font-weight: 800;">
            📖 Autoestudio: prima no inducir al error al alumno.
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
  <title>Test Slide 14</title>
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
        ('slide_14_opt1.html', 'slide_14_opt1.png', HTML_OPT1),
        ('slide_14_opt2.html', 'slide_14_opt2.png', HTML_OPT2),
        ('slide_14_opt3.html', 'slide_14_opt3.png', HTML_OPT3),
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
