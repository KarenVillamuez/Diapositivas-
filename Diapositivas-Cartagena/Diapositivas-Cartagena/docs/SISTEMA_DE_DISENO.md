# Sistema de Diseño Oficial: LHXT26 Cartagena 2026
**VI Congreso Internacional de Investigación Interdisciplinar**
*Documento de Especificación Técnica, Visual y Arquitectura de Diseño*

---

## 1. Filosofía y Principios Rectores

El sistema de diseño de la plantilla **LHXT26 Cartagena 2026** está concebido bajo una tradición **editorial académica formal** con reminiscencias del estilo tipográfico internacional (Escuela Suiza), adaptado a la identidad institucional del evento en Cartagena de Indias.

```
┌──────────────────────────────────────────────────────────────────────────────┐
│                            PRINCIPIOS FUNDAMENTALES                          │
├──────────────────────┬────────────────────────┬──────────────────────────────┤
│ 1. Rigor Académico   │ 2. Dualidad Tipográfica│ 3. Precisión Geométrica      │
│ Ausencia de adornos  │ Sans-Serif humanista   │ Rejilla fija de 1920×1080 px │
│ artificiales; cero   │ para lectura fluida +  │ con zonas de protección      │
│ cajas anidadas;      │ monoespaciado técnico  │ exactas y márgenes de 110 px │
│ contraste máximo.    │ para datos y códigos.  │ en todos los cuadrantes.     │
└──────────────────────┴────────────────────────┴──────────────────────────────┘
```

### 1.1. Reglas Estrictas de Composición Visual (Anti-Patrones Prohibidos)

1. **Prohibición Absoluta de Cajas Anidadas (Cero Rectángulos dentro de Rectángulos):**
   - Nunca debe dibujarse una tarjeta con borde o fondo dentro de otra tarjeta que ya posee borde o fondo (anti-patrón *card-in-card*).
   - Los metadatos, notas, fuentes y salidas secundarias deben integrarse con **separadores de línea sutiles de 1 px** (`border-top: 1px solid var(--c-border-subtle)`), nunca mediante cajas o recuadros flotantes internos.

2. **Garantía de Aire Negativo (Prevención de Amontonamiento):**
   - El bloque de contenido útil nunca debe sobrepasar `Y = 860 px`. Debe preservarse siempre un colchón de aire de al menos `100 px` respecto a la línea del pie de página (`Y = 972 px`).
   - Al ampliar el tamaño tipográfico para auditorio, los párrafos deben formularse de manera concisa y ejecutiva (máximo 2 a 3 líneas por ítem), evitando que los contenedores colapsen verticalmente contra el pie de página.

3. **Equilibrio Espacial y Erradicación del Espacio Muerto (Anti-patrón Top-Heavy):**
   - El contenido no debe colgarse exclusivamente del tercio superior de la diapositiva dejando 300–400 px de vacío blanco abandonado en la parte inferior.
   - En diapositivas con listas, agendas o bloques (como la Agenda o el Pipeline), el área de contenido (`.slide-content-area`) debe utilizar centrado o distribución vertical armónica (`display: flex; flex-direction: column; justify-content: center;` o reparto proporcional con `gap` generoso), llenando el lienzo con dignidad, equilibrio y presencia escénica.

4. **Armonía y Progresión de Escala Tipográfica (Fin de la Brecha Abrupta):**
   - Queda estrictamente prohibido colocar cifras o títulos colosales (60–80 px) inmediatamente al lado o encima de microtextos diminutos (18–20 px). La escala debe tener progresión fluida:
     - Títulos de diapositiva / Lead questions: `38 px` – `44 px` bold.
     - Subtítulos de sección / Nombres de bloque: `30 px` – `34 px` bold.
     - Cifras métricas maestras: `54 px` – `64 px` bold.
     - Conceptos y viñetas centrales: `24 px` – `28 px`.
     - Conclusiones y Veredictos integrados: `24 px` – `26 px` semibold/bold.
     - Metadatos y fuentes técnicas: mínimo `20 px` – `22 px` (nunca inferior a `20 px`).

