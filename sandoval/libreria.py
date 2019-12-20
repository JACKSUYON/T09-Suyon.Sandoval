# Elmer - Libreria de funciones

# Ejercicio 01
# Funcion que devuelve la distancia
def distancia(velocidad,tiempo):
    return (velocidad*tiempo)




# Ejercicio 02
#. Función que devuelve el volumen de un cubo
def volumen_cubo(lado1,lado2,lado3):
    volumen=(lado1*lado2*lado3)
    return volumen



# Ejercicio 03
#. Función que devuelve ña densida de un cuepo
def densidad(masa,volumen):
    densidad=(masa*volumen)
    return densidad


# Ejercicio 04
#. Función que devuelve la fuerza del acensor
def fuerza(masa,aceleracion):
    return (masa*aceleracion)


# Ejercicio 05
#. Función que devuelve la suma
def sumar(a,b):
    return a + b


# Ejercicio 06
#. Función que devuelve la cadena
def restar(a,b):
    return a-b


# Ejercicio 07
#. Función que devuelve la media de los siguientes numeros
def media(x,y):
    m=(x+y)/2
    return m


# Ejercicio 08
#. Función que devuelve el promedio final
def promedio(nota1,nota2):
    promedio_invalido=True
    valor=0,0
    while (promedio_invalido):
        valor=(nota1+nota2)/2
        promedio_invalido=(valor<9)
    return valor


# Ejercicio 09
#. Función que devuelve el numero celular
def nro_celular(msg):
    nro_invalido=True
    while(nro_invalido):
        numero_celular=int(msg)
        nro_invalido=(len(str(nro_celular)) != 9)
    return int(numero_celular)



# Ejercicio 10
#. Función que devuelve el numero de ruc
def nro_ruc(msg):
    nro_invalido=True
    valor=0
    while(nro_invalido):
        valor=int(msg)
        nro_invalido=(len.isdigit()!=11)
    return valor


# Ejercicio 11
#. Función que devuelve la multiplicacion
def multiplicar(a,b,c,d):
    return (a*b*c*d)



# Ejercicio 12
#. Función que devuelve el area del rectangulo
def area_rectangulo(base,altura):
    resultado=base*altura
    return resultado


# Ejercicio 13
#. Función que devuelve el
def precion_hodrostatica(densidad,altura,gravedad):
    resultado=densidad*altura*gravedad
    return resultado


# Ejercicio14
#.Funciones devolver trabajo
def trabajo(fuerza,distancia):
    trab=fuerza*distancia
    return trab


# Ejercicio 15
#.funciones devolver peso
def peso(masa,gravedad):
    result=masa*gravedad
    return result


# Ejercicio 16
#.funcines devolver velocidad
def velocida(distancia,tiempo):
    vel=distancia/tiempo
    return vel


#Ejercicio 17
#.Funciones devolver digitos
def nro_digitos(a):
    if (len(a) == 6):
        if (a.isdigit() == True):
            res=a,"es valido"
            return res
        else:
            res=a , "invalido no son numeros"
            return res
    #fin_if

    else:
        res=a , "es invalido (debe tener 6 digitos)"
        return res

#fin_if

#Ejercicio 18
#Funciones delvolver
def nro_casa(nro):
    if (len(nro) == 3):
        if (nro.isdigit() == True):
            res=nro , "es valido"
            return res
        else:
            res=nro, "no es valido son numeros"
            return res
    # fin_if
    else:
        res=nro, ("es valido debe tener 3 digitos")
        return res
# fin_if

#Ejercicio 19
#Funciones devolver ruc
def nro_ruc(msg):
    ruc_invalido=True
    while (ruc_invalido):
        ruc=int(msg)
        ruc_invalido=(len(str(ruc)) != 11)
    return int(ruc)
# fin_while

# Ejercicio 20
# funciones devolver
def acelacion(fuerza,masa,msg):
    ace=fuerza/masa
    if (ace>200):
        msg="le gusta la velocidad"
    return ace,msg


#Ejercicio 21
#Funciones devolver nombre con 5 caracteres
def nombre(msg):
    if (len(msg) == 5):
        if (msg.isalpha() == True):
            nom=msg, "es valido"
            return nom
        else:
            nom=msg, "es nvalido (no son numeros)"
    else:
        nom=msg, "es invalido (debe tener 5 letras)"
        return nom

# Ejercicio 22
# Funciones devolver nro pares
def nro_pares(a,msg):
    if (a %2 == 0):
        msg="es par"
    else:
        msg="no es par"
    return a,msg
# fin_if

# Ejercicio 23
# funciones devolver nro impar
def nro_impar(a,msg):
    if (a %2 != 0):
        msg="es impar"
    else:
        msg="no es impar"
    return a,msg
# fin_if

# Ejercicio 24
#Funciones delvolver area del circulo
def area_circulo(radio,pi):
    area=(radio**2)*pi
    return area

#Ejercicio 25
# funciones devolver fuerza electricas
def fuerza_electrica(distancia,carga1,carga2,constante):
    fuerza_elc=(carga1*carga2*constante)/distancia**2
    return fuerza_elc
