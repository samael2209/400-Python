# Definir una función max() que tome como argumento dos números 
# y devuelva el mayor de ellos.
# (Es cierto que python tiene una función max() incorporada, 
# pero hacerla nosotros mismos es un muy buen ejercicio.)

def Max(num1:int, num2:int) ->int:
    return num1 if num1 > num2 else num2

def main():
    num1 = int(input("Ingresa el primer numero: "))
    num2 = int(input("Ingresa el segundo numero: "))
    
    print(f"El numero mayor entre {num1} y {num2} es {Max(num1, num2)} ")
    
main()