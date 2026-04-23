# Diccionario de Traducción: 
# Crea un diccionario que traduzca palabras de un idioma a otro

def main():
    traduccion = {
        "hello": "hola",
        "goodbye": "adios",
        "thanks": "gracias",
        "please": "por favor",
        "yes": "si",
        "no": "no"
    }
    
    while True:
        print("\n1. Agregar palabra")
        print("2. Traducir palabra")
        print("3. Ver diccionario")
        print("4. Eliminar palabra")
        print("0. Salir")
        
        op = input("Opción: ")
        
        match op:
            case "1":
                español = input("Español: ")
                ingles = input("Inglés: ")
                traduccion[ingles] = español
                print("Agregada!")
            
            case "2":
                palabra = input("Palabra en inglés: ").lower()
                if palabra in traduccion:
                    print(f"Traducción: {traduccion[palabra]}")
                else:
                    print("Palabra no encontrada")
            
            case "3":
                for ingles, español in traduccion.items():
                    print(f"{ingles} -> {español}")
            
            case "4":
                palabra = input("Palabra en inglés: ").lower()
                if palabra in traduccion:
                    del traduccion[palabra]
                    print("Eliminada!")
                else:
                    print("No encontrada")
            
            case "0":
                print("Adiós!")
                break
main()