def contar_digitos(numero,digito):
    contador=0
    for i in numero:
        if i==digito:
            contador=contador+1
    return contador
numeroentero=str(input("Ingrese el numero entero: "))
digitocont=str(input("Ingrese el digito a contar: "))
cantdigito = contar_digitos(numeroentero,digitocont)
print("Número ingresado: "+numeroentero)
print("Digito: "+digitocont)
print(f"Cantidad de veces {digitocont} en el número: {cantdigito}")