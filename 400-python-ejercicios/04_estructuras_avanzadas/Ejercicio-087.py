# Desarrolla un programa que encuentre la diferencia simétrica entre dos conjuntos.


c1 = {1,2,3}
c2 = {9,3,4}
c3 = {4,5,1}
c4 = {1,5,3}


def diferencia(*args):
    r = set()
    
    for conjunto in args:
        
        for elemento in conjunto:
            if elemento in r:
                r.remove(elemento)
            else:
                r.add(elemento)
    
    return r

print(diferencia(c1,c2,c3,c4))