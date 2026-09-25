# -*- coding: utf-8 -*-
"""
Test Slide 14 with official Microsoft and Alibaba Cloud tech logos and stamps.
"""
import os
from playwright.sync_api import sync_playwright

output_dir = r"C:\Users\ASUS\.gemini\antigravity-ide\brain\a6624504-511c-4b9d-bc9a-468e348bde40"

# SVG Logos
LOGO_MICROSOFT = '''<svg width="22" height="22" viewBox="0 0 21 21"><rect x="1" y="1" width="9" height="9" fill="#F25022"/><rect x="11" y="1" width="9" height="9" fill="#7FBA00"/><rect x="1" y="11" width="9" height="9" fill="#00A4EF"/><rect x="11" y="11" width="9" height="9" fill="#FFB900"/></svg>'''

LOGO_ALIBABA = '''<svg width="24" height="24" viewBox="0 0 24 24" fill="#FF6A00"><path d="M2.5 7.5C2.5 6.4 3.4 5.5 4.5 5.5H8V8H5v8h3v2.5H4.5c-1.1 0-2-.9-2-2v-9zm19 0c0-1.1-.9-2-2-2H16V8h3v8h-3v2.5h3.5c1.1 0 2-.9 2-2v-9zM7 10.75h10v2.5H7v-2.5z"/></svg>'''

html = f'''<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <link rel="stylesheet" href="http://localhost:8085/styles.css">
  <style>
    .tech-stamp {{
      display: inline-flex;
      align-items: center;
      gap: 8px;
      font-family: var(--font-mono);
      font-weight: 800;
      text-transform: uppercase;
      box-shadow: 0 4px 14px rgba(0,0,0,0.08);
      white-space: nowrap;
    }}
  </style>
</head>
<body style="margin: 0; padding: 0; background: #0b0103;">
  <div id="presentation-viewport">
    <div id="slides-stage">
      <section class="slide s-white active" id="slide-14">
        <header class="slide-header">
          <div class="sh-left">
            <span class="sh-red-bar"></span>
            <span class="sh-category">03 · RESULTADOS · MODOS DE FALLO ASIMÉTRICOS</span>
          </div>
          <img src="http://localhost:8085/assets/image6.png" alt="#LoxTIC" class="sh-loxtic">
        </header>
        <div class="sh-divider"></div>

        <div class="slide-content-area" style="top: 175px; height: 720px; justify-content: center; gap: 24px;">
          
          <h2 class="s-lead-question" style="font-size: 38px; font-weight: 800; margin: 0; line-height: 1.2; color: #2C0509;">
            Alucinación frente a sobre-rechazo: cómo fallan dos modelos con la misma nota
          </h2>

          <!-- FILA 1: PHI-4-MINI CON LOGO MICROSOFT & STAMP ASIMÉTRICO -->
          <div style="background: #FAF5F5; border-left: 10px solid var(--c-wine-primary); padding: 26px 36px; display: grid; grid-template-columns: 460px 1fr 1fr; gap: 44px; align-items: center; position: relative;">
            
            <!-- Stamp Asimétrico Microsoft / MIT License -->
            <div class="tech-stamp" style="position: absolute; top: -16px; right: 28px; background: #FAF0F2; color: var(--c-wine-primary); border: 2px solid var(--c-wine-primary); font-size: 13.5px; padding: 5px 14px; transform: rotate(2.5deg); z-index: 10;">
              {LOGO_MICROSOFT}
              <span>MICROSOFT RESEARCH &bull; LICENCIA MIT</span>
            </div>

            <div style="border-right: 2px solid #EAE0E1; padding-right: 32px;">
              <div style="font-family: var(--font-mono); font-size: 19px; font-weight: 700; color: var(--c-wine-primary); letter-spacing: 1.5px; margin-bottom: 2px;">
                PERFIL PERMISIVO · Q = 0.8030
              </div>
              <div style="display: flex; align-items: center; gap: 12px; margin-bottom: 6px;">
                <div style="font-family: var(--font-sans); font-size: 40px; font-weight: 800; color: #2C0509; line-height: 1.1;">
                  Phi-4-mini <span style="font-size: 26px; font-weight: 600; color: #5D4A4D;">3.8B</span>
                </div>
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

          <!-- FILA 2: QWEN2.5-3B CON LOGO ALIBABA & STAMP ASIMÉTRICO -->
          <div style="background: #FAF5F5; border-left: 10px solid var(--c-red-accent); padding: 26px 36px; display: grid; grid-template-columns: 460px 1fr 1fr; gap: 44px; align-items: center; position: relative;">
            
            <!-- Stamp Asimétrico Alibaba / Apache 2.0 -->
            <div class="tech-stamp" style="position: absolute; top: -16px; right: 28px; background: #FFF0F0; color: var(--c-red-accent); border: 2px solid var(--c-red-accent); font-size: 13.5px; padding: 5px 14px; transform: rotate(-2.5deg); z-index: 10;">
              {LOGO_ALIBABA}
              <span>ALIBABA CLOUD &bull; APACHE 2.0</span>
            </div>

            <div style="border-right: 2px solid #EAE0E1; padding-right: 32px;">
              <div style="font-family: var(--font-mono); font-size: 19px; font-weight: 700; color: var(--c-red-accent); letter-spacing: 1.5px; margin-bottom: 2px;">
                PERFIL CONSERVADOR · Q = 0.8010
              </div>
              <div style="display: flex; align-items: center; gap: 12px; margin-bottom: 6px;">
                <div style="font-family: var(--font-sans); font-size: 40px; font-weight: 800; color: #2C0509; line-height: 1.1;">
                  Qwen2.5-3B <span style="font-size: 26px; font-weight: 600; color: #5D4A4D;">3.1B</span>
                </div>
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

          <!-- REMATE EDITORIAL INFERIOR (OPCIÓN P2) -->
          <div style="background: #FAF5F5; border-top: 3.5px solid var(--c-wine-primary); border-bottom: 3.5px solid var(--c-wine-primary); padding: 15px 24px; display: flex; justify-content: space-between; align-items: center;">
            <div style="display: flex; align-items: center; gap: 14px;">
              <span style="font-family: var(--font-mono); font-size: 19px; font-weight: 800; color: var(--c-wine-primary); letter-spacing: 1.5px; white-space: nowrap;">
                CONCLUSIÓN PEDAGÓGICA:
              </span>
              <span style="font-family: var(--font-sans); font-size: 23px; font-weight: 700; color: #110103; white-space: nowrap;">
                Modelos con idéntica nota numérica exigen entornos de despliegue completamente distintos.
              </span>
            </div>
            <span style="font-family: var(--font-mono); font-size: 16px; font-weight: 800; color: var(--c-wine-primary); letter-spacing: 1px; white-space: nowrap;">
              Tabla 3 (&times;4 semillas)
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
</html>'''

path_14 = os.path.join(output_dir, "slide_14_tech_preview.png")

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page(viewport={"width": 1920, "height": 1080})
    page.set_content(html)
    page.wait_for_timeout(600)
    page.screenshot(path=path_14)
    print("Saved Slide 14 tech preview to:", path_14)
    browser.close()
