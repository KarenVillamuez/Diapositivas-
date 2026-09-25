# -*- coding: utf-8 -*-
import os
from playwright.sync_api import sync_playwright

output_dir = r"C:\Users\ASUS\.gemini\antigravity-ide\brain\a6624504-511c-4b9d-bc9a-468e348bde40"
os.makedirs(output_dir, exist_ok=True)

# ---------------------------------------------------------------------------
# SVG 1: Slopegraph Grande (para Layout 72/28)
# Ancho 1100, Alto 440
# Escala 1.0 a 5.0 (y: 390 a 70, dy = 320px => 80px/unidad)
# x1 = 300, x2 = 800 (espacio generoso entre postes de 500px)
# R01: 3.00 (230) -> 1.67 (336.4)
# R02: 3.67 (176.4) -> 1.33 (363.6)
# R03: 3.33 (203.6) -> 1.00 (390.0)
# R04: 3.00 (230) -> 1.00 (390.0)
# R05: 4.00 (150) -> 1.00 (390.0)
# R06: 4.00 (150) -> 1.33 (363.6)
# R07: 3.00 (230) -> 2.33 (283.6)
# R08: 3.00 (230) -> 3.33 (203.6)
# R09: 3.00 (230) -> 3.33 (203.6)
# R10: 3.33 (203.6) -> 3.00 (230.0)
# ---------------------------------------------------------------------------

