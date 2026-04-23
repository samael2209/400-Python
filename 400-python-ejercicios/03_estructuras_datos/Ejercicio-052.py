# Calcular Histograma:
# Crea un histograma de letras a partir de una cadena de texto.

def histograma(txt:str)->dict:
    histograma = {}
    for caracter in txt:
        if caracter in histograma:
            histograma[caracter] += 1
        else:
            histograma[caracter] = 1
    return histograma

print(histograma("hhhhhhhhhhhjjjj"))