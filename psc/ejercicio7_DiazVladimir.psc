Algoritmo PromedioLista
    Definir n, i, suma, promedio, numero Como Entero
	
    Escribir "Ingrese la cantidad de n�meros en la lista:"
    Leer n
	
    suma <- 0
	
    Para i <- 1 Hasta n Hacer
        Escribir "Ingrese el n�mero ", i, ":"
        Leer numero
        suma <- suma + numero
    FinPara
	
    promedio <- suma / n
	
    Escribir "El promedio de la lista es: ", promedio
FinAlgoritmo