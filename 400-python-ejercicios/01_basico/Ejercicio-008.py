# Hacer un programa que cuente del 1 al 100 inclusive 
# e imprima los números que son  divisibles por 2 y por 5.

for i in range(1, 101):
    if i % 5 == 0 and i % 2 == 0:
        print(f"{i} son divisibles para 2 y 5")
    elif i % 2 == 0:
        print(f"{i} es un numero par")
    elif i % 5 == 0:
        print(f"{i} son numeros divisibles para 5")
    else:
        print(i)
