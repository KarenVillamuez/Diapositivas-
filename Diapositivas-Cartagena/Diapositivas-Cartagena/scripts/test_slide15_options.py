# -*- coding: utf-8 -*-
import os
from playwright.sync_api import sync_playwright

output_dir = r"C:\Users\ASUS\.gemini\antigravity-ide\brain\a6624504-511c-4b9d-bc9a-468e348bde40"
os.makedirs(output_dir, exist_ok=True)

# SVG Slopegraph Helper with exact 10 responses from Table 4
# Scale 1.0 (bottom, y=300) to 5.0 (top, y=60), dy = 240px for 4 units => 60px/unit
# T1 x=190, T2 x=510
# R01: T1=3.00 (y=180), T2=1.67 (y=260) [Both No - Gray]
# R02: T1=3.67 (y=140), T2=1.33 (y=280) [T1 Yes - Wine]
# R03: T1=3.33 (y=160), T2=1.00 (y=300) [T1 Yes - Wine]
# R04: T1=3.00 (y=180), T2=1.00 (y=300) [Both No - Gray]
# R05: T1=4.00 (y=120), T2=1.00 (y=300) [T1 Yes - Wine]
# R06: T1=4.00 (y=120), T2=1.33 (y=280) [Both No - Gray]
# R07: T1=3.00 (y=180), T2=2.33 (y=220) [T2 Yes - Red]
# R08: T1=3.00 (y=180), T2=3.33 (y=160) [T2 Yes - Red]
# R09: T1=3.00 (y=180), T2=3.33 (y=160) [T2 Yes - Red]
# R10: T1=3.33 (y=160), T2=3.00 (y=180) [Both No - Gray]

