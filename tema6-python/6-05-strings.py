# coding=utf-8

# todos los métodos de strings
# print [method for method in dir(unaString) if callable(getattr(unaString, method))]

miString = 'Cadena'

# métodos de mayúsculas / minusculas
print miString.capitalize()
print miString.lower()
print miString.upper()
print miString.swapcase()

print
# analizando los caracteres
print miString.islower()
print miString.isupper()
print miString.istitle()
print miString.isalnum() # es alfanumérica (no espacios)
print miString.isalpha() # es alfabética (solo letras)
print miString.isdigit() # es número (solo dígitos)

print
# métodos de búsqueda
print miString.count('na')
print miString.find('na')
print miString.find('nda')
print miString.startswith('Cad')
print miString.endswith('ena')

print miString.strip() #elimina espacios al comienzo y final
print miString.strip('Ca') # elimina los caracteres
print miString.rstrip('na') # elimina solo al final (right)
print miString.lstrip('CS') # elimina solo al comienzo (left)

print miString.join(' otra string')
print miString.partition("e") # divide la cadena en una tupla con la parte antes y despué
print "dadaedededadede".split("e") # divide la cadena en una tupla con la parte antes y despué
print miString.splitlines()
