# -*- coding: utf-8 -*-
"""
Script to test asymmetric tech badges, icons and logos on Slide 07.
"""
import os
from playwright.sync_api import sync_playwright

output_dir = r"C:\Users\ASUS\.gemini\antigravity-ide\brain\a6624504-511c-4b9d-bc9a-468e348bde40"

# SVG Icons:
# 1. Book / Curriculum:
ICON_BOOK = '''<svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"/><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"/><line x1="9" y1="7" x2="15" y2="7"/><line x1="9" y1="11" x2="13" y2="11"/></svg>'''

# 2. Hybrid Search (Magnifier + dense vectors):
ICON_SEARCH = '''<svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="11" cy="11" r="7"/><line x1="21" y1="21" x2="16.65" y2="16.65"/><path d="M11 8v6M8 11h6"/></svg>'''

# 3. Cross-Encoder / Neural Network:
ICON_NEURAL = '''<svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="3" width="6" height="6" rx="1"/><rect x="15" y="3" width="6" height="6" rx="1"/><rect x="9" y="15" width="6" height="6" rx="1"/><path d="M6 9v3a3 3 0 0 0 3 3h3m3-6v3a3 3 0 0 1-3 3"/></svg>'''

# 4. CPU Chip / llama.cpp:
ICON_CPU = '''<svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="4" y="4" width="16" height="16" rx="2"/><rect x="9" y="9" width="6" height="6"/><line x1="9" y1="1" x2="9" y2="4"/><line x1="15" y1="1" x2="15" y2="4"/><line x1="9" y1="20" x2="9" y2="23"/><line x1="15" y1="20" x2="15" y2="23"/><line x1="20" y1="9" x2="23" y2="9"/><line x1="20" y1="14" x2="23" y2="14"/><line x1="1" y1="9" x2="4" y2="9"/><line x1="1" y1="14" x2="4" y2="14"/></svg>'''

# USB Stick SVG:
ICON_USB = '''<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M10 7v6a2 2 0 0 0 4 0V7"/><path d="M8 7h8V3H8z"/><path d="M10 21h4a2 2 0 0 0 2-2v-6H8v6a2 2 0 0 0 2 2z"/></svg>'''


