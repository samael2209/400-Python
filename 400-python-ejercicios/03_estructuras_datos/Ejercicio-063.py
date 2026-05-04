# Registro de Ventas: 
# Crea un programa que registre las ventas diarias de una tienda 
# utilizando un diccionario. 
# El diccionario debe contener las fechas como claves y las ventas 
# totales como valores.
# Utiliza una lista para almacenar los detalles de cada venta, que incluyen 
# el producto vendido, la cantidad y el precio unitario. 

from datetime import datetime
fecha = datetime.strptime("2026-05-01", "%Y-%m-%d")
ventas = {fecha:[]} 

factura = [
    ["Detergente", 3, 1.25],
    ["Cloro", 4, 0.50],
    ["Harian", 5, 0.75],
    ]

def ventas_totales(factura:list, ventas:dict)->dict:
    for nombre, cantidad, precio in factura:
        ventas[fecha].append({
            "nombre" : nombre,
            "cantidad": cantidad,
            "precio": precio,
            "subtotal": cantidad*precio
        })
    return ventas

    

def imprimir_ventas(ventas: dict):
    for fecha, items in ventas.items():
        print(f"\n📅 Fecha: {fecha.strftime('%Y-%m-%d')}")
        print("-" * 40)
        
        total = 0
        
        for item in items:
            print(f"{item['nombre']:<12} | Cant: {item['cantidad']:<2} | "
                  f"${item['precio']:<5} | Subtotal: ${item['subtotal']:.2f}")
            total += item["subtotal"]
        
        print("-" * 40)
        print(f"💰 TOTAL: ${total:.2f}")

ventas_totales(factura, ventas)
imprimir_ventas(ventas)