# Definir una función es_palindromo() 
# que reconoce palíndromos 
# (es decir, palabras que tienen 
# el mismo aspecto escritas invertidas), 
# ejemplo: es_palindromo ("radar") tendría que devolver True.


def es_palindromo(txt: str) -> bool:
    return txt == txt[::-1]

def main():
    texto = input("Ingresa una cadena: ")
    if es_palindromo(texto):
        print(f"'{texto}' es un palíndromo")
    else:
        print(f"'{texto}' no es un palíndromo")

main()