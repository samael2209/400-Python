# Desarrolla un programa que encuentre la tupla más común en una lista de tuplas

import random

contador = {}
t = [(random.randint(1,5),) for _ in range(20)]

for tupla in t:
    if tupla in contador:
        contador[tupla] += 1
    else:
        contador[tupla] = 1
    
mayor = max(contador, key=contador.get)

print("Lista:", t)
print("Conteo:", contador)
print("Más común:", mayor)
