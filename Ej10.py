def cambio_formato(fecha):
    dia,mes,anio=fecha.split('/')
    resultado=f"{anio}-{mes.zfill(2)}-{dia.zfill(2)}"
    return resultado
fecha_entrada=input("Ingrese la fecha (en formato dd/mm/yyyy): ")
fecha_salida=cambio_formato(fecha_entrada)
print("Input: "+fecha_entrada)
print("Output: "+fecha_salida)