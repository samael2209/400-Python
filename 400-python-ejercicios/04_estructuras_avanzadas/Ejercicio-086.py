# Crea una función que calcule la unión de múltiples conjuntos. 

c1 = {1,2,3}
c2 = {9,3,4}
c3 = {4,5,1}
c4 = {1,5,3}


def interce(*args):
    resultado = set()
    
    for elemento in args[0]:
        for conjunto in args[1:]:
            
            if elemento not in conjunto:
                esta_en_todos = True
                break
    if esta_en_todos:
        resultado.add(elemento)
    
    return resultado
        
        


def union(*args):
    r = set()
    
    for conjunto in args:
        for elemento in conjunto:
            r.add(elemento)
    
    return r

print(union(c1,c2,c3,c4))
print(interce(c1,c2,c3,c4))