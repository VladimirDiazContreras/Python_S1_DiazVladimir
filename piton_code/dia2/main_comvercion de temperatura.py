def convertir_temperatura(valor,escala):
    try:
        ## es para dectectar errores 
        valor= float(valor)
        if escala.lower()=='c':
            ## el lower es para comparar texto sin importar las mayusculas 
            return(valor * 9/5)+32
        ## da el valor de celsius a frha
        elif escala.lower ()=='f':
            return(valor-32)*5/9
        ## frha a cels
        else :
            return "escala no valida. uas 'c' o 'f' "
    except ValueError:
        return "entrada invalida." 
print(convertir_temperatura(100,'C'))


