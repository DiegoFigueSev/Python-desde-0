'''
Como vimos en los if, tenemos ciertas expresiones
como in, is, etc.

Estos mas que expresiones, son operadores de pertenencia

A continuacion veremos algunos de estos
'''

'''
OPERADOR DE PERTENENCIA: in / not in

Evalua si se encuentra un objeto en una determinada
coleccion
'''

print('3' in [1,2,3])

print(3 not in [1,2,3])



'''
OPERADORES DE IDENTIDAD: is /is not

Indica si dos variables hacen referencia al mismo objeto
Esto implica si dos variables distintias tienen el mismo id()
'''

a, b = 10, 10.0
print(a is b)
print(a == b)

print(type(2) is int)

print(3 is not 10)


'''
OPERADORES LOGICOS: and; or; not

Recuerdas cuando tocamos el tema de booleanos 
en la seccion 2? mencionamos algunos operadores
booleanos. Pues son estos 

Estos son operadores que trabajan con valores booleanos
llamados tambien operadores logicos o condicionales
'''

# and 
# Valida si el lado izquierdo y derecho son true
print(2 == 2 and 'd' in 'diego')

# or
# valida si algunos de los lados es True
print (2 != 2 or 10 is 10)

# not
# devuelve el valor opuesto al booleanos
# como hacer !true o !false
print(not True)