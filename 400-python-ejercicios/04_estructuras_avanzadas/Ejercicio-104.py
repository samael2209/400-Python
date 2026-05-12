# Implementa una función que elimine duplicados de una lista manteniendo el 
# orden original y almacene los elementos únicos en un conjunto.

import random 

numeros = [random.randint(0,4) for _ in range(13)]

def remover_duplicados(numeros:list)->tuple:
    if not numeros:
        return [], set()
    
    unicos = []
    vistos = set()
    
    for numero in numeros:
        
        if numero not in vistos:
            unicos.append(numero)
            vistos.add(numero)
    
    return unicos, vistos

print("Lista original:")
print(numeros)

lista_unica, conjunto = remover_duplicados(numeros)

print("\nLista sin duplicados:")
print(lista_unica)

print("\nConjunto de elementos únicos:")
print(conjunto)