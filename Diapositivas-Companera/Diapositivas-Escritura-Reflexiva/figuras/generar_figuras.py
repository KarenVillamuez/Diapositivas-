# -*- coding: utf-8 -*-
"""
Generador Vectorial de Figuras Científicas - LHXT26 Cartagena 2026
Artículo: Diseño de un Modelo de Escritura Reflexiva Mediado por Inteligencia Artificial
Genera SVG vectorial y PNG a 300 DPI utilizando la paleta oficial del congreso.
"""

import math
import os
from pathlib import Path
import fitz  # PyMuPDF

FIGURAS_DIR = Path(__file__).resolve().parent

# Paleta Oficial LHXT26 Cartagena
C_WINE_DARK = "#32060D"
C_WINE_PRIMARY = "#460811"
C_TEXT_DARK = "#2C0509"
C_RED_ACCENT = "#C9101B"
C_GOLD = "#F5C21B"
C_GOLD_DARK = "#B38600"
C_PINK_BG = "#FAF5F5"
C_BORDER_SUBTLE = "#EAE0E1"
C_LINE_RULE = "#E4DADB"
C_GRAY_TEXT = "#5D4A4D"
C_GRAY_MUTED = "#8D7A7D"
C_WHITE = "#FFFFFF"

# ==============================================================================
# FIGURA 1: RADAR COMPARATIVO DE 6 MODELOS DE ESCRITURA REFLEXIVA
# ==============================================================================
def generar_figura_1():
    w, h = 1400, 950
    cx, cy = 600, 470
    radius = 330
    
    axes = [
        "Recursividad",
        "Desglose\nAndamiable",
        "Potencial\nFrente a IA",
        "Aplicabilidad\nProfesional",
        "Mediación\nDialógica",
        "Integración\nEmocional"
    ]
    num_axes = len(axes)
    
    # Niveles: 1: Bajo, 2: Medio, 3: Alto
    models = {
        "Flower y Hayes": {
            "vals": [3, 3, 3, 2, 1, 1],
            "color": C_WINE_PRIMARY,
            "fill": "rgba(70, 8, 17, 0.22)",
            "width": 4.5,
            "dash": "none",
            "highlight": True
        },
        "Schön": {
            "vals": [3, 1, 3, 3, 3, 3],
            "color": C_RED_ACCENT,
            "fill": "rgba(201, 16, 27, 0.22)",
            "width": 4.5,
            "dash": "none",
            "highlight": True
        },
        "Bereiter y Scardamalia": {
            "vals": [2, 2, 2, 1, 2, 1],
            "color": "#4A6B82",
            "fill": "none",
            "width": 2.2,
            "dash": "6,4",
            "highlight": False
        },
        "Kellogg": {
            "vals": [2, 2, 1, 1, 1, 1],
            "color": "#7A5C80",
            "fill": "none",
            "width": 2.2,
            "dash": "4,4",
            "highlight": False
        },
        "Zimmerman y Risemberg": {
            "vals": [2, 3, 2, 2, 1, 3],
            "color": "#8C6A3E",
            "fill": "none",
            "width": 2.2,
            "dash": "8,4",
            "highlight": False
        },
        "Grupo Didactext": {
            "vals": [2, 2, 1, 3, 2, 2],
            "color": "#3B7A57",
            "fill": "none",
            "width": 2.2,
            "dash": "5,3",
            "highlight": False
        }
    }
    
    def get_coords(val, idx):
        # Ángulo: empieza arriba (idx 0 a -90 deg)
        angle = -math.pi / 2 + idx * (2 * math.pi / num_axes)
        r = (val / 3.0) * radius
        return cx + r * math.cos(angle), cy + r * math.sin(angle)
    
    svg = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="100%" height="100%">']
    svg.append(f'<rect width="{w}" height="{h}" fill="{C_WHITE}"/>')
    
    # Título y subtítulo
    svg.append(f'<text x="60" y="60" font-family="Arial, sans-serif" font-size="28" font-weight="bold" fill="{C_TEXT_DARK}">EVALUACIÓN COMPARATIVA DE MODELOS TEÓRICOS</text>')
    svg.append(f'<text x="60" y="92" font-family="Arial, sans-serif" font-size="18" fill="{C_GRAY_TEXT}">Análisis multidimensional de 6 propuestas para mediación conversacional de escritura asistida</text>')
    svg.append(f'<line x1="60" y1="110" x2="{w-60}" y2="110" stroke="{C_BORDER_SUBTLE}" stroke-width="2"/>')
    
    # Rejilla concéntrica del radar (Niveles 1, 2, 3)
    levels = [1, 2, 3]
    level_names = ["Bajo (1)", "Medio (2)", "Alto (3)"]
    for lev, name in zip(levels, level_names):
        poly_pts = []
        for i in range(num_axes):
            px, py = get_coords(lev, i)
            poly_pts.append(f"{px:.1f},{py:.1f}")
        fill_col = "#FAF5F5" if lev == 3 else ("#FFFFFF" if lev == 2 else "#F8EEEE")
        svg.append(f'<polygon points="{" ".join(poly_pts)}" fill="{fill_col}" stroke="{C_BORDER_SUBTLE}" stroke-width="1.8"/>')
        # Etiqueta de nivel en eje vertical
        ly = cy - (lev / 3.0) * radius
        svg.append(f'<text x="{cx + 10}" y="{ly + 16}" font-family="Courier New, monospace" font-size="13" font-weight="bold" fill="{C_GRAY_MUTED}">{name}</text>')
    
    # Ejes radiales
    for i in range(num_axes):
        px, py = get_coords(3, i)
        svg.append(f'<line x1="{cx}" y1="{cy}" x2="{px}" y2="{py}" stroke="{C_BORDER_SUBTLE}" stroke-width="2"/>')
        
        # Etiquetas de los ejes
        angle = -math.pi / 2 + i * (2 * math.pi / num_axes)
        label_r = radius + 40
        lx = cx + label_r * math.cos(angle)
        ly = cy + label_r * math.sin(angle)
        
        lines = axes[i].split("\n")
        anchor = "middle"
        if math.cos(angle) > 0.3:
            anchor = "start"
            lx += 10
        elif math.cos(angle) < -0.3:
            anchor = "end"
            lx -= 10
            
        if len(lines) == 1:
            svg.append(f'<text x="{lx}" y="{ly + 5}" font-family="Arial, sans-serif" font-size="18" font-weight="bold" fill="{C_TEXT_DARK}" text-anchor="{anchor}">{lines[0]}</text>')
        else:
            svg.append(f'<text x="{lx}" y="{ly - 6}" font-family="Arial, sans-serif" font-size="18" font-weight="bold" fill="{C_TEXT_DARK}" text-anchor="{anchor}">{lines[0]}</text>')
            svg.append(f'<text x="{lx}" y="{ly + 16}" font-family="Arial, sans-serif" font-size="18" font-weight="bold" fill="{C_TEXT_DARK}" text-anchor="{anchor}">{lines[1]}</text>')

    # Dibujar modelos secundarios primero
    for name, data in models.items():
        if data["highlight"]:
            continue
        poly_pts = []
        for i in range(num_axes):
            px, py = get_coords(data["vals"][i], i)
            poly_pts.append(f"{px:.1f},{py:.1f}")
        svg.append(f'<polygon points="{" ".join(poly_pts)}" fill="none" stroke="{data["color"]}" stroke-width="{data["width"]}" stroke-dasharray="{data["dash"]}"/>')

    # Dibujar modelos seleccionados (Flower & Hayes y Schön)
    for name, data in models.items():
        if not data["highlight"]:
            continue
        poly_pts = []
        for i in range(num_axes):
            px, py = get_coords(data["vals"][i], i)
            poly_pts.append(f"{px:.1f},{py:.1f}")
        svg.append(f'<polygon points="{" ".join(poly_pts)}" fill="{data["fill"]}" stroke="{data["color"]}" stroke-width="{data["width"]}"/>')
        # Puntos en vértices
        for i in range(num_axes):
            px, py = get_coords(data["vals"][i], i)
            svg.append(f'<circle cx="{px}" cy="{py}" r="5.5" fill="{data["color"]}" stroke="{C_WHITE}" stroke-width="2"/>')

    # Panel lateral derecho de Leyenda y Conclusión Teórica
    lx = 1010
    ly = 150
    svg.append(f'<rect x="{lx}" y="{ly}" width="340" height="710" fill="{C_PINK_BG}" stroke="{C_BORDER_SUBTLE}" stroke-width="1.5"/>')
    svg.append(f'<rect x="{lx}" y="{ly}" width="340" height="8" fill="{C_WINE_PRIMARY}"/>')
    
    svg.append(f'<text x="{lx + 24}" y="{ly + 40}" font-family="Courier New, monospace" font-size="16" font-weight="bold" fill="{C_RED_ACCENT}" letter-spacing="1">MODELOS SELECCIONADOS</text>')
    
    # Item 1: Flower y Hayes
    svg.append(f'<rect x="{lx + 24}" y="{ly + 60}" width="20" height="20" fill="{C_WINE_PRIMARY}"/>')
    svg.append(f'<text x="{lx + 54}" y="{ly + 76}" font-family="Arial, sans-serif" font-size="19" font-weight="bold" fill="{C_TEXT_DARK}">Flower y Hayes (1981)</text>')
    svg.append(f'<text x="{lx + 54}" y="{ly + 100}" font-family="Arial, sans-serif" font-size="15" fill="{C_GRAY_TEXT}">Proceso cognitivo cíclico: planear,</text>')
    svg.append(f'<text x="{lx + 54}" y="{ly + 120}" font-family="Arial, sans-serif" font-size="15" fill="{C_GRAY_TEXT}">redactar y revisar. Aporta las fases.</text>')

    # Item 2: Schön
    svg.append(f'<rect x="{lx + 24}" y="{ly + 148}" width="20" height="20" fill="{C_RED_ACCENT}"/>')
    svg.append(f'<text x="{lx + 54}" y="{ly + 164}" font-family="Arial, sans-serif" font-size="19" font-weight="bold" fill="{C_TEXT_DARK}">Schön (1983)</text>')
    svg.append(f'<text x="{lx + 54}" y="{ly + 188}" font-family="Arial, sans-serif" font-size="15" fill="{C_GRAY_TEXT}">Práctica reflexiva en la acción.</text>')
    svg.append(f'<text x="{lx + 54}" y="{ly + 208}" font-family="Arial, sans-serif" font-size="15" fill="{C_GRAY_TEXT}">Aporta el diálogo y la sorpresa.</text>')

    svg.append(f'<line x1="{lx + 24}" y1="{ly + 235}" x2="{lx + 316}" y2="{ly + 235}" stroke="{C_BORDER_SUBTLE}" stroke-width="1.5"/>')
    svg.append(f'<text x="{lx + 24}" y="{ly + 265}" font-family="Courier New, monospace" font-size="15" font-weight="bold" fill="{C_GRAY_MUTED}" letter-spacing="1">MODELOS CONTRASTADOS</text>')

    other_models = [
        ("Bereiter y Scardamalia", "#4A6B82", "Transformar vs. decir conocimiento"),
        ("Kellogg", "#7A5C80", "Sobrecarga de memoria de trabajo"),
        ("Zimmerman y Risemberg", "#8C6A3E", "Autorregulación y motivación"),
        ("Grupo Didactext", "#3B7A57", "Didáctica sociocognitiva general")
    ]
    
    oy = ly + 295
    for mname, mcol, mdesc in other_models:
        svg.append(f'<line x1="{lx + 24}" y1="{oy + 8}" x2="{lx + 46}" y2="{oy + 8}" stroke="{mcol}" stroke-width="3" stroke-dasharray="4,3"/>')
        svg.append(f'<text x="{lx + 54}" y="{oy + 12}" font-family="Arial, sans-serif" font-size="16" font-weight="bold" fill="{C_TEXT_DARK}">{mname}</text>')
        svg.append(f'<text x="{lx + 54}" y="{oy + 30}" font-family="Arial, sans-serif" font-size="13" fill="{C_GRAY_MUTED}">{mdesc}</text>')
        oy += 48

    # Veredicto de articulación
    vy = ly + 510
    svg.append(f'<rect x="{lx + 16}" y="{vy}" width="308" height="175" fill="{C_WHITE}" stroke="{C_GOLD_DARK}" stroke-width="2"/>')
    svg.append(f'<rect x="{lx + 16}" y="{vy}" width="308" height="6" fill="{C_GOLD}"/>')
    svg.append(f'<text x="{lx + 30}" y="{vy + 32}" font-family="Courier New, monospace" font-size="14" font-weight="bold" fill="{C_GOLD_DARK}">HALLAZGO DE SELECCIÓN</text>')
    svg.append(f'<text x="{lx + 30}" y="{vy + 60}" font-family="Arial, sans-serif" font-size="15" font-weight="bold" fill="{C_TEXT_DARK}">Complementariedad Exacta:</text>')
    svg.append(f'<text x="{lx + 30}" y="{vy + 82}" font-family="Arial, sans-serif" font-size="14" fill="{C_GRAY_TEXT}">Ningún modelo por sí solo cubría la</text>')
    svg.append(f'<text x="{lx + 30}" y="{vy + 102}" font-family="Arial, sans-serif" font-size="14" fill="{C_GRAY_TEXT}">necesidad. Flower y Hayes da la división</text>')
    svg.append(f'<text x="{lx + 30}" y="{vy + 122}" font-family="Arial, sans-serif" font-size="14" fill="{C_GRAY_TEXT}">operativa; Schön la lógica reflexiva</text>')
    svg.append(f'<text x="{lx + 30}" y="{vy + 142}" font-family="Arial, sans-serif" font-size="14" font-weight="bold" fill="{C_RED_ACCENT}">que impide que la IA sustituya al autor.</text>')

    # Epígrafe inferior
    svg.append(f'<text x="60" y="{h - 35}" font-family="Arial, sans-serif" font-size="16" font-weight="bold" fill="{C_TEXT_DARK}">Fig. 1. Evaluación comparativa de modelos de escritura reflexiva.</text>')
    svg.append(f'<text x="600" y="{h - 35}" font-family="Arial, sans-serif" font-size="15" font-style="italic" fill="{C_GRAY_MUTED}">Figure 1. Comparative evaluation of reflective writing models. Fuente: Autores.</text>')

    svg.append('</svg>')
    out_svg = FIGURAS_DIR / "figura_1_radar.svg"
    out_svg.write_text("\n".join(svg), encoding="utf-8")
    print(f"Figura 1 generada en: {out_svg}")
    return out_svg

