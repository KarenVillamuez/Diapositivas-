# -*- coding: utf-8 -*-
import os
from playwright.sync_api import sync_playwright

output_dir = r"C:\Users\ASUS\.gemini\antigravity-ide\brain\a6624504-511c-4b9d-bc9a-468e348bde40"
os.makedirs(output_dir, exist_ok=True)

# ===========================================================================
# C-P1: Banda Inferior Destacada con Métrica Gigante (56px)
# Sentido de colores:
# - Fila Superior: CRITERIOS METODOLÓGICOS (Borde Pizarra/Editorial #5D4A4D + Acento Vino #800020)
# - Fila Inferior: MODELOS RECOMENDADOS (C3 = Vino Qwen, C4 = Rojo Phi)
# ===========================================================================
CONTENT_CP1 = '''
    <h2 class="s-lead-question" style="font-size: 38px; font-weight: 800; margin: 0; line-height: 1.2; color: #2C0509;">
      Apego al texto no es aprendizaje: criterios para auditar y desplegar tutores
    </h2>

    <div style="display: grid; grid-template-columns: 1fr 1fr; grid-template-rows: 1fr 1fr; gap: 24px; flex: 1; margin-top: 14px;">
      
      <!-- C1: El Diagnóstico Crítico (Rojo Alerta) -->
      <div style="background: #FAF5F5; border-top: 8px solid #C51625; padding: 24px 30px; display: flex; flex-direction: column; justify-content: space-between;">
        <div>
          <div style="font-family: var(--font-mono); font-size: 16px; font-weight: 800; color: #C51625; letter-spacing: 1.5px; margin-bottom: 6px;">
            CRITERIO 01 · EL RIESGO OCULTO
          </div>
          <div style="font-family: var(--font-sans); font-size: 32px; font-weight: 900; color: #110103; margin-bottom: 8px;">
            La Falacia del Promedio
          </div>
          <div style="font-family: var(--font-sans); font-size: 23px; color: #2C0509; line-height: 1.35; font-weight: 600;">
            El valor global premia la copia de palabras del libro, pero oculta que el tutor inventa respuestas erróneas cuando no sabe.
          </div>
        </div>
        
        <!-- Bloque Métrica Destacada -->
        <div style="background: #FFFFFF; border-left: 6px solid #C51625; padding: 10px 18px; display: flex; align-items: baseline; gap: 16px; margin-top: 8px;">
          <span style="font-family: var(--font-mono); font-size: 52px; font-weight: 900; color: #C51625; line-height: 1;">0.795</span>
          <span style="font-family: var(--font-sans); font-size: 19px; font-weight: 800; color: #110103;">Apego engañoso (no predice aprendizaje)</span>
        </div>
      </div>

      <!-- C2: La Regla Metodológica (Pizarra Neutral / Editorial) -->
      <div style="background: #FAF5F5; border-top: 8px solid #4A3B3D; padding: 24px 30px; display: flex; flex-direction: column; justify-content: space-between;">
        <div>
          <div style="font-family: var(--font-mono); font-size: 16px; font-weight: 800; color: #4A3B3D; letter-spacing: 1.5px; margin-bottom: 6px;">
            CRITERIO 02 · EL ESTÁNDAR TÉCNICO
          </div>
          <div style="font-family: var(--font-sans); font-size: 32px; font-weight: 900; color: #110103; margin-bottom: 8px;">
            Auditoría Desglosada
          </div>
          <div style="font-family: var(--font-sans); font-size: 23px; color: #2C0509; line-height: 1.35; font-weight: 600;">
            <strong style="color: #4A3B3D;">Prohibido calificar con nota única:</strong> una auditoría rigurosa exige evaluar por separado recuperación, fidelidad y rechazo.
          </div>
        </div>

        <!-- Bloque Métrica Destacada -->
        <div style="background: #FFFFFF; border-left: 6px solid #4A3B3D; padding: 10px 18px; display: flex; align-items: baseline; gap: 16px; margin-top: 8px;">
          <span style="font-family: var(--font-mono); font-size: 52px; font-weight: 900; color: #4A3B3D; line-height: 1;">3</span>
          <span style="font-family: var(--font-sans); font-size: 19px; font-weight: 800; color: #110103;">Dimensiones obligatorias independientes</span>
        </div>
      </div>

      <!-- C3: Qwen2.5-3B (Vino Institucional) -->
      <div style="background: #FAF5F5; border-top: 8px solid var(--c-wine-primary); padding: 24px 30px; display: flex; flex-direction: column; justify-content: space-between;">
        <div>
          <div style="font-family: var(--font-mono); font-size: 16px; font-weight: 800; color: var(--c-wine-primary); letter-spacing: 1.5px; margin-bottom: 6px;">
            DESPLIEGUE A · AUTOESTUDIO AUTÓNOMO
          </div>
          <div style="font-family: var(--font-sans); font-size: 32px; font-weight: 900; color: var(--c-wine-primary); margin-bottom: 8px;">
            Qwen2.5-3B: Prioridad Certeza
          </div>
          <div style="font-family: var(--font-sans); font-size: 23px; color: #2C0509; line-height: 1.35; font-weight: 600;">
            Sin profesor que supervise, inventar una respuesta deseduca al alumno. Es preferible que el tutor admita no saber.
          </div>
        </div>

        <!-- Bloque Métrica Destacada (IMPOSIBLE DE PERDERSE) -->
        <div style="background: #FFFFFF; border-left: 6px solid var(--c-wine-primary); padding: 10px 18px; display: flex; align-items: baseline; gap: 16px; margin-top: 8px;">
          <span style="font-family: var(--font-mono); font-size: 56px; font-weight: 900; color: var(--c-wine-primary); line-height: 1;">85.7%</span>
          <span style="font-family: var(--font-sans); font-size: 19px; font-weight: 800; color: #110103;">Rechazo certero ante preguntas trampa</span>
        </div>
      </div>

      <!-- C4: Phi-4-mini (Rojo Acento) -->
      <div style="background: #FAF5F5; border-top: 8px solid var(--c-red-accent); padding: 24px 30px; display: flex; flex-direction: column; justify-content: space-between;">
        <div>
          <div style="font-family: var(--font-mono); font-size: 16px; font-weight: 800; color: var(--c-red-accent); letter-spacing: 1.5px; margin-bottom: 6px;">
            DESPLIEGUE B · AULA ASISTIDA CON DOCENTE
          </div>
          <div style="font-family: var(--font-sans); font-size: 32px; font-weight: 900; color: var(--c-red-accent); margin-bottom: 8px;">
            Phi-4-mini: Prioridad Fluidez
          </div>
          <div style="font-family: var(--font-sans); font-size: 23px; color: #2C0509; line-height: 1.35; font-weight: 600;">
            En clase interactiva prima mantener el ritmo pedagógico: no frena al grupo y el docente corrige en vivo.
          </div>
        </div>

        <!-- Bloque Métrica Destacada (IMPOSIBLE DE PERDERSE) -->
        <div style="background: #FFFFFF; border-left: 6px solid var(--c-red-accent); padding: 10px 18px; display: flex; align-items: baseline; gap: 16px; margin-top: 8px;">
          <span style="font-family: var(--font-mono); font-size: 56px; font-weight: 900; color: var(--c-red-accent); line-height: 1;">0.0%</span>
          <span style="font-family: var(--font-sans); font-size: 19px; font-weight: 800; color: #110103;">Bloqueos al diálogo durante la sesión</span>
        </div>
      </div>

    </div>
'''

