# Listas de nombres y apellidos
nombres = [
    ["Adrián"], ["Alejandra"], ["Ámbar", "Isabella"], ["Andrés", "David"],
    ["Aura", "Camila"], ["Camilo", "Andrés"], ["Daniel", "Esteban"],
    ["David", "Santiago"], ["Edgar", "Leonardo"], ["Gerson", "Steven"],
    ["Harley", "Yefrey"], ["John", "Stiven"], ["Juan", "David"], ["Juan", "David"],
    ["Juan", "David"], ["Juan", "Eduardo"], ["Juan", "Fernando"], ["Juan", "Jose"],
    ["Maria", "Juliana"], ["Mateo", "Roman"], ["Naya", "Zarela"], ["Nicolas"],
    ["Omar", "Fernando"], ["Santiago"], ["Santiago", "Andrés"], ["Santiago"],
    ["Sara", "Sofía"], ["Sayara", "Yurley"], ["Sergio", "Andrés"],
    ["Simón", "Dante"], ["Thomas", "Sebastián"], ["Vladimir"]
]

apellidos = [
    ["Quintero", "Pinzón"], ["Pinzón", "Alvarez"], ["Plata", "López"],
    ["Reyes", "Espinel"], ["Pico", "Araque"], ["Suárez", "Fuentes"],
    ["Guerrero", "Quintero"], ["Vera", "Mendez"], ["Acevedo", "Arteaga"],
    ["Chaparro", "Martínez"], ["Cabrales", "Vargas"], ["Negron", "Regalado"],
    ["Saavedra", "Jaimez"], ["Santoyo", "Jaimes"], ["Vargas", "Soto"],
    ["Pinilla", "Guzmán"], ["Umaña", "Barragan"], ["Abril", "Roman"],
    ["Saavedra", "Mejia"], ["Camargo"], ["Lizcano", "Jaimes"], ["Chedraui", "Mantilla"],
    ["Granados", "Parra"], ["Aguilar", "Vesga"], ["Quiñonez", "Sosa"],
    ["Jaimes", "Perez"], ["Díaz", "Rodríguez"], ["Aparicio", "Arciniegas"],
    ["Rueda", "Hernández"], ["Salamanca", "Galvis"], ["Bastos", "Garcia"],
    ["Diaz", "Contreras"]
]

def mostrar_estudiantes():
    """Muestra la lista de estudiantes."""
    print("\nLista de estudiantes:")
    for i in range(len(nombres)):
        nombre_completo = " ".join(nombres[i])
        apellido_completo = " ".join(apellidos[i]) if i < len(apellidos) else "[Apellido no disponible]"
        print(f"{i + 1}. {nombre_completo} {apellido_completo}")

def agregar_estudiante():
    """Agrega un nuevo estudiante a las listas."""
    nombre = input("Ingrese el nombre(s) del estudiante (separado por espacios): ").split()
    apellido = input("Ingrese el apellido(s) del estudiante (separado por espacios): ").split()
    nombres.append(nombre)
    apellidos.append(apellido)
    print("\nEstudiante agregado con éxito.")

def editar_estudiante():
    """Edita un estudiante existente."""
    mostrar_estudiantes()
    try:
        num = int(input("\nIngrese el número del estudiante a editar: ")) - 1
        if 0 <= num < len(nombres):
            nombres[num] = input("Nuevo nombre(s): ").split()
            apellidos[num] = input("Nuevo apellido(s): ").split()
            print("\nEstudiante editado con éxito.")
        else:
            print("\nNúmero inválido.")
    except ValueError:
        print("\nError: Ingrese un número válido.")

def eliminar_estudiante():
    """Elimina un estudiante de la lista."""
    mostrar_estudiantes()
    try:
        num = int(input("\nIngrese el número del estudiante a eliminar: ")) - 1
        if 0 <= num < len(nombres):
            nombres.pop(num)
            apellidos.pop(num)
            print("\nEstudiante eliminado con éxito.")
        else:
            print("\nNúmero inválido.")
    except ValueError:
        print("\nError: Ingrese un número válido.")

def menu():
    """Muestra el menú principal y gestiona las opciones del usuario."""
    while True:
        print("\nBienvenido al programa de lista de estudiantes")
        print("1. Agregar estudiante")
        print("2. Ver lista de estudiantes")
        print("3. Editar estudiante")
        print("4. Eliminar estudiante")
        print("5. Salir")

        opcion = input(": ")

        if opcion == "1":
            agregar_estudiante()
        elif opcion == "2":
            mostrar_estudiantes()
        elif opcion == "3":
            editar_estudiante()
        elif opcion == "4":
            eliminar_estudiante()
        elif opcion == "5":
            print("\nSaliendo del programa...")
            break
        else:
            print("\nOpción no válida, intente de nuevo.")

# Ejecutar el menú principal
menu()