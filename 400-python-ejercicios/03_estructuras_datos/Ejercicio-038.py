# Escribir un programa que permita procesar datos de pasajeros
# de viaje en una lista de tuplas con la siguiente forma: 
# (nombre, dni, destino). 
# Ejemplo: 
# [("Manuel Juarez", 19823451, "Liverpool"), 
# ("Silvana Paredes", 22709128, "Buenos Aires"), 
# ("Rosa Ortiz", 15123978, "Glasgow"), 
# ("Luciana Hernandez", 38981374, "Lisboa")] 
# Además, en otra lista de tuplas se almacenan los datos de cada ciudad 
# y el país al que pertenecen. 
# Ejemplo: 
# [("Buenos Aires","Argentina"), 
# ("Glasgow","Escocia"), 
# ("Lisboa", "Portugal"), 
# ("Liverpool","Inglaterra"), 
# ("Madrid","España")] 
# Hacer un menú iterativo que permita al usuario realizar las siguientes 
# operaciones: 
# -Agregar pasajeros a la lista de viajeros. 
# -Agregar ciudades a la lista de ciudades. 
# -Dado el DNI de un pasajero, ver a qué ciudad viaja. 
# -Dada una ciudad, mostrar la cantidad de pasajeros que viajan a esa ciudad. 
# -Dado el DNI de un pasajero, ver a qué país viaja. 
# -Dado un país, mostrar cuántos pasajeros viajan a ese país. 
# -Salir del programa. 

# (nombre, dni, destino).
pasajeros = [("Manuel Juarez", 19823451, "Liverpool"), 
             ("Rosa Ortiz", 15123978, "Glasgow"), 
             ("Luciana Hernandez", 38981374, "Lisboa")] 

# (ciudad, pais)
paises = [("Buenos Aires","Argentina"), 
        ("Glasgow","Escocia"), 
        ("Lisboa", "Portugal"), 
        ("Liverpool","Inglaterra"), 
        ("Madrid","España")] 

# -Agregar pasajeros a la lista de viajeros. 
def agregar_pasajeros(nombre:str, dni:int, destino:str)->list:
        return pasajeros.append((nombre, dni, destino))

# -Agregar ciudades a la lista de ciudades. 
def agregar_ciudades(ciudad:str, pais:str) -> list:
        return pais.append((ciudad, pais))

# Dado el DNI de un pasajero, ver a qué ciudad viaja. 
def buscarByDni(dni:int)->str:
        for i in pasajeros:
                if dni == i[1]:
                        return i
        return f'No se encuentra'

# Dada una ciudad, mostrar la cantidad de pasajeros que viajan a esa ciudad.
def buscarByCiudad(ciudad:str)->str:
    conteo = sum(1 for p in pasajeros if p[2]==ciudad)
    print(f"Pasajeros que viajan a {ciudad}: {conteo}")
   
# Dado el DNI de un pasajero, ver a qué país viaja
def buscarPaisByDni(dni:int) -> str:
    for pasajero in pasajeros:
        if pasajero[1] == dni:
            destino = pasajero[2]
            for ciudad, pais in paises:
                if ciudad == destino:
                    return pais
    return "No encontrado"
                        
# -Dado un país, mostrar cuántos pasajeros viajan a ese país. 
def buscarByPais(pais:str):
    conteo = 0
    for c, p in paises:
        if p == pais:
            for pasajero in pasajeros:
                if pasajero[2] == c:
                    conteo += 1
    print(f"Pasajeros que viajan a {pais}: {conteo}")
            
def main():
    while True:
        print("1. Agregar pasajeros a la lista de viajeros") 
        print("2. Agregar ciudades a la lista de ciudades")
        print("3. Dado el DNI de un pasajero, ver a qué ciudad viaja. ")
        print("4. Dada una ciudad, mostrar la cantidad de pasajeros que viajan a esa ciudad. ")
        print("5. Dado el DNI de un pasajero, ver a qué país viaja. ")
        print("6. Dado un país, mostrar cuántos pasajeros viajan a ese país. ")
        print("0. Salir del programa. ")
        opcion = input("Ingresa una de las opciones: ")
        
        match opcion:
            case "1":
                print("Agregar pasajeros: ")
                nombre = input("Nombre: ")
                dni = int(input("Dni: "))
                destino = input("Destino: ")
                agregar_pasajeros(nombre, dni, destino)
                print("Pasajero agregado! ")
            case "2":
                ciudad = input("Ciudad: ")
                pais = input("Pais: ")
                agregar_ciudades(ciudad, pais)
                print("Ciudad agregada correctamente! ")
            case "3":
                dni = int(input("Ingresa el dni a buscar: "))
                print(buscarByDni(dni))
            case "4":
                ciudad = input("Ingresa la ciudad para saber cuantas personas viajan: ")
                buscarByCiudad(ciudad)
            case "5":
                dni = int(input("Ingresa un dni para buscar: "))
                print(buscarPaisByDni(dni))
            case "6":
                pais = input("Ingresa un pais: ")
                buscarByPais(pais)
            case "0":
                print("Adiós!")
                break
                
		
main()