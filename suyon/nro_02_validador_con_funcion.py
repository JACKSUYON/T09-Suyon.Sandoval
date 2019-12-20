import libreria
import os

#Argumentos
masa=int(os.sys.argv[1])
volumen=int(os.sys.argv[2])

densidad=libreria.numero_electrones(masa,volumen)
print("la densidad es:",densidad)
