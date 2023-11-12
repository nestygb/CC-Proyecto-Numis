# :coin: Hito 2 :coin:

A continuación, se describirán los procesos y tareas realizadas para llevar a cabo el hito 2.

La adopción de TDD en mi código proporciona beneficios significativos al desarrollo, al permitir la detección temprana de errores, garantizar el cumplimiento de requisitos a través de pruebas automatizadas, mejorar la estructura del código mediante diseño modular, facilitar la refactorización segura, generar documentación automática, fomentar la colaboración en equipos, aumentar la confianza en el código y reducir el costo de corrección de errores. Al escribir pruebas antes de la implementación, TDD establece una base sólida para el desarrollo, mejorando la calidad y la mantenibilidad del software.

Se añadio el fichero cc.yaml con las claves especificadas [fichero](https://github.com/nestygb/CC-Proyecto-Numis/blob/main/cc.yaml).

## Contenidos

- Gestor de Tareas
- Biblioteca de Aserciones
- Marco de pruebas

### Gestores de Tareas

En este punto se define el gestor de tareas "invoke", el cual es un gestor de tareas y ejecución de comandos para Python. Su objetivo principal es proporcionar una forma sencilla y consistente de definir y ejecutar tareas, especialmente en el contexto de desarrollo y automatización de proyectos. 

Instalación del invoke:
```
pip install invoke
```

### Biblioteca de Aserciones

Python tiene una declaración de aserción integrada llamada assert. Puedes usarla para verificar si una expresión es verdadera. Si la expresión es falsa, se levanta una excepción AssertionError.
```
def test_buscar_por_codigo_existente(coleccion):
    resultados = coleccion.buscar_por_codigo("002")
    assert len(resultados) == 1
    assert resultados[0].codigo == "002"
```
### Marco de pruebas

Instalación del Entorno Virtual 
```
python -m venv evnumis
```
Instalación del Ejecutor de Pruebas Unitarias en Python
```
pip install pytest
```
Activación del Entorno virtual
```
 .\evnumis\Scripts\activate
```
Para ejecutar las pruebas unitarias se puede realizar mediante los comandos "invoke test" o "pytest"