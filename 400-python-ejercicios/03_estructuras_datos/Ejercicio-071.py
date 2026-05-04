# Registro de Viajes:
# Diseña una aplicación para registrar viajes.
# Utiliza un diccionario que almacene información sobre viajes,
# donde cada viaje tiene un destino, una lista de lugares
# visitados (almacenados como tuplas de nombre y fecha) y una descripción.

def agregar_viaje(viajes:dict, destino:str, lugares:list, descripcion:str) -> dict:
    if destino in viajes:
        print("El viaje ya existe!")
        return viajes
    
    viajes[destino] = {
        "lugares": lugares,
        "descripcion": descripcion
    }
    return viajes

def ver_viaje(viajes:dict, destino:str):
    if destino in viajes:
        return viajes[destino]
    return "Viaje no encontrado"

def actualizar_viaje(viajes:dict, destino:str, lugares=None, descripcion=None):
    if destino not in viajes:
        print("Viaje no encontrado!")
        return
    
    if lugares:
        viajes[destino]["lugares"] = lugares
    if descripcion:
        viajes[destino]["descripcion"] = descripcion

def eliminar_viaje(viajes:dict, destino:str):
    if destino in viajes:
        del viajes[destino]
        print(f"Viaje a {destino} eliminado!")
    else:
        print("Viaje no encontrado")

def main():
    viajes = {
        "Paris": {
            "lugares": [("Torre Eiffel", "2024-01-15"), ("Louvre", "2024-01-16")],
            "descripcion": "Viaje romántico"
        }
    }
    
    while True:
        print("\n1. Agregar viaje")
        print("2. Ver viaje")
        print("3. Actualizar viaje")
        print("4. Eliminar viaje")
        print("5. Ver todos")
        print("0. Salir")
        
        op = input("Opción: ")
        
        match op:
            case "1":
                destino = input("Destino: ")
                lugares = []
                while True:
                    lugar = input("Lugar (0 para terminar): ")
                    if lugar == "0":
                        break
                    fecha = input("Fecha (YYYY-MM-DD): ")
                    lugares.append((lugar, fecha))
                desc = input("Descripción: ")
                agregar_viaje(viajes, destino, lugares, desc)
                print("Viaje agregado!")
            
            case "2":
                destino = input("Destino: ")
                print(ver_viaje(viajes, destino))
            
            case "3":
                destino = input("Destino: ")
                lugares = input("Nuevos lugares (dejar vacío para no cambiar): ")
                desc = input("Nueva descripción (dejar vacío para no cambiar): ")
                actualizar_viaje(
                    viajes, destino,
                    [(l, "") for l in lugares.split(",")] if lugares else None,
                    desc if desc else None
                )
                print("Actualizado!")
            
            case "4":
                destino = input("Destino: ")
                eliminar_viaje(viajes, destino)
            
            case "5":
                for dest, datos in viajes.items():
                    print(f"{dest}: {datos['descripcion']}")
            
            case "0":
                print("¡Adiós!")
                break

main()
