import libreria
import os

#Argumentos
pi=3.1416
radio=int(os.sys.argv[1])
generatriz=int(os.sys.argv[2])

area_lateral_cono=libreria.area_lateral_cono(pi,radio,generatriz)
print("el area lateral del cono es :",area_lateral_cono)


