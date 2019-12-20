import libreria
import os

#Argumentos
pi=3.1416
radio1=int(os.sys.argv[1])
generatriz=int(os.sys.argv[2])

area_lateral_cilindro=libreria.area_lateral_cilindro(pi,radio1,generatriz)
print("el area lateral del cilindro es:",area_lateral_cilindro)
