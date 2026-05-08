# Implementa una función que verifique 
# si un conjunto es un subconjunto de otro conjunto.

cp = {
    frozenset({1,2,3}),
    frozenset({2,3,4}),
    frozenset({3,4,5})
}

c1 = {1,2,3}

for s in cp:
    subconjunto = True
    
    for x  in c1:
        if x not in s:
            subconjunto = False
            break 

    print(s, subconjunto)
            
        