SVG_SLOPEGRAPH = '''
<svg viewBox="0 0 700 340" style="width: 100%; height: auto; font-family: var(--font-sans);">
  <!-- Guías de fondo horizontales -->
  <line x1="160" y1="60" x2="540" y2="60" stroke="#EAE0E1" stroke-width="1" stroke-dasharray="4 4" />
  <line x1="160" y1="120" x2="540" y2="120" stroke="#EAE0E1" stroke-width="1" stroke-dasharray="4 4" />
  <line x1="160" y1="180" x2="540" y2="180" stroke="#EAE0E1" stroke-width="1" stroke-dasharray="4 4" />
  <line x1="160" y1="240" x2="540" y2="240" stroke="#EAE0E1" stroke-width="1" stroke-dasharray="4 4" />
  <line x1="160" y1="300" x2="540" y2="300" stroke="#EAE0E1" stroke-width="1" stroke-dasharray="4 4" />

  <!-- Ejes verticales de docentes -->
  <line x1="190" y1="45" x2="190" y2="310" stroke="#460811" stroke-width="3" />
  <line x1="510" y1="45" x2="510" y2="310" stroke="#C9101B" stroke-width="3" />

  <!-- Cabeceras de ejes con medias oficiales -->
  <text x="190" y="24" font-size="21" font-weight="800" fill="#460811" text-anchor="middle">Docente 1</text>
  <text x="190" y="42" font-size="16" font-weight="700" fill="#460811" text-anchor="middle" font-family="var(--font-mono)">Media: 3.33</text>

  <text x="510" y="24" font-size="21" font-weight="800" fill="#C9101B" text-anchor="middle">Docente 2</text>
  <text x="510" y="42" font-size="16" font-weight="700" fill="#C9101B" text-anchor="middle" font-family="var(--font-mono)">Media: 1.93</text>

  <!-- Escalas numéricas (1.0 a 5.0) -->
  <text x="175" y="65" font-size="16" fill="#8D7A7D" text-anchor="end" font-weight="700" font-family="var(--font-mono)">5.0</text>
  <text x="175" y="125" font-size="16" fill="#8D7A7D" text-anchor="end" font-weight="700" font-family="var(--font-mono)">4.0</text>
  <text x="175" y="185" font-size="16" fill="#8D7A7D" text-anchor="end" font-weight="700" font-family="var(--font-mono)">3.0</text>
  <text x="175" y="245" font-size="16" fill="#8D7A7D" text-anchor="end" font-weight="700" font-family="var(--font-mono)">2.0</text>
  <text x="175" y="305" font-size="16" fill="#8D7A7D" text-anchor="end" font-weight="700" font-family="var(--font-mono)">1.0</text>

  <text x="525" y="65" font-size="16" fill="#8D7A7D" font-weight="700" font-family="var(--font-mono)">5.0</text>
  <text x="525" y="125" font-size="16" fill="#8D7A7D" font-weight="700" font-family="var(--font-mono)">4.0</text>
  <text x="525" y="185" font-size="16" fill="#8D7A7D" font-weight="700" font-family="var(--font-mono)">3.0</text>
  <text x="525" y="245" font-size="16" fill="#8D7A7D" font-weight="700" font-family="var(--font-mono)">2.0</text>
  <text x="525" y="305" font-size="16" fill="#8D7A7D" font-weight="700" font-family="var(--font-mono)">1.0</text>

  <!-- 10 LÍNEAS REALES DE LA TABLA 4 (FIGURA 4) -->
  <!-- Neutras (Desaprobadas por ambos) -->
  <line x1="190" y1="180" x2="510" y2="260" stroke="#8D7A7D" stroke-width="2" opacity="0.45" />
  <line x1="190" y1="180" x2="510" y2="300" stroke="#8D7A7D" stroke-width="2" opacity="0.45" />
  <line x1="190" y1="120" x2="510" y2="280" stroke="#8D7A7D" stroke-width="2" opacity="0.45" />
  <line x1="190" y1="160" x2="510" y2="180" stroke="#8D7A7D" stroke-width="2" opacity="0.45" />

  <!-- Aprobadas solo por Docente 1 (Vino institucional) -->
  <line x1="190" y1="140" x2="510" y2="280" stroke="#460811" stroke-width="3" opacity="0.85" />
  <line x1="190" y1="160" x2="510" y2="300" stroke="#460811" stroke-width="3" opacity="0.85" />
  <line x1="190" y1="120" x2="510" y2="300" stroke="#460811" stroke-width="4" opacity="0.95" />

  <!-- Aprobadas solo por Docente 2 (Rojo carmesí acento) -->
  <line x1="190" y1="180" x2="510" y2="220" stroke="#C9101B" stroke-width="3" opacity="0.85" />
  <line x1="190" y1="180" x2="510" y2="160" stroke="#C9101B" stroke-width="3" opacity="0.85" />
  <line x1="190" y1="180" x2="510" y2="160" stroke="#C9101B" stroke-width="3" opacity="0.85" />

  <!-- Puntos Docente 1 -->
  <circle cx="190" cy="120" r="6" fill="#460811" />
  <circle cx="190" cy="140" r="5" fill="#460811" />
  <circle cx="190" cy="160" r="5" fill="#460811" />
  <circle cx="190" cy="180" r="7" fill="#460811" />

  <!-- Puntos Docente 2 -->
  <circle cx="510" cy="160" r="6" fill="#C9101B" />
  <circle cx="510" cy="180" r="5" fill="#8D7A7D" />
  <circle cx="510" cy="220" r="5" fill="#C9101B" />
  <circle cx="510" cy="260" r="5" fill="#8D7A7D" />
  <circle cx="510" cy="280" r="6" fill="#460811" />
  <circle cx="510" cy="300" r="7" fill="#C9101B" />
</svg>
'''

