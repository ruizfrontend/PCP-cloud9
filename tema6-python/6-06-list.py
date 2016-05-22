# coding=utf-8

miLista = ['Cadena', 'de', 'cosas']
print miLista

# todos los métodos de una lista
print [method for method in dir(miLista) if callable(getattr(miLista, method))]
print

# añadiendo elementos
miLista.append("Nuevo elemento")
miLista.extend(["incluimos varios", " elementos"])
miLista.insert(3, "Elemento intercalado")

print miLista
print

# eliminando elementos
miLista.pop()
miLista.pop(3)
miLista.remove("cosas")

print miLista
print

# modificando orden
miLista.reverse()
miLista.sort(reverse=True)

print miLista
print

# print miLista.count()

# crear, iterar y ejecutar una lista todo en una línea
print [x.upper() for x in miLista]
print

# unión de listas
miLista2 = ['otra', 'lista']
print miLista + miLista2
print

# no elimina duplicados
print miLista2 + miLista2

elm1, elm2 = [3, 4]
print elm1, elm2