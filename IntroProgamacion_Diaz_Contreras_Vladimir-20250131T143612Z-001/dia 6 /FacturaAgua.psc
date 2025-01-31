Algoritmo FacturaAgua
    // Declaración de variables
    Definir nombreCliente, direccion, barrio Como Cadena
    Definir estrato, consumo Como Entero
    Definir valorMetroCubico, descuento, valorFactura, valorConDescuento, iva, totalAPagar Como Real
    
    // Asignar el valor fijo del metro cúbico
    valorMetroCubico <- 3000
    descuento <- 0
    
    // Leer datos del cliente
    Escribir "Ingrese el nombre del cliente: "
    Leer nombreCliente
    Escribir "Ingrese la dirección: "
    Leer direccion
    Escribir "Ingrese el barrio: "
    Leer barrio
    Escribir "Ingrese el estrato (1-4): "
    Leer estrato
    Escribir "Ingrese el consumo en metros cúbicos: "
    Leer consumo
	
    // Calcular el valor de la factura sin descuento
    valorFactura <- consumo * valorMetroCubico
	
    // Determinar el descuento según el estrato
    Segun estrato Hacer
        1: descuento <- valorFactura * 0.05
        2: descuento <- valorFactura * 0.04
        3: descuento <- valorFactura * 0.03
        4: descuento <- valorFactura * 0.02
        De Otro Modo: descuento <- 0
    Fin Segun
	
    // Calcular el valor con descuento y el IVA
    valorConDescuento <- valorFactura - descuento
    iva <- valorConDescuento * 0.10
    totalAPagar <- valorConDescuento + iva
	
    // Mostrar el resumen de pago
    Escribir "==============================="
    Escribir "NOMBRE CLIENTE: ", nombreCliente
    Escribir "DIRECCION: ", direccion
    Escribir "BARRIO: ", barrio
    Escribir "ESTRATO: ", estrato
    Escribir "METROS CUBICOS CONSUMIDOS: ", consumo
    Escribir "VALOR METRO CUBICO: $", valorMetroCubico
    Escribir "VALOR DEL DESCUENTO SI APLICA: $", descuento
    Escribir "VALOR IVA (10%): $", iva
    Escribir "TOTAL A PAGAR: $", totalAPagar
    Escribir "==============================="
FinAlgoritmo