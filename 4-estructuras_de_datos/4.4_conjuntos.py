'''
Los tipos conjunto, pueden ser:
- conjunto mutable (set)
- conjunto inmutable (frozenset)

Aunque suempre son mutables.

OJO: UN SET NO ES INDEXEABLE
'''

'''
Los conjuntos es una coleccion, ordenada
de elementos QUE NO SE REPITEN
'''

'''
Sus usos basicos son la verificacion de pertenencia
y la eliminacion de entradas duplicadas
'''

'''
Para crear un conjunto se usa la funcion: set()
Pero tambien podemos hacerlo con llaves {}

OJO: Para crear un conjunto vacio, debemos usar
si o si su constructor
'''

conjunto_a = {1, 2, 3, 4, 5}
conjunto_b = {3, 4, 6, 7, 8}

# No existe algo como conjunto_a[0] !!!! 

'''
Para tener un mejor entendimiento de conjuntos
pensemos en algebra basica, logica.
Es lo mismo, los circulos, etc.

Las operaciones que soporta los conjuntos son:
- union
- interseccion
- diferencia
- etc
'''

print(conjunto_a)
print(conjunto_b)

# LOGICA DE CONJUNTOS

# Pertenece a A pero no a B 
print(conjunto_a - conjunto_b)
# Pertenece a B pero no a A
print(conjunto_b - conjunto_a) 

# Union : |
print(conjunto_a | conjunto_b)

# Interseccion : &
print(conjunto_a & conjunto_b)

# Pertenece a A y B pero no a ambos
print(conjunto_a ^ conjunto_b)


'''
Algunos metodos de conjuntos son:
'''

# add(x)
conjunto_a.add(10)

# clear() : remueve todos 

# copy()

# discard() : elimina un elemento 
conjunto_a.discard(10)


'''
Todo tipo de iterador que le pasemos a un set
pasara los elementos 1x1
'''

texto = 'diego'
conjunto = set(texto)
print(conjunto)


'''
CONVERSION
'''

conjunto = set([1, 2, 'diego'])
print(conjunto)

# Para hacer un frozen set debemos de hacerlo unicamente 
# con objetos inmutables
conjunto = frozenset([1,2,3,(1,2)])
print(conjunto)