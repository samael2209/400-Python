# Crea un función “ConvertirEspaciado”, que reciba como parámetro un texto 
# y devuelve una cadena con un espacio adicional tras cada letra. 
# Por ejemplo, “Hola, tú” devolverá “H o l a , t ú “. 
# Crea un programa principal donde se use dicha función.

def ConvertirEspaciado(txt:str) -> str:
    return "".join(c + " " for c in txt)

def main():
    txt = input("Ingresa una oración: ")
    resultado = ConvertirEspaciado(txt)
    print(f"Original: '{txt}'")
    print(f"Espaciado: '{resultado}'")

main()