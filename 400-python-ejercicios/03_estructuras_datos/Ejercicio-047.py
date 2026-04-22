# Contar Palabras: 
# Dada una cadena de texto, crea un diccionario que cuente cuántas veces 
# aparece cada palabra.

def contar_palabras(palabras:str) -> dict:
    contador = {}
    palabra = palabras.split(" ")
    for i in palabra:

        if i in contador:
            contador[i] += 1
        else:
            contador[i] = 1
    return contador


c = contar_palabras("Jordy Jordy Jordy hola hola popo estrella lopez")
print(c)