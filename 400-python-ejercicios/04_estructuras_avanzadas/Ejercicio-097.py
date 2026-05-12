# Escribe un programa que gestione un diccionario de productos,
# donde cada producto tiene un nombre y 
# una lista de revisiones de usuarios 
# (almacenadas como diccionarios con comentarios y calificaciones).

# =========================
# DICCIONARIO PRINCIPAL
# =========================

productos = {
    "producto_1": {
        "nombre": "Laptop Lenovo",

        "revisiones": [
            {
                "usuario": "Jordy",
                "comentario": "Muy buena laptop para programar",
                "calificacion": 5
            },

            {
                "usuario": "Ana",
                "comentario": "Buen rendimiento y batería",
                "calificacion": 4
            }
        ]
    },

    "producto_2": {
        "nombre": "Mouse Logitech",

        "revisiones": [
            {
                "usuario": "Carlos",
                "comentario": "Muy cómodo para gaming",
                "calificacion": 5
            },

            {
                "usuario": "Maria",
                "comentario": "Buen diseño pero algo caro",
                "calificacion": 4
            }
        ]
    },

    "producto_3": {
        "nombre": "Teclado Mecánico",

        "revisiones": [
            {
                "usuario": "Luis",
                "comentario": "Excelente sonido y calidad",
                "calificacion": 5
            },

            {
                "usuario": "Sofia",
                "comentario": "Las teclas son muy suaves",
                "calificacion": 5
            }
        ]
    }
}



# =========================
# CREAR PRODUCTO
# =========================

def agregar_producto(
    productos: dict,
    nombre: str
) -> dict:

    codigo_producto = f"producto_{len(productos) + 1}"

    productos[codigo_producto] = {
        "nombre": nombre,
        "revisiones": []
    }

    return productos


# =========================
# AGREGAR REVISION
# =========================

def agregar_revision(
    productos: dict,
    codigo_producto: str,
    usuario: str,
    comentario: str,
    calificacion: int
) -> dict:

    if codigo_producto in productos:

        revision = {
            "usuario": usuario,
            "comentario": comentario,
            "calificacion": calificacion
        }

        productos[codigo_producto]["revisiones"].append(revision)

    else:
        print("Producto no encontrado")

    return productos


# =========================
# LEER PRODUCTOS
# =========================

def mostrar_productos(productos: dict) -> None:

    for codigo, producto in productos.items():

        print(f"\nCódigo: {codigo}")
        print(f"Nombre: {producto['nombre']}")

        print("Revisiones:")

        for revision in producto["revisiones"]:

            print(f"Usuario: {revision['usuario']}")
            print(f"Comentario: {revision['comentario']}")
            print(f"Calificación: {revision['calificacion']}")
            print("-" * 20)


# =========================
# ACTUALIZAR PRODUCTO
# =========================

def actualizar_producto(
    productos: dict,
    codigo_producto: str,
    nuevo_nombre: str
) -> dict:

    if codigo_producto in productos:

        productos[codigo_producto]["nombre"] = nuevo_nombre

    else:
        print("Producto no encontrado")

    return productos


# =========================
# ELIMINAR PRODUCTO
# =========================

def eliminar_producto(
    productos: dict,
    codigo_producto: str
) -> dict:

    if codigo_producto in productos:

        del productos[codigo_producto]

    else:
        print("Producto no encontrado")

    return productos


# =========================
# USO DEL CRUD
# =========================

agregar_producto(productos, "Laptop Lenovo")
agregar_producto(productos, "Mouse Logitech")

agregar_revision(
    productos,
    "producto_1",
    "Jordy",
    "Excelente rendimiento",
    5
)

agregar_revision(
    productos,
    "producto_1",
    "Ana",
    "Muy buena batería",
    4
)

mostrar_productos(productos)

actualizar_producto(
    productos,
    "producto_2",
    "Mouse Gamer Logitech"
)

eliminar_producto(
    productos,
    "producto_1"
)

print("\nDespués de actualizar y eliminar:\n")

mostrar_productos(productos)