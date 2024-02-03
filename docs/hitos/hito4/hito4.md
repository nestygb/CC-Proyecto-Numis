# :coin: Hito 4 :coin:

A continuación, se describirán los procesos y tareas realizadas para llevar a cabo el hito 4, el cual consiste en la preparación del proyecto para la integración continua, donde se eligió Jenkins como sistema de integración continua debido a su compatibilidad con los frameworks y por las caracteristicas que posee para la ejecución de los test.

## Contenidos

- [Configuración de Jenkins](#CJ).
- [Github en Jenkins](#GJ).
- [Pipeline en Jenkins](#PJ).
- [Archivo Jenkinsfile](#AJ).
- [Webhook en Github](#WG).
- [Ejecución de las Actions de GitHub y jobs de Jenkins](#EA).

<a name="CJ"></a>
## Configuración de Jenkins

Instalado Jenkins se selecciona por defecto el puerto 8080 que va a ejecutarse en el servidor local. Una vez registrados se instalan los pluggins necesarios Pipeline, Docker, entre otros y procedemos a crear nuestro proyecto:

![Numis](/docs/img/Jenkins1.png)

<a name="GJ"></a>
## Github en Jenkins

Configuración en Jenkins para conectar Github mediante la URL 

![Numis](/docs/img/Github.png)

<a name="PJ"></a>
## Pipeline en Jenkins

Luego se procede a la configuración de Pipeline en Jenkins (Build Triggers: GitHub hook trigger for GITScm polling y Trigger builds remotely) para la autenticación de las actions de Github, seguido a esto se procede a establecer la direccion del repositorio en Github, la branch en donde se aloja este repositorio y el archivo Jenkinsfile que es el que contendrá los procesos a ejecutar cuando se ejecute algún cambio en el repositorio.

<a name="AJ"></a>
## Archivo Jenkinsfile

Creacion del archivo Jenkinsfile que proporciona una descripción del proceso de construcción y despliegue en Jenkins utilizando la sintaxis declarativa.

![Numis](/docs/img/Jenkinsfile.png)

<a name="WG"></a>
## Webhook en Github

En la configuracion de nuestro repositorio en Webhooks creamos una nueva y especificamos la direccion de nuestro dashboard en Jenkins.

![Numis](/docs/img/Webhooks.png)

<a name="EA"></a>
## Ejecución de las Actions de GitHub y jobs de Jenkins

Como resultado final procedemos a la ejecución de las Actions

![Numis](/docs/img/EjecActions.png)