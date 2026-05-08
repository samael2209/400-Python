# Escribe una función que calcule la intersección 
# de dos conjuntos sin utilizar el operador &. 

a = {6, 4, 5, 9}
b = {5, 6, 5, 9}

if len(a) > len(b):
    a, b = b, a

inteseccion = set()

for x in a:
    if x in b:
        inteseccion.add(x)
print(inteseccion)