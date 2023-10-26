## :rocket: Preparación inicial del entorno de trabajo :rocket:

Este texto se centra en los procedimientos necesarios para establecer adecuadamente el entorno laboral utilizando las plataformas de git y GitHub. El propósito es garantizar el uso efectivo de los distintos repositorios y cumplir con los requisitos exigidos en las diversas entregas.

### Creación de los repositorios

Repositorios que contiene el proyecto

- [Repositorio de mi proyecto Numis](https://github.com/nestygb/CC-Proyecto-Numis)

- [Fork creado al repositorio de la asignatura](https://github.com/nestygb/CC-23-24)

Una vez realizado lo anterior, procedí a clonar dichos repositorios desde GitHub a mi local:

```
$ git clone https://github.com/nestygb/CC-23-24
```

```
$ git clone https://github.com/nestygb/CC-Proyecto-Numis
```

### Configuración de la cuenta personal de GitHub

Para identificarme dentro de la plataforma, se añadió mi foto de perfil, la universidad donde estudio y otros datos del perfil.

### Configuración de nombre y correo electrónico para que apareza en los commits

Asocié el correo electrónico como unnusuario a git. Haciendo uso de estos comandos:

```
$ git config --global user.name "Nestor E Gonzalez Bravo"
$ git config --global user.email nestygb@gmail.com
```

Para comprobar que los cambios se realizaron correctamente se utilizó este comando:

```
$ git config --list
```
### Creación de claves y subida de clave pública a GitHub

Creación de la clave publico y privada a GitHub

```
$ ssh-keygen -t ed25519 -C "nestygb@gmail.com"
```
Añadiendo las claves anteriormente generadas al agente _ssh_.

```
$ eval `ssh-agent -s`
Agent pid 1406
```

```
$ ssh-add ~/.ssh/id_ed25519
```
Añadi en mi perfil de GitHb la clave publica en la siguiente ruta (en el apartado _Settings_ > _SSH and GPG keys_) que se encuentra almacenada en el fichero C:\Users\nesty\.ssh.

### Activar el segundo factor de autenticación

Para la autentificación de doble factor, en el apartado de _Settings_ > _Password and authentication_ para habilitarlo se selecciona _Two-factor authentication_. En este caso, se ha seleccionado el envío de un código a través de un mensaje de texto (SMS) como segunda forma de autenticación de GitHub.