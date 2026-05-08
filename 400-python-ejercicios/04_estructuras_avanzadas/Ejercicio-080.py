# Diseña un programa que combine dos listas de tuplas en una sola lista,
# eliminando duplicados basados en el primer elemento de cada tupla

t1 = [(i, i*2) for i in range(3)]
t2 = [(i, i*6) for i in range(9)]

# 1. Reservar espacio total
t = [None] * (len(t1) + len(t2))

# 2. Copiar manualmente
k = 0

# copiar t1
for i in range(len(t1)):
    t[k] = t1[i]
    k += 1

# copiar t2
for j in range(len(t2)):
    t[k] = t2[j]
    k += 1


print(t)