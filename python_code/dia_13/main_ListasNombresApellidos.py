## lista de nombres y apellidos en la que se pueden cambiar nombres y apellidos 
nombres = [
    ["Adrián"],
    ["Alejandra"],
    ["Ámbar", "Isabella"],
    ["Andrés", "David"],
    ["Aura", "Camila"],
    ["Camilo", "Andrés"],
    ["Daniel", "Esteban"],
    ["David", "Santiago"],
    ["Edgar", "Leonardo"],
    ["Gerson", "Steven"],
    ["Harley", "Yefrey"],
    ["John", "Stiven"],
    ["Juan", "David"],
    ["Juan", "David"],
    ["Juan", "David"],
    ["Juan", "Eduardo"],
    ["Juan", "Fernando"],
    ["Juan", "Jose"],
    ["Maria", "Juliana"],
    ["Mateo", "Roman"],
    ["Naya", "Zarela"],
    ["Nicolas"],
    ["Omar", "Fernando"],
    ["Santiago"],
    ["Santiago", "Andrés"],
    ["Santiago"],
    ["Sara", "Sofía"],
    ["Sayara", "Yurley"],
    ["Sergio", "Andrés"],
    ["Simón", "Dante"],
    ["Thomas", "Sebastián"],
    ["Vladimir"]
]

apellidos = [
    ["Quintero", "Pinzón"],
    ["Pinzón", "Alvarez"],
    ["Plata", "López"],
    ["Reyes", "Espinel"],
    ["Pico", "Araque"],
    ["Suárez", "Fuentes"],
    ["Guerrero", "Quintero"],
    ["Vera", "Mendez"],
    ["Acevedo", "Arteaga"],
    ["Chaparro", "Martínez"],
    ["Cabrales", "Vargas"],
    ["Negron", "Regalado"],
    ["Saavedra", "Jaimez"],
    ["Santoyo", "Jaimes"],
    ["Vargas", "Soto"],
    ["Pinilla", "Guzmán"],
    ["Umaña", "Barragan"],
    ["Abril", "Roman"],
    ["Saavedra", "Mejia"],
    ["Camargo"],
    ["Lizcano", "Jaimes"],
    ["Chedraui", "Mantilla"],
    ["Granados", "Parra"],
    ["Aguilar", "Vesga"],
    ["Quiñonez", "Sosa"],
    ["Jaimes", "Perez"],
    ["Díaz", "Rodríguez"],
    ["Aparicio", "Arciniegas"],
    ["Rueda", "Hernández"],
    ["Salamanca", "Galvis"],
    ["Bastos", "Garcia"],
    ["Diaz", "Contreras"]
]

booleanito = True
while booleanito:
    print("\nBienvenido al programa de lista de estudiantes")
    print("¿Qué te gustaría hacer?")
    print("1. Agregar nombres")
    print("2. Ver nombres")
    print("3. Editar nombres")
    print("4. Eliminar nombres")
    print("5. Agregar apellidos")
    print("6. Editar apellidos")
    print("7. Eliminar apellidos")
    print("8. Salir del programa")
    
    opcionUsuario = int(input(": "))
    
    if opcionUsuario == 2:
        print("Lista de estudiantes:")
        for i in range(len(nombres)):
            if i < len(apellidos):  # Asegúrate de que ambas listas estén sincronizadas
                print(f"Estudiante #{i+1}: {nombres[i]} {apellidos[i]}")
            else:
                print(f"Estudiante #{i+1}: {nombres[i]} [Apellido no disponible]")

    elif opcionUsuario == 8:
        booleanito = False
        break

    elif opcionUsuario == 1:
        nombreEstudiante = input("¿Qué nombre te gustaría agregarle a los nombres?: ")
        nombres.append([nombreEstudiante])
        apellidoEstudiante = input("¿Qué apellido te gustaría agregarle al estudiante?: ")
        apellidos.append([apellidoEstudiante])
        print("Lista nueva de estudiantes:")
        for i in range(len(nombres)):
            if i < len(apellidos):
                print(f"Estudiante #{i+1}: {nombres[i]} {apellidos[i]}")
            else:
                print(f"Estudiante #{i+1}: {nombres[i]} [Apellido no disponible]")

    elif opcionUsuario == 3:
        print("Lista de estudiantes:")
        for i in range(len(nombres)):
            if i < len(apellidos):
                print(f"Estudiante #{i+1}: {nombres[i]} {apellidos[i]}")
            else:
                print(f"Estudiante #{i+1}: {nombres[i]} [Apellido no disponible]")
        numeroEstudiante = int(input("¿Qué estudiante quieres editar? (Número): "))
        nombreEstudianteNuevo = input("¿Cuál será el nombre nuevo?: ")
        apellidosEstudianteNuevo = input("¿Cuál será el apellido nuevo?: ")
        nombres[numeroEstudiante-1] = [nombreEstudianteNuevo]
        apellidos[numeroEstudiante-1] = [apellidosEstudianteNuevo]

    elif opcionUsuario == 4:
        print("Lista de estudiantes:")
        for i in range(len(nombres)):
            if i < len(apellidos):
                print(f"Estudiante #{i+1}: {nombres[i]} {apellidos[i]}")
            else:
                print(f"Estudiante #{i+1}: {nombres[i]} [Apellido no disponible]")
        numeroEstudiante = int(input("¿Qué estudiante quieres eliminar? (Número): "))
        nombres.pop(numeroEstudiante-1)
        apellidos.pop(numeroEstudiante-1)

    elif opcionUsuario == 5:
        nombreEstudiante = input("¿Qué apellido te gustaría agregarle al estudiante?: ")
        apellidos.append([nombreEstudiante])
        print("Lista nueva de estudiantes:")
        for i in range(len(nombres)):
            if i < len(apellidos):
                print(f"Estudiante #{i+1}: {nombres[i]} {apellidos[i]}")
            else:
                print(f"Estudiante #{i+1}: {nombres[i]} [Apellido no disponible]")

    elif opcionUsuario == 6:
        print("Lista de estudiantes:")
        for i in range(len(nombres)):
            if i < len(apellidos):
                print(f"Estudiante #{i+1}: {nombres[i]} {apellidos[i]}")
            else:
                print(f"Estudiante #{i+1}: {nombres[i]} [Apellido no disponible]")
        numeroEstudiante = int(input("¿Qué estudiante quieres editar? (Número): "))
        apellidoEstudianteNuevo = input("¿Cuál será el apellido nuevo?: ")
        apellidos[numeroEstudiante-1] = [apellidoEstudianteNuevo]

    elif opcionUsuario == 7:
        print("Lista de estudiantes:")
        for i in range(len(nombres)):
            if i < len(apellidos):
                print(f"Estudiante #{i+1}: {nombres[i]} {apellidos[i]}")
            else:
                print(f"Estudiante #{i+1}: {nombres[i]} [Apellido no disponible]")
        numeroEstudiante = int(input("¿De qué estudiante quieres eliminar el apellido  ? (Número): "))
        apellidos.pop(numeroEstudiante-1)
## desarrollado por : vladimir diaz contreras Ti: 1096066731
