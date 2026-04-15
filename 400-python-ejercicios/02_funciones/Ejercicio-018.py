# Crea una función “calcularMaxMin” que recibe una lista con valores
# numéricos y devuelve el valor máximo y el mínimo. 
# Crea un programa que pida números por teclado y 
# muestre el máximo y el mínimo, utilizando la función anterior.

def CalcularMaxMin(list_num:list) -> tuple:
    maximo = list_num[0]
    minimo = list_num[0]

    for num in list_num:
        if num > maximo:
            maximo = num
        if num < minimo:
            minimo = num

    return maximo, minimo


list_num = []
while True:
    entrada = input("Ingresa un numero (o ingresa 'x' para salir) :")
    if entrada == "x":
        break 
    list_num.append(float(entrada))


if list_num:
    maximo, minimo = CalcularMaxMin(list_num)
    print(f"Máximo: {maximo}")
    print(f"Mínimo: {minimo}")
