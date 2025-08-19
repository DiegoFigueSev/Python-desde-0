'''
Una lista por comprension o List comprenhension

Es una de las principales ventajas de Python

Una list comprenhension nos permite crear
listas de elementos en una sola linea de codigo
'''

from math import pi


lista = [x**3 for x in range(4)]
print(lista)

# que es lo mismo que hacer:
cubos = []
for i in range(5):
    cubos.append(i ** 3)
print(cubos)

'''
Como tal el resultado es el mismo, pero resulta
menos claro
'''

'''
La sintaxis de las listas por comprension es:
lista = [expresión for elemento in iterable]

La lista puede tener cero o mas declaraciones for o if
'''

'''
Los usos mas comunes de este tipo de listas es
cuando cada elemento es el resultado de 
alguna operacion apliada a cada miembro de otra 
secuencia o iterable.
'''

# Basicamente como aplicar un map con menos pasos

lista = [(x,y) for x in [1,2,3] for y in [4,5,6] if x != y]
print(lista)
# La creacion anterior nos regresa todas las 
# combinaciones que podemos hacer entre las 
# dos listas, siemrpe y cuando se cumpla
# el if

'''
Las listas por comprension pueden tener tambien
expresiones complejas y funciones anidadas
'''

lista = [str(round(pi, i)) for i in range (1,6)]
print(lista)
'''
En este caso ya no se usa una variable nromal x
si no el elemento de la lista sera el retorno de una funcion
'''


'''
LAS LISTAS DE COMPRENSION IGUAL PUEDEN ANIDARSE
'''

matrix = [[1,2,3,4], [5,6,7,8], [9,10,11,12]]
lista = [[row[i] for row in matrix] for i in range(4)]
print(lista)