# ==============================================================================
# FIGURA 2: MODELO DE ESCRITURA REFLEXIVA SIN MEDIACIÓN DE IA (P1 A P8)
# ==============================================================================
def generar_figura_2():
    w, h = 1500, 920
    cx, cy = 750, 460
    
    phases = [
        {"id": "P1", "name": "Actuación inicial", "desc": "Escritura fluida desde el repertorio tácito sin juicio analítico.", "model": "Schön", "color": C_WINE_PRIMARY},
        {"id": "P2", "name": "Giro de Sorpresa", "desc": "Interrupción de la rutina por un desajuste percibido en el texto.", "model": "Schön", "color": C_WINE_PRIMARY, "break": True},
        {"id": "P3", "name": "Generación de Ideas", "desc": "Ideación libre y sin censura para producir material bruto.", "model": "Flower & Hayes", "color": C_RED_ACCENT},
        {"id": "P4", "name": "Organización", "desc": "Jerarquización y estructura lógica del material generado.", "model": "Flower & Hayes", "color": C_RED_ACCENT},
        {"id": "P5", "name": "Definición de Metas", "desc": "Establecimiento de objetivos claros de contenido y de proceso.", "model": "Flower & Hayes", "color": C_RED_ACCENT},
        {"id": "P6", "name": "Traducción", "desc": "Transformación de ideas en lenguaje tolerando la imperfección.", "model": "Flower & Hayes", "color": C_RED_ACCENT},
        {"id": "P7", "name": "Evaluación / Relectura", "desc": "Contraste con metas iniciales y detección de discrepancias.", "model": "Flower & Hayes + Schön", "color": C_GOLD_DARK, "break": True},
        {"id": "P8", "name": "Integración", "desc": "Reconstrucción del quiebre y ajuste de la estrategia futura.", "model": "Schön", "color": C_WINE_PRIMARY},
    ]
    
    svg = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="100%" height="100%">']
    svg.append(f'<rect width="{w}" height="{h}" fill="{C_WHITE}"/>')
    
    # Encabezado
    svg.append(f'<text x="60" y="55" font-family="Arial, sans-serif" font-size="28" font-weight="bold" fill="{C_TEXT_DARK}">MODELO DE ESCRITURA REFLEXIVA SIN MEDIACIÓN DE IA</text>')
    svg.append(f'<text x="60" y="85" font-family="Arial, sans-serif" font-size="18" fill="{C_GRAY_TEXT}">Proceso cíclico y recursivo de 8 fases: momentos de avance, duda analítica y reajuste</text>')
    svg.append(f'<line x1="60" y1="102" x2="{w-60}" y2="102" stroke="{C_BORDER_SUBTLE}" stroke-width="2"/>')

    # Marcadores de flechas para SVG
    svg.append('<defs>')
    svg.append(f'<marker id="arrow-forward" markerWidth="9" markerHeight="9" refX="7" refY="4.5" orient="auto"><polygon points="0 0, 9 4.5, 0 9" fill="{C_WINE_PRIMARY}"/></marker>')
    svg.append(f'<marker id="arrow-recursive" markerWidth="9" markerHeight="9" refX="7" refY="4.5" orient="auto"><polygon points="0 0, 9 4.5, 0 9" fill="{C_RED_ACCENT}"/></marker>')
    svg.append('</defs>')

    # Círculo / Núcleo Central
    core_w, core_h = 360, 220
    svg.append(f'<rect x="{cx - core_w/2}" y="{cy - core_h/2}" width="{core_w}" height="{core_h}" fill="{C_PINK_BG}" stroke="{C_WINE_PRIMARY}" stroke-width="3"/>')
    svg.append(f'<rect x="{cx - core_w/2}" y="{cy - core_h/2}" width="{core_w}" height="8" fill="{C_WINE_PRIMARY}"/>')
    svg.append(f'<text x="{cx}" y="{cy - 45}" font-family="Courier New, monospace" font-size="16" font-weight="bold" fill="{C_RED_ACCENT}" text-anchor="middle" letter-spacing="1">PROCESO AUTÓNOMO</text>')
    svg.append(f'<text x="{cx}" y="{cy - 12}" font-family="Arial, sans-serif" font-size="24" font-weight="bold" fill="{C_WINE_DARK}" text-anchor="middle">Modelo de Escritura</text>')
    svg.append(f'<text x="{cx}" y="{cy + 18}" font-family="Arial, sans-serif" font-size="24" font-weight="bold" fill="{C_WINE_DARK}" text-anchor="middle">Reflexiva</text>')
    svg.append(f'<line x1="{cx - 130}" y1="{cy + 36}" x2="{cx + 130}" y2="{cy + 36}" stroke="{C_BORDER_SUBTLE}" stroke-width="1.5"/>')
    svg.append(f'<text x="{cx}" y="{cy + 58}" font-family="Arial, sans-serif" font-size="14" fill="{C_GRAY_TEXT}" text-anchor="middle">El escritor va y viene entre fases</text>')
    svg.append(f'<text x="{cx}" y="{cy + 78}" font-family="Arial, sans-serif" font-size="14" font-weight="bold" fill="{C_RED_ACCENT}" text-anchor="middle">Puntos de duda detienen la rutina</text>')

    # Disposición elíptica de las 8 fases
    rx_radius = 560
    ry_radius = 290
    
    node_coords = []
    for i, p in enumerate(phases):
        # Ángulo: P1 arriba a la izquierda, luego gira en sentido horario
        angle = -math.pi * 0.75 + i * (2 * math.pi / 8)
        nx = cx + rx_radius * math.cos(angle)
        ny = cy + ry_radius * math.sin(angle)
        node_coords.append((nx, ny))

    # Trazos y flechas recursivas entre nodos
    # Bucle recursivo P7 -> P4 (reordenar ideas tras relectura)
    p7x, p7y = node_coords[6]
    p4x, p4y = node_coords[3]
    svg.append(f'<path d="M {p7x - 40} {p7y + 20} Q {cx} {cy + 190} {p4x + 40} {p4y + 20}" fill="none" stroke="{C_RED_ACCENT}" stroke-width="3" stroke-dasharray="6,4" marker-end="url(#arrow-recursive)"/>')
    svg.append(f'<text x="{cx}" y="{cy + 180}" font-family="Courier New, monospace" font-size="14" font-weight="bold" fill="{C_RED_ACCENT}" text-anchor="middle">RECURSIVIDAD: Ajuste ante desajuste detectado</text>')

    # Dibujar las 8 tarjetas de fases
    card_w = 265
    card_h = 100
    for i, p in enumerate(phases):
        nx, ny = node_coords[i]
        x = nx - card_w/2
        y = ny - card_h/2
        
        # Sombra sutil y tarjeta ortogonal
        svg.append(f'<rect x="{x}" y="{y}" width="{card_w}" height="{card_h}" fill="{C_WHITE}" stroke="{C_BORDER_SUBTLE}" stroke-width="1.5"/>')
        # Barra lateral izquierda temática
        svg.append(f'<rect x="{x}" y="{y}" width="7" height="{card_h}" fill="{p["color"]}"/>')
        
        # Badge de fase (P1..P8)
        svg.append(f'<rect x="{x + 14}" y="{y + 12}" width="36" height="26" fill="{p["color"]}"/>')
        svg.append(f'<text x="{x + 32}" y="{y + 30}" font-family="Courier New, monospace" font-size="16" font-weight="bold" fill="{C_WHITE}" text-anchor="middle">{p["id"]}</text>')
        
        # Nombre de fase
        svg.append(f'<text x="{x + 58}" y="{y + 30}" font-family="Arial, sans-serif" font-size="17" font-weight="bold" fill="{C_TEXT_DARK}">{p["name"]}</text>')
        
        # Descripción
        desc_lines = []
        words = p["desc"].split(" ")
        curr = ""
        for w_item in words:
            if len(curr + " " + w_item) < 32:
                curr += (" " if curr else "") + w_item
            else:
                desc_lines.append(curr)
                curr = w_item
        if curr:
            desc_lines.append(curr)
            
        for line_idx, line in enumerate(desc_lines[:2]):
            svg.append(f'<text x="{x + 16}" y="{y + 58 + line_idx * 18}" font-family="Arial, sans-serif" font-size="13" fill="{C_GRAY_TEXT}">{line}</text>')
            
        # Marca de punto de quiebre / duda
        if p.get("break"):
            svg.append(f'<rect x="{x + card_w - 90}" y="{y + 10}" width="82" height="18" fill="{C_PINK_BG}" stroke="{C_RED_ACCENT}" stroke-width="1"/>')
            svg.append(f'<text x="{x + card_w - 49}" y="{y + 23}" font-family="Courier New, monospace" font-size="11" font-weight="bold" fill="{C_RED_ACCENT}" text-anchor="middle">QUIEBRE</text>')

    # Flechas secuenciales entre nodos sucesivos
    for i in range(len(phases)):
        n1 = node_coords[i]
        n2 = node_coords[(i + 1) % len(phases)]
        if i == len(phases) - 1:
            continue # P8 no se conecta directamente a P1 en automático
            
        # Calcular vector
        dx = n2[0] - n1[0]
        dy = n2[1] - n1[1]
        dist = math.hypot(dx, dy)
        ux = dx / dist
        uy = dy / dist
        
        start_x = n1[0] + ux * 135
        start_y = n1[1] + uy * 55
        end_x = n2[0] - ux * 140
        end_y = n2[1] - uy * 55
        
        svg.append(f'<line x1="{start_x:.1f}" y1="{start_y:.1f}" x2="{end_x:.1f}" y2="{end_y:.1f}" stroke="{C_WINE_PRIMARY}" stroke-width="2.5" marker-end="url(#arrow-forward)"/>')

    # Leyenda al pie
    svg.append(f'<text x="60" y="{h - 35}" font-family="Arial, sans-serif" font-size="16" font-weight="bold" fill="{C_TEXT_DARK}">Fig. 2. Modelo de escritura reflexiva sin mediación por la inteligencia artificial.</text>')
    svg.append(f'<text x="690" y="{h - 35}" font-family="Arial, sans-serif" font-size="15" font-style="italic" fill="{C_GRAY_MUTED}">Puntos P2 y P7 identifican los momentos exactos de duda donde se activa la mediación posterior. Fuente: Autores.</text>')

    svg.append('</svg>')
    out_svg = FIGURAS_DIR / "figura_2_modelo_sin_ia.svg"
    out_svg.write_text("\n".join(svg), encoding="utf-8")
    print(f"Figura 2 generada en: {out_svg}")
    return out_svg

