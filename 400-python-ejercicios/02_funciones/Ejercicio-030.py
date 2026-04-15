# Escribir una función que tome un carácter y devuelva True si es una vocal, 
# de lo contrario devuelve False.

def es_vocal(c: str) -> bool:
    return c.lower() in "aeiou"
        
def main():
    char = input("Ingresa un carácter: ")
    if es_vocal(char):
        print(f"'{char}' es una vocal")
    else:
        print(f"'{char}' no es una vocal")
main()