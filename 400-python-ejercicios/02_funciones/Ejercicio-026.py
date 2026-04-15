# Queremos crear un programa que trabaje con fracciones a/b. 
# Para representar una fracción vamos a utilizar dos enteros: numerador y denominador.

def Fracciones(numerador: int, denominador: int) -> tuple:
    if denominador == 0:
        raise ValueError("El denominador no puede ser cero")
    return numerador, denominador, numerador / denominador

def main():
    try:
        num = int(input("Numerador: "))
        den = int(input("Denominador: "))
        n, d, resultado = Fracciones(num, den)
        print(f"{n}/{d} = {resultado:.2f}")
    except ValueError as e:
        print(e)
main()