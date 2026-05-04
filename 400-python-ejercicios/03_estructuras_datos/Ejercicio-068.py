# Almacenamiento de Recetas: 
# Diseña un programa que gestione recetas de cocina. 
# Utiliza un diccionario para almacenar recetas donde cada receta tiene un nombre, 
# una lista de ingredientes (almacenados como tuplas de nombre y cantidad), 
# y un conjunto de instrucciones. 

def agregar_receta(recetas:dict, nombre:str, ingredientes:list )->dict:
    
    if nombre in recetas:
        print("receta ya existente! ")
    
    recetas[nombre] = {

        "Ingredientes": ingredientes
        
    }
    
    return recetas

def main():
    recetas = {
        "Nombre receta" : {
            "Ingredientes" : [
                ("Ingrediente 1","Cantidad"),
                ("Ingrediente 2","Cantidad"),
                ("Ingrediente 3","Cantidad"),
                ]
            }
        }
    
    nombre = input("Ingresa nombre de la receta: ")
    lista_ingredientes = []
    contador = 1
    
    while True:
        opcion = input(f"Debes de ingresar nombre de los ingredientes de la receta {nombre} (1 si - 0 no): ")
        if opcion == "0":
            break
        ingrediente = input("Ingresa el imgrediente : ")
        cantidad = input(f"Ingresa la cantidad  -- {ingrediente} -- : ")
        print(f"Numero de actores ingresados  --{contador}--")
        lista_ingredientes.append((ingrediente,cantidad),)
            
        contador += 1
        
    
    a = agregar_receta(recetas,nombre, lista_ingredientes)
    
    print(a)

main()