# ==============================================================================
# FIGURA 3: MODELO MEDIADO POR INTELIGENCIA ARTIFICIAL (IA COMO ESPEJO)
# ==============================================================================
def generar_figura_3():
    w, h = 1560, 960
    cx, cy = 780, 480
    
    svg = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="100%" height="100%">']
    svg.append(f'<rect width="{w}" height="{h}" fill="{C_WHITE}"/>')
    
    # Encabezado institucional
    svg.append(f'<text x="60" y="55" font-family="Arial, sans-serif" font-size="28" font-weight="bold" fill="{C_TEXT_DARK}">MODELO INTEGRADO CON MEDIACIÓN CONVERSACIONAL DE IA</text>')
    svg.append(f'<text x="60" y="85" font-family="Arial, sans-serif" font-size="18" fill="{C_GRAY_TEXT}">El autor en el centro de control; la IA como espejo que devuelve preguntas sin redactar ni evaluar</text>')
    svg.append(f'<line x1="60" y1="102" x2="{w-60}" y2="102" stroke="{C_BORDER_SUBTLE}" stroke-width="2"/>')

    # Anillo orbital de las fases P1 a P8
    ring_radius = 290
    svg.append(f'<circle cx="{cx}" cy="{cy}" r="{ring_radius}" fill="none" stroke="{C_BORDER_SUBTLE}" stroke-width="38"/>')
    svg.append(f'<circle cx="{cx}" cy="{cy}" r="{ring_radius}" fill="none" stroke="{C_WINE_PRIMARY}" stroke-width="3" stroke-dasharray="10,6"/>')

    # NÚCLEO CENTRAL: EL AUTOR
    core_w, core_h = 350, 240
    svg.append(f'<rect x="{cx - core_w/2}" y="{cy - core_h/2}" width="{core_w}" height="{core_h}" fill="{C_PINK_BG}" stroke="{C_WINE_PRIMARY}" stroke-width="4"/>')
    svg.append(f'<rect x="{cx - core_w/2}" y="{cy - core_h/2}" width="{core_w}" height="10" fill="{C_WINE_PRIMARY}"/>')
    svg.append(f'<text x="{cx}" y="{cy - 55}" font-family="Courier New, monospace" font-size="16" font-weight="bold" fill="{C_RED_ACCENT}" text-anchor="middle" letter-spacing="2">ROL CENTRAL EXCLUSIVO</text>')
    svg.append(f'<text x="{cx}" y="{cy - 18}" font-family="Arial, sans-serif" font-size="30" font-weight="bold" fill="{C_WINE_DARK}" text-anchor="middle">EL AUTOR</text>')
    svg.append(f'<text x="{cx}" y="{cy + 12}" font-family="Arial, sans-serif" font-size="18" font-weight="bold" fill="{C_TEXT_DARK}" text-anchor="middle">Control y Criterio Propio</text>')
    svg.append(f'<line x1="{cx - 130}" y1="{cy + 30}" x2="{cx + 130}" y2="{cy + 30}" stroke="{C_BORDER_SUBTLE}" stroke-width="1.5"/>')
    svg.append(f'<text x="{cx}" y="{cy + 54}" font-family="Arial, sans-serif" font-size="14" fill="{C_GRAY_TEXT}" text-anchor="middle">• Decide metas y redacta el borrador</text>')
    svg.append(f'<text x="{cx}" y="{cy + 74}" font-family="Arial, sans-serif" font-size="14" fill="{C_GRAY_TEXT}" text-anchor="middle">• Responde a las preguntas si lo desea</text>')
    svg.append(f'<text x="{cx}" y="{cy + 94}" font-family="Arial, sans-serif" font-size="14" font-weight="bold" fill="{C_RED_ACCENT}" text-anchor="middle">• Puede omitir la reflexión y cerrar</text>')

    # Marcadores de nodos P1..P8 en el anillo
    phase_labels = ["P1", "P2", "P3", "P4", "P5", "P6", "P7", "P8"]
    phase_names = ["Actuación", "Sorpresa", "Ideación", "Organizar", "Metas", "Traducir", "Evaluar", "Integrar"]
    for i in range(8):
        angle = -math.pi * 0.75 + i * (2 * math.pi / 8)
        px = cx + ring_radius * math.cos(angle)
        py = cy + ring_radius * math.sin(angle)
        
        svg.append(f'<circle cx="{px}" cy="{py}" r="26" fill="{C_WHITE}" stroke="{C_WINE_PRIMARY}" stroke-width="3"/>')
        svg.append(f'<text x="{px}" y="{py + 7}" font-family="Courier New, monospace" font-size="16" font-weight="bold" fill="{C_WINE_PRIMARY}" text-anchor="middle">{phase_labels[i]}</text>')

    # 4 CAJAS DE INTERVENCIÓN DE LA IA (I1, I2, I3, I4)
    interventions = [
        {
            "id": "I1",
            "pos": "top-right",
            "x": 1070, "y": 140, "w": 430, "h": 160,
            "target_angle": -math.pi * 0.5, # entre P2 y P3
            "phase": "Fase P2 → P3: Ideación",
            "prompt": "¿Qué otros ángulos no has considerado aún?",
            "role": "Ensancha el espacio de ideación sin sugerir contenido ni introducir términos ajenos.",
            "color": C_WINE_PRIMARY
        },
        {
            "id": "I2",
            "pos": "bottom-right",
            "x": 1070, "y": 660, "w": 430, "h": 160,
            "target_angle": math.pi * 0.0, # entre P3 y P4
            "phase": "Fase P3 → P4: Organización",
            "prompt": "Representación jerárquica con el vocabulario del usuario",
            "role": "Propuesta estructural basada exclusivamente en los conceptos anotados por el autor.",
            "color": C_RED_ACCENT
        },
        {
            "id": "I3",
            "pos": "bottom-left",
            "x": 60, "y": 660, "w": 430, "h": 160,
            "target_angle": math.pi * 0.5, # entre P6 y P7
            "phase": "Fase P6 → P7: Evaluación",
            "prompt": "Tu meta era persuadir sobre... ¿En qué parte se aborda?",
            "role": "Contraste objetivo entre la intención inicial declarada y el borrador redactado.",
            "color": C_GOLD_DARK
        },
        {
            "id": "I4",
            "pos": "top-left",
            "x": 60, "y": 140, "w": 430, "h": 160,
            "target_angle": math.pi * 1.0, # entre P7 y P8
            "phase": "Fase P7 → P8: Integración",
            "prompt": "¿Qué esperabas que ocurriera al escribir esa frase?",
            "role": "Sostiene el espacio narrativo de la reflexión y consolida lo aprendido.",
            "color": C_WINE_PRIMARY
        }
    ]

    for item in interventions:
        ix, iy, iw, ih = item["x"], item["y"], item["w"], item["h"]
        svg.append(f'<rect x="{ix}" y="{iy}" width="{iw}" height="{ih}" fill="{C_PINK_BG}" stroke="{item["color"]}" stroke-width="2"/>')
        svg.append(f'<rect x="{ix}" y="{iy}" width="{iw}" height="6" fill="{item["color"]}"/>')
        
        # Badge
        svg.append(f'<rect x="{ix + 16}" y="{iy + 18}" width="34" height="26" fill="{item["color"]}"/>')
        svg.append(f'<text x="{ix + 33}" y="{iy + 36}" font-family="Courier New, monospace" font-size="16" font-weight="bold" fill="{C_WHITE}" text-anchor="middle">{item["id"]}</text>')
        svg.append(f'<text x="{ix + 60}" y="{iy + 36}" font-family="Courier New, monospace" font-size="15" font-weight="bold" fill="{item["color"]}">{item["phase"]}</text>')
        
        # Pregunta exacta entrecomillada
        svg.append(f'<text x="{ix + 16}" y="{iy + 70}" font-family="Arial, sans-serif" font-size="17" font-weight="bold" fill="{C_TEXT_DARK}">"{item["prompt"]}"</text>')
        
        # Explicación del rol
        svg.append(f'<line x1="{ix + 16}" y1="{iy + 92}" x2="{ix + iw - 16}" y2="{iy + 92}" stroke="{C_BORDER_SUBTLE}" stroke-width="1"/>')
        svg.append(f'<text x="{ix + 16}" y="{iy + 116}" font-family="Arial, sans-serif" font-size="14" fill="{C_GRAY_TEXT}">{item["role"][:48]}</text>')
        svg.append(f'<text x="{ix + 16}" y="{iy + 138}" font-family="Arial, sans-serif" font-size="14" fill="{C_GRAY_TEXT}">{item["role"][48:]}</text>')

        # Línea de llamada apuntando hacia el anillo
        tx = cx + ring_radius * math.cos(item["target_angle"])
        ty = cy + ring_radius * math.sin(item["target_angle"])
        
        call_x = ix + iw if "left" in item["pos"] else ix
        call_y = iy + ih / 2
        
        svg.append(f'<line x1="{call_x}" y1="{call_y}" x2="{tx}" y2="{ty}" stroke="{item["color"]}" stroke-width="2.5" stroke-dasharray="5,4"/>')
        svg.append(f'<circle cx="{tx}" cy="{ty}" r="6" fill="{item["color"]}"/>')

    # Franja inferior de principio rector
    svg.append(f'<rect x="60" y="{h - 95}" width="{w - 120}" height="45" fill="{C_WINE_PRIMARY}"/>')
    svg.append(f'<text x="{w/2}" y="{h - 66}" font-family="Arial, sans-serif" font-size="18" font-weight="bold" fill="{C_WHITE}" text-anchor="middle">PRINCIPIO DE NO SUSTITUCIÓN: La IA nunca redacta borradores ni califica; solo formula preguntas basadas en las palabras del autor.</text>')

    svg.append('</svg>')
    out_svg = FIGURAS_DIR / "figura_3_modelo_con_ia.svg"
    out_svg.write_text("\n".join(svg), encoding="utf-8")
    print(f"Figura 3 generada en: {out_svg}")
    return out_svg