# -------------------------------------------------------------
# OPCION A: Split Clásico Perfeccionado (Slopegraph + 3 Métricas Verticales + Franja P2)
# -------------------------------------------------------------
CONTENT_A = f'''
    <h2 class="s-lead-question" style="font-size: 38px; font-weight: 800; margin: 0; line-height: 1.2; color: #2C0509;">
      La prueba docente: cuando los evaluadores humanos discrepan del algoritmo
    </h2>

    <div style="display: grid; grid-template-columns: 880px 1fr; gap: 40px; align-items: stretch;">
      
      <!-- Columna Izquierda: Slopegraph con Tarjeta Editorial -->
      <div style="background: #FAF5F5; border: 2px solid #EAE0E1; border-left: 10px solid var(--c-wine-primary); padding: 24px 28px; display: flex; flex-direction: column; justify-content: space-between;">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
          <span style="font-family: var(--font-mono); font-size: 17px; font-weight: 700; color: var(--c-wine-primary); letter-spacing: 1.5px;">
            FIGURA 4 DEL PAPER · DISPARIDAD ENTRE DOCENTES
          </span>
          <span style="font-family: var(--font-mono); font-size: 16px; font-weight: 600; color: #5D4A4D;">
            10 respuestas evaluadas
          </span>
        </div>

        {SVG_SLOPEGRAPH}

        <!-- Leyenda cromática de líneas -->
        <div style="display: flex; justify-content: space-around; align-items: center; background: #FFFFFF; border: 1.5px solid #EAE0E1; padding: 10px 16px; margin-top: 10px;">
          <div style="display: flex; align-items: center; gap: 8px;">
            <div style="width: 22px; height: 4px; background: var(--c-wine-primary);"></div>
            <span style="font-family: var(--font-sans); font-size: 18px; font-weight: 700; color: #110103;">Aprobó Docente 1 (3)</span>
          </div>
          <div style="display: flex; align-items: center; gap: 8px;">
            <div style="width: 22px; height: 4px; background: var(--c-red-accent);"></div>
            <span style="font-family: var(--font-sans); font-size: 18px; font-weight: 700; color: #110103;">Aprobó Docente 2 (3)</span>
          </div>
          <div style="display: flex; align-items: center; gap: 8px;">
            <div style="width: 22px; height: 3px; background: #8D7A7D;"></div>
            <span style="font-family: var(--font-sans); font-size: 18px; font-weight: 600; color: #5D4A4D;">Reprobadas por ambos (4)</span>
          </div>
        </div>
      </div>

      <!-- Columna Derecha: 3 Métricas Abiertas con Barra de Acento -->
      <div style="display: flex; flex-direction: column; justify-content: space-between; gap: 16px;">
        
        <!-- Métrica 1: Kappa -->
        <div style="background: #FAF5F5; border-left: 8px solid var(--c-red-accent); padding: 20px 24px;">
          <div style="display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 4px;">
            <span style="font-family: var(--font-mono); font-size: 44px; font-weight: 800; color: var(--c-red-accent); line-height: 1;">
              &kappa; = -0.429
            </span>
            <span style="font-family: var(--font-mono); font-size: 18px; font-weight: 700; color: #2C0509;">
              DESACUERDO SEVERO
            </span>
          </div>
          <div style="font-family: var(--font-sans); font-size: 21px; color: #110103; font-weight: 600; line-height: 1.35;">
            <strong>Kappa de Cohen negativo:</strong> el grado de discrepancia entre los profesores supera lo esperable por azar.
          </div>
        </div>

        <!-- Métrica 2: Rho Spearman -->
        <div style="background: #FAF5F5; border-left: 8px solid var(--c-wine-primary); padding: 20px 24px;">
          <div style="display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 4px;">
            <span style="font-family: var(--font-mono); font-size: 44px; font-weight: 800; color: var(--c-wine-primary); line-height: 1;">
              &rho; = +0.14 y +0.26
            </span>
            <span style="font-family: var(--font-mono); font-size: 18px; font-weight: 700; color: #2C0509;">
              CORRELACIÓN NULA
            </span>
          </div>
          <div style="font-family: var(--font-sans); font-size: 21px; color: #110103; font-weight: 600; line-height: 1.35;">
            Sin asociación estadística (<span style="font-family: var(--font-mono); font-size: 19px;">p &gt; 0.40</span>) entre el puntaje algorítmico y el juicio humano.
          </div>
        </div>

        <!-- Métrica 3: 0 en común -->
        <div style="background: #FAF5F5; border-left: 8px solid #B38600; padding: 20px 24px;">
          <div style="display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 4px;">
            <span style="font-family: var(--font-mono); font-size: 44px; font-weight: 800; color: #B38600; line-height: 1;">
              0 en Común
            </span>
            <span style="font-family: var(--font-mono); font-size: 18px; font-weight: 700; color: #2C0509;">
              USO EN AULA DIRECTO
            </span>
          </div>
          <div style="font-family: var(--font-sans); font-size: 21px; color: #110103; font-weight: 600; line-height: 1.35;">
            Cada docente aprobó 3 respuestas sin modificar; <strong>ninguna fue aprobada por ambos a la vez</strong>.
          </div>
        </div>

      </div>
    </div>

    <!-- REMATE EDITORIAL INFERIOR TIPO P2 (Aprobado en Slide 14) -->
    <div style="background: #FAF5F5; border-top: 3.5px solid var(--c-wine-primary); border-bottom: 3.5px solid var(--c-wine-primary); padding: 14px 24px; display: flex; justify-content: space-between; align-items: center;">
      <div style="display: flex; align-items: center; gap: 14px;">
        <span style="font-family: var(--font-mono); font-size: 19px; font-weight: 800; color: var(--c-wine-primary); letter-spacing: 1.5px; white-space: nowrap;">
          LECCIÓN DE CAMPO:
        </span>
        <span style="font-family: var(--font-sans); font-size: 23px; font-weight: 700; color: #110103; white-space: nowrap;">
          Un puntaje de RAG alto no predice aceptación pedagógica ni garantiza consenso docente.
        </span>
      </div>
      <span style="font-family: var(--font-mono); font-size: 19px; font-weight: 700; color: #5D4A4D; white-space: nowrap; margin-left: 20px;">
        Tabla 4 del paper
      </span>
    </div>
'''

