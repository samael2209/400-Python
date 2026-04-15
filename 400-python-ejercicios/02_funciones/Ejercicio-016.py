# Crear una función que calcule la temperatura media de un día 
# a partir de la temperatura máxima y mínima. 
# Crear un programa principal, que utilizando la función anterior,
#  vaya pidiendo la temperatura máxima y mínima de cada día 
# y vaya mostrando la media. 
# El programa pedirá el número de días que se van a introducir


def TemperaturaMedia(temMax:float, temMin:float)->float:
    if temMax < temMin:
        temMax, temMin = temMin, temMax
    return (temMax + temMin) / 2

def main():
    numDias = int(input("Cuanto dias vas a ingresar: "))
    for i in range(numDias):
        temMax = float(input(f"Ingresa la temperatura maxima del dia {i+1}: "))
        temMin = float(input(f"Ingresa la temperatura minima del dia {i+1}: "))

        print(f"Día {i+1}: {TemperaturaMedia(temMax, temMin):.2f}°C")


main()