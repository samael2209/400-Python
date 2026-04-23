# Invertir Diccionario:
# Crea una función que invierta las claves y los valores en un diccionario.

def invertir(di1:dict)->dict:
    return {valor:clave for clave, valor in di1.items() }

def main():
    di1 = {
        "lo" : 1,
        "le" : 2,
    }
    
    d = invertir(di1)
    print(d)

main()