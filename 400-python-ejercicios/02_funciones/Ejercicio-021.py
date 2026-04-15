# Crear una función recursiva que permita calcular el factorial de un número. 
# Realiza un programa principal donde se lea un entero y se muestre el resultado 
# del factorial.

def Factorial(num:int)->int:
    if num == 0 or num == 1:
        return 1
    else:
        return num * Factorial(num - 1)

def main():
    num = int(input("Ingresa el numero: "))
    if num < 0:
        print("No existe factorial de numeros negativos")
        return
    print(f"El factorial de {num} es {Factorial(num)}")


main()