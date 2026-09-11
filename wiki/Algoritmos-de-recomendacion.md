**Issue:** #6<br>
**Estado:** Propuesta para aprobación del equipo<br>
**Fecha:** 2026-09-11

## 1. Pregunta del spike

¿Qué enfoque de recomendación permite entregar recomendaciones útiles en la primera versión de Git-Wreckers, considerando que el proyecto inicia sin historial de usuarios ni valoraciones propias?

## 2. Contexto y criterio de decisión

Git-Wreckers recomendará libros, cómics y manga a partir de un catálogo que aún debe definirse en el spike de fuentes de datos (#5). El PRD exige recomendaciones personalizadas, explicación básica y un comportamiento claro para usuarios sin historial. Por tanto, el enfoque inicial debe funcionar con metadatos de obras, ser explicable y no depender de una matriz grande de valoraciones.

Se compararon los enfoques con estos criterios: datos necesarios, capacidad de resolver el arranque en frío, explicabilidad, complejidad de implementación y viabilidad para un equipo académico con un catálogo y número de usuarios iniciales desconocidos.

## 3. Enfoques investigados

### 3.1 Filtrado basado en contenido (Content-Based Filtering, CBF)

Recomienda obras parecidas a las que un usuario valoró positivamente o seleccionó. La similitud se obtiene de atributos de la obra; para este proyecto: categoría, autoría, géneros, etiquetas, sinopsis y, si existe de forma confiable, idioma y demografía objetivo. En datos textuales puede usarse TF-IDF y similitud del coseno; no es necesario un modelo de aprendizaje profundo para la primera versión.

**Datos necesarios:** metadatos normalizados de las obras y, para personalizar, al menos una preferencia, selección o valoración del usuario.

**Ventajas:** funciona incluso con pocos usuarios; permite recomendar obras nuevas que ya tengan metadatos; es fácil explicar una sugerencia mediante géneros, etiquetas o autores en común; su costo de cómputo y operación es moderado.

**Desventajas:** puede sobreespecializar las recomendaciones y mostrar obras demasiado similares; la calidad depende de que las fuentes proporcionen metadatos completos y consistentes; requiere una estrategia de respaldo cuando el usuario aún no ha interactuado.

### 3.2 Filtrado colaborativo (Collaborative Filtering, CF)

Recomienda una obra porque usuarios con comportamientos parecidos la valoraron o consumieron. Puede implementarse por vecindad usuario-usuario, obra-obra o factorización de matrices.

**Datos necesarios:** una cantidad suficiente de interacciones usuario-obra, por ejemplo valoraciones, favoritos, clics o lecturas. Los identificadores de usuario y obra deben ser estables y las interacciones deben almacenarse de forma consistente.

**Ventajas:** puede descubrir relaciones que no aparecen en los metadatos y aumentar la diversidad; no depende de que una sinopsis o etiquetas sean exhaustivas.

**Desventajas:** presenta arranque en frío para usuarios y obras nuevas; la matriz inicial será dispersa; requiere controles de privacidad y mayor monitoreo de calidad. La literatura identifica la dispersión y el arranque en frío como retos centrales de CF.

### 3.3 Recomendación híbrida

Combina CBF y CF, por ejemplo calculando ambos puntajes y aplicando una combinación ponderada. Un ejemplo gradual para Git-Wreckers sería priorizar CBF al inicio y aumentar el peso de CF solo cuando el usuario y el catálogo tengan interacciones suficientes.

**Datos necesarios:** los metadatos de CBF más el historial de interacciones de CF, además de telemetría para evaluar y ajustar los pesos.

**Ventajas:** aprovecha los puntos fuertes de ambos enfoques y puede mitigar parte del arranque en frío y la sobreespecialización. Las revisiones de sistemas híbridos señalan precisamente la escasez de datos y el arranque en frío como problemas que buscan atender.

**Desventajas:** es el enfoque con más componentes, parámetros, pruebas y mantenimiento. Si se intenta desde el inicio, añade complejidad sin que todavía exista suficiente señal colaborativa para justificarla.

## 4. Comparación

| Criterio | Basado en contenido | Colaborativo | Híbrido |
|---|---|---|---|
| Datos mínimos | Metadatos de obras y una señal de preferencia opcional | Muchas interacciones usuario-obra | Metadatos e interacciones suficientes |
| Arranque en frío | Bueno para obras; requiere selección inicial para personalizar | Débil para usuarios y obras nuevas | Mejor que CF, si CBF funciona |
| Explicabilidad | Alta: géneros, etiquetas, autor o tema compartido | Media o baja: usuarios/obras similares | Media: debe explicitar qué componente influyó |
| Diversidad | Media; riesgo de sobreespecialización | Alta cuando hay datos | Alta si se balancean componentes |
| Complejidad inicial | Baja a media | Media a alta | Alta |
| Viabilidad actual | Alta | Baja | Media como evolución, baja como primera entrega |

## 5. Decisión propuesta

Se propone **CBF como recomendador de la primera versión**, acompañado por una lista de popularidad o novedades como respaldo para usuarios sin historial. No se recomienda iniciar con CF puro ni con un híbrido completo, porque el sistema no cuenta todavía con una base de usuarios ni con interacciones suficientes.

La decisión no descarta un híbrido. La arquitectura deberá exponer el cálculo de puntajes como un módulo intercambiable, de modo que CF pueda añadirse posteriormente sin reemplazar las pantallas ni el modelo de catálogo.

## 6. Diseño mínimo viable

1. Normalizar por obra: `id`, tipo, título, autores, géneros, etiquetas, sinopsis, fuente y fecha de actualización.
2. Construir un perfil de obra con géneros, etiquetas y texto de la sinopsis; iniciar con coincidencias exactas y/o TF-IDF con similitud del coseno.
3. Construir el perfil del usuario a partir de obras valoradas positivamente. La escala de valoración se definirá antes de implementar este paso.
4. Generar las primeras *K* obras por similitud, excluir las ya valoradas y diversificar resultados por autor y género cuando sea posible.
5. Mostrar una razón breve y comprobable: por ejemplo, “porque te gustaron obras de fantasía con la etiqueta aventura”.
6. Si no hay suficientes interacciones, pedir al usuario que seleccione géneros o algunas obras de interés y mostrar una lista de popularidad o novedades identificada como no personalizada.
7. Registrar impresiones, clics, valoraciones y ocultamientos sin almacenar más datos personales de los necesarios.

## 7. Evolución a híbrido: condición de entrada

CF se evaluará cuando el equipo tenga datos suficientes y representativos. Antes de activarlo se deberá comprobar que existen interacciones distribuidas entre múltiples usuarios y obras; no basta con un número total alto concentrado en pocos elementos.

El experimento deberá comparar CBF contra una combinación ponderada `puntaje = α × CBF + (1 - α) × CF`. El valor de `α` se ajustará con un conjunto de validación, no por intuición. Se mantendrá CBF para usuarios u obras nuevos y como explicación visible de las recomendaciones.

## 8. Evaluación y criterios de salida

Antes de adoptar el enfoque en producción, el equipo deberá:

- Crear un conjunto de prueba separado de las interacciones usadas para recomendar.
- Medir Precision@K y Recall@K para recomendaciones relevantes; complementar con cobertura y diversidad del catálogo.
- Registrar una señal simple del usuario, como “útil/no útil”, y observar clics o valoraciones posteriores.
- Comparar resultados contra la línea base de popularidad; un sistema personalizado no debe adoptarse si no aporta valor medible.
- Revisar ejemplos manuales para detectar recomendaciones erróneas, sesgos por tipo de obra y ausencia de explicaciones.

## 9. Riesgos y mitigaciones

| Riesgo | Mitigación |
|---|---|
| Metadatos incompletos o inconsistentes | Normalizar fuentes, guardar procedencia y mostrar campos faltantes sin inventarlos. |
| Usuario nuevo sin historial | Selección inicial de intereses y lista de popularidad/novedades. |
| Recomendaciones demasiado repetitivas | Diversificar por autor, género o categoría y medir cobertura. |
| Pocas valoraciones para CF | Mantener CBF como base y retrasar CF hasta validar suficiente señal. |
| Datos de interacción sensibles | Minimizar datos, proteger cuentas y documentar retención y uso. |

## 10. Trabajo posterior

- #5 debe definir fuentes que incluyan metadatos utilizables y sus licencias.
- #7 debe seleccionar la tecnología para indexar texto, calcular similitud y almacenar interacciones.
- #8 deberá reflejar el módulo de recomendación y sus dependencias en la arquitectura inicial.
- Crear historias técnicas para normalización del catálogo, perfil de obra, perfil de usuario, ranking, lista de respaldo y evaluación.

## 11. Fuentes

- P. Lops, M. de Gemmis y G. Semeraro, “Content-based Recommender Systems: State of the Art and Trends”, en *Recommender Systems Handbook*, Springer, 2011. [DOI](https://doi.org/10.1007/978-0-387-85820-3_3).
- X. Su y T. M. Khoshgoftaar, “A Survey of Collaborative Filtering Techniques”, *Advances in Artificial Intelligence*, 2009. [DOI](https://doi.org/10.1155/2009/421425).
- E. Çano y M. Morisio, “Hybrid Recommender Systems: A Systematic Literature Review”, 2019. [Artículo](https://arxiv.org/abs/1901.03888).
- S. Shrestha *et al.*, “Revisiting recommender systems: an investigative survey”, *Neural Computing and Applications*, 2025. [Artículo](https://doi.org/10.1007/s00521-024-10828-5).
