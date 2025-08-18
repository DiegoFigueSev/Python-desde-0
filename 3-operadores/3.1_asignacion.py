'''
Los operadores de asignacion nos permiten
asignar un valor a una variable
'''

# Operador = 
# Es el mas simple de todos 
a = 100

# Operador += 
# Suma a la variable 
a += 5
print(a)
a = 'hola'
a += 'mundo'
print(a)

# Operador -= 
a = 10
a -= 5
print(a)

# Operador *=
a = 'tun'
a *= 3
print(a)

# Operador /= 
a = 10
a /= 5
print(a)

# Operador **=
a = 10
a **= 2
print(a)

# Operador //=
a = 5
a //= 10
print(a)

# Operador %=
a = 5
a %= 10
print(a)

# Asignacion multiple
a, b, c = 10, 'hola', False
print(f'{a}, {b}, {c}')