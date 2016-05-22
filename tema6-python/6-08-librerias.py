# coding=utf-8

import os
import sys

# obtenemos todas las variables del sistema
for variable, valor in os.environ.iteritems(): 
    print "Variable %s valor - %s" % (variable, valor)
print

# acceder a información del sistema    
print 'Estamos ejecutando', sys.argv
print 'Python se ejecuta desde', sys.executable
print 'Version de python', sys.version 
print
