# Crea un función EscribirCentrado, 
# que reciba como parámetro un texto y lo escriba centrado en pantalla 
# (suponiendo una anchura de 80 columnas; 
# pista: deberás escribir 40 - longitud/2 espacios antes del texto).
# Además subraya el mensaje utilizando el carácter =.

def EscribirCentrado(txt:str):
    a = 40 - len(txt)//2
    print(" " * a + txt)
    print(" "*a + "=" * len(txt))

EscribirCentrado("Que tal, como te va?")