# Definir una función generar_n_caracteres() 
# que tome un entero n y devuelva el carácter 
# multiplicado por n. 
# Por ejemplo: generar_n_caracteres(5, "x") 
# debería devolver "xxxxx".

def generar_n_caracteres(num:int, caracter:str) -> str:
    return caracter*num

print(generar_n_caracteres(5,"x"))