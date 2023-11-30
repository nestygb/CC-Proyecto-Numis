import pytest
import os
import sys

# Obtén la ruta del directorio actual (donde se encuentra test_profile.py)
current_dir = os.path.dirname(__file__)

# Agrega el directorio de nivel superior al sys.path
sys.path.append(os.path.abspath(os.path.join(current_dir, '..')))

from src.useradmin.profile import PiezaNumismatica, ColeccionNumismatica

@pytest.fixture
def coleccion():
    # Configuración inicial para las pruebas
    coleccion = ColeccionNumismatica()
    coleccion.agregar_pieza(PiezaNumismatica("001", "Estados Unidos", "Dólar", 1975))
    coleccion.agregar_pieza(PiezaNumismatica("002", "Francia", "Franco", 1980))
    coleccion.agregar_pieza(PiezaNumismatica("003", "Italia", "Lira", 1995))
    coleccion.agregar_pieza(PiezaNumismatica("004", "Estados Unidos", "Centavo", 2000))
    return coleccion

def test_buscar_por_codigo_existente(coleccion):
    resultados = coleccion.buscar_por_codigo("002")
    assert len(resultados) == 1
    assert resultados[0].codigo == "002"

def test_buscar_por_codigo_inexistente(coleccion):
    resultados = coleccion.buscar_por_codigo("999")
    assert len(resultados) == 0

def test_buscar_por_pais_existente(coleccion):
    resultados = coleccion.buscar_por_pais("Estados Unidos")
    assert len(resultados) == 2
    assert resultados[0].pais == "Estados Unidos"
    assert resultados[1].pais == "Estados Unidos"

def test_buscar_por_pais_inexistente(coleccion):
    resultados = coleccion.buscar_por_pais("Alemania")
    assert len(resultados) == 0
