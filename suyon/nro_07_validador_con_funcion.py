import libreria
import os

#Argumentos
distancia=int(os.sys.argv[1])
velocidad1=int(os.sys.argv[2])
velocidad2=int(os.sys.argv[3])

tiempo_encuentro=libreria.tiempo_encuentro(distancia,velocidad1,velocidad2)
print("el tiempo de encuentro es:",tiempo_encuentro)