SVG_GRAPH_HERO_LARGE = '''
<svg viewBox="0 0 1140 450" style="width: 100%; height: auto; font-family: var(--font-sans);">
  <!-- Rejilla de fondo horizontal -->
  <line x1="220" y1="70" x2="880" y2="70" stroke="#EAE0E1" stroke-width="1.5" stroke-dasharray="5 5" />
  <line x1="220" y1="150" x2="880" y2="150" stroke="#EAE0E1" stroke-width="1.5" stroke-dasharray="5 5" />
  <line x1="220" y1="230" x2="880" y2="230" stroke="#EAE0E1" stroke-width="1.5" stroke-dasharray="5 5" />
  <line x1="220" y1="310" x2="880" y2="310" stroke="#EAE0E1" stroke-width="1.5" stroke-dasharray="5 5" />
  <line x1="220" y1="390" x2="880" y2="390" stroke="#EAE0E1" stroke-width="1.5" stroke-dasharray="5 5" />

  <!-- Postes verticales de docentes -->
  <line x1="280" y1="50" x2="280" y2="410" stroke="#460811" stroke-width="4" />
  <line x1="820" y1="50" x2="820" y2="410" stroke="#C9101B" stroke-width="4" />

  <!-- Cabeceras de postes -->
  <text x="280" y="24" font-size="26" font-weight="900" fill="#460811" text-anchor="middle">Docente 1</text>
  <text x="280" y="46" font-size="18" font-weight="800" fill="#460811" text-anchor="middle" font-family="var(--font-mono)">MEDIA: 3.33 / 5.0</text>

  <text x="820" y="24" font-size="26" font-weight="900" fill="#C9101B" text-anchor="middle">Docente 2</text>
  <text x="820" y="46" font-size="18" font-weight="800" fill="#C9101B" text-anchor="middle" font-family="var(--font-mono)">MEDIA: 1.93 / 5.0</text>

  <!-- Escalas numéricas -->
  <text x="255" y="77" font-size="20" fill="#8D7A7D" text-anchor="end" font-weight="800" font-family="var(--font-mono)">5.0</text>
  <text x="255" y="157" font-size="20" fill="#8D7A7D" text-anchor="end" font-weight="800" font-family="var(--font-mono)">4.0</text>
  <text x="255" y="237" font-size="20" fill="#8D7A7D" text-anchor="end" font-weight="800" font-family="var(--font-mono)">3.0</text>
  <text x="255" y="317" font-size="20" fill="#8D7A7D" text-anchor="end" font-weight="800" font-family="var(--font-mono)">2.0</text>
  <text x="255" y="397" font-size="20" fill="#8D7A7D" text-anchor="end" font-weight="800" font-family="var(--font-mono)">1.0</text>

  <text x="845" y="77" font-size="20" fill="#8D7A7D" font-weight="800" font-family="var(--font-mono)">5.0</text>
  <text x="845" y="157" font-size="20" fill="#8D7A7D" font-weight="800" font-family="var(--font-mono)">4.0</text>
  <text x="845" y="237" font-size="20" fill="#8D7A7D" font-weight="800" font-family="var(--font-mono)">3.0</text>
  <text x="845" y="317" font-size="20" fill="#8D7A7D" font-weight="800" font-family="var(--font-mono)">2.0</text>
  <text x="845" y="397" font-size="20" fill="#8D7A7D" font-weight="800" font-family="var(--font-mono)">1.0</text>

  <!-- 10 LÍNEAS REALES TABLA 4 -->
  <!-- 4 Neutras (Gris suave 3px) -->
  <line x1="280" y1="230" x2="820" y2="336" stroke="#8D7A7D" stroke-width="2.5" opacity="0.4" />
  <line x1="280" y1="230" x2="820" y2="390" stroke="#8D7A7D" stroke-width="2.5" opacity="0.4" />
  <line x1="280" y1="150" x2="820" y2="364" stroke="#8D7A7D" stroke-width="2.5" opacity="0.4" />
  <line x1="280" y1="204" x2="820" y2="230" stroke="#8D7A7D" stroke-width="2.5" opacity="0.4" />

  <!-- 3 Aprobadas por Docente 1 (Vino institucional 4.5px) -->
  <line x1="280" y1="176" x2="820" y2="364" stroke="#460811" stroke-width="4.5" opacity="0.95" />
  <line x1="280" y1="204" x2="820" y2="390" stroke="#460811" stroke-width="4.5" opacity="0.95" />
  <line x1="280" y1="150" x2="820" y2="390" stroke="#460811" stroke-width="5.5" opacity="1.0" />

  <!-- Anotación del mayor desplome: R05 de 4.0 a 1.0 -->
  <text x="440" y="270" font-size="16" font-weight="800" fill="#460811" font-family="var(--font-mono)" transform="rotate(24 440,270)">Desplome R05 (4.0 &rarr; 1.0)</text>

  <!-- 3 Aprobadas por Docente 2 (Rojo carmesí acento 4.5px) -->
  <line x1="280" y1="230" x2="820" y2="284" stroke="#C9101B" stroke-width="4.5" opacity="0.95" />
  <line x1="280" y1="230" x2="820" y2="204" stroke="#C9101B" stroke-width="4.5" opacity="0.95" />
  <line x1="280" y1="230" x2="820" y2="204" stroke="#C9101B" stroke-width="4.5" opacity="0.95" />

  <!-- Puntos Docente 1 -->
  <circle cx="280" cy="150" r="9" fill="#460811" />
  <circle cx="280" cy="176" r="7" fill="#460811" />
  <circle cx="280" cy="204" r="7" fill="#460811" />
  <circle cx="280" cy="230" r="10" fill="#460811" />

  <!-- Puntos Docente 2 -->
  <circle cx="820" cy="204" r="8" fill="#C9101B" />
  <circle cx="820" cy="230" r="7" fill="#8D7A7D" />
  <circle cx="820" cy="284" r="7" fill="#C9101B" />
  <circle cx="820" cy="336" r="7" fill="#8D7A7D" />
  <circle cx="820" cy="364" r="8" fill="#460811" />
  <circle cx="820" cy="390" r="10" fill="#C9101B" />
</svg>
'''

