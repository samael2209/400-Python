# Hacer un programa que solicite un color por teclado e imprima 
# “Puede pasar “ si el color ingresado es verde , 
# “Precaución “ si es amarillo , 
# “No pasar “ si es rojo o 
# “Color inválido” si es cualquier otro.

color = input("Ingresa un color: ").lower()

match color:
    case 'verde':
        print("Puede pasar")
    case 'amarillo':
        print("Precaucion al pasar")
    case 'rojo':
        print("No puede pasar")
    case _ :
        print("Color invalido")

