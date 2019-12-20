import libreria
import os

#Argumentos
area_base_de_la_piramide=int(os.sys.argv[1])
altura=int(os.sys.argv[2])

volumen_piramide=libreria.volumen_piramide(area_base_de_la_piramide,altura)
print("el volumen de la piramide es:",volumen_piramide)
