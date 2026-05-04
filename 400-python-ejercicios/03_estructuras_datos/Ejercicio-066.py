# Inventario de Tienda: 
# Desarrolla un programa que administre el inventario de una tienda. 
# Utiliza un diccionario para almacenar los productos como claves y sus detalles 
# (precio, cantidad en stock, etc.) como valores. 
# Permite que los usuarios agreguen nuevos productos y  actualicen la información existente. 


tienda = {
    "Cloro" : {
        "Precio" : 1.00,
        "cantidad" : 15,
    }
}

def agregar_producto(tienda:dict, nombre:str, precio:float, cantidad:int) -> dict:
    if nombre in tienda:
        print("El producto ya existe! ")
    else:
        tienda[nombre] = {
            "precio" : precio,
            "cantidad" : cantidad,
        }
        
    return tienda

def actualizar_producto(tienda:dict, nombre:str, precio:None, cantidad:None) -> dict:
    if nombre not in tienda:
        print("Producto no existente! ")
    if cantidad:
        tienda[nombre]["cantidad"] = cantidad
    
    tienda[nombre]['Precio'] = precio
    
    return tienda
    
        
print(actualizar_producto(tienda,"Cloro", 2.33, 9 ))
    