5. **Dignificación de Conclusiones y Veredictos (El Veredicto NO es una Nota al Pie):**
   - Las conclusiones determinantes de una diapositiva (tales como *"Veredicto: El algoritmo premia apego al texto, no pedagogía real"* o *"Meta: ..."*) jamás deben relegarse a un `editorial-footnote` diminuto de 18–20 px que simule una advertencia legal secundaria.
   - Deben presentarse como **filas de conclusión integradas**: tipografía legible de `24 px` – `26 px`, peso semibold/bold, color contrastado (vinotinto o rojo carmesí), separadas por una línea sutil de 1 px y con suficiente holgura vertical para funcionar como el remate visual y conceptual del bloque.

6. **Brevedad Telegráfica Estricta en Viñetas (Ancla Visual para el Ponente):**
   - Cada viñeta debe ser una sentencia corta o etiqueta conceptual + cifra (entre 3 y 6 palabras por viñeta).
   - Las diapositivas nunca deben contener párrafos narrativos que compitan con la atención auditiva del público; el ponente narra y la diapositiva ancla la evidencia.


---

## 2. Geometría Espacial y Retícula (Canvas & Layout)

### 2.1. Dimensiones del Canvas
- **Relación de aspecto:** `16:9` panorámica estándar.
- **Resolución nativa de referencia:** `1920 px × 1080 px`.
- **Equivalencia OpenXML DrawingML:** `18,288,000 EMU × 10,287,000 EMU` (1 píxel = 9,525 EMU).
- **Modelo de escalado:** Escenario rígido de tamaño base `1920×1080` centrado en viewport con escalado proporcional mediante `transform: scale(min(scaleX, scaleY))` para asegurar paridad pixel-perfect en proyectores `1080p`, pantallas `4K` y laptops `1366×768`.

### 2.2. Zonas Maestras y Ejes de Alineación
Todas las diapositivas claras (Slides 2 a 11) comparten una estructura espacial milimétrica:

```
Y = 0px    ┌──────────────────────────────────────────────────────────────────┐
           │ Barra de estado / progreso (opcional web)                        │
Y = 64px   │  [■] 05 · REFERENCIAS · APA VII                    #LoxTIC       │  <- HEADER (Alto: ~80px)
Y = 152px  │──────────────────────────────────────────────────────────────────│  <- REGLA VINOTINTO (Grosor: 2px)
           │                                                                  │
           │                                                                  │
           │                       ÁREA DE CONTENIDO                          │
           │                       (Alto útil: 760px)                         │
           │                                                                  │
           │                                                                  │
Y = 972px  │──────────────────────────────────────────────────────────────────│  <- REGLA INFERIOR (Grosor: 1px)
Y = 997px  │  VI CONGRESO · 2026                           LOHACEMOSXTIC.COM  │  <- FOOTER (Alto: ~40px)
Y = 1080px └──────────────────────────────────────────────────────────────────┘
           ^                                                                  ^
       X = 110px                                                          X = 1810px
       (Margen izq: 5.73%)                                                (Margen der: 5.73%)
```

### 2.3. Coordenadas Notables del Sistema

| Elemento Maestro | Eje X (Izquierda) | Eje Y (Superior) | Ancho | Alto | Propósito |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Margen Exterior Izquierdo** | `110 px` (5.73%) | — | — | — | Eje de referencia de todos los títulos y bloques. |
| **Margen Exterior Derecho** | — | — | `110 px` (5.73%) | — | Límite derecho del contenido. |
| **Ancho Útil de Trabajo** | `110 px` | — | `1700 px` (88.54%) | — | Bounding box principal de la diapositiva. |
| **Barra roja de categoría** | `110 px` | `75 px` | `6 px` | `44 px` | Indicador visual de jerarquía en cabecera. |
| **Texto de categoría superior**| `138 px` | `84 px` | Auto | `31 px` | Etiqueta temática en Courier New. |
| **Logotipo `#LoxTIC` (Cabecera)** | `1664 px` | `64 px` | `146 px` | `66 px` | Identificador de marca del congreso. |
| **Línea Divisoria de Cabecera** | `110 px` | `152 px` | `1700 px` | `2 px` | Separador vinotinto institucional (`#460811`). |
| **Línea Divisoria de Pie** | `110 px` | `972 px` | `1700 px` | `1 px` | Separador sutil grisáceo (`#E4DADB`). |
| **Texto de Pie Izquierdo** | `110 px` | `997 px` | Auto | `35 px` | Metadato de sede/año (`VI CONGRESO · 2026`). |
| **Texto de Pie Derecho** | `1538 px` | `999 px` | Auto | `31 px` | Enlace institucional (`LOHACEMOSXTIC.COM`). |

