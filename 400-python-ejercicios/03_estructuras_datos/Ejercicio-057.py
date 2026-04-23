# Buscar Clave: 
# Escribe una función que busque una clave en un diccionario y devuelva su 
# valor o un mensaje de error si no se encuentra.

diccionario = {"n": 2, "m": 3}

def buscar_clave(d1:dict, clave):
    if clave in d1:
        return d1[clave]
    return "No se encontro la clave"

        
    
print(buscar_clave(diccionario, "n")) 
print(buscar_clave(diccionario, "p"))