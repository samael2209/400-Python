# Implementa un programa que encuentre el elemento que más se repite en una lista

import random

numeros = [random.randint(1,5) for _ in range(200)]
contador = {}

for n in numeros:
    if n in contador:
        contador[n] += 1
    else:
        contador[n] = 1

mayor = max(contador, key=contador.get)
print("Lista: ",numeros)
print("Mas comun: ",mayor)
print("Contador: ",contador)

    