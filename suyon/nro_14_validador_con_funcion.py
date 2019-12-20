import libreria
import os

#Argumentos
sueldo=int(os.sys.argv[1])
descuento=int(os.sys.argv[2])

total_salario_mensual=libreria.total_salario_mensual(sueldo,descuento)
print("el total del salario mensual es:",total_salario_mensual)

