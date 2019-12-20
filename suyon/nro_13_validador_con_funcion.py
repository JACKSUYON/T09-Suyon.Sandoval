import libreria
import os

#Argumentos
densidad=int(os.sys.argv[1])
altura=int(os.sys.argv[2])
gravedad=int(os.sys.argv[3])

presion=libreria.presion(densidad,altura,gravedad)
print("la presion es:",presion)

