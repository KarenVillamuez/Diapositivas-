# Guia de Posibilidades, Disposiciones y Uso: LHXT26 Web Presentation

> **VI Congreso Internacional de Investigacion Interdisciplinar · Cartagena 2026**  
> Documentacion tecnica y pedagogica del sistema de diapositivas web.

---

## 1. Estructura del Proyecto y Organizacion de Carpetas

Para respetar la pureza de la plantilla institucional y al mismo tiempo ofrecer todas las opciones de diseno sin sobrecargar al autor, el proyecto se divide en dos entornos:

### A. Subcarpeta `plantilla-limpia/` (Plantilla Basica 1:1)
- Ubicacion: `c:\Users\ASUS\Desktop\Diapositivas-Cartagena\plantilla-limpia\`
- Contenido: Copia literal, exacta e inalterada de la plantilla original de PowerPoint de 11 diapositivas.
- Proposito: Servir como base inmutable. Si el autor solo desea reemplazar textos en el esquema estandar del congreso (las 11 diapositivas originales), este directorio permanece intacto.

### B. Directorio Raiz `./` (Catalogo Lineal Extendido de 16 Diapositivas)
- Archivos: `index.html`, `styles.css`, `app.js`.
- Contenido: 16 diapositivas continuas, donde cada posibilidad de acomodacion (flujos por fases, matrices 2x2, tablas APA, graficos vectoriales, benchmarks comparativos, visores de algoritmo y anexos tecnicos) es una **diapositiva independiente y 100% visible**.

---

## 2. Por que Cada Opcion es una Diapositiva Independiente (PDF / PPTX)

En un entorno real de presentacion academica y para la exportacion a PDF o PowerPoint:

1. **El ponente no debe estar haciendo clics para cambiar pestanas:** Durante una exposicion en auditorio o congreso, el presentador avanza linealmente con un control remoto o teclado. No se interactua con menus complejos dentro de una lamina.
2. **Las vistas ocultas no se imprimen:** Si una acomodacion estuviera escondida detras de una pestana o un boton interactivo, al presionar `Ctrl + P` para generar el PDF o convertir a PPTX, el navegador solo imprimiria la pestana activa y descartaria todo el contenido oculto.
3. **Control total de seleccion:** Al tener cada variante como una diapositiva separada en el archivo `index.html`, el autor puede revisar todas las opciones visualmente y simplemente **eliminar las diapositivas que no vaya a utilizar**, conservando las que mejor se ajusten a los datos de su articulo.

---

## 3. Catalogo de las 16 Diapositivas del Deck Extendido

| Diapositiva | Identificador | Categoria / Titulo | Descripcion y Proposito |
| :--- | :--- | :--- | :--- |
| **01** | `#slide-1` | Portada Principal | Fondo vinotinto institucional (`#460811`), Torre del Reloj, titulo en espanol e ingles, autores y logos universitarios. |
| **02** | `#slide-2` | Resumen | Resumen ejecutivo continuo y linea de palabras clave normalizadas. |
| **03** | `#slide-3` | Estructura del Articulo | Agenda de la ponencia (01 Introduccion, 02 Metodologia, 03 Resultados, 04 Discusion, 05 Anexos, 06 Referencias). |
| **04** | `#slide-4` | Separador 01 Introduccion | Lamina de transicion con fondo vinotinto. |
| **05** | `#slide-5` | 01 · Planteamiento del Problema | Descripcion del problema de investigacion y contexto tematico. |
| **06** | `#slide-6` | 02 · Metodologia (Acomodacion A) | Estilo original de la plantilla: 2 bloques paralelos (Enfoque Metodologico + Fases del Procedimiento). |
| **07** | `#slide-7` | 02 · Metodologia (Acomodacion B) | **Pipeline Secuencial de 4 Fases:** 4 tarjetas continuas con numero de fase, estado formal (Completado, En Proceso, Planificado), descripcion, herramienta y producto de salida. |
| **08** | `#slide-8` | 02 · Metodologia (Acomodacion C) | **Matriz Analitica Cuadruple 2x2:** 4 cuadrantes con acentos de color para Variables Independientes (Q1), Variables Dependientes (Q2), Equipamiento (Q3) y Control de Validez (Q4). |
| **09** | `#slide-9` | 03 · Resultados (Acomodacion A) | **Tabla Formal APA 7.ª Edicion:** Lineas horizontales limpias, filas alternadas en rosa palido institucional, sin lineas verticales invasivas y con badge de sintesis estadistica al pie. |
| **10** | `#slide-10` | 03 · Resultados (Acomodacion B) | **Figura Vectorial SVG & Hallazgos:** Grafico de barras vectorial nativo de alta resolucion con leyenda formal y columna derecha con 3 metricas de impacto (`96.8%`, `-65.5%`, `n = 1,420`). |
| **11** | `#slide-11` | 03 · Resultados (Acomodacion C) | **Benchmark Comparativo Directo:** Dos tarjetas enfrentadas (Estado del Arte Tradicional vs. Propuesta LHXT26 de este estudio) con especificaciones tecnicas y badge de significancia. |
| **12** | `#slide-12` | 03 · Resultados (Acomodacion D) | **Algoritmo TIC & Gran Hallazgo:** Columna izquierda con visor de codigo estructurado monoespaciado (Python / PyTorch) y columna derecha con tarjeta hero monumental de hallazgo clave y enlace DOI. |
| **13** | `#slide-13` | 04 · Discusion y Conclusiones | 3 columnas tematicas (Discusion, Limitaciones, Conclusiones) y banner inferior de agradecimientos a entidades financiadoras. |
| **14** | `#slide-14` | 05 · Anexos Tecnicos (Lamina Formal) | Diapositiva completa dedicada a la formalizacion matematica (funcion objetivo penalizada) y tabla muestral con estadisticos ANOVA y Shapiro-Wilk. |
| **15** | `#slide-15` | 06 · Referencias Bibliograficas | Lista formal de citas en formato APA 7.ª con sangria y formato editorial academico. |
| **16** | `#slide-16` | Cierre Institucional | Titulo monumental de agradecimiento, correo institucional, boton de preguntas, codigo QR de la ponencia y logos oficiales. |

