Algoritmo RegistroVacunas
    // Declarar contadores para cada vacuna y grupo de edad
    Definir faN, faA, vN, vA, mN, mA, hN, oN, oA, total Como Entero
    Definir nombre, vacuna, resp Como Cadena
    Definir edad Como Entero
	
    // Inicializar contadores
    faN <- 0
    faA <- 0
    vN <- 0
    vA <- 0
    mN <- 0
    mA <- 0
    hN <- 0
    oN <- 0
    oA <- 0
    total <- 0
	
    // Proceso de registro
    Repetir
        // Leer datos del usuario
        Escribir "Ingrese el nombre: "
        Leer nombre
        Escribir "Ingrese la edad: "
        Leer edad
        Escribir "Ingrese la vacuna (fa, v, m, h, otra): "
        Leer vacuna
		
        // Clasificar y contar según el grupo de edad y vacuna
        Si edad < 18 Entonces
            // Es niño
            Si vacuna = "fa" Entonces
                faN <- faN + 1
            Sino
                Si vacuna = "v" Entonces
                    vN <- vN + 1
                Sino
                    Si vacuna = "m" Entonces
                        mN <- mN + 1
                    Sino
                        Si vacuna = "h" Entonces
                            hN <- hN + 1
                        Sino
                            oN <- oN + 1
                        Fin Si
                    Fin Si
                Fin Si
            Fin Si
        Sino
            // Es adulto
            Si vacuna = "fa" Entonces
                faA <- faA + 1
            Sino
                Si vacuna = "v" Entonces
                    vA <- vA + 1
                Sino
                    Si vacuna = "m" Entonces
                        mA <- mA + 1
                    Sino
                        oA <- oA + 1
                    Fin Si
                Fin Si
            Fin Si
        Fin Si
		
        // Incrementar total
        total <- total + 1
		
        // Consultar si desea continuar
        Escribir "¿Desea continuar registrando? (SI/NO): "
        Leer resp
    Hasta Que resp = "NO"
	
    // Mostrar resultados
    Escribir "RESULTADOS DEL REGISTRO"
    Escribir "FA - Niños: ", faN, " Adultos: ", faA
    Escribir "V - Niños: ", vN, " Adultos: ", vA
    Escribir "M - Niños: ", mN, " Adultos: ", mA
    Escribir "H - Niños: ", hN
    Escribir "OTRAS - Niños: ", oN, " Adultos: ", oA
    Escribir "TOTAL VACUNAS: ", total
FinAlgoritmo