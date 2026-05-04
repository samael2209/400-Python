# Diccionario de Estudiantes: 
# Crea un diccionario que almacene información sobre estudiantes, 
# donde cada estudiante tiene un nombre, 
# una lista de cursos en los que está inscrito y 
# una tupla con sus calificaciones para cada curso

estudiantes = {
    
}

#CRUD 
def crear_estudiante(estudiantes:dict,nombre:str, cursos:list, calificaciones:tuple) -> dict:
    if nombre in estudiantes:
        print("El estudiante ya existe en la base de datos! ")
        return
    
    if len(cursos) != len(calificaciones):
        print("Cursos y calificaciones no coinciden")
        return
    
    estudiantes[nombre] = {
        "cursos" : cursos,
        "calificaciones": calificaciones
    }
    
def leer_estudiante(estudiante:dict, nombre:str) -> dict:
    nombre = nombre.title()
    if nombre not in estudiante:
        print(f"Estudiante: {nombre} no encontrado!")
        return
    
    return estudiante[nombre]

def actualizar_estudiante(estudiante:dict, nombre:str, cursos=None, calificaciones=None):
    if nombre not in estudiante:
        print(f"Estudiante: {nombre} no encontrado!")
        return
    if cursos:
        estudiante[nombre]["cursos"] = cursos
    if len(calificaciones) != len(estudiante[nombre]["calificaciones"]):
        print("calificaciones no coinciden")
        return

    estudiante[nombre]["calificaciones"] = calificaciones

def eliminar_estudiante(estudiante:dict, nombre:str):
    if nombre  in estudiante:
        del estudiante[nombre]
    else:
        print(f"Estudiante: {nombre} no encontrado!")

crear_estudiante(estudiantes, "Jordy", ["ingles", "mate"], (7, 8))
crear_estudiante(estudiantes, "Maria", ["fisica"], (9,))

print(leer_estudiante(estudiantes, "Jordy"))

actualizar_estudiante(estudiantes, "Jordy", calificaciones=(10, 10))

eliminar_estudiante(estudiantes, "Maria")

print(estudiantes)