# -------------------------------------------------------------
# OPCION G1: Hero Slopegraph Gigante (72% ancho) + Columna Lateral Ultra-Minimalista (28%)
# -------------------------------------------------------------
CONTENT_G1 = f'''
    <h2 class="s-lead-question" style="font-size: 38px; font-weight: 800; margin: 0; line-height: 1.2; color: #2C0509;">
      La prueba docente: cuando los evaluadores humanos discrepan del algoritmo
    </h2>

    <div style="display: grid; grid-template-columns: 1180px 1fr; gap: 36px; align-items: stretch;">
      
      <!-- HERO PRINCIPAL: Slopegraph a Gran Escala -->
      <div style="background: #FAF5F5; border: 2px solid #EAE0E1; border-left: 12px solid var(--c-wine-primary); padding: 20px 28px; display: flex; flex-direction: column; justify-content: space-between;">
        <div style="display: flex; justify-content: space-between; align-items: center;">
          <span style="font-family: var(--font-mono); font-size: 19px; font-weight: 800; color: var(--c-wine-primary); letter-spacing: 1.5px;">
            FIGURA 4 DEL PAPER · DISPARIDAD RADICAL ENTRE EVALUADORES (N = 10)
          </span>
          <span style="font-family: var(--font-mono); font-size: 18px; font-weight: 700; color: var(--c-red-accent);">
            Caída neta: 3.33 &rarr; 1.93
          </span>
        </div>

        {SVG_GRAPH_HERO_LARGE}

        <!-- Leyenda ultra-clara integrada -->
        <div style="display: flex; justify-content: space-around; align-items: center; background: #FFFFFF; border: 1.5px solid #EAE0E1; padding: 12px 20px;">
          <div style="display: flex; align-items: center; gap: 12px;">
            <div style="width: 28px; height: 6px; background: var(--c-wine-primary);"></div>
            <span style="font-family: var(--font-sans); font-size: 19px; font-weight: 800; color: #110103;">Aprobó Docente 1 (3 de 10)</span>
          </div>
          <div style="display: flex; align-items: center; gap: 12px;">
            <div style="width: 28px; height: 6px; background: var(--c-red-accent);"></div>
            <span style="font-family: var(--font-sans); font-size: 19px; font-weight: 800; color: #110103;">Aprobó Docente 2 (3 de 10)</span>
          </div>
          <div style="display: flex; align-items: center; gap: 12px;">
            <div style="width: 28px; height: 4px; background: #8D7A7D;"></div>
            <span style="font-family: var(--font-sans); font-size: 19px; font-weight: 600; color: #5D4A4D;">Reprobadas por ambos (4 de 10)</span>
          </div>
        </div>
      </div>

      <!-- COLUMNA LATERAL ULTRA-SINTÉTICA (Texto Mínimo, Cifras Puras) -->
      <div style="display: flex; flex-direction: column; justify-content: space-between; gap: 14px;">
        
        <!-- Tarjeta 1: Cero en común (La más importante) -->
        <div style="background: #FAF5F5; border-left: 10px solid #B38600; padding: 22px 24px; flex: 1; display: flex; flex-direction: column; justify-content: center;">
          <div style="font-family: var(--font-mono); font-size: 60px; font-weight: 900; color: #B38600; line-height: 1;">
            0 / 10
          </div>
          <div style="font-family: var(--font-sans); font-size: 24px; font-weight: 800; color: #110103; margin-top: 6px;">
            Coincidencias en Aula
          </div>
          <div style="font-family: var(--font-sans); font-size: 19px; font-weight: 600; color: #5D4A4D; margin-top: 4px;">
            Aprobaciones 100% disjuntas.
          </div>
        </div>

        <!-- Tarjeta 2: Kappa de Cohen -->
        <div style="background: #FAF5F5; border-left: 10px solid var(--c-red-accent); padding: 22px 24px; flex: 1; display: flex; flex-direction: column; justify-content: center;">
          <div style="font-family: var(--font-mono); font-size: 52px; font-weight: 900; color: var(--c-red-accent); line-height: 1;">
            &kappa; = -0.429
          </div>
          <div style="font-family: var(--font-sans); font-size: 24px; font-weight: 800; color: #110103; margin-top: 6px;">
            Desacuerdo Severo
          </div>
          <div style="font-family: var(--font-sans); font-size: 19px; font-weight: 600; color: #5D4A4D; margin-top: 4px;">
            Discrepan más que el azar.
          </div>
        </div>

        <!-- Tarjeta 3: Correlación Spearman -->
        <div style="background: #FAF5F5; border-left: 10px solid var(--c-wine-primary); padding: 22px 24px; flex: 1; display: flex; flex-direction: column; justify-content: center;">
          <div style="font-family: var(--font-mono); font-size: 44px; font-weight: 900; color: var(--c-wine-primary); line-height: 1;">
            &rho; &le; +0.26
          </div>
          <div style="font-family: var(--font-sans); font-size: 24px; font-weight: 800; color: #110103; margin-top: 6px;">
            Correlación Nula
          </div>
          <div style="font-family: var(--font-sans); font-size: 19px; font-weight: 600; color: #5D4A4D; margin-top: 4px;">
            Sin relación con el algoritmo (<span style="font-family: var(--font-mono);">p &gt; 0.40</span>).
          </div>
        </div>

      </div>
    </div>

    <!-- REMATE EDITORIAL INFERIOR TIPO P2 -->
    <div style="background: #FAF5F5; border-top: 3.5px solid var(--c-wine-primary); border-bottom: 3.5px solid var(--c-wine-primary); padding: 14px 24px; display: flex; justify-content: space-between; align-items: center;">
      <div style="display: flex; align-items: center; gap: 14px;">
        <span style="font-family: var(--font-mono); font-size: 19px; font-weight: 800; color: var(--c-wine-primary); letter-spacing: 1.5px; white-space: nowrap;">
          LECCIÓN DE CAMPO:
        </span>
        <span style="font-family: var(--font-sans); font-size: 23px; font-weight: 700; color: #110103; white-space: nowrap;">
          Un puntaje algorítmico alto no predice aceptación pedagógica ni garantiza consenso docente.
        </span>
      </div>
      <span style="font-family: var(--font-mono); font-size: 19px; font-weight: 700; color: #5D4A4D; white-space: nowrap; margin-left: 20px;">
        Tabla 4 del paper
      </span>
    </div>
'''

