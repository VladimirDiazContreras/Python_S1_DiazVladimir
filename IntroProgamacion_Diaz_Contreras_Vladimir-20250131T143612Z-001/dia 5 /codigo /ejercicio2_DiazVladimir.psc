Algoritmo mayordetres
	definir num1, num2, num3 como entero 
	Escribir "ingresa el primer numero" 
	Leer num1 
	Escribir "ingresa el segundo numero" 
	Leer num2
	Escribir "ingresa el tercer numero "
	Leer num3
	Si (num1>=num2) y (num1>=num3) Entonces
		Escribir 'el numero mallor es:' , num1
	SiNo
		Si (num2>=num1) y (num2>=num3)  Entonces
			Escribir 'elnumero mayor es:', num2
		SiNo
			Escribir 'el numero mayor es :', num3
		FinSi
	FinSi
FinAlgoritmo
