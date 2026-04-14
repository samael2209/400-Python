#  Hacer un programa donde se muestre el siguiente dibujo                    
# *  *  *  *  *  *  *  *  *  *          
# *                          *                    
# *                          *
# *                          *
# *  *  *  *  *  *  *  *  *  *

for i in range(5):
    if i == 0 or i == 4:
        print("*  " * 10)
    else:
        print("*", " " * 26, "*", sep="")