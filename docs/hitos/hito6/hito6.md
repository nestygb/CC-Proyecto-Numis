# :coin: Hito 6 :coin:

A continuación se detallan todos los procesos y tareas para llevar a cabo el hito 6 Composición de Servicios, el cual está centrado en el diseño de un servicio utilizando Docker Compose para gestionar varios contenedores, incluyendo uno dedicado al almacenamiento de datos.

## Contenidos

- [Estructura del Clúster](#EC).
- [Configuración de contenedores](#CC).
- [Fichero de composición del clúster](#FCC).
- [Testeo del clúster](#test).


<a name="EC"></a>
## Estructura del Clúster

La estructura del cluster definida en el archivo [docker-compose.yml]https://github.com/nestygb/CC-Proyecto-Numis/blob/main/docker-compose.yml presenta varias características que la hacen adecuada para el despliegue y la gestión de la aplicación ya que en este se puede ver la "Separación de responsabilidades", en este se define diferentes servicios para diferentes componentes de la aplicación, lo que permite una clara separación de responsabilidades. Por ejemplo, se tienen servicios específicos para las pruebas, la API, Elasticsearch, Kibana y Fluentd. Esto facilita la gestión y el mantenimiento de cada componente de la aplicación de forma independiente. Tambien la "Escalabilidad", ya que la estructura del archivo docker-compose.yml está diseñada de manera que cada servicio pueda ser escalado individualmente según sea necesario. Por ejemplo, si se necesita aumentar la capacidad de almacenamiento y procesamiento de logs, se puede escalar el servicio de Elasticsearch o Fluentd sin afectar otros componentes de la aplicación. La "Resiliencia" se evidencia al definir dependencias entre los servicios (por ejemplo, el servicio de Kibana depende del servicio de Elasticsearch), se asegura que los componentes críticos de la aplicación estén disponibles antes de iniciar otros servicios. Esto contribuye a la resiliencia de la aplicación al garantizar que los servicios dependientes estén en funcionamiento antes de intentar utilizarlos. Se puede apreciar la "Centralización de logs", la inclusión de servicios como Elasticsearch, Kibana y Fluentd permite la centralización y el análisis de logs de manera eficiente. Elasticsearch proporciona un almacenamiento escalable y de alto rendimiento para los logs, Kibana ofrece una interfaz de usuario intuitiva para visualizar y analizar los datos de logs, y Fluentd se encarga de recopilar y enviar los logs de manera confiable a Elasticsearch. Por último la "Configuración personalizada" ayuda tambien debido a que se ha proporcionado la capacidad de personalizar la configuración de Fluentd montando un volumen que contiene archivos de configuración personalizados. Esto permite adaptar el comportamiento de Fluentd según las necesidades específicas de la aplicación.

<a name="CC"></a>
## Configuración de contenedores



<a name="FCC"></a>
## Fichero de composición del clúster

A continuación se expone el archivo [docker-compose.yml]https://github.com/nestygb/CC-Proyecto-Numis/blob/main/docker-compose.yml que orquesta y construye la aplicación Numis. De esta manera, se detallará el significada de cada parámetros, tal y como se puede observar:

![](/docs/img/docker-compose.yml1.png)
![](/docs/img/docker-compose.yml2.png)

<a name="test"></a>
## Testeo del clúster

