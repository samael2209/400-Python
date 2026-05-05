# Diseña un programa que elimine 
# todas las claves con valores pares de un diccionario.

numeros = {k :k**2 for k in range(100)}

print(numeros)

numeros = {k: v for k,v in numeros.items() if v % 2 != 0 }

print(numeros)