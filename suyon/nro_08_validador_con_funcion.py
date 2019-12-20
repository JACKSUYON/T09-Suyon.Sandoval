import libreria
import os

#Argumentos
distancia=int(os.sys.argv[1])
velocidad1=int(os.sys.argv[2])
velocidad2=int(os.sys.argv[3])

tiempo_alcance=libreria.tiempo_alcance(distancia,velocidad1,velocidad2)
print("el tiempo de alcance es:",tiempo_alcance)
