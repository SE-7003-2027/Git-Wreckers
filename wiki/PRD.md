**Versión:** 1.0<br>
**Estado:** Propuesto<br>
**Última actualización:** 2026-09-11<br>
**Responsable:** Equipo Git Wreckers

## 1. Resumen

Git-Wreckers es una aplicación web que centraliza información de libros, cómics y manga para ayudar a las personas a descubrir obras de su interés y conocer si existe información de disponibilidad en México. Las recomendaciones se generarán a partir de las características de las obras y de las preferencias y valoraciones del usuario.

## 2. Problema y oportunidad

La oferta de libros, cómics y manga es amplia y la información se encuentra distribuida en distintas fuentes. Esto dificulta comparar obras, descubrir contenido nuevo y saber qué opciones están relacionadas con México. El sistema ofrecerá un punto de consulta único y recomendaciones personalizadas, sin convertirse en una tienda ni sustituir a las fuentes originales.

## 3. Objetivos y métricas

### Objetivos

- Permitir consultar y buscar obras de las tres categorías.
- Ayudar a descubrir obras mediante exploración y recomendaciones.
- Aprovechar las valoraciones para mejorar la relevancia de las recomendaciones.
- Mostrar la fuente y la fecha de actualización de la información cuando sea posible.

### Indicadores de éxito

- Al menos 90% de las búsquedas de prueba devuelven resultados o un mensaje claro de “sin resultados”.
- Una búsqueda o consulta responde en un máximo de 3 segundos en condiciones normales, excluyendo caídas de fuentes externas.
- El 100% de las recomendaciones mostradas incluye la obra y la razón o características que la relacionan con el usuario, cuando esa información esté disponible.
- Se registran usuarios, valoraciones y consultas para evaluar adopción y uso.

## 4. Usuarios y casos de uso

### Usuario visitante

Puede explorar y buscar obras, consultar sus datos y revisar la información de disponibilidad. No puede guardar valoraciones ni recibir recomendaciones basadas en su historial.

### Usuario registrado

Puede iniciar sesión, valorar obras y consultar recomendaciones personalizadas basadas en sus preferencias e historial.

### Administrador o responsable de datos

Rol técnico u operativo que supervisa la actualización de fuentes y la calidad de los datos. Este rol queda fuera del flujo principal de la primera versión y se detallará posteriormente.

## 5. Alcance

### Incluye

- Aplicación web responsive.
- Registro, inicio y cierre de sesión.
- Búsqueda por título y, cuando los datos lo permitan, autor, género, categoría y etiquetas.
- Filtros y ordenamiento para explorar resultados.
- Ficha de cada obra con título, tipo, autoría, descripción, género/etiquetas, imagen y fuente cuando estén disponibles.
- Valoración de una obra por usuario registrado.
- Historial de valoraciones del usuario.
- Recomendaciones personalizadas y explicación básica de su relación.
- Información de disponibilidad o enlaces de consulta para México cuando la fuente lo proporcione.


## 6. Requisitos funcionales

Cada requisito es verificable y debe implementarse sin depender de una fuente única.

### RF01 - Registro

El sistema deberá permitir crear una cuenta con los datos definidos por el equipo, validar los campos obligatorios y rechazar un correo ya registrado.

### RF02 - Autenticación

El sistema deberá permitir iniciar y cerrar sesión, informar credenciales inválidas sin revelar cuál dato falló y restringir las funciones privadas a usuarios autenticados.

### RF03 - Búsqueda

El sistema deberá buscar obras por texto y mostrar resultados paginados o con carga progresiva. Cada resultado deberá indicar título y tipo de obra como mínimo.

### RF04 - Filtrado y exploración

El sistema deberá permitir explorar obras sin escribir una consulta y aplicar filtros disponibles, conservando una indicación clara de los filtros activos.

### RF05 - Detalle de obra

El sistema deberá mostrar una ficha de detalle y diferenciar los datos faltantes de los datos confirmados. La ficha deberá identificar la fuente de información.

### RF06 - Disponibilidad en México

Cuando exista información de una fuente configurada, el sistema deberá mostrarla junto con su fuente y fecha de consulta; si no existe, deberá mostrar “información no disponible” y no inferir disponibilidad.

### RF07 - Valoración

Un usuario autenticado deberá poder asignar una valoración dentro de la escala definida por el equipo, modificarla y verla asociada a la obra. Solo deberá existir una valoración vigente por usuario y obra.

### RF08 - Historial

El sistema deberá permitir al usuario consultar sus obras valoradas y la fecha de su última valoración.

### RF09 - Recomendaciones

El sistema deberá generar una lista de recomendaciones considerando, cuando existan, valoraciones, preferencias, categorías, géneros, autores o etiquetas. Cada recomendación deberá excluir obras ya valoradas por el usuario o indicarlo claramente.

### RF10 - Estados y errores

El sistema deberá mostrar estados diferenciados para carga, ausencia de resultados, error de conexión y fuente no disponible, ofreciendo reintentar cuando corresponda.

### RF11 - Privacidad de cuenta

