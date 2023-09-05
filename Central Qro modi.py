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
# Dar el precio
print(f"El precio para ir a ", ubicacion_elegida,f"es : {calcular_precio(ubicacion_elegida, precios)}")
