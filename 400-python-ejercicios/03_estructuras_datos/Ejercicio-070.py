# Registro de Compras: 
# Desarrolla un programa para registrar compras en una tienda en línea.
# Utiliza un diccionario para rastrear las compras de los clientes donde cada cliente tiene 
# un identificador único y una lista de productos comprados (almacenados como tuplas de 
# nombre del producto y cantidad). 
import uuid 

def registro_compras(diccionario:dict, lista_productors:list )->dict:
    
    diccionario[uuid.uuid4()] = lista_productors
    
    return diccionario

def main():
    compras = {
        uuid.uuid4() : [
            ("Nombre producto","cantidad"),
            ("Nombre producto","cantidad"),
            ("Nombre producto","cantidad"),
            ("Nombre producto","cantidad"),
                        ]
        }
    
    lsita_productos = []
    contador = 1
    
    while True:
        opcion = input(f"Debes de ingresar los datos del compra  (1 si - 0 no): ")
        if opcion == "0":
            break
        nombreProducto = input("Ingresa nombre : ")
        cantidad = input(f"Ingresa la cantidad  -- {nombreProducto} -- : ")
        print(f"Numero de prodcutos ingresados  --{contador}--")
        lsita_productos.append((nombreProducto,cantidad),)
            
        contador += 1
        
    
    a = registro_compras(compras, lsita_productos)
    
    print(a)

main()