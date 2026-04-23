# Contar Vocales: 
# Cuenta cuántas vocales hay en una cadena de texto y
# almacena el resultado en un diccionario.

def contar_vocales(txt:str)->dict:
    vocales = "aeiou"
    contador = {}
    for vocal in txt.lower():
        if vocal in vocales:
            if vocal in contador:
                contador[vocal] += 1
            else:
                contador[vocal] = 1
    return contador

print(contar_vocales("hola como estas hoy")) 