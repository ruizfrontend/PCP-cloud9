# coding=utf-8

# Condicional
valor = 1

if valor == 1:
    print 1
elif valor == 2:
    print 2
else:
    print 'ni uno ni dos'
print

# bucle while
value = 0
while value < 5:
    value += 1
    print 'valor', value
print

# bucle while infinito: necesitamos break
while True:
    nombre = raw_input("Indique su nombre: ") # solicita input al usuario
    if nombre:
        print 'Hello',nombre
        break
print

# bucle for con lista
for nombre in ['Ramón', 'Harri', 'Nayra', 'David'] : 
    print nombre
print

# bucle for con un rango  
for nombre in range(0, 10): 
    print nombre