# Vamos a mejorar el ejercicio anterior haciendo una función para validar la fecha. 
# De tal forma que al leer una fecha se asegura que es válida.si

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

def ValidarFecha(dia: int, mes: int, año: int) -> bool:
    if mes < 1 or mes > 12:
        return False
    if dia < 1 or dia > DiasDelMes(mes, año):
        return False
    return True

dia, mes, año = LeerFecha()
if ValidarFecha(dia, mes, año):
    print(f"El día juliano es: {Calcular_Dia_Juliano(dia, mes, año)}")
else:
    print("Fecha inválida")