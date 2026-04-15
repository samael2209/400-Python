# Definir una función max_de_tres(), 
# que tome tres números como argumentos 
# y devuelva el mayor de ellos.

def max_de_tres(n1:int, n2:int, n3:int) -> int:
    mayor = n1
    
    if n2 >= mayor:
        mayor = n2
    
    if n3 >= mayor:
        mayor = n3
    
    return mayor

print(max_de_tres(10,4,3))