# Club de socios
# Datos: número, nombre y apellido, fecha de ingreso (dd/mm/aaaa), cuota al día (s/n)

def cantidad_socios(socios: dict) -> int:
    return len(socios)

def registrar_pago(socios: dict, num_socio: int):
    if num_socio in socios:
        socios[num_socio][2] = "s"
        print(f"Socio #{num_socio} pagadó")
    else:
        print("Socio no encontrado")

def modificar_fecha(socios: dict):
    for num in socios:
        if socios[num][1] == "13/03/2018":
            socios[num][1] = "14/03/2018"
    print("Fechas actualizadas")

def eliminar_socio(socios: dict, nombre: str):
    for num, datos in list(socios.items()):
        if datos[0] == nombre:
            del socios[num]
            print(f"'{nombre}' eliminado")
            return
    print("Socio no encontrado")

def imprimir_listado(socios: dict):
    for num, datos in socios.items():
        print(f"#{num}: {datos[0]} | Fecha: {datos[1]} | Cuota: {datos[2]}")

def main():
    socios = {
        1: ["Amanda Núñez", "17/03/2009", "s"],
        2: ["Bárbara Molina", "17/03/2009", "s"],
        3: ["Lautaro Campos", "17/03/2009", "s"]
    }
    
    while True:
        print("\n1. Cantidad de socios")
        print("2. Registrar pago de cuota")
        print("3. Modificar fecha 13/03/2018 -> 14/03/2018")
        print("4. Eliminar socio por nombre")
        print("5. Listado completo")
        print("0. Salir")
        
        op = input("Opción: ")
        
        if op == "1":
            print(f"Total: {cantidad_socios(socios)}")
        
        elif op == "2":
            num = int(input("Número de socio: "))
            registrar_pago(socios, num)
        
        elif op == "3":
            modificar_fecha(socios)
        
        elif op == "4":
            nombre = input("Nombre y apellido: ")
            eliminar_socio(socios, nombre)
        
        elif op == "5":
            imprimir_listado(socios)
        
        elif op == "0":
            print("Adiós!")
            break

main()