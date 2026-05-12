# Crea una función que tome una lista de direcciones de correo electrónico y 
# divida las válidas de las inválidas en dos listas separadas.

correos = [
    "juan@gmail.com",
    "maria@hotmail.com",
    "correo_invalido",
    "pedro@",
    "@gmail.com",
    "ana123@yahoo.com",
    "test.email@dominio.org",
    "sinarroba.com",
    "otro@correo",
    "usuario@mail.net"
]

validos = []
invalidos = []

for correo in correos:
    if "@" in correo and "." in correo.split("@")[-1]:
        validos.append(correo)
    else:
        invalidos.append(correo)

print(validos)
print(invalidos)