# Unir Diccionarios: 
# Combina dos diccionarios en uno solo.

def unir_diccionarios(d1:dict, d2:dict):
    resultado = {}
    for clave, valor in d1.items():
        resultado[clave] = valor
    for clave, valor in d2.items():
        resultado[clave] = valor
    return resultado

def main():
    d1 = {"a": 1, "b": 2}
    d2 = {"c": 3, "d": 4}
    print(unir_diccionarios(d1, d2))
main()