# ==============================================================================
# FIGURA 4: DIAGRAMA DE ACTIVIDADES DE LA LÓGICA DEL AGENTE CONVERSACIONAL
# ==============================================================================
def generar_figura_4():
    w, h = 1560, 960
    
    svg = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="100%" height="100%">']
    svg.append(f'<rect width="{w}" height="{h}" fill="{C_WHITE}"/>')
    
    # Encabezado
    svg.append(f'<text x="60" y="55" font-family="Arial, sans-serif" font-size="28" font-weight="bold" fill="{C_TEXT_DARK}">DIAGRAMA DE ACTIVIDADES: LÓGICA OPERATIVA DEL AGENTE</text>')
    svg.append(f'<text x="60" y="85" font-family="Arial, sans-serif" font-size="18" fill="{C_GRAY_TEXT}">Árbol de decisión, disparadores semánticos, bucles reflexivos y ruta pragmática de salida directa</text>')
    svg.append(f'<line x1="60" y1="102" x2="{w-60}" y2="102" stroke="{C_BORDER_SUBTLE}" stroke-width="2"/>')

    # Marcadores de flechas
    svg.append('<defs>')
    svg.append(f'<marker id="f4-arrow" markerWidth="8" markerHeight="8" refX="6" refY="4" orient="auto"><polygon points="0 0, 8 4, 0 8" fill="{C_WINE_PRIMARY}"/></marker>')
    svg.append(f'<marker id="f4-gold" markerWidth="8" markerHeight="8" refX="6" refY="4" orient="auto"><polygon points="0 0, 8 4, 0 8" fill="{C_GOLD_DARK}"/></marker>')
    svg.append('</defs>')

    # 1. Nodo Inicio (Autor)
    svg.append(f'<rect x="60" y="440" width="180" height="70" fill="{C_PINK_BG}" stroke="{C_WINE_PRIMARY}" stroke-width="2.5"/>')
    svg.append(f'<rect x="60" y="440" width="180" height="6" fill="{C_WINE_PRIMARY}"/>')
    svg.append(f'<text x="150" y="472" font-family="Arial, sans-serif" font-size="16" font-weight="bold" fill="{C_TEXT_DARK}" text-anchor="middle">El escritor inicia</text>')
    svg.append(f'<text x="150" y="494" font-family="Arial, sans-serif" font-size="15" fill="{C_GRAY_TEXT}" text-anchor="middle">o comparte texto</text>')

    # Conector a Detección
    svg.append(f'<line x1="240" y1="475" x2="300" y2="475" stroke="{C_WINE_PRIMARY}" stroke-width="2.5" marker-end="url(#f4-arrow)"/>')

    # 2. Rombo 1: ¿Agente detecta señal?
    rx1, ry1 = 370, 475
    rw, rh = 70, 45
    pts1 = f"{rx1},{ry1-rh} {rx1+rw},{ry1} {rx1},{ry1+rh} {rx1-rw},{ry1}"
    svg.append(f'<polygon points="{pts1}" fill="{C_PINK_BG}" stroke="{C_WINE_PRIMARY}" stroke-width="2.5"/>')
    svg.append(f'<text x="{rx1}" y="{ry1 - 6}" font-family="Arial, sans-serif" font-size="14" font-weight="bold" fill="{C_TEXT_DARK}" text-anchor="middle">¿Detecta</text>')
    svg.append(f'<text x="{rx1}" y="{ry1 + 14}" font-family="Arial, sans-serif" font-size="14" font-weight="bold" fill="{C_TEXT_DARK}" text-anchor="middle">señal?</text>')

    # Si No -> Espera
    svg.append(f'<line x1="{rx1}" y1="{ry1+rh}" x2="{rx1}" y2="580" stroke="{C_GRAY_MUTED}" stroke-width="2" stroke-dasharray="4,3"/>')
    svg.append(f'<rect x="{rx1 - 70}" y="580" width="140" height="40" fill="{C_WHITE}" stroke="{C_BORDER_SUBTLE}" stroke-width="1"/>')
    svg.append(f'<text x="{rx1}" y="605" font-family="Arial, sans-serif" font-size="13" fill="{C_GRAY_MUTED}" text-anchor="middle">Espera pasiva</text>')

    # Si Sí -> Conector a Tipo de señal
    svg.append(f'<line x1="{rx1+rw}" y1="{ry1}" x2="500" y2="{ry1}" stroke="{C_WINE_PRIMARY}" stroke-width="2.5" marker-end="url(#f4-arrow)"/>')
    svg.append(f'<text x="465" y="{ry1 - 10}" font-family="Courier New, monospace" font-size="14" font-weight="bold" fill="{C_RED_ACCENT}">SÍ</text>')

    # 3. 4 Ramas según Tipo de Señal
    signals = [
        {"y": 180, "name": "Bloqueo / Repetición", "action": "Activar I1 o I2: Ensanchar o estructurar con sus términos"},
        {"y": 300, "name": "Desajuste con meta", "action": "Activar I3: Devolver fragmento conflictivo vs. meta"},
        {"y": 420, "name": "Sorpresa / Duda", "action": "Activar I4: Preguntar qué cambió en su comprensión"},
        {"y": 540, "name": "Consulta directa", "action": "Orientar sobre el paso actual sin sugerir contenido"}
    ]

    for s in signals:
        sy = s["y"]
        # Línea divisoria ortogonal
        svg.append(f'<path d="M 500 475 L 530 475 L 530 {sy + 30} L 560 {sy + 30}" fill="none" stroke="{C_WINE_PRIMARY}" stroke-width="2"/>')
        
        # Caja de Rama
        svg.append(f'<rect x="560" y="{sy}" width="310" height="60" fill="{C_PINK_BG}" stroke="{C_WINE_PRIMARY}" stroke-width="1.8"/>')
        svg.append(f'<text x="575" y="{sy + 24}" font-family="Courier New, monospace" font-size="14" font-weight="bold" fill="{C_RED_ACCENT}">[SEÑAL] {s["name"]}</text>')
        svg.append(f'<text x="575" y="{sy + 46}" font-family="Arial, sans-serif" font-size="13" fill="{C_TEXT_DARK}">{s["action"][:38]}...</text>')

        # Conector hacia Devolución
        svg.append(f'<path d="M 870 {sy + 30} L 900 {sy + 30} L 900 475 L 930 475" fill="none" stroke="{C_WINE_PRIMARY}" stroke-width="2"/>')

    # 4. Bloque Maestro: Devolver palabras en forma de pregunta
    svg.append(f'<rect x="930" y="430" width="220" height="90" fill="{C_WINE_PRIMARY}"/>')
    svg.append(f'<text x="1040" y="462" font-family="Courier New, monospace" font-size="14" font-weight="bold" fill="{C_GOLD}" text-anchor="middle">REGLA FUNDAMENTAL</text>')
    svg.append(f'<text x="1040" y="488" font-family="Arial, sans-serif" font-size="16" font-weight="bold" fill="{C_WHITE}" text-anchor="middle">Devolver palabras del</text>')
    svg.append(f'<text x="1040" y="508" font-family="Arial, sans-serif" font-size="16" font-weight="bold" fill="{C_WHITE}" text-anchor="middle">autor como pregunta</text>')

    # Conector a respuesta
    svg.append(f'<line x1="1150" y1="475" x2="1200" y2="475" stroke="{C_WINE_PRIMARY}" stroke-width="2.5" marker-end="url(#f4-arrow)"/>')

    # 5. Tres Caminos del Autor tras la pregunta
    # Camino 1: Responde y elabora -> Condición de avance
    svg.append(f'<path d="M 1200 475 L 1220 475 L 1220 280 L 1260 280" fill="none" stroke="{C_WINE_PRIMARY}" stroke-width="2.5" marker-end="url(#f4-arrow)"/>')
    svg.append(f'<rect x="1260" y="245" width="240" height="70" fill="{C_PINK_BG}" stroke="{C_WINE_PRIMARY}" stroke-width="2"/>')
    svg.append(f'<text x="1380" y="272" font-family="Courier New, monospace" font-size="14" font-weight="bold" fill="{C_WINE_PRIMARY}" text-anchor="middle">¿Cumple condición?</text>')
    svg.append(f'<text x="1380" y="296" font-family="Arial, sans-serif" font-size="14" font-weight="bold" fill="{C_RED_ACCENT}" text-anchor="middle">SÍ → Ofrecer avance a P+1</text>')

    # Camino 2: RUTA PRAGMÁTICA (Rechaza / Prisa)
    svg.append(f'<line x1="1200" y1="475" x2="1260" y2="475" stroke="{C_GOLD_DARK}" stroke-width="3" marker-end="url(#f4-gold)"/>')
    svg.append(f'<rect x="1260" y="440" width="240" height="70" fill="#FDF8E8" stroke="{C_GOLD_DARK}" stroke-width="2.5"/>')
    svg.append(f'<text x="1380" y="468" font-family="Courier New, monospace" font-size="14" font-weight="bold" fill="{C_GOLD_DARK}" text-anchor="middle">RUTA PRAGMÁTICA</text>')
    svg.append(f'<text x="1380" y="492" font-family="Arial, sans-serif" font-size="14" font-weight="bold" fill="{C_TEXT_DARK}" text-anchor="middle">Permitir saltar reflexión</text>')

    # Camino 3: Silencio / No responde
    svg.append(f'<path d="M 1200 475 L 1220 475 L 1220 670 L 1260 670" fill="none" stroke="{C_GRAY_MUTED}" stroke-width="2.5" marker-end="url(#f4-arrow)"/>')
    svg.append(f'<rect x="1260" y="635" width="240" height="70" fill="{C_WHITE}" stroke="{C_BORDER_SUBTLE}" stroke-width="2"/>')
    svg.append(f'<text x="1380" y="662" font-family="Courier New, monospace" font-size="14" font-weight="bold" fill="{C_GRAY_TEXT}" text-anchor="middle">SILENCIO / NO RESPUESTA</text>')
    svg.append(f'<text x="1380" y="686" font-family="Arial, sans-serif" font-size="14" fill="{C_GRAY_MUTED}" text-anchor="middle">No insistir; guardar silencio</text>')

    # Retorno de ciclo
    svg.append(f'<path d="M 1500 280 L 1530 280 L 1530 840 L 370 840 L 370 520" fill="none" stroke="{C_WINE_PRIMARY}" stroke-width="2" stroke-dasharray="6,4" marker-end="url(#f4-arrow)"/>')
    svg.append(f'<text x="950" y="830" font-family="Courier New, monospace" font-size="14" font-weight="bold" fill="{C_WINE_PRIMARY}" text-anchor="middle">BUCLE DE ACOMPAÑAMIENTO HASTA CONFRONTACIÓN O CIERRE DEL BORRADOR</text>')

    # Epígrafe inferior
    svg.append(f'<text x="60" y="{h - 35}" font-family="Arial, sans-serif" font-size="16" font-weight="bold" fill="{C_TEXT_DARK}">Fig. 4. Diagrama de actividades de la lógica de mediación del agente conversacional.</text>')
    svg.append(f'<text x="730" y="{h - 35}" font-family="Arial, sans-serif" font-size="15" font-style="italic" fill="{C_GRAY_MUTED}">Las intervenciones I1–I4 se activan a demanda del autor; la ruta pragmática garantiza fluidez. Fuente: Autores.</text>')

    svg.append('</svg>')
    out_svg = FIGURAS_DIR / "figura_4_diagrama_actividades.svg"
    out_svg.write_text("\n".join(svg), encoding="utf-8")
    print(f"Figura 4 generada en: {out_svg}")
    return out_svg

