# A) Solicitar al usuario que ingrese números, los cuales se guardarán en una lista.
#    Finalizar al ingresar el número 0, el cual no debe guardarse.
# B) A continuación, solicitar al usuario que ingrese un número y, si el número está en la lista,
#    eliminar su primera ocurrencia. Mostrar un mensaje si no es posible eliminar.
# C) Recorrer la lista para imprimir la sumatoria de todos los elementos.
# D) Solicitar al usuario otro número y crear una lista con los elementos de la lista original que
#    sean menores que el número dado. Imprimir esta nueva lista, iterando por ella.
# E) Generar e imprimir una nueva lista que contenga como elementos a tuplas de dos
#    elementos, cada una compuesta por un número de la lista original y la cantidad de veces que
#    aparece en ella.

def ingresar_numeros() -> list:
    numeros = []
    while True:
        n = int(input("Número (0 para salir): "))
        if n == 0:
            break
        numeros.append(n)
    return numeros

def eliminar_primera_ocurrencia(numeros: list) -> list:
    elim = int(input("Número a eliminar: "))
    if elim in numeros:
        numeros.remove(elim)
        print(f"'{elim}' eliminado")
    else:
        print("No está en la lista")
    return numeros

def sumatoria(numeros: list):
    total = 0
    for n in numeros:
        total += n
    print(f"Sumatoria: {total}")

def menores_que(numeros: list):
    limite = int(input("Ver números menores que: "))
    menores = []
    for n in numeros:
        if n < limite:
            menores.append(n)
    print("Menores:", menores)

def tuplas_frecuencia(numeros: list) -> list:
    resultado = []
    for n in numeros:
        conteo = 0
        for num in numeros:
            if num == n:
                conteo += 1
        if n not in [item[0] for item in resultado]:
            resultado.append((n, conteo))
    return resultado

def main():
    print("=== A) Ingresar números ===")
    numeros = ingresar_numeros()
    if not numeros:
        print("Lista vacía")
        return
    
    print("\n=== B) Eliminar primera ocurrencia ===")
    numeros = eliminar_primera_ocurrencia(numeros)
    
    print("\n=== C) Sumatoria ===")
    sumatoria(numeros)
    
    print("\n=== D) Menores que X ===")
    menores_que(numeros)
    
    print("\n=== E) Tuplas (número, frecuencia) ===")
    resultado = tuplas_frecuencia(numeros)
    print(resultado)

main()