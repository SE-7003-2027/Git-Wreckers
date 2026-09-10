# PRD - Product Requirements Document


## 1. Descripción del producto

Git-Wreckers es un sistema web de recomendación de libros, cómics y
manga disponibles en México.

El sistema busca ayudar a los usuarios a descubrir contenido que pueda
ser de su interés a partir de sus preferencias, búsquedas y
valoraciones.

La plataforma reunirá información de diferentes fuentes para mostrar
contenido disponible para los usuarios y facilitar su exploración.

## 2. Problema

Encontrar nuevos libros, cómics o manga puede ser complicado debido a la
gran cantidad de contenido disponible y a que la información puede
encontrarse distribuida entre diferentes plataformas.

El proyecto busca ofrecer una forma centralizada de explorar este
contenido y obtener recomendaciones de acuerdo con los intereses de cada
usuario.

## 3. Objetivo

Desarrollar una aplicación web que permita:

- Consultar información sobre libros, cómics y manga.
- Buscar contenido de interés.
- Explorar contenido por diferentes características.
- Registrar y consultar valoraciones de los usuarios.
- Generar recomendaciones personalizadas.
- Identificar contenido disponible en México.

## 4. Usuarios objetivo

El sistema está dirigido principalmente a personas interesadas en:

- Libros.
- Cómics.
- Manga.

Los usuarios podrán utilizar la plataforma para descubrir contenido
nuevo y recibir recomendaciones basadas en sus intereses.

## 5. Alcance

### 5.1 Incluye

El proyecto contempla inicialmente:

- Aplicación web.
- Registro e inicio de sesión de usuarios.
- Consulta de información sobre libros, cómics y manga.
- Búsqueda de contenido.
- Visualización de información de cada obra.
- Valoración de contenido por parte de los usuarios.
- Sistema de recomendaciones.
- Consulta de disponibilidad o información relacionada con México.
- Integración con fuentes de datos externas cuando sea necesario.

### 5.2 No incluye

Para la primera versión del proyecto no se contempla:

- Venta directa de libros, cómics o manga.
- Procesamiento de pagos.
- Distribución física de contenido.
- Creación de una tienda en línea.
- Sustituir las plataformas originales que proporcionan el contenido.

## 6. Requisitos funcionales

### RF01 - Registro de usuario

El sistema deberá permitir que un usuario cree una cuenta.

### RF02 - Inicio de sesión

El sistema deberá permitir que un usuario registrado inicie sesión.

### RF03 - Búsqueda

El sistema deberá permitir buscar libros, cómics y manga mediante
diferentes criterios.

### RF04 - Consulta de información

El sistema deberá mostrar información relevante de cada contenido.

### RF05 - Valoración

El sistema deberá permitir que los usuarios registrados valoren el
contenido.

### RF06 - Recomendaciones

El sistema deberá generar recomendaciones de contenido tomando en cuenta
la información disponible y las preferencias o valoraciones del usuario.

### RF07 - Exploración

El sistema deberá permitir explorar contenido sin necesidad de realizar
una búsqueda específica.

### RF08 - Disponibilidad en México

El sistema deberá proporcionar información relacionada con la
disponibilidad del contenido en México cuando dicha información se
encuentre disponible.

## 7. Requisitos no funcionales

### RNF01 - Usabilidad

La interfaz deberá ser sencilla de utilizar y permitir que los usuarios
encuentren contenido sin dificultad.

### RNF02 - Rendimiento

Las búsquedas y consultas deberán responder en un tiempo razonable.

### RNF03 - Seguridad

La información de los usuarios deberá manejarse de forma segura.

### RNF04 - Disponibilidad

El sistema deberá estar disponible para los usuarios durante el
funcionamiento normal de la aplicación.

### RNF05 - Mantenibilidad

El código deberá mantenerse organizado y documentado para facilitar
futuras modificaciones.

### RNF06 - Escalabilidad

La arquitectura deberá permitir agregar nuevas fuentes de información y
funcionalidades posteriormente.

## 8. Historias de usuario

Las historias de usuario detalladas se documentarán en GitHub Issues y/o
en una sección específica de la Wiki.

Algunas historias iniciales son:

### HU01 - Buscar contenido

Como usuario, quiero buscar libros, cómics o manga para encontrar
contenido que me interese.

### HU02 - Consultar información

Como usuario, quiero consultar información de una obra para conocer sus
características antes de decidir si me interesa.

### HU03 - Valorar contenido

Como usuario registrado, quiero valorar una obra para expresar mi
opinión y utilizar esta información para futuras recomendaciones.

### HU04 - Recibir recomendaciones

Como usuario, quiero recibir recomendaciones basadas en mis intereses
para descubrir contenido nuevo.

### HU05 - Explorar contenido

Como usuario, quiero explorar diferentes obras sin tener que buscar una
específica para descubrir contenido que no conocía.

## 9. Criterios de aceptación generales

El sistema deberá cumplir, como mínimo, con los siguientes criterios:

- Un usuario deberá poder registrarse e iniciar sesión.
- Un usuario deberá poder buscar contenido.
- El sistema deberá mostrar información de las obras encontradas.
- Un usuario registrado deberá poder valorar contenido.
- El sistema deberá utilizar las valoraciones y/o preferencias
  disponibles para generar recomendaciones.
- La información presentada deberá corresponder al contenido disponible
  en las fuentes utilizadas.
- La aplicación deberá ser accesible mediante una interfaz web.

## 10. Métricas de éxito

Para evaluar el funcionamiento del proyecto se podrán considerar:

- Cantidad de contenido disponible en el sistema.
- Cantidad de usuarios registrados.
- Cantidad de valoraciones realizadas.
- Cantidad de recomendaciones generadas.
- Tiempo de respuesta de las búsquedas.
- Porcentaje de recomendaciones consideradas útiles por los usuarios.

Estas métricas podrán modificarse conforme avance el proyecto.

## 11. Restricciones

El desarrollo del proyecto estará condicionado por:

- Tiempo disponible para el desarrollo.
- Tecnologías seleccionadas por el equipo.
- Disponibilidad y límites de las fuentes de datos externas.
- Información disponible sobre la disponibilidad de contenido en México.
- Recursos disponibles para ejecutar y mantener la aplicación.

## 12. Riesgos

Entre los principales riesgos identificados se encuentran:

- Cambios en las APIs o fuentes de datos utilizadas.
- Falta de información sobre disponibilidad en México.
- Limitaciones de las fuentes externas.
- Complejidad del algoritmo de recomendación.
- Tiempo insuficiente para implementar todas las funcionalidades
  planeadas.

## 13. Estado del documento

Este PRD representa una primera versión del documento de requisitos.

El contenido podrá actualizarse conforme el equipo defina con mayor
precisión las funcionalidades, tecnologías, fuentes de datos y alcance
del sistema.
