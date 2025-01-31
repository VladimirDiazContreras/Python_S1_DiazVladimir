Algoritmo Quiz_Solucion
	// Definición de variables
	Definir edad, duracionTrayecto Como Entero
	Definir tarifaBase, descuento, cargoAdicional, costoTotal Como Real
	Definir esEstudiante, esVeterano, asientoPremium, validoDescuento Como Cadena
	Escribir 'Ingrese la edad del pasajero:' // Para decir si SI=S o NO=N
	Leer edad
	// OPCIONAL : Verificar la edad si se corrigió, pero solamente manda un mensaje 
	Si edad<0 O edad>116 Entonces
		Escribir 'Error: La edad ingresada no es válida'
	FinSi
	// Solicita los datos al usuario ,exactamente como lo pide el enunciado
	Escribir '¿Es estudiante? (S/N):'
	Leer esEstudiante
	Escribir '¿Es veterano de guerra? (S/N):'
	Leer esVeterano
	Escribir 'Ingrese la duración del trayecto (en horas):'
	Leer duracionTrayecto
	Escribir '¿Desea asiento premium? (S/N):'
	Leer asientoPremium
	// Determinar tarifa base segun la edad
	Si edad>=18 Y edad<=59 Entonces
		tarifaBase <- 100
	SiNo
		Si edad>=3 Y edad<=17 Entonces
			tarifaBase <- 50
		SiNo
			Si edad>=60 Entonces
				tarifaBase <- 80
			SiNo
				Si edad>=0 Y edad<=2 Entonces
					// Edad entre 0 y 2 años
					tarifaBase <- 0
				FinSi
			FinSi
		FinSi
	FinSi
	// Calcular descuesnto
	descuento <- 0
	Si esVeterano='S' Y esEstudiante='S' Entonces
		Escribir 'Estimado, no puedes mezclar descuentos :sad:'
	SiNo
		Si esVeterano='S' Entonces
			descuento <- tarifaBase*0.5
			validoDescuento = "V"
		SiNo
			Si esEstudiante='S' Entonces
				descuento <- tarifaBase*0.2
				validoDescuento = "E"
			FinSi
		FinSi
	FinSi
	// Cargos adicionales
	cargoAdicional <- 0
	Si duracionTrayecto>5 Entonces
		cargoAdicional <- (tarifaBase-descuento)*0.15
	FinSi
	Si asientoPremium='S' Entonces
		cargoAdicional = cargoAdicional + 30
	FinSi
	// Calcular costo total
	costoTotal <- tarifaBase-descuento+cargoAdicional
	// Mostrar Resultados
	Escribir 'Tarifa base:', tarifaBase, ' USD' // BASADO EN PEMDAS
	Si validoDescuento='E' Entonces
		Escribir 'Descuento por estudiante:', descuento, ' USD'
	SiNo
		Si validoDescuento='V' Entonces
			Escribir 'Descuento por veterano:', descuento, ' USD'
		FinSi
	FinSi
	
	Si asientoPremium='S' Entonces
		Escribir 'Cargo adicional por trayecto largo:', cargoAdicional-30, ' USD'
		Escribir 'Cargo por asiento premium: 30 USD'
	SiNo
		Escribir 'Cargo adicional por trayecto largo:', cargoAdicional, ' USD'
	FinSi
	Escribir 'Costo total del boleto:', costoTotal, ' USD'
FinAlgoritmo