# -------------------------------------------------------------
# SVG 2: Slopegraph Panorámico a Pantalla Completa (1600px ancho)
# -------------------------------------------------------------
SVG_GRAPH_FULL_STAGE = '''
<svg viewBox="0 0 1600 360" style="width: 100%; height: auto; font-family: var(--font-sans);">
  <!-- Rejilla horizontal -->
  <line x1="280" y1="50" x2="1320" y2="50" stroke="#EAE0E1" stroke-width="1.5" stroke-dasharray="6 6" />
  <line x1="280" y1="120" x2="1320" y2="120" stroke="#EAE0E1" stroke-width="1.5" stroke-dasharray="6 6" />
  <line x1="280" y1="190" x2="1320" y2="190" stroke="#EAE0E1" stroke-width="1.5" stroke-dasharray="6 6" />
  <line x1="280" y1="260" x2="1320" y2="260" stroke="#EAE0E1" stroke-width="1.5" stroke-dasharray="6 6" />
  <line x1="280" y1="330" x2="1320" y2="330" stroke="#EAE0E1" stroke-width="1.5" stroke-dasharray="6 6" />

  <!-- Ejes -->
  <line x1="360" y1="40" x2="360" y2="340" stroke="#460811" stroke-width="4.5" />
  <line x1="1240" y1="40" x2="1240" y2="340" stroke="#C9101B" stroke-width="4.5" />

  <!-- Cabeceras de Ejes -->
  <text x="360" y="20" font-size="28" font-weight="900" fill="#460811" text-anchor="middle">Docente 1</text>
  <text x="360" y="40" font-size="20" font-weight="800" fill="#460811" text-anchor="middle" font-family="var(--font-mono)">MEDIA: 3.33 / 5.0 (Aprobó 3)</text>

  <text x="1240" y="20" font-size="28" font-weight="900" fill="#C9101B" text-anchor="middle">Docente 2</text>
  <text x="1240" y="40" font-size="20" font-weight="800" fill="#C9101B" text-anchor="middle" font-family="var(--font-mono)">MEDIA: 1.93 / 5.0 (Aprobó 3)</text>

  <!-- Escalas numéricas -->
  <text x="330" y="58" font-size="22" fill="#8D7A7D" text-anchor="end" font-weight="800" font-family="var(--font-mono)">5.0</text>
  <text x="330" y="128" font-size="22" fill="#8D7A7D" text-anchor="end" font-weight="800" font-family="var(--font-mono)">4.0</text>
  <text x="330" y="198" font-size="22" fill="#8D7A7D" text-anchor="end" font-weight="800" font-family="var(--font-mono)">3.0</text>
  <text x="330" y="268" font-size="22" fill="#8D7A7D" text-anchor="end" font-weight="800" font-family="var(--font-mono)">2.0</text>
  <text x="330" y="338" font-size="22" fill="#8D7A7D" text-anchor="end" font-weight="800" font-family="var(--font-mono)">1.0</text>

  <text x="1270" y="58" font-size="22" fill="#8D7A7D" font-weight="800" font-family="var(--font-mono)">5.0</text>
  <text x="1270" y="128" font-size="22" fill="#8D7A7D" font-weight="800" font-family="var(--font-mono)">4.0</text>
  <text x="1270" y="198" font-size="22" fill="#8D7A7D" font-weight="800" font-family="var(--font-mono)">3.0</text>
  <text x="1270" y="268" font-size="22" fill="#8D7A7D" font-weight="800" font-family="var(--font-mono)">2.0</text>
  <text x="1270" y="338" font-size="22" fill="#8D7A7D" font-weight="800" font-family="var(--font-mono)">1.0</text>

  <!-- 10 LÍNEAS REALES TABLA 4 -->
  <!-- 4 Neutras -->
  <line x1="360" y1="190" x2="1240" y2="283" stroke="#8D7A7D" stroke-width="2.5" opacity="0.4" />
  <line x1="360" y1="190" x2="1240" y2="330" stroke="#8D7A7D" stroke-width="2.5" opacity="0.4" />
  <line x1="360" y1="120" x2="1240" y2="307" stroke="#8D7A7D" stroke-width="2.5" opacity="0.4" />
  <line x1="360" y1="167" x2="1240" y2="190" stroke="#8D7A7D" stroke-width="2.5" opacity="0.4" />

  <!-- 3 Aprobadas por Docente 1 (Vino 5px) -->
  <line x1="360" y1="143" x2="1240" y2="307" stroke="#460811" stroke-width="5" opacity="0.95" />
  <line x1="360" y1="167" x2="1240" y2="330" stroke="#460811" stroke-width="5" opacity="0.95" />
  <line x1="360" y1="120" x2="1240" y2="330" stroke="#460811" stroke-width="6.5" opacity="1.0" />

  <!-- 3 Aprobadas por Docente 2 (Rojo 5px) -->
  <line x1="360" y1="190" x2="1240" y2="237" stroke="#C9101B" stroke-width="5" opacity="0.95" />
  <line x1="360" y1="190" x2="1240" y2="167" stroke="#C9101B" stroke-width="5" opacity="0.95" />
  <line x1="360" y1="190" x2="1240" y2="167" stroke="#C9101B" stroke-width="5" opacity="0.95" />

  <!-- Puntos Docente 1 -->
  <circle cx="360" cy="120" r="10" fill="#460811" />
  <circle cx="360" cy="143" r="8" fill="#460811" />
  <circle cx="360" cy="167" r="8" fill="#460811" />
  <circle cx="360" cy="190" r="11" fill="#460811" />

  <!-- Puntos Docente 2 -->
  <circle cx="1240" cy="167" r="9" fill="#C9101B" />
  <circle cx="1240" cy="190" r="8" fill="#8D7A7D" />
  <circle cx="1240" cy="237" r="8" fill="#C9101B" />
  <circle cx="1240" cy="283" r="8" fill="#8D7A7D" />
  <circle cx="1240" cy="307" r="9" fill="#460811" />
  <circle cx="1240" cy="330" r="11" fill="#C9101B" />

  <!-- Anotaciones dentro del gráfico para no ocupar espacio fuera -->
  <text x="700" y="245" font-size="19" font-weight="800" fill="#460811" font-family="var(--font-mono)" transform="rotate(13 700,245)">Desplomes severos: 4.0 &rarr; 1.0</text>
  <text x="680" y="165" font-size="18" font-weight="800" fill="#C9101B" font-family="var(--font-mono)" transform="rotate(-3 680,165)">Aprobadas por D2 suben: 3.0 &rarr; 3.3</text>
</svg>
'''

