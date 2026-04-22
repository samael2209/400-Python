# Eliminar Claves: 
# Escribe una función que elimine las claves de un diccionario 
# si su valor es mayor que un cierto umbral.

numeros = {
    "Diez mil": 10000,
    "Uno" : 1,
    "Cien" : 100,
    "Mil" : 1000,
    "dos" : 2
}

def eliminar_clave(d1:dict) -> dict:
    umbral = 20
    m = {k: v for k, v in d1.items() if v < umbral}
    return m


print(eliminar_clave(numeros))
    