# -*- coding: utf-8 -*-
"""
Test de soluciones de Alto Impacto sobre Fondo Claro para la Conclusión Pedagógica:
- K1: Fondo Blanco Puro (#FFFFFF) + Borde continuo de 3px + Acento lateral de 12px vinotinto + Badge institucional.
- K2: Fondo Suave (#FAF5F5) con Marco Vinotinto de 2px + Badge en bloque vinotinto sólido + Texto en negro carbón a 24px.
- K3: Franja Tono Resaltado (#FDE8E9) con Borde Rojo Carmesí de 2px + Barra lateral de 8px + Texto a 24px ultra-nítido.
"""
import os
from playwright.sync_api import sync_playwright

output_dir = r"C:\Users\ASUS\.gemini\antigravity-ide\brain\a6624504-511c-4b9d-bc9a-468e348bde40"
os.makedirs(output_dir, exist_ok=True)

BASE_CONTENT = '''
    <h2 class="s-lead-question" style="font-size: 38px; font-weight: 800; margin: 0; line-height: 1.2; color: #2C0509;">
      Alucinación frente a sobre-rechazo: cómo fallan dos modelos con la misma nota
    </h2>

    <!-- FILA 1: PHI-4-MINI -->
    <div style="background: #FAF5F5; border-left: 10px solid var(--c-wine-primary); padding: 26px 36px; display: grid; grid-template-columns: 460px 1fr 1fr; gap: 44px; align-items: center;">
      <div style="border-right: 2px solid #EAE0E1; padding-right: 32px;">
        <div style="font-family: var(--font-mono); font-size: 19px; font-weight: 700; color: var(--c-wine-primary); letter-spacing: 1.5px; margin-bottom: 2px;">
          PERFIL PERMISIVO · Q = 0.8030
        </div>
        <div style="font-family: var(--font-sans); font-size: 40px; font-weight: 800; color: #2C0509; line-height: 1.1; margin-bottom: 6px;">
          Phi-4-mini <span style="font-size: 26px; font-weight: 600; color: #5D4A4D;">3.8B</span>
        </div>
        <div style="font-family: var(--font-sans); font-size: 22px; font-weight: 700; color: #110103;">
          <strong style="color: var(--c-wine-primary);">Aula asistida:</strong> con docente activo.
        </div>
      </div>

      <div>
        <div style="display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 6px;">
          <span style="font-family: var(--font-sans); font-size: 22px; font-weight: 700; color: #2C0509;">Rechazo en trampas (14):</span>
          <span style="font-family: var(--font-mono); font-size: 40px; font-weight: 800; color: var(--c-red-accent); line-height: 1;">28.6%</span>
        </div>
        <div style="background: #EAE0E1; height: 30px; width: 100%; margin-bottom: 6px;">
          <div style="width: 28.6%; background: var(--c-red-accent); height: 100%;"></div>
        </div>
        <div style="font-family: var(--font-sans); font-size: 20px; color: var(--c-red-accent); font-weight: 700;">
          Alucina en 10 casos fuera del libro.
        </div>
      </div>

      <div>
        <div style="display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 6px;">
          <span style="font-family: var(--font-sans); font-size: 22px; font-weight: 700; color: #2C0509;">Falso rechazo (84 válidas):</span>
          <span style="font-family: var(--font-mono); font-size: 40px; font-weight: 800; color: var(--c-wine-primary); line-height: 1;">0.0%</span>
        </div>
        <div style="background: #EAE0E1; height: 30px; width: 100%; margin-bottom: 6px;">
          <div style="width: 0%; background: var(--c-wine-primary); height: 100%;"></div>
        </div>
        <div style="font-family: var(--font-sans); font-size: 20px; color: var(--c-wine-primary); font-weight: 700;">
          Fluidez total; jamás frena al alumno.
        </div>
      </div>
    </div>

    <!-- FILA 2: QWEN2.5-3B -->
    <div style="background: #FAF5F5; border-left: 10px solid var(--c-red-accent); padding: 26px 36px; display: grid; grid-template-columns: 460px 1fr 1fr; gap: 44px; align-items: center;">
      <div style="border-right: 2px solid #EAE0E1; padding-right: 32px;">
        <div style="font-family: var(--font-mono); font-size: 19px; font-weight: 700; color: var(--c-red-accent); letter-spacing: 1.5px; margin-bottom: 2px;">
          PERFIL CONSERVADOR · Q = 0.8010
        </div>
        <div style="font-family: var(--font-sans); font-size: 40px; font-weight: 800; color: #2C0509; line-height: 1.1; margin-bottom: 6px;">
          Qwen2.5-3B <span style="font-size: 26px; font-weight: 600; color: #5D4A4D;">3.1B</span>
        </div>
        <div style="font-family: var(--font-sans); font-size: 22px; font-weight: 700; color: #110103;">
          <strong style="color: var(--c-red-accent);">Autoestudio:</strong> sin docente presente.
        </div>
      </div>

      <div>
        <div style="display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 6px;">
          <span style="font-family: var(--font-sans); font-size: 22px; font-weight: 700; color: #2C0509;">Rechazo en trampas (14):</span>
          <span style="font-family: var(--font-mono); font-size: 40px; font-weight: 800; color: var(--c-wine-primary); line-height: 1;">85.7%</span>
        </div>
        <div style="background: #EAE0E1; height: 30px; width: 100%; margin-bottom: 6px;">
          <div style="width: 85.7%; background: var(--c-wine-primary); height: 100%;"></div>
        </div>
        <div style="font-family: var(--font-sans); font-size: 20px; color: var(--c-wine-primary); font-weight: 700;">
          Filtro riguroso frente a trampas.
        </div>
      </div>

      <div>
        <div style="display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 6px;">
          <span style="font-family: var(--font-sans); font-size: 22px; font-weight: 700; color: #2C0509;">Falso rechazo (84 válidas):</span>
          <span style="font-family: var(--font-mono); font-size: 40px; font-weight: 800; color: var(--c-red-accent); line-height: 1;">7.1%</span>
        </div>
        <div style="background: #EAE0E1; height: 30px; width: 100%; margin-bottom: 6px;">
          <div style="width: 25%; background: var(--c-red-accent); height: 100%;"></div>
        </div>
        <div style="font-family: var(--font-sans); font-size: 20px; color: var(--c-red-accent); font-weight: 700;">
          Sobre-rechazo por cautela extrema.
        </div>
      </div>
    </div>
'''

