# -*- coding: utf-8 -*-
import os
from playwright.sync_api import sync_playwright

output_dir = r"C:\Users\ASUS\.gemini\antigravity-ide\brain\a6624504-511c-4b9d-bc9a-468e348bde40"
os.makedirs(output_dir, exist_ok=True)

# ==============================================================================
# OPCIÓN A: Editorial Claro con Dos Paneles Simétricos y QR Destacado
# ==============================================================================
HTML_OPCION_A = '''<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <title>Slide 20 - Opción A</title>
  <link rel="stylesheet" href="http://localhost:8085/styles.css?v=33">
</head>
<body style="margin: 0; padding: 0; background: #0b0103;">
  <div id="presentation-viewport">
    <div id="slides-stage">
      <section class="slide s-white active" id="slide-20">
        <header class="slide-header">
          <div class="sh-left">
            <span class="sh-red-bar"></span>
            <span class="sh-category">05 · CIERRE · PREGUNTAS Y CONTACTO</span>
          </div>
          <img src="http://localhost:8085/assets/image6.png" alt="#LoxTIC" class="sh-loxtic">
        </header>
        <div class="sh-divider"></div>

        <div class="slide-content-area" style="top: 175px; height: 720px; justify-content: space-between;">
          <div>
            <h2 class="s-lead-question" style="font-size: 42px; font-weight: 800; margin: 0; line-height: 1.15; color: #2C0509;">
              Gracias por su atención
            </h2>
            <div style="font-family: var(--font-sans); font-size: 24px; color: #5D4A4D; font-weight: 600; margin-top: 4px;">
              Democratización de la IA en aulas rurales sin conexión a internet · VI Congreso Internacional Cartagena 2026
            </div>
          </div>

          <div style="display: grid; grid-template-columns: 1.15fr 0.85fr; gap: 32px; flex: 1; margin-top: 16px; margin-bottom: 16px;">
            
            <!-- Columna Izquierda: Agradecimientos y Evaluadores -->
            <div style="background: #FAF5F5; border-top: 6px solid var(--c-wine-primary); padding: 24px 30px; display: flex; flex-direction: column; justify-content: space-between;">
              <div>
                <div style="font-family: var(--font-mono); font-size: 15px; font-weight: 800; color: var(--c-wine-primary); letter-spacing: 1.5px; margin-bottom: 8px;">
                  RECONOCIMIENTOS INSTITUCIONALES
                </div>
                <div style="font-family: var(--font-sans); font-size: 25px; font-weight: 800; color: #110103; margin-bottom: 4px;">
                  Institución Universitaria Colegio Mayor del Cauca
                </div>
                <div style="font-family: var(--font-sans); font-size: 21px; color: #4A3B3D; font-weight: 600; line-height: 1.35;">
                  Grupo de Investigación I+D Informática &nbsp;·&nbsp; Semillero de Investigación BETABIT.
                </div>
              </div>

              <div style="border-top: 1px solid #E8DCDE; padding-top: 14px; margin-top: 10px;">
                <div style="font-family: var(--font-mono); font-size: 15px; font-weight: 800; color: var(--c-red-accent); letter-spacing: 1.5px; margin-bottom: 6px;">
                  DOCENTES EVALUADORES (EVALUACIÓN A CIEGAS)
                </div>
                <div style="font-family: var(--font-sans); font-size: 23px; font-weight: 800; color: #110103; margin-bottom: 2px;">
                  Juan Pablo Machado Vélez &nbsp;&amp;&nbsp; Stevens Álvarez Domínguez
                </div>
                <div style="font-family: var(--font-sans); font-size: 20px; color: #5D4A4D; line-height: 1.35;">
                  Agradecimiento especial por su rigurosa calibración pedagógica independiente y juicio ciego en contexto real.
                </div>
              </div>

              <!-- Logos Organizadores -->
              <div style="border-top: 1.5px solid #EAE0E1; padding-top: 14px; margin-top: 10px; display: flex; align-items: center; justify-content: space-between;">
                <span style="font-family: var(--font-mono); font-size: 12px; font-weight: 800; color: #7C6A6D; letter-spacing: 1px;">ENTIDADES COORGANIZADORAS:</span>
                <div style="display: flex; gap: 28px; align-items: center;">
                  <img src="http://localhost:8085/assets/image8.png" alt="U. Distrital" style="height: 44px; width: auto; object-fit: contain;">
                  <img src="http://localhost:8085/assets/image9.png" alt="UTB" style="height: 32px; width: auto; object-fit: contain;">
                  <img src="http://localhost:8085/assets/image10.png" alt="U. de Cartagena" style="height: 44px; width: auto; object-fit: contain;">
                </div>
              </div>
            </div>

            <!-- Columna Derecha: Preguntas, Contacto & QR -->
            <div style="background: #FAF5F5; border-top: 6px solid var(--c-red-accent); padding: 24px 30px; display: flex; flex-direction: column; justify-content: space-between;">
              <div>
                <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 6px;">
                  <span style="font-family: var(--font-mono); font-size: 15px; font-weight: 800; color: var(--c-red-accent); letter-spacing: 1.5px;">
                    SESIÓN DE PREGUNTAS
                  </span>
                  <span style="background: #FDE8E8; color: var(--c-red-accent); font-family: var(--font-mono); font-size: 13px; font-weight: 800; padding: 2px 8px;">
                    EN VIVO
                  </span>
                </div>
                <div style="font-family: var(--font-sans); font-size: 24px; font-weight: 800; color: #110103;">
                  Diálogo y Discusión Abierta
                </div>
                <div style="font-family: var(--font-sans); font-size: 19px; color: #5D4A4D; margin-top: 2px;">
                  Cartagena de Indias · 28 al 30 de octubre de 2026
                </div>
              </div>

              <!-- Correos -->
              <div style="border-top: 1px solid #E8DCDE; padding-top: 12px; margin-top: 6px;">
                <div style="font-family: var(--font-mono); font-size: 13px; font-weight: 800; color: var(--c-wine-primary); letter-spacing: 1px; margin-bottom: 4px;">
                  CORRESPONDENCIA &amp; AUTORES:
                </div>
                <div style="font-family: var(--font-mono); font-size: 19px; font-weight: 700; color: #110103; line-height: 1.4;">
                  fabian.hoyos@colmayor.edu.co<br>
                  yeison.munoz@colmayor.edu.co
                </div>
              </div>

              <!-- Bloque QR -->
              <div style="background: #FAF0F2; border: 1.5px solid #D8B8BE; padding: 12px 16px; display: flex; align-items: center; gap: 18px; margin-top: 8px;">
                <img src="http://localhost:8085/assets/image7.png" alt="QR" style="height: 105px; width: 105px; object-fit: contain; background: #FFFFFF; padding: 4px; border: 1px solid #D8B8BE;">
                <div>
                  <div style="font-family: var(--font-mono); font-size: 18px; font-weight: 900; color: var(--c-wine-primary);">
                    LOHACEMOSXTIC.COM
                  </div>
                  <div style="font-family: var(--font-sans); font-size: 17px; color: #110103; line-height: 1.3; font-weight: 600; margin-top: 2px;">
                    Repositorio abierto, código fuente y datos del benchmark.
                  </div>
                </div>
              </div>
            </div>

          </div>

          <!-- Banner Inferior -->
          <div style="background: #FAF5F5; border-top: 3.5px solid var(--c-wine-primary); border-bottom: 3.5px solid var(--c-wine-primary); padding: 14px 28px; display: flex; align-items: center; justify-content: space-between;">
            <span style="font-family: var(--font-sans); font-size: 22px; font-weight: 600; color: #110103;">
              VI Congreso Internacional de Investigación Interdisciplinar &nbsp;·&nbsp; Cartagena de Indias, 2026
            </span>
            <span style="font-family: var(--font-mono); font-size: 16px; font-weight: 800; color: var(--c-wine-primary); letter-spacing: 1px;">
              CIERRE DE PONENCIA
            </span>
          </div>
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

# ==============================================================================
# OPCIÓN B: Hero Dark Vinotinto Institucional (Cierre Simétrico con Portada Slide 1)
# ==============================================================================
HTML_OPCION_B = '''<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <title>Slide 20 - Opción B</title>
  <link rel="stylesheet" href="http://localhost:8085/styles.css?v=33">
