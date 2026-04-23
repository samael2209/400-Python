# Diccionario de Contactos: 
# Crea un diccionario de contactos con nombres y números de teléfono

def crear(dic:dict, clave, valor):
    dic[clave] = valor

def buscar(d1:dict, clave):
    return d1.get(clave, "No encontrado")

def actualizar(d1, clave, valor):
    if clave in d1:
        d1[clave] = valor
        return True
    return False

def eliminar(d1:dict, clave):
    if clave in d1:
        del d1[clave]
        return True
    return False

def main():
    contactos = {}
    
    while True:
        print("\n1. Crear contacto")
        print("2. Buscar contacto")
        print("3. Actualizar teléfono")
        print("4. Eliminar contacto")
        print("5. Ver todos")
        print("0. Salir")
        
        op = input("Opción: ")
        
        match op:
            case "1":
                nombre = input("Nombre: ")
                telefono = input("Teléfono: ")
                crear(contactos, nombre, telefono)
                print("Creado!")
            
            case "2":
                nombre = input("Nombre: ")
                print(buscar(contactos, nombre))
            
            case "3":
                nombre = input("Nombre: ")
                telefono = input("Nuevo teléfono: ")
                if actualizar(contactos, nombre, telefono):
                    print("Actualizado!")
                else:
                    print("No encontrado")
            
            case "4":
                nombre = input("Nombre: ")
                if eliminar(contactos, nombre):
                    print("Eliminado!")
                else:
                    print("No encontrado")
            
            case "5":
                for nombre, telefono in contactos.items():
                    print(f"{nombre}: {telefono}")
            
            case "0":
                print("Adiós!")
                break
main()