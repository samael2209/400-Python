# Diccionario de Frequencias: 
# Dada una lista de números, crea un diccionario que muestre 
# cuántas veces aparece cada número.

def frecuencia(numeros:list) -> dict:
    contador = {}
    for n in numeros:
        if n in contador:
            contador[n] += 1
        else:
            contador[n] = 1
    return contador

numeros = [1,2,2,2,2,4,5,6,7,7,8,8]
print(frecuencia(numeros))
