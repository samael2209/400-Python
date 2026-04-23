# Eliminar Clave: 
# Elimina una clave específica de un diccionario si existe

diccionario = {"n": 2, "m": 3}

def eliminar_clave(d1:dict, clave):
    if clave in d1:
        del d1[clave]
        return d1
    return "No se encontro la clave"

print(eliminar_clave(diccionario,"p"))

        