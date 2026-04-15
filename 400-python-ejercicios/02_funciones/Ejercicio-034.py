# Definir una función superposicion() 
# que tome dos listas y devuelva True 
# si tienen al menos 1 miembro en común 
# o devuelva False de lo contrario. 
# Escribir la función usando el bucle for anidado.

def superposicion(l1: list, l2: list) -> bool:
    return bool(set(l1) & set(l2))

# def superposicion(l1:list, l2:list) -> bool:
#     for i in l1:
#         for j in l2:
#             if i == j:
#                 return True
    
#     return False

def main():
    lista1 = [1, 2, 3]
    lista2 = [4, 6, 5]
    print(superposicion(lista1, lista2))
    lista3 = [1, 2, 3]
    lista4 = [3, 4, 5]
    print(superposicion(lista3, lista4))
main()