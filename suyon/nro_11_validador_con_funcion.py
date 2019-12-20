import libreria
import os

#Argumentos
Masa=int(os.sys.argv[1])
Aceleracion=int(os.sys.argv[2])

Fuerza=libreria.Fuerza(Masa,Aceleracion)
print("la fuerza es :",Fuerza)