# ===========================================================================
# C-P2: Layout Split con Gran Columna Numérica a la Derecha (60px)
# Cada cuadrante tiene el número como ancla visual inmediata.
# ===========================================================================
CONTENT_CP2 = '''
    <h2 class="s-lead-question" style="font-size: 38px; font-weight: 800; margin: 0; line-height: 1.2; color: #2C0509;">
      Apego al texto no es aprendizaje: criterios para auditar y desplegar tutores
    </h2>

    <div style="display: grid; grid-template-columns: 1fr 1fr; grid-template-rows: 1fr 1fr; gap: 24px; flex: 1; margin-top: 14px;">
      
      <!-- C1 -->
      <div style="background: #FAF5F5; border-top: 8px solid #C51625; padding: 22px 28px; display: grid; grid-template-columns: 1fr 170px; gap: 20px; align-items: center;">
        <div>
          <div style="font-family: var(--font-mono); font-size: 15px; font-weight: 800; color: #C51625; letter-spacing: 1.5px; margin-bottom: 4px;">
            01 · EL RIESGO OCULTO
          </div>
          <div style="font-family: var(--font-sans); font-size: 30px; font-weight: 900; color: #110103; margin-bottom: 8px;">
            La Falacia del Promedio
          </div>
          <div style="font-family: var(--font-sans); font-size: 22px; color: #2C0509; line-height: 1.35; font-weight: 600;">
            Mide copia del libro, pero encubre que el tutor inventa falsedades cuando no sabe la respuesta.
          </div>
        </div>
        <div style="background: #FFFFFF; border-left: 4px solid #C51625; padding: 14px; text-align: center;">
          <div style="font-family: var(--font-mono); font-size: 48px; font-weight: 900; color: #C51625; line-height: 1;">0.795</div>
          <div style="font-family: var(--font-sans); font-size: 14px; font-weight: 800; color: #5D4A4D; margin-top: 6px;">Apego Engañoso</div>
        </div>
      </div>

      <!-- C2 -->
      <div style="background: #FAF5F5; border-top: 8px solid #4A3B3D; padding: 22px 28px; display: grid; grid-template-columns: 1fr 170px; gap: 20px; align-items: center;">
        <div>
          <div style="font-family: var(--font-mono); font-size: 15px; font-weight: 800; color: #4A3B3D; letter-spacing: 1.5px; margin-bottom: 4px;">
            02 · EL ESTÁNDAR TÉCNICO
          </div>
          <div style="font-family: var(--font-sans); font-size: 30px; font-weight: 900; color: #110103; margin-bottom: 8px;">
            Auditoría Desglosada
          </div>
          <div style="font-family: var(--font-sans); font-size: 22px; color: #2C0509; line-height: 1.35; font-weight: 600;">
            <strong>Prohibida la nota única:</strong> es obligatorio evaluar recuperación, fidelidad y rechazo por separado.
          </div>
        </div>
        <div style="background: #FFFFFF; border-left: 4px solid #4A3B3D; padding: 14px; text-align: center;">
          <div style="font-family: var(--font-mono); font-size: 48px; font-weight: 900; color: #4A3B3D; line-height: 1;">3</div>
          <div style="font-family: var(--font-sans); font-size: 14px; font-weight: 800; color: #5D4A4D; margin-top: 6px;">Dimensiones</div>
        </div>
      </div>

      <!-- C3 -->
      <div style="background: #FAF5F5; border-top: 8px solid var(--c-wine-primary); padding: 22px 28px; display: grid; grid-template-columns: 1fr 170px; gap: 20px; align-items: center;">
        <div>
          <div style="font-family: var(--font-mono); font-size: 15px; font-weight: 800; color: var(--c-wine-primary); letter-spacing: 1.5px; margin-bottom: 4px;">
            03 · SIN DOCENTE (AUTOESTUDIO)
          </div>
          <div style="font-family: var(--font-sans); font-size: 30px; font-weight: 900; color: var(--c-wine-primary); margin-bottom: 8px;">
            Qwen2.5-3B: Certeza
          </div>
          <div style="font-family: var(--font-sans); font-size: 22px; color: #2C0509; line-height: 1.35; font-weight: 600;">
            En soledad no hay profesor que corrija. Admitir no saber evita enseñar errores pedagógicos.
          </div>
        </div>
        <div style="background: #FFFFFF; border-left: 4px solid var(--c-wine-primary); padding: 14px; text-align: center;">
          <div style="font-family: var(--font-mono); font-size: 54px; font-weight: 900; color: var(--c-wine-primary); line-height: 1;">85.7%</div>
          <div style="font-family: var(--font-sans); font-size: 14px; font-weight: 800; color: var(--c-wine-primary); margin-top: 6px;">Rechazo Certero</div>
        </div>
      </div>

      <!-- C4 -->
      <div style="background: #FAF5F5; border-top: 8px solid var(--c-red-accent); padding: 22px 28px; display: grid; grid-template-columns: 1fr 170px; gap: 20px; align-items: center;">
        <div>
          <div style="font-family: var(--font-mono); font-size: 15px; font-weight: 800; color: var(--c-red-accent); letter-spacing: 1.5px; margin-bottom: 4px;">
            04 · CON DOCENTE (AULA)
          </div>
          <div style="font-family: var(--font-sans); font-size: 30px; font-weight: 900; color: var(--c-red-accent); margin-bottom: 8px;">
            Phi-4-mini: Fluidez
          </div>
          <div style="font-family: var(--font-sans); font-size: 22px; color: #2C0509; line-height: 1.35; font-weight: 600;">
            En clase prima no frenar la dinámica: interacción continua y el profesor modera en tiempo real.
          </div>
        </div>
        <div style="background: #FFFFFF; border-left: 4px solid var(--c-red-accent); padding: 14px; text-align: center;">
          <div style="font-family: var(--font-mono); font-size: 54px; font-weight: 900; color: var(--c-red-accent); line-height: 1;">0.0%</div>
          <div style="font-family: var(--font-sans); font-size: 14px; font-weight: 800; color: var(--c-red-accent); margin-top: 6px;">Bloqueos al Diálogo</div>
        </div>
      </div>

    </div>
'''

