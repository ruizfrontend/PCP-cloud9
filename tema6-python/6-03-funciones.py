# coding=utf-8

# una función con un parámetro y un valor por defecto
def helloWorld(nombre='World'):
    print 'Hola', nombre

helloWorld()
helloWorld('unir')


# podemos pasar los parámetros por su nombre desordenados
def pruebaParametros(nombre='World', apellidos=''):
    print 'Hola', nombre, apellidos

pruebaParametros(apellidos='programacion', nombre='curso')


# enviando una lista como parámetros
listaParametros = ['David', 'Ruiz']
pruebaParametros(*listaParametros) # ojo con el asterisco


# o un diccionario 
diccionarioParametros = { 'apellidos': 'bienvenida', 'nombre': 'otra'}
pruebaParametros(**diccionarioParametros) # ojo con el doble asterisco


# recoge cualquier número de parámetros como una tupla
def multiplesParametros(*parametros):
    for parametro in parametros:
        print parametro

multiplesParametros('parametro1', 'parametro2', 'parametro3')


# en todo momento podemos acceder a las variables y funciones
# definidas en nuestro contexto o globalmente

def pruebaContexto():
    var1 = 'valor'
    print locals()
    print globals()

pruebaContexto()
print range(5)
print [x*x for x in range(5) if x % 2 == 0]