# Escribir un programa que procese strings ingresados por el usuario. 
# La lectura finaliza cuando se hayan procesado 50 strings.
# Al finalizar, informar la cantidad total de ocurrencias de cada carácter, 
# en todos los strings ingresados. 
# Ejemplo: "r":5, "%":3, "a":8, "9":1.
# ¿Cómo se podrían informar las ocurrencias de las letras del alfabeto únicamente, 
# incluyendo el valor 0 para las letras que no aparecieron

def main():
    contador = {}

    txt = input("Ingresa string (50 max): ")

    for letra in txt:
        if letra in contador:
            contador[letra] += 1
        else:
            contador[letra] = 1
    
    print("\nOcurrencias:")
    for letra, total in contador.items():
        print(f"'{letra}': {total}")
main()