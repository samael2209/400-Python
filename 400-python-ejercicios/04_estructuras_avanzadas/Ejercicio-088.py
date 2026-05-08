# Escribe una función que elimine elementos duplicados 
# de una lista sin cambiar su orden.
import random 

l1 = [random.randint(1,7) for _ in range(30)]

r = []
vistos = set()

for x in l1:
    
    if x not in vistos:
        r.append(x)
        vistos.add(x)

print("Original:", l1)
print("Sin duplicados:", r)