# -------------------------------------------------------------
# OPCION B: Doble Tarjeta Equilibrada (50/50): Slopegraph vs Matriz de Decisión Binaria
# -------------------------------------------------------------
CONTENT_B = f'''
    <h2 class="s-lead-question" style="font-size: 38px; font-weight: 800; margin: 0; line-height: 1.2; color: #2C0509;">
      La prueba docente: cuando los evaluadores humanos discrepan del algoritmo
    </h2>

    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 36px; align-items: stretch;">
      
      <!-- Lado 1: Slopegraph Cuantitativo -->
      <div style="background: #FAF5F5; border: 2px solid #EAE0E1; border-left: 10px solid var(--c-wine-primary); padding: 24px 30px; display: flex; flex-direction: column; justify-content: space-between;">
        <div style="font-family: var(--font-mono); font-size: 18px; font-weight: 700; color: var(--c-wine-primary); letter-spacing: 1.5px; margin-bottom: 4px;">
          CALIFICACIÓN CUANTITATIVA (ESCALA 1.0 A 5.0)
        </div>

        {SVG_SLOPEGRAPH}

        <div style="background: #FFFFFF; border: 1.5px solid #EAE0E1; padding: 12px 18px; display: flex; justify-content: space-between; align-items: center;">
          <span style="font-family: var(--font-sans); font-size: 20px; font-weight: 700; color: #2C0509;">
            Caída neta de medias: <span style="font-family: var(--font-mono); color: var(--c-red-accent); font-size: 24px;">3.33 &rarr; 1.93</span>
          </span>
          <span style="font-family: var(--font-mono); font-size: 18px; font-weight: 700; color: #5D4A4D;">
            Disparidad de rigor
          </span>
        </div>
      </div>

      <!-- Lado 2: Matriz de Desacuerdo Cualitativo -->
      <div style="background: #FAF5F5; border: 2px solid #EAE0E1; border-left: 10px solid var(--c-red-accent); padding: 24px 30px; display: flex; flex-direction: column; justify-content: space-between;">
        <div style="font-family: var(--font-mono); font-size: 18px; font-weight: 700; color: var(--c-red-accent); letter-spacing: 1.5px; margin-bottom: 4px;">
          DECISIÓN CUALITATIVA DE APROBACIÓN EN AULA
        </div>

        <!-- Macro-cifra 0 / 10 -->
        <div style="background: #FFFFFF; border: 2px solid #EAE0E1; padding: 18px 24px; text-align: center;">
          <div style="font-family: var(--font-mono); font-size: 68px; font-weight: 900; color: var(--c-red-accent); line-height: 1;">
            0 / 10
          </div>
          <div style="font-family: var(--font-sans); font-size: 24px; font-weight: 800; color: #110103; margin-top: 4px;">
            Coincidencias en Respuestas Aprobadas
          </div>
          <div style="font-family: var(--font-sans); font-size: 19px; color: #5D4A4D; margin-top: 4px;">
            Cada profesor seleccionó 3 respuestas sin modificar, pero en conjuntos completamente disjuntos.
          </div>
        </div>

        <!-- 2 Píldoras de métricas de correlación -->
        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 18px;">
          <div style="background: #FFFFFF; border: 1.5px solid #EAE0E1; padding: 14px 18px;">
            <div style="font-family: var(--font-mono); font-size: 32px; font-weight: 800; color: var(--c-red-accent);">
              &kappa; = -0.429
            </div>
            <div style="font-family: var(--font-sans); font-size: 18px; font-weight: 700; color: #2C0509;">
              Desacuerdo severo
            </div>
            <div style="font-family: var(--font-sans); font-size: 16px; color: #5D4A4D;">
              Kappa de Cohen negativo.
            </div>
          </div>

          <div style="background: #FFFFFF; border: 1.5px solid #EAE0E1; padding: 14px 18px;">
            <div style="font-family: var(--font-mono); font-size: 32px; font-weight: 800; color: var(--c-wine-primary);">
              &rho; &le; +0.26
            </div>
            <div style="font-family: var(--font-sans); font-size: 18px; font-weight: 700; color: #2C0509;">
              Correlación nula
            </div>
            <div style="font-family: var(--font-sans); font-size: 16px; color: #5D4A4D;">
              Sin significancia (p &gt; 0.40).
            </div>
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
          Un puntaje de RAG alto no predice aceptación pedagógica ni garantiza consenso docente.
        </span>
      </div>
      <span style="font-family: var(--font-mono); font-size: 19px; font-weight: 700; color: #5D4A4D; white-space: nowrap; margin-left: 20px;">
        Tabla 4 del paper
      </span>
    </div>
'''

