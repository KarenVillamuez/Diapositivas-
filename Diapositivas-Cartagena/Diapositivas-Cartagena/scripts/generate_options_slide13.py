# -*- coding: utf-8 -*-
"""
Generación de 3 opciones de diseño para Slide 13:
- Opción A: Contraste Visual 15x-18x (Gráfica SVG limpia de dispersión a la izquierda + 3 tarjetas métricas a la derecha).
- Opción B: Tríptico de 3 Columnas Ejecutivas (0.002 Diferencia | 18.5x Varianza | p = 0.569 Wilcoxon) con conclusión metodológica al pie.
- Opción C: Gráfica de Barras Comparativas de la Figura 3 (Desviación Intra-modelo 0.037 vs Diferencia Inter-modelo 0.025 vs Brecha Neta 0.002) + Tarjetas de Auditoría.
"""
import os
from playwright.sync_api import sync_playwright

output_dir = r"C:\Users\ASUS\.gemini\antigravity-ide\brain\a6624504-511c-4b9d-bc9a-468e348bde40"
os.makedirs(output_dir, exist_ok=True)

# -----------------------------------------------------------------------------
# OPCIÓN A: Contraste de Magnitud (SVG Proporcional + 3 Tarjetas Planas a la Derecha)
# -----------------------------------------------------------------------------
OPCION_A_HTML = '''
<section class="slide s-white active" id="slide-13-opt-a">
  <header class="slide-header">
    <div class="sh-left">
      <span class="sh-red-bar"></span>
      <span class="sh-category">03 · RESULTADOS · EL FALSO EMPATE ESTADÍSTICO</span>
    </div>
    <img src="assets/image6.png" alt="#LoxTIC" class="sh-loxtic">
  </header>
  <div class="sh-divider"></div>

  <div class="slide-content-area" style="justify-content: space-between; padding: 14px 0 6px 0;">
    
    <!-- Título Principal con Ortografía Impecable -->
    <h2 class="s-lead-question" style="font-size: 38px; font-weight: 800; margin: 0; line-height: 1.2;">
      La ilusión del 0.795: la variación por semilla supera la diferencia entre modelos
    </h2>

    <!-- GRID 2 COLUMNAS: Hero Gráfico a la Izquierda + Métricas a la Derecha -->
    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 32px; flex: 1; align-items: stretch; margin: 16px 0;">
      
      <!-- HERO IZQUIERDO: Gráfico de Proporción Real (Varianza vs Diferencia) -->
      <div style="background: #FAF5F5; border: 2.5px solid var(--c-wine-primary); padding: 24px 28px; display: flex; flex-direction: column; justify-content: space-between;">
        
        <div>
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px;">
            <span style="font-family: var(--font-sans); font-size: 22px; font-weight: 800; color: var(--c-wine-dark);">
              MAGNITUD DEL EFECTO: RUIDO VS. SEÑAL
            </span>
            <span style="font-family: var(--font-mono); font-size: 20px; font-weight: 800; color: var(--c-red-accent); background: #FFE4E6; border: 1.5px solid var(--c-red-accent); padding: 2px 10px;">
              FIGURA 3 DEL PAPER
            </span>
          </div>

          <!-- SVG Visualmente Exacto y Proporcional -->
          <svg viewBox="0 0 760 290" style="width: 100%; height: auto; font-family: var(--font-sans);">
            <!-- Líneas de Guía -->
            <line x1="60" y1="30" x2="720" y2="30" stroke="#E2D6D8" stroke-dasharray="4,4" />
            <line x1="60" y1="120" x2="720" y2="120" stroke="#E2D6D8" stroke-dasharray="4,4" />
            <line x1="60" y1="210" x2="720" y2="210" stroke="#2C0509" stroke-width="2.5" />
            
            <!-- Barra 1: Varianza por Semilla (0.037) -->
            <rect x="130" y="40" width="130" height="170" fill="var(--c-wine-primary)" />
            <text x="195" y="28" font-size="28" font-weight="800" fill="var(--c-wine-primary)" text-anchor="middle">0.037</text>
            <text x="195" y="242" font-size="21" font-weight="800" fill="#110103" text-anchor="middle">Varianza Semilla</text>
            <text x="195" y="268" font-size="19" font-weight="600" fill="#5D4A4D" text-anchor="middle">Desviación estándar</text>

            <!-- Barra 2: Diferencia Inter-Modelos (0.025) -->
            <rect x="330" y="95" width="130" height="115" fill="var(--c-red-accent)" />
            <text x="395" y="83" font-size="28" font-weight="800" fill="var(--c-red-accent)" text-anchor="middle">0.025</text>
            <text x="395" y="242" font-size="21" font-weight="800" fill="#110103" text-anchor="middle">Diferencia Modelos</text>
            <text x="395" y="268" font-size="19" font-weight="600" fill="#5D4A4D" text-anchor="middle">Media absoluta</text>

            <!-- Barra 3: Brecha Neta (0.002) -->
            <rect x="530" y="201" width="130" height="9" fill="#B38600" />
            <text x="595" y="190" font-size="28" font-weight="800" fill="#B38600" text-anchor="middle">0.002</text>
            <text x="595" y="242" font-size="21" font-weight="800" fill="#110103" text-anchor="middle">Brecha Neta</text>
            <text x="595" y="268" font-size="19" font-weight="600" fill="#5D4A4D" text-anchor="middle">Phi vs. Qwen</text>
          </svg>
        </div>

        <!-- Remate del Gráfico -->
        <div style="background: #FFFFFF; border: 1.5px solid var(--c-wine-primary); padding: 12px 18px; font-family: var(--font-sans); font-size: 21px; color: #110103; font-weight: 700; line-height: 1.3;">
          <strong style="color: var(--c-wine-primary);">Conclusión empírica:</strong> El ruido estocástico de las semillas (0.037) es <strong>18.5× mayor</strong> que la diferencia final entre modelos (0.002).
        </div>

      </div>

      <!-- DERECHA: 3 Tarjetas con la Estructura Horizontal Limpia de K2.2 -->
      <div style="display: flex; flex-direction: column; justify-content: space-between; gap: 16px;">
        
        <!-- Tarjeta 1: La Brecha Neta -->
        <div style="background: #FAF5F5; border: 2.5px solid var(--c-wine-primary); display: flex; align-items: stretch; flex: 1;">
          <div style="flex: 0 0 190px; background: #FFFFFF; border-right: 2.5px solid var(--c-wine-primary); color: var(--c-wine-primary); font-family: var(--font-mono); font-size: 25px; font-weight: 800; display: flex; align-items: center; justify-content: center; text-align: center; padding: 10px;">
            Δ = 0.002
          </div>
          <div style="flex: 1; padding: 14px 20px; display: flex; flex-direction: column; justify-content: center;">
            <div style="font-family: var(--font-sans); font-size: 23px; font-weight: 800; color: var(--c-wine-dark); margin-bottom: 2px;">
              Promedio General: 0.8030 vs. 0.8010
            </div>
            <div style="font-family: var(--font-sans); font-size: 21px; color: #110103; font-weight: 600; line-height: 1.3;">
              Phi-4-mini y Qwen2.5-3B empatan en la práctica con solo 2 milésimas de separación.
            </div>
          </div>
        </div>

        <!-- Tarjeta 2: Veredicto Wilcoxon -->
        <div style="background: #FAF5F5; border: 2.5px solid var(--c-red-accent); display: flex; align-items: stretch; flex: 1;">
          <div style="flex: 0 0 190px; background: #FFFFFF; border-right: 2.5px solid var(--c-red-accent); color: var(--c-red-accent); font-family: var(--font-mono); font-size: 23px; font-weight: 800; display: flex; align-items: center; justify-content: center; text-align: center; padding: 10px; line-height: 1.2;">
            p = 0.569<br><span style="font-size: 19px; color: #555;">W = 31.0</span>
          </div>
          <div style="flex: 1; padding: 14px 20px; display: flex; flex-direction: column; justify-content: center;">
            <div style="font-family: var(--font-sans); font-size: 23px; font-weight: 800; color: var(--c-wine-dark); margin-bottom: 2px;">
              Prueba de Rangos de Wilcoxon
            </div>
            <div style="font-family: var(--font-sans); font-size: 21px; color: #110103; font-weight: 600; line-height: 1.3;">
              Al ser <strong>p > 0.05</strong>, se descarta cualquier diferencia estadísticamente significativa.
            </div>
          </div>
        </div>

        <!-- Tarjeta 3: Inversión de Ranking -->
        <div style="background: #FAF5F5; border: 2.5px solid #8A5500; display: flex; align-items: stretch; flex: 1;">
          <div style="flex: 0 0 190px; background: #FFFFFF; border-right: 2.5px solid #8A5500; color: #8A5500; font-family: var(--font-mono); font-size: 25px; font-weight: 800; display: flex; align-items: center; justify-content: center; text-align: center; padding: 10px;">
            18.5×
          </div>
          <div style="flex: 1; padding: 14px 20px; display: flex; flex-direction: column; justify-content: center;">
            <div style="font-family: var(--font-sans); font-size: 23px; font-weight: 800; color: var(--c-wine-dark); margin-bottom: 2px;">
              Inversión del Ganador por Semilla
            </div>
            <div style="font-family: var(--font-sans); font-size: 21px; color: #110103; font-weight: 600; line-height: 1.3;">
              El modelo que gana en la semilla 42 pierde en la semilla 7: <strong>el azar define el ranking</strong>.
            </div>
          </div>
        </div>

      </div>

    </div>

    <!-- BANNER DE ALERTA METODOLÓGICA (100% Plano, Alto Impacto) -->
    <div style="background: #FAF5F5; border: 2px solid var(--c-red-accent); border-left: 8px solid var(--c-red-accent); padding: 14px 22px; display: flex; justify-content: space-between; align-items: center;">
      <span style="font-family: var(--font-sans); font-size: 22px; font-weight: 800; color: var(--c-wine-dark);">
        ⚠️ ALERTA METODOLÓGICA: Prohibido declarar modelos ganadores basándose en una sola corrida sin réplicas estocásticas.
      </span>
      <span style="font-family: var(--font-mono); font-size: 20px; font-weight: 800; color: var(--c-red-accent); white-space: nowrap;">
        4 SEMILLAS OBLIGATORIAS
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

# -----------------------------------------------------------------------------
# OPCIÓN B: Tríptico de 3 Columnas Ejecutivas Horizontales
# -----------------------------------------------------------------------------
OPCION_B_HTML = '''
<section class="slide s-white active" id="slide-13-opt-b">
  <header class="slide-header">
    <div class="sh-left">
      <span class="sh-red-bar"></span>
      <span class="sh-category">03 · RESULTADOS · EL FALSO EMPATE ESTADÍSTICO</span>
    </div>
    <img src="assets/image6.png" alt="#LoxTIC" class="sh-loxtic">
  </header>
  <div class="sh-divider"></div>

  <div class="slide-content-area" style="justify-content: space-between; padding: 14px 0 6px 0;">
    
    <h2 class="s-lead-question" style="font-size: 38px; font-weight: 800; margin: 0; line-height: 1.2;">
      La ilusión del 0.795: la variación por semilla supera la diferencia entre modelos
    </h2>

    <!-- TRÍPTICO DE 3 COLUMNAS: Los 3 Hallazgos Estadísticos Fundamentales -->
    <div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 28px; flex: 1; margin: 18px 0; align-items: stretch;">
      
      <!-- Columna 1: La Brecha Neta -->
      <div style="background: #FAF5F5; border: 2.5px solid var(--c-wine-primary); border-top: 8px solid var(--c-wine-primary); padding: 24px 26px; display: flex; flex-direction: column; justify-content: space-between;">
        <div>
          <div style="font-family: var(--font-mono); font-size: 20px; font-weight: 800; color: var(--c-wine-primary); letter-spacing: 0.5px; margin-bottom: 8px;">
            01 · EL ESPEJISMO NETO
          </div>
          <div style="font-family: var(--font-sans); font-size: 64px; font-weight: 800; color: var(--c-wine-primary); line-height: 1; margin-bottom: 12px;">
            0.002
          </div>
          <h3 style="font-family: var(--font-sans); font-size: 25px; font-weight: 800; color: var(--c-wine-dark); margin: 0 0 10px 0;">
            Phi-4: 0.8030 vs. Qwen: 0.8010
          </h3>
          <p style="font-family: var(--font-sans); font-size: 22px; color: #110103; font-weight: 600; line-height: 1.4; margin: 0;">
            Una sola corrida sugiere que un modelo es superior por apenas <strong>dos milésimas</strong>, creando una falsa jerarquía.
          </p>
        </div>
        <div style="margin-top: 14px; padding-top: 10px; border-top: 2px solid rgba(70,8,17,0.2); font-family: var(--font-sans); font-size: 21px; font-weight: 700; color: var(--c-wine-primary);">
          Media de 4 réplicas estocásticas.
        </div>
      </div>

      <!-- Columna 2: La Varianza Estocástica -->
      <div style="background: #FAF5F5; border: 2.5px solid var(--c-red-accent); border-top: 8px solid var(--c-red-accent); padding: 24px 26px; display: flex; flex-direction: column; justify-content: space-between;">
        <div>
          <div style="font-family: var(--font-mono); font-size: 20px; font-weight: 800; color: var(--c-red-accent); letter-spacing: 0.5px; margin-bottom: 8px;">
            02 · EL RUIDO DOMINANTE
          </div>
          <div style="font-family: var(--font-sans); font-size: 64px; font-weight: 800; color: var(--c-red-accent); line-height: 1; margin-bottom: 12px;">
            18.5×
          </div>
          <h3 style="font-family: var(--font-sans); font-size: 25px; font-weight: 800; color: var(--c-wine-dark); margin: 0 0 10px 0;">
            Desviación por Semilla: 0.037
          </h3>
          <p style="font-family: var(--font-sans); font-size: 22px; color: #110103; font-weight: 600; line-height: 1.4; margin: 0;">
            La dispersión generada por cambiar la semilla aleatoria es <strong>18 veces mayor</strong> que la brecha neta entre modelos.
          </p>
        </div>
        <div style="margin-top: 14px; padding-top: 10px; border-top: 2px solid rgba(201,16,27,0.2); font-family: var(--font-sans); font-size: 21px; font-weight: 700; color: var(--c-red-accent);">
          El ranking se invierte según la semilla.
        </div>
      </div>

      <!-- Columna 3: El Veredicto de Wilcoxon -->
      <div style="background: #FAF5F5; border: 2.5px solid #8A5500; border-top: 8px solid #8A5500; padding: 24px 26px; display: flex; flex-direction: column; justify-content: space-between;">
        <div>
          <div style="font-family: var(--font-mono); font-size: 20px; font-weight: 800; color: #8A5500; letter-spacing: 0.5px; margin-bottom: 8px;">
            03 · VEREDICTO DE RIGOR
          </div>
          <div style="font-family: var(--font-sans); font-size: 64px; font-weight: 800; color: #8A5500; line-height: 1; margin-bottom: 12px;">
            p = 0.569
          </div>
          <h3 style="font-family: var(--font-sans); font-size: 25px; font-weight: 800; color: var(--c-wine-dark); margin: 0 0 10px 0;">
            Prueba de Rangos (W = 31.0)
          </h3>
          <p style="font-family: var(--font-sans); font-size: 22px; color: #110103; font-weight: 600; line-height: 1.4; margin: 0;">
            La prueba no paramétrica de Wilcoxon confirma un <strong>empate estadístico absoluto</strong>: ningún modelo es superior.
          </p>
        </div>
        <div style="margin-top: 14px; padding-top: 10px; border-top: 2px solid rgba(138,85,0,0.2); font-family: var(--font-sans); font-size: 21px; font-weight: 700; color: #8A5500;">
          Diferencia estadísticamente nula.
        </div>
      </div>

    </div>

    <!-- BANNER DE CIERRE METODOLÓGICO -->
    <div style="background: #FAF5F5; border: 2px solid var(--c-red-accent); border-left: 8px solid var(--c-red-accent); padding: 14px 22px; display: flex; justify-content: space-between; align-items: center;">
      <span style="font-family: var(--font-sans); font-size: 22px; font-weight: 800; color: var(--c-wine-dark);">
        ⚠️ REGLA PARA EVALUAR SLM: Prohibido declarar modelos ganadores mediante una única corrida sin control de varianza.
      </span>
      <span style="font-family: var(--font-mono); font-size: 20px; font-weight: 800; color: var(--c-red-accent); white-space: nowrap;">
        CONTROL ESTOCÁSTICO
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

