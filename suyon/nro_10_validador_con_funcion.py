import libreria
import os

#Argumentos
base_mayor=int(os.sys.argv[1])
base_menor=int(os.sys.argv[2])
altura=int(os.sys.argv[3])

area_del_trapecio=libreria.area_del_trapecio(base_mayor,base_menor,altura)
print("el area del trapecio es:",area_del_trapecio)