# -------------------------------------------------------------
# OPCION C: Enfoque Panorámico Horizontal (Slopegraph Ancho Superior + 3 Tarjetas Inferiores)
# -------------------------------------------------------------
SVG_SLOPEGRAPH_WIDE = '''
<svg viewBox="0 0 1600 240" style="width: 100%; height: auto; font-family: var(--font-sans);">
  <!-- Guías horizontales -->
  <line x1="380" y1="40" x2="1220" y2="40" stroke="#EAE0E1" stroke-width="1" stroke-dasharray="4 4" />
  <line x1="380" y1="85" x2="1220" y2="85" stroke="#EAE0E1" stroke-width="1" stroke-dasharray="4 4" />
  <line x1="380" y1="130" x2="1220" y2="130" stroke="#EAE0E1" stroke-width="1" stroke-dasharray="4 4" />
  <line x1="380" y1="175" x2="1220" y2="175" stroke="#EAE0E1" stroke-width="1" stroke-dasharray="4 4" />
  <line x1="380" y1="220" x2="1220" y2="220" stroke="#EAE0E1" stroke-width="1" stroke-dasharray="4 4" />

  <!-- Ejes -->
  <line x1="420" y1="30" x2="420" y2="230" stroke="#460811" stroke-width="3.5" />
  <line x1="1180" y1="30" x2="1180" y2="230" stroke="#C9101B" stroke-width="3.5" />

  <!-- Cabeceras -->
  <text x="420" y="16" font-size="20" font-weight="800" fill="#460811" text-anchor="middle">Docente 1 (Media: 3.33)</text>
  <text x="1180" y="16" font-size="20" font-weight="800" fill="#C9101B" text-anchor="middle">Docente 2 (Media: 1.93)</text>

  <!-- Escalas -->
  <text x="400" y="46" font-size="16" fill="#8D7A7D" text-anchor="end" font-weight="700" font-family="var(--font-mono)">5.0</text>
  <text x="400" y="91" font-size="16" fill="#8D7A7D" text-anchor="end" font-weight="700" font-family="var(--font-mono)">4.0</text>
  <text x="400" y="136" font-size="16" fill="#8D7A7D" text-anchor="end" font-weight="700" font-family="var(--font-mono)">3.0</text>
  <text x="400" y="181" font-size="16" fill="#8D7A7D" text-anchor="end" font-weight="700" font-family="var(--font-mono)">2.0</text>
  <text x="400" y="226" font-size="16" fill="#8D7A7D" text-anchor="end" font-weight="700" font-family="var(--font-mono)">1.0</text>

  <text x="1200" y="46" font-size="16" fill="#8D7A7D" font-weight="700" font-family="var(--font-mono)">5.0</text>
  <text x="1200" y="91" font-size="16" fill="#8D7A7D" font-weight="700" font-family="var(--font-mono)">4.0</text>
  <text x="1200" y="136" font-size="16" fill="#8D7A7D" font-weight="700" font-family="var(--font-mono)">3.0</text>
  <text x="1200" y="181" font-size="16" fill="#8D7A7D" font-weight="700" font-family="var(--font-mono)">2.0</text>
  <text x="1200" y="226" font-size="16" fill="#8D7A7D" font-weight="700" font-family="var(--font-mono)">1.0</text>

  <!-- Líneas Neutras -->
  <line x1="420" y1="130" x2="1180" y2="190" stroke="#8D7A7D" stroke-width="2" opacity="0.45" />
  <line x1="420" y1="130" x2="1180" y2="220" stroke="#8D7A7D" stroke-width="2" opacity="0.45" />
  <line x1="420" y1="85" x2="1180" y2="205" stroke="#8D7A7D" stroke-width="2" opacity="0.45" />
  <line x1="420" y1="115" x2="1180" y2="130" stroke="#8D7A7D" stroke-width="2" opacity="0.45" />

  <!-- Aprobadas Docente 1 -->
  <line x1="420" y1="100" x2="1180" y2="205" stroke="#460811" stroke-width="3" opacity="0.85" />
  <line x1="420" y1="115" x2="1180" y2="220" stroke="#460811" stroke-width="3" opacity="0.85" />
  <line x1="420" y1="85" x2="1180" y2="220" stroke="#460811" stroke-width="4" opacity="0.95" />

  <!-- Aprobadas Docente 2 -->
  <line x1="420" y1="130" x2="1180" y2="160" stroke="#C9101B" stroke-width="3" opacity="0.85" />
  <line x1="420" y1="130" x2="1180" y2="115" stroke="#C9101B" stroke-width="3" opacity="0.85" />
  <line x1="420" y1="130" x2="1180" y2="115" stroke="#C9101B" stroke-width="3" opacity="0.85" />

  <!-- Puntos -->
  <circle cx="420" cy="85" r="6" fill="#460811" />
  <circle cx="420" cy="100" r="5" fill="#460811" />
  <circle cx="420" cy="115" r="5" fill="#460811" />
  <circle cx="420" cy="130" r="7" fill="#460811" />

  <circle cx="1180" cy="115" r="6" fill="#C9101B" />
  <circle cx="1180" cy="130" r="5" fill="#8D7A7D" />
  <circle cx="1180" cy="160" r="5" fill="#C9101B" />
  <circle cx="1180" cy="190" r="5" fill="#8D7A7D" />
  <circle cx="1180" cy="205" r="6" fill="#460811" />
  <circle cx="1180" cy="220" r="7" fill="#C9101B" />
</svg>
'''

