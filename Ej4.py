registro={}
cantidad=int(input("Ingrese la cantidad de alumnos a registrar:"))
for i in range(0,cantidad):
    nombre=""
    nombre=input("Ingrese el nombre del alumno: ")
    registro[nombre]=[]
    for j in range(0,3):
        registro[nombre].append(input("Ingrese la nota: "))
for alumno in registro:
    print("Alumno: "+alumno+",")
    print("Notas: "+str(registro[alumno]))