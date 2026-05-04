# Directorio Telefónico: 
# Crea un directorio telefónico que almacene contactos como un diccionario 
# donde las claves son nombres y los valores son tuplas con números de teléfono 
# y direcciones de correo electrónico.

def agregar_contacto(recetas:dict, nombre:str, datos_contacto:list )->dict:
    
    if nombre in recetas:
        print("receta ya existente! ")
    
    recetas[nombre] = datos_contacto
    
    return recetas

def main():
    contactos = {
        "Nombre contacto" : [("0987456321","correo@gmail.com.ec")]
        }
    
    nombre = input("Ingresa nombre del cotacto: ")
    datos_contacto = []
    contador = 1
    
    while True:
        opcion = input(f"Debes de ingresar los datos del contacto  {nombre} (1 si - 0 no): ")
        if opcion == "0":
            break
        telefono = input("Ingresa el numero de telefono : ")
        email = input(f"Ingresa el correo electronico  -- {nombre} -- : ")
        print(f"Numero de actores ingresados  --{contador}--")
        datos_contacto.append((telefono,email),)
            
        contador += 1
        
    
    a = agregar_contacto(contactos,nombre, datos_contacto)
    
    print(a)

main()