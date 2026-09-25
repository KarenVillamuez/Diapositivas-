# -*- coding: utf-8 -*-
"""
Compilador Modular de Diapositivas - LHXT26 Cartagena 2026
Lee cada slide individual desde la carpeta /slides/ y genera index.html
"""

import os
import glob
import re

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SLIDES_DIR = os.path.join(ROOT_DIR, 'slides')
OUTPUT_FILE = os.path.join(ROOT_DIR, 'index.html')

HEADER_TEMPLATE = '''<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>VI Congreso Internacional de Investigación Interdisciplinar | Escritura Reflexiva Asistida por IA</title>
  <meta name="description" content="Diseño de un modelo de mediación conversacional para la escritura reflexiva asistida por inteligencia artificial. VI Congreso Internacional Cartagena 2026.">
  <link rel="stylesheet" href="styles.css?v=2">
  <link rel="icon" type="image/png" href="assets/image2.png">
</head>
<body>

  <!-- Viewport de Presentación -->
  <main id="presentation-viewport">
    
    <!-- Barra de progreso superior -->
    <div id="progress-bar">
      <div id="progress-fill"></div>
    </div>

    <!-- Escenario 16:9 auto-escalable -->
    <div id="slides-stage">
'''

FOOTER_TEMPLATE = '''
    </div><!-- /#slides-stage -->

    <!-- Panel flotante de notas del orador (toggle con tecla N) -->
    <div id="speaker-notes-panel" style="display: none; position: fixed; bottom: 25px; left: 50%; transform: translateX(-50%); width: 85%; max-width: 1400px; background: rgba(50, 6, 13, 0.95); color: #FFFFFF; border-left: 8px solid var(--c-gold); padding: 18px 28px; z-index: 9999; font-family: var(--font-sans); font-size: 21px; line-height: 1.4; box-shadow: 0 10px 40px rgba(0,0,0,0.8);">
      <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
        <span style="font-family: var(--font-mono); font-size: 15px; font-weight: bold; color: var(--c-gold); letter-spacing: 1.5px;">GUION ORAL DEL PONENTE (TECLA N PARA OCULTAR)</span>
        <span id="notes-slide-indicator" style="font-family: var(--font-mono); font-size: 15px; color: #EAE0E1;"></span>
      </div>
      <div id="speaker-notes-content" style="color: #FAF5F5;"></div>
    </div>

  </main>

  <script src="app.js?v=2"></script>
</body>
</html>
'''

def build():
    slide_files = sorted(glob.glob(os.path.join(SLIDES_DIR, 'slide_*.html')))
    if not slide_files:
        raise FileNotFoundError(f"No se encontraron archivos en {SLIDES_DIR}")
    
    print(f"Ensamblando {len(slide_files)} diapositivas modulares desde {SLIDES_DIR}...")
    
    slides_content = []
    for sf in slide_files:
        with open(sf, 'r', encoding='utf-8') as f:
            slides_content.append(f.read().strip())
    
    full_html = HEADER_TEMPLATE + "\n\n".join(slides_content) + FOOTER_TEMPLATE
    
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        f.write(full_html)
    
    print(f"Éxito: {OUTPUT_FILE} generado con {len(slide_files)} diapositivas modulares.")

if __name__ == '__main__':
    build()
