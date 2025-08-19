'''
Las tuplas son un objeto del tipo secuencia.

Basicamente son listas INMUTABLES.
Pueden ser indexadas pero sus elementos no 
pueden modificarse.
'''

tupla = (2,3);

# Pueden anidarse 
tupla = (2,3, (3,3))
print(tupla)

# Son inmutables, pero pueden contener valores
# mutables

tupla = (2, 3, [1,2])
print(tupla)
tupla[2].append(3)
print(tupla)

'''
Normalmente las tuplas contienen una secuencia
HETEROGENEA de elementos que son accedidos al 
desenpaquetar o indexar
'''

'''
Un problema en tuplas, durante su construccion,
es cuando contienen 0 o 1 item

- Las tuplas vacias se construyen mediante
un par de parentesis vacios

- Las tuplas con un item se construyen con el 
mismo par de parentesis pero con una coma a 
continuacion del valor 
FEO PERO EFECTIVO
'''

tupla_vacia = ()
print(type(tupla_vacia))

tupla_u = (1,)
print(type(tupla_u))

'''
EMPAQUETADO Y DES-ENPAQUETADO

Similar a JS
Podemos empaquetar valores en tuplas y desen
paquetarlas de la siguiente forma:
'''

enpaquetado = 1, 2, 'esta es una tupla'
print(enpaquetado)

x, y, z = enpaquetado
print(f'{x=}, {y=}, {z=}')

# Desenpaquetando nested tuples
t = 1, 2, 3, ('hola', 'adios')
x, y, z, (a, b) = t
print(a)

'''
CONVERSION

Para realizar la conversion, usamos la funcion:
- tuple()
'''
lista = [1,2,3,4]
tupla = tuple(lista)
print(tupla)


'''
EJEMPLO
'''

print("Definiendo conexión a BD MySQL")
print("==============================\n")

conexion_bd = (
    "127.0.0.1",
    "root",
    "qwerty",
    "nomina",
)
print(f"Conexión típica: {conexion_bd}, {type(conexion_bd)}")

conexion_completa = (
    conexion_bd,
    "3307",
    "10",
)
print(
    f"\nConexión con parámetros adicionales: {conexion_completa}, {type(conexion_completa)}\n",
)

print(f"IP de la BD: {conexion_completa[0][0]}")
print(f"Usuario de la BD: {conexion_completa[0][1]}")
print(f"Contraseña de la BD: {conexion_completa[0][2]}")
print(f"Nombre de la BD: {conexion_completa[0][3]}")
print(f"Puerto de conexión: {conexion_completa[1]}")
print(f"Tiempo de espera en conexión: {conexion_completa[2]}")

print(
    """\nMás información acerca de MySQL y Python \
https://pymysql.readthedocs.io/en/latest/"""
)