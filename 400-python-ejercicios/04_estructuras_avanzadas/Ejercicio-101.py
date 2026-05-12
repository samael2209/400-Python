# Desarrolla un programa que administre un diccionario de ciudades y sus 
# temperaturas máximas diarias (almacenadas como una lista de tuplas con fechas y 
# temperaturas). 


temperaturas_ciudades = {
    "Quito": [
        ("2026-05-10", 22),
        ("2026-05-11", 24),
    ],

    "Guayaquil": [
        ("2026-05-10", 31),
        ("2026-05-11", 32),
    ]
}


# CREATE
def agregar_ciudad(diccionario: dict, ciudad: str):
    if ciudad in diccionario:
        print("La ciudad ya existe")
    else:
        diccionario[ciudad] = []
        print(f"{ciudad} agregada correctamente")


def agregar_temperatura(diccionario: dict, ciudad: str, fecha: str, temperatura: int):
    if ciudad in diccionario:
        diccionario[ciudad].append((fecha, temperatura))
        print("Temperatura agregada")
    else:
        print("La ciudad no existe")


# READ
def mostrar_ciudades(diccionario: dict):
    for ciudad, datos in diccionario.items():
        print(f"\nCiudad: {ciudad}")

        for fecha, temperatura in datos:
            print(f"Fecha: {fecha} | Temperatura: {temperatura}°C")


def mostrar_ciudad(diccionario: dict, ciudad: str):
    if ciudad in diccionario:
        print(f"\nCiudad: {ciudad}")

        for fecha, temperatura in diccionario[ciudad]:
            print(f"Fecha: {fecha} | Temperatura: {temperatura}°C")
    else:
        print("Ciudad no encontrada")


# UPDATE
def actualizar_temperatura(diccionario: dict, ciudad: str, fecha: str, nueva_temp: int):
    if ciudad in diccionario:

        lista = diccionario[ciudad]

        for i, (f, temp) in enumerate(lista):

            if f == fecha:
                lista[i] = (fecha, nueva_temp)
                print("Temperatura actualizada")
                return

        print("Fecha no encontrada")

    else:
        print("Ciudad no encontrada")


# DELETE
def eliminar_ciudad(diccionario: dict, ciudad: str):
    if ciudad in diccionario:
        del diccionario[ciudad]
        print("Ciudad eliminada")
    else:
        print("Ciudad no encontrada")


def eliminar_temperatura(diccionario: dict, ciudad: str, fecha: str):
    if ciudad in diccionario:

        lista = diccionario[ciudad]

        for dato in lista:

            if dato[0] == fecha:
                lista.remove(dato)
                print("Registro eliminado")
                return

        print("Fecha no encontrada")

    else:
        print("Ciudad no encontrada")


# =========================
# PRUEBAS
# =========================

agregar_ciudad(temperaturas_ciudades, "Cuenca")

agregar_temperatura(
    temperaturas_ciudades,
    "Cuenca",
    "2026-05-12",
    20
)

mostrar_ciudades(temperaturas_ciudades)

actualizar_temperatura(
    temperaturas_ciudades,
    "Quito",
    "2026-05-10",
    26
)

eliminar_temperatura(
    temperaturas_ciudades,
    "Guayaquil",
    "2026-05-10"
)

eliminar_ciudad(
    temperaturas_ciudades,
    "Cuenca"
)

print("\n======= RESULTADO FINAL =======")
mostrar_ciudades(temperaturas_ciudades)