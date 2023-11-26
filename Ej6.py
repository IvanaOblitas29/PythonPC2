a=0
b=1
fin=50
arreglo=[]
while a<=fin:
    arreglo.append(a)
    a,b=b,a+b
print(arreglo)