# -----------------------------------------------------------------------------
# OPCIÓN C: Recreación Fiel de Figura 3 (Barras Horizontales Idénticas al Paper)
# -----------------------------------------------------------------------------
OPCION_C_HTML = '''
<section class="slide s-white active" id="slide-13-opt-c">
  <header class="slide-header">
    <div class="sh-left">
      <span class="sh-red-bar"></span>
      <span class="sh-category">03 · RESULTADOS · EL FALSO EMPATE ESTADÍSTICO</span>
    </div>
    <img src="assets/image6.png" alt="#LoxTIC" class="sh-loxtic">
  </header>
  <div class="sh-divider"></div>

  <div class="slide-content-area" style="justify-content: space-between; padding: 14px 0 6px 0;">
    
    <h2 class="s-lead-question" style="font-size: 38px; font-weight: 800; margin: 0; line-height: 1.2;">
      La ilusión del 0.795: la variación por semilla supera la diferencia entre modelos
    </h2>

    <div style="display: grid; grid-template-columns: 1.15fr 0.85fr; gap: 32px; flex: 1; margin: 16px 0; align-items: stretch;">
      
      <!-- HERO IZQUIERDO: Recreación de las 2 Barras Horizontales de la Fig 3 del Paper -->
      <div style="background: #FAF5F5; border: 2.5px solid var(--c-wine-primary); padding: 22px 26px; display: flex; flex-direction: column; justify-content: space-between;">
        <div>
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 16px;">
            <span style="font-family: var(--font-sans); font-size: 23px; font-weight: 800; color: var(--c-wine-dark);">
              FIGURA 3 DEL PAPER: RESUMEN DESCRIPTIVO
            </span>
            <span style="font-family: var(--font-mono); font-size: 20px; font-weight: 800; color: var(--c-wine-primary); background: #FFFFFF; border: 1.5px solid var(--c-wine-primary); padding: 2px 10px;">
              ESCALA REAL
            </span>
          </div>

          <!-- Barra 1 Horizontal: Desviación Estándar Intra-Modelo -->
          <div style="margin-bottom: 22px;">
            <div style="display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 6px;">
              <span style="font-family: var(--font-sans); font-size: 22px; font-weight: 800; color: var(--c-wine-dark);">
                Desviación intra-modelo por pregunta (ruido de semillas):
              </span>
              <span style="font-family: var(--font-mono); font-size: 32px; font-weight: 800; color: var(--c-red-accent);">
                0.037
              </span>
            </div>
            <div style="background: #EAE0E1; height: 38px; border: 1.5px solid #2C0509; width: 100%;">
              <div style="background: var(--c-red-accent); height: 100%; width: 100%; display: flex; align-items: center; padding-left: 14px; color: #FFFFFF; font-family: var(--font-sans); font-size: 20px; font-weight: 800;">
                RUIDO ESTOCÁSTICO DOMINANTE
              </div>
            </div>
          </div>

          <!-- Barra 2 Horizontal: Diferencia Inter-Modelo -->
          <div style="margin-bottom: 22px;">
            <div style="display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 6px;">
              <span style="font-family: var(--font-sans); font-size: 22px; font-weight: 800; color: var(--c-wine-dark);">
                Diferencia absoluta entre medias de modelos:
              </span>
              <span style="font-family: var(--font-mono); font-size: 32px; font-weight: 800; color: var(--c-wine-primary);">
                0.025
              </span>
            </div>
            <div style="background: #EAE0E1; height: 38px; border: 1.5px solid #2C0509; width: 100%;">
              <div style="background: var(--c-wine-primary); height: 100%; width: 67.5%; display: flex; align-items: center; padding-left: 14px; color: #FFFFFF; font-family: var(--font-sans); font-size: 20px; font-weight: 800;">
                SEPARACIÓN ENTRE MODELOS
              </div>
            </div>
          </div>

          <!-- Barra 3 Horizontal: Diferencia Neta Total -->
          <div>
            <div style="display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 6px;">
              <span style="font-family: var(--font-sans); font-size: 22px; font-weight: 800; color: var(--c-wine-dark);">
                Brecha neta global (Phi-4-mini frente a Qwen2.5-3B):
              </span>
              <span style="font-family: var(--font-mono); font-size: 32px; font-weight: 800; color: #8A5500;">
                0.002
              </span>
            </div>
            <div style="background: #EAE0E1; height: 38px; border: 1.5px solid #2C0509; width: 100%;">
              <div style="background: #B38600; height: 100%; width: 5.4%; min-width: 8px;"></div>
            </div>
          </div>

        </div>

        <div style="margin-top: 14px; background: #FFFFFF; border: 1.5px solid var(--c-wine-primary); padding: 12px 18px; font-family: var(--font-sans); font-size: 21px; color: #110103; font-weight: 700; line-height: 1.3;">
          La brecha global (0.002) representa apenas el <strong>5.4% de la varianza por semilla</strong>.
        </div>
      </div>

      <!-- DERECHA: 2 Tarjetas Robustas de Resultados -->
      <div style="display: flex; flex-direction: column; justify-content: space-between; gap: 20px;">
        
        <!-- Tarjeta 1: Wilcoxon -->
        <div style="background: #FAF5F5; border: 2.5px solid var(--c-red-accent); padding: 22px 26px; flex: 1; display: flex; flex-direction: column; justify-content: space-between;">
          <div>
            <div style="display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 6px;">
              <span style="font-family: var(--font-sans); font-size: 24px; font-weight: 800; color: var(--c-wine-dark);">
                Prueba no paramétrica de Wilcoxon
              </span>
              <span style="font-family: var(--font-mono); font-size: 24px; font-weight: 800; color: var(--c-red-accent);">
                p = 0.569
              </span>
            </div>
            <p style="font-family: var(--font-sans); font-size: 22px; color: #110103; font-weight: 600; line-height: 1.35; margin: 0;">
              Con estadístico <strong>W = 31.0</strong> y <strong>p > 0.05</strong>, se descarta cualquier diferencia estadísticamente detectable entre ambos modelos.
            </p>
          </div>
          <div style="margin-top: 10px; font-family: var(--font-sans); font-size: 21px; font-weight: 700; color: var(--c-red-accent);">
            ● Conclusión: Rendimiento formalmente indistinguible.
          </div>
        </div>

        <!-- Tarjeta 2: Varianza e Inversión -->
        <div style="background: #FAF5F5; border: 2.5px solid var(--c-wine-primary); padding: 22px 26px; flex: 1; display: flex; flex-direction: column; justify-content: space-between;">
          <div>
            <div style="display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 6px;">
              <span style="font-family: var(--font-sans); font-size: 24px; font-weight: 800; color: var(--c-wine-dark);">
                Dispersión por Semillas Aleatorias
              </span>
              <span style="font-family: var(--font-mono); font-size: 24px; font-weight: 800; color: var(--c-wine-primary);">
                18.5× Mayor
              </span>
            </div>
            <p style="font-family: var(--font-sans); font-size: 22px; color: #110103; font-weight: 600; line-height: 1.35; margin: 0;">
              El ranking entre Phi-4 y Qwen2.5 se invierte en función de la semilla estocástica: el ganador cambia por puro azar de muestreo.
            </p>
          </div>
          <div style="margin-top: 10px; font-family: var(--font-sans); font-size: 21px; font-weight: 700; color: var(--c-wine-primary);">
            ● Alerta: Una sola ejecución engaña al investigador.
          </div>
        </div>

      </div>

    </div>

    <!-- BANNER DE CIERRE METODOLÓGICO -->
    <div style="background: #FAF5F5; border: 2px solid var(--c-red-accent); border-left: 8px solid var(--c-red-accent); padding: 14px 22px; display: flex; justify-content: space-between; align-items: center;">
      <span style="font-family: var(--font-sans); font-size: 22px; font-weight: 800; color: var(--c-wine-dark);">
        ⚠️ REQUISITO CIENTÍFICO: Toda evaluación de modelos SLM en aula rural exige múltiples corridas con control de semillas.
      </span>
      <span style="font-family: var(--font-mono); font-size: 20px; font-weight: 800; color: var(--c-red-accent); white-space: nowrap;">
        4 SEMILLAS (42, 7, 123, 2026)
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
  <title>Test Slide 13 Options</title>
  <link rel="stylesheet" href="http://localhost:8085/styles.css?v=24">
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
        ('slide_13_opt_a.html', 'slide_13_opt_a.png', OPCION_A_HTML),
        ('slide_13_opt_b.html', 'slide_13_opt_b.png', OPCION_B_HTML),
        ('slide_13_opt_c.html', 'slide_13_opt_c.png', OPCION_C_HTML),
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
            page.wait_for_timeout(500)
            page.screenshot(path=png_path)
            print(f"Captured: {png_name}")

        browser.close()

if __name__ == '__main__':
    main()
