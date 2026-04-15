# Definir una función inversa() 
# que calcule la inversión de una cadena. 
# Por ejemplo la cadena "estoy probando" 
# debería devolver la cadena "odnaborp yotse"

def inversa(txt:str) -> str:
    cadena_vacia = ""
    for i in txt:
        cadena_vacia = i + cadena_vacia
        
    return cadena_vacia

def main():
    texto = input("Ingresa una cadena: ")
    print(f"Invertida: {inversa(texto)}")
main()