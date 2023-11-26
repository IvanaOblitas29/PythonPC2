def factorial(numero):
    fact=1
    for i in range(1,numero+1):
        fact=fact*i
    return fact
averiguar=int(input("Ingrese un numero: "))
resultado=factorial(averiguar)
print(f"El factorial de {averiguar} es {resultado}")