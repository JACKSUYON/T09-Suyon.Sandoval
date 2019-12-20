import libreria
import os
distncia=int(os.sys.argv[1])
carga1=int(os.sys.argv[2])
carga2=int(os.sys.argv[3])
constante=int(os.sys.argv[4])
msg=libreria.fuerza_electrica(distncia,carga1,carga2,constante)
print(msg)
