# -*- coding: utf-8 -*-
"""
Variantes de refinamiento para Slide 14 - OPCIÓN 2 (Díptico Modelo a Modelo)
Aplicando rigurosamente:
1. SISTEMA_DE_DISENO.md: Paleta institucional estricta (sin verde, sin emojis),
   progresión tipográfica de auditorio (>=22px, métricas 54-64px),
   sin cajas anidadas, sin espacio muerto (distribución armónica Y=200 a Y=880).
2. DECISIONES_DISENO.md: Textos concisos en 1-2 líneas, contraste máximo (#110103 sobre #FAF5F5),
   ortografía 100% impecable en español, veredictos pedagógicos dignificados a 24-26px.
3. GUIA_DE_POSIBILIDADES.md: Benchmark comparativo directo entre modelos.
"""
import os
from playwright.sync_api import sync_playwright

output_dir = r"C:\Users\ASUS\.gemini\antigravity-ide\brain\a6624504-511c-4b9d-bc9a-468e348bde40"
os.makedirs(output_dir, exist_ok=True)

# =============================================================================
# VARIANTE 2A: Díptico con Barras Institucionales y Distribución Vertical Completa
# =============================================================================
HTML_VAR_2A = '''
<section class="slide s-white active" id="slide-14-v2a">
  <header class="slide-header">
    <div class="sh-left">
      <span class="sh-red-bar"></span>
      <span class="sh-category">03 · RESULTADOS · MODOS DE FALLO ASIMÉTRICOS</span>
    </div>
    <img src="http://localhost:8085/assets/image6.png" alt="#LoxTIC" class="sh-loxtic">
  </header>
  <div class="sh-divider"></div>

  <div class="slide-content-area" style="justify-content: space-between; padding: 10px 0 4px 0; height: calc(100% - 30px);">
    
    <!-- TITULAR AUDITORIO -->
    <h2 class="s-lead-question" style="font-size: 42px; font-weight: 800; margin: 0; line-height: 1.2; color: #2C0509;">
      Alucinación frente a sobre-rechazo: cómo fallan dos modelos con la misma nota
    </h2>

    <!-- DÍPTICO COMPARATIVO: DOS GRANDES COLUMNAS QUE LLENAN EL LIENZO -->
    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 36px; flex: 1; align-items: stretch; margin: 18px 0 10px 0;">
      
      <!-- COLUMNA 1: PHI-4-MINI (PERFIL PERMISIVO) -->
      <div style="background: #FAF5F5; border-top: 8px solid var(--c-wine-primary); padding: 28px 32px; display: flex; flex-direction: column; justify-content: space-between;">
        
        <!-- Encabezado de Tarjeta -->
        <div>
          <div style="display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 8px;">
            <span style="font-family: var(--font-mono); font-size: 22px; font-weight: 800; color: var(--c-wine-primary); letter-spacing: 1.5px;">
              PERFIL PERMISIVO · FLUIDEZ
            </span>
            <span style="font-family: var(--font-mono); font-size: 24px; font-weight: 700; color: var(--c-wine-dark);">
              Q = 0.8030
            </span>
          </div>

          <div style="font-family: var(--font-sans); font-size: 38px; font-weight: 800; color: #2C0509; margin-bottom: 24px;">
            Phi-4-mini <span style="font-size: 26px; font-weight: 600; color: #5D4A4D;">(3.8B · Microsoft)</span>
          </div>

          <!-- Métrica 1: Rechazo Certero -->
          <div style="margin-bottom: 24px;">
            <div style="display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 8px;">
              <span style="font-family: var(--font-sans); font-size: 23px; font-weight: 700; color: #2C0509;">
                Rechazo certero (14 sondas trampa):
              </span>
              <span style="font-family: var(--font-mono); font-size: 38px; font-weight: 800; color: var(--c-red-accent);">
                28.6% <span style="font-size: 22px; font-weight: 700; color: #5D4A4D;">(4/14)</span>
              </span>
            </div>
            <!-- Barra Proporcional Institucional -->
            <div style="background: #EAE0E1; height: 16px; width: 100%; margin-bottom: 8px;">
              <div style="width: 28.6%; background: var(--c-red-accent); height: 100%;"></div>
            </div>
            <div style="font-family: var(--font-sans); font-size: 22px; color: var(--c-red-accent); font-weight: 700;">
              Alucina en 10 casos fuera del libro de texto.
            </div>
          </div>

          <!-- Métrica 2: Falso Rechazo -->
          <div style="margin-bottom: 20px;">
            <div style="display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 8px;">
              <span style="font-family: var(--font-sans); font-size: 23px; font-weight: 700; color: #2C0509;">
                Falso rechazo (84 consultas válidas):
              </span>
              <span style="font-family: var(--font-mono); font-size: 38px; font-weight: 800; color: var(--c-wine-primary);">
                0.0% <span style="font-size: 22px; font-weight: 700; color: #5D4A4D;">(0/84)</span>
              </span>
            </div>
            <!-- Barra Proporcional Institucional -->
            <div style="background: #EAE0E1; height: 16px; width: 100%; margin-bottom: 8px;">
              <div style="width: 0%; background: var(--c-wine-primary); height: 100%;"></div>
            </div>
            <div style="font-family: var(--font-sans); font-size: 22px; color: var(--c-wine-primary); font-weight: 700;">
              Fluidez total; jamás bloquea una pregunta legítima.
            </div>
          </div>
        </div>

        <!-- Veredicto Pedagógico Dignificado (Fila Integrada con Línea Sutil) -->
        <div style="border-top: 2px solid #E2D6D8; padding-top: 18px; margin-top: 10px;">
          <div style="font-family: var(--font-mono); font-size: 20px; font-weight: 800; color: var(--c-wine-primary); letter-spacing: 1.5px; margin-bottom: 6px;">
            VEREDICTO PEDAGÓGICO
          </div>
          <div style="font-family: var(--font-sans); font-size: 24px; font-weight: 700; color: #110103; line-height: 1.35;">
            Aula asistida: el docente modera y corrige alucinaciones, aprovechando la fluidez sin fricción.
          </div>
        </div>

      </div>

      <!-- COLUMNA 2: QWEN2.5-3B (PERFIL CONSERVADOR) -->
      <div style="background: #FAF5F5; border-top: 8px solid var(--c-red-accent); padding: 28px 32px; display: flex; flex-direction: column; justify-content: space-between;">
        
        <!-- Encabezado de Tarjeta -->
        <div>
          <div style="display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 8px;">
            <span style="font-family: var(--font-mono); font-size: 22px; font-weight: 800; color: var(--c-red-accent); letter-spacing: 1.5px;">
              PERFIL CONSERVADOR · SEGURIDAD
            </span>
            <span style="font-family: var(--font-mono); font-size: 24px; font-weight: 700; color: var(--c-wine-dark);">
              Q = 0.8010
            </span>
          </div>

          <div style="font-family: var(--font-sans); font-size: 38px; font-weight: 800; color: #2C0509; margin-bottom: 24px;">
            Qwen2.5-3B <span style="font-size: 26px; font-weight: 600; color: #5D4A4D;">(3.1B · Alibaba)</span>
          </div>

          <!-- Métrica 1: Rechazo Certero -->
          <div style="margin-bottom: 24px;">
            <div style="display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 8px;">
              <span style="font-family: var(--font-sans); font-size: 23px; font-weight: 700; color: #2C0509;">
                Rechazo certero (14 sondas trampa):
              </span>
              <span style="font-family: var(--font-mono); font-size: 38px; font-weight: 800; color: var(--c-wine-primary);">
                85.7% <span style="font-size: 22px; font-weight: 700; color: #5D4A4D;">(12/14)</span>
              </span>
            </div>
            <!-- Barra Proporcional Institucional -->
            <div style="background: #EAE0E1; height: 16px; width: 100%; margin-bottom: 8px;">
              <div style="width: 85.7%; background: var(--c-wine-primary); height: 100%;"></div>
            </div>
            <div style="font-family: var(--font-sans); font-size: 22px; color: var(--c-wine-primary); font-weight: 700;">
              Filtro estricto; bloquea preguntas fuera del libro.
            </div>
          </div>

          <!-- Métrica 2: Falso Rechazo -->
          <div style="margin-bottom: 20px;">
            <div style="display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 8px;">
              <span style="font-family: var(--font-sans); font-size: 23px; font-weight: 700; color: #2C0509;">
                Falso rechazo (84 consultas válidas):
              </span>
              <span style="font-family: var(--font-mono); font-size: 38px; font-weight: 800; color: var(--c-red-accent);">
                7.1% <span style="font-size: 22px; font-weight: 700; color: #5D4A4D;">(6/84)</span>
              </span>
            </div>
            <!-- Barra Proporcional Institucional -->
            <div style="background: #EAE0E1; height: 16px; width: 100%; margin-bottom: 8px;">
              <div style="width: 25%; background: var(--c-red-accent); height: 100%;"></div>
            </div>
            <div style="font-family: var(--font-sans); font-size: 22px; color: var(--c-red-accent); font-weight: 700;">
              Sobre-rechazo; bloquea al alumno en consultas válidas.
            </div>
          </div>
        </div>

        <!-- Veredicto Pedagógico Dignificado (Fila Integrada con Línea Sutil) -->
        <div style="border-top: 2px solid #E2D6D8; padding-top: 18px; margin-top: 10px;">
          <div style="font-family: var(--font-mono); font-size: 20px; font-weight: 800; color: var(--c-red-accent); letter-spacing: 1.5px; margin-bottom: 6px;">
            VEREDICTO PEDAGÓGICO
          </div>
          <div style="font-family: var(--font-sans); font-size: 24px; font-weight: 700; color: #110103; line-height: 1.35;">
            Autoestudio: sin docente, prima la certeza absoluta de no inducir al error factual.
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

# =============================================================================
# VARIANTE 2B: Díptico con Números Gigantes Monumentales (60px) + Desglose Limpio
# =============================================================================
HTML_VAR_2B = '''
<section class="slide s-white active" id="slide-14-v2b">
  <header class="slide-header">
    <div class="sh-left">
      <span class="sh-red-bar"></span>
      <span class="sh-category">03 · RESULTADOS · MODOS DE FALLO ASIMÉTRICOS</span>
    </div>
    <img src="http://localhost:8085/assets/image6.png" alt="#LoxTIC" class="sh-loxtic">
  </header>
  <div class="sh-divider"></div>

  <div class="slide-content-area" style="justify-content: space-between; padding: 10px 0 4px 0; height: calc(100% - 30px);">
    
    <!-- TITULAR AUDITORIO -->
    <h2 class="s-lead-question" style="font-size: 42px; font-weight: 800; margin: 0; line-height: 1.2; color: #2C0509;">
      Alucinación frente a sobre-rechazo: cómo fallan dos modelos con la misma nota
    </h2>

    <!-- DÍPTICO CON NÚMEROS MONUMENTALES -->
    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 36px; flex: 1; align-items: stretch; margin: 18px 0 10px 0;">
      
      <!-- PHI-4-MINI -->
      <div style="background: #FAF5F5; border-top: 8px solid var(--c-wine-primary); padding: 28px 32px; display: flex; flex-direction: column; justify-content: space-between;">
        
        <div>
          <div style="display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 6px;">
            <span style="font-family: var(--font-mono); font-size: 21px; font-weight: 800; color: var(--c-wine-primary); letter-spacing: 1.5px;">
              PERFIL PERMISIVO · FLUIDEZ
            </span>
            <span style="font-family: var(--font-mono); font-size: 24px; font-weight: 700; color: var(--c-wine-dark);">
              NOTA: 0.8030
            </span>
          </div>

          <div style="font-family: var(--font-sans); font-size: 38px; font-weight: 800; color: #2C0509; margin-bottom: 24px;">
            Phi-4-mini (3.8B)
          </div>

          <!-- Dos Bloques Métricos con Línea Lateral S8 -->
          <div style="display: flex; flex-direction: column; gap: 20px;">
            
            <!-- Métrica 1 -->
            <div style="display: flex; gap: 18px; align-items: center;">
              <div style="width: 6px; height: 78px; background: var(--c-red-accent); flex-shrink: 0;"></div>
              <div>
                <div style="display: flex; align-items: baseline; gap: 12px;">
                  <span style="font-family: var(--font-mono); font-size: 52px; font-weight: 800; color: var(--c-red-accent); line-height: 1;">28.6%</span>
                  <span style="font-family: var(--font-sans); font-size: 24px; font-weight: 800; color: #2C0509;">Rechazo certero</span>
                  <span style="font-family: var(--font-mono); font-size: 20px; font-weight: 700; color: #5D4A4D;">(4/14)</span>
                </div>
                <div style="font-family: var(--font-sans); font-size: 22px; color: var(--c-red-accent); font-weight: 700; margin-top: 4px;">
                  Alucina e inventa hechos en 10 preguntas fuera del libro.
                </div>
              </div>
            </div>

            <!-- Métrica 2 -->
            <div style="display: flex; gap: 18px; align-items: center;">
              <div style="width: 6px; height: 78px; background: var(--c-wine-primary); flex-shrink: 0;"></div>
              <div>
                <div style="display: flex; align-items: baseline; gap: 12px;">
                  <span style="font-family: var(--font-mono); font-size: 52px; font-weight: 800; color: var(--c-wine-primary); line-height: 1;">0.0%</span>
                  <span style="font-family: var(--font-sans); font-size: 24px; font-weight: 800; color: #2C0509;">Falso rechazo</span>
                  <span style="font-family: var(--font-mono); font-size: 20px; font-weight: 700; color: #5D4A4D;">(0/84)</span>
                </div>
                <div style="font-family: var(--font-sans); font-size: 22px; color: var(--c-wine-primary); font-weight: 700; margin-top: 4px;">
                  Fluidez absoluta; jamás bloquea a un alumno con dudas legítimas.
                </div>
              </div>
            </div>

          </div>
        </div>

        <!-- Veredicto Pedagógico Dignificado -->
        <div style="border-top: 2px solid #E2D6D8; padding-top: 18px; margin-top: 10px;">
          <div style="font-family: var(--font-mono); font-size: 20px; font-weight: 800; color: var(--c-wine-primary); letter-spacing: 1.5px; margin-bottom: 6px;">
            VEREDICTO PEDAGÓGICO
          </div>
          <div style="font-family: var(--font-sans); font-size: 24px; font-weight: 700; color: #110103; line-height: 1.35;">
            Aula guiada: el docente en clase supervisa y corrige, aprovechando una conversación sin trabas.
          </div>
        </div>

      </div>

      <!-- QWEN2.5-3B -->
      <div style="background: #FAF5F5; border-top: 8px solid var(--c-red-accent); padding: 28px 32px; display: flex; flex-direction: column; justify-content: space-between;">
        
        <div>
          <div style="display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 6px;">
            <span style="font-family: var(--font-mono); font-size: 21px; font-weight: 800; color: var(--c-red-accent); letter-spacing: 1.5px;">
              PERFIL CONSERVADOR · SEGURIDAD
            </span>
            <span style="font-family: var(--font-mono); font-size: 24px; font-weight: 700; color: var(--c-wine-dark);">
              NOTA: 0.8010
            </span>
          </div>

          <div style="font-family: var(--font-sans); font-size: 38px; font-weight: 800; color: #2C0509; margin-bottom: 24px;">
            Qwen2.5-3B (3.1B)
          </div>

          <!-- Dos Bloques Métricos con Línea Lateral S8 -->
          <div style="display: flex; flex-direction: column; gap: 20px;">
            
            <!-- Métrica 1 -->
            <div style="display: flex; gap: 18px; align-items: center;">
              <div style="width: 6px; height: 78px; background: var(--c-wine-primary); flex-shrink: 0;"></div>
              <div>
                <div style="display: flex; align-items: baseline; gap: 12px;">
                  <span style="font-family: var(--font-mono); font-size: 52px; font-weight: 800; color: var(--c-wine-primary); line-height: 1;">85.7%</span>
                  <span style="font-family: var(--font-sans); font-size: 24px; font-weight: 800; color: #2C0509;">Rechazo certero</span>
                  <span style="font-family: var(--font-mono); font-size: 20px; font-weight: 700; color: #5D4A4D;">(12/14)</span>
                </div>
                <div style="font-family: var(--font-sans); font-size: 22px; color: var(--c-wine-primary); font-weight: 700; margin-top: 4px;">
                  Filtro riguroso; frena el 85.7% de preguntas trampa fuera de libro.
                </div>
              </div>
            </div>

            <!-- Métrica 2 -->
            <div style="display: flex; gap: 18px; align-items: center;">
              <div style="width: 6px; height: 78px; background: var(--c-red-accent); flex-shrink: 0;"></div>
              <div>
                <div style="display: flex; align-items: baseline; gap: 12px;">
                  <span style="font-family: var(--font-mono); font-size: 52px; font-weight: 800; color: var(--c-red-accent); line-height: 1;">7.1%</span>
                  <span style="font-family: var(--font-sans); font-size: 24px; font-weight: 800; color: #2C0509;">Falso rechazo</span>
                  <span style="font-family: var(--font-mono); font-size: 20px; font-weight: 700; color: #5D4A4D;">(6/84)</span>
                </div>
                <div style="font-family: var(--font-sans); font-size: 22px; color: var(--c-red-accent); font-weight: 700; margin-top: 4px;">
                  Sobre-rechazo; rechaza 6 preguntas válidas por cautela extrema.
                </div>
              </div>
            </div>

          </div>
        </div>

        <!-- Veredicto Pedagógico Dignificado -->
        <div style="border-top: 2px solid #E2D6D8; padding-top: 18px; margin-top: 10px;">
          <div style="font-family: var(--font-mono); font-size: 20px; font-weight: 800; color: var(--c-red-accent); letter-spacing: 1.5px; margin-bottom: 6px;">
            VEREDICTO PEDAGÓGICO
          </div>
          <div style="font-family: var(--font-sans); font-size: 24px; font-weight: 700; color: #110103; line-height: 1.35;">
            Autoestudio: sin profesor presente, prima no inducir al error al estudiante autónomo.
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

