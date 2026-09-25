# -*- coding: utf-8 -*-
import os
from playwright.sync_api import sync_playwright

output_dir = r"C:\Users\ASUS\.gemini\antigravity-ide\brain\a6624504-511c-4b9d-bc9a-468e348bde40"
os.makedirs(output_dir, exist_ok=True)

# ---------------------------------------------------------------------------
# SVG 1: Contraste Bicolor D1 (Vino) vs D2 (Rojo), 4 Muted (Gris sutil)
# ---------------------------------------------------------------------------
SVG_G1_A = '''
<svg viewBox="0 0 1140 450" style="width: 100%; height: auto; font-family: var(--font-sans);">
  <!-- Rejilla horizontal sutil de fondo -->
  <line x1="220" y1="70" x2="880" y2="70" stroke="#E6DCDE" stroke-width="1.2" stroke-dasharray="4 4" />
  <line x1="220" y1="150" x2="880" y2="150" stroke="#E6DCDE" stroke-width="1.2" stroke-dasharray="4 4" />
  <line x1="220" y1="230" x2="880" y2="230" stroke="#E6DCDE" stroke-width="1.2" stroke-dasharray="4 4" />
  <line x1="220" y1="310" x2="880" y2="310" stroke="#E6DCDE" stroke-width="1.2" stroke-dasharray="4 4" />
  <line x1="220" y1="390" x2="880" y2="390" stroke="#E6DCDE" stroke-width="1.2" stroke-dasharray="4 4" />

  <!-- Ejes verticales de docentes -->
  <line x1="280" y1="60" x2="280" y2="400" stroke="#460811" stroke-width="3.5" />
  <line x1="820" y1="60" x2="820" y2="400" stroke="#C9101B" stroke-width="3.5" />

  <!-- Cabeceras de ejes con medias -->
  <text x="280" y="24" font-size="28" font-weight="900" fill="#460811" text-anchor="middle">Docente 1</text>
  <text x="280" y="48" font-size="19" font-weight="800" fill="#460811" text-anchor="middle" font-family="var(--font-mono)">MEDIA: 3.33</text>

  <text x="820" y="24" font-size="28" font-weight="900" fill="#C9101B" text-anchor="middle">Docente 2</text>
  <text x="820" y="48" font-size="19" font-weight="800" fill="#C9101B" text-anchor="middle" font-family="var(--font-mono)">MEDIA: 1.93</text>

  <!-- Escalas numéricas (1.0 a 5.0) -->
  <text x="255" y="77" font-size="20" fill="#A08D90" text-anchor="end" font-weight="700" font-family="var(--font-mono)">5.0</text>
  <text x="255" y="157" font-size="20" fill="#A08D90" text-anchor="end" font-weight="700" font-family="var(--font-mono)">4.0</text>
  <text x="255" y="237" font-size="20" fill="#A08D90" text-anchor="end" font-weight="700" font-family="var(--font-mono)">3.0</text>
  <text x="255" y="317" font-size="20" fill="#A08D90" text-anchor="end" font-weight="700" font-family="var(--font-mono)">2.0</text>
  <text x="255" y="397" font-size="20" fill="#A08D90" text-anchor="end" font-weight="700" font-family="var(--font-mono)">1.0</text>

  <text x="845" y="77" font-size="20" fill="#A08D90" font-weight="700" font-family="var(--font-mono)">5.0</text>
  <text x="845" y="157" font-size="20" fill="#A08D90" font-weight="700" font-family="var(--font-mono)">4.0</text>
  <text x="845" y="237" font-size="20" fill="#A08D90" font-weight="700" font-family="var(--font-mono)">3.0</text>
  <text x="845" y="317" font-size="20" fill="#A08D90" font-weight="700" font-family="var(--font-mono)">2.0</text>
  <text x="845" y="397" font-size="20" fill="#A08D90" font-weight="700" font-family="var(--font-mono)">1.0</text>

  <!-- LÍNEAS OPACADAS DE FONDO (4 Reprobadas por ambos docentes: tenues y finas) -->
  <line x1="280" y1="230" x2="820" y2="336" stroke="#D2C5C7" stroke-width="1.8" opacity="0.45" />
  <line x1="280" y1="230" x2="820" y2="390" stroke="#D2C5C7" stroke-width="1.8" opacity="0.45" />
  <line x1="280" y1="150" x2="820" y2="364" stroke="#D2C5C7" stroke-width="1.8" opacity="0.45" />
  <line x1="280" y1="204" x2="820" y2="230" stroke="#D2C5C7" stroke-width="1.8" opacity="0.45" />

  <!-- LÍNEAS PROTAGONISTAS DOCENTE 1: Aprobadas por D1 (Vino 5px) que se desploman -->
  <line x1="280" y1="176" x2="820" y2="364" stroke="#460811" stroke-width="4.5" />
  <line x1="280" y1="204" x2="820" y2="390" stroke="#460811" stroke-width="4.5" />
  <line x1="280" y1="150" x2="820" y2="390" stroke="#460811" stroke-width="5.5" />

  <!-- LÍNEAS PROTAGONISTAS DOCENTE 2: Aprobadas por D2 (Rojo 4.5px) -->
  <line x1="280" y1="230" x2="820" y2="284" stroke="#C9101B" stroke-width="4.5" />
  <line x1="280" y1="230" x2="820" y2="204" stroke="#C9101B" stroke-width="4.5" />
  <line x1="280" y1="230" x2="820" y2="204" stroke="#C9101B" stroke-width="4.5" />

  <!-- Puntos destacados de las líneas clave -->
  <circle cx="280" cy="150" r="8" fill="#460811" />
  <circle cx="280" cy="176" r="7.5" fill="#460811" />
  <circle cx="280" cy="204" r="7.5" fill="#460811" />
  <circle cx="280" cy="230" r="8" fill="#460811" />

  <circle cx="820" cy="204" r="8.5" fill="#C9101B" />
  <circle cx="820" cy="284" r="7.5" fill="#C9101B" />
  <circle cx="820" cy="364" r="7.5" fill="#460811" />
  <circle cx="820" cy="390" r="9" fill="#460811" />
</svg>
'''

