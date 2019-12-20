import libreria
import os

#Argumentos
trabajo_util=int(os.sys.argv[1])
trabajo_suministrado=int(os.sys.argv[2])


eficiencia=libreria.eficiencia(trabajo_util,trabajo_suministrado)
print("la eficiencia es :",eficiencia)