</head>
<body style="margin: 0; padding: 0; background: #0b0103;">
  <div id="presentation-viewport">
    <div id="slides-stage">
      <section class="slide s-cover active" id="slide-20" style="background: #32060D; position: relative; overflow: hidden;">
        
        <!-- Silueta sutil de la Torre de Cartagena a la derecha -->
        <img src="http://localhost:8085/assets/image1.png" alt="Torre" class="s1-tower-bg" style="opacity: 0.16;">

        <!-- Cabecera institucional oscura -->
        <header class="slide-header" style="border: none;">
          <div class="sh-left">
            <span class="sh-red-bar"></span>
            <span class="sh-category" style="color: var(--c-gold);">05 · CIERRE · PREGUNTAS Y DISCUSIÓN</span>
          </div>
          <img src="http://localhost:8085/assets/image6.png" alt="#LoxTIC" class="sh-loxtic">
        </header>
        <div style="height: 2px; background: rgba(245, 194, 27, 0.35); margin: 0 110px;"></div>

        <div class="slide-content-area" style="top: 175px; height: 720px; justify-content: space-between; z-index: 5;">
          
          <div>
            <div style="display: flex; align-items: center; gap: 14px; margin-bottom: 6px;">
              <span style="font-family: var(--font-mono); font-size: 18px; font-weight: 800; color: var(--c-gold); letter-spacing: 2px;">
                VI CONGRESO INTERNACIONAL CARTAGENA 2026
              </span>
            </div>
            <h1 style="font-family: var(--font-sans); font-size: 68px; font-weight: 800; color: #FFFFFF; line-height: 1.1; margin: 0;">
              Gracias por su atención
            </h1>
            <p style="font-family: var(--font-sans); font-size: 26px; color: rgba(255, 255, 255, 0.85); margin: 6px 0 0 0;">
              Democratización de la IA en aulas rurales sin conexión a internet
            </p>
          </div>

          <div style="display: grid; grid-template-columns: 1.1fr 0.9fr; gap: 32px; flex: 1; margin-top: 20px; margin-bottom: 20px;">
            
            <!-- Tarjeta Izquierda Oscura: Agradecimientos y Evaluadores -->
            <div style="background: rgba(255, 255, 255, 0.05); border: 1px solid rgba(255, 255, 255, 0.15); border-top: 4px solid var(--c-gold); padding: 24px 30px; display: flex; flex-direction: column; justify-content: space-between;">
              <div>
                <div style="font-family: var(--font-mono); font-size: 14px; font-weight: 800; color: var(--c-gold); letter-spacing: 1.5px; margin-bottom: 6px;">
                  RECONOCIMIENTOS INSTITUCIONALES
                </div>
                <div style="font-family: var(--font-sans); font-size: 25px; font-weight: 800; color: #FFFFFF; margin-bottom: 4px;">
                  Institución Universitaria Colegio Mayor del Cauca
                </div>
                <div style="font-family: var(--font-sans); font-size: 20px; color: rgba(255, 255, 255, 0.8); line-height: 1.35;">
                  Grupo I+D Informática &nbsp;·&nbsp; Semillero de Investigación BETABIT.
                </div>
              </div>

              <div style="border-top: 1px solid rgba(255, 255, 255, 0.12); padding-top: 12px; margin-top: 8px;">
                <div style="font-family: var(--font-mono); font-size: 14px; font-weight: 800; color: #FF9EAA; letter-spacing: 1.5px; margin-bottom: 4px;">
                  DOCENTES EVALUADORES (EVALUACIÓN A CIEGAS)
                </div>
                <div style="font-family: var(--font-sans); font-size: 22px; font-weight: 700; color: #FFFFFF;">
                  Juan Pablo Machado Vélez &nbsp;&amp;&nbsp; Stevens Álvarez Domínguez
                </div>
                <div style="font-family: var(--font-sans); font-size: 18px; color: rgba(255, 255, 255, 0.7); margin-top: 2px;">
                  Por su valiosa colaboración en la auditoría y calibración pedagógica en contexto real.
                </div>
              </div>

              <!-- Logos sobre fondo blanco nítido -->
              <div style="border-top: 1px solid rgba(255, 255, 255, 0.12); padding-top: 12px; margin-top: 8px; display: flex; align-items: center; justify-content: space-between;">
                <span style="font-family: var(--font-mono); font-size: 12px; font-weight: 700; color: rgba(255, 255, 255, 0.6);">COORGANIZADORES:</span>
                <div style="background: #FFFFFF; padding: 6px 14px; display: flex; gap: 20px; align-items: center;">
                  <img src="http://localhost:8085/assets/image8.png" alt="U. Distrital" style="height: 34px; width: auto; object-fit: contain;">
                  <img src="http://localhost:8085/assets/image9.png" alt="UTB" style="height: 26px; width: auto; object-fit: contain;">
                  <img src="http://localhost:8085/assets/image10.png" alt="U. de Cartagena" style="height: 34px; width: auto; object-fit: contain;">
                </div>
              </div>
            </div>

            <!-- Tarjeta Derecha Oscura: Preguntas, Contacto & QR Blanco -->
            <div style="background: rgba(255, 255, 255, 0.05); border: 1px solid rgba(255, 255, 255, 0.15); border-top: 4px solid var(--c-red-accent); padding: 24px 30px; display: flex; flex-direction: column; justify-content: space-between;">
              <div>
                <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 4px;">
                  <span style="font-family: var(--font-mono); font-size: 15px; font-weight: 800; color: var(--c-gold); letter-spacing: 1.5px;">
                    SESIÓN DE PREGUNTAS
                  </span>
                  <span style="background: var(--c-red-accent); color: #FFFFFF; font-family: var(--font-mono); font-size: 12px; font-weight: 800; padding: 2px 8px;">
                    MICRÓFONO ABIERTO
                  </span>
                </div>
                <div style="font-family: var(--font-sans); font-size: 22px; font-weight: 700; color: #FFFFFF;">
                  Espacio para preguntas y debate
                </div>
              </div>

              <!-- Correos -->
              <div style="border-top: 1px solid rgba(255, 255, 255, 0.12); padding-top: 10px; margin-top: 4px;">
                <div style="font-family: var(--font-mono); font-size: 13px; font-weight: 800; color: var(--c-gold); letter-spacing: 1px; margin-bottom: 4px;">
                  CORRESPONDENCIA &amp; AUTORES:
                </div>
                <div style="font-family: var(--font-mono); font-size: 19px; color: #FFFFFF; line-height: 1.4;">
                  fabian.hoyos@colmayor.edu.co<br>
                  yeison.munoz@colmayor.edu.co
                </div>
              </div>

              <!-- QR Card en Blanco Contrastado -->
              <div style="background: #FFFFFF; padding: 12px 16px; display: flex; align-items: center; gap: 16px; margin-top: 8px;">
                <img src="http://localhost:8085/assets/image7.png" alt="QR" style="height: 98px; width: 98px; object-fit: contain;">
                <div>
                  <div style="font-family: var(--font-mono); font-size: 18px; font-weight: 900; color: var(--c-wine-primary);">
                    LOHACEMOSXTIC.COM
                  </div>
                  <div style="font-family: var(--font-sans); font-size: 16px; color: #222; line-height: 1.25; font-weight: 600; margin-top: 2px;">
                    Repositorio de código abierto, datos y benchmark reproducible.
                  </div>
                </div>
              </div>
            </div>

          </div>

          <!-- Pie oscuro -->
          <div style="border-top: 1px solid rgba(255, 255, 255, 0.2); padding-top: 12px; display: flex; justify-content: space-between; align-items: center;">
            <span style="font-family: var(--font-sans); font-size: 20px; color: rgba(255, 255, 255, 0.7);">
              Cartagena de Indias · 28 al 30 de octubre de 2026
            </span>
            <span style="font-family: var(--font-mono); font-size: 16px; font-weight: 800; color: var(--c-gold);">
              LOHACEMOSXTIC.COM · SLM OFFLINE
            </span>
          </div>

        </div>

        <div class="slide-footer-rule" style="background: rgba(255,255,255,0.15);"></div>
        <footer class="slide-footer">
          <span class="sf-left" style="color: rgba(255,255,255,0.5);">VI CONGRESO CARTAGENA · 2026</span>
          <span class="sf-right" style="color: rgba(255,255,255,0.5);">LOHACEMOSXTIC.COM · SLM OFFLINE</span>
        </footer>
      </section>
    </div>
  </div>
