# coding=utf-8

# importamos un módulo
import miPaquete.miModulo

print miPaquete.miModulo.CONSTANTE


# alias simplifican las llamadas y evitan conflictos de nombres
import miPaquete.miModulo as alias

print alias.CONSTANTE

# importamos solo la constante
from miPaquete.miModulo import CONSTANTE

print CONSTANTE

# podemos darla un alias también
from miPaquete.miModulo import CONSTANTE as aliasCONSTANTE

print aliasCONSTANTE