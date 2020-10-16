import math

"""
***************************************************************
@@ ejercicio 1 @@
un metodo python que haga la suma de 2 numeros
2+4 = 6
"""


# start-->
def suma(num1,num2):
    result = num1+num2
    return result


"""
***************************************************************
@@ ejercicio 2 @@
la suma de los numeros pares del 1 al 1000
"""


# start-->
def sumaPares(longitud):

    sumatotal = 0
    i = 0
    sumatotal = 0
    while i <= int(longitud):
        if (i %2 == 0):
            sumatotal += i
        i += 1
    return sumatotal


"""
***************************************************************
@@ ejercicio 3 @@
encontrar el area total de superficie de un cilindro
radio = 5 m
altura = 7 m
area lateral: 2*pi*r*a
area circulo: 2*pi*r^2
area total: area lateral + area circulo
"""


# start-->
def areaTotalCilindro(radio, altura):
    result = round(areaLateral(radio,altura) + areaCirculo(radio),2)

    return result


def areaLateral(radio, altura):
    result = 2.0*math.pi*radio*altura
    return result


def areaCirculo(radio):
    result = 2.0*math.pi*radio**2
    return result


"""
***************************************************************
@@ ejercicio 4 @@
el ejercicio numero 3 convertirlo en una clase

"""


# start-->
class Cilindro:
 
    def __init__(self, radio, altura):
        
        self.radio = radio
        self.altura = altura
        
    def areaTotalCilindro(self):
        result = round(areaLateral(self.radio,self.altura) + areaCirculo(self.radio),2)
        return result

    def areaLateral(self):
        result = 2.0*math.pi*self.radio*self.altura
        return result
    def areaCirculo(self):
        result = 2.0*math.pi*self.radio**2
        return result


        
        
            
        


"""
***************************************************************
@@ ejercicio 5 @@
restaurante de pizzas
pizza
    nombre
    lugar
    costo
    conDescuento
    descuento
"""


class Restaurante:
    def __init__(self):
        self.restaurante = ()
    def ordenar(self,nombre,lugar,costo,conDescuento,descuento):
        neworder = (nombre,lugar,costo,conDescuento,descuento)
        self.restaurante.append(tuple(neworder))


    
    def costoTotal(self):
        costo = 0 
        costoTotal = 0 
        for orden in self.restaurante:
            costo = Restaurante[2]
            costoTotal =  costoTotal + costo
            return costoTotal

        return 0

    def costoTotalConDescuento(self):
        return 0


class Pizza:
    pass


"""
***************************************************************
@@ ejercicio 6 @@
colocar este proyecto en github
colocar aca debajo la url
ademas colocar la url en un archivo
github_<nombre>_<codigo>.txt y subirlo a moodle
"""


# github url-->
def getGithubUrl():
    result = "https://github.com/guillegacia/parcialv2.git"
    return result
