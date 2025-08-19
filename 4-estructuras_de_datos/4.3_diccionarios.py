'''
El diccionario, define una relacion uno a uno 
entre clave y valor 

Los diccionarios son mutables e indexables
'''

'''
El diccionario es el unico tipo de mapeo 
(Pero existen otros en la libreria standar)
'''

'''
Los diccionarios se pueden crear colocando una
lista separada por coma de pares <<<key:value>>>
entre {}
'''

dicc = {'nombre':'diego', 'edad': 23}

'''
Aunque tambien podemos usar el constructor dict()
'''

dicc = dict()
print(dicc)

'''
Cuando las claves son cadenas simples, 
podemos especificar los pares usando
argumentos de palabras clave p kwa
'''

dicc = dict(nombre='Diego Figueroa', edad= 23)
print(dicc)

'''
A diferencia de de las secuencias indexadas por
numeros.
Los diccionarios son idezados por keys

Estos keys pueden ser de cualquier tipo INMUTABLE!
Las tuplas pueden ser keys siempre y cuando 
su contenido sean solo valores inmutables
'''

'''
Indexacion
'''
nombre = dicc['nombre']
print(nombre)

'''
Agregacion
'''
dicc['esVaron'] = True
print(dicc)

'''
ELIMINACION!

Como ya vimos en listas, una manera de eliminar
casi general en Python algunos elementos
es usando el operador: del
'''

del dicc['esVaron']
print(dicc)

'''
Para comprobar que una clave esta en un diccionario
se usa el operador: in
'''

print('esVaron' in dicc)

'''
Entre sus metodos, podemos destacar:
- copy() : crea una shallow copy 
- clear() : remueve los elementos
- items() : nos devuelve una lista de tuplas (x, y)
donde x es la clave y Y el valor 
Esta ultima es demasiado util al iterar 
'''

items = dicc.items()
print(items)


'''
Algunas de sus funciones son:
- len()
'''

print(len(dicc))

'''
CONVERSIONES

Para realizar la conversion se usa:

dict()
'''
