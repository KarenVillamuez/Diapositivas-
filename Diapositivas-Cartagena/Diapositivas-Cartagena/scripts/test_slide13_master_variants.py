# -*- coding: utf-8 -*-
"""
Generación de 3 variantes maestras para Slide 13 sin fallas visuales:
- Variante A (Contraste de Magnitud en Barras Verticales): 0.037 vs 0.025 vs 0.002 espaciadas perfectamente + 3 tarjetas K2.2.
- Variante B (Resumen Horizontal Proporcional de la Figura 3): Barras horizontales directas a escala + 3 tarjetas K2.2.
- Variante C (Dispersión Curricular Detallada G1-R2): Gráfica de puntos y bigotes de las 12 preguntas de la Figura 3 + 3 tarjetas K2.2.
"""
import os
from playwright.sync_api import sync_playwright

output_dir = r"C:\Users\ASUS\.gemini\antigravity-ide\brain\a6624504-511c-4b9d-bc9a-468e348bde40"
os.makedirs(output_dir, exist_ok=True)

# -----------------------------------------------------------------------------
# VARIANTE A: Contraste de Magnitud en Barras Verticales
# -----------------------------------------------------------------------------
VAR_A_HTML = '''
<section class="slide s-white active" id="slide-13-var-a">
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

    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 32px; flex: 1; align-items: stretch; margin: 16px 0;">
      
      <!-- HERO IZQUIERDO: Barras Verticales Espaciadas Perfectamente -->
      <div style="background: #FAF5F5; border: 2.5px solid var(--c-wine-primary); padding: 22px 26px; display: flex; flex-direction: column; justify-content: space-between;">
        <div>
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
            <span style="font-family: var(--font-sans); font-size: 23px; font-weight: 800; color: var(--c-wine-dark);">
              MAGNITUD DEL EFECTO: RUIDO VS. SEÑAL
            </span>
            <span style="font-family: var(--font-mono); font-size: 20px; font-weight: 800; color: var(--c-red-accent); background: #FFE4E6; border: 1.5px solid var(--c-red-accent); padding: 2px 10px;">
              FIGURA 3 DEL PAPER
            </span>
          </div>

          <svg viewBox="0 0 760 290" style="width: 100%; height: auto; font-family: var(--font-sans);">
            <!-- Líneas de escala -->
            <line x1="40" y1="35" x2="720" y2="35" stroke="#E2D6D8" stroke-dasharray="4,4" />
            <line x1="40" y1="125" x2="720" y2="125" stroke="#E2D6D8" stroke-dasharray="4,4" />
            <line x1="40" y1="215" x2="720" y2="215" stroke="#2C0509" stroke-width="2.5" />
            
            <!-- Barra 1: Varianza por Semilla (0.037) -->
            <rect x="80" y="45" width="150" height="170" fill="var(--c-wine-primary)" />
            <text x="155" y="30" font-size="34" font-weight="800" fill="var(--c-wine-primary)" text-anchor="middle">0.037</text>
            <text x="155" y="246" font-size="22" font-weight="800" fill="#110103" text-anchor="middle">Varianza Semillas</text>
            <text x="155" y="272" font-size="19" font-weight="600" fill="#5D4A4D" text-anchor="middle">Desviación estándar</text>

            <!-- Barra 2: Diferencia Inter-Modelos (0.025) -->
            <rect x="310" y="100" width="150" height="115" fill="var(--c-red-accent)" />
            <text x="385" y="85" font-size="34" font-weight="800" fill="var(--c-red-accent)" text-anchor="middle">0.025</text>
            <text x="385" y="246" font-size="22" font-weight="800" fill="#110103" text-anchor="middle">Diferencia Modelos</text>
            <text x="385" y="272" font-size="19" font-weight="600" fill="#5D4A4D" text-anchor="middle">Media absoluta</text>

            <!-- Barra 3: Brecha Neta (0.002) -->
            <rect x="540" y="206" width="150" height="9" fill="#B38600" />
            <text x="615" y="192" font-size="34" font-weight="800" fill="#B38600" text-anchor="middle">0.002</text>
            <text x="615" y="246" font-size="22" font-weight="800" fill="#110103" text-anchor="middle">Brecha Neta</text>
            <text x="615" y="272" font-size="19" font-weight="600" fill="#5D4A4D" text-anchor="middle">Phi vs. Qwen</text>
          </svg>
        </div>

        <div style="border-top: 2px solid rgba(70,8,17,0.25); padding-top: 12px; font-family: var(--font-sans); font-size: 22px; color: #110103; font-weight: 700; line-height: 1.35;">
          <strong style="color: var(--c-wine-primary);">Conclusión empírica:</strong> El ruido de las semillas (0.037) es <strong>18.5× mayor</strong> que la diferencia final entre modelos (0.002).
        </div>
      </div>

      <!-- DERECHA: 3 Tarjetas Horizontales K2.2 -->
      <div style="display: flex; flex-direction: column; justify-content: space-between; gap: 16px;">
        
        <!-- Tarjeta 1: La Brecha Neta -->
        <div style="background: #FAF5F5; border: 2.5px solid var(--c-wine-primary); display: flex; align-items: stretch; flex: 1;">
          <div style="flex: 0 0 200px; background: #FFFFFF; border-right: 2.5px solid var(--c-wine-primary); color: var(--c-wine-primary); font-family: var(--font-mono); font-size: 26px; font-weight: 800; display: flex; align-items: center; justify-content: center; text-align: center; padding: 10px;">
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
          <div style="flex: 0 0 200px; background: #FFFFFF; border-right: 2.5px solid var(--c-red-accent); color: var(--c-red-accent); font-family: var(--font-mono); font-size: 23px; font-weight: 800; display: flex; align-items: center; justify-content: center; text-align: center; padding: 10px; line-height: 1.2;">
            p = 0.569<br><span style="font-size: 19px; color: #555;">W = 31.0</span>
          </div>
          <div style="flex: 1; padding: 14px 20px; display: flex; flex-direction: column; justify-content: center;">
            <div style="font-family: var(--font-sans); font-size: 23px; font-weight: 800; color: var(--c-wine-dark); margin-bottom: 2px;">
              Prueba de Rangos de Wilcoxon
            </div>
            <div style="font-family: var(--font-sans); font-size: 21px; color: #110103; font-weight: 600; line-height: 1.3;">
              Al ser <strong>p > 0.05</strong>, se descarta cualquier superioridad estadísticamente significativa.
            </div>
          </div>
        </div>

        <!-- Tarjeta 3: Inversión de Ranking -->
        <div style="background: #FAF5F5; border: 2.5px solid #8A5500; display: flex; align-items: stretch; flex: 1;">
          <div style="flex: 0 0 200px; background: #FFFFFF; border-right: 2.5px solid #8A5500; color: #8A5500; font-family: var(--font-mono); font-size: 26px; font-weight: 800; display: flex; align-items: center; justify-content: center; text-align: center; padding: 10px;">
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

    <!-- BANNER DE ALERTA METODOLÓGICA -->
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
# VARIANTE B: Barras Horizontales Fieles al Paper + 3 Tarjetas Horizontales K2.2
# -----------------------------------------------------------------------------
VAR_B_HTML = '''
<section class="slide s-white active" id="slide-13-var-b">
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

    <div style="display: grid; grid-template-columns: 1.05fr 0.95fr; gap: 32px; flex: 1; margin: 16px 0; align-items: stretch;">
      
      <!-- HERO IZQUIERDO: Barras Horizontales Proporcionales -->
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

          <!-- Barra 1: Ruido Estocástico -->
          <div style="margin-bottom: 20px;">
            <div style="display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 6px;">
              <span style="font-family: var(--font-sans); font-size: 22px; font-weight: 800; color: var(--c-wine-dark);">
                Desviación intra-modelo por pregunta (semillas):
              </span>
              <span style="font-family: var(--font-mono); font-size: 32px; font-weight: 800; color: var(--c-red-accent);">
                0.037
              </span>
            </div>
            <div style="background: #EAE0E1; height: 38px; border: 2px solid #2C0509; width: 100%;">
              <div style="background: var(--c-red-accent); height: 100%; width: 100%; display: flex; align-items: center; padding-left: 14px; color: #FFFFFF; font-family: var(--font-sans); font-size: 20px; font-weight: 800;">
                RUIDO ESTOCÁSTICO DOMINANTE
              </div>
            </div>
          </div>

          <!-- Barra 2: Diferencia Inter-Modelo -->
          <div style="margin-bottom: 20px;">
            <div style="display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 6px;">
              <span style="font-family: var(--font-sans); font-size: 22px; font-weight: 800; color: var(--c-wine-dark);">
                Diferencia absoluta entre medias de modelos:
              </span>
              <span style="font-family: var(--font-mono); font-size: 32px; font-weight: 800; color: var(--c-wine-primary);">
                0.025
              </span>
            </div>
            <div style="background: #EAE0E1; height: 38px; border: 2px solid #2C0509; width: 100%;">
              <div style="background: var(--c-wine-primary); height: 100%; width: 67.5%; display: flex; align-items: center; padding-left: 14px; color: #FFFFFF; font-family: var(--font-sans); font-size: 20px; font-weight: 800;">
                SEPARACIÓN ENTRE MODELOS
              </div>
            </div>
          </div>

          <!-- Barra 3: Brecha Neta -->
          <div>
            <div style="display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 6px;">
              <span style="font-family: var(--font-sans); font-size: 22px; font-weight: 800; color: var(--c-wine-dark);">
                Brecha neta global (Phi-4 frente a Qwen2.5):
              </span>
              <span style="font-family: var(--font-mono); font-size: 32px; font-weight: 800; color: #8A5500;">
                0.002
              </span>
            </div>
            <div style="background: #EAE0E1; height: 38px; border: 2px solid #2C0509; width: 100%;">
              <div style="background: #B38600; height: 100%; width: 5.4%; min-width: 10px;"></div>
            </div>
          </div>
        </div>

        <div style="border-top: 2px solid rgba(70,8,17,0.25); padding-top: 12px; font-family: var(--font-sans); font-size: 22px; color: #110103; font-weight: 700; line-height: 1.35;">
          La brecha neta (0.002) representa apenas el <strong>5.4% de la varianza por semilla</strong>.
        </div>
      </div>

      <!-- DERECHA: 3 Tarjetas Horizontales K2.2 -->
      <div style="display: flex; flex-direction: column; justify-content: space-between; gap: 16px;">
        
        <div style="background: #FAF5F5; border: 2.5px solid var(--c-wine-primary); display: flex; align-items: stretch; flex: 1;">
          <div style="flex: 0 0 190px; background: #FFFFFF; border-right: 2.5px solid var(--c-wine-primary); color: var(--c-wine-primary); font-family: var(--font-mono); font-size: 26px; font-weight: 800; display: flex; align-items: center; justify-content: center; text-align: center; padding: 10px;">
            Δ = 0.002
          </div>
          <div style="flex: 1; padding: 14px 20px; display: flex; flex-direction: column; justify-content: center;">
            <div style="font-family: var(--font-sans); font-size: 23px; font-weight: 800; color: var(--c-wine-dark); margin-bottom: 2px;">
              Promedio General: 0.8030 vs. 0.8010
            </div>
            <div style="font-family: var(--font-sans); font-size: 21px; color: #110103; font-weight: 600; line-height: 1.3;">
              Phi-4-mini y Qwen2.5-3B empatan con solo 2 milésimas de diferencia media.
            </div>
          </div>
        </div>

        <div style="background: #FAF5F5; border: 2.5px solid var(--c-red-accent); display: flex; align-items: stretch; flex: 1;">
          <div style="flex: 0 0 190px; background: #FFFFFF; border-right: 2.5px solid var(--c-red-accent); color: var(--c-red-accent); font-family: var(--font-mono); font-size: 23px; font-weight: 800; display: flex; align-items: center; justify-content: center; text-align: center; padding: 10px; line-height: 1.2;">
            p = 0.569<br><span style="font-size: 19px; color: #555;">W = 31.0</span>
          </div>
          <div style="flex: 1; padding: 14px 20px; display: flex; flex-direction: column; justify-content: center;">
            <div style="font-family: var(--font-sans); font-size: 23px; font-weight: 800; color: var(--c-wine-dark); margin-bottom: 2px;">
              Prueba de Rangos de Wilcoxon
            </div>
            <div style="font-family: var(--font-sans); font-size: 21px; color: #110103; font-weight: 600; line-height: 1.3;">
              Al ser <strong>p > 0.05</strong>, se descarta cualquier superioridad estadísticamente medible.
            </div>
          </div>
        </div>

        <div style="background: #FAF5F5; border: 2.5px solid #8A5500; display: flex; align-items: stretch; flex: 1;">
          <div style="flex: 0 0 190px; background: #FFFFFF; border-right: 2.5px solid #8A5500; color: #8A5500; font-family: var(--font-mono); font-size: 26px; font-weight: 800; display: flex; align-items: center; justify-content: center; text-align: center; padding: 10px;">
            18.5×
          </div>
          <div style="flex: 1; padding: 14px 20px; display: flex; flex-direction: column; justify-content: center;">
            <div style="font-family: var(--font-sans); font-size: 23px; font-weight: 800; color: var(--c-wine-dark); margin-bottom: 2px;">
              Inversión del Ganador por Semilla
            </div>
            <div style="font-family: var(--font-sans); font-size: 21px; color: #110103; font-weight: 600; line-height: 1.3;">
              El modelo que gana en la semilla 42 pierde en la semilla 7: <strong>el azar define el podio</strong>.
            </div>
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

