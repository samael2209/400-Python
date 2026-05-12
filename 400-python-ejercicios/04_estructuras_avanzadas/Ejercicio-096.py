# Desarrolla una función que encuentre el empleado 
# con el salario más alto en una lista de empleados (diccionarios) y muestre su información.

empleados = [
    {
        "nombre": "Jordy",
        "cargo": "Backend",
        "salario": 1200
    },

    {
        "nombre": "Anais",
        "cargo": "Diseñadora",
        "salario": 1800
    },

    {
        "nombre": "Carlos",
        "cargo": "Administrador",
        "salario": 1500
    }
]

def sueldo_max(empleados:dict) :
    mayor = empleados[0]
    
    for empleado in empleados:
        if empleado["salario"] > mayor["salario"]:
            mayor = empleado
    
    print(mayor)

sueldo_max(empleados)