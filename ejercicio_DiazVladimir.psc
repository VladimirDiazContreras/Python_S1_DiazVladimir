Algoritmo TablaDeMultiplicar
    Definir n, i, resultado Como Entero
	
    Escribir "Ingrese el n�mero para generar su tabla de multiplicar:"
    Leer n
	
    Escribir "Tabla de multiplicar de ", n, ":"
	
    Para i <- 1 Hasta 10 Hacer
        resultado <- n * i
        Escribir n, " x ", i, " = ", resultado
    FinPara
FinAlgoritmo