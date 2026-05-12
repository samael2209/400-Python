# Diseña un programa que organice una lista de estudiantes (diccionarios)
# en función de sus calificaciones (almacenadas como una tupla).

estudiantes = [
    {
        "nombre": "Jordy",

        "calificaciones": (
            9.5,
            8.7,
            10.0
        )
    },

    {
        "nombre": "Ana",

        "calificaciones": (
            7.8,
            8.2,
            9.0
        )
    },

    {
        "nombre": "Carlos",

        "calificaciones": (
            6.5,
            7.0,
            7.8
        )
    },

    {
        "nombre": "Maria",

        "calificaciones": (
            9.8,
            9.5,
            9.7
        )
    },

    {
        "nombre": "Luis",

        "calificaciones": (
            8.0,
            7.9,
            8.4
        )
    }
]

promedios = []

for estudiante in estudiantes:
    suma = 0
    
    for calificaciones in estudiante["calificaciones"]:
        suma = suma + calificaciones
    promedio = suma / len(estudiante['calificaciones'])
    promedios.append(promedio)
n = len(estudiantes)
for i in range(n):
    for j in range(n - 1 - i):
        if promedios[j] < promedios[j + 1]:
            estudiantes[j], estudiantes[j + 1] = estudiantes[j + 1] ,estudiantes[j]
            promedios[j], promedios[j + 1] = promedios[j + 1], promedios[j]

print("Estudiantes ordenados por promedio (mayor a menor):\n")
for i in range(len(estudiantes)):
    print(f"{i + 1}. {estudiantes[i]['nombre']}: {promedios[i]:.2f}")