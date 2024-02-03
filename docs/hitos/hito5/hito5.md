# :coin: Hito 5 :coin:

En este hito se define la elección y justificación de los distintos frameworks utilizados para microservicios, se ha llevado a cabo la documentación y diseño completo de la API, se ha levantado un conjunto de contenedores para la realización y visualización de logs.

## Contenidos

- [Framework Utilizado](#FU).
- [Diseño de la API](#API).
- [Especificación OpenAPI](#OpenAPI).
- [Demostración de las APIs creadas en la web](#demo).


<a name="FU"></a>
## Framework Utilizado

Para el desarrollo de este hito se seleccionó el framework Flask por su simplicidad, flexibilidad y velocidad de desarrollo, permitiendo una implementación ágil y adaptativa. Además, la integración de Swagger facilita la documentación automatizada de las APIs, mejorando la comprensión y colaboración entre equipos de desarrollo y documentación. Flask destaca por su extensibilidad, escalabilidad y una activa comunidad, mientras que Swagger proporciona una interfaz intuitiva y estándares abiertos para una documentación clara y accesible, debido a que esta utiliza estándares abiertos como OpenAPI, lo que asegura la portabilidad y la compatibilidad con otras herramientas y servicios en el ecosistema de desarrollo de APIs. Esta combinación ha demostrado ser esencial para construir microservicios eficientes y fácilmente mantenibles en un entorno dinámico.

![](/docs/img/flask.png)

<a name="API"></a>
## Diseño de la API

A continuacion se muestran los metodos de las APIs utilizando el framework antes descrito, los cuales fueron implementados en el fichero app.py

Primeramente importamos los modulos y luego se configura la aplicación Flask, seguidamente se configura el sistema de registro (logging) de la aplicación Flask, especificando un archivo de registro (app.log), el nivel de registro (INFO), y el formato del mensaje.

Configurado lo anterior se crea una "Colección e Piezas Numismáticas" y se define una ruta en la aplicación (La documentación de Swagger para esta ruta se especifica utilizando docstrings bajo el formato de Swagger/OpenAPI.)

Posterior a esto podemos ver los ejemplos de codigos de las API que permiten la obtención de todas las piezas numismáticas existentes y la adición de nuevas piezas mediante solicitudes GET y POST, respectivamente.

![](/docs/img/app.py1.png)
![](/docs/img/app.py2.png)
![](/docs/img/app.py3.png)


<a name="OpenAPI"></a>
## Especificación OpenAPI

La creación de ficheros de especificación OpenAPI, en formato YAML (.yml) dentro de la carpeta "Swagger" es esencial para documentar y describir de manera detallada cómo interactuar con las API. Estos ficheros actúan como documentación centralizada que define los detalles de la API, incluyendo qué datos se deben proporcionar en las solicitudes y qué se puede esperar como respuesta. Es decir que el propósito es servir como un contrato claro entre el consumidor y el proveedor de la API, describiendo los puntos de entrada (rutas), los métodos HTTP admitidos, los parámetros requeridos, el formato de los datos y las respuestas esperadas. A continuación se muestran dichos ficheros:

![](/docs/img/swagger.png)


<a name="demo"></a>
## Demostración de las APIs creadas en la web

Inicializada la aplicación Flask mediante la ejecución del comando "python app.py" quedan configuradas las rutas, establecidas las configuraciones de la aplicación y lista para manejar solicitudes web.

Luego nos dirigimos a la ruta web local de Swagger (http://127.0.0.1:5000/) para ver como se muestran las APIs creadas:

![](/docs/img/swagger.png)




