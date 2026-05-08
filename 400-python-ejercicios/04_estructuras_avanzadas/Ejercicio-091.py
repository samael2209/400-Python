# Crea un programa que realice una rotación a la izquierda en una lista (los elementos se 
# desplazan hacia la izquierda).

#Creamos la lista
l = [1,2,3,4,5]

# Guardamos el primer elemento de la lista
primero = l[0]

# iteramos sobre el largo de la lista - 1
for i in range(len(l) - 1):
    # guardamos el elemento de la posicion "i" en la posicion siguiente "i + 1"
    l[i] = l[i+1]

# Colocamos al final de la lista el primer elemento
l[-1] = primero

print(l)