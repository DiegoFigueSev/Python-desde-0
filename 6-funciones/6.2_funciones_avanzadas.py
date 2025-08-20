'''
Python tiene varias funciones avanzadas, entre las cuales estan:
'''

'''
Funcion predicado

Basicamente es una funcion que solo retorna true o false
'''

'''
Funcion anonima

Es una funcion sin nombre. 
El contenido de una funcion anonima debe ser una unica expresion en 
lugar de un bloque de acciones.

Las funciones anonimas se implementan en python mediante expreciones lambda
'''

a = lambda x, y: x + y
print(a(1, 3))

'''
Expresiones lambda

La sintaxis de los lamda es:

lambda [parametros] : [retorno]
donde los parametros son la lista de parametros en cuestion 
y el retorno es la accion que se realizara sobre dicha lista
'''

b = lambda y, *x, t, **z: sum(x) # Igual podemos mandar argumentos arbitarios
print(b(1,2,3,4,t=None, valor=3))
# La definicion de parametros arbitarios son similares al matching
# Se pueden hacer varias definiciones de argumentos con lamdas, queda a curiosidad del dev


