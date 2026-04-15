# Escribir una funcion sum() y una función multip()
# que sumen y multipliquen respectivamente todos los números 
# de una lista. 
# Por ejemplo: sum([1,2,3,4]) debería devolver 10 
# y multip([1,2,3,4])debería devolver 24.

def SumaLista(lista_numeros:list) -> int:
    t = 0
    for n in lista_numeros:
        t += n
    return t

def Multip(lista_numeros) -> int:
    t = 1
    for n in lista_numeros:
        t *= n
    return t

def main():
    numeros = [1, 2, 3, 4]
    print(f"Suma: {SumaLista(numeros)}")
    print(f"Multiplicación: {Multip(numeros)}")
main()
        