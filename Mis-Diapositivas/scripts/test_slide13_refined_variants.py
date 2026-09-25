# -*- coding: utf-8 -*-
"""
Generación de 3 variantes refinadas para Slide 13 (El Falso Empate de 0.795):
- Variante A1: Hero Gráfico de Magnitud Vertical (0.037 vs 0.025 vs 0.002) corregido sin colisiones de texto ni cajas anidadas + 3 tarjetas horizontales K2.2.
- Variante A2: Recreación de las Barras Horizontales de la Figura 3 del paper (0.037 vs 0.025 vs 0.002) + 2 tarjetas de gran formato a la derecha.
- Variante A3: Gráfica de dispersión por preguntas de la Figura 3 (G1-R2) reconstruida en SVG vectorial limpio + panel de auditoría estadística.
"""
import os
from playwright.sync_api import sync_playwright

output_dir = r"C:\Users\ASUS\.gemini\antigravity-ide\brain\a6624504-511c-4b9d-bc9a-468e348bde40"
os.makedirs(output_dir, exist_ok=True)

# -----------------------------------------------------------------------------
# VARIANTE A1: Hero Gráfico Vertical Limpio + 3 Tarjetas Horizontales K2.2
# -----------------------------------------------------------------------------
A1_HTML = '''
<section class="slide s-white active" id="slide-13-a1">
  <header class="slide-header">
    <div class="sh-left">
      <span class="sh-red-bar"></span>
      <span class="sh-category">03 · RESULTADOS · EL FALSO EMPATE ESTADÍSTICO</span>
    </div>
    <img src="assets/image6.png" alt="#LoxTIC" class="sh-loxtic">
  </header>
  <div class="sh-divider"></div>

  <div class="slide-content-area" style="justify-content: space-between; padding: 14px 0 6px 0;">
    
    <!-- Título Principal -->
    <h2 class="s-lead-question" style="font-size: 38px; font-weight: 800; margin: 0; line-height: 1.2;">
      La ilusión del 0.795: la variación por semilla supera la diferencia entre modelos
    </h2>

    <!-- GRID PRINCIPAL: 2 Columnas Equilibradas -->
    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 32px; flex: 1; align-items: stretch; margin: 16px 0;">
      
      <!-- HERO IZQUIERDO: Gráfico de Magnitud (Sin cuadros anidados) -->
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

          <!-- SVG Rediseñado con Espaciado Generoso y Cero Colisiones -->
          <svg viewBox="0 0 760 300" style="width: 100%; height: auto; font-family: var(--font-sans);">
            <!-- Líneas de escala -->
            <line x1="50" y1="35" x2="720" y2="35" stroke="#E2D6D8" stroke-dasharray="4,4" />
            <line x1="50" y1="125" x2="720" y2="125" stroke="#E2D6D8" stroke-dasharray="4,4" />
            <line x1="50" y1="215" x2="720" y2="215" stroke="#2C0509" stroke-width="2.5" />
            
            <!-- Barra 1: Varianza por Semilla (0.037) -->
            <rect x="110" y="45" width="140" height="170" fill="var(--c-wine-primary)" />
            <text x="180" y="32" font-size="32" font-weight="800" fill="var(--c-wine-primary)" text-anchor="middle">0.037</text>
            <text x="180" y="246" font-size="22" font-weight="800" fill="#110103" text-anchor="middle">Varianza Semillas</text>
            <text x="180" y="272" font-size="19" font-weight="600" fill="#5D4A4D" text-anchor="middle">Desviación estándar</text>

            <!-- Barra 2: Diferencia Inter-Modelos (0.025) -->
            <rect x="320" y="100" width="140" height="115" fill="var(--c-red-accent)" />
            <text x="390" y="87" font-size="32" font-weight="800" fill="var(--c-red-accent)" text-anchor="middle">0.025</text>
            <text x="390" y="246" font-size="22" font-weight="800" fill="#110103" text-anchor="middle">Diferencia Modelos</text>
            <text x="390" y="272" font-size="19" font-weight="600" fill="#5D4A4D" text-anchor="middle">Media absoluta</text>

            <!-- Barra 3: Brecha Neta (0.002) -->
            <rect x="530" y="206" width="140" height="9" fill="#B38600" />
            <text x="600" y="194" font-size="32" font-weight="800" fill="#B38600" text-anchor="middle">0.002</text>
            <text x="600" y="246" font-size="22" font-weight="800" fill="#110103" text-anchor="middle">Brecha Neta</text>
            <text x="600" y="272" font-size="19" font-weight="600" fill="#5D4A4D" text-anchor="middle">Phi vs. Qwen</text>
          </svg>
        </div>

        <!-- Conclusión sin caja anidada -->
        <div style="border-top: 2px solid rgba(70,8,17,0.25); padding-top: 12px; font-family: var(--font-sans); font-size: 22px; color: #110103; font-weight: 700; line-height: 1.35;">
          <strong style="color: var(--c-wine-primary);">Conclusión empírica:</strong> El ruido de las semillas (0.037) es <strong>18.5× mayor</strong> que la diferencia final entre modelos (0.002).
        </div>

      </div>

      <!-- DERECHA: 3 Tarjetas con la Estructura Horizontal Limpia de K2.2 -->
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

    <!-- BANNER DE ALERTA METODOLÓGICA (100% Plano) -->
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
# VARIANTE A2: Recreación de las Barras Horizontales de la Figura 3 del Paper
# -----------------------------------------------------------------------------
A2_HTML = '''
<section class="slide s-white active" id="slide-13-a2">
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
      
      <!-- HERO IZQUIERDO: Barras Horizontales Fieles al Paper (Sin cajas dentro de cajas) -->
      <div style="background: #FAF5F5; border: 2.5px solid var(--c-wine-primary); padding: 22px 26px; display: flex; flex-direction: column; justify-content: space-between;">
        <div>
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 20px;">
            <span style="font-family: var(--font-sans); font-size: 23px; font-weight: 800; color: var(--c-wine-dark);">
              FIGURA 3 DEL PAPER: RESUMEN DESCRIPTIVO
            </span>
            <span style="font-family: var(--font-mono); font-size: 20px; font-weight: 800; color: var(--c-wine-primary); background: #FFFFFF; border: 1.5px solid var(--c-wine-primary); padding: 2px 10px;">
              ESCALA REAL
            </span>
          </div>

          <!-- Barra 1: Ruido Estocástico -->
          <div style="margin-bottom: 24px;">
            <div style="display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 6px;">
              <span style="font-family: var(--font-sans); font-size: 22px; font-weight: 800; color: var(--c-wine-dark);">
                Desviación intra-modelo por pregunta (ruido de semillas):
              </span>
              <span style="font-family: var(--font-mono); font-size: 34px; font-weight: 800; color: var(--c-red-accent);">
                0.037
              </span>
            </div>
            <div style="background: #EAE0E1; height: 42px; border: 2px solid #2C0509; width: 100%;">
              <div style="background: var(--c-red-accent); height: 100%; width: 100%; display: flex; align-items: center; padding-left: 14px; color: #FFFFFF; font-family: var(--font-sans); font-size: 21px; font-weight: 800; letter-spacing: 0.5px;">
                RUIDO ESTOCÁSTICO DOMINANTE
              </div>
            </div>
          </div>

          <!-- Barra 2: Diferencia Inter-Modelo -->
          <div style="margin-bottom: 24px;">
            <div style="display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 6px;">
              <span style="font-family: var(--font-sans); font-size: 22px; font-weight: 800; color: var(--c-wine-dark);">
                Diferencia absoluta entre medias de modelos:
              </span>
              <span style="font-family: var(--font-mono); font-size: 34px; font-weight: 800; color: var(--c-wine-primary);">
                0.025
              </span>
            </div>
            <div style="background: #EAE0E1; height: 42px; border: 2px solid #2C0509; width: 100%;">
              <div style="background: var(--c-wine-primary); height: 100%; width: 67.5%; display: flex; align-items: center; padding-left: 14px; color: #FFFFFF; font-family: var(--font-sans); font-size: 21px; font-weight: 800; letter-spacing: 0.5px;">
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
              <span style="font-family: var(--font-mono); font-size: 34px; font-weight: 800; color: #8A5500;">
                0.002
              </span>
            </div>
            <div style="background: #EAE0E1; height: 42px; border: 2px solid #2C0509; width: 100%;">
              <div style="background: #B38600; height: 100%; width: 5.4%; min-width: 10px;"></div>
            </div>
          </div>
        </div>

        <div style="border-top: 2px solid rgba(70,8,17,0.25); padding-top: 12px; font-family: var(--font-sans); font-size: 22px; color: #110103; font-weight: 700; line-height: 1.35;">
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
            ● Alerta: Una sola corrida engaña al investigador.
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
# VARIANTE A3: Dispersión Vectorial por Preguntas (G1 a R2) Reconstruida
# -----------------------------------------------------------------------------
A3_HTML = '''
<section class="slide s-white active" id="slide-13-a3">
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
      
      <!-- HERO IZQUIERDO: Gráfico de Dispersión y Solapamiento por Pregunta -->
      <div style="background: #FAF5F5; border: 2.5px solid var(--c-wine-primary); padding: 20px 24px; display: flex; flex-direction: column; justify-content: space-between;">
        <div>
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
            <span style="font-family: var(--font-sans); font-size: 22px; font-weight: 800; color: var(--c-wine-dark);">
              SOLAPAMIENTO Y DISPERSIÓN POR PREGUNTA
            </span>
            <div style="display: flex; gap: 14px; font-family: var(--font-sans); font-size: 19px; font-weight: 700;">
              <span style="color: var(--c-wine-primary);">● Phi-4-mini</span>
              <span style="color: var(--c-red-accent);">● Qwen2.5-3B</span>
            </div>
          </div>

          <!-- SVG Visualizando el Rango de Variación por Preguntas (G1-G4, V1-V3, W1-W3, R1-R2) -->
          <svg viewBox="0 0 760 290" style="width: 100%; height: auto; font-family: var(--font-sans);">
            <!-- Eje Y -->
            <line x1="60" y1="20" x2="720" y2="20" stroke="#E2D6D8" stroke-dasharray="3,3" />
            <text x="45" y="25" font-size="16" fill="#8D7A7D" font-weight="700">0.90</text>
            
            <line x1="60" y1="90" x2="720" y2="90" stroke="#E2D6D8" stroke-dasharray="3,3" />
            <text x="45" y="95" font-size="16" fill="#8D7A7D" font-weight="700">0.80</text>

            <line x1="60" y1="160" x2="720" y2="160" stroke="#E2D6D8" stroke-dasharray="3,3" />
            <text x="45" y="165" font-size="16" fill="#8D7A7D" font-weight="700">0.70</text>

            <line x1="60" y1="230" x2="720" y2="230" stroke="#2C0509" stroke-width="2" />
            <text x="45" y="235" font-size="16" fill="#8D7A7D" font-weight="700">0.60</text>

            <!-- 12 Pares de Preguntas Curriculares con Barras de Dispersión Solapadas -->
            <!-- G1 -->
            <line x1="100" y1="85" x2="100" y2="120" stroke="var(--c-wine-primary)" stroke-width="4" />
            <circle cx="100" cy="102" r="6" fill="var(--c-wine-primary)" />
            <line x1="112" y1="90" x2="112" y2="125" stroke="var(--c-red-accent)" stroke-width="4" />
            <circle cx="112" cy="106" r="6" fill="var(--c-red-accent)" />
            <text x="106" y="255" font-size="17" font-weight="700" fill="#2C0509" text-anchor="middle">G1</text>

            <!-- G2 (Alta Varianza) -->
            <line x1="155" y1="40" x2="155" y2="145" stroke="var(--c-wine-primary)" stroke-width="4" />
            <circle cx="155" cy="88" r="6" fill="var(--c-wine-primary)" />
            <line x1="167" y1="65" x2="167" y2="210" stroke="var(--c-red-accent)" stroke-width="4" />
            <circle cx="167" cy="135" r="6" fill="var(--c-red-accent)" />
            <text x="161" y="255" font-size="17" font-weight="700" fill="#2C0509" text-anchor="middle">G2</text>

            <!-- G3 -->
            <line x1="210" y1="50" x2="210" y2="70" stroke="var(--c-wine-primary)" stroke-width="4" />
            <circle cx="210" cy="58" r="6" fill="var(--c-wine-primary)" />
            <line x1="222" y1="60" x2="222" y2="130" stroke="var(--c-red-accent)" stroke-width="4" />
            <circle cx="222" cy="85" r="6" fill="var(--c-red-accent)" />
            <text x="216" y="255" font-size="17" font-weight="700" fill="#2C0509" text-anchor="middle">G3</text>

            <!-- G4 -->
            <line x1="265" y1="55" x2="265" y2="85" stroke="var(--c-wine-primary)" stroke-width="4" />
            <circle cx="265" cy="68" r="6" fill="var(--c-wine-primary)" />
            <line x1="277" y1="65" x2="277" y2="115" stroke="var(--c-red-accent)" stroke-width="4" />
            <circle cx="277" cy="80" r="6" fill="var(--c-red-accent)" />
            <text x="271" y="255" font-size="17" font-weight="700" fill="#2C0509" text-anchor="middle">G4</text>

            <!-- V1 -->
            <line x1="320" y1="110" x2="320" y2="185" stroke="var(--c-wine-primary)" stroke-width="4" />
            <circle cx="320" cy="145" r="6" fill="var(--c-wine-primary)" />
            <circle cx="332" cy="90" r="6" fill="var(--c-red-accent)" />
            <text x="326" y="255" font-size="17" font-weight="700" fill="#2C0509" text-anchor="middle">V1</text>

            <!-- V2 -->
            <line x1="375" y1="75" x2="375" y2="125" stroke="var(--c-wine-primary)" stroke-width="4" />
            <circle cx="375" cy="92" r="6" fill="var(--c-wine-primary)" />
            <line x1="387" y1="80" x2="387" y2="120" stroke="var(--c-red-accent)" stroke-width="4" />
            <circle cx="387" cy="95" r="6" fill="var(--c-red-accent)" />
            <text x="381" y="255" font-size="17" font-weight="700" fill="#2C0509" text-anchor="middle">V2</text>

            <!-- V3 -->
            <line x1="430" y1="85" x2="430" y2="140" stroke="var(--c-wine-primary)" stroke-width="4" />
            <circle cx="430" cy="110" r="6" fill="var(--c-wine-primary)" />
            <line x1="442" y1="80" x2="442" y2="160" stroke="var(--c-red-accent)" stroke-width="4" />
            <circle cx="442" cy="115" r="6" fill="var(--c-red-accent)" />
            <text x="436" y="255" font-size="17" font-weight="700" fill="#2C0509" text-anchor="middle">V3</text>

            <!-- W1 (Varianza Máxima) -->
            <line x1="485" y1="30" x2="485" y2="175" stroke="var(--c-wine-primary)" stroke-width="4" />
            <circle cx="485" cy="95" r="6" fill="var(--c-wine-primary)" />
            <line x1="497" y1="60" x2="497" y2="110" stroke="var(--c-red-accent)" stroke-width="4" />
            <circle cx="497" cy="78" r="6" fill="var(--c-red-accent)" />
            <text x="491" y="255" font-size="17" font-weight="700" fill="#2C0509" text-anchor="middle">W1</text>

            <!-- W2 -->
            <line x1="540" y1="40" x2="540" y2="95" stroke="var(--c-wine-primary)" stroke-width="4" />
            <circle cx="540" cy="65" r="6" fill="var(--c-wine-primary)" />
            <line x1="552" y1="50" x2="552" y2="105" stroke="var(--c-red-accent)" stroke-width="4" />
            <circle cx="552" cy="72" r="6" fill="var(--c-red-accent)" />
            <text x="546" y="255" font-size="17" font-weight="700" fill="#2C0509" text-anchor="middle">W2</text>

            <!-- W3 -->
            <line x1="595" y1="80" x2="595" y2="115" stroke="var(--c-wine-primary)" stroke-width="4" />
            <circle cx="595" cy="94" r="6" fill="var(--c-wine-primary)" />
            <line x1="607" y1="50" x2="607" y2="155" stroke="var(--c-red-accent)" stroke-width="4" />
            <circle cx="607" cy="90" r="6" fill="var(--c-red-accent)" />
            <text x="601" y="255" font-size="17" font-weight="700" fill="#2C0509" text-anchor="middle">W3</text>

            <!-- R1 -->
            <line x1="650" y1="75" x2="650" y2="95" stroke="var(--c-wine-primary)" stroke-width="4" />
            <circle cx="650" cy="85" r="6" fill="var(--c-wine-primary)" />
            <line x1="662" y1="80" x2="662" y2="100" stroke="var(--c-red-accent)" stroke-width="4" />
            <circle cx="662" cy="92" r="6" fill="var(--c-red-accent)" />
            <text x="656" y="255" font-size="17" font-weight="700" fill="#2C0509" text-anchor="middle">R1</text>

            <!-- R2 -->
            <line x1="705" y1="105" x2="705" y2="135" stroke="var(--c-wine-primary)" stroke-width="4" />
            <circle cx="705" cy="120" r="6" fill="var(--c-wine-primary)" />
            <line x1="717" y1="60" x2="717" y2="215" stroke="var(--c-red-accent)" stroke-width="4" />
            <circle cx="717" cy="125" r="6" fill="var(--c-red-accent)" />
            <text x="711" y="255" font-size="17" font-weight="700" fill="#2C0509" text-anchor="middle">R2</text>
          </svg>
        </div>

        <div style="border-top: 2px solid rgba(70,8,17,0.25); padding-top: 10px; font-family: var(--font-sans); font-size: 21px; color: #110103; font-weight: 700; line-height: 1.3;">
          Las barras de dispersión se cruzan y solapan en casi todas las preguntas: no existe superioridad detectable.
        </div>
      </div>

      <!-- DERECHA: 3 Tarjetas de Resumen Estadístico -->
      <div style="display: flex; flex-direction: column; justify-content: space-between; gap: 16px;">
        
        <div style="background: #FAF5F5; border: 2.5px solid var(--c-wine-primary); display: flex; align-items: stretch; flex: 1;">
          <div style="flex: 0 0 190px; background: #FFFFFF; border-right: 2.5px solid var(--c-wine-primary); color: var(--c-wine-primary); font-family: var(--font-mono); font-size: 25px; font-weight: 800; display: flex; align-items: center; justify-content: center; text-align: center; padding: 10px;">
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

        <div style="background: #FAF5F5; border: 2.5px solid #8A5500; display: flex; align-items: stretch; flex: 1;">
          <div style="flex: 0 0 190px; background: #FFFFFF; border-right: 2.5px solid #8A5500; color: #8A5500; font-family: var(--font-mono); font-size: 25px; font-weight: 800; display: flex; align-items: center; justify-content: center; text-align: center; padding: 10px;">
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
  <title>Test Slide 13 Variants</title>
  <link rel="stylesheet" href="http://localhost:8085/styles.css?v=25">
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
        ('slide_13_a1.html', 'slide_13_a1.png', A1_HTML),
        ('slide_13_a2.html', 'slide_13_a2.png', A2_HTML),
        ('slide_13_a3.html', 'slide_13_a3.png', A3_HTML),
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
