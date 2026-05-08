# Crea una función que divida 
# una lista de números en dos listas de tuplas, 
# una con números pares y otra con números impares. 

lista_numeros = [i for i in range(50)]

#Primera forma
lis_pares = []
lis_impares = []

for n in lista_numeros:
    if n % 2 == 0:
        lis_pares.append((n,))
    else:
        lis_impares.append((n,))

#Segunda forma
lista_pares = [(j,) for j in lista_numeros if j % 2 == 0]

lista_impares = [(k,) for k in lista_numeros if k % 2 != 0]

#Tercera forma
from collections import defaultdict
resultado = defaultdict(list)

for n in lista_numeros:
    clave = "pares" if n % 2 == 0 else "impares"
    resultado[clave].append((n,))

print("Pares", resultado['pares'])
print("Impares", resultado['impares'])