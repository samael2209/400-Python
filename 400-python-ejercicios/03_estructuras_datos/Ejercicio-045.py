# Filtrar por Valor: 
# Escribe una función que filtre un diccionario de estudiantes para obtener 
# solo aquellos que hayan aproba

def main():
    estudiantes = {
        "Jordy":"aprobado",
        "Juan" : "reprovado",
        "Anais": "aprobado"
    }
    
    r = aprovados(estudiantes)
    print(r)

def aprovados(estudiantes:dict):
    return {nombre : estado for nombre, estado in estudiantes.items() if estado == "aprobado"}
main()