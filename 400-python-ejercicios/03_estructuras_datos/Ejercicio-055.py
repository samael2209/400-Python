# Ordenar Diccionario: 
# Ordena un diccionario por sus claves o valores.

Original= {'z': 3, 'a': 1, 'm': 5, 'b': 2}

def ordenar_por_claves(dic: dict):
    claves = list(dic.keys())
    for i in range(len(claves)):
        for j in range(i + 1, len(claves)):
            if claves[i] > claves[j]:
                claves[i], claves[j] = claves[j], claves[i]
    return {k: dic[k] for k in claves}
    


def ordenar_por_valores(dic: dict):
    items = list(dic.items())
    for i in range(len(items)):
        for j in range(i + 1, len(items)):
            if items[i][1] > items[j][1]:
                items[i], items[j] = items[j], items[i]
    return {k: v for k, v in items}


def main():
    diccionario = {
        "z": 3,
        "a": 1,
        "m": 5,
        "b": 2
    }
    
    print("Original:", diccionario)
    print("Por claves:", ordenar_por_claves(diccionario))
    print("Por valores:", ordenar_por_valores(diccionario))
main()