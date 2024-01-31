from flask import Flask, jsonify, request
from flasgger import Swagger
from flasgger.utils import swag_from
import logging

from useradmin.profile import ColeccionNumismatica, PiezaNumismatica

app = Flask(__name__)
swagger = Swagger(app)

# logging para Flask
logging.basicConfig(filename='app.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
app.logger.addHandler(logging.StreamHandler())
app.logger.setLevel(logging.INFO)

coleccion = ColeccionNumismatica()
# Agregar algunas piezas a la colección
coleccion.agregar_pieza(PiezaNumismatica("001", "Estados Unidos", "Dólar", 1975))
coleccion.agregar_pieza(PiezaNumismatica("002", "Francia", "Franco", 1980))
coleccion.agregar_pieza(PiezaNumismatica("003", "Italia", "Lira", 1995))
coleccion.agregar_pieza(PiezaNumismatica("004", "Estados Unidos", "Centavo", 2000))

@app.route('/')
def hello_world():
    """
    Ruta de bienvenida.
    ---
    responses:
      200:
        description: Mensaje de bienvenida
    """
    return jsonify(message='Hola de bienvenida')

@app.route('/piezas', methods=['GET'])
@swag_from('swagger/get_piezas.yml')
def get_piezas():
    """
    Obtener todas las piezas numismáticas.
    ---
    responses:
      200:
        description: Lista de piezas numismáticas
    """
    return jsonify([{
        'codigo': pieza.codigo,
        'pais': pieza.pais,
        'descripcion': pieza.descripcion,
        'anio': pieza.anio
    } for pieza in coleccion.inventario])

@app.route('/piezas', methods=['POST'])
@swag_from('swagger/post_pieza.yml')
def post_pieza():
    """
    Agregar una nueva pieza numismática.
    ---
    parameters:
      - in: body
        name: pieza
        required: true
        schema:
          type: object
          properties:
            codigo:
              type: string
            pais:
              type: string
            descripcion:
              type: string
            anio:
              type: integer
    responses:
      201:
        description: Pieza numismática agregada con éxito
    """
    data = request.get_json()
    nueva_pieza = PiezaNumismatica(data['codigo'], data['pais'], data['descripcion'], data['anio'])
    coleccion.agregar_pieza(nueva_pieza)
    return jsonify(message=f'Pieza {data["codigo"]} agregada con éxito'), 201

if __name__ == '__main__':
    app.run(debug=True)
