# Unir Listas en Diccionario: 
# Convierte dos listas en un diccionario, utilizando una como 
# claves y la otra como valores.

l_claves = ["a","e","i","o","u"]
l_valores = [1,2,3,4,5]

d1 = {l_claves[i]: l_valores[i] for i in range(len(l_claves))}

print(d1)