html_template = f'''<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<link rel="stylesheet" href="../../styles.css">
<style>
  body {{ margin: 0; background: #333; display: flex; flex-direction: column; gap: 40px; padding: 20px; }}
  .slide {{ position: relative; width: 1920px; height: 1080px; background: #FFF; overflow: hidden; margin: 0 auto; box-shadow: 0 10px 30px rgba(0,0,0,0.5); }}
  
  /* Badges asimétricos estilo editorial */
  .tech-sticker {{
    display: inline-flex;
    align-items: center;
    gap: 8px;
    font-family: var(--font-mono);
    font-weight: 800;
    text-transform: uppercase;
    letter-spacing: 1px;
    box-shadow: 0 4px 14px rgba(0,0,0,0.08);
    transition: transform 0.2s ease;
  }}
</style>
</head>
<body>

<!-- ====================================================================
     OPCIÓN 1: ICONOS EN HEADER DE PASOS + STICKERS ASIMÉTRICOS EN PASO 4 Y BANNER
     ==================================================================== -->
<section class="slide s-white" id="slide-7-opt1">
  <header class="slide-header">
    <div class="sh-left">
      <span class="sh-red-bar"></span>
      <span class="sh-category">02 &middot; METODOLOG&Iacute;A &middot; PIPELINE RAG LOCAL</span>
    </div>
    <img src="../../assets/image6.png" alt="#LoxTIC" class="sh-loxtic">
  </header>
  <div class="sh-divider"></div>

  <div class="slide-content-area" style="justify-content: center; padding-top: 10px; padding-bottom: 20px;">
    <div style="display: flex; align-items: baseline; justify-content: space-between; margin-bottom: 30px;">
      <h2 class="s-lead-question" style="font-size: 46px; font-weight: 800; margin: 0; line-height: 1.2;">
        Flujo secuencial del pipeline RAG: de la consulta a la generaci&oacute;n
      </h2>
      <!-- Badge de tecnología asimétrico en cabecera -->
      <div class="tech-sticker" style="background: #2C0509; color: #FFFFFF; font-size: 14px; padding: 6px 14px; transform: rotate(-2deg); border: 1px solid rgba(255,255,255,0.2);">
        <span style="color: var(--c-gold); font-size: 16px;">⚡</span>
        STACK 100% C++ &amp; EMBEDDINGS LOCALES
      </div>
    </div>

    <div style="display: flex; flex-direction: column; gap: 26px;">
      
      <!-- Fila de Proceso Conectado -->
      <div style="display: flex; align-items: stretch; gap: 14px; position: relative;">
        
        <!-- Paso 1 -->
        <div style="flex: 1; background: #FAF5F5; border-left: 6px solid var(--c-wine-primary); padding: 24px 22px; position: relative;">
          <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 8px;">
            <span style="font-family: var(--font-mono); font-size: 18px; font-weight: 700; color: var(--c-wine-primary); letter-spacing: 1px;">
              PASO 01
            </span>
            <div style="color: var(--c-wine-primary); opacity: 0.85;">
              {ICON_BOOK}
            </div>
          </div>
          <div style="font-family: var(--font-sans); font-size: 29px; font-weight: 800; color: var(--c-text-dark); margin-bottom: 12px; line-height: 1.15;">
            Corpus Curricular
          </div>
          <div style="font-family: var(--font-sans); font-size: 25px; color: #110103; line-height: 1.42;">
            Libro abierto <em>College ESL</em>: <strong style="color: var(--c-wine-primary);">339 trozos</strong> (&le; 512 palabras).
          </div>
        </div>

        <!-- Flecha 1 -->
        <div style="display: flex; align-items: center; justify-content: center; flex-shrink: 0; color: var(--c-wine-primary);">
          <svg width="44" height="44" viewBox="0 0 24 24" fill="currentColor">
            <path d="M12 4l-1.41 1.41L16.17 11H4v2h12.17l-5.58 5.59L12 20l8-8-8-8z"/>
          </svg>
        </div>

        <!-- Paso 2 -->
        <div style="flex: 1; background: #FAF5F5; border-left: 6px solid var(--c-wine-primary); padding: 24px 22px; position: relative;">
          <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 8px;">
            <span style="font-family: var(--font-mono); font-size: 18px; font-weight: 700; color: var(--c-wine-primary); letter-spacing: 1px;">
              PASO 02
            </span>
            <div style="color: var(--c-wine-primary); opacity: 0.85;">
              {ICON_SEARCH}
            </div>
          </div>
          <div style="font-family: var(--font-sans); font-size: 29px; font-weight: 800; color: var(--c-text-dark); margin-bottom: 12px; line-height: 1.15;">
            B&uacute;squeda H&iacute;brida
          </div>
          <div style="font-family: var(--font-sans); font-size: 25px; color: #110103; line-height: 1.42;">
            <strong style="color: var(--c-wine-primary);">Fusi&oacute;n RRF (60/40)</strong>: denso + BM25 con expansi&oacute;n l&eacute;xica.
          </div>
        </div>

        <!-- Flecha 2 -->
        <div style="display: flex; align-items: center; justify-content: center; flex-shrink: 0; color: var(--c-red-accent);">
          <svg width="44" height="44" viewBox="0 0 24 24" fill="currentColor">
            <path d="M12 4l-1.41 1.41L16.17 11H4v2h12.17l-5.58 5.59L12 20l8-8-8-8z"/>
          </svg>
        </div>

        <!-- Paso 3 -->
        <div style="flex: 1; background: #FAF5F5; border-left: 6px solid var(--c-red-accent); padding: 24px 22px; position: relative;">
          <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 8px;">
            <span style="font-family: var(--font-mono); font-size: 18px; font-weight: 700; color: var(--c-red-accent); letter-spacing: 1px;">
              PASO 03
            </span>
            <div style="color: var(--c-red-accent); opacity: 0.85;">
              {ICON_NEURAL}
            </div>
          </div>
          <div style="font-family: var(--font-sans); font-size: 29px; font-weight: 800; color: var(--c-text-dark); margin-bottom: 12px; line-height: 1.15;">
            Reranker Neuronal
          </div>
          <div style="font-family: var(--font-sans); font-size: 25px; color: #110103; line-height: 1.42;">
            Cross-Encoder <em>MiniLM</em>: <strong style="color: var(--c-red-accent);">suprime el ruido</strong> antes de la CPU.
          </div>
        </div>

        <!-- Flecha 3 -->
        <div style="display: flex; align-items: center; justify-content: center; flex-shrink: 0; color: #9A7200;">
          <svg width="44" height="44" viewBox="0 0 24 24" fill="currentColor">
            <path d="M12 4l-1.41 1.41L16.17 11H4v2h12.17l-5.58 5.59L12 20l8-8-8-8z"/>
          </svg>
        </div>

        <!-- Paso 4 con Badge Inclinado Flotante -->
        <div style="flex: 1; background: #FAF5F5; border-left: 6px solid var(--c-gold); padding: 24px 22px; position: relative;">
          <!-- Sticker tecnológico flotante inclinado en esquina -->
          <div class="tech-sticker" style="position: absolute; top: -15px; right: 10px; background: #C9101B; color: #FFFFFF; font-size: 12px; padding: 4px 10px; transform: rotate(3deg); z-index: 10; border: 1.5px solid #FFFFFF;">
            <code>llama.cpp</code> &bull; C/C++
          </div>
          
          <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 8px;">
            <span style="font-family: var(--font-mono); font-size: 18px; font-weight: 700; color: #9A7200; letter-spacing: 1px;">
              PASO 04
            </span>
            <div style="color: #9A7200; opacity: 0.85;">
              {ICON_CPU}
            </div>
          </div>
          <div style="font-family: var(--font-sans); font-size: 29px; font-weight: 800; color: var(--c-text-dark); margin-bottom: 12px; line-height: 1.15;">
            Inferencia Local
          </div>
          <div style="font-family: var(--font-sans); font-size: 25px; color: #110103; line-height: 1.42;">
            Motor <code>llama.cpp</code> a <strong style="color: #9A7200;">1.9 tok/s</strong> en <strong>CPU est&aacute;ndar sin GPU</strong>.
          </div>
        </div>

      </div>

      <!-- Tarjeta Panorámica de Principio Técnico con Sello Asimétrico Flotante -->
      <div style="background: #FAF5F5; border: 2px solid var(--c-wine-primary); padding: 26px 36px; display: flex; align-items: center; gap: 36px; position: relative;">
        
        <!-- Sello Asimétrico Flotante Tipo Estampa Técnica -->
        <div class="tech-sticker" style="position: absolute; top: -16px; right: 30px; background: #FAF0F2; color: var(--c-wine-primary); border: 2px solid var(--c-wine-primary); padding: 5px 14px; font-size: 13px; transform: rotate(-2.5deg); z-index: 5;">
          {ICON_USB}
          <span>PLUG &amp; PLAY &bull; PORTABLE EN USB 3.0</span>
        </div>

        <div style="flex: 0 0 220px; width: 220px; text-align: center;">
          <div style="font-family: var(--font-sans); font-size: 56px; font-weight: 800; color: var(--c-wine-primary); line-height: 1;">
            100%
          </div>
          <div style="font-family: var(--font-mono); font-size: 18px; font-weight: 700; color: #110103; margin-top: 6px; letter-spacing: 1px;">
            LOCAL / USB
          </div>
        </div>
        <div style="width: 2px; height: 80px; background: var(--c-border-subtle); flex-shrink: 0;"></div>
        <div style="flex: 1;">
          <div style="font-family: var(--font-sans); font-size: 28px; font-weight: 700; color: var(--c-text-dark); margin-bottom: 8px;">
            Principio Operativo: Cero Dependencia de Servidores
          </div>
          <p style="font-family: var(--font-sans); font-size: 25px; color: #110103; line-height: 1.45; margin: 0;">
            Todo el pipeline (b&uacute;squeda, re-ranking e inferencia del modelo SLM) se ejecuta en la <strong>memoria RAM del computador del aula</strong> sin enviar un solo byte a la nube.
          </p>
        </div>
      </div>

    </div>
  </div>

  <div class="slide-footer-rule"></div>
  <footer class="slide-footer">
    <span class="sf-left">VI CONGRESO CARTAGENA &middot; 2026</span>
    <span class="sf-right">LOHACEMOSXTIC.COM &middot; SLM OFFLINE</span>
  </footer>
</section>

</body>
</html>
'''

preview_path = os.path.join(output_dir, "test_slide07_preview.html")
with open(preview_path, "w", encoding="utf-8") as f:
    f.write(html_template)

print("Generated test HTML at:", preview_path)

screenshot_path = os.path.join(output_dir, "slide_07_tech_opt1.png")
with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page(viewport={"width": 1920, "height": 1080})
    page.goto(f"file:///{preview_path.replace(os.sep, '/')}")
    page.wait_for_timeout(600)
    page.screenshot(path=screenshot_path)
    print("Screenshot saved to:", screenshot_path)
    browser.close()
