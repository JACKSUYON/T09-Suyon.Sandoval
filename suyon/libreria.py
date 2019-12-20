#Jack-Libreria de funciones

#1.funcion que devuelve el numero de electrones
def numero_electrones(numero_de_protones,carga):
    return (numero_de_protones + carga)

#2.funcion que devuelve la densidad
def densidad(masa,volumen):
    return (masa*volumen)

#3.funcion que devuelve el area lateral de un cono
def area_lateral_cono(pi,radio,generatriz):
    return (pi*radio*generatriz)

#4.funcion que devuelve el area total piramide
def area_total_piramide(area_lateral_piramide,area_base_piramide):
    return (area_lateral_piramide + area_base_piramide)

#5.funcion que devuelve el volumen de una piramide
def volumen_piramide(area_base_de_la_piramide,altura):
    return ((area_base_de_la_piramide*altura)/3)

#6.funcion que devuelve el area lateral del cilindro
def area_lateral_cilindro(pi,radio1,generatriz1):
    return(2*pi*radio1*generatriz1)

#7.funcion que devuelve tiempo de enuentro
def tiempo_encuentro(distancia,velocidad1,velocidad2):
    return (distancia)/(velocidad1 + velocidad2)

#8.funcion que devuelve el tiempo de alcance
def tiempo_alcance(distancia,velocidad1,velocidad2):
    return ((distancia)/(velocidad1 - velocidad2))

#9.funcion que devuelve la presion hidrostatica
def presion_hidrostatica(densidad,gravedad,altura):
    return (densidad*gravedad*altura)

#10.funcion que devuelve el area del trapecio
def area_del_trapecio(base_mayor,base_menor,altura):
    return ((base_mayor+base_menor)*altura)/2

#11.funcion que devuelve la fuerza
def Fuerza(Masa,Aceleracion):
    return (Masa*Aceleracion)

#12.funcion que devuelve la altura
def altura(velocidad_inicial,velocidad_final,tiempo):
    return ((velocidad_inicial+velocidad_final)/2)*tiempo

#13.funcion que devuelve la presion
def presion(densidad,altura,gravedad):
    return (densidad*altura*gravedad)

#14.funcion que devuelve el total del salario mensual
def total_salario_mensual(sueldo,descuento):
    return (sueldo-descuento)

#15.funcion que devuelve la eficiencia
def eficiencia(trabajo_util,trabajo_suministrado):
    return trabajo_util/trabajo_suministrado

#16.funcion que devuelve el area del circulo
def area_circulo(radio,pi,msg):
    res=(pi*radio**2)
    if (res>100):
        msg="el area es demasiodo grande"
    return res,msg



