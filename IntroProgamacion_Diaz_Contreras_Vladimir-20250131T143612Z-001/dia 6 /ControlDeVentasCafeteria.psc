Algoritmo ControlDeVentasCafeteria
    Definir empanada_trigo, empanada_yuca, buñuelos, papas, gaseosa, speedmax Como Entero
    Definir opcion, cantidad, total_general Como Entero
    Definir precio Como Real
	
    empanada_trigo <- 0
    empanada_yuca <- 0
    buñuelos <- 0
    papas <- 0
    gaseosa <- 0
    speedmax <- 0
    total_general <- 0
	
    Repetir
        Escribir "Seleccione un producto:"
        Escribir "1. Empanadas de trigo con pollo - $3000"
        Escribir "2. Empanadas de yuca con pollo y queso - $3000"
        Escribir "3. Buñuelos - $2500"
        Escribir "4. Papas rellenas - $4500"
        Escribir "5. Gaseosa - $2000"
        Escribir "6. Speedmax - $2000"
        Escribir "7. Finalizar jornada"
        Leer opcion
		
        Si opcion = 7 Entonces
            Escribir "Fin de la jornada."
            Escribir "Total recaudado: $", total_general
            Escribir "Empanadas de trigo con pollo: $", empanada_trigo
            Escribir "Empanadas de yuca con pollo: $", empanada_yuca
            Escribir "Buñuelos: $", buñuelos
            Escribir "Papas rellenas: $", papas
            Escribir "Gaseosa: $", gaseosa
            Escribir "Speedmax: $", speedmax
            Escribir "TOTAL RECAUDADO: $", total_general
        Sino
            Si opcion >= 1 Y opcion <= 6 Entonces
                Escribir "Ingrese la cantidad: "
                Leer cantidad
				
                Segun opcion Hacer
                    Caso 1:
                        precio <- 3000
                        empanada_trigo <- empanada_trigo + (precio * cantidad)
                        total_general <- total_general + (precio * cantidad)
                    Caso 2:
                        precio <- 3000
                        empanada_yuca <- empanada_yuca + (precio * cantidad)
                        total_general <- total_general + (precio * cantidad)
                    Caso 3:
                        precio <- 2500
                        buñuelos <- buñuelos + (precio * cantidad)
                        total_general <- total_general + (precio * cantidad)
                    Caso 4:
                        precio <- 4500
                        papas <- papas + (precio * cantidad)
                        total_general <- total_general + (precio * cantidad)
                    Caso 5:
                        precio <- 2000
                        gaseosa <- gaseosa + (precio * cantidad)
                        total_general <- total_general + (precio * cantidad)
                    Caso 6:
                        precio <- 2000
                        speedmax <- speedmax + (precio * cantidad)
                        total_general <- total_general + (precio * cantidad)
                FinSegun
            Sino
                Escribir "Opción no válida. Intente nuevamente."
            FinSi
        FinSi
    Hasta Que opcion = 7
FinAlgoritmo
