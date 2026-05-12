# Desarrolla una función que encuentre la intersección de múltiples conjuntos 
# almacenados en un diccionario.

conjuntos = {
    "grupo_1": {1, 2, 3, 4, 5},
    "grupo_2": {3, 4, 5, 6, 7},
    "grupo_3": {2, 3, 4, 5, 8},
    "grupo_4": {0, 3, 4, 5, 9}
}


def encontrar_interseccion(diccionario: dict) -> set:

    valores = list(diccionario.values())

    primer_conjunto = valores[0]

    resultado = set()

    for numero in primer_conjunto:

        comun = True

        for conjunto in valores[1:]:

            if numero not in conjunto:
                comun = False
                break

        if comun:
            resultado.add(numero)

    return resultado


resultado = encontrar_interseccion(conjuntos)

print(resultado)