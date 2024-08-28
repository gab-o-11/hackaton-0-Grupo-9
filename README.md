# Hackathon 1: Dominando Git y GitHub 🚀

### Consideraciones Generales 📋

Bienvenidos a la primera hackathon del semestre 20242 del curso CS2031: Desarrollo Basado en Plataformas. En esta edición, nos centraremos exclusivamente en Git y GitHub, herramientas fundamentales para cualquier desarrollador. En lugar de enfocarnos en la escritura de código, nos dedicaremos a perfeccionar nuestras habilidades en el manejo de repositorios, la colaboración en equipos y la integración continua.

Para esta hackathon, cada equipo estará compuesto por cuatro (4) miembros. Será crucial que trabajen en conjunto para cumplir con todos los checkpoints establecidos. Es importante que mantengan una comunicación constante y que asignen tareas de manera equitativa. Al ser una actividad grupal, la organización y la cooperación serán clave para el éxito.

### Instrucciones Generales 📝

1. **Formación de Equipos**: Los equipos deben estar conformados por 4 alumnos de la misma sección de laboratorio. Cada equipo debe asegurarse de que todos sus miembros participen activamente en cada checkpoint.

2. **Gestión de Repositorios**: Solo se permitirá un repositorio por equipo, el cual deberá cumplir con los requisitos especificados en cada checkpoint. La calidad del trabajo en cada checkpoint será evaluada con base en el cumplimiento de los requisitos, la correcta utilización de Git y GitHub, y la capacidad de resolver conflictos y problemas de manera efectiva.

3. **Entrega y Evaluación**: Al finalizar la hackathon, se revisará el repositorio de cada equipo. Asegúrense de cumplir con todos los requisitos antes de la hora límite. Se evaluará tanto el trabajo grupal como la participación individual a través del historial de commits y los pull requests realizados.

### Checkpoints 📌

#### **Checkpoint 1: Configuración Inicial** ⚙️
- **Objetivo**: Configurar adecuadamente el entorno de trabajo local y la cuenta en GitHub.
  - **Tareas**:
    1. Cada miembro del equipo debe configurar Git en su máquina local (configurar usuario, email, nombre).
    2. Crear o asegurarse de tener una cuenta en GitHub.
    3. Generar claves SSH en sus máquinas locales y agregarlas a sus cuentas de GitHub.
  - **Evaluación**: Mostrar la configuración de Git local y la adición exitosa de la clave SSH en su cuenta de GitHub.

#### **Checkpoint 2: Creación y Configuración del Repositorio** 📦
- **Objetivo**: Crear y configurar un repositorio en GitHub que refleje buenas prácticas de desarrollo colaborativo.
  - **Tareas**:
    1. Crear un repositorio público o privado en GitHub. Este repositorio será compartido por todos los miembros del equipo.
    2. Crear un archivo `README.md` en el repositorio (vacío por ahora).
    3. Configurar las reglas de la rama `main` para que no se pueda hacer `push` directo a esta rama. Los cambios en `main` solo deben realizarse mediante pull requests aprobados.
  - **Evaluación**: Proveer un enlace al repositorio y capturas de pantalla de la configuración de las reglas de la rama `main`.

#### **Checkpoint 3: Gestión de Issues y Pull Requests** 🔄
- **Objetivo**: Implementar un flujo de trabajo que simule un entorno colaborativo real.
  - **Tareas**:
    1. Crear un issue en GitHub para cada miembro del equipo. El título del issue debe reflejar la tarea que realizará cada miembro (ejemplo: "Añadir nombre al README.md").
    2. Cada miembro del equipo debe crear una rama nueva a partir del issue asignado (la rama debe llevar el nombre del issue).
    3. Cada miembro deberá modificar el archivo `README.md` añadiendo su nombre y un breve párrafo de presentación.
    4. Realizar un pull request de cada rama hacia `main` y completar el proceso de revisión y aprobación.
    5. Resolver cualquier conflicto que pueda surgir durante el proceso de merge.
  - **Evaluación**: Mostrar los issues creados, las ramas correspondientes, y el historial de pull requests. Se verificará que haya un pull request por cada miembro del equipo.