# -------------------------------------------------------------
# OPCION G2: Escenario Panorámico Total (Gráfica al 100% de ancho + 3 Píldoras de Cifras Puras)
# -------------------------------------------------------------
CONTENT_G2 = f'''
    <h2 class="s-lead-question" style="font-size: 38px; font-weight: 800; margin: 0; line-height: 1.2; color: #2C0509;">
      La prueba docente: cuando los evaluadores humanos discrepan del algoritmo
    </h2>

    <!-- EL SLOPEGRAPH OCUPA TODO EL CENTRO DE LA LÁMINA -->
    <div style="background: #FAF5F5; border: 2px solid #EAE0E1; border-left: 12px solid var(--c-wine-primary); padding: 18px 30px; display: flex; flex-direction: column; justify-content: space-between;">
      <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 4px;">
        <span style="font-family: var(--font-mono); font-size: 18px; font-weight: 800; color: var(--c-wine-primary); letter-spacing: 1.5px;">
          FIGURA 4 DEL PAPER · DISPARIDAD ENTRE EVALUADORES INDEPENDIENTES (N = 10)
        </span>
        <div style="display: flex; gap: 24px; align-items: center;">
          <div style="display: flex; align-items: center; gap: 8px;">
            <div style="width: 20px; height: 5px; background: var(--c-wine-primary);"></div>
            <span style="font-family: var(--font-sans); font-size: 17px; font-weight: 700; color: #110103;">Aprobó Docente 1</span>
          </div>
          <div style="display: flex; align-items: center; gap: 8px;">
            <div style="width: 20px; height: 5px; background: var(--c-red-accent);"></div>
            <span style="font-family: var(--font-sans); font-size: 17px; font-weight: 700; color: #110103;">Aprobó Docente 2</span>
          </div>
          <div style="display: flex; align-items: center; gap: 8px;">
            <div style="width: 20px; height: 3px; background: #8D7A7D;"></div>
            <span style="font-family: var(--font-sans); font-size: 17px; font-weight: 600; color: #5D4A4D;">Reprobadas por ambos</span>
          </div>
        </div>
      </div>

      {SVG_GRAPH_FULL_STAGE}
    </div>

    <!-- TIRA DE 3 STATS HIPER-SINTÉTICAS (Sin párrafos, solo el número y el veredicto) -->
    <div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 24px;">
      <div style="background: #FFFFFF; border: 2px solid #EAE0E1; border-left: 10px solid #B38600; padding: 14px 22px; display: flex; align-items: center; justify-content: space-between;">
        <div>
          <div style="font-family: var(--font-sans); font-size: 20px; font-weight: 800; color: #110103;">
            Coincidencias en Aula
          </div>
          <div style="font-family: var(--font-sans); font-size: 17px; color: #5D4A4D; font-weight: 600;">
            Aprobación 100% disjunta (3 vs 3).
          </div>
        </div>
        <div style="font-family: var(--font-mono); font-size: 50px; font-weight: 900; color: #B38600; line-height: 1; white-space: nowrap; margin-left: 12px;">
          0 / 10
        </div>
      </div>

      <div style="background: #FFFFFF; border: 2px solid #EAE0E1; border-left: 10px solid var(--c-red-accent); padding: 14px 22px; display: flex; align-items: center; justify-content: space-between;">
        <div>
          <div style="font-family: var(--font-sans); font-size: 20px; font-weight: 800; color: #110103;">
            Desacuerdo Sistemático
          </div>
          <div style="font-family: var(--font-sans); font-size: 17px; color: #5D4A4D; font-weight: 600;">
            Kappa de Cohen negativo.
          </div>
        </div>
        <div style="font-family: var(--font-mono); font-size: 42px; font-weight: 900; color: var(--c-red-accent); line-height: 1; white-space: nowrap; margin-left: 12px;">
          &kappa; = -0.429
        </div>
      </div>

      <div style="background: #FFFFFF; border: 2px solid #EAE0E1; border-left: 10px solid var(--c-wine-primary); padding: 14px 22px; display: flex; align-items: center; justify-content: space-between;">
        <div>
          <div style="font-family: var(--font-sans); font-size: 20px; font-weight: 800; color: #110103;">
            Correlación con Algoritmo
          </div>
          <div style="font-family: var(--font-sans); font-size: 17px; color: #5D4A4D; font-weight: 600;">
            Sin relación (<span style="font-family: var(--font-mono);">p &gt; 0.40</span>).
          </div>
        </div>
        <div style="font-family: var(--font-mono); font-size: 42px; font-weight: 900; color: var(--c-wine-primary); line-height: 1; white-space: nowrap; margin-left: 12px;">
          &rho; &le; +0.26
        </div>
      </div>
    </div>

    <!-- REMATE EDITORIAL INFERIOR TIPO P2 -->
    <div style="background: #FAF5F5; border-top: 3.5px solid var(--c-wine-primary); border-bottom: 3.5px solid var(--c-wine-primary); padding: 12px 24px; display: flex; justify-content: space-between; align-items: center;">
      <div style="display: flex; align-items: center; gap: 14px;">
        <span style="font-family: var(--font-mono); font-size: 18px; font-weight: 800; color: var(--c-wine-primary); letter-spacing: 1.5px; white-space: nowrap;">
          LECCIÓN DE CAMPO:
        </span>
        <span style="font-family: var(--font-sans); font-size: 22px; font-weight: 700; color: #110103; white-space: nowrap;">
          Un puntaje algorítmico alto no predice aceptación pedagógica ni garantiza consenso docente.
        </span>
      </div>
      <span style="font-family: var(--font-mono); font-size: 18px; font-weight: 700; color: #5D4A4D; white-space: nowrap; margin-left: 20px;">
        Tabla 4 del paper
      </span>
    </div>
'''

