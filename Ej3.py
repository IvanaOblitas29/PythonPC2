respuesta="SI"
numeros=[]
par=0
impar=0
while respuesta=="SI":
    respuesta=input("Desea ingresar un número?: ")
    if respuesta=="SI":
        numero=int(input("Ingrese el número: "))
        numeros.append(numero)
    if  respuesta=="NO":
        break
print("Números ingresados: "+ str(numeros))
for i in numeros:
    if i%2==0:
        par=par+1
    else:
        impar=impar+1
print("Cantidad de números pares: "+str(par))
print("Cantidad de números impares: "+str(impar))