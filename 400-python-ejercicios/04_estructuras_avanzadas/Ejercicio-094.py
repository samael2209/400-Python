
# Implementa una función que reciba una lista de empleados (diccionarios) 
# y calcule el salario promedio.


empleados = [
    {
        "nombre": "Jordy",
        "cargo": "Backend Developer",
        "salario": 1200
    },

    {
        "nombre": "Ana",
        "cargo": "Diseñadora UX/UI",
        "salario": 950
    },

    {
        "nombre": "Carlos",
        "cargo": "Administrador",
        "salario": 1500
    },

    {
        "nombre": "Maria",
        "cargo": "Data Analyst",
        "salario": 1300
    }
]

def salario_promedio(empleados:dict)->int:
    suma_salarios = 0
    
    for empleado in empleados:
        suma_salarios += empleado['salario']
        
    promedio = suma_salarios / len(empleados)
    
    return promedio
    

salario_promedio(empleados)