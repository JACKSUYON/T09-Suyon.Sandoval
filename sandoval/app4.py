# Ejercicio 04
import libreria
import os
msa=int(os.sys.argv[1])
aceler=int(os.sys.argv[2])

f=libreria.fuerza(msa,aceler)
msg="la fuerza del asensor es:{}"
print(msg.format(f))

