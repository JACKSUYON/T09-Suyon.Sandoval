import libreria
import os
densidad=int(os.sys.argv[1])
altura=int(os.sys.argv[2])
gravedad=float(os.sys.argv[3])

res=libreria.precion_hodrostatica(densidad,altura,gravedad)
print(int(res))