# ===========================================================================
# C-P3: Placas Heroicas Monolíticas (Fondo Sólido de Color para el Porcentaje)
# El porcentaje está en una placa de color saturado con tipografía blanca colosal.
# ===========================================================================
CONTENT_CP3 = '''
    <h2 class="s-lead-question" style="font-size: 38px; font-weight: 800; margin: 0; line-height: 1.2; color: #2C0509;">
      Apego al texto no es aprendizaje: criterios para auditar y desplegar tutores
    </h2>

    <div style="display: grid; grid-template-columns: 1fr 1fr; grid-template-rows: 1fr 1fr; gap: 24px; flex: 1; margin-top: 14px;">
      
      <!-- C1 -->
      <div style="background: #FAF5F5; border-top: 8px solid #C51625; padding: 24px 30px; display: flex; flex-direction: column; justify-content: space-between;">
        <div style="display: flex; justify-content: space-between; align-items: flex-start; gap: 16px;">
          <div>
            <div style="font-family: var(--font-mono); font-size: 16px; font-weight: 800; color: #C51625; letter-spacing: 1.5px; margin-bottom: 4px;">
              01 · EL RIESGO OCULTO
            </div>
            <div style="font-family: var(--font-sans); font-size: 30px; font-weight: 900; color: #110103;">
              La Falacia del Promedio
            </div>
          </div>
          <div style="background: #C51625; color: #FFFFFF; padding: 6px 14px; text-align: center; border-radius: 3px; min-width: 100px;">
            <div style="font-family: var(--font-mono); font-size: 32px; font-weight: 900; line-height: 1;">0.795</div>
            <div style="font-family: var(--font-sans); font-size: 11px; font-weight: 800; letter-spacing: 1px;">ENGAÑOSO</div>
          </div>
        </div>
        <div style="font-family: var(--font-sans); font-size: 24px; color: #2C0509; line-height: 1.35; font-weight: 600; margin-top: 8px;">
          El puntaje premia copiar del libro, pero encubre que el tutor inventa falsedades cuando no sabe la respuesta.
        </div>
      </div>

      <!-- C2 -->
      <div style="background: #FAF5F5; border-top: 8px solid #4A3B3D; padding: 24px 30px; display: flex; flex-direction: column; justify-content: space-between;">
        <div style="display: flex; justify-content: space-between; align-items: flex-start; gap: 16px;">
          <div>
            <div style="font-family: var(--font-mono); font-size: 16px; font-weight: 800; color: #4A3B3D; letter-spacing: 1.5px; margin-bottom: 4px;">
              02 · EL ESTÁNDAR TÉCNICO
            </div>
            <div style="font-family: var(--font-sans); font-size: 30px; font-weight: 900; color: #110103;">
              Auditoría Desglosada
            </div>
          </div>
          <div style="background: #4A3B3D; color: #FFFFFF; padding: 6px 14px; text-align: center; border-radius: 3px; min-width: 100px;">
            <div style="font-family: var(--font-mono); font-size: 32px; font-weight: 900; line-height: 1;">3</div>
            <div style="font-family: var(--font-sans); font-size: 11px; font-weight: 800; letter-spacing: 1px;">DIMENSIONES</div>
          </div>
        </div>
        <div style="font-family: var(--font-sans); font-size: 24px; color: #2C0509; line-height: 1.35; font-weight: 600; margin-top: 8px;">
          <strong>Prohibida la nota única:</strong> es obligatorio evaluar recuperación, fidelidad y rechazo por separado.
        </div>
      </div>

      <!-- C3 -->
      <div style="background: #FAF5F5; border-top: 8px solid var(--c-wine-primary); padding: 24px 30px; display: flex; flex-direction: column; justify-content: space-between;">
        <div style="display: flex; justify-content: space-between; align-items: flex-start; gap: 16px;">
          <div>
            <div style="font-family: var(--font-mono); font-size: 16px; font-weight: 800; color: var(--c-wine-primary); letter-spacing: 1.5px; margin-bottom: 4px;">
              03 · AUTOESTUDIO SIN DOCENTE
            </div>
            <div style="font-family: var(--font-sans); font-size: 30px; font-weight: 900; color: var(--c-wine-primary);">
              Qwen2.5-3B: Certeza
            </div>
          </div>
          <div style="background: var(--c-wine-primary); color: #FFFFFF; padding: 8px 18px; text-align: center; border-radius: 3px; min-width: 140px;">
            <div style="font-family: var(--font-mono); font-size: 40px; font-weight: 900; line-height: 1;">85.7%</div>
            <div style="font-family: var(--font-sans); font-size: 12px; font-weight: 800; letter-spacing: 1px;">RECHAZO</div>
          </div>
        </div>
        <div style="font-family: var(--font-sans); font-size: 24px; color: #2C0509; line-height: 1.35; font-weight: 600; margin-top: 8px;">
          En soledad no hay profesor que corrija. Admitir ignorancia es pedagógico; inventar deseduca.
        </div>
      </div>

      <!-- C4 -->
      <div style="background: #FAF5F5; border-top: 8px solid var(--c-red-accent); padding: 24px 30px; display: flex; flex-direction: column; justify-content: space-between;">
        <div style="display: flex; justify-content: space-between; align-items: flex-start; gap: 16px;">
          <div>
            <div style="font-family: var(--font-mono); font-size: 16px; font-weight: 800; color: var(--c-red-accent); letter-spacing: 1.5px; margin-bottom: 4px;">
              04 · AULA CON DOCENTE
            </div>
            <div style="font-family: var(--font-sans); font-size: 30px; font-weight: 900; color: var(--c-red-accent);">
              Phi-4-mini: Fluidez
            </div>
          </div>
          <div style="background: var(--c-red-accent); color: #FFFFFF; padding: 8px 18px; text-align: center; border-radius: 3px; min-width: 140px;">
            <div style="font-family: var(--font-mono); font-size: 40px; font-weight: 900; line-height: 1;">0.0%</div>
            <div style="font-family: var(--font-sans); font-size: 12px; font-weight: 800; letter-spacing: 1px;">BLOQUEOS</div>
          </div>
        </div>
        <div style="font-family: var(--font-sans); font-size: 24px; color: #2C0509; line-height: 1.35; font-weight: 600; margin-top: 8px;">
          En clase prima la interacción continua: no frena al grupo y el docente modera en tiempo real.
        </div>
      </div>

    </div>
'''