# -----------------------------------------------------------------------------
# VARIANTE C: Dispersión Curricular Detallada G1-R2 (Puntos y Bigotes)
# -----------------------------------------------------------------------------
VAR_C_HTML = '''
<section class="slide s-white active" id="slide-13-var-c">
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

    <div style="display: grid; grid-template-columns: 1.12fr 0.88fr; gap: 32px; flex: 1; margin: 16px 0; align-items: stretch;">
      
      <!-- HERO IZQUIERDO: Gráfico de Dispersión y Solapamiento por Pregunta -->
      <div style="background: #FAF5F5; border: 2.5px solid var(--c-wine-primary); padding: 20px 24px; display: flex; flex-direction: column; justify-content: space-between;">
        <div>
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
            <span style="font-family: var(--font-sans); font-size: 22px; font-weight: 800; color: var(--c-wine-dark);">
              SOLAPAMIENTO Y DISPERSIÓN POR PREGUNTA
            </span>
            <div style="display: flex; gap: 16px; font-family: var(--font-sans); font-size: 20px; font-weight: 800;">
              <span style="color: var(--c-wine-primary);">● Phi-4-mini</span>
              <span style="color: var(--c-red-accent);">● Qwen2.5-3B</span>
            </div>
          </div>

          <svg viewBox="0 0 760 290" style="width: 100%; height: auto; font-family: var(--font-sans);">
            <!-- Eje Y con etiquetas nítidas y separadas -->
            <line x1="75" y1="20" x2="730" y2="20" stroke="#E2D6D8" stroke-dasharray="3,3" />
            <text x="35" y="26" font-size="18" fill="#5D4A4D" font-weight="700">0.90</text>
            
            <line x1="75" y1="90" x2="730" y2="90" stroke="#E2D6D8" stroke-dasharray="3,3" />
            <text x="35" y="96" font-size="18" fill="#5D4A4D" font-weight="700">0.80</text>

            <line x1="75" y1="160" x2="730" y2="160" stroke="#E2D6D8" stroke-dasharray="3,3" />
            <text x="35" y="166" font-size="18" fill="#5D4A4D" font-weight="700">0.70</text>

            <line x1="75" y1="230" x2="730" y2="230" stroke="#2C0509" stroke-width="2.5" />
            <text x="35" y="236" font-size="18" fill="#5D4A4D" font-weight="700">0.60</text>

            <!-- 12 Pares de Preguntas Curriculares con Barras de Dispersión Solapadas -->
            <!-- G1 -->
            <line x1="110" y1="85" x2="110" y2="120" stroke="var(--c-wine-primary)" stroke-width="4.5" />
            <circle cx="110" cy="102" r="7" fill="var(--c-wine-primary)" />
            <line x1="124" y1="90" x2="124" y2="125" stroke="var(--c-red-accent)" stroke-width="4.5" />
            <circle cx="124" cy="106" r="7" fill="var(--c-red-accent)" />
            <text x="117" y="258" font-size="18" font-weight="800" fill="#2C0509" text-anchor="middle">G1</text>

            <!-- G2 (Alta Varianza) -->
            <line x1="162" y1="40" x2="162" y2="145" stroke="var(--c-wine-primary)" stroke-width="4.5" />
            <circle cx="162" cy="88" r="7" fill="var(--c-wine-primary)" />
            <line x1="176" y1="65" x2="176" y2="210" stroke="var(--c-red-accent)" stroke-width="4.5" />
            <circle cx="176" cy="135" r="7" fill="var(--c-red-accent)" />
            <text x="169" y="258" font-size="18" font-weight="800" fill="#2C0509" text-anchor="middle">G2</text>

            <!-- G3 -->
            <line x1="214" y1="50" x2="214" y2="70" stroke="var(--c-wine-primary)" stroke-width="4.5" />
            <circle cx="214" cy="58" r="7" fill="var(--c-wine-primary)" />
            <line x1="228" y1="60" x2="228" y2="130" stroke="var(--c-red-accent)" stroke-width="4.5" />
            <circle cx="228" cy="85" r="7" fill="var(--c-red-accent)" />
            <text x="221" y="258" font-size="18" font-weight="800" fill="#2C0509" text-anchor="middle">G3</text>

            <!-- G4 -->
            <line x1="266" y1="55" x2="266" y2="85" stroke="var(--c-wine-primary)" stroke-width="4.5" />
            <circle cx="266" cy="68" r="7" fill="var(--c-wine-primary)" />
            <line x1="280" y1="65" x2="280" y2="115" stroke="var(--c-red-accent)" stroke-width="4.5" />
            <circle cx="280" cy="80" r="7" fill="var(--c-red-accent)" />
            <text x="273" y="258" font-size="18" font-weight="800" fill="#2C0509" text-anchor="middle">G4</text>

            <!-- V1 -->
            <line x1="318" y1="110" x2="318" y2="185" stroke="var(--c-wine-primary)" stroke-width="4.5" />
            <circle cx="318" cy="145" r="7" fill="var(--c-wine-primary)" />
            <circle cx="332" cy="90" r="7" fill="var(--c-red-accent)" />
            <text x="325" y="258" font-size="18" font-weight="800" fill="#2C0509" text-anchor="middle">V1</text>

            <!-- V2 -->
            <line x1="370" y1="75" x2="370" y2="125" stroke="var(--c-wine-primary)" stroke-width="4.5" />
            <circle cx="370" cy="92" r="7" fill="var(--c-wine-primary)" />
            <line x1="384" y1="80" x2="384" y2="120" stroke="var(--c-red-accent)" stroke-width="4.5" />
            <circle cx="384" cy="95" r="7" fill="var(--c-red-accent)" />
            <text x="377" y="258" font-size="18" font-weight="800" fill="#2C0509" text-anchor="middle">V2</text>

            <!-- V3 -->
            <line x1="422" y1="85" x2="422" y2="140" stroke="var(--c-wine-primary)" stroke-width="4.5" />
            <circle cx="422" cy="110" r="7" fill="var(--c-wine-primary)" />
            <line x1="436" y1="80" x2="436" y2="160" stroke="var(--c-red-accent)" stroke-width="4.5" />
            <circle cx="436" cy="115" r="7" fill="var(--c-red-accent)" />
            <text x="429" y="258" font-size="18" font-weight="800" fill="#2C0509" text-anchor="middle">V3</text>

            <!-- W1 (Alta Varianza) -->
            <line x1="474" y1="30" x2="474" y2="175" stroke="var(--c-wine-primary)" stroke-width="4.5" />
            <circle cx="474" cy="95" r="7" fill="var(--c-wine-primary)" />
            <line x1="488" y1="60" x2="488" y2="110" stroke="var(--c-red-accent)" stroke-width="4.5" />
            <circle cx="488" cy="78" r="7" fill="var(--c-red-accent)" />
            <text x="481" y="258" font-size="18" font-weight="800" fill="#2C0509" text-anchor="middle">W1</text>

            <!-- W2 -->
            <line x1="526" y1="40" x2="526" y2="95" stroke="var(--c-wine-primary)" stroke-width="4.5" />
            <circle cx="526" cy="65" r="7" fill="var(--c-wine-primary)" />
            <line x1="540" y1="50" x2="540" y2="105" stroke="var(--c-red-accent)" stroke-width="4.5" />
            <circle cx="540" cy="72" r="7" fill="var(--c-red-accent)" />
            <text x="533" y="258" font-size="18" font-weight="800" fill="#2C0509" text-anchor="middle">W2</text>

            <!-- W3 -->
            <line x1="578" y1="80" x2="578" y2="115" stroke="var(--c-wine-primary)" stroke-width="4.5" />
            <circle cx="578" cy="94" r="7" fill="var(--c-wine-primary)" />
            <line x1="592" y1="50" x2="592" y2="155" stroke="var(--c-red-accent)" stroke-width="4.5" />
            <circle cx="592" cy="90" r="7" fill="var(--c-red-accent)" />
            <text x="585" y="258" font-size="18" font-weight="800" fill="#2C0509" text-anchor="middle">W3</text>

            <!-- R1 -->
            <line x1="630" y1="75" x2="630" y2="95" stroke="var(--c-wine-primary)" stroke-width="4.5" />
            <circle cx="630" cy="85" r="7" fill="var(--c-wine-primary)" />
            <line x1="644" y1="80" x2="644" y2="100" stroke="var(--c-red-accent)" stroke-width="4.5" />
            <circle cx="644" cy="92" r="7" fill="var(--c-red-accent)" />
            <text x="637" y="258" font-size="18" font-weight="800" fill="#2C0509" text-anchor="middle">R1</text>

            <!-- R2 -->
            <line x1="682" y1="105" x2="682" y2="135" stroke="var(--c-wine-primary)" stroke-width="4.5" />
            <circle cx="682" cy="120" r="7" fill="var(--c-wine-primary)" />
            <line x1="696" y1="60" x2="696" y2="215" stroke="var(--c-red-accent)" stroke-width="4.5" />
            <circle cx="696" cy="125" r="7" fill="var(--c-red-accent)" />
            <text x="689" y="258" font-size="18" font-weight="800" fill="#2C0509" text-anchor="middle">R2</text>
          </svg>
        </div>

        <div style="border-top: 2px solid rgba(70,8,17,0.25); padding-top: 10px; font-family: var(--font-sans); font-size: 21px; color: #110103; font-weight: 700; line-height: 1.3;">
          Las barras de dispersión se cruzan y solapan en casi todas las preguntas: no existe superioridad detectable.
        </div>
      </div>

      <!-- DERECHA: 3 Tarjetas Horizontales K2.2 -->
      <div style="display: flex; flex-direction: column; justify-content: space-between; gap: 16px;">
        
        <div style="background: #FAF5F5; border: 2.5px solid var(--c-wine-primary); display: flex; align-items: stretch; flex: 1;">
          <div style="flex: 0 0 190px; background: #FFFFFF; border-right: 2.5px solid var(--c-wine-primary); color: var(--c-wine-primary); font-family: var(--font-mono); font-size: 26px; font-weight: 800; display: flex; align-items: center; justify-content: center; text-align: center; padding: 10px;">
            Δ = 0.002
          </div>
          <div style="flex: 1; padding: 14px 20px; display: flex; flex-direction: column; justify-content: center;">
            <div style="font-family: var(--font-sans); font-size: 23px; font-weight: 800; color: var(--c-wine-dark); margin-bottom: 2px;">
              Promedio General (4 Semillas)
            </div>
            <div style="font-family: var(--font-sans); font-size: 21px; color: #110103; font-weight: 600; line-height: 1.3;">
              0.8030 (Phi-4-mini) frente a 0.8010 (Qwen2.5-3B).
            </div>
          </div>
        </div>

        <div style="background: #FAF5F5; border: 2.5px solid var(--c-red-accent); display: flex; align-items: stretch; flex: 1;">
          <div style="flex: 0 0 190px; background: #FFFFFF; border-right: 2.5px solid var(--c-red-accent); color: var(--c-red-accent); font-family: var(--font-mono); font-size: 23px; font-weight: 800; display: flex; align-items: center; justify-content: center; text-align: center; padding: 10px; line-height: 1.2;">
            p = 0.569<br><span style="font-size: 19px; color: #555;">W = 31.0</span>
          </div>
          <div style="flex: 1; padding: 14px 20px; display: flex; flex-direction: column; justify-content: center;">
            <div style="font-family: var(--font-sans); font-size: 23px; font-weight: 800; color: var(--c-wine-dark); margin-bottom: 2px;">
              Prueba de Wilcoxon
            </div>
            <div style="font-family: var(--font-sans); font-size: 21px; color: #110103; font-weight: 600; line-height: 1.3;">
              Al ser <strong>p > 0.05</strong>, se confirma empate estadístico formal.
            </div>
          </div>
        </div>

        <div style="background: #FAF5F5; border: 2.5px solid var(--c-red-accent); display: flex; align-items: stretch; flex: 1;">
          <div style="flex: 0 0 190px; background: #FFFFFF; border-right: 2.5px solid var(--c-red-accent); color: var(--c-red-accent); font-family: var(--font-mono); font-size: 26px; font-weight: 800; display: flex; align-items: center; justify-content: center; text-align: center; padding: 10px;">
            18.5×
          </div>
          <div style="flex: 1; padding: 14px 20px; display: flex; flex-direction: column; justify-content: center;">
            <div style="font-family: var(--font-sans); font-size: 23px; font-weight: 800; color: var(--c-wine-dark); margin-bottom: 2px;">
              Varianza vs. Diferencia
            </div>
            <div style="font-family: var(--font-sans); font-size: 21px; color: #110103; font-weight: 600; line-height: 1.3;">
              La semilla estocástica explica 18.5 veces más variación que el modelo.
            </div>
          </div>
        </div>

      </div>

    </div>

    <!-- BANNER DE CIERRE METODOLÓGICO -->
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

HTML_WRAPPER = '''<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Test Slide 13 Master Variants</title>
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
        ('slide_13_var_a.html', 'slide_13_var_a.png', VAR_A_HTML),
        ('slide_13_var_b.html', 'slide_13_var_b.png', VAR_B_HTML),
        ('slide_13_var_c.html', 'slide_13_var_c.png', VAR_C_HTML),
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
