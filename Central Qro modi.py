# Crear una lista de ubicaciones disponibles
ubicaciones_disponibles = ["Jalisco", "Aguascalientes", "Ciudad de México", "Chiapas"]

# Crear un diccionario con los precios por ubicación
precios = { "Jalisco": 100, "Aguascalientes": 150, "Ciudad de México": 200, "Chiapas": 250}

# Definir el precio total
def calcular_precio(ubicacion_elegida, precios):
    if ubicacion_elegida in precios:
        return precios[ubicacion_elegida] * 1.05
    else:
        return "Ubicación no válida"
# Pedir al usuario que elija una ubicación
print("Ubicaciones disponibles:")
for i, ubicacion in enumerate(ubicaciones_disponibles):
    print(f"{i + 1}. {ubicacion}")

opcion_ubicacion = int(input("Seleccione una ubicación (1-4): ")) - 1
ubicacion_elegida = ubicaciones_disponibles[opcion_ubicacion]

# Preguntar al usuario si quiere un viaje redondo o simple
tipo_de_viaje = input("¿Quiere un viaje redondo o uno simple? (redondo/simple): ")

# Validar la entrada del usuario
while tipo_de_viaje.lower() not in ["redondo", "simple"]:
    tipo_de_viaje = input("Por favor, ingrese 'redondo' o 'simple': ")

# Preguntar al usuario el día para el viaje simple
dia_viaje_simple = input("¿Qué día quiere elegir para el viaje de ida? ")

# Preguntar al usuario el día de regreso para el viaje redondo si es necesario
dia_viaje_regreso = None
if tipo_de_viaje.lower() == "redondo":
    dia_viaje_regreso = input("¿Qué día quiere elegir para el viaje de regreso? ")

# Mostrar la información seleccionada por el usuario
print("\nResumen de su elección:")
print(f"Tipo de viaje: {tipo_de_viaje}")
print(f"Día del viaje simple: {dia_viaje_simple}")
if dia_viaje_regreso:
    print(f"Día del viaje de regreso: {dia_viaje_regreso}")

# Crear una matriz de 6x5 con valores de 1 a 30
asientos = []
numero_asiento = 1
for i in range(6):
    fila = []
    for j in range(5):
        fila.append(numero_asiento)
        numero_asiento += 1
    asientos.append(fila)

for fila in asientos:
    print(fila)
# Pedir al usuario que elija un asiento
asiento_elegido = int(input("Elige un asiento del 1 al 30: "))
# Verificar si el asiento está disponible 
encontrado = False
for i in range(len(asientos)):
    if asiento_elegido in asientos[i]:
        fila = i
        columna = asientos[i].index(asiento_elegido)
        asientos[fila][columna] = 'X'  # Marcar el asiento como ocupado
        encontrado = True
        break
# Mostrar la matriz actualizada
if encontrado:
    print(f"Has elegido el asiento {asiento_elegido}.")
    for fila in asientos:
        print(fila)
else:
    print("Asiento no disponible. Por favor, elige otro asiento.")

# Dar el precio
print(f"El precio para ir a ", ubicacion_elegida,f"es : {calcular_precio(ubicacion_elegida, precios)}")

if dia_viaje_regreso:
    precio_total = calcular_precio(ubicacion_elegida, precios)
    if tipo_de_viaje.lower() == "redondo":
        precio_total *= 2
    print(f"El precio total es: {precio_total}")










