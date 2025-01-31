Algoritmo primos
	Definir n, i Como Entero
	Escribir "Ingrese un número:"
	Leer n
	
	Si n <= 1 Entonces
		Escribir "no es primo."
	Sino
		Si n = 2 Entonces
			Escribir " es primo."
		Sino
			Si n Mod 2 = 0 Entonces
				Escribir "no es primo."
			Sino
				Escribir "es primo."
				Para i = 3 Hasta Raiz(n) Con Paso 2 Hacer
					Si n Mod i = 0 Entonces
						Escribir " no es primo."
					FinSi
				FinPara
			FinSi
		FinSi
	FinSi
	
FinAlgoritmo
