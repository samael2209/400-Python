# Diseña un programa que encuentre todos los elementos 
# únicos en una lista y los almacene en un conjunto

import random

l_numeros = [random.randint(1,3) for _ in range(20)]

unicos = set()

for n in l_numeros:
    unicos.add(n)

print(unicos)