# -----------------------------------------------------------------------------
# REMATE K1: Fondo Blanco Puro + Borde Vinotinto 3px + Acento Lateral 12px + Texto 24px
# -----------------------------------------------------------------------------
REMATE_K1 = '''
    <div style="background: #FFFFFF; border: 2.5px solid var(--c-wine-primary); border-left: 12px solid var(--c-wine-primary); padding: 16px 28px; display: flex; justify-content: space-between; align-items: center; box-shadow: 0 4px 14px rgba(70, 8, 17, 0.08);">
      <div style="display: flex; align-items: center; gap: 16px;">
        <span style="font-family: var(--font-mono); font-size: 19px; font-weight: 800; color: #FFFFFF; background: var(--c-wine-primary); padding: 5px 14px; letter-spacing: 1.5px; white-space: nowrap;">
          CONCLUSIÓN
        </span>
        <span style="font-family: var(--font-sans); font-size: 24px; font-weight: 800; color: #110103; line-height: 1.25;">
          Modelos con idéntica nota numérica exigen entornos de despliegue completamente distintos.
        </span>
      </div>
      <span style="font-family: var(--font-mono); font-size: 19px; font-weight: 700; color: #5D4A4D; white-space: nowrap; margin-left: 24px;">
        Tabla 3 (×4 semillas)
      </span>
    </div>
'''

