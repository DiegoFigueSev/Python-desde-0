'''
La sentencia conficional: if
se usa para tomar decisiones, este evalua basicamente 
una operacion logica.
Es decir, una expresion que de como resultado true o false
'''

numero = 10

if numero > 0:
    print('el numero es mayor a 0')
    
'''
Sentencia if

if EXPRESSION, significa que si cumple la expresion,
ejecuta el bloque de sentencia seguido
'''

if numero > 5:
    print('El numero es mayor a 5')
    
'''
Setencia: elif

elif EXPRESSION, significa, de lo contrario Si se cumple 
ejecuta el bloque de codigo
'''

if numero < 0:
    print('Error')
elif (numero > 0):
    print('El numero es mayor a 0')
    
'''
Sentencia: else

else EXPRESSION, significa, de lo contrario.
'''

if numero < 0:
    print('NUmero es menor a 0')
else:
    print('Numero es mayor a 0')
    
    
'''
EXPRESIONES CONDICIONALES! 
'''

# Expresion: if -> se evalua a false cuando hace:
# numero igual a cero: 0, 0.0
# Coleccion vacia: lista, tupla, diccionario
# False, None
# De lo contrario cualquier cosa diferente sera true
if 3:
    pass

# Expresion: == 
# Se usa para validar igualdad

if 3 == 3:
    print('3 es igual a 3')
    
# Expresion: != 
# Se usa para validar desigualdad

if 2 != 3:
    print('1 es diferente de 3')

# Expresion: in
# Se usa para validar la pertenencia de un elemento
# dentro de un iterable
if 'i' in 'Diego':
    print('i esta dentro de Diego')

# Expresion is
# Se usa para validar un elemento con un tipo de dato

if numero is int:
    print('Es un entero')
    
    
# Expresiones: <, >, <=, >= 
# Se usa para validar mayor que menor que
if 3 <= 3:
    print('El numero es igual o menor que 3')
