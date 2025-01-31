Algoritmo MayorYMenor
    Definir num1, num2, num3 Como Entero
    
    Escribir "Ingresa el primer número: "
    Leer num1
    Escribir "Ingresa el segundo número: "
    Leer num2
    Escribir "Ingresa el tercer número: "
    Leer num3
	
    // Determinar el mayor
    Si (num1 > num2) Y (num1 > num3) Entonces
        Escribir "El mayor es: ", num1
    Sino
        Si (num2 > num1) Y (num2 > num3) Entonces
            Escribir "El mayor es: ", num2
        Sino
            Escribir "El mayor es: ", num3
        FinSi
    FinSi
	
    // Determinar el menor
    Si (num1 < num2) Y (num1 < num3) Entonces
        Escribir "El menor es: ", num1
    Sino
        Si (num2 < num1) Y (num2 < num3) Entonces
            Escribir "El menor es: ", num2
        Sino
            Escribir "El menor es: ", num3
        FinSi
    FinSi
FinAlgoritmo