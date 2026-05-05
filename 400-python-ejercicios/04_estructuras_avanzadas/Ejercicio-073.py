# Crea un programa que encuentre la clave 
# con el valor máximo en un diccionario de números enteros.

numeros = {
    1 : "uno",
    2 : "dos",
    100 : "cien",
    1000 : "mil"
}

valores = list(numeros.keys())

maximo = valores[0]
for v in valores:
    if v > maximo:
        maximo = v

print(maximo)