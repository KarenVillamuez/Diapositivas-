# -*- coding: utf-8 -*-
"""
Compilador Modular de Diapositivas - LHXT26 Cartagena 2026
Lee cada slide individual desde la carpeta /slides/ y genera index.html
"""

import os
import glob

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SLIDES_DIR = os.path.join(ROOT_DIR, 'slides')
OUTPUT_FILE = os.path.join(ROOT_DIR, 'index.html')

HEADER_TEMPLATE = '''<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>VI Congreso Internacional de Investigación Interdisciplinar | RAG Offline &amp; SLM</title>
  <meta name="description" content="Evaluación de SLM y RAG Offline en hardware de aula rural sin conectividad. VI Congreso Internacional Cartagena 2026.">
  <link rel="stylesheet" href="styles.css?v=13">
</head>
<body>

  <!-- Escenario Fijo 1920x1080 con Escalado Proporcional -->
  <main id="presentation-viewport">
    <div id="slides-stage">
'''

FOOTER_TEMPLATE = '''
    </div><!-- /#slides-stage -->
  </main>

  <script src="app.js?v=13"></script>
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
    
    print(f"Exito: {OUTPUT_FILE} generado con {len(slide_files)} diapositivas modulares.")

if __name__ == '__main__':
    build()
