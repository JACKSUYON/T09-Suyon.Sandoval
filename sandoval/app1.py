# Ejercicio 01
# Programa que utiliza la funcion sumar
import libreria
import os

v=int(os.sys.argv[1])
t=int(os.sys.argv[2])

d=libreria.distancia(v,t)
msg="La disancia de {} y {} es : {}"
print(msg.format(v,t,d))