El sistema deberá permitir consultar y eliminar las valoraciones e información de cuenta conforme a las reglas de privacidad que defina el equipo.

## 7. Requisitos no funcionales

- **RNF01 Usabilidad:** los flujos de búsqueda, detalle, valoración y recomendaciones deberán ser comprensibles en una interfaz responsive.
- **RNF02 Rendimiento:** el 95% de las búsquedas deberá responder en hasta 3 segundos bajo la carga objetivo definida por el equipo.
- **RNF03 Seguridad:** las contraseñas no deberán almacenarse en texto plano; las sesiones y datos privados deberán protegerse contra acceso no autorizado.
- **RNF04 Disponibilidad y resiliencia:** una falla de una fuente externa no deberá impedir consultar datos almacenados de otras fuentes ni romper la interfaz.
- **RNF05 Accesibilidad:** la interfaz deberá usar HTML semántico, navegación por teclado, contraste suficiente y textos alternativos para imágenes relevantes.
- **RNF06 Mantenibilidad:** requisitos, decisiones técnicas e integraciones deberán documentarse; el código deberá contar con pruebas para los flujos principales.
- **RNF07 Escalabilidad:** la integración de una nueva fuente deberá poder realizarse mediante un adaptador sin reescribir la lógica de recomendaciones.
- **RNF08 Observabilidad:** deberán registrarse errores técnicos y tiempos de respuesta sin almacenar contraseñas ni datos sensibles innecesarios.

## 8. Reglas de negocio y supuestos

- Una obra puede pertenecer a libro, cómic o manga; la categoría debe mostrarse explícitamente.
- Los datos de fuentes externas pueden estar incompletos, duplicados o desactualizados y deberán normalizarse antes de mostrarse.
- La disponibilidad en México significa únicamente que una fuente reporta información relacionada con México; no constituye una garantía de inventario.
- Las recomendaciones deben poder explicar, al menos de forma básica, qué preferencia o característica las motivó.
- Para un usuario sin valoraciones suficientes se mostrará una lista general o de obras populares, claramente identificada como no personalizada.
- La escala de valoración, la retención de cuenta y la fuente inicial de datos son decisiones pendientes del equipo y deberán registrarse antes de implementar los módulos correspondientes.

## 9. Historias de usuario y criterios de aceptación

### HU01 - Buscar contenido

Como visitante, quiero buscar libros, cómics o manga para encontrar obras de mi interés.

**Criterios:** dado un término válido, se muestran coincidencias con título y tipo; ante cero coincidencias se muestra un mensaje claro; ante un error de fuente se muestra el estado de error sin perder la consulta.

### HU02 - Consultar información

Como visitante, quiero consultar la ficha de una obra para conocer sus características y su disponibilidad en México.

**Criterios:** la ficha muestra los campos disponibles, distingue campos faltantes, identifica la fuente y muestra disponibilidad solo cuando está respaldada por datos.

### HU03 - Valorar contenido

Como usuario registrado, quiero valorar una obra para expresar mi opinión y mejorar mis recomendaciones.

**Criterios:** un visitante recibe una indicación para iniciar sesión; un usuario autenticado puede guardar y modificar una valoración; no se crean duplicados para la misma obra.

### HU04 - Recibir recomendaciones

Como usuario registrado, quiero recibir recomendaciones basadas en mis intereses para descubrir contenido nuevo.

**Criterios:** se muestra una lista; cada elemento incluye una razón o característica relacionada; si no hay historial suficiente se muestra una lista general y una indicación para valorar obras.

### HU05 - Explorar contenido

Como visitante, quiero explorar obras por categoría y filtros para descubrir contenido sin conocer un título.

**Criterios:** se puede iniciar la exploración sin consulta; los filtros activos son visibles; quitar filtros actualiza los resultados.

## 10. Dependencias, restricciones y riesgos

Las dependencias principales son la selección de tecnologías, una fuente de datos con permisos de uso, límites de APIs y la definición de disponibilidad para México. Los riesgos son cambios de API, datos incompletos, baja cantidad inicial de valoraciones y complejidad del recomendador. Mitigaciones: adaptadores por fuente, caché y manejo de fallos, datos de respaldo y comenzar con recomendación basada en contenido.

## 11. Trazabilidad y definición de terminado

Cada requisito deberá vincularse con una issue o historia de usuario y sus pruebas. Una funcionalidad se considerará terminada cuando esté implementada, probada, documentada, revisada por otro integrante y pueda demostrarse con sus criterios de aceptación.

## 12. Pendientes

- Seleccionar fuente(s) de datos y confirmar sus licencias y límites.
- Definir escala de valoración y carga objetivo.
- Seleccionar algoritmo inicial de recomendación.
- Definir políticas de privacidad y recuperación de cuenta.
- Desglosar las historias en issues técnicas y priorizarlas en el backlog.

## 13. Historial del documento

| Versión | Fecha | Cambios |
|---|---|---|
| 1.0 | 2026-09-11 | Primera versión formal con alcance, requisitos verificables, reglas de negocio, criterios de aceptación y pendientes. |