CONTENT_C = f'''
    <h2 class="s-lead-question" style="font-size: 38px; font-weight: 800; margin: 0; line-height: 1.2; color: #2C0509;">
      La prueba docente: cuando los evaluadores humanos discrepan del algoritmo
    </h2>

    <!-- Slopegraph Panorámico Superior -->
    <div style="background: #FAF5F5; border: 2px solid #EAE0E1; border-left: 10px solid var(--c-wine-primary); padding: 18px 30px;">
      <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 2px;">
        <span style="font-family: var(--font-mono); font-size: 17px; font-weight: 700; color: var(--c-wine-primary); letter-spacing: 1.5px;">
          FIGURA 4 DEL PAPER · DISPARIDAD ENTRE DOCENTES (N = 10 RESPUESTAS)
        </span>
        <span style="font-family: var(--font-sans); font-size: 17px; font-weight: 700; color: var(--c-red-accent);">
          Caída neta de medias: 3.33 &rarr; 1.93
        </span>
      </div>
      {SVG_SLOPEGRAPH_WIDE}
    </div>

    <!-- 3 Tarjetas Horizontales Inferiores -->
    <div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 24px;">
      <div style="background: #FAF5F5; border-left: 8px solid var(--c-red-accent); padding: 18px 22px;">
        <div style="font-family: var(--font-mono); font-size: 40px; font-weight: 800; color: var(--c-red-accent); line-height: 1; margin-bottom: 4px;">
          &kappa; = -0.429
        </div>
        <div style="font-family: var(--font-sans); font-size: 20px; font-weight: 800; color: #110103; margin-bottom: 4px;">
          Desacuerdo Sistemático
        </div>
        <div style="font-family: var(--font-sans); font-size: 18px; color: #5D4A4D; line-height: 1.3;">
          Kappa de Cohen negativo: discrepan con mayor severidad que el azar.
        </div>
      </div>

      <div style="background: #FAF5F5; border-left: 8px solid var(--c-wine-primary); padding: 18px 22px;">
        <div style="font-family: var(--font-mono); font-size: 40px; font-weight: 800; color: var(--c-wine-primary); line-height: 1; margin-bottom: 4px;">
          &rho; = +0.14 / +0.26
        </div>
        <div style="font-family: var(--font-sans); font-size: 20px; font-weight: 800; color: #110103; margin-bottom: 4px;">
          Correlación Nula
        </div>
        <div style="font-family: var(--font-sans); font-size: 18px; color: #5D4A4D; line-height: 1.3;">
          Sin relación con la métrica automática (<span style="font-family: var(--font-mono);">p &gt; 0.40</span> en ambos casos).
        </div>
      </div>

      <div style="background: #FAF5F5; border-left: 8px solid #B38600; padding: 18px 22px;">
        <div style="font-family: var(--font-mono); font-size: 40px; font-weight: 800; color: #B38600; line-height: 1; margin-bottom: 4px;">
          0 en Común
        </div>
        <div style="font-family: var(--font-sans); font-size: 20px; font-weight: 800; color: #110103; margin-bottom: 4px;">
          Aprobación Disjunta
        </div>
        <div style="font-family: var(--font-sans); font-size: 18px; color: #5D4A4D; line-height: 1.3;">
          Cada docente aprobó 3 de 10; ¡cero coincidencias compartidas!
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
          Un puntaje de RAG alto no predice aceptación pedagógica ni garantiza consenso docente.
        </span>
      </div>
      <span style="font-family: var(--font-mono); font-size: 19px; font-weight: 700; color: #5D4A4D; white-space: nowrap; margin-left: 20px;">
        Tabla 4 del paper
      </span>
    </div>
'''

HTML_TEMPLATE = '''<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Test Slide 15 Options</title>
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

        <div class="slide-content-area" style="top: 175px; height: 720px; justify-content: center; gap: 22px;">
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
        ('slide_15_opt_A.html', 'slide_15_opt_A.png', CONTENT_A),
        ('slide_15_opt_B.html', 'slide_15_opt_B.png', CONTENT_B),
        ('slide_15_opt_C.html', 'slide_15_opt_C.png', CONTENT_C),
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
