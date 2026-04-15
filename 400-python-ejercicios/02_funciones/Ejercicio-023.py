# Escribir dos funciones que permitan calcular:
# La cantidad de segundos en un tiempo dado en horas, minutos y segundos.
# La cantidad de horas, minutos y segundos de un tiempo dado en segundos.
# Escribe un programa principal con un menú donde se pueda elegir 
# la opción de convertir a segundos, convertir a horas,minutos 
# y segundos o salir del programa

def ConversionSegundos(h:int, m:int, s:int) -> int :
    return h * 3600 + m * 60 + s

def ConversionHoras(s:int)->tuple:
    h = s // 3600
    m = (s % 3600) // 60
    seg = s % 60
    return h, m, seg

def main():
    while True:
        print("\n1. Convertir a segundos")
        print("2. Convertir a horas:minutos:segundos")
        print("3. Salir")
        opcion = input("Elige una opción: ")

        match opcion:
            case "1":
                h = int(input("Horas: "))
                m = int(input("Minutos: "))
                s = int(input("Segundos: "))
                print(f"Total: {ConversionSegundos(h,m,s)} segundos")
            case "2":
                total = int(input("Segundos totales: "))
                h, m, s = ConversionHoras(total)
                print(f"{h:02d}:{m:02d}:{s:02d}")
            case "3":
                print("Adios!")
                break

main()