# Diseña una función que divida una lista en sub-listas de tamaño fijo

import random as r

#Definimos la lista
l = [r.randint(1,6) for _ in range(40)]

#tamano definiod
tam = 9

#Lista resultante
resultado = []
#bloques en los cuales se guarda los numeros
bloque = []


contador = 0

#iteramos cada elemento en la lista original
for elemento in l:

    # cada numero lo agregamos al bloqe
    bloque.append(elemento)
    #aumentamos el cotador
    contador += 1

    # comparamos el numero del contador con el tamano que definimos 
    if contador == tam:
        # si son iguales agregamos el bloque a resultado
        resultado.append(bloque)

        # reiniciamos el bloqe y el contador
        bloque = []
        contador = 0

# guardamos los numeros sobrantes
if bloque:
    resultado.append(bloque)

print(resultado)


l = [r.randint(1,6) for _ in range(40)]

tama = 3

cantidad_bloques = (len(l) + tam - 1) // tama

resultado = [None] * cantidad_bloques

i = 0
j = 0

bloque = [None] * tama

for elemento in l:
    bloque[j] = elemento
    j += 1
    
    if j == tama:
        
        resultado[i] = bloque
        
        bloque = [None] * tama
        
        i += 1
        j = 0

if j > 0:
    resultado[i] = bloque[:j]

print(resultado)