---

## 3. Tokens de Color y Sistema Cromático

La paleta está extraída directamente de las definiciones de color RGB del paquete OpenXML de la plantilla. Utiliza contrastes altos aptos para auditorios iluminados o proyectores de baja luminosidad.

### 3.1. Tabla de Tokens Cromáticos Oficiales

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                             PALETA INSTITUCIONAL                            │
├───────────────┬──────────────┬─────────────┬────────────────────────────────┤
│ Variable CSS  │ Valor Hex    │ Muestra     │ Rol Semántico                  │
├───────────────┼──────────────┼─────────────┼────────────────────────────────┤
│ --c-wine-dark │ #32060D      │ [█████████] │ Fondo Portada (Slide 1) y      │
│               │              │             │ Separador (Slide 4).           │
├───────────────┼──────────────┼─────────────┼────────────────────────────────┤
│ --c-wine-prim │ #460811      │ [█████████] │ Encabezados de tabla, reglas   │
│               │              │             │ principales, marca de pie dir. │
├───────────────┼──────────────┼─────────────┼────────────────────────────────┤
│ --c-text-dark │ #2C0509      │ [█████████] │ Títulos principales H1/H2 en   │
│               │              │             │ diapositivas claras (alto C).   │
├───────────────┼──────────────┼─────────────┼────────────────────────────────┤
│ --c-red-accent│ #C9101B      │ [█████████] │ Píldora de cabecera, números   │
│               │              │             │ de contenido, viñetas, botones.│
├───────────────┼──────────────┼─────────────┼────────────────────────────────┤
│ --c-red-dark  │ #C00D1A      │ [█████████] │ Énfasis inline ("Palabras cl.")│
├───────────────┼──────────────┼─────────────┼────────────────────────────────┤
│ --c-gold      │ #F5C21B      │ [█████████] │ Insignias técnicas monoespacio,│
│               │              │             │ numeral 01 hero, barra métrica.│
├───────────────┼──────────────┼─────────────┼────────────────────────────────┤
│ --c-pink-bg   │ #FAF5F5      │ [█████████] │ Superficies de tarjetas, cajas │
│               │              │             │ metodológicas, filas alternas. │
├───────────────┼──────────────┼─────────────┼────────────────────────────────┤
│ --c-gray-text │ #5D4A4D      │ [█████████] │ Cuerpo de texto, párrafos,     │
│               │              │             │ referencias bibliográficas.    │
├───────────────┼──────────────┼─────────────┼────────────────────────────────┤
│ --c-gray-clos │ #7C6A6D      │ [█████████] │ Metadatos de fecha, autores en │
│               │              │             │ cierre, descripciones en agenda│
├───────────────┼──────────────┼─────────────┼────────────────────────────────┤
│ --c-gray-head │ #A08D90      │ [█████████] │ Categorías superiores en mono, │
│               │              │             │ metadatos de pie izquierdo.    │
├───────────────┼──────────────┼─────────────┼────────────────────────────────┤
│ --c-gray-mute │ #8D7A7D      │ [█████████] │ Avisos de pie, notas de anexos │
├───────────────┼──────────────┼─────────────┼────────────────────────────────┤
│ --c-line-rule │ #E4DADB      │ [█████████] │ Línea divisoria de pie.        │
├───────────────┼──────────────┼─────────────┼────────────────────────────────┤
│ --c-border-sub│ #EAE0E1      │ [█████████] │ Borde inferior de tabla.       │
├───────────────┼──────────────┼─────────────┼────────────────────────────────┤
│ --c-dashed    │ #D8CDCF      │ [█████████] │ Borde discontinuo de figuras.  │
├───────────────┼──────────────┼─────────────┼────────────────────────────────┤
│ --c-white     │ #FFFFFF      │ [█████████] │ Fondo de diapositiva estándar. │
└───────────────┴──────────────┴─────────────┴────────────────────────────────┘
```

### 3.2. Reglas de Contraste y Accesibilidad
- **Fondos oscuros (`#32060D`):** El texto debe ser exclusivamente `#FFFFFF` (títulos y autores) o `#F5C21B` (etiquetas doradas monoespacio).
- **Fondos claros (`#FFFFFF` y `#FAF5F5`):** 
  - Los títulos van en `#2C0509` (relación de contraste superior a `14:1`).
  - El texto de lectura va en `#5D4A4D` (relación de contraste superior a `7.5:1`).
  - El texto secundario/monoespaciado va en `#7C6A6D` o `#A08D90` (superior a `4.5:1` en tamaños de 18pt o superiores).

