# Definir un histograma procedimiento() 
# que tome una lista de números enteros 
# e imprima un histograma en la pantalla. 
# Ejemplo: procedimiento([4, 9, 7]) 
# debería imprimir lo siguiente:
# ****
# *********
# *******

def procedimiento(numeros: list):
    for n in numeros:
        print("x" * n)
    
def main():
    entrada = input("Ingresa números separados por coma: ")
    numeros = [int(n.strip()) for n in entrada.split(",")]
    procedimiento(numeros)
main()