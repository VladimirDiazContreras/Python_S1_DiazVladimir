Algoritmo Fibonacci
    Definir n, a, b, siguiente, i Como Entero
	
    Escribir "Ingrese el n�mero de t�rminos de la serie Fibonacci que desea ver:"
    Leer n
	
    a <- 0
    b <- 1
    Escribir "Serie Fibonacci: "
	
    Para i <- 1 Hasta n Hacer
        Escribir a
        siguiente <- a + b
        a <- b
        b <- siguiente
    FinPara
FinAlgoritmo