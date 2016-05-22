# coding=utf-8

myDiccionario = {'valor1': 10, 'valor2': 20}

# todos los métodos del diccionario"
print [method for method in dir(myDiccionario) if callable(getattr(myDiccionario, method))]
print

# accedemos a un valor
print myDiccionario['valor1']
print


# si no esxiste da error
# print myDiccionario['valor3']

# con get podemos hacerlo sin riesgo
print myDiccionario.get('valor3') # devuelve None
print

# incluso usando un valor por defecto
print myDiccionario.get('valor3', 'nuevo')
print


# podemos comprobar si existe
if myDiccionario.has_key('valor2'):
    print myDiccionario['valor2']
print


# o también
if 'valor2' in myDiccionario:
    print myDiccionario['valor2']
print

# todas las llaves como unalista
print myDiccionario.keys()


# y los valores
print myDiccionario.items()

