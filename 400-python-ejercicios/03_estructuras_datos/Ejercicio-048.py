# Eliminar Duplicados: 
# Elimina los elementos duplicados de una lista y almacénalos en un 
# diccionario.

mi_lista = [1,1,1,2,2,3,3,3,3,4,5,6,7,8,9]

def eliminar_duplicados(listaNumeros:list) -> tuple:
    conteo = {}
    for elemento in listaNumeros:
        if elemento in conteo:
            conteo[elemento] += 1
        else: 
            conteo[elemento] = 1
    n = set(mi_lista)
    return {elem: cant for elem, cant in conteo.items() if cant > 1}, n


r , n = eliminar_duplicados(mi_lista)
print(r)
print(n)