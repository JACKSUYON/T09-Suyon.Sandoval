import libreria
import os

#Argumentos

velocidad_inicial=int(os.sys.argv[1])
velocidad_final=int(os.sys.argv[2])
tiempo=int(os.sys.argv[3])

altura=libreria.altura(velocidad_inicial,velocidad_final,tiempo)
print("la altura es:",altura)
