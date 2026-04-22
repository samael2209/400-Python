# Solicitar al usuario que ingrese los nombres de pila de los alumnos de nivel primario 
# de una escuela, finalizando al ingresar “x”. 
# A continuación, solicitar que ingrese los nombres de los alumnos de nivel secundario, 
# finalizando al ingresar “x”.
# - Informar los nombres de todos los alumnos de nivel primario y los de nivel secundario, sin 
# repeticiones.<>
# - Informar qué nombres se repiten entre los alumnos de nivel primario y secundario.
# -Informar qué nombres de nivel primario no se repiten en los de nivel secundario.

def nombres_primaria():
    lista_primaria = []
    while True:
        nombre_primaria=input("Ingresa los nombres de los de primaria: ")
        if nombre_primaria != "x":
            lista_primaria.append(nombre_primaria)
        else:
            break
    return lista_primaria
        
def nombres_secundaria():
    lista_secundaria = []
    while True:
        nombre_secundaria=input("Ingresa los nombres de los de secundaria: ")
        if nombre_secundaria != "x":
            lista_secundaria.append(nombre_secundaria)
        else:
            break
    return lista_secundaria

def main():
    primaria = set(nombres_primaria())
    secundaria = set(nombres_secundaria())
    
    print(f"Primaria sin repeticiones: {primaria}")
    print(f"Secundaria sin repeticiones: {secundaria}")
    repetidos = primaria & secundaria    # - l1 & l2 = intersección (elementos en ambos)
    print(f"Nombres repetidos: {repetidos}")
    no_repetidos = primaria - secundaria # - l1 - l2 = diferencia (elementos en l1 pero no en l2)
    print(f"De primaria que no están en secundaria: {no_repetidos}")
      
main()