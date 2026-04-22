# Valor Mínimo y Máximo: 
# Encuentra el valor mínimo y máximo en un diccionario de números.

numeros = {
    "Diez mil": 10000,
    "Uno" : 1,
    "Cien" : 100,
    "Mil" : 1000
}

def min_max(numeros:dict):
    
    valores = list(numeros.values())
    
    maximo = valores[0]
    for v in valores:
        if v > maximo:
            maximo = v

    minimo = valores[0]
    for v in valores:
        if v < minimo:
            minimo = v
    
    return [maximo, minimo]

print(min_max(numeros))


    