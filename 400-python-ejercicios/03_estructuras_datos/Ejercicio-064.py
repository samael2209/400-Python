# Puntuaciones de Jugadores:
# Diseña un juego que registre las puntuaciones de múltiples 
# jugadores. 
# Crea un diccionario que almacene el nombre de cada 
# jugador como clave y una 
# tupla de sus puntuaciones como valor. 
# Luego, permite que los jugadores agreguen nuevas 
# puntuaciones a sus registros.

puntuaciones = {"jordy" : (12,3,4)}

def agregar_puntuacion(puntuaciones:dict)->dict:
    
    nombre = input("Ingresa tu nombre: ")
    
    if nombre not in puntuaciones:
        puntuaciones[nombre] = ()
    
    while True:
        puntuacion = int(input("Ingresa tu puntuacion (0 para salir): "))
        if puntuacion == 0:
            break
        
        puntuaciones[nombre] += (puntuacion,)
    return puntuaciones



print(agregar_puntuacion(puntuaciones))