---

## 4. Sistema Tipográfico Dual (Typography System)

El diseño opera exclusivamente con dos familias tipográficas estándar: **Arial** y **Courier New**. No se utilizan fuentes de terceros ni variables externas para garantizar una reproducción exacta y compatible en cualquier sistema operativo sin fallos de carga o sustitución de glifos.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                           DUALIDAD TIPOGRÁFICA                              │
├──────────────────────────────────────┬──────────────────────────────────────┤
│ Arial (Sans-Serif Humanista)         │ Courier New (Monospace Mecánico)     │
│ • Títulos de diapositiva y portada   │ • Números de sección (01, 02, etc.)  │
│ • Cuerpo de texto y entradillas      │ • Categorías en cabecera de página   │
│ • Filas de tabla y leyendas de figura│ • Metadatos de pie de página y fechas │
│ • Referencias bibliográficas APA VII │ • Encabezados de tabla de datos      │
│ • Coautores y filiaciones            │ • Insignias técnicas y URLs          │
└──────────────────────────────────────┴──────────────────────────────────────┘
```

### 4.1. Escala Tipográfica Normalizada para Auditorio (1920 × 1080 px)

En auditorios y salas de conferencias, el público se ubica a distancias de 10 a 30 metros de la pantalla de proyección. La escala tipográfica está calibrada con el estándar de alta legibilidad para evitar texto diminuto:

| Nivel / Rol | Familia | Tamaño PPTX | Tamaño CSS | Peso | Interlineado | Tracking | Color |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Hero Display (Slide 1/16)** | Arial | `66.0 pt` | `88 px` | 700 (Bold) | `1.10` | Normal | `#FFFFFF` / `#2C0509` |
| **Hero Separator (Slide 4)** | Courier New | `81.0 pt` | `108 px` | 700 (Bold) | `1.00` | Normal | `#F5C21B` |
| **Hero Separator Title** | Arial | `66.0 pt` | `88 px` | 700 (Bold) | `1.10` | Normal | `#FFFFFF` |
| **Page Title H2 (Standard)** | Arial | `48.0 pt` | `64 px` | 700 (Bold) | `1.15` | Normal | `#2C0509` |
| **Slide 2 Title (Resumen)** | Courier New | `40.5 pt` | `54 px` | 700 (Bold) | `1.10` | `1.5 px` | `#460811` |
| **Section Title (Cards/Agenda)**| Arial | `30.0 pt` | `40 px` – `42 px` | 700 (Bold) | `1.20` | Normal | `#2C0509` |
| **Agenda Number Badge** | Courier New | `31.5 pt` | `42 px` | 700 (Bold) | `1.00` | Normal | `#C9101B` |
| **Header Category Badge** | Courier New | `21.0 pt` | `28 px` | 700 (Bold) | `1.00` | `2 px` | `#A08D90` |
| **Body Lead (Entradilla)** | Arial | `27.0 pt` | `36 px` | 400 (Regular)| `1.55` | Normal | `#5D4A4D` |
| **Body Standard (Párrafos/Bullets)**| Arial | `24.0 pt` | `32 px` | 400 (Regular)| `1.50` | Normal | `#2C0509` / `#5D4A4D` |
| **KPI Big Number (Slide 10/12)**| Arial / Mono | `70.5 pt` | `94 px` | 700 (Bold) | `1.00` | Normal | `#460811` |
| **Table Header Cells** | Courier New | `21.0 pt` | `28 px` | 700 (Bold) | `1.00` | `2 px` | `#FFFFFF` |
| **Table Data Cells** | Arial | `21.0 pt` | `28 px` | 400 (Regular)| `1.35` | Normal | `#5D4A4D` |
| **Code Viewer (Slide 12)** | Courier New | `19.5 pt` | `26 px` | 400/700 | `1.60` | Normal | `#FCE8EB` |
| **Math Box (Slide 14)** | Courier New | `22.5 pt` | `30 px` | 700 (Bold) | `1.45` | Normal | `#32060D` |
| **Footer Metadata** | Courier New | `18.0 pt` | `24 px` | 400/700 | `1.00` | `1.5 px` | `#A08D90` / `#460811` |
| **Footnote / Badge Meta** | Arial / Mono | `18.0 pt` | `24 px` | 400/700 | `1.30` | Normal | `#8D7A7D` |

