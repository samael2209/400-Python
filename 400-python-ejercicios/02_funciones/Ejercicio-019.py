# Diseñar una función que calcule 
# el área y el perímetro de una circunferencia. 
# Utiliza dicha función en un programa principal que lea el radio de 
# una circunferencia y muestre su área y perímetro.
from math import pi


def Circunferencia(r:float)->tuple:
    area = pi * r**2

    perimetro = 2 * pi * r

    return area, perimetro

def main():
    radio = float(input("Ingresa el radio de la circunferencia: "))
    if radio <= 0 :
        print("El radio debe de ser positivo")
        return

    a, p = Circunferencia(r=radio)    
    print(f"Área: {a:.2f} cm²")
    print(f"Perímetro:: {p:.2f} cm")

main()
