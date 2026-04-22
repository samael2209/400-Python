# Calcular Promedio: 
# Dado un diccionario de estudiantes y sus calificaciones, calcula el 
# promedio de calificaciones.

def main():
    promedio = {
        'Juan' : 5,
        'Jordy' : 2,
        'Anais' : 7,
        'Meredith' : 8
    }
    print(f"Promedio: {calcular_promedio(promedio):.2f}")

def calcular_promedio(promedios:dict)->float:
    total = sum(promedios.values())
    return total/len(promedios)
    
        
main()