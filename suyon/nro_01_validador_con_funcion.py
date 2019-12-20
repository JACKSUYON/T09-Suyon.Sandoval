import libreria
import os

#Argumentos
numero_de_protones=int(os.sys.argv[2])
carga=int(os.sys.argv[2])

numero_electrones=libreria.numero_electrones(numero_de_protones,carga)
print("el numero de electrones es:",numero_electrones)

