# Crear una subrutina llamada “Login”, 
# que recibe un nombre de usuario y una contraseña y 
# te devuelve Verdadero si el nombre de usuario es “usuario1”
#  y la contraseña es “asdasd”. 
# Además recibe el número de intentos que se ha intentado 
# hacer login y si no se ha podido hacer login incremente este valor.
#  Crear un programa principal donde se pida un nombre de usuario 
# y una contraseña y se intente hacer login, 
# solamente tenemos tres oportunidades para intentarlo.

def Login(usuario:str, password:str) -> bool:
    return usuario == "usuario1" and password == "asdasd"

def main():
    contador = 3
   
    while contador >= 0:
        usuario = input("Ingrese su usuario: ")
        password = input("Ingrese su contraseña: ")

        if Login(usuario, password):
            print("Bienvenido!!")
            return
        else:
            contador -= 1
            if contador > 0:
                print(f"Login fallido. Te quedan {contador} intento(s)")
            else:
                print("Login fallido. Acceso denegado.")

main()