# ==============================================================================
# FIGURA 5: MATRIZ DE VALIDACIÓN PRÁCTICA CON TRES PERFILES
# ==============================================================================
def generar_figura_5():
    w, h = 1560, 840
    
    svg = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="100%" height="100%">']
    svg.append(f'<rect width="{w}" height="{h}" fill="{C_WHITE}"/>')
    
    # Encabezado
    svg.append(f'<text x="60" y="55" font-family="Arial, sans-serif" font-size="28" font-weight="bold" fill="{C_TEXT_DARK}">PRUEBAS DE ESCRITORIO: RESPUESTA DE LA MEDIACIÓN ANTE TRES PERFILES</text>')
    svg.append(f'<text x="60" y="85" font-family="Arial, sans-serif" font-size="18" fill="{C_GRAY_TEXT}">Simulaciones con Novato, Competente y Experto: adaptabilidad al punto de partida y no sustitución</text>')
    svg.append(f'<line x1="60" y1="102" x2="{w-60}" y2="102" stroke="{C_BORDER_SUBTLE}" stroke-width="2"/>')

    # Columnas de Fases P3 a P8
    cols = [
        {"id": "P3", "name": "Generar ideas", "w": 220},
        {"id": "P4", "name": "Organizar", "w": 220},
        {"id": "P5", "name": "Definir metas", "w": 220},
        {"id": "P6", "name": "Redactar", "w": 220},
        {"id": "P7", "name": "Releer / Evaluar", "w": 220},
        {"id": "P8", "name": "Integración", "w": 220}
    ]
    
    start_x = 220
    header_y = 125
    header_h = 50
    
    # Celda superior izquierda
    svg.append(f'<rect x="60" y="{header_y}" width="160" height="{header_h}" fill="{C_WINE_DARK}"/>')
    svg.append(f'<text x="140" y="{header_y + 32}" font-family="Courier New, monospace" font-size="16" font-weight="bold" fill="{C_WHITE}" text-anchor="middle">PERFIL</text>')
    
    cx = start_x
    for c in cols:
        svg.append(f'<rect x="{cx}" y="{header_y}" width="{c["w"]}" height="{header_h}" fill="{C_WINE_PRIMARY}" stroke="{C_WHITE}" stroke-width="1.5"/>')
        svg.append(f'<text x="{cx + c["w"]/2}" y="{header_y + 24}" font-family="Courier New, monospace" font-size="16" font-weight="bold" fill="{C_GOLD}" text-anchor="middle">{c["id"]}</text>')
        svg.append(f'<text x="{cx + c["w"]/2}" y="{header_y + 42}" font-family="Arial, sans-serif" font-size="13" font-weight="bold" fill="{C_WHITE}" text-anchor="middle">{c["name"]}</text>')
        cx += c["w"]

    # FILA 1: NOVATO
    r1_y = 185
    r1_h = 180
    svg.append(f'<rect x="60" y="{r1_y}" width="160" height="{r1_h}" fill="{C_PINK_BG}" stroke="{C_BORDER_SUBTLE}" stroke-width="1.5"/>')
    svg.append(f'<rect x="60" y="{r1_y}" width="6" height="{r1_h}" fill="{C_WINE_PRIMARY}"/>')
    svg.append(f'<text x="140" y="{r1_y + 65}" font-family="Arial, sans-serif" font-size="22" font-weight="bold" fill="{C_TEXT_DARK}" text-anchor="middle">Novato</text>')
    svg.append(f'<text x="140" y="{r1_y + 95}" font-family="Courier New, monospace" font-size="13" fill="{C_RED_ACCENT}" text-anchor="middle">Recorrido</text>')
    svg.append(f'<text x="140" y="{r1_y + 115}" font-family="Courier New, monospace" font-size="13" fill="{C_RED_ACCENT}" text-anchor="middle">Completo</text>')

    r1_cells = [
        {"author": "Se traba repitiendo palabras.", "ai": "Devuelve sus términos sin sugerir ideas."},
        {"author": "Siente que sus notas dicen lo mismo.", "ai": "Junta todo en un solo bloque estructurado."},
        {"author": "Fija meta simple: 'el celular distrae'.", "ai": "Pide ideas y meta antes de redactar."},
        {"author": "Escribe un borrador breve.", "ai": "Guarda silencio para no interrumpir."},
        {"author": "Relee y lo ve suficiente.", "ai": "Respeta su cierre sin insistir."},
        {"skip": True, "title": "NO REQUERIDO", "desc": "Cierra el proceso en P7 por decisión propia."}
    ]
    
    cx = start_x
    for cell in r1_cells:
        svg.append(f'<rect x="{cx}" y="{r1_y}" width="220" height="{r1_h}" fill="{C_WHITE}" stroke="{C_BORDER_SUBTLE}" stroke-width="1.5"/>')
        if cell.get("skip"):
            svg.append(f'<rect x="{cx + 10}" y="{r1_y + 10}" width="200" height="{r1_h - 20}" fill="{C_PINK_BG}" stroke="{C_GRAY_MUTED}" stroke-width="1" stroke-dasharray="4,4"/>')
            svg.append(f'<text x="{cx + 110}" y="{r1_y + 85}" font-family="Courier New, monospace" font-size="14" font-weight="bold" fill="{C_GRAY_MUTED}" text-anchor="middle">{cell["title"]}</text>')
            svg.append(f'<text x="{cx + 110}" y="{r1_y + 110}" font-family="Arial, sans-serif" font-size="12" fill="{C_GRAY_TEXT}" text-anchor="middle">{cell["desc"][:24]}</text>')
            svg.append(f'<text x="{cx + 110}" y="{r1_y + 128}" font-family="Arial, sans-serif" font-size="12" fill="{C_GRAY_TEXT}" text-anchor="middle">{cell["desc"][24:]}</text>')
        else:
            svg.append(f'<text x="{cx + 16}" y="{r1_y + 35}" font-family="Arial, sans-serif" font-size="14" font-weight="bold" fill="{C_TEXT_DARK}">{cell["author"][:24]}</text>')
            svg.append(f'<text x="{cx + 16}" y="{r1_y + 55}" font-family="Arial, sans-serif" font-size="14" font-weight="bold" fill="{C_TEXT_DARK}">{cell["author"][24:]}</text>')
            
            # Badge IA
            svg.append(f'<rect x="{cx + 16}" y="{r1_y + 85}" width="32" height="20" fill="{C_WINE_PRIMARY}"/>')
            svg.append(f'<text x="{cx + 32}" y="{r1_y + 100}" font-family="Courier New, monospace" font-size="12" font-weight="bold" fill="{C_WHITE}" text-anchor="middle">IA</text>')
            svg.append(f'<text x="{cx + 16}" y="{r1_y + 125}" font-family="Arial, sans-serif" font-size="13" fill="{C_GRAY_TEXT}">{cell["ai"][:25]}</text>')
            svg.append(f'<text x="{cx + 16}" y="{r1_y + 145}" font-family="Arial, sans-serif" font-size="13" fill="{C_GRAY_TEXT}">{cell["ai"][25:]}</text>')
        cx += 220

    # FILA 2: COMPETENTE
    r2_y = 375
    r2_h = 180
    svg.append(f'<rect x="60" y="{r2_y}" width="160" height="{r2_h}" fill="{C_PINK_BG}" stroke="{C_BORDER_SUBTLE}" stroke-width="1.5"/>')
    svg.append(f'<rect x="60" y="{r2_y}" width="6" height="{r2_h}" fill="{C_RED_ACCENT}"/>')
    svg.append(f'<text x="140" y="{r2_y + 65}" font-family="Arial, sans-serif" font-size="22" font-weight="bold" fill="{C_TEXT_DARK}" text-anchor="middle">Competente</text>')
    svg.append(f'<text x="140" y="{r2_y + 95}" font-family="Courier New, monospace" font-size="13" fill="{C_WINE_PRIMARY}" text-anchor="middle">Recorrido</text>')
    svg.append(f'<text x="140" y="{r2_y + 115}" font-family="Courier New, monospace" font-size="13" fill="{C_WINE_PRIMARY}" text-anchor="middle">Acotado</text>')

    r2_cells = [
        {"skip": True, "title": "NO REQUERIDO", "desc": "Llega con ideas ya estructuradas."},
        {"author": "Pide evaluar sus ideas.", "ai": "Rehúsa calificar; valida utilidad."},
        {"author": "Fija meta: autonomía con disciplina.", "ai": "Solicita insumos previos al texto."},
        {"author": "Redacta 2 párrafos fluidos.", "ai": "Guarda silencio durante redacción."},
        {"author": "Nota contradicción en §2.", "ai": "Muestra el choque; autor reescribe."},
        {"skip": True, "title": "NO REQUERIDO", "desc": "Cierra satisfecho tras reescritura."}
    ]
    
    cx = start_x
    for cell in r2_cells:
        svg.append(f'<rect x="{cx}" y="{r2_y}" width="220" height="{r2_h}" fill="{C_WHITE}" stroke="{C_BORDER_SUBTLE}" stroke-width="1.5"/>')
        if cell.get("skip"):
            svg.append(f'<rect x="{cx + 10}" y="{r2_y + 10}" width="200" height="{r2_h - 20}" fill="{C_PINK_BG}" stroke="{C_GRAY_MUTED}" stroke-width="1" stroke-dasharray="4,4"/>')
            svg.append(f'<text x="{cx + 110}" y="{r2_y + 85}" font-family="Courier New, monospace" font-size="14" font-weight="bold" fill="{C_GRAY_MUTED}" text-anchor="middle">{cell["title"]}</text>')
            svg.append(f'<text x="{cx + 110}" y="{r2_y + 110}" font-family="Arial, sans-serif" font-size="12" fill="{C_GRAY_TEXT}" text-anchor="middle">{cell["desc"][:24]}</text>')
            svg.append(f'<text x="{cx + 110}" y="{r2_y + 128}" font-family="Arial, sans-serif" font-size="12" fill="{C_GRAY_TEXT}" text-anchor="middle">{cell["desc"][24:]}</text>')
        else:
            svg.append(f'<text x="{cx + 16}" y="{r2_y + 35}" font-family="Arial, sans-serif" font-size="14" font-weight="bold" fill="{C_TEXT_DARK}">{cell["author"][:24]}</text>')
            svg.append(f'<text x="{cx + 16}" y="{r2_y + 55}" font-family="Arial, sans-serif" font-size="14" font-weight="bold" fill="{C_TEXT_DARK}">{cell["author"][24:]}</text>')
            
            svg.append(f'<rect x="{cx + 16}" y="{r2_y + 85}" width="32" height="20" fill="{C_RED_ACCENT}"/>')
            svg.append(f'<text x="{cx + 32}" y="{r2_y + 100}" font-family="Courier New, monospace" font-size="12" font-weight="bold" fill="{C_WHITE}" text-anchor="middle">IA</text>')
            svg.append(f'<text x="{cx + 16}" y="{r2_y + 125}" font-family="Arial, sans-serif" font-size="13" fill="{C_GRAY_TEXT}">{cell["ai"][:25]}</text>')
            svg.append(f'<text x="{cx + 16}" y="{r2_y + 145}" font-family="Arial, sans-serif" font-size="13" fill="{C_GRAY_TEXT}">{cell["ai"][25:]}</text>')
        cx += 220

    # FILA 3: EXPERTO
    r3_y = 565
    r3_h = 180
    svg.append(f'<rect x="60" y="{r3_y}" width="160" height="{r3_h}" fill="{C_PINK_BG}" stroke="{C_BORDER_SUBTLE}" stroke-width="1.5"/>')
    svg.append(f'<rect x="60" y="{r3_y}" width="6" height="{r3_h}" fill="{C_GOLD_DARK}"/>')
    svg.append(f'<text x="140" y="{r3_y + 65}" font-family="Arial, sans-serif" font-size="22" font-weight="bold" fill="{C_TEXT_DARK}" text-anchor="middle">Experto</text>')
    svg.append(f'<text x="140" y="{r3_y + 95}" font-family="Courier New, monospace" font-size="13" fill="{C_GOLD_DARK}" text-anchor="middle">Revisión</text>')
    svg.append(f'<text x="140" y="{r3_y + 115}" font-family="Courier New, monospace" font-size="13" fill="{C_GOLD_DARK}" text-anchor="middle">Avanzada</text>')

    # P3 a P6 unidos (Fases previas ya elaboradas)
    span_w = 220 * 4
    svg.append(f'<rect x="{start_x}" y="{r3_y}" width="{span_w}" height="{r3_h}" fill="{C_WHITE}" stroke="{C_BORDER_SUBTLE}" stroke-width="1.5"/>')
    svg.append(f'<rect x="{start_x + 20}" y="{r3_y + 20}" width="{span_w - 40}" height="{r3_h - 40}" fill="{C_PINK_BG}" stroke="{C_GRAY_MUTED}" stroke-width="1.5" stroke-dasharray="6,4"/>')
    svg.append(f'<text x="{start_x + span_w/2}" y="{r3_y + 80}" font-family="Courier New, monospace" font-size="18" font-weight="bold" fill="{C_WINE_PRIMARY}" text-anchor="middle">FASES PREVIAS YA ELABORADAS (P3 A P6 SUPERADOS)</text>')
    svg.append(f'<text x="{start_x + span_w/2}" y="{r3_y + 115}" font-family="Arial, sans-serif" font-size="16" fill="{C_GRAY_TEXT}" text-anchor="middle">El escritor llega directamente con un borrador avanzado terminado; el asistente se acopla de inmediato.</text>')

    # P7
    p7_x = start_x + span_w
    svg.append(f'<rect x="{p7_x}" y="{r3_y}" width="220" height="{r3_h}" fill="{C_WHITE}" stroke="{C_BORDER_SUBTLE}" stroke-width="1.5"/>')
    svg.append(f'<text x="{p7_x + 16}" y="{r3_y + 35}" font-family="Arial, sans-serif" font-size="14" font-weight="bold" fill="{C_TEXT_DARK}">Al releer, su texto</text>')
    svg.append(f'<text x="{p7_x + 16}" y="{r3_y + 55}" font-family="Arial, sans-serif" font-size="14" font-weight="bold" fill="{C_TEXT_DARK}">contradice su tesis.</text>')
    svg.append(f'<rect x="{p7_x + 16}" y="{r3_y + 85}" width="32" height="20" fill="{C_GOLD_DARK}"/>')
    svg.append(f'<text x="{p7_x + 32}" y="{r3_y + 100}" font-family="Courier New, monospace" font-size="12" font-weight="bold" fill="{C_WHITE}" text-anchor="middle">IA</text>')
    svg.append(f'<text x="{p7_x + 16}" y="{r3_y + 125}" font-family="Arial, sans-serif" font-size="13" fill="{C_GRAY_TEXT}">Pregunta qué descubrió</text>')
    svg.append(f'<text x="{p7_x + 16}" y="{r3_y + 145}" font-family="Arial, sans-serif" font-size="13" fill="{C_GRAY_TEXT}">de nuevo en la relectura.</text>')

    # P8
    p8_x = p7_x + 220
    svg.append(f'<rect x="{p8_x}" y="{r3_y}" width="220" height="{r3_h}" fill="{C_WHITE}" stroke="{C_BORDER_SUBTLE}" stroke-width="1.5"/>')
    svg.append(f'<text x="{p8_x + 16}" y="{r3_y + 35}" font-family="Arial, sans-serif" font-size="14" font-weight="bold" fill="{C_TEXT_DARK}">Cambia su marco</text>')
    svg.append(f'<text x="{p8_x + 16}" y="{r3_y + 55}" font-family="Arial, sans-serif" font-size="14" font-weight="bold" fill="{C_TEXT_DARK}">conceptual previo.</text>')
    svg.append(f'<rect x="{p8_x + 16}" y="{r3_y + 85}" width="32" height="20" fill="{C_WINE_PRIMARY}"/>')
    svg.append(f'<text x="{p8_x + 32}" y="{r3_y + 100}" font-family="Courier New, monospace" font-size="12" font-weight="bold" fill="{C_WHITE}" text-anchor="middle">IA</text>')
    svg.append(f'<text x="{p8_x + 16}" y="{r3_y + 125}" font-family="Arial, sans-serif" font-size="13" fill="{C_GRAY_TEXT}">Cierra reconociendo</text>')
    svg.append(f'<text x="{p8_x + 16}" y="{r3_y + 145}" font-family="Arial, sans-serif" font-size="13" fill="{C_GRAY_TEXT}">la plena autoría.</text>')

    # Epígrafe inferior
    svg.append(f'<text x="60" y="{h - 35}" font-family="Arial, sans-serif" font-size="16" font-weight="bold" fill="{C_TEXT_DARK}">Fig. 5. Prueba de escritorio con tres perfiles simulados.</text>')
    svg.append(f'<text x="490" y="{h - 35}" font-family="Arial, sans-serif" font-size="15" font-style="italic" fill="{C_GRAY_MUTED}">Demuestra adaptabilidad al vocabulario, respeto al cierre voluntario y no sustitución. Fuente: Autores.</text>')

    svg.append('</svg>')
    out_svg = FIGURAS_DIR / "figura_5_validacion_practica.svg"
    out_svg.write_text("\n".join(svg), encoding="utf-8")
    print(f"Figura 5 generada en: {out_svg}")
    return out_svg

def exportar_pngs():
    svgs = [
        FIGURAS_DIR / "figura_1_radar.svg",
        FIGURAS_DIR / "figura_2_modelo_sin_ia.svg",
        FIGURAS_DIR / "figura_3_modelo_con_ia.svg",
        FIGURAS_DIR / "figura_4_diagrama_actividades.svg",
        FIGURAS_DIR / "figura_5_validacion_practica.svg"
    ]
    for s_path in svgs:
        if not s_path.exists():
            continue
        png_path = s_path.with_suffix(".png")
        doc = fitz.open(str(s_path))
        page = doc[0]
        # 300 DPI
        pix = page.get_pixmap(dpi=300)
        pix.save(str(png_path))
        print(f"Exportado PNG 300 DPI: {png_path} ({pix.width}x{pix.height} px)")

if __name__ == "__main__":
    print("Iniciando generación de figuras científicas vectoriales...")
    generar_figura_1()
    generar_figura_2()
    generar_figura_3()
    generar_figura_4()
    generar_figura_5()
    print("Exportando a PNG de alta resolución (300 DPI) con PyMuPDF...")
    exportar_pngs()
    print("¡Proceso de figuras finalizado exitosamente!")
