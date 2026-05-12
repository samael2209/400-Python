# Crea un programa que gestione una lista de usuarios, 
# donde cada usuario es un diccionario con nombre, 
# correo electrónico y 
# una lista de pedidos realizados 
# (almacenados como diccionarios con detalles de productos).


usuarios = [
    {
        "nombre": "Jordy",
        "correo": "jordy@gmail.com",
        "pedidos": [
            {
                "producto": "Laptop",
                "cantidad": 1,
                "precio": 900
            },
            {
                "producto": "Mouse",
                "cantidad": 2,
                "precio": 25
            }
        ]
    },

    {
        "nombre": "Ana",
        "correo": "ana@gmail.com",
        "pedidos": [
            {
                "producto": "Teclado",
                "cantidad": 1,
                "precio": 50
            }
        ]
    }
]

def agregar_usuario(usuarios, nombre, correo):
    usuario = {
        "nombre" : nombre,
        "correo" : correo,
        "pedidos" : []
    }
    
    usuarios.append(usuario)

def agregar_pedido(usuarios, correo, producto, cantidad, precio):
    for usuario in usuarios:
        if usuario['correo'] == correo:
            
            pedido = {
                "producto" : producto,
                "cantidad" : cantidad,
                "precio" : precio
            }
            
            usuario["pedidos"].append(pedido)



agregar_usuario(usuarios, "Jordy", "jordy@gmail.com")

agregar_pedido(
    usuarios,
    "jordy@gmail.com",
    "Laptop",
    1,
    900
)

print(usuarios)