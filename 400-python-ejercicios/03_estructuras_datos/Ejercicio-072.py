# Registro de Pedidos:
# Crea un sistema de registro de pedidos para un restaurante.
# Utiliza un diccionario que almacene detalles de pedidos
# donde cada pedido tiene un número de pedido único,
# una lista de elementos del pedido (almacenados como tuplas de nombre del plato y cantidad),
# y un estado (pendiente, entregado, etc.).

import uuid

def agregar_pedido(pedidos:dict, elementos:list, estado:str="pendiente") -> dict:
    pedidos[uuid.uuid4()] = {
        "elementos": elementos,
        "estado": estado
    }
    return pedidos

def ver_pedido(pedidos:dict, num_pedido:str):
    return pedidos.get(num_pedido, "Pedido no encontrado")

def actualizar_estado(pedidos:dict, num_pedido:str, nuevo_estado:str):
    if num_pedido in pedidos:
        pedidos[num_pedido]["estado"] = nuevo_estado
        return True
    return False

def eliminar_pedido(pedidos:dict, num_pedido:str):
    if num_pedido in pedidos:
        del pedidos[num_pedido]
        return True
    return False

def main():
    pedidos = {
        uuid.uuid4(): {
            "elementos": [("Pizza", 2), ("Pasta", 1)],
            "estado": "entregado"
        }
    }
    
    while True:
        print("\n1. Agregar pedido")
        print("2. Ver pedido")
        print("3. Actualizar estado")
        print("4. Eliminar pedido")
        print("5. Ver todos")
        print("0. Salir")
        
        op = input("Opción: ")
        
        match op:
            case "1":
                elementos = []
                while True:
                    plato = input("Plato (0 para terminar): ")
                    if plato == "0":
                        break
                    cantidad = int(input("Cantidad: "))
                    elementos.append((plato, cantidad))
                agregar_pedido(pedidos, elementos)
                print("Pedido agregado!")
            
            case "2":
                num = input("Número de pedido: ")
                print(ver_pedido(pedidos, num))
            
            case "3":
                num = input("Número de pedido: ")
                estado = input("Nuevo estado (pendiente/entregado): ")
                if actualizar_estado(pedidos, num, estado):
                    print("Actualizado!")
                else:
                    print("No encontrado")
            
            case "4":
                num = input("Número de pedido: ")
                if eliminar_pedido(pedidos, num):
                    print("Eliminado!")
                else:
                    print("No encontrado")
            
            case "5":
                for num, datos in pedidos.items():
                    print(f"{num}: {datos['elementos']} - {datos['estado']}")
            
            case "0":
                print("¡Adiós!")
                break

main()