---

## 5. Componentes Maestros y Patrones de Interfaz

### 5.1. Cabecera Institucional Estándar (`.slide-header`)
Utilizada en todas las diapositivas con fondo blanco (Slides 2, 3, 5 a 15).
- **Indicador vertical:** Rectángulo rojo plano (`#C9101B`) de `5 px` de ancho por `36 px` de alto.
- **Texto de categoría:** `Courier New`, `28 px`, `font-weight: 700`, `letter-spacing: 2px`, en mayúsculas sostenidas, color `#A08D90`.
- **Logotipo de evento:** Imagen institucional `#LoxTIC` vinotinto (`#460811`), altura `54 px`, alineada a la derecha.
- **Línea divisoria:** Regla horizontal continua de `2 px` de grosor, color `#460811`, ubicada en `Y = 152 px`.

```
[ | ] 01 · INTRODUCCIÓN                                                 #LoxTIC
───────────────────────────────────────────────────────────────────────────────
```

### 5.2. Pie de Página Institucional (`.slide-footer`)
- **Regla superior:** Línea sutil gris (`#E4DADB`) de `1 px` de grosor en `Y = 972 px`.
- **Lado izquierdo:** `VI CONGRESO · 2026` o `CARTAGENA · 28–30 OCT 2026` en `Courier New`, `24 px`, color `#A08D90`.
- **Lado derecho:** `LOHACEMOSXTIC.COM` en `Courier New`, `24 px`, negrita, color `#460811`.

```
───────────────────────────────────────────────────────────────────────────────
VI CONGRESO · 2026                                            LOHACEMOSXTIC.COM
```

### 5.3. Bloque de Lista con Viñetas Circulares (`.s5-bullets-list`)
- **Marcador:** Círculo geométrico de `12 px × 12 px`, color `#C9101B`, alineado con la primera línea de texto.
- **Espaciado:** Distancia de `24 px` entre viñeta y texto; separación vertical de `32 px` entre ítems.
- **Texto:** `Arial`, `32 px`, color `#2C0509`.

```
  ●  Contexto y antecedentes: qué se sabe hasta ahora.
  ●  Vacío o problema identificado en la literatura.
  ●  Objetivo general y pregunta de investigación.
```

### 5.4. Bloques Metodológicos Comparativos (`.s6-block`)
- **Superficie:** Rectángulo plano de `822 px × 262 px` con fondo rosado pálido `#FAF5F5`. **Sin bordes redondeados** (`border-radius: 0px`).
- **Barra de acento superior:** Línea sólida de `6 px` de alto en el borde superior:
  - Bloque 1 (Diseño): Vinotinto `#460811`.
  - Bloque 2 (Muestra): Rojo carmesí `#C9101B`.
