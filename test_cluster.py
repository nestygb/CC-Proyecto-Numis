import requests
import time
import pytest

@pytest.fixture(scope="module", autouse=True) # Espera a que los servicios estén completamente levantados antes de ejecutar las pruebas
def wait_for_services():
    time.sleep(10)  # Espera 10 segundos para que los servicios se levanten completamente
    yield

def test_api_endpoint():
    response = requests.get("http://localhost:5000/")  # Realiza una petición GET al endpoint "/"
    assert response.status_code == 200  # Verifica que se reciba un código de estado 200 OK
    assert response.json()["message"] == "Piezas para intercambio o venta"  # Verifica que el mensaje de respuesta sea el esperado

def test_ping_endpoint():
    response = requests.get("http://localhost:5000/piezas")  # Realiza una petición GET al endpoint "/piezas"
    assert response.status_code == 200  # Verifica que se reciba un código de estado 200 OK

if __name__ == "__main__":
    pytest.main()
