# El día juliano correspondiente a una fecha es un número entero 
# que indica los días que han transcurrido desde el 1 de enero del año indicado. 
# Queremos crear un programa principal que al introducir una fecha nos diga el día juliano que corresponde. 
#  Para ello podemos hacer las siguientes subrutinas:
#  LeerFecha: Nos permite leer por teclado una fecha (día, mes y año).
#  DiasDelMes: Recibe un mes y un año y nos dice los días de ese mes en ese año.
#  EsBisiesto: Recibe un año y nos dice si es bisiesto.
#  Calcular_Dia_Juliano: recibe una fecha y nos devuelve el día juliano.

def LeerFecha() -> tuple:
    dia = int(input("Dia: "))
    mes = int(input("Mes: "))
    año = int(input("Año: "))

    return dia, mes, año

def EsBisiesto(año:int) -> bool:
    return año % 4 == 0 and (año % 100 != 0 or año % 400 == 0)

def DiasDelMes(mes:int, año:int) -> int:
    dias_por_mes = [31,28,31,30,31,30,31,31,30,31,30,31]
    if mes == 2 and EsBisiesto(año):
        return 29
    return dias_por_mes[mes - 1]

def Calcular_Dia_Juliano(dia:int, mes:int, año:int) -> int:
    dia_juliano = 0
    for m in range(1, mes):
        dia_juliano += DiasDelMes(m, año)
    return dia_juliano + dia

dia, mes, año = LeerFecha()
print(f"El día juliano es: {Calcular_Dia_Juliano(dia, mes, año)}")