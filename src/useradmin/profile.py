class PiezaNumismatica:
    def __init__(self, codigo, pais, descripcion, anio):
        self.codigo = codigo
        self.pais = pais
        self.descripcion = descripcion
        self.anio = anio

class ColeccionNumismatica:
    def __init__(self):
        self.inventario = []

    def agregar_pieza(self, pieza):
        self.inventario.append(pieza)

    def buscar_por_codigo(self, codigo):
        return [pieza for pieza in self.inventario if pieza.codigo == codigo]

    def buscar_por_pais(self, pais):
        return [pieza for pieza in self.inventario if pieza.pais == pais]

# Ejemplo de uso
coleccion = ColeccionNumismatica()

# Agregar algunas piezas a la colección
coleccion.agregar_pieza(PiezaNumismatica("001", "Estados Unidos", "Dólar", 1975))
coleccion.agregar_pieza(PiezaNumismatica("002", "Francia", "Franco", 1980))
coleccion.agregar_pieza(PiezaNumismatica("003", "Italia", "Lira", 1995))
coleccion.agregar_pieza(PiezaNumismatica("004", "Estados Unidos", "Centavo", 2000))

# Buscar por código
resultados_codigo = coleccion.buscar_por_codigo("002")
print("Resultados por código:")
for pieza in resultados_codigo:
    print(f"Código: {pieza.codigo}, País: {pieza.pais}, Descripción: {pieza.descripcion}, Año: {pieza.anio}")

# Buscar por país
resultados_pais = coleccion.buscar_por_pais("Estados Unidos")
print("\nResultados por país:")
for pieza in resultados_pais:
    print(f"Código: {pieza.codigo}, País: {pieza.pais}, Descripción: {pieza.descripcion}, Año: {pieza.anio}")
