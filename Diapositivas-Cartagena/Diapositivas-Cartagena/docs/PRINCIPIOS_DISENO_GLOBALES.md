# Principios Globales y Filosofía de Diseño
## VI Congreso Internacional de Investigación Interdisciplinar · Cartagena 2026 (LHXT26)

Este documento condensa los principios rectores, criterios estéticos y decisiones de diseño transversales adoptadas durante la creación y refinamiento de las 20 diapositivas de la presentación oficial. A diferencia de la bitácora diapositiva por diapositiva ([DECISIONES_DISENO.md](file:///c:/Users/ASUS/Desktop/Diapositivas-Cartagena/docs/DECISIONES_DISENO.md)), este texto establece el **manifiesto de diseño global** que rige toda la identidad visual del proyecto.

---

## 1. El Principio Óptico del Auditorio (Legibilidad a 15–20 Metros)

Toda decisión visual se evaluó bajo las condiciones reales de una sala de conferencias con proyector de alta potencia y luz ambiental, donde la audiencia se ubica entre 10 y 25 metros de distancia:

* **Erradicación Total del Microtexto**:
  * Cualquier elemento tipográfico inferior a `22px` se convierte en una mancha ilegible a la distancia y compite con la voz del ponente.
  * **Reglas de Escala Tipográfica**:
    * **Preguntas Gancho y Títulos de Cabecera**: `38px` a `46px` (extra-bold, peso `800`–`900`).
    * **Títulos de Tarjetas y Secciones**: `28px` a `34px`.
    * **Texto de Lectura y Explicaciones**: Mínimo `24px` a `27px` (semi-bold `600`, `line-height: 1.35`–`1.45`).
    * **Cifras Métricas Monumentales**: `52px` a `68px` en tipografía monoespaciada extra-bold.
* **Prohibición de Texto Claro sobre Fondo Oscuro en el Cuerpo**:
  * Las cajas o tarjetas oscuras con letras blancas pierden contraste de forma dramática en proyectores en salones iluminados.
  * **Regla**: El contenido sustancial de la ponencia siempre se monta sobre fondos claros (`#FFFFFF`, `#FAF5F5` o `#FAF0F2`) con texto en negro carbón profundo (`#110103`) o vinotinto oscuro (`#2C0509`).
  * Los fondos oscuros (*Hero Dark* en vinotinto profundo `--c-wine-dark`) se reservan con exclusividad a la Portada (Slide 01) y a los Separadores de Capítulo (Slides 04, 06, 11 y 16), donde solo existe un título colosal y la silueta arquitectónica.
* **El Remate Editorial de Doble Regla (Alto Impacto sin Fondo Oscuro)**:
  * Para enfatizar una conclusión cumbre o la Tesis Defendida sin recurrir a fondos oscuros opacos, se adoptó el estándar de la **franja clara delimitada por dos reglas horizontales vinotinto de 3.5px** (`border-top: 3.5px solid var(--c-wine-primary); border-bottom: 3.5px solid var(--c-wine-primary)` sobre fondo `#FAF5F5`).

---

## 2. Geometría y Composición (Estilo Suizo 100% Plano y Ortogonal)

* **Tolerancia Cero a las Esquinas Redondeadas (`border-radius: 0;`)**:
  * Las curvas o bordes redondeados introducen una estética informal o de aplicación web genérica que desentona con el rigor académico.
  * Toda la interfaz mantiene una geometría ortogonal estricta con **ángulos a 90°** en contenedores, tarjetas, marcos de códigos QR, insignias de estado y barras de porcentaje.
* **Prohibición de "Cuadros dentro de Cuadros" (Anti-Nidación)**:
  * Se eliminó el anidamiento excesivo de tarjetas dentro de tarjetas con bordes repetitivos (`.flow-card`, `.card-key-takeaway`).
  * Se sustituyó por **retículas tipográficas abiertas**, donde los datos y frases flotan sobre el lienzo claro delimitados únicamente por espinazos verticales delgados de 2px (`#E2D2D2` / `#D8B8BE`), barras laterales de 6–8px de acento cromático o sutiles filetes de 1.5px.
* **Erradicación del Espacio Muerto y del "Top-Heavy"**:
  * Se rechazó la acumulación del contenido en la parte superior que dejaba vacíos estériles de 200–300px al pie del lienzo.
  * La composición utiliza una distribución vertical completa (**`justify-content: space-between`** en contenedores de `height: 720px`), extendiendo las retículas panorámicas a lo largo de los 1700px útiles en formato 16:9.
* **Alineación Geométrica Continua**:
  * Las líneas divisorias verticales, los anchos de columnas de métricas (estandarizados por ejemplo en `290px`) y los márgenes perimetrales guardan coincidencia exacta entre filas sucesivas, eliminando cualquier desfase visual.
* **Respiración y Holgura de Márgenes (Paddings Generosos)**:
  * Ninguna cifra, porcentaje o gráfica debe colisionar con los bordes de su contenedor. Se garantiza un colchón de aire perimetral mínimo de `24px` a `36px` alrededor de cada bloque.

---

## 3. Síntesis Textual y Narrativa Oral ("Decir lo Justo, sin Relleno")

* **Diseño para Exposición en Dúo (Frases Gancho)**:
  * Las diapositivas no son un documento para lectura individual, sino el soporte de una narrativa oral coordinada entre dos investigadores.
  * Cada lámina cuenta con una **Pregunta de Cabecera o Tesis Directa** (`.s-lead-question`) que conecta la idea previa con la actual, brindando continuidad fluida sin saltos temáticos.
* **Eliminación Radical de la Redundancia ("Decir mucho y a la vez nada")**:
  * Se erradicaron los párrafos explicativos densos, subtítulos poéticos, notas al pie que duplicaban conceptos y rótulos innecesarios como *"Figura X del paper"*.
  * Si una gráfica o número ya expone la evidencia, el texto acompañante se sintetiza en **1 sola frase concisa con anclaje factual comprobable**.
* **Negritas de Escaneo Rápido (Lectura en 1 Segundo)**:
  * Uso selectivo y quirúrgico de `<strong>` en términos clave (*"falso empate"*, *"sin conexión a internet"*, *"sin profesor: admitir no saber"*), permitiendo que la audiencia asimile el mensaje en un parpadeo mientras sigue la voz de los ponentes.
* **Descarte Total de Listas de Viñetas Convencionales (`ul/li`)**:
  * Prohibición de listas tradicionales con puntos negros, que generan sensación de borrador o texto amontonado. Toda la información se estructura mediante filas horizontales, tarjetas paralelas, dípticos o matrices 2×2.

---

## 4. Tratamiento de Gráficas y Evidencia Empírica

* **El Gráfico Científico como Héroe Central**:
  * Cuando una diapositiva presenta datos cuantitativos clave (curvas de distribución, slopegraph de desacuerdo docente o gráfico de dispersión de semillas), **la gráfica ocupa el foco principal del lienzo** con amplias dimensiones (`viewBox` generosos).
  * Se retiran leyendas decorativas y cajas periféricas que encajonan la visualización, permitiendo que la figura respire con autonomía.
* **Atenuación de Ruido y Jerarquía de Enfoque**:
  * En visualizaciones con múltiples trazas (por ejemplo, las 10 respuestas del slopegraph), las trayectorias no concluyentes se atenúan en grises tenues (`#D8CBCD` al 40% de opacidad) para que las discrepancias críticas resalten de inmediato en líneas gruesas de 5.5px a 6.5px en colores institucionales.
* **Barras de Porcentajes Panorámicas vs. Tablas Saturadas**:
  * En lugar de tablas numéricas complejas, los porcentajes se representan mediante barras horizontales de **30px de espesor** con cifras monoespaciadas de **`40px`**, permitiendo comparaciones asimétricas instantáneas (p. ej., 85.7% vs. 28.6%).
* **Tangibilidad Mediante Capturas Reales**:
  * En lugar de depender exclusivamente de esquemas teóricos de cajas, se reservó una diapositiva completa (Slide 08) para exhibir **capturas reales de la interfaz del software funcionando offline**, garantizando credibilidad técnica y evidencia de campo.

---

## 5. Código Cromático Semántico e Institucional

Los colores nunca se emplean como simple adorno; cada matiz cumple una función semántica precisa:

* **Vinotinto Institucional (`#460811` / `var(--c-wine-primary)`)**:
  * Representa la identidad de la *Institución Universitaria Colegio Mayor del Cauca*, el rigor metodológico, la Tesis Defendida y las condiciones de apego a la verdad.
* **Rojo Carmesí de Acción (`#C9101B` / `var(--c-red-accent)`)**:
  * Señala alertas críticas, modos de fallo asimétricos, riesgo de alucinación, discrepancia docente severa y etiquetas de estado en vivo (`EN VIVO`).
* **Dorado / Ámbar (`#B38600` / `var(--c-gold)`)**:
  * Utilizado para advertencias de cautela, el resultado del falso empate estadístico de Wilcoxon y la métrica de coincidencia cero en aula (`0 / 10`).
* **Gris Neutro y Pizarra (`#4A3B3D` / `#D8CBCD`)**:
  * Proporciona la base textual secundaria, espinazos de alineación y atenuación de datos de referencia.

---

## 6. Rigor Académico y Cero Distracciones

* **Odio Absoluto a los Emojis**:
  * Prohibición absoluta de emojis o iconos infantiles tanto en el HTML como en la documentación. Se emplean exclusivamente caracteres tipográficos formales (`★`, `·`, `&`) o etiquetas monoespaciadas solemnes.
* **Cero Interactividad Innecesaria**:
  * Descarte de pestañas clicables, efectos de acordeón o botones interactivos diseñados para web. La presentación responde exclusivamente a las teclas de flecha del teclado, asegurando estabilidad técnica total en la tarima y compatibilidad perfecta al exportar a PDF.
* **Rigor Ortográfico Integral**:
  * Revisión exhaustiva de tildes y grafías formales en todo el texto en español (*Investigación*, *Informática*, *Metodología*, *Autónomo*, *Diálogo*, *Muñoz-Gómez*, *Hoyos-Cerón*, *Vélez*, *Álvarez*, etc.).
  * Formato formal de referencias científicas bajo estándar APA 7.ª edición.

---

## 7. Arquitectura Técnica y Modularidad

* **Modularidad Estricta de Código (1 Slide = 1 Archivo)**:
  * Separación radical del código monolítico original en 20 archivos independientes (`slides/slide_01.html` a `slides/slide_20.html`).
  * Ensamblaje automatizado y reproducible mediante el compilador Python [scripts/build.py](file:///c:/Users/ASUS/Desktop/Diapositivas-Cartagena/scripts/build.py), produciendo un [index.html](file:///c:/Users/ASUS/Desktop/Diapositivas-Cartagena/index.html) unificado y libre de conflictos.
* **Organización Limpia del Repositorio**:
  * Distribución clara en carpetas:
    * `slides/`: Fuentes modulares HTML de las 20 diapositivas.
    * `scripts/`: Scripts de compilación, generación de opciones y verificación automatizada en Playwright.
    * `assets/`: Logotipos institucionales, capturas de pantalla de la aplicación y figuras científicas.
    * `docs/`: Documentación de diseño, bitácoras de decisiones y artículos base.
* **Metodología de Validación Visual Iterativa**:
  * Ninguna diapositiva se dio por terminada sin antes generar opciones visuales comparativas y capturar la vista real proyectada en servidor local (`http://localhost:8085/`), verificando su equilibrio estético antes de la aprobación definitiva.
