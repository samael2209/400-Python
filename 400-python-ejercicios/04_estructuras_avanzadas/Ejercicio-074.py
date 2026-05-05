# Implementa una función que fusione dos diccionarios 
# sin utilizar el operador de actualización (update)

numeros:dict = {
    1 : "uno",
    2 : "dos",
    100 : "cien",
    1000 : "mil"
}

numeros2:dict = {
    3 : "uno",
    4 : "dos",
    500 : "cien",
    9000 : "mil"
}

resultado = {
    k: numeros2[k] if k in numeros2 else numeros[k]
    for k in set(numeros) | set(numeros2)
}

print(resultado)

