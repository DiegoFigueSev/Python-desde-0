'''

Que es una variable? 
r. Una variable es un espacio en memoria 
donde almacenamos informacion

Cuando creamos una variable esta en automatico 
tiene un valor hexadecimal, este valor
es la direccion en memoria al contenido de esa 
variable (a su valor)

Estas variables pueden dividirse en:
- locales 
- globales
- Enclosing
- Builtins 

Python resuelve el nombre de las variables, en el
siguiente orden:
- Local: Verifica el nombre la variable dentro
de la funcion o comprension
- Enclosing: Verifica el nombre de la variable
en la funcion padre (Osea cuando tenemos fun-
ciones anidadas)
- Global: Nombres definidos en el archivo .py
- Builtins: Nombres precargados, como: len, print
range, Exception. Ultimo lugar donde lo busca

NOTA: Bloques como if/for/while/try no crean 
un scope nuevo

'''

# Creacion de una variable
a = 1
a = int

b = float

print(b)

# Como tal python no tiene soporte a constantes
# Pero estas se las definen en mayusculas 
# Investigar mas sobre PEP8
CONSTANTE = 'constante'

'''

Siguiente el PEP8
Las recomendaciones para escribir variables son:
- Hacerlo en snake case : mi_variable

'''

# Una variable privada es asi: 

_privada = 3

