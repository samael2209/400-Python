# Crear una función que calcule el MCD de dos número por el método de Euclides. 
# El método de Euclides es el siguiente:
# Se divide el número mayor entre el menor.
# Si la división es exacta, el divisor es el MCD.
# Si la división no es exacta, dividimos el divisor entre el resto obtenido 
# y se continúa de esta forma hasta obtener una división exacta, 
# siendo el último divisor el MCD.
# Crea un programa principal que lea dos números enteros y muestre el MCD.

def MCD(numMax:int, numMin:int) -> bool:
    if numMin == 0:
        return numMax
    return MCD(numMin, numMax % numMin)

def main():
    num1 = int(input("Primer numero: "))
    num2 = int(input("Segundo numero: "))

    print(f"El MCD de {num1} y {num2} es {MCD(num1, num2)}")

main()