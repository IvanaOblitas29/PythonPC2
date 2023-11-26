def primo(numero):
    if numero<2:
        return False
    for i in range(2,numero):
        if numero%i==0:
            return False
    return True
numero = int(input("Ingrese el numero a verificar: "))
if primo(numero):
    print(f"{numero} es un número primo.")
else:
    print(f"{numero} no es un número primo.")