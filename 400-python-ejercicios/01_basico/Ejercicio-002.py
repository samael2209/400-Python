# Hacer un programa que solicite por teclado dos número 
# y muestre la suma , la resta ,la multiplicación y la división de esos números 

num1:int = int(input("Ingresa tu primer numero: "))
num2:int = int(input("Ingresa tu segundo numero: "))

print(f"La suma de los numeros {num1} y {num2} es {num1 + num2}")
print(f"La resta de los numeros {num1} y {num2} es {num1 - num2}")
print(f"La multiplicacion de los numeros {num1} y {num2} es {num1 * num2}")
if num2 != 0 :
    print(f"La division de los numeros {num1} y {num2} es {num1 / num2}")
else:
    print(f"No se puede dividir para cero {num2}")
