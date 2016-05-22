# coding=utf-8

# Esto es un comentario

"""y esto también,
pero de varias líneas """

unBooleano = True

unEntero = 30

unFloating = 0.1

unaOperacion = unEntero * unFloating

unaString = 'texto'

# ver el tipo de una variable
print type(unaString)

# tuplas => lista invariables
unaTupla = ('texto', 10, 2.5)

    #accediendo
print unaTupla[1]
print unaTupla[1:2]
print unaTupla[:2]


# cambiando una tupla => object does not support item assignment
# unaTupla[1] = 'otroTexto' 


# listas => pueden variar
unaLista = ['texto', 15, 2.8, 'otro dato', 25]
print unaLista[1]


# diccionarios => como json
unDiccionario = {'valor1': 10, 'valor2': 20}


# asignación múltiple
a, b, c = 'string', 15, True


# como en javascript los tipos son objetos con una serie de métodos incluidos
# mostramos todos los métodos de la lista


print "métodos del booleano"
print
print [method for method in dir(unBooleano) if callable(getattr(unBooleano, method))]
print

print "métodos del entero"
print
print [method for method in dir(unEntero) if callable(getattr(unEntero, method))]
print

print "métodos del flotante"
print
print [method for method in dir(unFloating) if callable(getattr(unFloating, method))]
print

print "métodos de la tupla"
print
print [method for method in dir(unaTupla) if callable(getattr(unaTupla, method))]
print
