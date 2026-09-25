# Bitácora de Decisiones de Diseño y Contenido

Este documento registra los acuerdos, descartes y justificaciones técnicas/editoriales tomadas durante la construcción de la presentación oficial para el **VI Congreso Internacional de Investigación Interdisciplinar (Cartagena 2026)** slide por slide. 

Para consultar el manifiesto y marco transversal de diseño, ver: [PRINCIPIOS_DISENO_GLOBALES.md](file:///c:/Users/ASUS/Desktop/Diapositivas-Cartagena/docs/PRINCIPIOS_DISENO_GLOBALES.md).

---

## Slide 01: Portada Oficial (Hero Dark)

* **Archivo fuente**: `slides/slide_01.html`
* **Compilado en**: `index.html` (`#slide-1`)
* **Arquetipo**: Portada institucional sobre fondo oscuro vino tinto con marca de agua de la Torre del Reloj de Cartagena.
* **Propósito en ponencia**: Apertura y presentación formal de ponentes e institución.

### Formato Panorámico en 2 Líneas (Mayor Amplitud Horizontal)
* **Amplitud horizontal del bloque (`.s1-title-block`)**: Se amplió a `max-width: 1580px` para aprovechar el ancho 16:9, reduciendo drásticamente la altura vertical del bloque de texto.
* **Título principal en 2 líneas (`.s1-main-title`)**: Fijado en **`56px`** extra-bold (`800`) con `line-height: 1.18`. Ahora se distribuye de manera horizontal en solo 2 líneas en vez de 3:
  * *Línea 1*: Selección de modelos compactos para tutoría de
  * *Línea 2*: inglés mediante un benchmark RAG sin conexión
* **Subtítulo en inglés en 1 sola línea (`.s1-sub-title`)**: **`32px`** cursiva.
* **Autores en 1 sola línea (`.s1-authors-list`)**: **`26px`** blanco nítido.
* **Filiación en 1 sola línea (`.s1-affiliation`)**: **`22px`** dorado.

---

## Slide 02: Resumen Ejecutivo (Executive Hook)

* **Archivo fuente**: `slides/slide_02.html`
* **Compilado en**: `index.html` (`#slide-2`)
* **Arquetipo**: Filas editoriales con acentos cromáticos laterales (Opción B seleccionada).
* **Propósito en ponencia**: Primer contacto sustancial con la audiencia (30 a 45 segundos). Plantear el conflicto (exclusión), la solución técnica (RAG local) y el hallazgo contraintuitivo (falso empate), sin sobrecargar con detalles que pertenecen a las secciones posteriores.

---

### 1. Estructura y Distribución Visual (Layout)
* **Patrón de 3 filas horizontales independientes**: Se descartó la versión saturada original (que mezclaba especificaciones de hardware, gráficas y métricas) y el tríptico de 3 columnas estrechas.
* **Contenedores diferenciados**: Cada fila utiliza un fondo neutro cálido (`#FAF5F5`) con un borde lateral izquierdo de `8px` que asigna código de color semántico a cada idea:
  * **Fila 1 (Problema)**: Vino tinto institucional (`#6B1D2F` / `var(--c-wine-primary)`).
  * **Fila 2 (Solución / Propuesta)**: Rojo tecnológico de acción (`#C92A2A` / `var(--c-red-accent)`).
  * **Fila 3 (Hallazgo crítico)**: Dorado / Ámbar de advertencia (`#9A7200` / `var(--c-gold)`).

---

### 2. Principio de Proyección para Auditorio (Eliminación de Microtextos)
* **Regla de legibilidad a distancia (10–20 metros)**: Ningún texto debe ser inferior a `24px`. Los textos de 16–20 px se convierten en manchas borrosas en el proyector y compiten con la voz del ponente.
* **Elementos eliminados**:
  * **Subetiquetas bajo los números**: Se eliminaron *"Sin internet rural"*, *"Offline en USB"* y *"Falso empate"*.
  * **Prefijos de índice mono**: Se eliminaron *"01 · PROBLEMA"*, *"02 · PROPUESTA"* y *"03 · HALLAZGO"*.
  * **Barra inferior de nota al pie**: Se retiró el cintillo *"Propósito de la ponencia..."*, permitiendo que el slide respire con márgenes amplios y limpios.

---

### 3. Escala Tipográfica Definitiva
* **Pregunta de cabecera (`h2.s-lead-question`)**: Aumentada a **`46px`** bold (`line-height: 1.25`) para proyectar autoridad y legibilidad desde el fondo del auditorio.
* **Cifras de impacto**: `68px` con peso `800` (extra-bold), centradas en su columna.
* **Títulos de concepto (`h3`)**: `32px` bold en color oscuro de alto contraste (`#1A1A1A`).
* **Cuerpo explicativo (`p`)**: `26px` con interlineado `1.45`, limitado estrictamente a 2 líneas concisas.
* **Negritas de escaneo rápido**: Se aplicaron `<strong>` selectivos para que la audiencia capte las ideas clave en 1 segundo:
  * Fila 1: *conectividad y pagos en dólares*, *más de la mitad*.
  * Fila 2: *SLM*, *memoria USB en CPU de aula*.
  * Fila 3: *conductas opuestas*, *no pedagogía*.

---

### 4. Precisión Geométrica (Alineación Pixel-Perfect de Divisores)
* **Problema detectado**: Había un desfase de `22.6px` en la línea divisoria vertical de la Fila 1 respecto a las Filas 2 y 3, debido a que `min-width: 190px` se expandía de forma desigual con el ancho de caracteres de `"58.6%"` frente a `"100%"`.
* **Solución aplicada**: Se estandarizó el ancho del contenedor numérico a un valor fijo de `flex: 0 0 260px; width: 260px; text-align: center;` en las tres filas.
* **Resultado**: Las tres líneas divisorias verticales (`2px` de grosor, color sutil) quedan alineadas a la misma coordenada horizontal exacta (**`X = 453.4375 px`**), logrando una línea vertical continua y matemáticamente armónica.

---

## Slide 03: Estructura de la Ponencia (Roadmap / Agenda)

* **Archivo fuente**: `slides/slide_03.html`
* **Compilado en**: `index.html` (`#slide-3`)
* **Arquetipo**: Roadmap horizontal de 4 columnas (Opción C, Variante C1 Ultra-Minimalista seleccionada).
* **Propósito en ponencia**: Presentar la hoja de ruta de la exposición en menos de 20 segundos. Anticipar los 4 momentos clave del relato investigativo sin adelantar métricas ni saturar la pantalla.

---

### 1. Enfoque Temático (Alineación con los 4 Separadores)
* **Descarte de secciones de relleno**: Se eliminaron definitivamente *"05 Agradecimientos"* y *"06 Referencias"* de la agenda, ya que en una ponencia académica estas no constituyen momentos expositivos de la agenda.
* **Los 4 Momentos Reales**:
  * `01` · **Contexto y Problema Rural** (coincide con Slide 4 y 5).
  * `02` · **Metodología y Pipeline RAG** (coincide con Slide 6 a 9).
  * `03` · **Resultados y Hallazgos** (coincide con Slide 10 a 14).
  * `04` · **Conclusiones y Recomendaciones** (coincide con Slide 15 a 17).

---

### 2. Eliminación de Textos Pretenciosos y Redundantes
* **Título claro y contundente**: Se reemplazó el título rebuscado *"Cuatro momentos para desmontar la evaluación de la IA educativa local"* por el directo y académico **"Ruta de la Presentación"**, escalado a **`48px`** bold para dominar con autoridad la diapositiva.
* **Cero texto secundario / microtextos**: Se eliminaron las frases pequeñas bajo cada columna y la repetición de estadísticas ya mencionadas en el Slide 2 (58.6%, 14 preguntas, 0.795).
* **Protagonismo del ponente**: Al dejar únicamente el número gigante y el título conceptual, la diapositiva sirve como guía visual limpia mientras el ponente introduce oralmente cada sección.

---

### 3. Distribución y Jerarquía Visual
* **4 tarjetas verticales esbeltas**: Distribuidas horizontalmente (`display: flex; gap: 28px;`) con fondo `#FAF5F5` y borde superior de `8px` con código cromático progresivo:
  * Paso 01: Vino institucional (`#6B1D2F`).
  * Paso 02: Vino medio (`#8B263E`).
  * Paso 03: Rojo de alerta / hallazgo (`#C92A2A`).
  * Paso 04: Dorado de cierre institucional (`#9A7200`).
* **Números de fase**: `76px` ultra-negrita (`font-weight: 800`).
* **Línea de acento interna**: `48px × 4px` del mismo color de la fase.
* **Títulos de sección**: `32px` bold en color oscuro (`#1A1A1A`), centrados verticalmente en la tarjeta.

---

## Slide 04: Separador 01 - Contexto y Problema Rural (Hero Dark + GPS)

* **Archivo fuente**: `slides/slide_04.html`
* **Compilado en**: `index.html` (`#slide-4`)
* **Arquetipo**: Separador de capítulo con indicador de ruta / stepper horizontal (Opción C seleccionada).
* **Propósito en ponencia**: Transición de 5 a 10 segundos para introducir el Bloque 1 de la investigación.

### Decisiones de Diseño y Contenido
* **Coherencia con la Ruta**: Se renombró de *"Introduccion"* (sin tilde) a **"Contexto y Problema Rural"**, alineado al 100% con el nombre de la etapa fijado en el Slide 3.
* **Eliminación de párrafos pretenciosos**: Se sustituyó el texto largo por una frase simple, directa y cercana: *"Brecha de conectividad y necesidad de tutoría local sin internet."*
* **Stepper / Indicador de Progreso Horizontal**: Se incorporó una barra inferior fija con los 4 bloques temáticos. La fase actual se destaca con una línea superior dorada y tipografía en blanco nítido, sin etiquetas redundantes como "ACTIVO" (el código cromático ya comunica el estado de forma visual e intuitiva). Este patrón sirve como GPS visual para los separadores posteriores (Slides 6, 10 y 15).
* **Identidad Institucional**: Se conservó la silueta tenue de la Torre de Cartagena a la derecha para mantener consistencia con la portada.

---

## Slide 05: 01 · Contexto y Problema Rural (Tríptico Limpio B3-L1)

* **Archivo fuente**: `slides/slide_05.html`
* **Compilado en**: `index.html` (`#slide-5`)
* **Arquetipo**: Tríptico de 3 columnas verticales de altura natural y centrada (Variante B3-L1 seleccionada).
* **Propósito en ponencia**: Plantear el punto de partida de la investigación (la brecha de conectividad rural) y formular de inmediato las dos preguntas de investigación que guiaron el benchmark experimental.

### Decisiones de Diseño y Contenido
* **Eliminación de "Cuadros dentro de cuadros"**: Se descartó la versión previa que contenía cajas blancas anidadas dentro de cada columna y una barra inferior flotante. Cada columna es ahora un bloque continuo limpio (`#FAF5F5`) con un borde superior distintivo de `8px`.
* **Eliminación de textos residuales de bajo contraste**: Se retiraron los párrafos secundarios en gris al pie de cada tarjeta (*"Las APIs en la nube son inviables..."*, etc.), que resultaban redundantes y competían con la explicación oral del ponente.
* **Escala Tipográfica de Alto Impacto para Auditorio**:
  * Título de cabecera (`.s-lead-question`): **`46px`** bold (*"De la brecha de conectividad a las preguntas que guiaron el benchmark"*).
  * Etiquetas de fase: **`20px`** monospace (`01 · LA REALIDAD`, `02 · PREGUNTA 1`, `03 · PREGUNTA 2`).
  * Títulos de concepto: **`34px`** bold (`Brecha Rural`, `Elección de Modelo`, `Auditoría de Calidad`).
  * Cifras/Palabras de impacto: **`72px`** extra-bold (`58.6%`, `SLM`, `Offline`).
  * Cuerpo esencial: **`28px`** (`line-height: 1.45`) con negritas selectivas, legible con total nitidez a 20 metros.
* **Corrección de ortografía y tono**: Se fijaron todas las tildes faltantes y se erradicaron términos pretenciosos como *"monopolio de nube"* o *"la brecha invisible"*.

---

## Slide 06: Separador 02 - Metodología y Pipeline RAG (Hero Dark + GPS)

* **Archivo fuente**: `slides/slide_06.html`
* **Compilado en**: `index.html` (`#slide-6`)
* **Arquetipo**: Separador de capítulo con indicador de ruta / stepper horizontal (continuidad exacta con Slide 4).
* **Propósito en ponencia**: Transición de 5 a 10 segundos para dar inicio al Bloque 2 (Metodología técnica).

### Decisiones de Diseño y Contenido
* **Coherencia con la Ruta**: Se tituló **"Metodología y Pipeline RAG"** (`74px` extra-bold), con ortografía impecable, idéntico a la fase 02 definida en el Slide 3.
* **Subtítulo conciso y humilde**: *"Arquitectura local, pipeline híbrido y protocolo de evaluación ciega."* (`30px`), eliminando descripciones extensas innecesarias.
* **Stepper / GPS Visual**: Se activó la etapa `02` con acento dorado brillante (`var(--c-gold)`), pasando la fase `01` a estado completado/sutil y manteniendo `03` y `04` tenues en espera, sin texto redundante de estado.
* **Identidad Institucional**: Se eliminaron las 3 torres repetitivas del diseño original de plantilla y se estandarizó con la silueta tenue de la Torre de Cartagena a la derecha sobre fondo vino oscuro (`--c-wine-dark`).

---

## Slide 07: 02 · Metodología / Pipeline RAG Local (Flujo Secuencial - Opción B)

* **Archivo fuente**: `slides/slide_07.html`
* **Compilado en**: `index.html` (`#slide-7`)
* **Arquetipo**: Pipeline de flujo horizontal secuencial con flechas conectoras + franja panorámica de principio técnico (Opción B seleccionada).
* **Propósito en ponencia**: Explicar con claridad de ingeniería las 4 etapas del pipeline RAG que corre en el aula, mostrando el viaje del dato desde el libro de texto hasta la respuesta en pantalla.

### Decisiones de Diseño y Contenido
* **Diagrama de Proceso Horizontal y Flechas Iconográficas**: Las 4 etapas se conectan mediante flechas vectoriales gruesas de 44px (`stroke` / `fill` con presencia visual destacada para visibilidad a 20 metros) con transición cromática semántica:
  * Flecha 1 (Vino): hacia Paso 02.
  * Flecha 2 (Rojo): hacia Paso 03.
  * Flecha 3 (Dorado): hacia Paso 04.
* **Eliminación de "Cuadros dentro de cuadros"**: Se descartó la versión saturada de la plantilla que incluía filas de conclusión anidadas dentro de cada columna.
* **Tarjeta Panorámica de Principio Técnico con Borde Completo Equilibrado**:
  * Se eliminó el `border-left: 8px` unilateral para evitar saturar el patrón de bordes gruesos ("no abusemos de esos bordes").
  * Se aplicó un borde continuo de `2px solid var(--c-wine-primary)` que enmarca todo el recuadro de manera limpia, simétrica y formal.
  * Mantiene la cifra **100% LOCAL / USB** (`56px`), enfatizando que todo el proceso opera en la RAM de la máquina del colegio sin tocar la nube.
* **Escala Tipográfica y Contraste de Alto Impacto para Auditorio**:
  * Título de cabecera (`.s-lead-question`): **`46px`** bold (*"Flujo secuencial del pipeline RAG: de la consulta a la generación"*).
  * Etiquetas de paso: **`19px`** monospace (`PASO 01` a `PASO 04`).
  * Títulos de etapa: **`30px`** ultra-bold (`font-weight: 800`), con jerarquía visual dominante sobre el cuerpo de la tarjeta y ajustados para no romper líneas.
  * Cuerpo explicativo: **`25px`** en **negro carbón (`#110103`)** para erradicar el bajo contraste del gris anterior, con negritas y acentos cromáticos temáticos en las métricas clave (`339 trozos`, `Fusión RRF (60/40)`, `suprime el ruido`, `1.9 tok/s en CPU estándar sin GPU`).
* **Capa Visual Asimétrica: Íconos SVG y Chips Técnicos Monumentales (Variante A2-2 Aprobada)**:
  * **Ruptura de la Rigidez Ortogonal**: Para complementar la retícula sin alterar la estructura aprobada, se introdujeron sellos técnicos en ángulo (`rotate(-2.5deg)` y `rotate(3deg)`) con rotación orgánica física.
  * **Íconos Vectoriales en Cabecera**: Cada tarjeta integra un ícono SVG minimalista al lado de la etiqueta de paso: Libro curricular (Paso 1), Búsqueda densa/léxica (Paso 2), Red neuronal cross-encoder (Paso 3) y Chip CPU de silicio (Paso 4).
  * **Chips de Contenido Técnico Monumental (`14px` monoespaciado)**: En lugar de micro-adornos ilegibles, cada paso exhibe una estampa con información técnica sustancial:
    * *Paso 01*: `CORPUS · MEN (PDF)` (`rotate(-2.5deg)`, fondo vino suave).
    * *Paso 02*: `BM25 + DENSO (RRF)` (`rotate(2deg)`, fondo vino suave).
    * *Paso 03*: `CROSS-ENCODER MINILM` (`rotate(-2.5deg)`, fondo rojo suave).
    * *Paso 04*: `llama.cpp · C/C++` (`rotate(3deg)`, fondo rojo carmesí sólido con borde blanco).
  * **Sello de Portabilidad en Tarjeta Inferior**: Estampa en ángulo (`rotate(-2.5deg)`) cabalgando el borde superior de la tarjeta 100% LOCAL: `PLUG & PLAY · PORTABLE EN USB 3.0` con ícono de memoria USB.
* **Ortografía Técnica Rigurosa**: Corrección de tildes en *Metodología, híbrido, búsqueda, léxica, inferencia, ejecución*.

---

## Slide 08: 02 · Metodología / Demostración en Aula (Interfaz Local y Telemetría - Opción B)

* **Archivo fuente**: `slides/slide_08.html`
* **Compilado en**: `index.html` (`#slide-8`)
* **Arquetipo**: Layout dividido con marco de ventana para pantallazo de software + panel lateral de telemetría de 3 tarjetas (Opción B seleccionada).
* **Propósito en ponencia**: Probar la tangibilidad de la investigación mostrando la interfaz real que opera en el aula rural, sirviendo de puente directo entre la arquitectura teórica (Slide 7) y el banco experimental de pruebas (Slide 9).
* **Desplazamiento de diapositivas**: Se desplazaron en cascada las diapositivas 8 a 19 hacia 9 a 20 para albergar esta demostración sin alterar el orden temático posterior.

### Decisiones de Diseño y Contenido
* **Lienzo Hero Dark de Alto Contraste**:
  * Se configuró el fondo de la diapositiva en **vinotinto oscuro institucional (`--c-wine-dark: #32060D`)** con la marca de agua sutil de la Torre de Cartagena.
  * Este fondo oscuro actúa como marco de contraste dramático para que **la captura de pantalla (blanca/clara) y las tarjetas de telemetría (claras)** resalten de forma inmediata y nítida en proyección.
* **Columna Principal (Marco de Ventana del Software)**:
  * Contenedor con barra superior oscura de sistema (3 puntos de control, título en monospace `LoxTIC Assistant · Local SLM UI · 127.0.0.1:8000` y badge `● 100% OFFLINE`).
  * Fondo blanco interior de máxima luminosidad.
  * Soporte automático para imagen real: carga `assets/app_screenshot.png` vía `<img>`.
  * Fallback / Maqueta didáctica estructurada: mientras se agrega el archivo de imagen, despliega un flujo simulado con la consulta del estudiante, el trozo de evidencia recuperado del libro y la respuesta del modelo SLM local.
* **Columna Lateral (Panel de Telemetría de Aula - 3 Tarjetas Claras)**:
  * Diseñadas en **fondo claro (`#FAF5F5`)** con sombra sutil para flotar sobre el fondo vinotinto, respondiendo a la regla de oro de visibilidad en auditorio: *"los proyectores reproducen los textos con mucha mayor nitidez sobre fondos claros que sobre fondos oscuros"*.
  * Textos en **negro carbón profundo (`#110103`)** para contraste óptimo.
  * **Tarjeta 1 (Telemetría de Hardware)**: `1.9 tok/s en CPU Estándar` (`28px` dorado), inferencia en RAM ≤ 3.8 GB sin GPU.
  * **Tarjeta 2 (Trazabilidad Curricular)**: `Cita Pedagógica Visible` (`28px` vino), páginas y fragmentos citados con rigor pedagógico.
  * **Tarjeta 3 (Aislamiento de Red)**: `0 KB/s de Tráfico Externo` (`28px` rojo), Wi-Fi apagado y privacidad total garantizada.
* **Escala Tipográfica y Contraste**:
  * Título: `46px` extra-bold blanco nítido (`#FFFFFF`) (*"Interacción real en el aula: interfaz local y generación offline"*).
  * Etiquetas de fase: `18px` monospace en vino.
  * Titulares de métrica: `28px` extra-bold.
  * Textos descriptivos: `23px` en negro carbón (`#110103`) con negritas selectivas.
  * Cabecera y Pie de página adaptados con acentos dorados (`var(--c-gold)`).

---

## Slide 09: 02 · Metodología / Banco Curricular (Tabla Editorial Limpia - Opción A Refinada)

* **Archivo fuente**: `slides/slide_09.html`
* **Compilado en**: `index.html` (`#slide-9`)
* **Arquetipo**: Tabla editorial académica de alta legibilidad con tarjeta de balance inferior (Opción A seleccionada y refinada).
* **Propósito en ponencia**: Presentar la taxonomía del banco de pruebas (14 preguntas en total: 12 basadas estrictamente en el libro de texto oficial y 2 sondas de rechazo fuera de dominio para auditar alucinaciones).

### Decisiones de Diseño y Contenido
* **Eliminación Total de Artefactos de Paper**: Se descartaron los rótulos redundantes tipo *"Tabla 1. Cobertura curricular..."* o subtítulos en inglés, integrando toda la información en una tabla ejecutiva y moderna.
* **Corrección de Ortografía y Acentuación**: Tildes rigurosas en cabecera y contenido (*METODOLOGÍA, CÓDIGOS, PÁGINAS, PROPÓSITO PEDAGÓGICO, definición, párrafos, comprensión, información*).
* **Solución de Contraste en Columna "PÁGINAS"**:
  * Se sustituyó el gris atenuado original (`#444444` / mono regular) por **negro carbón profundo (`#110103`)** con tipografía sans-serif robusta a **`26px` bold (`font-weight: 800`)**.
  * Para la fila de sondas ("Ausente en libro"), se aplicó una insignia sutil con borde fino (`color: #900C13; background: #FFE4E6; border: 1.5px solid var(--c-red-accent); font-weight: 800; font-size: 22px;`) que no se desvanece en proyección.
* **Eliminación de Redundancia en Fila de Sondas**: Se retiró la etiqueta repetitiva `<span ...>SONDA</span>` de la primera columna, manteniendo el nombre limpio (*"Fuera de alcance"*) ya que el concepto de sonda está claramente explicado en la columna de propósito pedagógico.
* **Resumen Tipográfico Inferior Sutil (Variante A1)**:
  * En lugar de un recuadro cerrado que recargaba la diapositiva, se adoptó una **línea tipográfica abierta y equilibrada** (`26px` en vino institucional a la izquierda y `24px` con acentos en vino y rojo a la derecha).
  * Aporta respiro visual a la composición y mantiene el protagonismo en la tabla evaluativa.

---

## Slide 10: 02 · Metodología / Matriz Experimental (Diseño Factorial - Opción D2 Aprobada)

* **Archivo fuente**: `slides/slide_10.html`
* **Compilado en**: `index.html` (`#slide-10`)
* **Arquetipo**: Matriz factorial 2×2 con panel superior ejecutivo y cuadrantes horizontales basados en cifras rectoras (cierre del Capítulo 02 de Metodología).
* **Propósito en ponencia**: Presentar la rigurosidad del diseño experimental ($14 \text{ preguntas} \times 7 \text{ esquemas RAG} \times 2 \text{ modelos SLM} = 196 \text{ combinaciones base} \times 4 \text{ réplicas} = 784 \text{ inferencias auditadas}$).

### Decisiones de Diseño y Contenido
* **Título Estratégico en una Sola Línea (`38px`)**:
  * Se sustituyó el titular que duplicaba los números por uno conceptual y riguroso: **«Diseño factorial: evaluación sistemática de búsqueda, inferencia y varianza»**.
  * Se redujo el tamaño de `46px` a `38px`, permitiendo que entre limpiamente en una sola línea y otorgando mayor respiro visual a la parte superior.
* **Banner Superior Ejecutivo Diferenciado y Centrado**:
  * Se asignó fondo blanco puro (`#FFFFFF`) con borde carbón profundo de `2px solid #2C0509` para desvincularlo totalmente del Cuadrante 1 (evitando que parezca la misma tarjeta).
  * Cada mitad (`196` y `784`) está internamente centrada, equilibrando armónicamente la cifra y su desglose factorial.
* **Descongestión Radical de Textos (Opción D2)**:
  * Se eliminaron todos los párrafos explicativos largos (>60% de reducción de texto).
  * Cada cuadrante se rediseñó con una cifra rectora dominante en `72px` monospace ultra-bold (`6`, `1`, `4`, `2`), separada por una línea vertical sutil de su especificación técnica concisa:
    1. **6 Esquemas BM25**: `top-k: 3 a 10 • Temp: 0.1 a 0.7` | Recuperación léxica por coincidencia exacta.
    2. **1 Esquema Denso**: `Embeddings • Temp: 0.30 fija` | Recuperación vectorial semántica.
    3. **4 Semillas de Réplica**: `42 · 7 · 123 · 2026` | Control estocástico y dispersión.
    4. **2 Métricas de Auditoría**: `Léxica + Semántica` | Fidelidad estricta al libro de texto.
* **Escala Tipográfica Ampliada para Auditorio (Cero Microtextos)**:
  * Cifras de banner aumentadas a `54px`, títulos a `24px` bold, y fórmulas explicativas ampliadas de `19px` a **`22px`** en negro carbón con resaltados cromáticos.
  * Títulos de cuadrantes ampliados a **`30px`** extra-bold.
  * Especificaciones técnicas (`top-k`, `Temp`, semillas, métricas) ampliadas a **`24px` monospace bold**.
  * Subtextos descriptivos ampliados de `21px` a **`23px`** en `#110103` (`font-weight: 600`), garantizando legibilidad total a 15–20 metros.
* **Corrección Ortográfica Total**: Tildes en *Metodología, parámetros, únicas, configuración, léxica, semántica, recuperación, estocástico, réplicas, auditoría, métrica, automática*.

---

## Slide 11: Separador 03 - Resultados y Discusión (Hero Dark + GPS)

* **Archivo fuente**: `slides/slide_11.html`
* **Compilado en**: `index.html` (`#slide-11`)
* **Arquetipo**: Separador de capítulo con indicador de ruta / stepper horizontal (continuidad exacta con Slides 4 y 6).
* **Propósito en ponencia**: Transición de 5 a 10 segundos para dar inicio al Bloque 3 (Resultados empíricos, deconstrucción métrica y evaluación docente).

### Decisiones de Diseño y Contenido
* **Coherencia con la Ruta y Título Formal**: Se tituló **«Resultados y Discusión»** (`74px` extra-bold), con ortografía impecable, idéntico a la fase 03 definida en el Slide 3.
* **Subtítulo conciso y riguroso**: *«El falso empate de 0.795, la dispersión por semillas y el choque con el juicio docente.»* (`30px`), anticipando las tres tensiones científicas clave del capítulo.
* **Stepper / GPS Visual**: Se activó la etapa `03` con acento dorado brillante (`var(--c-gold)`), pasando las fases `01` y `02` a estado completado/sutil y manteniendo `04` tenue en espera.
---

## Slide 12: 03 · Resultados / Deconstrucción de la Ecuación 1 (Variante P2 Aprobada)

* **Archivo fuente**: `slides/slide_12.html`
* **Compilado en**: `index.html` (`#slide-12`)
* **Arquetipo**: Auditoría métrica heroica con barra segmentada (reconstrucción fiel de la Figura 1 del paper) y dos tarjetas de distorsión en código.
* **Propósito en ponencia**: Demostrar la falla estructural de la métrica automática de calidad $Q$: el 60% de la nota califica la relación pregunta-contexto y el largo de la respuesta, ignorando por completo el contenido generado por el modelo.

### Decisiones de Diseño y Contenido
* **Eliminación Total de «Cuadros dentro de cuadros»**:
  * Se descartaron las cajas anidadas con bordes interiores para las insignias.
  * Se adoptó la distribución horizontal limpia de la **Variante K2.2 / P2**: la tarjeta se divide en una columna métrica lateral a sangre y un área de explicación técnica, sin recuadros flotantes internos.
* **Solución de Contraste (Cero Fondos Oscuros con Letras Claras)**:
  * Las columnas laterales de las métricas (`0.00 → 0.50` y `Nota = 0.80`) se diseñaron sobre **fondo blanco puro (`#FFFFFF`)**, con tipografía monospace bold en vino oscuro (`#460811`) y rojo acento (`#C9101B`), evitando fondos oscuros que pierden definición en proyección.
  * El cuerpo de las tarjetas utiliza fondo suave `#FAF5F5` y texto en negro carbón profundo (`#110103`, `22px bold`), asegurando lectura instantánea a 15–20 metros.
* **Punteros Superiores Inspirados en la Figura 1 (K2.4)**:
  * Puntero 1 (Grounding 40%): `● 40% Evalúa fidelidad semántica` (`23px bold` en vino oscuro).
  * Puntero 2 (Relevance 40%): `▼ ¡Aquí la respuesta NO es dato de entrada!` (`24px bold` en rojo de alerta).
  * Puntero 3 (Longitud 20%): `▼ Solo caracteres` (`23px bold` en ocre profundo).
  * Punteros directos sobre el fondo blanco, sin cajas pesadas, guiando la mirada de la audiencia hacia la zona ciega de la fórmula.
* **Barra Hero Imponente (142px de altura)**:
  * Proporciones exactas de la fórmula: 40% Vino, 40% Rojo, 20% Ocre con esquinas 100% rectas.
  * Cifras dominantes en **`52px`** bold (`40%`, `40%`, `20%`).
  * Etiquetas de término en **`24px`** y subtítulos de función en **`21px`**.
  * **Eliminación de la fórmula repetitiva en gris**: Se retiró la línea secundaria `Q(r, q, C) = 0.40·G + ...` bajo la barra, ya que duplicaba la información de forma redundante con tipografía pequeña de bajo aporte. Al suprimirla, la barra respira con holgura y la diapositiva gana pureza visual.
* **Tarjetas de Distorsión Ultra-Sintéticas (1 frase técnica por trampa)**:
  * **Coseno Reescalado $(x+1)/2$**: *"Respuestas desconectadas del libro obtienen **0.50 aprobado** como piso garantizado."*
  * **Premio al Rechazo (9 Frases)**: *"Nueve frases fijas reciben **0.80 directo**, premiando a modelos que rehúyen responder."*

---

## Slide 13: 03 · Resultados / El Falso Empate Estadístico y Variación por Semillas (Variante C1 + T3 Aprobada)

* **Archivo fuente**: `slides/slide_13.html`
* **Compilado en**: `index.html` (`#slide-13`)
* **Arquetipo**: Reconstrucción de la Figura 3 del paper (gráfico de dispersión dot-and-whisker plot) + métricas abiertas nativas de la plantilla.
* **Propósito en ponencia**: Demostrar que la diferencia de 0.002 entre Phi-4-mini y Qwen2.5-3B es un falso empate estadístico ($p = 0.569$ en prueba de Wilcoxon), y que la variación estocástica intra-modelo por cambio de semilla ($0.037$) es $18.5\times$ superior a la brecha neta, haciendo científicamente obligatorio evaluar con múltiples semillas.

### Decisiones de Diseño y Contenido
* **Hero Central Superior (Figura 3 del Paper)**:
  * Gráfica de dispersión a todo lo ancho con los 12 pares de preguntas curriculares (**G1 a R2**).
  * Bigotes de dispersión y puntos de media generosos (`stroke-width: 5.5px`, `r: 8.5px`) para **Phi-4-mini** (`#460811`) y **Qwen2.5-3B** (`#C9101B`).
  * Evidencia visual inmediata: los bigotes de error se cruzan y solapan en casi todas las preguntas, demostrando empíricamente la ausencia de un modelo superior.
* **Retorno al Estilo Nativo de la Plantilla con Síntesis L3**:
  * Se sustituyeron los recuadros cerrados por el patrón abierto de métricas de la plantilla (`.s8-metric-item`), con **barra lateral vertical de 7px** de acento y textos compactos en dos líneas limpias:
  * Métrica 1 (Vino): `p = 0.569` **Empate Real** (`52px` mono) / *Wilcoxon (W = 31.0) · Brecha neta de apenas **0.002**.*
  * Métrica 2 (Rojo): `18.5×` **Ruido Estocástico** (`52px` mono) / *Desviación de **0.037** · Obligatorio evaluar con 4 semillas.*
* **Eliminación Total de Sobrecarga y Texto de Relleno**:
  * Se suprimieron párrafos explicativos largos y etiquetas redundantes (*"Figura 3 del paper"*).
  * Se eliminó el banner inferior de alerta que saturaba la diapositiva, integrando la exigencia metodológica directamente en la segunda métrica.
  * La gráfica superior gana todo el protagonismo, respirando con total claridad desde 20 metros.

---

## Slide 14: 03 · Resultados / Modos de Fallo Asimétricos (Díptico Panorámico Horizontal R3 Aprobado)

* **Archivo fuente**: `slides/slide_14.html`
* **Compilado en**: `index.html` (`#slide-14`)
* **Arquetipo**: Díptico panorámico horizontal en dos filas con barras porcentuales heroicas (Variante R3 seleccionada).
* **Propósito en ponencia**: Presentar el hallazgo empírico de la Tabla 3 del paper: dos modelos con idéntico puntaje general ($Q \approx 0.80$) exhiben modos de fallo totalmente opuestos y asimétricos (alucinación en Phi-4-mini vs. sobre-rechazo en Qwen2.5-3B), demostrando que la nota cuantitativa oculta riesgos pedagógicos divergentes y condiciona su entorno de despliegue escolar.

### Decisiones de Diseño y Contenido
* **Díptico Panorámico Horizontal en 16:9 (Erradicación del Espacio Muerto)**:
  * Frente a las columnas verticales tradicionales que acumulaban vacíos de hasta 200px o saturación de texto, se adoptó una arquitectura en **dos grandes filas horizontales** (una por modelo).
  * Distribución natural: el lienzo de 1700px se divide en una celda de identidad a la izquierda (460px) y dos barras métricas anchas y paralelas a la derecha.
* **Barras de Porcentajes como Protagonistas Heroicas**:
  * Altura de barra ampliada a **30px** con pista neutra de fondo (`#EAE0E1`) y llenado sólido en colores institucionales.
  * Cifras métricas colosales en tipografía monoespaciada de **`40px` bold**:
    * **Phi-4-mini**: `28.6%` (4/14) en rojo acento (sondas trampa) | `0.0%` (0/84) en vino institucional (consultas válidas).
    * **Qwen2.5-3B**: `85.7%` (12/14) en vino institucional (sondas trampa) | `7.1%` (6/84) en rojo acento (consultas válidas).
* **Depuración Extrema de Texto (Anclaje Factual en 1 Sola Línea)**:
  * Se eliminaron todos los párrafos explicativos, subtítulos decorativos y etiquetas redundantes.
  * Cada métrica cuenta únicamente con: Etiqueta formal + Cifra mono destacada + Barra de 30px + **1 sola frase concisa de evidencia**:
    * *"Alucina en 10 casos fuera del libro."* / *"Fluidez total; jamás frena al alumno."*
    * *"Filtro riguroso frente a trampas."* / *"Sobre-rechazo por cautela extrema."*
* **Remate Pedagógico de Alto Contraste para Auditorio (Opción P2 Aprobada)**:
  * Cada modelo declara de forma ejecutiva su aplicación real: **Aula asistida** (con docente que guía y supervisa) frente a **Autoestudio** (sin profesor, donde prima la certeza de no engañar al alumno).
  * Para evitar la pérdida de legibilidad de los textos blancos sobre fondos oscuros en salones con alta luz ambiental, se implementó la **Franja Editorial con Doble Guía Superior e Inferior de 3.5px** en vinotinto institucional (`var(--c-wine-primary)`) sobre fondo marfil suave (`#FAF5F5`).
  * Toda la sentencia entra en **1 sola línea continua** sin quiebres: `CONCLUSIÓN PEDAGÓGICA:` en monoespaciada vinotinto (`19px`) + la tesis central en negro carbón profundo (`#110103`, `23px` bold), garantizando contraste óptico máximo y lectura fluida hasta la última fila del auditorio.
  * Incluye la referencia formal `Tabla 3 (×4 semillas)` a la derecha y conserva un holgado colchón de aire de más de 120px sobre la barra del pie de página.

---

## Slide 15: 03 · Resultados / El Choque con el Criterio Docente (Slopegraph Monumental Flat + Métricas Directas - Opción G1-C2 Aprobada)

* **Archivo fuente**: `slides/slide_15.html`
* **Compilado en**: `index.html` (`#slide-15`)
* **Arquetipo**: Slopegraph monumental sobre lienzo 100% abierto (sin recuadros) + columna lateral de 3 métricas sintéticas.
* **Propósito en ponencia**: Demostrar empíricamente la disparidad entre la evaluación algorítmica y el criterio de docentes de aula (Tabla 4 y Figura 4 del paper): dos profesores discreparon radicalmente entre sí ($\kappa = -0.429$, acuerdo peor que el azar) y con el benchmark automático ($\rho \le +0.26$, correlación nula), validando 3 respuestas cada uno sin coincidir en una sola ($0/10$).

### Decisiones de Diseño y Contenido
* **Selección del Arquetipo G1-C (Lienzo 100% Abierto y Flat)**:
  * Se descartaron los contenedores con bordes pesados y cajas cerradas ("cuadros dentro de cuadros").
  * El gráfico slopegraph flota directamente sobre el fondo del slide con respiración panorámica y generosa (`viewBox="0 0 1140 540"`).
  * Los dos ejes verticales de los evaluadores se separaron a **640px de amplitud** (Variante C2), suavizando las pendientes para que los cruces se distingan a 20 metros.
* **Depuración Extrema de Saturación y Ruido Visual**:
  * **Eliminación del encabezado decorativo**: Se retiró el texto `FIGURA 4 · CALIFICACIONES INDEPENDIENTES` y la barra divisoria superior que encajonaban la gráfica.
  * **Eliminación de la nota editorial inferior**: Se suprimió la franja de lección de campo al pie para permitir que el gráfico y las métricas tengan total libertad vertical sin comprimirse.
  * **Eliminación de la leyenda repetitiva**: Se erradicaron los textos largos de *"Aprobó Docente 1..."*, *"Aprobó Docente 2..."*. El código cromático es autoexplicativo a través de las cabeceras de los ejes.
* **Jerarquía Cromática y Atenuación de Datos Secundarios**:
  * **4 respuestas reprobadas por ambos docentes**: Opacadas al máximo en un gris neutro muy suave (`#D8CBCD`, 2px, opacidad 0.40) para no competir con el mensaje central.
  * **3 respuestas aprobadas por Docente 1**: Resaltadas en **Vinotinto Institucional (`#460811`, 5.0–6.5px)**; evidencian el desplome directo desde calificaciones altas (4.0, 3.67, 3.33) hasta la nota mínima (1.0 y 1.33) asignada por el Docente 2.
  * **3 respuestas aprobadas por Docente 2**: Resaltadas en **Rojo Carmesí (`#C9101B`, 5.0px)**; muestran notas de 2.33 y 3.33 consideradas aptas para aula por el Docente 2 pero que el Docente 1 calificó con apenas 3.0.
* **Columna Lateral de Máximo Impacto Numérico**:
  * Tres tarjetas limpias en `#FAF5F5` con acentos verticales de 10px en Oro, Rojo y Vino, sin prosa de relleno:
    1. **`0 / 10`** (`68px` mono) en Oro (`#B38600`): **Coincidencias en Aula** / *Aprobaciones 100% disjuntas.*
    2. **`κ = -0.429`** (`54px` mono) en Rojo (`#C9101B`): **Desacuerdo Severo** / *Kappa de Cohen negativo (peor que el azar).*
    3. **`ρ ≤ +0.26`** (`48px` mono) en Vino (`#460811`): **Correlación Nula** / *Sin relación con el algoritmo ($p > 0.40$).*

---

## Slide 16: Separador 04 - Discusión y Conclusiones (Hero Dark + GPS Stepper)

* **Archivo fuente**: `slides/slide_16.html`
* **Compilado en**: `index.html` (`#slide-16`)
* **Arquetipo**: Separador de capítulo con indicador de ruta / stepper horizontal (continuidad exacta con Slides 04, 06 y 11).
* **Propósito en ponencia**: Transición de 5 a 10 segundos para dar inicio al Bloque 4 y final de la ponencia (Discusión pedagógica, implicaciones institucionales y directrices de despliegue rural).

### Decisiones de Diseño y Contenido
* **Coherencia con la Ruta General (Slide 3)**:
  * Título oficial: **"Discusión y Conclusiones"** (`74px` extra-bold blanco), ortografía impecable con tilde.
  * Subtítulo conciso y formal: *"Matriz de riesgo pedagógico, criterios de adopción y lecciones para el aula rural."* (`30px`), eliminando retórica pretenciosa.
* **Stepper / GPS Visual (Fase 4 Activa)**:
  * Se activa la etapa `04` con borde superior dorado brillante (`var(--c-gold)`), etiqueta `04` en dorado y rótulo *"Conclusiones"* en blanco nítido y bold.
  * Las etapas previas (`01 Contexto Rural`, `02 Metodología RAG`, `03 Resultados`) pasan a estado completado en blanco sutil (`rgba(255,255,255,0.4)` / `rgba(255,255,255,0.7)`), comunicando visualmente a la audiencia que nos encontramos en la recta final de la exposición.
* **Identidad Institucional**:
  * Silueta sutil y elegante de la Torre de Cartagena a la derecha sobre fondo vinotinto profundo (`--c-wine-dark`).
  * Eliminación de las 3 torres repetidas de la plantilla original para garantizar limpieza y sofisticación visual.

---

## Slide 17: 04 · Discusión · Guía Metodológica de Elección (Matriz 2x2 Split C-3B)

* **Archivo fuente**: `slides/slide_17.html`
* **Compilado en**: `index.html` (`#slide-17`)
* **Arquetipo**: Matriz cuadrante 2×2 con Split Lateral Heroico y Cero Cajas Anidadas (Opción C-3B seleccionada y verificada).
* **Propósito en ponencia**: Desmontar la falacia del promedio agregado (0.795) y entregar a la audiencia la directriz metodológica concreta de selección de modelos según el entorno pedagógico (sin docente vs con docente).

### Decisiones de Diseño y Contenido
* **Eliminación Total de "Cuadros dentro de Cuadros"**:
  * Se suprimieron las placas o rectángulos de color anidados que contenían los porcentajes.
  * La métrica numérica se transformó en pura tipografía monumental sobre el fondo limpio `#FAF5F5` de la tarjeta, separada por una línea divisoria vertical sutil de `3px solid #E5D5D5`.
* **Escala Tipográfica de Alto Impacto y Máxima Síntesis**:
  * Título de cabecera (`.s-lead-question`): **`38px`** extra-bold (*"Apego al texto no es aprendizaje: criterios para auditar y desplegar tutores"*).
  * Títulos de cada cuadrante: **`35px`** extra-bold (`font-weight: 900`).
  * Cifras y porcentajes monumentales: **`64px`** y **`68px`** monoespaciados en negrita extrema (`font-weight: 900`).
  * Texto explicativo ultra-sintetizado: **`28px`** semi-bold (`font-weight: 600`, `line-height: 1.35`), reducido a un máximo de 9–11 palabras por tarjeta para lectura instantánea a 25 metros.
* **Sentido Lógico y Semántico de la Paleta Cromática**:
  * **Fila Superior (Criterios Científicos)**:
    * *Cuadrante 01 (`#C51625` Rojo Alerta):* La Falacia del Promedio $\rightarrow$ **`0.795`** Apego engañoso | *"Mide copia del libro, no comprensión real ni capacidad pedagógica."*
    * *Cuadrante 02 (`#4A3B3D` Gris Pizarra Neutral):* Auditoría Desglosada $\rightarrow$ **`3`** Dimensiones | *"Prohibido promedio único: auditar fidelidad y rechazo por separado."*
  * **Fila Inferior (Despliegue de Modelos en Producción)**:
    * *Cuadrante 03 (`var(--c-wine-primary)` Vino Institucional):* Autoestudio Autónomo $\rightarrow$ **Qwen2.5-3B** $\rightarrow$ **`85.7%`** Rechazo certero | *"Sin profesor: preferible admitir no saber antes que inventar."*
    * *Cuadrante 04 (`var(--c-red-accent)` Rojo Acento):* Aula Asistida $\rightarrow$ **Phi-4-mini** $\rightarrow$ **`0.0%`** Bloqueos al diálogo | *"Con profesor: prima la fluidez y el docente corrige en vivo."*
* **Ajuste y Respiración de Paddings (Espaciado Perimetral Holgado)**:
  * Se amplió el ancho de la columna de métricas de `190px` a **`245px`** con padding perimetral de tarjeta de **`26px 36px`**.
  * Se ajustó el tamaño de los números y porcentajes a **`58px`** monoespaciados (`letter-spacing: -1px`), garantizando un margen libre superior a **`50px`** respecto al borde derecho y más de **`40px`** respecto a la línea divisoria.
  * La línea divisoria vertical se estilizó como un espinazo editorial de **`130px`** de altura centrado verticalmente (`2px solid #E2D2D2`), perfectamente alineado con la altura del bloque textual y eliminando cualquier sensación de saturación perimetral.
* **Ortografía y Rigor Académico**: Tildes corregidas en *Discusión*, *Guía*, *Metodológica*, *Elección*, *Auditoría*, *Técnico*, *Autónomo*, *Diálogo*.

---

## Slide 18: 04 · Conclusiones y Aportes (3 Filas Editoriales + Tesis Defendida)

* **Archivo fuente**: `slides/slide_18.html`
* **Compilado en**: `index.html` (`#slide-18`)
* **Arquetipo**: 3 Filas Editoriales con Columna Métrica Izquierda y Banner de Cierre Alineado (Evolución armónica del arquetipo de Slide 2).
* **Propósito en ponencia**: Clímax de los aportes sustantivos de la investigación (3 lecciones definitivas) y declaración formal de la tesis defendida ante el congreso.

### Decisiones de Diseño y Contenido
* **Eliminación Total de Listas de Viñetas (`ul/li`)**:
  * Se suprimieron las listas con viñetas genéricas del borrador preliminar.
  * Se sustituyeron por 3 bloques horizontales estructurados, legibles y de alto rango editorial.
* **Escala Tipográfica para Auditorio ("Cuida los textos y que no sean tan pequeños")**:
  * Lead Question: **`38px`** extra-bold (*"Tres lecciones para la adopción real de tutores de IA en aulas desconectadas"*).
  * Títulos de cada lección: **`32px`** bold (`font-weight: 900`).
  * Textos explicativos: **`27px`** semi-bold (`font-weight: 600`, `line-height: 1.35`), limitados estrictamente a 2 líneas concisas con negritas estratégicas.
  * Números de impacto: **`56px`** monoespaciados en Filas 1 y 2, y **`42px`** monoespaciado en Fila 3 (`κ = -0.429` en una sola línea nítida).
* **Precisión Geométrica y Alineación Continua**:
  * Las 3 filas y el banner inferior comparten una columna izquierda estandarizada de **`290px`**.
  * La línea divisoria vertical (`2px solid #E2D2D2` / `#D8B8BE`) corre por la misma coordenada horizontal a lo largo de toda la diapositiva, garantizando coherencia visual absoluta.
* **Banner Tesis Defendida: Opción F3 (Doble Regla Editorial Horizontal 100% Plana)**:
  * **Eliminación Total de Esquinas Redondeadas (`border-radius: 0`)**: En estricto apego al estilo editorial suizo y a las demás diapositivas del proyecto ([styles.css:1973](file:///c:/Users/ASUS/Desktop/Diapositivas-Cartagena/styles.css#L1973)), se erradicaron las esquinas redondeadas ajenas al sistema de diseño.
  * **Estructura Editorial Inspirada en Slide 14**: Enmarcado superior e inferior con dos reglas continuas en Vino Institucional (`border-top: 3.5px solid var(--c-wine-primary)` y `border-bottom: 3.5px solid var(--c-wine-primary)`), eliminando bordes laterales para evitar que simule una 4ta fila de lecciones.
  * **Etiqueta Tipográfica Integrada**: Columna izquierda compacta con rótulo monoespaciado `APORTE CENTRAL` (`13px`, tracking `1.5px`) sobre `Tesis Defendida` (`24px`, bold `900`), separado del cuerpo por un tick vertical de 2px (`#D8B8BE`).
  * **Texto Central de Máxima Convicción (`27px`)**: *"Democratizar la IA educativa rural mediante hardware común, sin transferir jamás la soberanía pedagógica a los algoritmos."*
* **Ortografía y Rigor Académico**: Tildes y acentuación formal completas en *Conclusiones*, *Aportes*, *Adopción*, *Conexión*, *Técnica*, *Metodología*, *Común*, *Estocásticas*, *Pedagógica*, *Calibración*, *Soberanía*.

---

## Slide 19: 05 · Referencias Bibliográficas Clave (Paneles Editoriales APA VII · Opción A2-1)

* **Archivo fuente**: `slides/slide_19.html`
* **Compilado en**: `index.html` (`#slide-19`)
* **Arquetipo**: Dos Grandes Paneles Editoriales Estructurados con Destacado Fino y Remate Institucional de Doble Regla (Opción A2-1 seleccionada y verificada).
* **Propósito en ponencia**: Proporcionar el soporte bibliográfico formal y científico de la ponencia en estándar APA 7.ª edición, destacando el artículo base de los autores en *Revista Entramado* y erradicando el espacio muerto del borrador inicial.

### Decisiones de Diseño y Contenido
* **Erradicación del Espacio Muerto (Anti-patrón Top-Heavy Resuelto)**:
  * El contenido anterior flotaba como texto simple en el tercio superior dejando más de 350px de vacío blanco.
  * Se diseñaron dos grandes paneles simétricos con fondo `#FAF5F5` y padding generoso (`24px 30px`), equilibrando la retícula vertical y llenando el lienzo con balance suizo.
* **Geometría 100% Plana y Ortogonal (`border-radius: 0;`)**:
  * Esquinas estrictamente a 90°, alineadas con el sistema de diseño oficial de Cartagena 2026.
* **Estructura de Paneles Temáticos**:
  * **Panel Izquierdo (`border-top: 6px solid var(--c-wine-primary)` - Vinotinto Institucional)**:
    * *01 · RAG Y EVALUACIÓN AUTOMATIZADA*
    * `Lewis et al. (2020)` · RAG Fundacional (`NeurIPS 2020`).
    * `Es et al. (2024)` · Evaluación Métrica RAGAs (`EACL 2024`).
    * `Nogueira & Cho (2019)` · Reordenamiento Semántico Cross-Encoder (`arXiv:1901.04085`).
  * **Panel Derecho (`border-top: 6px solid var(--c-red-accent)` - Rojo Carmesí)**:
    * *02 · MODELOS SLM Y ARTÍCULO BASE*
    * `Muñoz-Gómez, Hoyos-Cerón, & Caiza (2026)` · **Artículo Base del Benchmark**:
      * Enmarcado con filete fino homogéneo de 1.5px (`#D8B8BE`) en tono vino suave (`#FAF0F2`), **sin bordes laterales gruesos**, manteniendo simetría total.
      * Insignia prominente en **`15px`** monoespaciado extra-bold: `★ ARTÍCULO BASE DEL BENCHMARK` en blanco sobre vinotinto sólido.
      * Sub-rótulos institucionales: `COLMAYOR CAUCA` y `REVISTA ENTRAMADO · 2026`.
      * Autores en **`24px`** extra-bold (`font-weight: 900`, `var(--c-wine-primary)`).
    * `Abouelenin et al. (2025)` · SLM Evaluado Phi-4-mini (`arXiv:2503.01743`).
    * `Yang et al. (2024)` · SLM Evaluado Qwen2.5 (`arXiv:2412.15115`).
* **Remate Institucional de Doble Regla (Estilo Slide 14/18)**:
  * Banner horizontal inferior delimitado por dos líneas horizontales en Vinotinto (`border-top: 3.5px solid var(--c-wine-primary)` y `border-bottom: 3.5px solid var(--c-wine-primary)`), integrando la filiación del congreso y enlace al benchmark: `LOHACEMOSXTIC.COM`.
* **Corrección Ortográfica Integral**: Tildes añadidas en *Referencias*, *Bibliográficas*, *Evaluación*, *Automatizada*, *Muñoz-Gómez*, *Hoyos-Cerón*, *Artículo*, *Investigación*.

---

## Slide 20: 05 · Cierre · Preguntas, Agradecimientos y Contacto (Panel Editorial Claro · Opción A Aprobada)

* **Archivo fuente**: `slides/slide_20.html`
* **Compilado en**: `index.html` (`#slide-20`)
* **Arquetipo**: Dos Grandes Paneles Editoriales Simétricos con Reconocimiento Institucional, Evaluación a Ciegas, Coorganizadores, Preguntas en Vivo, Correspondencia y Tarjeta QR.
* **Propósito en ponencia**: Cierre definitivo de la presentación ante el auditorio del VI Congreso Internacional de Investigación Interdisciplinar, expresando gratitud formal, reconociendo el rigor del juicio ciego docente, rindiendo tributo a las universidades coorganizadoras y habilitando canales de correspondencia y acceso al repositorio abierto.

### Decisiones de Diseño y Contenido
* **Estructura Arquitectónica Simétrica y Balanceada (1.15fr : 0.85fr)**:
  * Frente a diseños con fondo oscuro o cajas anidadas, se implementó el **Arquetipo Editorial Claro** con fondo `#FAF5F5` y respiración perimetral holgada (`24px 30px`), garantizando continuidad cromática impecable con los slides precedentes (14, 18 y 19).
* **Geometría 100% Plana y Ortogonal (`border-radius: 0;`)**:
  * Esquinas estrictamente a 90° en todos los contenedores, badges, marco del código QR y banner inferior, manteniendo fidelidad absoluta al sistema de diseño suizo y la directriz global de no redondear bordes.
* **Panel Izquierdo: Reconocimientos y Rigor Científico (`border-top: 6px solid var(--c-wine-primary)`)**:
  * **Filiación Institucional**: Institución Universitaria Colegio Mayor del Cauca, Grupo de Investigación I+D Informática y Semillero BETABIT.
  * **Docentes Evaluadores Independientes**: Reconocimiento expreso y destacado a los profesores *Juan Pablo Machado Vélez* & *Stevens Álvarez Domínguez* por su evaluación a ciegas y calibración pedagógica en contexto real.
  * **Entidades Coorganizadoras**: Inclusión horizontal armónica de los logotipos oficiales de la *Universidad Distrital Francisco José de Caldas*, la *Universidad Tecnológica de Bolívar (UTB)* y la *Universidad de Cartagena*, normalizados en escala y alineados al pie del panel.
* **Panel Derecho: Sesión de Preguntas, Autores y QR (`border-top: 6px solid var(--c-red-accent)`)**:
  * **Sesión de Preguntas**: Rótulo de invitación al diálogo y discusión abierta con insignia `EN VIVO` en rojo acento.
  * **Correspondencia Formal**: Correos electrónicos de los ponentes (`fabian.hoyos@colmayor.edu.co` y `yeison.munoz@colmayor.edu.co`) en tipografía monoespaciada bold de `19px`.
  * **Tarjeta QR de Acceso al Benchmark**: Enmarcado plano de 1.5px (`#D8B8BE`) en tono marfil suave (`#FAF0F2`), código QR en alta fidelidad sobre fondo blanco nítido, enlace monumental en negrita extrema a `LOHACEMOSXTIC.COM` y descripción del repositorio abierto de código y datos empíricos.
* **Remate Institucional de Doble Regla Vinotinto (Estilo Slides 14, 18 y 19)**:
  * Banner inferior delimitado por dos líneas horizontales en Vinotinto (`border-top: 3.5px solid var(--c-wine-primary)` y `border-bottom: 3.5px solid var(--c-wine-primary)`), integrando la filiación de Cartagena 2026 y el rótulo monoespaciado `CIERRE DE PONENCIA`.
* **Corrección Ortográfica Rigurosa**: Tildes y acentuación formal auditadas (*atención*, *Institución*, *Informática*, *Investigación*, *Vélez*, *Álvarez*, *Domínguez*, *evaluación*, *Sesión*, *Diálogo*, *Discusión*, *código*).

---

# Iteración 2: Incorporación Sistemática de Sellos Asimétricos, Logos Oficiales e Iconografía Técnica

A partir de la directriz del usuario de romper la rigidez ortogonal sin alterar el contenido aprobado ni la escala legible a distancia, se ejecutó un despliegue transversal de **sellos asimétricos flotantes** (`.tech-stamp`), **iconos vectoriales SVG** y **marcas tecnológicas oficiales**.

### Principios Rectores de la Iteración 2:
1. **Asimetría Orgánica**: Rotaciones sutiles alternadas entre `-2.5°` y `+3.0°` (`transform: rotate(...)`) que rompen la monotonía de las cajas sin perder alineación general ni generar solapamiento de textos.
2. **Dimensionamiento Sustantivo**: Microchips ampliados a `13px`–`15px` en tipografía monoespaciada bold (`font-weight: 800`), con bordes sólidos de `1.5px`–`2px` y sombras suaves (`box-shadow: 0 4px 14px rgba(0,0,0,0.08)`), garantizando que aporten información técnica concreta y no actúen como mero adorno.
3. **Geometría 100% Plana**: Erradicación total de esquinas redondeadas residuales (`border-radius: 0;`).
4. **Logotipos y Marcas Oficiales**:
   * **Microsoft Research**: Cuadrícula de 4 colores `#f25022`, `#00a4ef`, `#7fba00`, `#ffb900` + licencia MIT en Slides 14, 17 y 19.
   * **Alibaba Cloud**: Emblema en corchetes característico en naranja `#FF6A00` + licencia Apache 2.0 en Slides 14, 17 y 19.
5. **Inventario por Diapositiva**:
   * **Slide 02**: Sellos asimétricos en las 3 filas: `BARRERA NUBE · PAGOS USD` (+2°), `USB 3.0 · OFFLINE x86 · SIN GPU` (-2.5°), `WILCOXON p = 0.569 · N = 12 PARES` (+2°).
   * **Slide 05**: Sellos asimétricos sobre el borde superior de cada columna: `DANE 2024 · EXCLUSIÓN` (-2.5°), `SLM 3B · CPU LOCAL` (+2.5°), `AIR-GAPPED · RAGAs` (-2°).
   * **Slide 07**: Variante A2-2 aprobada: Sellos técnicos de gran formato en los 4 pasos del pipeline (`FAISS · MINI-LM`, `CROSS-ENCODER`, `llama.cpp · C/C++`) y sello panorámico `PLUG & PLAY · PORTABLE EN USB 3.0` (-2.5°).
   * **Slide 08**: Corrección de esquinas a 90° y sellos en las 3 tarjetas de telemetría: `RAM ≤ 3.8 GB · SIN GPU` (+2°), `COLLEGE ESL · CITAS REALES` (-2.5°), `AIR-GAPPED · PRIVACIDAD 100%` (+2°).
   * **Slide 09**: Sello flotante superior `COLLEGE ESL WRITERS · N = 14 ÍTEMS` (+2°), corrección a 90° de la etiqueta de rechazo `AUSENTE EN LIBRO` (-2°) e icono SVG de alerta.
   * **Slide 10**: Sello cenital en banner `★ AUDITORÍA FACTORIAL COMPLETA` (+2°) y 4 sellos asimétricos en los cuadrantes factoriales: `LÉXICO · EXACT MATCH` (-2°), `FAISS · MINI-LM` (+2°), `CONTROL MONTE CARLO` (-2.5°), `AUDITORÍA RAGAs · MEN` (+2°).
   * **Slide 12**: Sello flotante de cabecera `RAGAs MODIFICADA · ECUACIÓN 1` (+2.5°) y sellos asimétricos en tarjetas de distorsión: `PISO MATEMÁTICO INFLADO` (-2°) y `DISTORSIÓN HEURÍSTICA` (+2°).
   * **Slide 13**: Sello flotante en gráfica de dispersión `N = 4 SEMILLAS · ANÁLISIS MULTI-RUN` (+2°) y micro-badges con SVGs en métricas inferiores: `MATCHED-PAIRS` (-2°) y `VARIANZA ESTOCÁSTICA` (+2°).
   * **Slide 14**: Díptico con logos oficiales y sellos: Microsoft Research + `MIT LICENSE` (+2.5°) y Alibaba Cloud + `APACHE 2.0` (-2.5°).
   * **Slide 15**: Sello flotante cenital `EVALUACIÓN CIEGA · 2 DOCENTES EXPERTOS` (-2°) y badge `INTER-RATER RELIABILITY` (+2°) sobre tarjeta Kappa.
   * **Slide 17**: Sellos en los 4 cuadrantes de la matriz: `ALERTA METODOLÓGICA` (-2.5°), `NUEVO ESTÁNDAR` (+2°), Alibaba Cloud + `APACHE 2.0` (-2°) y Microsoft + `MIT` (+2.5°).
   * **Slide 18**: Sellos en las 3 lecciones finales: `PLUG & PLAY · USB 3.0` (+2°), `MULTI-SEMILLA OBLIGATORIA` (-2.5°), `DOCENCIA SITUADA` (+2°).
   * **Slide 19**: Micro-chips de marca con logos vectoriales para `MICROSOFT` (+1.5°) y `ALIBABA CLOUD` (-1.5°) en las fuentes de modelos SLM.

---

# Iteración 3: Erradicación del Abuso de Mini-Chips e Integración de Fotografía Documental y Evidencia Tecnológica Real

### Diagnóstico Crítico y Mandato del Usuario
El usuario identificó una sobreutilización del recurso estilístico de los sellos asimétricos y micro-chips:
> *"pero abusaste de poner los mini-chips y los iconos . la idea era imagenes de las tecnologias e imagenes de cualquier cosa , pero no abusar del mismo recurso en todo"*

La repetición mecánica de estampas rotadas con borde y sombra generaba saturación visual y convertía un recurso tipográfico en un patrón genérico. El objetivo real de la presentación es exhibir **evidencia fotográfica auténtica del contexto rural colombiano, hardware real auditado, libros de texto curriculares y logotipos oficiales de las tecnologías evaluadas**, dotando a cada diapositiva de variedad editorial y rigor documental.

### Principios Rectores de la Iteración 3:
1. **Cero Repetición de Trucos Gráficos**: Eliminación total del patrón de sellos flotantes inclinados (`transform: rotate(...)`) en todas las diapositivas de la presentación.
2. **Fotografía Documental Auténtica de Campo y Tecnologías**:
   * **Slide 05 (Contexto Rural y Brecha)**: Incorporación de `assets/photo_rural_classroom.jpg`, una fotografía documental realista de un aula de cómputo en una escuela rural colombiana, con estudiantes en computadores de escritorio, luz natural y montañas andinas visibles a través de las ventanas. Rompe la simetría de 3 cajas con un diseño editorial de dos columnas (Fotografía documental + Cifra rectora del 58.6% y las dos preguntas de investigación).
   * **Slide 08 (Demostración de Hardware Escolar)**: Incorporación de `assets/tech_usb_offline.jpg`, fotografía macro y documental de una memoria USB 3.0 metálica conectada al puerto frontal de un PC escolar Dell OptiPlex en plena aula activa con estudiantes de fondo. Brinda prueba táctil y física del despliegue *plug & play* sin tarjeta gráfica (GPU).
   * **Slide 09 (Corpus Curricular y Banco de Evaluación)**: Incorporación de `assets/book_college_esl.jpg`, fotografía documental del libro abierto *College ESL Writers* sobre un pupitre de madera con ejercicios de gramática, notas manuscritas y bolígrafo. Acompaña a la tabla de 14 preguntas mediante un panel lateral de metadatos curriculares (339 trozos, control anti-alucinación, citas página a página).
3. **Logotipos Tecnológicos Integrados Nativamente (Sin Estampas Flotantes)**:
   * **Slide 14**: Los isotipos de **Microsoft Research** (cuadrícula de 4 colores) y **Alibaba Cloud** (emblema vectorial naranja) se ubican directamente junto al nombre de cada modelo (`Phi-4-mini` y `Qwen2.5-3B`), acompañados de insignias planas de licencia (`MIT` y `APACHE 2.0`), eliminando las estampas rotadas que flotaban sobre el borde.
   * **Slide 17**: Los logotipos de Alibaba y Microsoft se integran dentro de los encabezados de los Cuadrantes 3 y 4 de forma ortogonal y limpia.
4. **Limpieza Sistemática de Sellos Inclinados**:
   * **Slides 02, 07, 10, 12, 13, 14, 15, 17, 18 y 19**: Retorno a la pureza geométrica ortogonal. Las métricas, gráficas de dispersión (dot-whisker plot) y slopegraphs respiran con máxima autoridad académica y legibilidad proyectada a 15–20 metros.
5. **Geometría 100% Plana**: Todo contenedor, marco de imagen y botón respeta estrictamente `border-radius: 0;`.

---

# Iteración 4: Erradicación Definitiva de Mini-Chips, Ilustraciones Vectoriales Animadas Éticas, Citas Discretas y Emblemas de Modelos en Esquina

### Diagnóstico Crítico y Mandato del Usuario
El usuario emitió directrices precisas y categóricas para optimizar la legibilidad y la ética de la presentación:
1. *"quita todos esos mini-chips , no se ven por lo cual no aportan nada ."*
2. *"y en las imagenes añadiste textos , que no estan mal pero si dejas solo el mas importante y que si se vea es mejor ."*
3. *"y debes poner referencia de donde sacas la imagen y ponerla debajo en algun lugar , no que se vea del todo pero solo por cumplir"*
4. *"Creo que para no usa imagenes reales , es mejor que generes ilustraciones animadas . esas si es mejor que las generes . esas fotos que estabas sacando moralmente no me parecian ."*
5. *"para los iconos o logos de los modelos hazlos un poco mas grandes por que ni se notan o ponlos en una esquina de la tarjeta asi como grandecitos e inclinados."*

### Decisiones de Diseño y Solución Implementada:

1. **Erradicación Absoluta de Mini-Chips e Insignias Píldora**:
   - Se barrieron y eliminaron por completo las micro-etiquetas con fondos encapsulados (`padding: 2px 8px`, `font-size: 11px–13px`) que resultaban invisibles desde el auditorio.
   - **Slide 05**: Eliminación de chips de preguntas (`SLM ≤ 3B • CPU ESCOLAR` y `AIR-GAPPED • EVALUACIÓN`).
   - **Slide 07**: Eliminación de los 4 chips de pasos (`PDF • MEN`, `BM25 + DENSO (RRF)`, `MINILM RERANKER`, `llama.cpp • C++`) y del chip de la tarjeta panorámica inferior (`PORTABLE EN USB 3.0`).
   - **Slide 08**: Eliminación de chips de telemetría (`RAM ≤ 3.8 GB` y `0 KB/s EXTERNO`).
   - **Slide 09**: Sustitución del micro-chip `Ausente` por tipografía de tabla clara y legible (`Sin registro`).
   - **Slide 10**: Eliminación de los 4 chips de cuadrantes factoriales (`LÉXICO`, `SEMÁNTICO`, `MONTE CARLO`, `RAGAs • MEN`).
   - **Slide 14**: Eliminación de chips de licencias (`MIT` y `APACHE 2.0`).
   - **Slide 17**: Eliminación de chips de encabezado de modelos (`ALIBABA • APACHE 2.0` y `MICROSOFT • MIT`).
   - **Slide 19**: Eliminación de chips de conteo de fuentes (`3 FUENTES`) y badges redundantes en referencias de autores.
   - **Slide 20**: Eliminación del chip `EN VIVO`.

2. **Ilustraciones Vectoriales Animadas Originales (Ética y Privacidad Escolar)**:
   - Ante la legítima objeción ética de utilizar fotografías de menores de edad en aulas rurales sin consentimiento explícito, se reemplazaron las fotos por ilustraciones vectoriales animadas en formato SVG nativo, con la paleta de color institucional (vino `#7B1113`, oro `#D4AF37`, rojo `#C51625` y fondos `#FAF5F5`):
   - **Slide 05 (`assets/illustration_rural_offline.svg`)**: Escena editorial animada de un aula escolar con ventana a las montañas colombianas, escritorio de madera con libro de gramática, computador con interfaz de asistente local LoxTIC y badge animado flotante *100% AIR-GAPPED*.
   - **Slide 08 (`assets/illustration_usb_deployment.svg`)**: Diagrama técnico animado en modo oscuro con la memoria SanDisk Ultra Flair USB 3.0 conectada al chasis escolar Dell, emitiendo pulsos de datos animados hacia el chip de CPU x86 a 1.9 tok/s sin GPU.
   - **Slide 09 (`assets/illustration_college_esl_book.svg`)**: Ilustración vectorial del libro de texto curricular *College ESL Writers* (Capítulo 4, fórmulas de Present Perfect y trozo semántico #142) con cinta marcapáginas dorada animada.

3. **Titular Único Prominente en Ilustraciones**:
   - En lugar de saturar las ilustraciones con múltiples carteles, etiquetas flotantes y banners inferiores, se conservó **únicamente el titular más importante**, proyectado en gran escala (`18px–22px` extra-bold en blanco nítido sobre degradado oscuro) para máxima legibilidad.

4. **Citas de Fuente Discretas al Pie**:
   - Se añadió una línea de atribución pequeña (`10.5px–11px` en monospace `#8D7A7D`, `opacity: 0.75`) debajo de cada contenedor de ilustración, cumpliendo rigurosamente con los estándares de citación académica sin restar protagonismo visual a la diapositiva.

5. **Engrandecimiento y Emblemas Inclinados de Modelos SLM (Slides 14 y 17)**:
   - **Slide 14 (Modos de Fallo)**:
     - **Microsoft Phi-4-mini**: Logotipo nítido ampliado a **`48px × 48px`** con leve inclinación (`-5°`) junto al título, y en la esquina superior derecha de la tarjeta un gran emblema/marca de agua inclinado de **`125px × 125px`** a **`-10°`** con opacidad elegante (`0.15`).
     - **Alibaba Qwen2.5-3B**: Logotipo nítido ampliado a **`50px × 50px`** con leve inclinación (`+5°`) junto al título, y en la esquina superior derecha de la tarjeta un gran emblema de corchetes de **`125px × 125px`** a **`+10°`** con opacidad elegante (`0.15`).
   - **Slide 17 (Matriz de Decisión)**:
     - En los Cuadrantes 3 y 4 se integraron emblemas de esquina grandecitos e inclinados (`95px` a `+12°` y `90px` a `-10°`), junto a logotipos de cabecera ampliados a `34px–36px`.

6. **Corrección de Cuadrante Azul de Microsoft (Slide 17)**:
   - Se corrigió la coordenada del rectángulo azul (`#00A4EF`) en el logotipo de Microsoft del Cuadrante 4 (`Phi-4-mini`), que había quedado sobrepuesta en la posición `(11, 11)` junto al amarillo en lugar de `(1, 11)`, restaurando los 4 colores de marca oficiales.

---

# Iteración 5: Simetría Estricta, Eliminación de Redundancias y Concreción Visual

## Solicitud del Usuario
1. *"En la diapositiva 5, se entiende un poco la escena, pero la parte de la torre o donde esta la usb esta un poco abstracta y como se añadio la escena el separador queda sobrepuesto `<div style="width: 2px; height: 75px; background: var(--c-border-subtle); flex-shrink: 0;"></div>`"*
2. *"En la diapositiva 08 si quedó mejor, habria que pulir un poco y cuidar detalles."*
3. *"en la dipositiva 09, habria que ver que no hayan cosas redundantes con lo nuevo que se añadio, o sea que la tabla y lo otro no digan lo mismo, en el caso de que hayan cosas, dejar las de la tabla. y trata de ser un poco mas detallista que todo quede simetrico o a mismas alturas y asi, no se si me entiendes."*

## Decisiones e Implementaciones de Diseño

1. **Diapositiva 05 · Erradicación de Separador Sobrepuesto y Portátil sobre Fondo Claro en Español**:
   - **Separador Eliminado**: Se eliminó por completo el `<div>` flotante de 75px que provocaba sobreposición con el texto de la brecha rural. En su lugar, el bloque DANE 2024 se estructuró con `grid-template-columns: auto 1fr;` y un `border-right: 2px solid var(--c-border-subtle)` nativo en la celda del 58.6%, garantizando alineación indestructible y cero solapamiento.
   - **Fondo Claro de Alto Contraste (`assets/illustration_rural_offline.svg`)**:
     - Atendiendo la observación (*"pon el portátil sobre un fondo como claro, porque el portátil oscuro sobre fondo oscuro casi no se logra ver bien"*), se sustituyó el fondo oscuro por un **fondo de estudio claro y luminoso** (degradado blanco perla a crema rosáceo `#FFFFFF` → `#EBE0E3`), con sombra suave y realista.
     - El portátil oscuro grafito, el teclado y la pantalla OLED color vino con el escudo dorado contrastan ahora con máxima nitidez y definición.
     - La **memoria USB 3.0** en metal plateado pulido y rojo resalta con total claridad en el lateral.
     - **100% en Español**: Textos legibles y precisos (*"100% AISLADO"*, *"INFERENCIA LOCAL · CERO NUBE"*, *"LoxTIC · Asistente Local Autónomo"*, *"✓ Consulta curricular resuelta"*).
     - La ilustración se integra armónicamente con la diapositiva blanca, manteniendo el banner inferior para asentar la base del contenedor.

2. **Diapositiva 08 · Máxima Simplicidad: Solo la Memoria USB**:
   - Atendiendo la solicitud directa (*"yo la haria hasta mas sencilla, dejaria solo la usb, sin tanto detalle"*), se eliminaron por completo el chasis del computador, la placa base, las pistas de circuitos y los pines de CPU.
   - En [`assets/illustration_usb_deployment.svg`](file:///c:/Users/ASUS/Desktop/Diapositivas-Cartagena/assets/illustration_usb_deployment.svg) se dejó **exclusivamente la memoria USB 3.0 SanDisk Ultra Flair**: centrada, icónica y con iluminación de estudio sobre fondo oscuro, cuerpo metálico pulido, relieve ergonómico posterior en rojo institucional, logotipo en relieve y conector Tipo A con lengüetas azules USB 3.0. Una pieza gráfica pura, limpia y sin sobrecarga visual.
   - Se mantuvieron las alturas y bordes de las tarjetas de telemetría y aislamiento (`1.9 tok/s` y `Cita Exacta & Air-Gapped`) perfectamente alineadas con el marco de la aplicación local.

3. **Diapositiva 09 · Simetría Rigurosa y Cero Redundancias**:
   - **Eliminación de Redundancia**: Se eliminó del bloque lateral la tarjeta de "CONTROL ANTI-ALUCINACIÓN / 2 Sondas Falsas", ya que duplicaba la información de la Fila 5 de la tabla (*Fuera de alcance · F1 – F2 · 2 sondas de rechazo*). La información se preservó exclusivamente en la tabla, tal como instruyó el usuario.
   - **Nuevo Contenido Complementario**: El contenedor lateral del libro se dedicó al *Corpus RAG Vectorial (339 trozos ≤ 512 palabras)* y al *Cotejo en el Aula (Citas página a página con el libro físico)*.
   - **Simetría y Alturas Idénticas**: Ambas columnas se sincronizaron con un contenedor principal de `height: 585px`. La columna izquierda cuenta con la tabla arriba y la barra de resumen (*TOTAL: 14 ÍTEMS*) abajo; la columna derecha cuenta con la tarjeta del libro arriba y una barra gemela de licencia (*LICENCIA ABIERTA · Hall & Wallace CC BY-NC-SA 3.0*) abajo, con idéntica altura (`56px`), mismo margen superior (`16px`), mismo fondo y bordes exactos, logrando una simetría visual impecable.
