# Ejercicio 02
# Programa que utiliza la funcion area_cuadrado
import libreria
import os

a=int(os.sys.argv[1])
b=int(os.sys.argv[2])
c=int(os.sys.argv[2])

vol=libreria.volumen_cubo(a,b,c)
msg="El volumen del cubo es: {}"
print(msg.format(a))
