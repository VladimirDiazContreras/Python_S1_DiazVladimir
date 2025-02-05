import json
from datos_inmuebles import inmuebles

# Archivo JSON para persistencia
ARCHIVO_JSON = "inmuebles.json"

# Función para calcular el precio del inmueble
def calcular_precio(inmueble):
    antiguedad = 2025 - inmueble['año']
    base = inmueble['metros'] * 1000 + inmueble['habitaciones'] * 5000 + (15000 if inmueble['garaje'] else 0)
    if inmueble['zona'] == 'A':
        precio = base * (1 - antiguedad / 100)
    elif inmueble['zona'] == 'B':
        precio = base * (1 - antiguedad / 100) * 1.5
    else:
        return None
    return round(precio, 2)

# Función para buscar inmuebles dentro de un presupuesto
def buscar_inmuebles(presupuesto):
    resultado = []
    for inmueble in inmuebles:
        precio = calcular_precio(inmueble)
        if precio and precio <= presupuesto:
            inmueble_con_precio = inmueble.copy()
            inmueble_con_precio['precio'] = precio
            resultado.append(inmueble_con_precio)
    return resultado

# Función para guardar los inmuebles en un archivo JSON
def guardar_datos():
    with open(ARCHIVO_JSON, 'w') as f:
        json.dump(inmuebles, f, indent=4)

# Función para cargar inmuebles desde un archivo JSON
def cargar_datos():
    global inmuebles
    try:
        with open(ARCHIVO_JSON, 'r') as f:
            inmuebles = json.load(f)
    except FileNotFoundError:
        guardar_datos()

# Función para agregar un inmueble
def agregar_inmueble():
    try:
        año = int(input("Año de construcción: "))
        metros = int(input("Metros cuadrados: "))
        habitaciones = int(input("Número de habitaciones: "))
        garaje = input("Tiene garaje? (s/n): ").strip().lower() == 's'
        zona = input("Zona (A/B): ").strip().upper()
        if zona not in ['A', 'B']:
            raise ValueError("Zona inválida.")
        nuevo_inmueble = {'año': año, 'metros': metros, 'habitaciones': habitaciones, 'garaje': garaje, 'zona': zona}
        inmuebles.append(nuevo_inmueble)
        guardar_datos()
        print("Inmueble agregado correctamente.")
    except ValueError as e:
        print(f"Error: {e}")

# Función para listar inmuebles
def listar_inmuebles():
    for i, inmueble in enumerate(inmuebles):
        print(f"{i + 1}. {inmueble}")

# Función para actualizar un inmueble
def actualizar_inmueble():
    listar_inmuebles()
    try:
        index = int(input("Ingrese el número del inmueble a actualizar: ")) - 1
        if index < 0 or index >= len(inmuebles):
            raise IndexError("Índice fuera de rango.")
        inmuebles[index]['año'] = int(input("Nuevo año de construcción: "))
        inmuebles[index]['metros'] = int(input("Nuevos metros cuadrados: "))
        inmuebles[index]['habitaciones'] = int(input("Nuevo número de habitaciones: "))
        inmuebles[index]['garaje'] = input("Tiene garaje? (s/n): ").strip().lower() == 's'
        inmuebles[index]['zona'] = input("Zona (A/B): ").strip().upper()
        guardar_datos()
        print("Inmueble actualizado correctamente.")
    except (ValueError, IndexError) as e:
        print(f"Error: {e}")

# Función para eliminar un inmueble
def eliminar_inmueble():
    listar_inmuebles()
    try:
        index = int(input("Ingrese el número del inmueble a eliminar: ")) - 1
        if index < 0 or index >= len(inmuebles):
            raise IndexError("Índice fuera de rango.")
        del inmuebles[index]
        guardar_datos()
        print("Inmueble eliminado correctamente.")
    except (ValueError, IndexError) as e:
        print(f"Error: {e}")

# Función del menú principal
def menu():
    cargar_datos()
    while True:
        print("\n--- MENÚ ---")
        print("1. Buscar inmuebles por presupuesto")
        print("2. Agregar un inmueble")
        print("3. Listar inmuebles")
        print("4. Actualizar un inmueble")
        print("5. Eliminar un inmueble")
        print("6. Salir")

        opcion = input("Seleccione una opción: ").strip()
        
        if opcion == '1':
            try:
                presupuesto = float(input("Ingrese su presupuesto: "))
                resultado = buscar_inmuebles(presupuesto)
                if resultado:
                    print("\nInmuebles dentro del presupuesto:")
                    for r in resultado:
                        print(r)
                else:
                    print("No hay inmuebles en ese rango de precio.")
            except ValueError:
                print("Presupuesto inválido.")

        elif opcion == '2':
            agregar_inmueble()
        
        elif opcion == '3':
            listar_inmuebles()
        
        elif opcion == '4':
            actualizar_inmueble()
        
        elif opcion == '5':
            eliminar_inmueble()
        
        elif opcion == '6':
            print("Saliendo del programa.")
            break
        
        else:
            print("Opción no válida. Intente de nuevo.")

# Ejecutar el menú si el script es ejecutado directamente
if __name__ == "__main__":
    menu()
