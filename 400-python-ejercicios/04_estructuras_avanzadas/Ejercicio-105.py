# Crea un programa que administre una lista de invitados a un evento, utilizando 
# un diccionario para rastrear la asistencia (utilizando un conjunto).


# =========================================
# LISTA DE INVITADOS Y ASISTENCIA
# =========================================

evento = {
    "invitados": {
        "Jordy",
        "Ana",
        "Carlos",
        "María",
        "Luis"
    },

    "asistieron": set()
}


# =========================================
# CREATE
# =========================================

def agregar_invitado(evento: dict, nombre: str):

    if nombre in evento["invitados"]:
        print("El invitado ya existe")

    else:
        evento["invitados"].add(nombre)
        print("Invitado agregado")


def registrar_asistencia(evento: dict, nombre: str):

    if nombre in evento["invitados"]:

        evento["asistieron"].add(nombre)
        print("Asistencia registrada")

    else:
        print("El invitado no existe")


# =========================================
# READ
# =========================================

def mostrar_invitados(evento: dict):

    print("\n===== LISTA DE INVITADOS =====")

    for invitado in evento["invitados"]:
        print("-", invitado)


def mostrar_asistentes(evento: dict):

    print("\n===== ASISTENTES =====")

    if not evento["asistieron"]:
        print("Aún no hay asistentes")

    else:
        for asistente in evento["asistieron"]:
            print("-", asistente)


def mostrar_faltantes(evento: dict):

    faltantes = evento["invitados"] - evento["asistieron"]

    print("\n===== INVITADOS QUE NO ASISTIERON =====")

    if not faltantes:
        print("Todos asistieron")

    else:
        for persona in faltantes:
            print("-", persona)


# =========================================
# UPDATE
# =========================================

def actualizar_nombre(evento: dict, nombre_viejo: str, nombre_nuevo: str):

    if nombre_viejo in evento["invitados"]:

        evento["invitados"].remove(nombre_viejo)
        evento["invitados"].add(nombre_nuevo)

        if nombre_viejo in evento["asistieron"]:

            evento["asistieron"].remove(nombre_viejo)
            evento["asistieron"].add(nombre_nuevo)

        print("Nombre actualizado")

    else:
        print("El invitado no existe")


# =========================================
# DELETE
# =========================================

def eliminar_invitado(evento: dict, nombre: str):

    if nombre in evento["invitados"]:

        evento["invitados"].remove(nombre)

        if nombre in evento["asistieron"]:
            evento["asistieron"].remove(nombre)

        print("Invitado eliminado")

    else:
        print("El invitado no existe")


# =========================================
# PRUEBAS
# =========================================

mostrar_invitados(evento)

registrar_asistencia(evento, "Jordy")
registrar_asistencia(evento, "Ana")

mostrar_asistentes(evento)

mostrar_faltantes(evento)

actualizar_nombre(
    evento,
    "Carlos",
    "Carlitos"
)

agregar_invitado(
    evento,
    "Pedro"
)

eliminar_invitado(
    evento,
    "Luis"
)

print("\n===== RESULTADO FINAL =====")

mostrar_invitados(evento)
mostrar_asistentes(evento)
mostrar_faltantes(evento)