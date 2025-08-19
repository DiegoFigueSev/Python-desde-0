'''

En Python hay varios tipos de datos COMPUESTOS
y dentro de las secuencias, estan los tipos 
str -> Strings.
Si, un str es un dato compuesto e iterable

Otro tipo muy importante son las listas
Dentro de una lista tenemos una agrupacion 
de valores separados por comas y entre 
corchetes.
Estas listas pueden contener items de 
diferentes tipos

'''

usuario = ['Diego', 'Figueroa', 23, 8032745]

'''

Las listas en Python son: 
- heterogeneas: Pueden estar conformadas 
por elementos distintos; incluso otras listas
- mutables: sus elementos pueden modificarse

'''

'''

A las listas igual se las conoce como 
"Estructura de datos formada por una 
secuencia ordenada de objetos" 

'''

# Las listas son indexeables
nombre_usuario = usuario[0]
apellido_usuario = usuario[1]

print(f'El nombre es {nombre_usuario}')

# Soporta el SLICE
nombre_completo = usuario[:2]
'''
Algo a tomar en cuenta en SLICE es que:
[i:j:k]
el valor i es el inicio -> se lo toma en cuenta
el valor j es el final -> No se lo toma en cuenta
el valor k es la secuencia
'''
print(usuario[-3:3])

# Operaciones sobre listas

# Concatenacion
usuario + [('edad', 23)]
usuario += [3]

# Mutabilidad
usuario[0] = 'Roberto'
print(usuario)

usuario[:2] = ['Daniela', 'Sevillano']
print(usuario)

'''
Cuando asignamos una lista a una variable,
esta variable tiene referencia al punto en memoria 
de dicha lista existente.
Una asignacion simple de datos mutables.
NUNCA COPIA LA DATA
Si no que asignamos a la nueva variable esa
posicion en memoria.

Esto quiere decir que si hacemos cambios sobre
la lista nueva, se vera refledo en la anterior
'''
numeros = [1, 2, 3, 4, 5]
numeros_aux = numeros
numeros_aux[:] = [2,3]
print(numeros) # Resultado: [2, 3]

'''
Para solucionar esto, podemos hacer uso de SLICE
TODAS LAS OPERACIONES DE SLICE retornan una lista 
nueva que contiene los elementos pedidos.

El SLICE hace un shallow copy o una copia 
superficial de la lista original.
'''

numeros = [1,2,3,4,5]
numeros_aux = numeros[:] # Copia de inicio a fin
numeros_aux += [1]
print(numeros_aux)

'''
El SLICE es una operacion potente.
Nos permite hacer operaciones como:
- change
- remove
- clear
'''

letters = ['a', 'b', 'c', 'd']

#change
letters[1:3] = ['B', 'C']
print(letters)

#remove
letters[1:3] = []
print(letters)

#clear
letters[:] = []
print(letters)

'''
UN OPERADOR ULTRA IMPORTANTE ES: *

Este operador se usa para desenpaquetar
los elementos de una lista.
(Similar a hacer [...list] en dart)
'''

list1 = [1,2]
lista2= [*list1, 3, 4] 
# Aunque declaremos la lista 1 dentro de la 2
# No pasara nada si editamos lista 1
# Ya que la lista se crea con los valores
# Al momento de la asignacion
print(lista2)
list1 += [2,2,2]
print(lista2)
# Si no usasemos * tendriamos:
lista2 = [list1, 3, 4]
print(lista2) # [[ , , , ], , , ] lista anidada

'''
FUNCIONES PARA LISTAS:
'''

#append(x) : Agrega un elemento al final
usuario.append(32)

#count(x) : Recibe un elemento y cuenta 
# La cantidad de veces que aparece 
usuario.count('Diego')

#extend([x]) : Extiende una lisat en base a un iterable
usuario.extend((2,3,4,5))
usuario.extend({'diego':32})
print(usuario)

#index(x) : Recibe un elemento y devuelve su primer index
usuario.index('Daniela')

#insert(x,y) : Inserta un elemento x en la posicion y
usuario.insert(2, 3)

#pop() : devuelve el ultimo elemento de la lista y borra dicho elemento
usuario.pop()
# Tambien puede recibir un argumento del index del elemento

#remove(x) : Recibe un elemento x y borra su primera aparicion en la lista
usuario.remove('Daniela')

#reverse() : Invierte el orden de la lista
usuario.reverse()

'''
IMPORTANTE! 

Estos metodos son del tipo None (void para los compas)
QUIERE DECIR QUE NO RETORNARA NADA
editaran la lista na mas
'''

#sort(fx,y)
# fx : funcion para realizar la ordenacion -> boolean
# y : Booleano para invertir el orden
# usuario.sort(key=lambda x : x) 

'''
Para convertir cualquier tipo de dato a lista
se usa list()
'''

nombre = list('Diego')


'''
IMPORTANTE

Para eliminar un valor de la lista no se usa remove
se usa el operador: del

del es superpotente
elimina lo que le mandemos
hasta puede eliminar la variable y su puntero a su seccion en memoria
'''

del usuario[:5]
print(usuario)

del usuario
print(usuario) # error: usuario is not defined