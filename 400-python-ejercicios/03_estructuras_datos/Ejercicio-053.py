# Diccionario Anidado: CRUD básico de tienda

def crear_producto(tienda: dict, nombre: str, precio: float, descripcion: str):
    tienda[nombre] = {'precio': precio, 'descrip': descripcion}

def leer_producto(tienda: dict, nombre: str):
    if nombre in tienda:
        return tienda[nombre]
    return None

def actualizar_producto(tienda: dict, nombre: str, precio: float = None, descripcion: str = None):
    if nombre in tienda:
        if precio is not None:
            tienda[nombre]['precio'] = precio
        if descripcion is not None:
            tienda[nombre]['descrip'] = descripcion
        return True
    return False

def eliminar_producto(tienda: dict, nombre: str):
    if nombre in tienda:
        del tienda[nombre]
        return True
    return False

def main():
     tienda = {
        "atun": {'precio': 4.25, 'descrip': 'atún caro'},
        "sardina": {'precio': 2.32, 'descrip': 'sardina cara'},
        "leche": {'precio': 1.00, 'descrip': 'leche de vaca'}
    }
     while True:
        print("\n1. Crear producto")
        print("2. Leer producto")
        print("3. Actualizar producto")
        print("4. Eliminar producto")
        print("5. Ver todos")
        print("0. Salir")
        
        op = input("Opción: ")
        
        match op:
            case "1":
                nombre = input("Nombre: ")
                precio = float(input("Precio: "))
                desc = input("Descripción: ")
                crear_producto(tienda, nombre, precio, desc)
                print("Creado!")
            
            case "2":
                nombre = input("Nombre: ")
                datos = leer_producto(tienda, nombre)
                print(datos if datos else "No encontrado")
            
            case "3":
                nombre = input("Nombre: ")
                precio = input("Nuevo precio (Enter=sin cambiar): ")
                desc = input("Nueva descripción (Enter=sin cambiar): ")
                actualizar_producto(
                    tienda, nombre,
                    float(precio) if precio else None,
                    desc if desc else None
                )
                print("Actualizado!")
            
            case "4":
                nombre = input("Nombre: ")
                if eliminar_producto(tienda, nombre):
                    print("Eliminado!")
                else:
                    print("No encontrado")
            
            case "5":
                for nombre, datos in tienda.items():
                    print(f"{nombre}: {datos}")
            
            case "0":
                print("Adiós!")
                break

main()