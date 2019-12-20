import libreria
import os

#Argumentos
area_lateral_piramide=int(os.sys.argv[1])
area_base_piramide=int(os.sys.argv[2])

area_total_piramide=libreria.area_total_piramide(area_lateral_piramide,area_base_piramide)
print("el area total de la piramide es:",area_total_piramide)
