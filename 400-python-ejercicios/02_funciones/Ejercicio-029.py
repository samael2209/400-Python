# Definir una función que calcule la longitud de una lista o una cadena dada. 
# (Es cierto que Python tiene la función len() incorporada, 
# pero escribirla por nosotros mismos resulta un muy buen ejercicio).

def longitud(secuencia)->int:
    contador = 0
    for _ in secuencia:
        contador += 1
    return contador

def main():
    opcion = input("1. Cadena de texto\n2. Lista\nElige: ")
    
    if opcion == "1":
        texto = input("Ingresa una cadena: ")
        print(f"Longitud: {longitud(texto)}")
    elif opcion == "2":
        lista = input("Ingresa elementos separados por coma: ").split(",")
        print(f"Longitud: {longitud(lista)}")
main()
        
    