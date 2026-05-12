# Diseña un programa que gestione una lista de tareas
# pendientes de múltiples usuarios, 
# utilizando un diccionario donde las claves son los usuarios 
# y los valores son conjuntos de tareas.

tareas_usuarios = {
    "Jordy": {
        "Estudiar Python",
        "Hacer ejercicio",
        "Leer documentación"
    },

    "Ana": {
        "Diseñar interfaz",
        "Terminar reporte"
    }
}


# =========================
# CREATE
# =========================

def agregar_usuario(diccionario: dict, usuario: str):

    if usuario in diccionario:
        print("El usuario ya existe")

    else:
        diccionario[usuario] = set()
        print("Usuario agregado")


def agregar_tarea(diccionario: dict, usuario: str, tarea: str):

    if usuario in diccionario:
        diccionario[usuario].add(tarea)
        print("Tarea agregada")

    else:
        print("El usuario no existe")


# =========================
# READ
# =========================

def mostrar_usuarios(diccionario: dict):

    for usuario, tareas in diccionario.items():

        print(f"\nUsuario: {usuario}")

        for tarea in tareas:
            print("-", tarea)


def mostrar_tareas_usuario(diccionario: dict, usuario: str):

    if usuario in diccionario:

        print(f"\nTareas de {usuario}:")

        for tarea in diccionario[usuario]:
            print("-", tarea)

    else:
        print("Usuario no encontrado")


# =========================
# UPDATE
# =========================

def actualizar_tarea(diccionario: dict, usuario: str, tarea_vieja: str, tarea_nueva: str):

    if usuario in diccionario:

        if tarea_vieja in diccionario[usuario]:

            diccionario[usuario].remove(tarea_vieja)
            diccionario[usuario].add(tarea_nueva)

            print("Tarea actualizada")

        else:
            print("La tarea no existe")

    else:
        print("Usuario no encontrado")


# =========================
# DELETE
# =========================

def eliminar_usuario(diccionario: dict, usuario: str):

    if usuario in diccionario:

        del diccionario[usuario]
        print("Usuario eliminado")

    else:
        print("Usuario no encontrado")


def eliminar_tarea(diccionario: dict, usuario: str, tarea: str):

    if usuario in diccionario:

        if tarea in diccionario[usuario]:

            diccionario[usuario].remove(tarea)
            print("Tarea eliminada")

        else:
            print("La tarea no existe")

    else:
        print("Usuario no encontrado")


# =========================
# PRUEBAS
# =========================

agregar_usuario(tareas_usuarios, "Carlos")

agregar_tarea(
    tareas_usuarios,
    "Carlos",
    "Aprender Go"
)

mostrar_usuarios(tareas_usuarios)

actualizar_tarea(
    tareas_usuarios,
    "Jordy",
    "Leer documentación",
    "Leer sobre APIs"
)

eliminar_tarea(
    tareas_usuarios,
    "Ana",
    "Diseñar interfaz"
)

eliminar_usuario(
    tareas_usuarios,
    "Carlos"
)

print("\n======= RESULTADO FINAL =======")
mostrar_usuarios(tareas_usuarios)