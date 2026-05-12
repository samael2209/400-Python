# Escribe un programa que gestione un diccionario de productos en stock, donde 
# las claves son los productos y los valores son conjuntos de ubicaciones donde se 
# almacenan.

# =========================================
# PRODUCTOS Y UBICACIONES EN STOCK
# =========================================

stock_productos = {
    "Laptop": {
        "Bodega A",
        "Bodega C"
    },

    "Mouse": {
        "Bodega B",
        "Bodega C"
    },

    "Teclado": {
        "Bodega A"
    }
}


# =========================================
# CREATE
# =========================================

def agregar_producto(diccionario: dict, producto: str):

    if producto in diccionario:
        print("El producto ya existe")

    else:
        diccionario[producto] = set()
        print("Producto agregado")


def agregar_ubicacion(diccionario: dict, producto: str, ubicacion: str):

    if producto in diccionario:

        diccionario[producto].add(ubicacion)
        print("Ubicación agregada")

    else:
        print("El producto no existe")


# =========================================
# READ
# =========================================

def mostrar_productos(diccionario: dict):

    print("\n===== PRODUCTOS EN STOCK =====")

    for producto, ubicaciones in diccionario.items():

        print(f"\nProducto: {producto}")

        for ubicacion in ubicaciones:
            print("-", ubicacion)


def mostrar_producto(diccionario: dict, producto: str):

    if producto in diccionario:

        print(f"\nUbicaciones de {producto}:")

        for ubicacion in diccionario[producto]:
            print("-", ubicacion)

    else:
        print("Producto no encontrado")


# =========================================
# UPDATE
# =========================================

def actualizar_producto(diccionario: dict, producto_viejo: str, producto_nuevo: str):

    if producto_viejo in diccionario:

        diccionario[producto_nuevo] = diccionario[producto_viejo]

        del diccionario[producto_viejo]

        print("Producto actualizado")

    else:
        print("Producto no encontrado")


def actualizar_ubicacion(
    diccionario: dict,
    producto: str,
    ubicacion_vieja: str,
    ubicacion_nueva: str
):

    if producto in diccionario:

        if ubicacion_vieja in diccionario[producto]:

            diccionario[producto].remove(ubicacion_vieja)
            diccionario[producto].add(ubicacion_nueva)

            print("Ubicación actualizada")

        else:
            print("La ubicación no existe")

    else:
        print("Producto no encontrado")


# =========================================
# DELETE
# =========================================

def eliminar_producto(diccionario: dict, producto: str):

    if producto in diccionario:

        del diccionario[producto]
        print("Producto eliminado")

    else:
        print("Producto no encontrado")


def eliminar_ubicacion(diccionario: dict, producto: str, ubicacion: str):

    if producto in diccionario:

        if ubicacion in diccionario[producto]:

            diccionario[producto].remove(ubicacion)
            print("Ubicación eliminada")

        else:
            print("Ubicación no encontrada")

    else:
        print("Producto no encontrado")


# =========================================
# PRUEBAS
# =========================================

mostrar_productos(stock_productos)

agregar_producto(
    stock_productos,
    "Monitor"
)

agregar_ubicacion(
    stock_productos,
    "Monitor",
    "Bodega D"
)

actualizar_producto(
    stock_productos,
    "Mouse",
    "Mouse Gamer"
)

actualizar_ubicacion(
    stock_productos,
    "Laptop",
    "Bodega A",
    "Bodega Principal"
)

eliminar_ubicacion(
    stock_productos,
    "Teclado",
    "Bodega A"
)

eliminar_producto(
    stock_productos,
    "Monitor"
)

print("\n===== RESULTADO FINAL =====")

mostrar_productos(stock_productos)