</body>
</html>
'''

# ==============================================================================
# OPCIÓN C: Formato Editorial Claro con Gran Módulo de Preguntas & QR Horizontal
# ==============================================================================
HTML_OPCION_C = '''<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <title>Slide 20 - Opción C</title>
  <link rel="stylesheet" href="http://localhost:8085/styles.css?v=33">
</head>
<body style="margin: 0; padding: 0; background: #0b0103;">
  <div id="presentation-viewport">
    <div id="slides-stage">
      <section class="slide s-white active" id="slide-20">
        <header class="slide-header">
          <div class="sh-left">
            <span class="sh-red-bar"></span>
            <span class="sh-category">05 · CIERRE · SESIÓN DE PREGUNTAS</span>
          </div>
          <img src="http://localhost:8085/assets/image6.png" alt="#LoxTIC" class="sh-loxtic">
        </header>
        <div class="sh-divider"></div>

        <div class="slide-content-area" style="top: 175px; height: 720px; justify-content: space-between;">
          
          <!-- Bloque Superior: Título y Agradecimientos -->
          <div style="background: #FAF5F5; border-top: 6px solid var(--c-wine-primary); padding: 26px 36px;">
            <div style="display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 12px;">
              <h2 style="font-family: var(--font-sans); font-size: 44px; font-weight: 900; color: #110103; margin: 0; line-height: 1;">
                Gracias por su atención
              </h2>
              <span style="font-family: var(--font-mono); font-size: 16px; font-weight: 800; color: var(--c-wine-primary); letter-spacing: 1px;">
                VI CONGRESO CARTAGENA 2026
              </span>
            </div>
            
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 36px; border-top: 1px solid #EAE0E1; padding-top: 14px;">
              <div>
                <div style="font-family: var(--font-mono); font-size: 13px; font-weight: 800; color: var(--c-wine-primary); letter-spacing: 1px; margin-bottom: 2px;">
                  RECONOCIMIENTOS INSTITUCIONALES:
                </div>
                <div style="font-family: var(--font-sans); font-size: 22px; font-weight: 800; color: #110103;">
                  Institución Universitaria Colegio Mayor del Cauca
                </div>
                <div style="font-family: var(--font-sans); font-size: 19px; color: #4A3B3D; font-weight: 600;">
                  Grupo I+D Informática &nbsp;·&nbsp; Semillero BETABIT
                </div>
              </div>
              <div>
                <div style="font-family: var(--font-mono); font-size: 13px; font-weight: 800; color: var(--c-red-accent); letter-spacing: 1px; margin-bottom: 2px;">
                  DOCENTES EVALUADORES (EVALUACIÓN A CIEGAS):
                </div>
                <div style="font-family: var(--font-sans); font-size: 22px; font-weight: 800; color: #110103;">
                  Juan Pablo Machado Vélez &nbsp;&amp;&nbsp; Stevens Álvarez Domínguez
                </div>
                <div style="font-family: var(--font-sans); font-size: 19px; color: #5D4A4D;">
                  Calibración pedagógica y juicio ciego en contexto real
                </div>
              </div>
            </div>
          </div>

          <!-- Bloque Inferior: 3 Columnas (Logos + Preguntas + QR) -->
          <div style="display: grid; grid-template-columns: 1fr 1.3fr 1fr; gap: 24px; flex: 1; margin-top: 16px; margin-bottom: 16px;">
            
            <!-- Tarjeta 1: Entidades Coorganizadoras -->
            <div style="background: #FAF5F5; border: 1.5px solid #EAE0E1; padding: 18px 24px; display: flex; flex-direction: column; justify-content: space-between;">
              <div style="font-family: var(--font-mono); font-size: 13px; font-weight: 800; color: #5D4A4D; letter-spacing: 1px;">
                COORGANIZADORES
              </div>
              <div style="display: flex; flex-direction: column; gap: 14px; align-items: center; justify-content: center; flex: 1;">
                <img src="http://localhost:8085/assets/image8.png" alt="U. Distrital" style="height: 40px; width: auto; object-fit: contain;">
                <img src="http://localhost:8085/assets/image9.png" alt="UTB" style="height: 28px; width: auto; object-fit: contain;">
                <img src="http://localhost:8085/assets/image10.png" alt="U. de Cartagena" style="height: 40px; width: auto; object-fit: contain;">
              </div>
            </div>

            <!-- Tarjeta 2: Sesión de Preguntas y Contacto -->
            <div style="background: #FAF5F5; border-top: 4px solid var(--c-red-accent); border: 1.5px solid #EAE0E1; border-top: 4px solid var(--c-red-accent); padding: 18px 24px; display: flex; flex-direction: column; justify-content: space-between;">
              <div>
                <div style="font-family: var(--font-mono); font-size: 13px; font-weight: 800; color: var(--c-red-accent); letter-spacing: 1px; margin-bottom: 2px;">
                  SESIÓN DE PREGUNTAS
                </div>
                <div style="font-family: var(--font-sans); font-size: 26px; font-weight: 800; color: #110103;">
                  Diálogo Abierto
                </div>
              </div>
              <div style="border-top: 1px solid #EAE0E1; padding-top: 10px;">
                <div style="font-family: var(--font-mono); font-size: 12px; font-weight: 800; color: var(--c-wine-primary); margin-bottom: 2px;">
                  CORRESPONDENCIA:
                </div>
                <div style="font-family: var(--font-mono); font-size: 18px; font-weight: 700; color: #110103; line-height: 1.35;">
                  fabian.hoyos@colmayor.edu.co<br>
                  yeison.munoz@colmayor.edu.co
                </div>
              </div>
            </div>

            <!-- Tarjeta 3: QR Repositorio -->
            <div style="background: #FAF2F3; border: 1.5px solid #D8B8BE; padding: 18px 20px; display: flex; flex-direction: column; align-items: center; justify-content: center; text-align: center;">
              <img src="http://localhost:8085/assets/image7.png" alt="QR" style="height: 115px; width: 115px; object-fit: contain; background: #FFFFFF; padding: 4px; border: 1px solid #D8B8BE; margin-bottom: 8px;">
              <div style="font-family: var(--font-mono); font-size: 16px; font-weight: 900; color: var(--c-wine-primary);">
                LOHACEMOSXTIC.COM
              </div>
              <div style="font-family: var(--font-sans); font-size: 14px; color: #5D4A4D; margin-top: 2px; font-weight: 600;">
                Benchmark &amp; Recursos
              </div>
            </div>

          </div>

          <!-- Remate Inferior -->
          <div style="background: #FAF5F5; border-top: 3.5px solid var(--c-wine-primary); border-bottom: 3.5px solid var(--c-wine-primary); padding: 12px 28px; display: flex; align-items: center; justify-content: space-between;">
            <span style="font-family: var(--font-sans); font-size: 21px; font-weight: 600; color: #110103;">
              Artículo de investigación presentado en el VI Congreso Internacional de Investigación Interdisciplinar · Cartagena 2026
            </span>
            <span style="font-family: var(--font-mono); font-size: 15px; font-weight: 800; color: var(--c-wine-primary);">
              SLM OFFLINE
            </span>
          </div>
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
    variants = [
        ("slide20_opcion_a_editorial_claro", HTML_OPCION_A),
        ("slide20_opcion_b_hero_dark_vinotinto", HTML_OPCION_B),
        ("slide20_opcion_c_modulos_balanceados", HTML_OPCION_C),
    ]

    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(viewport={"width": 1920, "height": 1080})

        for name, html in variants:
            tmp_html = os.path.join(output_dir, f"{name}.html")
            tmp_png = os.path.join(output_dir, f"{name}.png")
            with open(tmp_html, "w", encoding="utf-8") as f:
                f.write(html)
            page.goto(f"file:///{tmp_html.replace(os.sep, '/')}")
            page.wait_for_timeout(400)
            page.screenshot(path=tmp_png)
            print(f"Generated {name}.png")

        browser.close()

if __name__ == '__main__':
    main()