# -----------------------------------------------------------------------------
# REMATE K2: Fondo Suave #FAF5F5 + Doble Línea Vinotinto (Top y Bottom 3px) + Tipografía 25px
# -----------------------------------------------------------------------------
REMATE_K2 = '''
    <div style="background: #FAF5F5; border-top: 3px solid var(--c-wine-primary); border-bottom: 3px solid var(--c-wine-primary); padding: 16px 28px; display: flex; justify-content: space-between; align-items: center;">
      <span style="font-family: var(--font-sans); font-size: 24px; font-weight: 800; color: #110103; line-height: 1.3;">
        <strong style="color: var(--c-wine-primary); font-family: var(--font-mono); letter-spacing: 1.5px; font-size: 22px; margin-right: 12px;">CONCLUSIÓN PEDAGÓGICA:</strong> Modelos con idéntica nota numérica exigen entornos de despliegue completamente distintos.
      </span>
      <span style="font-family: var(--font-mono); font-size: 19px; font-weight: 700; color: #5D4A4D; white-space: nowrap; margin-left: 24px;">
        Tabla 3 del paper
      </span>
    </div>
'''

# -----------------------------------------------------------------------------
# REMATE K3: Fondo Suavemente Teñido #FDE8E9 + Borde Rojo Carmesí + Barra 8px
# -----------------------------------------------------------------------------
REMATE_K3 = '''
    <div style="background: #FDF0F1; border: 2px solid var(--c-wine-primary); border-left: 10px solid var(--c-red-accent); padding: 16px 28px; display: flex; justify-content: space-between; align-items: center;">
      <div style="display: flex; align-items: center; gap: 16px;">
        <span style="font-family: var(--font-mono); font-size: 19px; font-weight: 800; color: var(--c-red-accent); background: #FFFFFF; border: 1.5px solid var(--c-red-accent); padding: 5px 12px; letter-spacing: 1.5px; white-space: nowrap;">
          CONCLUSIÓN CLAVE
        </span>
        <span style="font-family: var(--font-sans); font-size: 24px; font-weight: 800; color: #110103; line-height: 1.25;">
          Modelos con idéntica nota numérica exigen entornos de despliegue completamente distintos.
        </span>
      </div>
      <span style="font-family: var(--font-mono); font-size: 19px; font-weight: 700; color: #5D4A4D; white-space: nowrap; margin-left: 24px;">
        Tabla 3 (×4 semillas)
      </span>
    </div>
'''

HTML_TEMPLATE = '''<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Test Slide 14 High Contrast Light</title>
  <link rel="stylesheet" href="http://localhost:8085/styles.css?v=26">
</head>
<body style="margin: 0; padding: 0; background: #0b0103;">

  <div id="presentation-viewport">
    <div id="slides-stage">
      <section class="slide s-white active">
        <header class="slide-header">
          <div class="sh-left">
            <span class="sh-red-bar"></span>
            <span class="sh-category">03 · RESULTADOS · MODOS DE FALLO ASIMÉTRICOS</span>
          </div>
          <img src="http://localhost:8085/assets/image6.png" alt="#LoxTIC" class="sh-loxtic">
        </header>
        <div class="sh-divider"></div>

        <div class="slide-content-area" style="top: 175px; height: 720px; justify-content: center; gap: 24px;">
          {base_content}
          {remate}
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
        ('slide_14_remate_k1.html', 'slide_14_remate_k1.png', REMATE_K1),
        ('slide_14_remate_k2.html', 'slide_14_remate_k2.png', REMATE_K2),
        ('slide_14_remate_k3.html', 'slide_14_remate_k3.png', REMATE_K3),
    ]

    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(viewport={"width": 1920, "height": 1080})

        for html_name, png_name, remate in options:
            html_path = os.path.join(output_dir, html_name)
            png_path = os.path.join(output_dir, png_name)

            content = HTML_TEMPLATE.format(base_content=BASE_CONTENT, remate=remate)
            with open(html_path, 'w', encoding='utf-8') as f:
                f.write(content)

            page.goto(f"file:///{html_path.replace(os.sep, '/')}")
            page.wait_for_timeout(400)
            page.screenshot(path=png_path)
            print(f"Captured: {png_name}")

        browser.close()

if __name__ == '__main__':
    main()
