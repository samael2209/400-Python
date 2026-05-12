# Implementa una función que tome una lista de números y devuelva una tupla con el 
# valor mínimo y máximo.
import random as rd

numeros = [rd.randint(20, 50) ** 2 for i in range(9)]

print(numeros)


def tupla_max_min(numeros: list) -> tuple:

    mayor = numeros[0]
    menor = numeros[0]

    for numero in numeros:

        if numero > mayor:
            mayor = numero

        if numero < menor:
            menor = numero

    # primero mínimo, luego máximo
    return menor, mayor


print(tupla_max_min(numeros))