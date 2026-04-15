# Crea un programa que pida dos número enteros al usuario 
# y diga si alguno de ellos es múltiplo del otro. 
# Crea una función EsMultiplo que reciba los dos números, 
# y devuelve si el primero es múltiplo del segundo.

def EsMultiplo(n1:int, n2 :int)->bool:
    if n2 == 0:
        return False
    return n1 % n2 == 0

n1 = int(input("Numero 1: "))
n2 = int(input("Numero 2: "))

if EsMultiplo(n1, n2):
    print(f"{n1} es multiplo de {n2}")
elif EsMultiplo(n2, n1):
    print(f"{n2} es multiplo de {n1}")
else:
    print("No son multiplos entre si")



EsMultiplo(10,5)