HTML_TEMPLATE = '''<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Test Slide 15 Graph Hero</title>
  <link rel="stylesheet" href="http://localhost:8085/styles.css?v=26">
</head>
<body style="margin: 0; padding: 0; background: #0b0103;">

  <div id="presentation-viewport">
    <div id="slides-stage">
      <section class="slide s-white active">
        <header class="slide-header">
          <div class="sh-left">
            <span class="sh-red-bar"></span>
            <span class="sh-category">03 · RESULTADOS · EL CHOQUE CON EL CRITERIO DOCENTE</span>
          </div>
          <img src="http://localhost:8085/assets/image6.png" alt="#LoxTIC" class="sh-loxtic">
        </header>
        <div class="sh-divider"></div>

        <div class="slide-content-area" style="top: 175px; height: 720px; justify-content: center; gap: 20px;">
          {content}
        </div>

        <div class="slide-footer-rule"></div>
        <footer class="slide-footer">
          <span class="sf-left">VI CONGRESO CARTAGENA · 2026</span>
          <span class="sf-right">LOHACEMOSXTIC.COM · SLM OFFLINE</span>
        </footer>
      </section>
    </div>
  </div>

</body>
</html>
'''

def main():
    options = [
        ('slide_15_hero_G1.html', 'slide_15_hero_G1.png', CONTENT_G1),
        ('slide_15_hero_G2.html', 'slide_15_hero_G2.png', CONTENT_G2),
    ]

    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(viewport={"width": 1920, "height": 1080})

        for html_name, png_name, content in options:
            html_path = os.path.join(output_dir, html_name)
            png_path = os.path.join(output_dir, png_name)

            full_html = HTML_TEMPLATE.format(content=content)
            with open(html_path, 'w', encoding='utf-8') as f:
                f.write(full_html)

            page.goto(f"file:///{html_path.replace(os.sep, '/')}")
            page.wait_for_timeout(400)
            page.screenshot(path=png_path)
            print(f"Captured: {png_name}")

        browser.close()

if __name__ == '__main__':
    main()
