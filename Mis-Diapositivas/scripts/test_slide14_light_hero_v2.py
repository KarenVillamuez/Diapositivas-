# -*- coding: utf-8 -*-
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

# P1: Franja con Acento Lateral 10px Vinotinto + Marco 2px + Todo en 1 línea
REMATE_P1 = '''
    <div style="background: #FFFFFF; border: 2px solid var(--c-wine-primary); border-left: 12px solid var(--c-wine-primary); padding: 14px 24px; display: flex; justify-content: space-between; align-items: center; box-shadow: 0 4px 14px rgba(70, 8, 17, 0.06);">
      <div style="display: flex; align-items: center; gap: 14px;">
        <span style="font-family: var(--font-mono); font-size: 19px; font-weight: 800; color: var(--c-wine-primary); letter-spacing: 1.5px; white-space: nowrap;">
          CONCLUSIÓN PEDAGÓGICA:
        </span>
        <span style="font-family: var(--font-sans); font-size: 23px; font-weight: 700; color: #110103; white-space: nowrap;">
          Modelos con idéntica nota numérica exigen entornos de despliegue completamente distintos.
        </span>
      </div>
      <span style="font-family: var(--font-mono); font-size: 19px; font-weight: 700; color: #5D4A4D; white-space: nowrap; margin-left: 20px;">
        Tabla 3
      </span>
    </div>
'''

# P2: Franja Editorial con Doble Línea Superior e Inferior de 3px
REMATE_P2 = '''
    <div style="background: #FAF5F5; border-top: 3.5px solid var(--c-wine-primary); border-bottom: 3.5px solid var(--c-wine-primary); padding: 15px 24px; display: flex; justify-content: space-between; align-items: center;">
      <div style="display: flex; align-items: center; gap: 14px;">
        <span style="font-family: var(--font-mono); font-size: 19px; font-weight: 800; color: var(--c-wine-primary); letter-spacing: 1.5px; white-space: nowrap;">
          CONCLUSIÓN PEDAGÓGICA:
        </span>
        <span style="font-family: var(--font-sans); font-size: 23px; font-weight: 700; color: #110103; white-space: nowrap;">
          Modelos con idéntica nota numérica exigen entornos de despliegue completamente distintos.
        </span>
      </div>
      <span style="font-family: var(--font-mono); font-size: 19px; font-weight: 700; color: #5D4A4D; white-space: nowrap; margin-left: 20px;">
        Tabla 3 (×4 semillas)
      </span>
    </div>
'''

# P3: Marco Completo Suave con Badge Destacado en Cápsula Vino
REMATE_P3 = '''
    <div style="background: #FAF5F5; border: 2.5px solid var(--c-wine-primary); padding: 14px 24px; display: flex; justify-content: space-between; align-items: center;">
      <div style="display: flex; align-items: center; gap: 16px;">
        <span style="font-family: var(--font-mono); font-size: 18px; font-weight: 800; color: var(--c-wine-primary); background: #F0E6E8; border: 1.5px solid #D8C4C7; padding: 4px 12px; letter-spacing: 1.5px; white-space: nowrap;">
          CONCLUSIÓN PEDAGÓGICA
        </span>
        <span style="font-family: var(--font-sans); font-size: 23px; font-weight: 700; color: #110103; white-space: nowrap;">
          Modelos con idéntica nota numérica exigen entornos de despliegue completamente distintos.
        </span>
      </div>
      <span style="font-family: var(--font-mono); font-size: 19px; font-weight: 700; color: #5D4A4D; white-space: nowrap; margin-left: 20px;">
        Tabla 3 del paper
      </span>
    </div>
'''

HTML_TEMPLATE = '''<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Test Slide 14 Light Hero V2</title>
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
        ('slide_14_remate_p1.html', 'slide_14_remate_p1.png', REMATE_P1),
        ('slide_14_remate_p2.html', 'slide_14_remate_p2.png', REMATE_P2),
        ('slide_14_remate_p3.html', 'slide_14_remate_p3.png', REMATE_P3),
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