# ---------------------------------------------------------------------------
# SVG 2: Enfoque Desplome Dramático (Solo 3 de D1 en Rojo Acento, 7 en Gris)
# ---------------------------------------------------------------------------
SVG_G1_B = '''
<svg viewBox="0 0 1140 450" style="width: 100%; height: auto; font-family: var(--font-sans);">
  <!-- Rejilla -->
  <line x1="220" y1="70" x2="880" y2="70" stroke="#E6DCDE" stroke-width="1.2" stroke-dasharray="4 4" />
  <line x1="220" y1="150" x2="880" y2="150" stroke="#E6DCDE" stroke-width="1.2" stroke-dasharray="4 4" />
  <line x1="220" y1="230" x2="880" y2="230" stroke="#E6DCDE" stroke-width="1.2" stroke-dasharray="4 4" />
  <line x1="220" y1="310" x2="880" y2="310" stroke="#E6DCDE" stroke-width="1.2" stroke-dasharray="4 4" />
  <line x1="220" y1="390" x2="880" y2="390" stroke="#E6DCDE" stroke-width="1.2" stroke-dasharray="4 4" />

  <!-- Ejes -->
  <line x1="280" y1="60" x2="280" y2="400" stroke="#460811" stroke-width="3.5" />
  <line x1="820" y1="60" x2="820" y2="400" stroke="#C9101B" stroke-width="3.5" />

  <text x="280" y="24" font-size="28" font-weight="900" fill="#460811" text-anchor="middle">Docente 1</text>
  <text x="280" y="48" font-size="19" font-weight="800" fill="#460811" text-anchor="middle" font-family="var(--font-mono)">MEDIA: 3.33</text>

  <text x="820" y="24" font-size="28" font-weight="900" fill="#C9101B" text-anchor="middle">Docente 2</text>
  <text x="820" y="48" font-size="19" font-weight="800" fill="#C9101B" text-anchor="middle" font-family="var(--font-mono)">MEDIA: 1.93</text>

  <!-- Escalas -->
  <text x="255" y="77" font-size="20" fill="#A08D90" text-anchor="end" font-weight="700" font-family="var(--font-mono)">5.0</text>
  <text x="255" y="157" font-size="20" fill="#A08D90" text-anchor="end" font-weight="700" font-family="var(--font-mono)">4.0</text>
  <text x="255" y="237" font-size="20" fill="#A08D90" text-anchor="end" font-weight="700" font-family="var(--font-mono)">3.0</text>
  <text x="255" y="317" font-size="20" fill="#A08D90" text-anchor="end" font-weight="700" font-family="var(--font-mono)">2.0</text>
  <text x="255" y="397" font-size="20" fill="#A08D90" text-anchor="end" font-weight="700" font-family="var(--font-mono)">1.0</text>

  <text x="845" y="77" font-size="20" fill="#A08D90" font-weight="700" font-family="var(--font-mono)">5.0</text>
  <text x="845" y="157" font-size="20" fill="#A08D90" font-weight="700" font-family="var(--font-mono)">4.0</text>
  <text x="845" y="237" font-size="20" fill="#A08D90" font-weight="700" font-family="var(--font-mono)">3.0</text>
  <text x="845" y="317" font-size="20" fill="#A08D90" font-weight="700" font-family="var(--font-mono)">2.0</text>
  <text x="845" y="397" font-size="20" fill="#A08D90" font-weight="700" font-family="var(--font-mono)">1.0</text>

  <!-- 7 LÍNEAS OPACADAS EN GRIS TENUE -->
  <line x1="280" y1="230" x2="820" y2="336" stroke="#D8CBCD" stroke-width="1.8" opacity="0.4" />
  <line x1="280" y1="230" x2="820" y2="390" stroke="#D8CBCD" stroke-width="1.8" opacity="0.4" />
  <line x1="280" y1="150" x2="820" y2="364" stroke="#D8CBCD" stroke-width="1.8" opacity="0.4" />
  <line x1="280" y1="204" x2="820" y2="230" stroke="#D8CBCD" stroke-width="1.8" opacity="0.4" />
  <line x1="280" y1="230" x2="820" y2="284" stroke="#D8CBCD" stroke-width="1.8" opacity="0.4" />
  <line x1="280" y1="230" x2="820" y2="204" stroke="#D8CBCD" stroke-width="1.8" opacity="0.4" />
  <line x1="280" y1="230" x2="820" y2="204" stroke="#D8CBCD" stroke-width="1.8" opacity="0.4" />

  <!-- SOLO LAS 3 APROBADAS POR DOCENTE 1 SE RESALTAN EN ROJO CARMESÍ HEROICO -->
  <line x1="280" y1="176" x2="820" y2="364" stroke="#C9101B" stroke-width="5" />
  <line x1="280" y1="204" x2="820" y2="390" stroke="#C9101B" stroke-width="5" />
  <line x1="280" y1="150" x2="820" y2="390" stroke="#C9101B" stroke-width="6.5" />

  <!-- Puntos del desplome -->
  <circle cx="280" cy="150" r="9" fill="#460811" />
  <circle cx="280" cy="176" r="8" fill="#460811" />
  <circle cx="280" cy="204" r="8" fill="#460811" />

  <circle cx="820" cy="364" r="8" fill="#C9101B" />
  <circle cx="820" cy="390" r="10.5" fill="#C9101B" />

  <!-- Etiqueta sobre la pendiente de mayor caída -->
  <text x="500" y="270" font-size="19" font-weight="900" fill="#C9101B" font-family="var(--font-sans)" transform="rotate(24 500,270)">Desplome directo a reprobación</text>
</svg>
'''

