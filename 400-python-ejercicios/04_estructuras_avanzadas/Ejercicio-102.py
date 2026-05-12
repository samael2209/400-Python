# Escribe una función que encuentre el elemento más común en una lista de 
# tuplas y muestre cuántas veces aparece. 

datos = [
    ("manzana", "rojo"),
    ("pera", "verde"),
    ("manzana", "rojo"),
    ("uva", "morado"),
    ("pera", "verde"),
    ("manzana", "rojo"),
    ("kiwi", "verde")
]

contador = {}

for dato in datos:
    if dato in contador:
        contador[dato] += 1
    else:
        contador[dato] = 1

elemento = max(contador, key=contador.get)

print("Elemento más común:", elemento)
print("Cantidad de veces:", contador[elemento])