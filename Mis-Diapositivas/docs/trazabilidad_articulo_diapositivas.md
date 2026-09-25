# Trazabilidad entre artículo y diapositivas

## Fuente y criterio de revisión

La fuente canónica es `Articulo_[ID]_Hoyos_Munoz_Caiza.docx`. El documento no se modificó. La presentación se revisó para que no afirme resultados que el estudio no midió, en particular aprendizaje, intervención en aula, equivalencia entre modelos o una recomendación de despliegue.

## Correspondencia de las 20 diapositivas

| Diapositiva | Función en la ponencia | Correspondencia con el artículo | Estado |
|---|---|---|---|
| 1 | Título, autores y afiliación | Título español e inglés, tres autores y afiliación | Coincide |
| 2 | Resumen ejecutivo | Brecha de conectividad, ejecución desde USB y coincidencia de 0.795 | Coincide con cautela |
| 3 | Ruta de la ponencia | Contexto, metodología, resultados, discusión y conclusiones | Coincide |
| 4 | Separador de contexto | Introducción | Coincide |
| 5 | Problema y preguntas | Conectividad rural, dos modelos, equipo sin GPU y alcance del evaluador | Coincide |
| 6 | Separador metodológico | Metodología | Coincide |
| 7 | Flujo RAG | RRF 0.60/0.40, BM25, recuperación densa, reordenamiento e inferencia local | Corregida |
| 8 | Demostración técnica | USB, interfaz local, Core i5, 8 GB de RAM y velocidades observadas | Corregida |
| 9 | Banco de preguntas y corpus | College ESL Writers, 299 páginas, 12 preguntas de contenido y 2 sondas | Corregida |
| 10 | Diseño experimental | 196 combinaciones base, 140 ejecuciones adicionales, siete configuraciones y cuatro semillas | Corregida |
| 11 | Separador de resultados | Coincidencia de 0.795, variación entre semillas y piloto docente | Corregida |
| 12 | Composición del puntaje | Pesos 0.40/0.40/0.20, transformación de cosenos y rama de negativa | Corregida |
| 13 | Comparación entre modelos | 0.8030 frente a 0.8010, W = 31.0, p = 0.569, dispersión interna 0.037 | Corregida |
| 14 | Respuestas sin respaldo y falsos rechazos | 4/14, 12/14, 0/84 y 6/84, según modelo | Corregida |
| 15 | Valoración docente | Diez respuestas, cuatro coincidencias de uso, kappa = -0.429 y asociaciones con el indicador | Corregida |
| 16 | Separador de discusión | Alcance del evaluador, patrones de fallo y trabajo posterior | Corregida |
| 17 | Implicación metodológica | Análisis por componentes, rechazos correctos y falsos rechazos | Corregida |
| 18 | Conclusiones | Factibilidad en el equipo evaluado, variación entre semillas y piloto docente | Coincide con cautela |
| 19 | Fuentes esenciales | Se retiró una referencia ausente del artículo y se añadió el corpus utilizado | Corregida |
| 20 | Cierre y acceso | Autores, agradecimientos, correos institucionales y repositorio | Corregida |

## Refuerzos ya integrados

- **Alcance del diseño.** La diapositiva 10 incorpora una franja que indica laboratorio, ausencia de estudiantes y ausencia de medición de aprendizaje.
- **Relación entre métricas.** La diapositiva 13 incorpora rho = -0.273 para Phi y rho = -0.066 para Qwen, junto con la relación entre `cfg_eval_full` y cobertura de palabras clave.
- **Límites de generalización.** La diapositiva 18 incorpora el alcance condensado: un libro, 14 preguntas, cuatro semillas, un equipo y sin estudiantes.

## Contenido que conviene mantener para la explicación oral

Estos elementos aparecen en el artículo, pero todavía no tienen una visual o un rótulo suficientemente directo en la presentación.

1. **Descomposición observada del puntaje por pregunta.** La diapositiva 12 explica la fórmula, pero no muestra los datos de la Figura 2. Conviene explicar que puntuaciones próximas pueden provenir de combinaciones diferentes de `grounding`, `relevance` y longitud.

3. **Activaciones de la rama de negativa.** La fórmula muestra el valor constante de 0.80, pero falta indicar su frecuencia: 4 de 98 ejecuciones en Phi y 18 de 98 en Qwen. Este dato conecta la lógica del código con los patrones de fallo.

3. **Diseño exacto del piloto docente.** La diapositiva 15 ya muestra los resultados, pero conviene decir que provienen de cinco preguntas, diez respuestas, dos docentes ciegos y una escala de 1 a 5. Esto evita interpretar el gráfico como una evaluación de aula.

4. **Reproducción de la ecuación.** El artículo informa que al recomputar `cfg_eval_full`, la diferencia máxima frente al puntaje almacenado fue menor que 0.001. Es un resultado técnico útil para sostener la trazabilidad del benchmark, aunque puede permanecer como nota si el tiempo es limitado.

## Elementos que no deben presentarse como resultados

- No se debe afirmar que el tutor mejora aprendizaje, comprensión o desempeño estudiantil.
- No se debe presentar la ejecución local como una validación de despliegue en aula.
- No se debe afirmar equivalencia, igualdad o superioridad estable entre Phi y Qwen.
- No se debe usar la velocidad observada para generalizar a otros equipos.
- No se debe presentar el piloto docente como calibración suficiente del evaluador.

## Prioridad para una ponencia de 20 diapositivas

La presentación conserva 20 diapositivas. Los puntos pendientes se explican oralmente; la frecuencia de activaciones puede mencionarse en la diapositiva 14 y la reproducción de la ecuación puede quedar como nota metodológica o en el repositorio.
