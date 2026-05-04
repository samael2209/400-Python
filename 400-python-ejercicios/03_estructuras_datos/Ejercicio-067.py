# Registro de Películas: 
# Crea un diccionario que contenga información sobre películas,
# donde cada película tiene un título, 
# un año de lanzamiento y una lista de actores principales 
# representados como tuplas (nombre del actor, papel en la película).



def agregar_pelicula(peliculas:dict, nombre:str, estreno:int, actores:list )->dict:
    
    if nombre in peliculas:
        print("Pelicula ya existente! ")
    
    peliculas[nombre] = {
        "Esteno" : estreno,
        "Actores": actores
        
    }
    
    return peliculas


def main():
    peliculas = {
        "Michi" : {
            "Estreno" : 2000,
            "Actores" : [
                ("Gato","Actor principal"),
                ("Gato2", "Actor secundario")]
            }
        }
    
    nombre = input("Ingresa nombre de la pelicula: ")
    estreno = int(input("Ingresa el anio del estreno: "))
    lista_actores = []
    contador = 1
    
    while True:
        opcion = input(f"Debes de ingresar nombre de los actores de la pelicula {nombre} (1 si - 0 no): ")
        if opcion == "0":
            break
        actor = input("Ingresa el nombre del actor: ")
        papel = input(f"Ingresa el papel del actor -- {actor} -- : ")
        print(f"Numero de actores ingresados  --{contador}--")
        lista_actores.append((actor,papel),)
            
        contador += 1
        
    
    a = agregar_pelicula(peliculas,nombre, estreno, lista_actores)
    
    print(a)

main()