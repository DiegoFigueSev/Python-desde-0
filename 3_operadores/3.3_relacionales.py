'''
Los valores booleanos son resultado de 
expresiones que utilizan operadores de relacion
(comparacion entre valores)



NOTA: NO CONFUNDIR CON LOS OPERADORES BOOLEANOS
'''

# Igualdad datos == 
a = 4 == 4 # True
a = 3 != 'hola' # False
# Para tomar en cuenta: 
a = 3 == 3 and 3 != 'hola' # True

# Desigualdad != 
a = 3 != 'hola' # True

# < menor que 
a = 3 < 4 # True

# > mayor que 
a = 3 > 10 # False

# <= menor o igual que 
a = 3 <= 3 # True

# >= mayor o igual que 
a = 2 >= 3 # False


lista1, lista2 = [1, "Lista Python", 23], [11, "Lista Python", 23]
print(lista1 != lista2) # True

a = 3
b = 3
print(a == b)

'''

En los datos mutables, la comparacion aunque 
tengan el mismo contenido, no sera igual.

'''

a = 'hola'
b = 'hola'
print(a == b)