# ---------------------------------------------------------------------------
# SVG 3: Canvas Flotante / Ultra-Flat (Gráfico sin contenedor externo)
# ---------------------------------------------------------------------------
SVG_G1_C = SVG_G1_A

# -------------------------------------------------------------
# OPCION G1-A: Bicolor Contraste (Docente 1 vs Docente 2)
# -------------------------------------------------------------
CONTENT_G1_A = f'''
    <h2 class="s-lead-question" style="font-size: 38px; font-weight: 800; margin: 0; line-height: 1.2; color: #2C0509;">
      La prueba docente: cuando los evaluadores humanos discrepan del algoritmo
    </h2>

    <div style="display: grid; grid-template-columns: 1180px 1fr; gap: 36px; align-items: stretch;">
      
      <!-- CONTENEDOR DE GRÁFICA: Un solo cuadro exterior, sin cuadros adentro -->
      <div style="background: #FAF5F5; border: 2px solid #EAE0E1; border-left: 12px solid var(--c-wine-primary); padding: 24px 32px; display: flex; flex-direction: column; justify-content: space-between;">
        
        <div style="display: flex; justify-content: space-between; align-items: baseline;">
          <span style="font-family: var(--font-mono); font-size: 19px; font-weight: 800; color: var(--c-wine-primary); letter-spacing: 1.5px;">
            FIGURA 4 · CALIFICACIONES INDEPENDIENTES (N = 10)
          </span>
          <span style="font-family: var(--font-mono); font-size: 18px; font-weight: 700; color: var(--c-red-accent);">
            Caída de media: 3.33 &rarr; 1.93
          </span>
        </div>

        {SVG_G1_A}

        <!-- LEYENDA TOTALMENTE ABIERTA (Sin cuadro ni bordes internos) -->
        <div style="display: flex; justify-content: space-between; align-items: center; padding-top: 12px; border-top: 1.5px solid #EAE0E1;">
          <div style="display: flex; align-items: center; gap: 10px;">
            <div style="width: 26px; height: 6px; background: var(--c-wine-primary);"></div>
            <span style="font-family: var(--font-sans); font-size: 19px; font-weight: 800; color: #110103;">Aprobó Docente 1 (3 de 10)</span>
          </div>
          <div style="display: flex; align-items: center; gap: 10px;">
            <div style="width: 26px; height: 6px; background: var(--c-red-accent);"></div>
            <span style="font-family: var(--font-sans); font-size: 19px; font-weight: 800; color: #110103;">Aprobó Docente 2 (3 de 10)</span>
          </div>
          <div style="display: flex; align-items: center; gap: 10px;">
            <div style="width: 26px; height: 3px; background: #D2C5C7;"></div>
            <span style="font-family: var(--font-sans); font-size: 18px; font-weight: 600; color: #8D7A7D;">Reprobadas por ambos (4 de 10)</span>
          </div>
        </div>

      </div>

      <!-- COLUMNA DERECHA: TEXTO MÍNIMO ABSOLUTO (Solo cifras y veredictos en 1 línea) -->
      <div style="display: flex; flex-direction: column; justify-content: space-between; gap: 16px;">
        
        <!-- Métrica 1 -->
        <div style="background: #FAF5F5; border-left: 10px solid #B38600; padding: 24px; flex: 1; display: flex; flex-direction: column; justify-content: center;">
          <div style="font-family: var(--font-mono); font-size: 64px; font-weight: 900; color: #B38600; line-height: 1;">
            0 / 10
          </div>
          <div style="font-family: var(--font-sans); font-size: 24px; font-weight: 800; color: #110103; margin-top: 6px;">
            Coincidencias en Aula
          </div>
          <div style="font-family: var(--font-sans); font-size: 19px; color: #5D4A4D; font-weight: 600; margin-top: 4px;">
            Aprobaciones 100% disjuntas.
          </div>
        </div>

        <!-- Métrica 2 -->
        <div style="background: #FAF5F5; border-left: 10px solid var(--c-red-accent); padding: 24px; flex: 1; display: flex; flex-direction: column; justify-content: center;">
          <div style="font-family: var(--font-mono); font-size: 52px; font-weight: 900; color: var(--c-red-accent); line-height: 1;">
            &kappa; = -0.429
          </div>
          <div style="font-family: var(--font-sans); font-size: 24px; font-weight: 800; color: #110103; margin-top: 6px;">
            Desacuerdo Severo
          </div>
          <div style="font-family: var(--font-sans); font-size: 19px; color: #5D4A4D; font-weight: 600; margin-top: 4px;">
            Kappa de Cohen negativo.
          </div>
        </div>

        <!-- Métrica 3 -->
        <div style="background: #FAF5F5; border-left: 10px solid var(--c-wine-primary); padding: 24px; flex: 1; display: flex; flex-direction: column; justify-content: center;">
          <div style="font-family: var(--font-mono); font-size: 46px; font-weight: 900; color: var(--c-wine-primary); line-height: 1;">
            &rho; &le; +0.26
          </div>
          <div style="font-family: var(--font-sans); font-size: 24px; font-weight: 800; color: #110103; margin-top: 6px;">
            Correlación Nula
          </div>
          <div style="font-family: var(--font-sans); font-size: 19px; color: #5D4A4D; font-weight: 600; margin-top: 4px;">
            Sin relación con algoritmo (<span style="font-family: var(--font-mono); font-weight: 700;">p &gt; 0.40</span>).
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
# OPCION G1-B: Desplome Focal (Solo D1 resaltado, 7 en Gris)
# -------------------------------------------------------------
CONTENT_G1_B = f'''
    <h2 class="s-lead-question" style="font-size: 38px; font-weight: 800; margin: 0; line-height: 1.2; color: #2C0509;">
      La prueba docente: cuando los evaluadores humanos discrepan del algoritmo
    </h2>

    <div style="display: grid; grid-template-columns: 1180px 1fr; gap: 36px; align-items: stretch;">
      
      <!-- CONTENEDOR DE GRÁFICA -->
      <div style="background: #FAF5F5; border: 2px solid #EAE0E1; border-left: 12px solid var(--c-wine-primary); padding: 24px 32px; display: flex; flex-direction: column; justify-content: space-between;">
        
        <div style="display: flex; justify-content: space-between; align-items: baseline;">
          <span style="font-family: var(--font-mono); font-size: 19px; font-weight: 800; color: var(--c-wine-primary); letter-spacing: 1.5px;">
            FIGURA 4 · LO QUE DOCENTE 1 APRUEBA, DOCENTE 2 LO REPRUEBA
          </span>
          <span style="font-family: var(--font-mono); font-size: 18px; font-weight: 700; color: var(--c-red-accent);">
            Caída de media: 3.33 &rarr; 1.93
          </span>
        </div>

        {SVG_G1_B}

        <!-- LEYENDA ABIERTA -->
        <div style="display: flex; justify-content: space-between; align-items: center; padding-top: 12px; border-top: 1.5px solid #EAE0E1;">
          <div style="display: flex; align-items: center; gap: 10px;">
            <div style="width: 28px; height: 6px; background: var(--c-red-accent);"></div>
            <span style="font-family: var(--font-sans); font-size: 19px; font-weight: 800; color: #110103;">Respuestas aprobadas por Docente 1 que Docente 2 reprueba (1.0)</span>
          </div>
          <div style="display: flex; align-items: center; gap: 10px;">
            <div style="width: 28px; height: 3px; background: #D8CBCD;"></div>
            <span style="font-family: var(--font-sans); font-size: 18px; font-weight: 600; color: #8D7A7D;">Resto de respuestas evaluadas (7)</span>
          </div>
        </div>

      </div>

      <!-- COLUMNA DERECHA: TEXTO MÍNIMO ABSOLUTO -->
      <div style="display: flex; flex-direction: column; justify-content: space-between; gap: 16px;">
        
        <!-- Métrica 1 -->
        <div style="background: #FAF5F5; border-left: 10px solid #B38600; padding: 24px; flex: 1; display: flex; flex-direction: column; justify-content: center;">
          <div style="font-family: var(--font-mono); font-size: 64px; font-weight: 900; color: #B38600; line-height: 1;">
            0 / 10
          </div>
          <div style="font-family: var(--font-sans); font-size: 24px; font-weight: 800; color: #110103; margin-top: 6px;">
            Coincidencias en Aula
          </div>
          <div style="font-family: var(--font-sans); font-size: 19px; color: #5D4A4D; font-weight: 600; margin-top: 4px;">
            Aprobaciones 100% disjuntas.
          </div>
        </div>

        <!-- Métrica 2 -->
        <div style="background: #FAF5F5; border-left: 10px solid var(--c-red-accent); padding: 24px; flex: 1; display: flex; flex-direction: column; justify-content: center;">
          <div style="font-family: var(--font-mono); font-size: 52px; font-weight: 900; color: var(--c-red-accent); line-height: 1;">
            &kappa; = -0.429
          </div>
          <div style="font-family: var(--font-sans); font-size: 24px; font-weight: 800; color: #110103; margin-top: 6px;">
            Desacuerdo Severo
          </div>
          <div style="font-family: var(--font-sans); font-size: 19px; color: #5D4A4D; font-weight: 600; margin-top: 4px;">
            Kappa de Cohen negativo.
          </div>
        </div>

        <!-- Métrica 3 -->
        <div style="background: #FAF5F5; border-left: 10px solid var(--c-wine-primary); padding: 24px; flex: 1; display: flex; flex-direction: column; justify-content: center;">
          <div style="font-family: var(--font-mono); font-size: 46px; font-weight: 900; color: var(--c-wine-primary); line-height: 1;">
            &rho; &le; +0.26
          </div>
          <div style="font-family: var(--font-sans); font-size: 24px; font-weight: 800; color: #110103; margin-top: 6px;">
            Correlación Nula
          </div>
          <div style="font-family: var(--font-sans); font-size: 19px; color: #5D4A4D; font-weight: 600; margin-top: 4px;">
            Sin relación con algoritmo (<span style="font-family: var(--font-mono); font-weight: 700;">p &gt; 0.40</span>).
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
# OPCION G1-C: Canvas Abierto / Ultra-Flat (Gráfica sin recuadro exterior)
# -------------------------------------------------------------
CONTENT_G1_C = f'''
    <h2 class="s-lead-question" style="font-size: 38px; font-weight: 800; margin: 0; line-height: 1.2; color: #2C0509;">
      La prueba docente: cuando los evaluadores humanos discrepan del algoritmo
    </h2>

    <div style="display: grid; grid-template-columns: 1180px 1fr; gap: 40px; align-items: stretch;">
      
      <!-- CONTENEDOR 100% FLAT (Cero cajas ni bordes, lienzo libre y puro) -->
      <div style="display: flex; flex-direction: column; justify-content: space-between; padding: 10px 0;">
        
        <div style="display: flex; justify-content: space-between; align-items: baseline; border-bottom: 2px solid var(--c-wine-primary); padding-bottom: 10px;">
          <span style="font-family: var(--font-mono); font-size: 19px; font-weight: 800; color: var(--c-wine-primary); letter-spacing: 1.5px;">
            FIGURA 4 · CALIFICACIONES INDEPENDIENTES (N = 10)
          </span>
          <span style="font-family: var(--font-mono); font-size: 18px; font-weight: 700; color: var(--c-red-accent);">
            Caída de media: 3.33 &rarr; 1.93
          </span>
        </div>

        {SVG_G1_C}

        <!-- LEYENDA ABIERTA -->
        <div style="display: flex; justify-content: space-between; align-items: center; padding-top: 14px; border-top: 1.5px solid #EAE0E1;">
          <div style="display: flex; align-items: center; gap: 10px;">
            <div style="width: 26px; height: 6px; background: var(--c-wine-primary);"></div>
            <span style="font-family: var(--font-sans); font-size: 19px; font-weight: 800; color: #110103;">Aprobó Docente 1 (3 de 10)</span>
          </div>
          <div style="display: flex; align-items: center; gap: 10px;">
            <div style="width: 26px; height: 6px; background: var(--c-red-accent);"></div>
            <span style="font-family: var(--font-sans); font-size: 19px; font-weight: 800; color: #110103;">Aprobó Docente 2 (3 de 10)</span>
          </div>
          <div style="display: flex; align-items: center; gap: 10px;">
            <div style="width: 26px; height: 3px; background: #D2C5C7;"></div>
            <span style="font-family: var(--font-sans); font-size: 18px; font-weight: 600; color: #8D7A7D;">Reprobadas por ambos (4 de 10)</span>
          </div>
        </div>

      </div>

      <!-- COLUMNA DERECHA: TARJETAS MINIMALISTAS -->
      <div style="display: flex; flex-direction: column; justify-content: space-between; gap: 16px;">
        
        <!-- Métrica 1 -->
        <div style="background: #FAF5F5; border-left: 10px solid #B38600; padding: 24px; flex: 1; display: flex; flex-direction: column; justify-content: center;">
          <div style="font-family: var(--font-mono); font-size: 64px; font-weight: 900; color: #B38600; line-height: 1;">
            0 / 10
          </div>
          <div style="font-family: var(--font-sans); font-size: 24px; font-weight: 800; color: #110103; margin-top: 6px;">
            Coincidencias en Aula
          </div>
          <div style="font-family: var(--font-sans); font-size: 19px; color: #5D4A4D; font-weight: 600; margin-top: 4px;">
            Aprobaciones 100% disjuntas.
          </div>
        </div>

        <!-- Métrica 2 -->
        <div style="background: #FAF5F5; border-left: 10px solid var(--c-red-accent); padding: 24px; flex: 1; display: flex; flex-direction: column; justify-content: center;">
          <div style="font-family: var(--font-mono); font-size: 52px; font-weight: 900; color: var(--c-red-accent); line-height: 1;">
            &kappa; = -0.429
          </div>
          <div style="font-family: var(--font-sans); font-size: 24px; font-weight: 800; color: #110103; margin-top: 6px;">
            Desacuerdo Severo
          </div>
          <div style="font-family: var(--font-sans); font-size: 19px; color: #5D4A4D; font-weight: 600; margin-top: 4px;">
            Kappa de Cohen negativo.
          </div>
        </div>

        <!-- Métrica 3 -->
        <div style="background: #FAF5F5; border-left: 10px solid var(--c-wine-primary); padding: 24px; flex: 1; display: flex; flex-direction: column; justify-content: center;">
          <div style="font-family: var(--font-mono); font-size: 46px; font-weight: 900; color: var(--c-wine-primary); line-height: 1;">
            &rho; &le; +0.26
          </div>
          <div style="font-family: var(--font-sans); font-size: 24px; font-weight: 800; color: #110103; margin-top: 6px;">
            Correlación Nula
          </div>
          <div style="font-family: var(--font-sans); font-size: 19px; color: #5D4A4D; font-weight: 600; margin-top: 4px;">
            Sin relación con algoritmo (<span style="font-family: var(--font-mono); font-weight: 700;">p &gt; 0.40</span>).
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

HTML_TEMPLATE = '''<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Test Slide 15 Declutter Master</title>
  <link rel="stylesheet" href="http://localhost:8085/styles.css?v=27">
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

        <div class="slide-content-area" style="top: 175px; height: 720px; justify-content: center; gap: 24px;">
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
        ('slide_15_master_A.html', 'slide_15_master_A.png', CONTENT_G1_A),
        ('slide_15_master_B.html', 'slide_15_master_B.png', CONTENT_G1_B),
        ('slide_15_master_C.html', 'slide_15_master_C.png', CONTENT_G1_C),
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