#### **Checkpoint 4: Desarrollo del CRUD en FastAPI** ⚙️
- **Objetivo**: Implementar un CRUD básico utilizando FastAPI y almacenar los datos en un archivo JSON.
  - **Tareas**:
    1. Crear un archivo `crud.py` donde se implementará un CRUD básico utilizando FastAPI.
    2. El CRUD deberá manejar operaciones básicas de creación, lectura, actualización y eliminación (Create, Read, Update, Delete).
    3. Los datos manejados por el CRUD se almacenarán en un archivo JSON que debe ser actualizado dinámicamente.
    4. Asegurarse de que el CRUD sea funcional y esté correctamente documentado en el archivo `README.md`.
    5. Implementar los siguientes endpoints adicionales:
       - **Obtener todos los productos antes de una fecha específica**
         - **Endpoint**: `GET /items/before/{date}`
         - **Descripción**: Obtener todos los equipos que fueron ingresados antes de una fecha específica.
         - **Respuesta**: Una lista de todos los objetos de equipo antes de la fecha dada.
       - **Obtener todos los productos en un rango de precios**
         - **Endpoint**: `GET /items/price_range/`
         - **Descripción**: Obtener todos los equipos cuyo precio esté dentro de un rango específico.
         - **Parámetros de consulta**: `min_price` (float), `max_price` (float).
         - **Respuesta**: Una lista de todos los objetos de equipo dentro del rango de precios especificado.
  - **Evaluación**: Se verificará la correcta implementación del CRUD, la actualización del archivo JSON con cada operación y el funcionamiento de los nuevos endpoints. Se revisará la documentación en el `README.md`.

#### **Checkpoint 5: Pruebas Automatizadas con GitHub Actions** 🤖
- **Objetivo**: Configurar la integración continua para asegurar la calidad del código mediante pruebas automatizadas.
  - **Tareas**:
    1. Se les proporcionará un archivo `test_crud.py` que contiene pruebas automatizadas para el CRUD implementado en el Checkpoint 4.
    2. Configurar un GitHub Action que ejecute automáticamente `test_crud.py` cada vez que se realice un pull request a `main`.
    3. Asegurarse de que todas las pruebas pasen correctamente.
    4. Documentar en el `README.md` cómo configuraron el GitHub Action y los resultados esperados de las pruebas.
  - **Evaluación**: Se verificará la configuración del GitHub Action y que todas las pruebas se ejecuten correctamente en cada pull request.

### Endpoints del CRUD en FastAPI

A continuación se listan todos los endpoints que se deberán implementar en `crud.py`:

1. **Crear un equipo en el inventario**
   - **Endpoint**: `POST /items/`
   - **Descripción**: Agregar un nuevo equipo al inventario.
   - **Cuerpo de la solicitud**: JSON con los siguientes campos:
     ```json
     {
       "id": "str",
       "name": "str",
       "description": "str",
       "quantity": "int",
       "price": "float",
       "date_of_entry": "str"  // Formato YYYY-MM-DD
     }
     ```
   - **Respuesta**: El objeto del equipo recién creado.

2. **Obtener todos los equipos**
   - **Endpoint**: `GET /items/`
   - **Descripción**: Obtener la lista de todos los equipos en el inventario.
   - **Respuesta**: Una lista de todos los objetos de equipo.

3. **Obtener un equipo por ID**
   - **Endpoint**: `GET /items/{id}`
   - **Descripción**: Obtener la información de un equipo específico utilizando su ID.
   - **Respuesta**: El objeto del equipo correspondiente al ID proporcionado.

4. **Actualizar un equipo**
   - **Endpoint**: `PUT /items/{id}`
   - **Descripción**: Actualizar la información de un equipo específico utilizando su ID.
   - **Cuerpo de la solicitud**: JSON con los campos que se desean actualizar (mismo formato que en la creación).
   - **Respuesta**: El objeto del equipo actualizado.

5. **Eliminar un equipo**
   - **Endpoint**: `DELETE /items/{id}`
   - **Descripción**: Eliminar un equipo del inventario utilizando su ID.
   - **Respuesta**: Un mensaje confirmando la eliminación.

6. **Obtener todos los productos antes de una fecha específica**
   - **Endpoint**: `GET /items/before/{date}`
   - **Descripción**: Obtener todos los equipos que fueron ingresados antes de una fecha específica.
   - **Respuesta**: Una lista de todos los objetos de equipo antes de la fecha dada.

7. **Obtener todos los productos en un rango de precios**
   - **Endpoint**: `GET /items/price_range/`
   - **Descripción**: Obtener todos los equipos cuyo precio esté dentro de un rango específico.
   - **Parámetros de consulta**: `min_price` (float), `max_price` (float).
   - **Respuesta**: Una lista de todos los objetos de equipo dentro del rango de precios especificado.

### Consideraciones Finales

- **Comunicación**: Mantengan una comunicación constante a través de plataformas como Slack, Discord o el foro del curso para resolver dudas y coordinarse de manera eficiente.
- **Documentación**: Asegúrense de documentar cada paso realizado en el repositorio, utilizando los mensajes de commit y el archivo `README.md`.
- **Fecha Límite**: La hackathon deberá completarse antes del [fecha límite específica], momento en el cual los repositorios serán revisados.

¡Buena suerte a todos!⚡ Que esta hackathon sea una oportunidad para fortalecer su dominio de Git y GitHub.
