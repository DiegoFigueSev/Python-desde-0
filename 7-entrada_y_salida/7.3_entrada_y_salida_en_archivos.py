'''
Podemos manipular archivos.

Para esto Python nos incirpora un tipo integrado llamado: file

El cual es manipulado mediante un objeto archivo el cual archivo
el cual fue generado a trave de una funcion integrada en Python.
'''


'''
Antes de ver sobre manipular archivos, veremos como crearlos.


Esto se logra con el modulo os
el cual nos prmite realizar operaciones en el sistema oeprativo
como: crear una carpeta, listar contenidos, finalizar procesos, etc.
'''

import os

carpeta = 'carpeta'

# Cambiar de directorio
os.chdir('7-entrada_y_salida')

# Crear una carpeta:
os.makedirs(carpeta)

# Listar el contenido
os.listdir('./')

# Mostrar el directorio de trabajo
os.getcwd()

# Es un archivo?
os.path.isfile(carpeta)

# Es una carpeta? 
os.path.isdir(carpeta)

# Renombrar un archivo 
# os.rename([nombre], [nombre nuevo])

# Eliminar un archivo
# os.remove([archivo])

# Eliminar una carpeta
# os.rmdir([carpeta])

'''
Como vimos no hay alguna opciones para crear archivos,

os no crea archivos.

el modulo file si!
'''

'''
Ahora veamos las funciones para manipular archivos
'''

# open -> para abrir o crear archivos
# close -> para cerrar el archivo
archivo = open(f'./{carpeta}/datos.txt', 'a+')
for linea in archivo:
    print(linea)
archivo.close()

# wrhite -> escribir dentro del archivo
archivo = open(f'./{carpeta}/datos.txt', 'w')
archivo.write('Esta es una prueba \ny otra prueba mas.')
archivo.close()

# read() -> leer un archivo
archivo = open(f'./{carpeta}/datos.txt')
contenido = archivo.read()
print(contenido)
archivo.close()

'''
Para ver los diferentes modos al abrir un archivo ver el siguiente
enlace:

https://www.geeksforgeeks.org/python/file-mode-in-python/
'''



