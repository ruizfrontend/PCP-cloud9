# coding=utf-8

# abrir archivos
myFile = open('../readme.md')


# leer el archivo completo
print myFile.read()

# punteros apuntan a la linea actual, lo reiniciamos
myFile.seek(0)

# leer una línea
print 'leemos una línea: ', myFile.readline()
print


# puntero: dónde estamos leyendo:
print 'Leído hasta caracter', myFile.tell() # reiniciamos puntero
print


# y guardarlo como una lista de lineas
print myFile.readlines()


# al terminar con un archivo hay que cerrarlo
myFile.close()


# un bucle con todo el proceso
with open('../readme.md') as f:
    for line in f:
        print 'linea:', line


# crear y escribe archivo
newFile = open('./textFile', 'w') # w para escribir, r para leer y a para añadir
newFile.write('Hello file')
newFile.close()