---

## 4. Como Personalizar su Ponencia

Para armar su presentacion final:

1. **Abra `index.html` en su editor de codigo.**
2. **Seleccione la acomodacion de Metodologia que prefiera:**
   - Si su estudio tiene 2 ejes basicos: conserve la **Diapositiva 6** y borre las diapositivas 7 y 8.
   - Si su estudio tiene etapas secuenciales: conserve la **Diapositiva 7** (Pipeline) y borre la 6 y la 8.
   - Si su estudio tiene matrices o taxonomias: conserve la **Diapositiva 8** (Matriz 2x2) y borre la 6 y la 7.
3. **Seleccione la acomodacion de Resultados que prefiera:**
   - Si presenta tablas experimentales: conserve la **Diapositiva 9** (Tabla APA).
   - Si presenta graficos comparativos: conserve la **Diapositiva 10** (Grafico SVG).
   - Si compara directamente contra modelos previos: conserve la **Diapositiva 11** (Benchmark).
   - Si presenta aportes computacionales o algoritmos: conserve la **Diapositiva 12** (Visor de Codigo).
   *(Tambien puede conservar dos o tres de ellas si su articulo cuenta con tablas, graficos y codigo).*
4. **Anexos Tecnicos:** Si el jurado requiere verificar demostraciones matematicas o tablas muestrales, conserve la **Diapositiva 14**. Si no las requiere, simplemente elimine ese bloque `<section>`.

---

## 5. Como Exportar a PDF y PPTX

La presentacion cuenta con reglas CSS `@media print` calibradas para generar paginas vectoriales perfectas:

1. Abra la presentacion en Google Chrome, Microsoft Edge o cualquier navegador moderno (`http://localhost:8085/index.html`).
2. Presione **`Ctrl + P`** o haga clic en el boton **Exportar PDF** de la barra de herramientas.
3. En la ventana de impresion:
   - **Destino:** Guardar como PDF.
   - **Disposicion:** Horizontal (Landscape).
   - **Margenes:** Ninguno (None).
   - **Graficos de fondo:** Activado (Checked).
4. Haga clic en **Guardar**.
5. Obtendra un documento PDF de alta fidelidad donde cada diapositiva ocupa exactamente una pagina panoramica 16:9 con todas las fuentes vectoriales nitidas.
6. **Para pasar a PPTX:** Puede importar el PDF resultante directamente en PowerPoint (`Insertar > Objeto` o mediante herramientas directas de conversion PDF a PPTX de Adobe o convertidores vectoriales), manteniendo la proporcion 16:9 exacta.

---

## 6. Atajos de Teclado del Ponente

| Tecla | Funcion |
| :--- | :--- |
| **`Flecha Derecha` / `Espacio` / `PageDown`** | Avanzar a la siguiente diapositiva. |
| **`Flecha Izquierda` / `Backspace` / `PageUp`** | Retroceder a la diapositiva anterior. |
| **`Home` / `End`** | Ir a la primera diapositiva (Portada) o a la ultima (Cierre). |
| **`L`** | Activar o desactivar el Puntero Laser virtual en pantalla. |
| **`O`** | Abrir o cerrar la Cuadricula de miniaturas de todas las diapositivas. |
| **`F`** | Activar o desactivar Pantalla Completa. |
| **`T`** | Pausar o reanudar el cronometro de ponencia (15 minutos). Doble clic en el cronometro lo reinicia a 15:00. |
| **`H`** | Ocultar o mostrar la barra de herramientas inferior. |
| **`Esc`** | Cerrar el visor de cuadricula. |
| **`Ctrl + P`** | Abrir el dialogo de exportacion a PDF. |
