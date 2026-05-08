# Implementa una función 
# que encuentre la tupla con la mayor suma 
# de elementos en una lista de tuplas.


t = [(1, 2), (3, 4), (0, 10), (2, 2)]

tupla_mayor = None
suma_mayor = float("-inf")

for tupla in t:
    s = sum(tupla)

    if s > suma_mayor:
        tupla_mayor = tupla
        suma_mayor = s
    

print(tupla_mayor)