- **Etiqueta temática:** `Courier New`, `26 px`, negrita, color `#C00D1A`.
- **Título interior:** `Arial`, `40 px`, negrita, color `#2C0509`.
- **Texto descriptivo:** `Arial`, `28 px`, color `#5D4A4D`.

```
┌────────────────────────────────────────┐ ┌────────────────────────────────────────┐
│[Barra vinotinto 5px #460811]           │ │[Barra roja 5px #C9101B]                │
│                                        │ │                                        │
│  DISEÑO                                │ │  MUESTRA E INSTRUMENTOS                │
│  Tipo de estudio                       │ │  Participantes y técnicas              │
│  Enfoque, alcance y periodo...         │ │  Población, criterios de selección...  │
└────────────────────────────────────────┘ └────────────────────────────────────────┘
```

### 5.5. Tabla de Datos Científica (`.s7-native-table`)
- **Títulos bilingües:**
  - Título en español: `Arial Bold`, `32 px`, color `#2C0509` (`Tabla 1. Título de la tabla.`).
  - Título en inglés: `Arial Italic`, `24 px`, color `#7C6A6D` (`Table 1. Título de la tabla en inglés`).
- **Encabezado de tabla:** 
  - Fondo sólido vinotinto institucional `#460811`.
  - Texto centrado en `Courier New Bold`, `20 px`, color `#FFFFFF`, `letter-spacing: 1.5px`.
  - Padding: `16 px` vertical.
- **Filas de datos:**
  - Fila 1 y 3: Fondo blanco `#FFFFFF`.
  - Fila 2: Fondo rosado suave `#FAF5F5`.
  - Borde divisorio entre celdas: `1 px solid #EAE0E1`.
  - Celda de variable (columna 1): `Arial Bold`, `22 px`, color `#2C0509`.
  - Celdas de datos: `Arial Regular`, `22 px`, color `#5D4A4D`.
- **Borde de cierre inferior:** Línea gruesa de `3 px solid #460811`.
- **Nota metodológica al pie:** `Arial Regular`, `20 px`, color `#7C6A6D` (`Fuente: elaboración propia...`).

### 5.6. Bloque de Métricas y Hallazgos (`.s8-metric-item`)
- **Barra vertical de color:** `5 px` de ancho por `99 px` de alto.
  - Métrica 1: Vinotinto `#460811`.
  - Métrica 2: Rojo `#C9101B`.
  - Métrica 3: Dorado `#F5C21B`.
- **Valor numérico (KPI):** `Arial Bold`, `52 px`, color `#2C0509`.
- **Etiqueta descriptiva:** `Arial Regular`, `24 px`, color `#5D4A4D`.

```
  │ 00%
  │ Lectura del primer resultado.
  
  │ 0,00
  │ Lectura del segundo resultado.
  
  │ n = 00
  │ Tamaño de la muestra analizada.
```

### 5.7. Contenedor de Figura Científica (`.s8-figure-container`)
- **Dimensiones:** `913 px` de ancho por `524 px` de alto.
- **Borde:** `2 px dashed #D8CDCF` (trazo discontinuo).
- **Fondo:** `#FAF5F5` uniforme.
- **Placeholder central:** `Courier New`, `22 px`, color `#8D7A7D`, `letter-spacing: 2px`.
- **Epígrafe inferior:** Alineado al margen izquierdo de la figura (`110 px`), título en español (`Arial Bold`, `26 px`) y título en inglés en cursiva (`Arial Italic`, `22 px`).

### 5.8. Franja de Agradecimientos e Instituciones (`.s9-ack-banner`)
- **Dimensiones:** Ancho completo de trabajo (`1700 px`), alto `84 px`.
- **Fondo:** `#FAF5F5` continuo.
- **Acento lateral:** Barra vertical roja de `5 px` en `#C9101B`.
- **Tipografía:** `Arial`, `22 px`, con título `Agradecimientos:` en negrita vinotinto `#460811` y texto en `#5D4A4D`.

---

