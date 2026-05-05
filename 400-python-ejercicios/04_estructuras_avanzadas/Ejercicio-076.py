# Crea una función que encuentre todas las claves que tienen valores
# iguales en dos diccionarios diferentes

numeros1 = {k:k for k in range(0,101, 3)}
numeros2 = {k:k for k in range(0,101)}

def claves_iguales(numeros1:dict, numeros2:dict) -> list:
    return [k for k in numeros1 if k in numeros2 and numeros1[k] == numeros2[k]]

def claves_iguales_optimizada(numeros1:dict, numeros2:dict) -> list:
    claves_comunes = numeros1.keys() & numeros2.keys()
    return [k for k in claves_comunes if numeros1[k] == numeros2[k] ]

