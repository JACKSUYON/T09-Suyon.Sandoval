import libreria
import os

#Argumentos
densidad=int(os.sys.argv[1])
gravedad=int(os.sys.argv[2])
altura=int(os.sys.argv[3])

presion_hidrostatica=libreria.presion_hidrostatica(densidad,gravedad,altura)
print("la presion hidrostatica :",presion_hidrostatica)

