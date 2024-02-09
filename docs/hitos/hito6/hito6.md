# :coin: Hito 6 :coin:

A continuación se detallan todos los procesos y tareas para llevar a cabo el hito 6 Composición de Servicios, el cual está centrado en el diseño de un servicio utilizando Docker Compose para gestionar varios contenedores, incluyendo uno dedicado al almacenamiento de datos.

## Contenidos

- [Estructura del Clúster](#EC).
- [Configuración de contenedores](#CC).
- [Fichero de composición del clúster](#FCC).
- [Testeo del clúster](#test).


<a name="EC"></a>
## Estructura del Clúster

La estructura del cluster definida en el archivo [docker-compose.yml](https://github.com/nestygb/CC-Proyecto-Numis/blob/main/docker-compose.yml) presenta varias características que la hacen adecuada para el despliegue y la gestión de la aplicación ya que en este se puede ver la "Separación de responsabilidades", en este se define diferentes servicios para diferentes componentes de la aplicación, lo que permite una clara separación de responsabilidades. Por ejemplo, se tienen servicios específicos para las pruebas, la API, Elasticsearch, Kibana y Fluentd. Esto facilita la gestión y el mantenimiento de cada componente de la aplicación de forma independiente. Tambien la "Escalabilidad", ya que la estructura del archivo docker-compose.yml está diseñada de manera que cada servicio pueda ser escalado individualmente según sea necesario. Por ejemplo, si se necesita aumentar la capacidad de almacenamiento y procesamiento de logs, se puede escalar el servicio de Elasticsearch o Fluentd sin afectar otros componentes de la aplicación. La "Resiliencia" se evidencia al definir dependencias entre los servicios (por ejemplo, el servicio de Kibana depende del servicio de Elasticsearch), se asegura que los componentes críticos de la aplicación estén disponibles antes de iniciar otros servicios. Esto contribuye a la resiliencia de la aplicación al garantizar que los servicios dependientes estén en funcionamiento antes de intentar utilizarlos. Se puede apreciar la "Centralización de logs", la inclusión de servicios como Elasticsearch, Kibana y Fluentd permite la centralización y el análisis de logs de manera eficiente. Elasticsearch proporciona un almacenamiento escalable y de alto rendimiento para los logs, Kibana ofrece una interfaz de usuario intuitiva para visualizar y analizar los datos de logs, y Fluentd se encarga de recopilar y enviar los logs de manera confiable a Elasticsearch. Por último la "Configuración personalizada" ayuda tambien debido a que se ha proporcionado la capacidad de personalizar la configuración de Fluentd montando un volumen que contiene archivos de configuración personalizados. Esto permite adaptar el comportamiento de Fluentd según las necesidades específicas de la aplicación.

<a name="CC"></a>
## Configuración de contenedores

Configuración de cada uno de los contenedores definidos en el archivo docker-compose.yml

Contenedor de pruebas (tests): El contenedor se construye a partir del directorio actual, lo que garantiza que cualquier cambio en el código se refleje en el contenedor de pruebas. Se monta el código fuente en el contenedor para que las pruebas puedan acceder a él y ejecutarse contra la última versión del código y se especifica el comando pytest para que las pruebas se ejecuten automáticamente al iniciar el contenedor.

Contenedor de la API (api): Similar al contenedor de pruebas, se construye a partir del directorio actual para asegurar que esté utilizando la última versión del código. Luego se monta el código fuente en el contenedor para que la API pueda acceder a él y ejecutarse correctamente. Se mapea el puerto 5000 del contenedor al puerto 5000 del host para permitir el acceso a la API desde fuera del contenedor. Por último se especifica el comando python app.py para iniciar la aplicación API dentro del contenedor.

Contenedor de Elasticsearch (elasticsearch): Se utiliza la imagen oficial de Elasticsearch proporcionada por Docker Hub para garantizar la fiabilidad y la compatibilidad. Se mapea el puerto 9200 del contenedor al puerto 9200 del host para permitir el acceso a Elasticsearch desde fuera del contenedor y se configura Elasticsearch como un nodo único (discovery.type=single-node) para simplificar la configuración y el despliegue.

Contenedor de Kibana (kibana): Al igual que en el anterior se utiliza la imagen oficial de Kibana y se mapea el puerto 5601 del contenedor al puerto 5601 del host para permitir el acceso a Kibana desde fuera del contenedor, especificando que este contenedor depende del contenedor de Elasticsearch para garantizar que Elasticsearch esté disponible antes de iniciar Kibana.

Contenedor de Fluentd (fluentd): Igualmente se utiliza la imagen oficial de Fluentd y se monta la configuración personalizada de Fluentd en el contenedor para adaptar su comportamiento según las necesidades del proyecto, tambien especificando que este contenedor depende del contenedor de Elasticsearch para garantizar que los logs se envíen correctamente a Elasticsearch. Por ultimo se configura el archivo de configuración de Fluentd (FLUENTD_CONF=fluent.conf) para personalizar su comportamiento.

<a name="FCC"></a>
## Fichero de composición del clúster

A continuación se expone el archivo [docker-compose.yml](https://github.com/nestygb/CC-Proyecto-Numis/blob/main/docker-compose.yml) que orquesta y construye la aplicación Numis. De esta manera, se detallará el significada de cada parámetros, tal y como se puede observar:

![](/docs/img/docker-compose.yml1.png)
![](/docs/img/docker-compose.yml2.png)

<a name="test"></a>
## Testeo del clúster

Se agregó un test para construir el clúster y responder a algunas peticiones, en el archivo [test_cluster.py](https://github.com/nestygb/CC-Proyecto-Numis/blob/main/test_cluster.py) se creo un script haciendo uso de la biblioteca de pruebas pytest para automatizar la construcción del clúster de contenedores definido en docker-compose.yml el cual realizará algunas peticiones para verificar que los servicios estén funcionando correctamente.

![](/docs/img/test%20cluster.png)

Posterior a esto se indicó en el archivo cc.yaml el nombre del fichero

![](/docs/img/cc-yaml.png)


![](/docs/img/imagesDocker.png)