# ===========================================================================
# C-P1-Flat: Métrica Monumental Pura (Sin cajas anidadas, 100% plano)
# ===========================================================================
CONTENT_CP1_FLAT = '''
    <h2 class="s-lead-question" style="font-size: 38px; font-weight: 800; margin: 0; line-height: 1.2; color: #2C0509;">
      Apego al texto no es aprendizaje: criterios para auditar y desplegar tutores
    </h2>

    <div style="display: grid; grid-template-columns: 1fr 1fr; grid-template-rows: 1fr 1fr; gap: 24px; flex: 1; margin-top: 14px;">
      
      <!-- C1: El Diagnóstico Crítico (Rojo Alerta) -->
      <div style="background: #FAF5F5; border-top: 8px solid #C51625; padding: 24px 32px; display: flex; flex-direction: column; justify-content: space-between;">
        <div>
          <div style="font-family: var(--font-mono); font-size: 16px; font-weight: 800; color: #C51625; letter-spacing: 1.5px; margin-bottom: 6px;">
            CRITERIO 01 · EL RIESGO OCULTO
          </div>
          <div style="font-family: var(--font-sans); font-size: 32px; font-weight: 900; color: #110103; margin-bottom: 8px;">
            La Falacia del Promedio
          </div>
          <div style="font-family: var(--font-sans); font-size: 24px; color: #2C0509; line-height: 1.35; font-weight: 600;">
            El valor global premia la copia de palabras del libro, pero oculta que el tutor inventa respuestas erróneas cuando no sabe.
          </div>
        </div>
        
        <!-- Bloque Métrica Plano Directo -->
        <div style="display: flex; align-items: baseline; gap: 16px; border-top: 2px solid #E5D5D5; padding-top: 12px; margin-top: 8px;">
          <span style="font-family: var(--font-mono); font-size: 54px; font-weight: 900; color: #C51625; line-height: 1;">0.795</span>
          <span style="font-family: var(--font-sans); font-size: 20px; font-weight: 800; color: #110103;">Apego engañoso (no predice aprendizaje)</span>
        </div>
      </div>

      <!-- C2: La Regla Metodológica (Pizarra Neutral / Editorial) -->
      <div style="background: #FAF5F5; border-top: 8px solid #4A3B3D; padding: 24px 32px; display: flex; flex-direction: column; justify-content: space-between;">
        <div>
          <div style="font-family: var(--font-mono); font-size: 16px; font-weight: 800; color: #4A3B3D; letter-spacing: 1.5px; margin-bottom: 6px;">
            CRITERIO 02 · EL ESTÁNDAR TÉCNICO
          </div>
          <div style="font-family: var(--font-sans); font-size: 32px; font-weight: 900; color: #110103; margin-bottom: 8px;">
            Auditoría Desglosada
          </div>
          <div style="font-family: var(--font-sans); font-size: 24px; color: #2C0509; line-height: 1.35; font-weight: 600;">
            <strong style="color: #4A3B3D;">Prohibido calificar con nota única:</strong> una auditoría rigurosa exige evaluar por separado recuperación, fidelidad y rechazo.
          </div>
        </div>

        <!-- Bloque Métrica Plano Directo -->
        <div style="display: flex; align-items: baseline; gap: 16px; border-top: 2px solid #E5D5D5; padding-top: 12px; margin-top: 8px;">
          <span style="font-family: var(--font-mono); font-size: 54px; font-weight: 900; color: #4A3B3D; line-height: 1;">3</span>
          <span style="font-family: var(--font-sans); font-size: 20px; font-weight: 800; color: #110103;">Dimensiones obligatorias independientes</span>
        </div>
      </div>

      <!-- C3: Qwen2.5-3B (Vino Institucional) -->
      <div style="background: #FAF5F5; border-top: 8px solid var(--c-wine-primary); padding: 24px 32px; display: flex; flex-direction: column; justify-content: space-between;">
        <div>
          <div style="font-family: var(--font-mono); font-size: 16px; font-weight: 800; color: var(--c-wine-primary); letter-spacing: 1.5px; margin-bottom: 6px;">
            DESPLIEGUE A · AUTOESTUDIO AUTÓNOMO
          </div>
          <div style="font-family: var(--font-sans); font-size: 32px; font-weight: 900; color: var(--c-wine-primary); margin-bottom: 8px;">
            Qwen2.5-3B: Prioridad Certeza
          </div>
          <div style="font-family: var(--font-sans); font-size: 24px; color: #2C0509; line-height: 1.35; font-weight: 600;">
            Sin profesor que supervise, inventar una respuesta deseduca al alumno. Es preferible que el tutor admita no saber.
          </div>
        </div>

        <!-- Bloque Métrica Plano Directo -->
        <div style="display: flex; align-items: baseline; gap: 16px; border-top: 2px solid #E5D5D5; padding-top: 12px; margin-top: 8px;">
          <span style="font-family: var(--font-mono); font-size: 58px; font-weight: 900; color: var(--c-wine-primary); line-height: 1;">85.7%</span>
          <span style="font-family: var(--font-sans); font-size: 20px; font-weight: 800; color: #110103;">Rechazo certero ante preguntas trampa</span>
        </div>
      </div>

      <!-- C4: Phi-4-mini (Rojo Acento) -->
      <div style="background: #FAF5F5; border-top: 8px solid var(--c-red-accent); padding: 24px 32px; display: flex; flex-direction: column; justify-content: space-between;">
        <div>
          <div style="font-family: var(--font-mono); font-size: 16px; font-weight: 800; color: var(--c-red-accent); letter-spacing: 1.5px; margin-bottom: 6px;">
            DESPLIEGUE B · AULA ASISTIDA CON DOCENTE
          </div>
          <div style="font-family: var(--font-sans); font-size: 32px; font-weight: 900; color: var(--c-red-accent); margin-bottom: 8px;">
            Phi-4-mini: Prioridad Fluidez
          </div>
          <div style="font-family: var(--font-sans); font-size: 24px; color: #2C0509; line-height: 1.35; font-weight: 600;">
            En clase interactiva prima mantener el ritmo pedagógico: no frena al grupo y el docente corrige en vivo.
          </div>
        </div>

        <!-- Bloque Métrica Plano Directo -->
        <div style="display: flex; align-items: baseline; gap: 16px; border-top: 2px solid #E5D5D5; padding-top: 12px; margin-top: 8px;">
          <span style="font-family: var(--font-mono); font-size: 58px; font-weight: 900; color: var(--c-red-accent); line-height: 1;">0.0%</span>
          <span style="font-family: var(--font-sans); font-size: 20px; font-weight: 800; color: #110103;">Bloqueos al diálogo durante la sesión</span>
        </div>
      </div>

    </div>
'''

HTML_TEMPLATE = '''<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Test Slide 17 C Perfected</title>
  <link rel="stylesheet" href="http://localhost:8085/styles.css?v=33">
</head>
<body style="margin: 0; padding: 0; background: #0b0103;">

  <div id="presentation-viewport">
    <div id="slides-stage">
      <section class="slide s-white active">
        <header class="slide-header">
          <div class="sh-left">
            <span class="sh-red-bar"></span>
            <span class="sh-category">04 · DISCUSIÓN · GUÍA METODOLÓGICA DE ELECCIÓN</span>
          </div>
          <img src="http://localhost:8085/assets/image6.png" alt="#LoxTIC" class="sh-loxtic">
        </header>
        <div class="sh-divider"></div>

        <div class="slide-content-area" style="top: 175px; height: 720px; justify-content: space-between;">
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
        ('slide_17_cp1.html', 'slide_17_cp1.png', CONTENT_CP1),
        ('slide_17_cp1_flat.html', 'slide_17_cp1_flat.png', CONTENT_CP1_FLAT),
        ('slide_17_cp2.html', 'slide_17_cp2.png', CONTENT_CP2),
        ('slide_17_cp3.html', 'slide_17_cp3.png', CONTENT_CP3),
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