## 6. Arquetipos de Diapositiva (Slide Archetypes)

El mazo de diapositivas consta de 11 pantallas agrupadas en 6 patrones arquitectónicos:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                           CATÁLOGO DE ARQUETIPOS                            │
├────────────┬─────────────────────────────┬──────────────────────────────────┤
│ Tipo       │ Diapositivas                │ Características Clave            │
├────────────┼─────────────────────────────┼──────────────────────────────────┤
│ Arquetipo A│ Slide 1 (Portada Principal) │ Fondo vinotinto #32060D,         │
│ Hero Dark  │ Slide 4 (Separador Sección) │ silueta de Cartagena, dorado     │
│            │                             │ #F5C21B y logotipos blancos.     │
├────────────┼─────────────────────────────┼──────────────────────────────────┤
│ Arquetipo B│ Slide 3 (Agenda/Contenido)  │ Lista pura en 2 columnas,        │
│ Editorial  │ Slide 10 (Referencias APA)  │ números en Courier New rojo,     │
│ List       │                             │ sin tarjetas, indentación limpia.│
├────────────┼─────────────────────────────┼──────────────────────────────────┤
│ Arquetipo C│ Slide 2 (Resumen Ejecutivo) │ Título central, entradilla larga │
│ Single Lead│ Slide 5 (Planteamiento)     │ en bloque continuo y viñetas     │
│            │                             │ cuadradas rojas.                 │
├────────────┼─────────────────────────────┼──────────────────────────────────┤
│ Arquetipo D│ Slide 6 (Metodología 2 col) │ Tarjetas de superficie #FAF5F5   │
│ Split Box  │ Slide 9 (Discusión 3 col)   │ con barras superiores temáticas  │
│            │                             │ y títulos jerárquicos.           │
├────────────┼─────────────────────────────┼──────────────────────────────────┤
│ Arquetipo E│ Slide 7 (Tabla de Datos)    │ Datos tabulares formales con     │
│ Scientific │ Slide 8 (Figura + Métricas) │ filas alternas o división visual │
│ Evidence   │                             │ figura/KPIs.                     │
├────────────┼─────────────────────────────┼──────────────────────────────────┤
│ Arquetipo F│ Slide 11 (Cierre institucional│ Encabezado invertido, botón    │
│ Closing    │                            │ PREGUNTAS, QR escaneable limpio │
│            │                             │ y triada de logos a color.       │
└────────────┴─────────────────────────────┴──────────────────────────────────┘
```

---

## 7. Inventario de Activos Multimedia Nativos (`assets/`)

Todos los archivos gráficos son nativos, extraídos del paquete OpenXML original:

| Archivo | Formato | Dimensiones | Función en el Sistema de Diseño |
| :--- | :--- | :--- | :--- |
| [`image1.png`](file:///c:/Users/ASUS/Desktop/Diapositivas-Cartagena/assets/image1.png) | PNG Transparente | Vectorial | Ilustración lineal blanca de la Torre del Reloj de Cartagena. Usada con opacidad atenuada (18%) como marca de agua en Portada (Slide 1) y en trío inferior en Separador (Slide 4). |
| [`image2.png`](file:///c:/Users/ASUS/Desktop/Diapositivas-Cartagena/assets/image2.png) | PNG Transparente | 290×131 px | Logotipo oficial `#LoxTIC` en blanco puro para fondos oscuros (Slide 1). |
| [`image3.png`](file:///c:/Users/ASUS/Desktop/Diapositivas-Cartagena/assets/image3.png) | PNG Transparente | 284×97 px | Escudo oficial de la Universidad Distrital Francisco José de Caldas (versión monocromática blanca, Slide 1). |
| [`image4.png`](file:///c:/Users/ASUS/Desktop/Diapositivas-Cartagena/assets/image4.png) | PNG Transparente | 255×70 px | Logotipo oficial de la Universidad Tecnológica de Bolívar - UTB (versión blanca, Slide 1). |
| [`image5.png`](file:///c:/Users/ASUS/Desktop/Diapositivas-Cartagena/assets/image5.png) | PNG Transparente | 218×97 px | Escudo oficial de la Universidad de Cartagena (versión blanca, Slide 1). |
| [`image6.png`](file:///c:/Users/ASUS/Desktop/Diapositivas-Cartagena/assets/image6.png) | PNG Transparente | 172×78 px | Logotipo oficial `#LoxTIC` en vinotinto institucional `#460811` para cabecera de todas las diapositivas claras (Slides 2 a 11). |
| [`image7.png`](file:///c:/Users/ASUS/Desktop/Diapositivas-Cartagena/assets/image7.png) | PNG Transparente | 299×318 px | Código QR oficial del artículo recortado limpiamente sin bordes rojos externos (`<a:srcRect>`), enlaza a `LOHACEMOSXTIC.COM` (Slide 11). |
| [`image8.png`](file:///c:/Users/ASUS/Desktop/Diapositivas-Cartagena/assets/image8.png) | PNG Transparente | 127×46 px | Escudo Universidad Distrital a color institucional en pie de cierre (Slide 11, posición 1). |
| [`image9.png`](file:///c:/Users/ASUS/Desktop/Diapositivas-Cartagena/assets/image9.png) | PNG Transparente | 94×46 px | Logotipo UTB azul oficial en pie de cierre (Slide 11, posición 2). |
| [`image10.png`](file:///c:/Users/ASUS/Desktop/Diapositivas-Cartagena/assets/image10.png)| PNG Transparente | 95×46 px | Escudo Universidad de Cartagena a todo color en pie de cierre (Slide 11, posición 3). |

---

## 8. Reglas de Implementación en Código Web

### 8.1. Declaración de Variables Globales CSS (`:root`)
Para replicar o extender este sistema de diseño en nuevas diapositivas o interfaces, deben utilizarse las variables oficiales:

```css
:root {
  /* Paleta cromática oficial */
  --c-wine-dark: #32060D;
  --c-wine-primary: #460811;
  --c-text-dark: #2C0509;
  --c-red-accent: #C9101B;
  --c-red-dark: #C00D1A;
  --c-gold: #F5C21B;
  --c-pink-bg: #FAF5F5;
  --c-border-subtle: #EAE0E1;
  --c-line-rule: #E4DADB;
  --c-dashed: #D8CDCF;
  --c-gray-text: #5D4A4D;
  --c-gray-muted: #8D7A7D;
  --c-gray-header: #A08D90;
  --c-gray-closing: #7C6A6D;
  --c-white: #FFFFFF;

  /* Fuentes del sistema nativo */
  --font-sans: Arial, Helvetica, -apple-system, sans-serif;
  --font-mono: "Courier New", Courier, monospace;

  /* Parámetros de canvas 16:9 */
  --canvas-w: 1920px;
  --canvas-h: 1080px;
  --margin-x: 110px; /* 5.73% */
  --content-w: 1700px; /* 88.54% */
}
```

### 8.2. Reglas Prohibitivas del Sistema (Anti-Patrones)
1. **Prohibido el uso de bordes redondeados (`border-radius > 0`)** en tarjetas de contenido, tablas o cajas métricas. El diseño es 100% cartesiano y formal.
2. **Prohibido el uso de sombras proyectadas (`box-shadow`)** en los elementos internos de las diapositivas. Las únicas sombras permitidas son las del marco exterior del viewport de presentación.
3. **Prohibido el uso de gradientes en fondos de contenido.** Solo se permiten colores planos (`#FFFFFF`, `#FAF5F5`, `#32060D`).
4. **Prohibido agregar sangría francesa** en listas bibliográficas a menos que el original PPTX la contemple de manera explícita.
5. **Prohibido sustituir `Courier New` por fuentes monoespaciadas modernas** (como Fira Code o JetBrains Mono); la identidad de LHXT26 se basa en el carácter tipográfico de máquina de escribir clásica de `Courier New`.

---

*Documento consolidado para el repositorio de diapositivas interactivas del VI Congreso Internacional de Investigación Interdisciplinar (LHXT26 - Cartagena 2026).*
