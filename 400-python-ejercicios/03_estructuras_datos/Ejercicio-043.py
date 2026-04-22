# Contar Elementos: 
# Escribe una función que cuente cuántas veces aparece cada elemento 
# en una lista y lo almacene en un diccionario.

def contarElemento(elementos:list) -> dict:
    contador = {}
    for i in elementos:
        if i in contador:
            contador[i] += 1
        else:
            contador[i] = 1
    return contador

def main():
    elementos = [1,1,1,1,1,1,1,1,1,1,1,3]
    r = contarElemento(elementos)
    print(r)
    

main()