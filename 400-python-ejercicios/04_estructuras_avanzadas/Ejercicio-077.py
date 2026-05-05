# Desarrolla un programa que calcule 
# la suma de los valores en un diccionario anidado. 

m = {i :{j:i*j for j in range(3,5,1)} for i in range(5)}

suma = 0
for s in m.values():
    for valor in s.values():
        suma += valor

suma2 = sum(valor for s in m.values() for valor in s.values())


print(m)
print(suma)
print(suma2)
