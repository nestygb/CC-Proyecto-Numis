# :coin: Hito 3 :coin:

A continuación, se describirán los procesos y tareas realizadas para llevar a cabo el hito 3.

## Contenidos

- [Justificación de la elección del contenedor base](#ECB).
- [Justificación del Dockerfile creado](#JD).
- [Contenedores en DockerHub](#CD).
- [Otras tareas desarrolladas](#Otras).

<a name="ECB"></a>
# Elección del contenedor base
Para llevar a cabo la elección del contenedor base a utilizar en función a las decisiones tomadas en el [Hito 2](./../hito2/hito2.md) y teniendo en cuentas tanto las herramientas como los _frameworks_ y lenguajes que se emplearán. De esta manera, los criterios de selección seguidos se han basado en el tamaño de la imagen, el tiempo de ejecución, funcionalidad y características incluidas. Por consiguiente, dado que el lenguaje utilizado es *python* se han contemplado lo siguiente:

- python: Esta es la imagen oficial de Python y está disponible con diferentes versiones. Esta es la elejida como contenedor base con la versión 3.9.

```text
FROM python:3.9
```
<a name="JD"></a>
# Justificación del Dockerfile creado
En esta sección se llevará a cabo una descripción del archivo Dockerfile creado. Para ello, se ha tenido en cuenta la guía de buenas prácticas proporcionada por Docker. Además, dado que se ha utilziado una imagen de node con base alpine y se requieren diferentes paquetes para el correcto funcionamiento del contenedor de pruebas se ha seguido también esta guía.

## Configuración del contenedor

- Primero creamos el archivo requirements.txt usando el comando desde el directorio raiz del proyecto:

```text
pip freeze > requirements.txt
```

## Creacion del archivo Dockerfile

Se crea el archivo _Dokerfile_, que es un archivo de configuración utilizado en Docker para construir imágenes de contenedores.

```text
    FROM python:3.9

    WORKDIR /app

    COPY . /app

    RUN pip install -r requirements.txt  

    CMD [ "pytest" ]
```

## Creación del archivo docker-compose.yml

Se crea el archivo para simplificar la ejecución del contenedor en docker.

```text
    version: '3'
    services:
    tests:
        build: .
        volumes:
        - .:/app
  
```

## Ejecución del contenedor

Se abre una terminal en el directorio raiz del proyecto y se ejecuta comando para construir la imagen del contenedor:

```text
docker-compose build
```

![Docker build](/docs/img/docker_build.png)

## Iniciar los servicios definidos en el archivo docker-compose.yml

```text
docker-compose up
```

![Docker up](/docs/img/docker_up.png)

## Ejecucion de los tests

```text
docker-compose run tests
```

![Docker tests](/docs/img/docker_run_test.png)


<a name="CD"></a>
# Contenedores en DockerHub
## Actualización y subida de la imagen a DockerHub
Se ha empleado DockerHub para almacenar el contenedor de comprobación de los tests puesto que se trata de un servicio proporcionado por Docker que además de permitir realizar búsquedas y compartir imágenes de contenedores también permite llevar a cabo acciones programadas sobre un repositorio cargado, es decir, nos hemos ayudado de los _webhooks_ de _GitHub Actions_.
En nuestro caso, tal y como se ha comentado, se utilziará para alojar el contendor de test del proyecto, actualizando la iamgen de manera automática a través de un _Workflow_, el cual puede consultarse 
[aquí](github/workflow/docker_flow.yml).

![contenedor docker](/docs/img/docker_tag_image_push.png)

## Ejecucion de las Actions de GitHub y DockerHub

Se ejecutraron las GitHub Action

![contenedor docker](/docs/img/Action.png)