# =============================================================================
# VARIANTE 2C: Díptico con Barra Superior + Barras Proporcionales + KPI S8
# =============================================================================
HTML_VAR_2C = '''
<section class="slide s-white active" id="slide-14-v2c">
  <header class="slide-header">
    <div class="sh-left">
      <span class="sh-red-bar"></span>
      <span class="sh-category">03 · RESULTADOS · MODOS DE FALLO ASIMÉTRICOS</span>
    </div>
    <img src="http://localhost:8085/assets/image6.png" alt="#LoxTIC" class="sh-loxtic">
  </header>
  <div class="sh-divider"></div>

  <div class="slide-content-area" style="justify-content: space-between; padding: 10px 0 4px 0; height: calc(100% - 30px);">
    
    <!-- TITULAR AUDITORIO -->
    <h2 class="s-lead-question" style="font-size: 42px; font-weight: 800; margin: 0; line-height: 1.2; color: #2C0509;">
      Alucinación frente a sobre-rechazo: cómo fallan dos modelos con la misma nota
    </h2>

    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 36px; flex: 1; align-items: stretch; margin: 18px 0 10px 0;">
      
      <!-- PHI-4-MINI -->
      <div style="background: #FAF5F5; border-top: 8px solid var(--c-wine-primary); padding: 28px 32px; display: flex; flex-direction: column; justify-content: space-between;">
        
        <div>
          <div style="display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 6px;">
            <span style="font-family: var(--font-mono); font-size: 21px; font-weight: 800; color: var(--c-wine-primary); letter-spacing: 1.5px;">
              PERFIL PERMISIVO
            </span>
            <span style="font-family: var(--font-mono); font-size: 24px; font-weight: 800; color: var(--c-wine-dark);">
              NOTA: 0.8030
            </span>
          </div>

          <div style="font-family: var(--font-sans); font-size: 38px; font-weight: 800; color: #2C0509; margin-bottom: 22px;">
            Phi-4-mini <span style="font-size: 24px; font-weight: 600; color: #5D4A4D;">(3.8B · Fallback: 4.1%)</span>
          </div>

          <!-- Métrica 1 -->
          <div style="margin-bottom: 22px;">
            <div style="display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 6px;">
              <span style="font-family: var(--font-sans); font-size: 23px; font-weight: 700; color: #2C0509;">
                Rechazo certero (sondas trampa):
              </span>
              <span style="font-family: var(--font-mono); font-size: 34px; font-weight: 800; color: var(--c-red-accent);">
                28.6% <span style="font-size: 20px; font-weight: 700; color: #5D4A4D;">(4/14)</span>
              </span>
            </div>
            <div style="background: #EAE0E1; height: 16px; width: 100%; margin-bottom: 6px;">
              <div style="width: 28.6%; background: var(--c-red-accent); height: 100%;"></div>
            </div>
            <div style="font-family: var(--font-sans); font-size: 21px; color: var(--c-red-accent); font-weight: 700;">
              Alucina en 10 casos fuera del libro de texto.
            </div>
          </div>

          <!-- Métrica 2 -->
          <div style="margin-bottom: 18px;">
            <div style="display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 6px;">
              <span style="font-family: var(--font-sans); font-size: 23px; font-weight: 700; color: #2C0509;">
                Falso rechazo (consultas válidas):
              </span>
              <span style="font-family: var(--font-mono); font-size: 34px; font-weight: 800; color: var(--c-wine-primary);">
                0.0% <span style="font-size: 20px; font-weight: 700; color: #5D4A4D;">(0/84)</span>
              </span>
            </div>
            <div style="background: #EAE0E1; height: 16px; width: 100%; margin-bottom: 6px;">
              <div style="width: 0%; background: var(--c-wine-primary); height: 100%;"></div>
            </div>
            <div style="font-family: var(--font-sans); font-size: 21px; color: var(--c-wine-primary); font-weight: 700;">
              Fluidez total; jamás bloquea preguntas curriculares.
            </div>
          </div>
        </div>

        <!-- Base Pedagógica -->
        <div style="border-top: 2px solid #E2D6D8; padding-top: 18px;">
          <div style="font-family: var(--font-mono); font-size: 19px; font-weight: 800; color: var(--c-wine-primary); letter-spacing: 1.5px; margin-bottom: 4px;">
            APLICACIÓN PEDAGÓGICA RECOMENDADA
          </div>
          <div style="font-family: var(--font-sans); font-size: 23px; font-weight: 700; color: #110103; line-height: 1.35;">
            Aula asistida: interacción fluida donde el docente activo guía, modera y rectifica alucinaciones.
          </div>
        </div>

      </div>

      <!-- QWEN2.5-3B -->
      <div style="background: #FAF5F5; border-top: 8px solid var(--c-red-accent); padding: 28px 32px; display: flex; flex-direction: column; justify-content: space-between;">
        
        <div>
          <div style="display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 6px;">
            <span style="font-family: var(--font-mono); font-size: 21px; font-weight: 800; color: var(--c-red-accent); letter-spacing: 1.5px;">
              PERFIL CONSERVADOR
            </span>
            <span style="font-family: var(--font-mono); font-size: 24px; font-weight: 800; color: var(--c-wine-dark);">
              NOTA: 0.8010
            </span>
          </div>

          <div style="font-family: var(--font-sans); font-size: 38px; font-weight: 800; color: #2C0509; margin-bottom: 22px;">
            Qwen2.5-3B <span style="font-size: 24px; font-weight: 600; color: #5D4A4D;">(3.1B · Fallback: 18.4%)</span>
          </div>

          <!-- Métrica 1 -->
          <div style="margin-bottom: 22px;">
            <div style="display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 6px;">
              <span style="font-family: var(--font-sans); font-size: 23px; font-weight: 700; color: #2C0509;">
                Rechazo certero (sondas trampa):
              </span>
              <span style="font-family: var(--font-mono); font-size: 34px; font-weight: 800; color: var(--c-wine-primary);">
                85.7% <span style="font-size: 20px; font-weight: 700; color: #5D4A4D;">(12/14)</span>
              </span>
            </div>
            <div style="background: #EAE0E1; height: 16px; width: 100%; margin-bottom: 6px;">
              <div style="width: 85.7%; background: var(--c-wine-primary); height: 100%;"></div>
            </div>
            <div style="font-family: var(--font-sans); font-size: 21px; color: var(--c-wine-primary); font-weight: 700;">
              Filtro estricto; bloquea preguntas fuera del libro.
            </div>
          </div>

          <!-- Métrica 2 -->
          <div style="margin-bottom: 18px;">
            <div style="display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 6px;">
              <span style="font-family: var(--font-sans); font-size: 23px; font-weight: 700; color: #2C0509;">
                Falso rechazo (consultas válidas):
              </span>
              <span style="font-family: var(--font-mono); font-size: 34px; font-weight: 800; color: var(--c-red-accent);">
                7.1% <span style="font-size: 20px; font-weight: 700; color: #5D4A4D;">(6/84)</span>
              </span>
            </div>
            <div style="background: #EAE0E1; height: 16px; width: 100%; margin-bottom: 6px;">
              <div style="width: 25%; background: var(--c-red-accent); height: 100%;"></div>
            </div>
            <div style="font-family: var(--font-sans); font-size: 21px; color: var(--c-red-accent); font-weight: 700;">
              Sobre-rechazo; rechaza consultas legítimas por cautela.
            </div>
          </div>
        </div>

        <!-- Base Pedagógica -->
        <div style="border-top: 2px solid #E2D6D8; padding-top: 18px;">
          <div style="font-family: var(--font-mono); font-size: 19px; font-weight: 800; color: var(--c-red-accent); letter-spacing: 1.5px; margin-bottom: 4px;">
            APLICACIÓN PEDAGÓGICA RECOMENDADA
          </div>
          <div style="font-family: var(--font-sans); font-size: 23px; font-weight: 700; color: #110103; line-height: 1.35;">
            Autoestudio individual: sin profesor, prima la certeza de no engañar al estudiante.
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
  <title>Test Slide 14 Opcion 2</title>
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
        ('slide_14_v2a.html', 'slide_14_v2a.png', HTML_VAR_2A),
        ('slide_14_v2b.html', 'slide_14_v2b.png', HTML_VAR_2B),
        ('slide_14_v2c.html', 'slide_14_v2c.png', HTML_VAR_2C),
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
