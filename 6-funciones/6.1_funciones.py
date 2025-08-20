'''
Una funcion no es mas que un bloque de codigo asociado, que
recibe cero o mas argumentos como entrada, sigue una secuencia
de sentencias, las cuales ejecutan una operacion deseada
y devuelve un valor y/o realiza un procedimiento
'''

'''
El uso de funciones es un componente muy importante, para el 
paradigma de pogramacion ESTRUCTURADA.
Ya que nos permite: 
- Modularizar: Permite segmentar un programae n una serie de partes
- Reutilizacion: Permite reutilizar una misma funcion en varios lugares
'''

'''
La estructura de una funcion es la siguiente:

def NOMBRE(LISTA_DE_PARAMETROS):
    """DOCSTRING_DE_FUNCION"""
    SENTENCIAS
    return [EXPRESION]

- NOMBRE, es el nombre de la función.
- LISTA_DE_PARAMETROS, es la lista de parámetros que puede recibir una función.
- DOCSTRING_DE_FUNCION, es la cadena de caracteres usada para documentar la función.
- SENTENCIAS, es el bloque de sentencias en código fuente Python que realizar cierta operación dada.
- return, es la sentencia return en código Python.
- EXPRESION, es la expresión o variable que devuelve la sentencia return.

La sentencia def, es una definicion de funcion usada para crear
objetos del tipo funcion que son definidas por el usuario

Una definicion de funcion es una sentencia ejecutable.
Su ejecucion enlaza el nombre de la funcion en el 
NAMESPACE LOCAL ACTUAL (osea un envoltorio alrededor del codigo ejecutable)
El objeto FUNCION tiene una referencia al NAMESPACE LOCAL GLOBAL
'''

'''
A que nos referimos con namespace, etc? 
En otras palabras, al ejecutar una funcion estamos introduciendo
una nueva tabla de simbolos usada para las variables locales
Cuales son estas variables locales, las definidas dentro de cualqueir funcion

LOCAL -> Dentro de la funcion/clase

Estas referencias a variables hace la siguiente validacion:
- Primero mira la tabla local
- Luego la tabla local de funciones externas 
- Luego la tabla global
- Finalmente los buildint o nombres predefinidos
(Creo que ya hablamos de esto en otro punto pasado)
'''

a = 'Variable Global'
def example():
    """Funcion de ejemplo"""
    a = 'Variable Local'
    print(a)
example()
print(a)

'''
Como vimos en el anterior ejemplo, el definir una variable a dentro de
la funcion, no sobreescribe a la variable a global, en cambio 
introduce esta nueva a a la tabla local. Es por ello que al ejecutar 
la funcion e imprimir a fuera de la funcion no vemos cambio.
'''

'''
los arg que pasamos a una funcion, igual se introducen a la tabla 
de simbolos local. 
Por lo tanto los argumentos se pasan usando llamada por valor
(donde el valor es una referencia a un objeto)
'''

'''
En python, podemos objetar que la funcion example(), mas que 
una funcion, es un procedimiento (Esto porque no retorna nada, void para los compas)

Pero no es asi, todas las funciones retornan un valor, si no es
explicitamente, de forma implicita retorna NONE (void)
'''

# None seria nuestro void y nuestro null
print(example()) #None



'''
PARAMETROS Y ARGUMENTOS


Al definir una funcion, los valores que se reciben son parametros
Pero, durante la llamada los valores se denominan argumentos

Podemos tener diferentes tipos de parametros y argumentos
'''

# Argumentos por omision / Argumentos por defecto
# Podemos definir argumentos por defecto al definir la funcion
def printHello(msg = 'Hola mundo'):
    print(msg)
printHello()
# Los valores por omision son evaluados al momento de la definicion
# de la funcion. Entonces:
i = 10
def f(arg=i):
    print(arg)
i = 1
f() # Retorna 10 -> Porque? por lo mismo señalado arriba

# El valor por omision es evaluado una unica vez, pero existe
# diferencia cuando el objeto es mutable

# Los objetos mutables como argumentos son compartidos en 
# las subsiguientes llamadas por la manera en como se almacenan
# las variables locales
def f(a, L=[]):
    L.append(a)
    return L
print(f(1))
print(f(2))
print(f(3))
print(f(4))


# Argumentos por posicion
# Cuando enviamos los argumentos, si se reciben por orden en los 
# parametros definidos, singnifica que son por posicion

# Basicamente es por posicion, porque dependemos de la posicion
def resta(a, b):
    return a - b
print(resta(10 , 5)) # 5
print(resta(5 , 10)) # -5
# El resultado de la resta dependera de la posicion en la que mandems
# los argumentos.


# Argumentos por nombre / argumentos por palabra clave / keyboard argument
# Es posible evadir el orden de los parametros si indicamos durante la llamada
# el valor que tiene caa parametro a partir de su nombre
resta(b=5, a=10)
print(resta(b=5, a=10)) # 5
print(resta(a=10, b=5)) # 5
# Aqui el resultado ya no depende de la posicion, indicamos el valor del argumento directamente
'OJO: LOS ARGUMENTOS POR NOMBRE SIEMPRE DEBEN DE ESTAR DESPUES DE LOS POSICIONALES NO ANTES!!!!'


# Llamada sin argumentos 
# Si mandamos una funcion sin argumentos cuando los espera
# tendremos un error, pero podemos solucionarlo de la siguiente forma
def resta(a=None, b=None):
    if not (a and b): # Recordemos que None siempre regresa False
        print('Los argumentos no son validos')
    else:
        return a - b
resta(b=10)

'''
Una funcion igual puede tener multiples returns.

En si retorna una tupla, no nos iremos por las ramas
'''

def f():
    return 1, 2, 'hola'
a, b, c = f()
print(f'{a=}, {b=}, {c=}')



'''
PARAMETROS ESPECIALES

Como vimos podemos enviar argumentos posicionales, 
por palabra clave o hasta por omision, pero dejar esto al aire
para que el desarrollador lo use a su manera, puede dar lugar
a errores. 
Es por ello que Python ofrece parametros especiales, los cuales
nos ayudaran a definir que parametros son posicionales, que parametros son
standar (tanto posicional como por palabra clave) y que son unicamente por 
palabra clave

La estructura es la siguiente:

def f(pos1, pos2, /, pos_or_kwd, *, kwd1, kwd2):

Los parametros / y * son posicionales.
Estos parametros especiales nos ayudaran a definir las reglas de 
los argumentos

Tomar en cuenta lo siguiente:
- Todo lo que este ANTES de / ES POSICIONAL
- Todo lo que este  DESPUES de * ES POR PALABRA CLAVE
- Todo lo que este despues de / y antes de * ES STANDARD
'''

# EJEMPLO
def standard_arg(arg):
    print(arg)

standard_arg(10)
standard_arg(arg = 10)
#PERMITE AMBOS CASOS

def pos_only_arg(arg, /):
    print(arg)
pos_only_arg(1) # PERMITE UNICAMENTE ESTA LLAMADA

def kwd_only_arg(*, arg):
    print(arg)
kwd_only_arg(arg = 10) # PERMITE UNICAMENTE ESTA LLAMADA

def combined_args(pos_only, /, standard, *, kwd_only):
    print(f'{pos_only=} - {standard=} - {kwd_only=}')
combined_args(3, 'hola', kwd_only=(3,2))
combined_args(3, standard='hola', kwd_only=(3,2))



'''
ARGUMENTOS INDETERMINADOS

En algunas ocasiones nosotros no sabremos previamente cuandos elementos
necesitamos enviar a una funcion. 
En dicho caso podemos utilizar parametros indeterminados por posicion y/o nombre
'''


# Por posicion
# Debemos crear una lista dinamica de argumentos, es decir,
# una tupla, lo logramos definiendo un parametro de la forma formal *

def indeterminados_posicion(*args):
    for arg in args:
        print(arg, end=', ')
    print()
        
indeterminados_posicion(1, 2, 3, 4, 'hola')

# Como vimos, los argumentos que pasamos estan organizados dentro de una tupla
# Antes del numero de argumetnos cariable, podemos tener cero o mas argumentos
# normales.
# OJO!: DESPUES DE USAR *args, TODOS LOS ARGUMENTOS RESTANTES DEBEN SER KWD

def concat(*args, sep="/"):
    return sep.join(args)
 
print(concat("earth", "mars", "venus", sep="."))



# Por nombre clave
# Para recibir un numero arbitrario de parametros por nombre (clave-valor)
# debemos crear un diccionario dinamico de argumentos, definiendo el parametro de la forma formal **

def indeterminados_nombre(**kwargs):
    print(kwargs)
    
indeterminados_nombre(nombre='diego', edad=23) # Similar al constructor de diccionarios dict()
# OJO: NO EXISTEN MAS PARAMETROS DESPUES DE **KWARGS, ESTE ES EL RESIDUO

# Al recibirlo como un diciconario podemos iterearlo segun clave y valor
def indeterminados_nombre(**kwargs):
    for k, v in kwargs.items():
        print(f'{k=}, {v=}')
indeterminados_nombre(diego=32, jose=34)



'''
EJEMPLO PRACTICO
'''

# Podemos tener una colision si hacemos 
# def foo(name, **kwds):
#   return 'name' in kwds
# Si hacemos una llamada a la funcion tendremos un error 
# Esto porque definimos a name como un argumento standar, puede ser posicional
# o tambien como palabra clave

# Si nosotros enviamos foo(1, name=2)
# No saltara un error porque tenemos name y name (porque el parametro name se lo peude tomar como nombre igual)

# Para eso la solucion es la siguiente:
def foo(name, /, **kwdards):
    return 'name' in kwdards

print(foo(1, name='Diego'))


'''
DESENPAQUETANDO LOS ARGUMENTOS 

Podemos tener una situacion inversa, cuando tenemos la lista de argumetnos
pre establecida antes de la funcion pero estas necesitan ser desenpaquetadas para llamar 
a la funcion que requiere los argumentos posicionales separados
'''

# Para este ejemplo usaremos range, que requiere dos numeros de inico y final
rangos = [1, 5]
print(list(range(*rangos)))

'''
del mismo modo podemos desenpaquetar un diccionario
'''

def f(*, nombre, edad, peso):
    print(f'{nombre=}, {edad=}, {peso=}')
args = dict(nombre='Diego', edad=34, peso=10)
f(**args)

'''
Basicamente lo unico que hacemos es desenpaquetar la los argumentos de
la lista o diccionario y pasarle a la funcion como tal
'''




'''
SENTENCIAS

Las funciones pueden manear 2 sentencias:
- pass : No hace nada, es como un None, pero no hace absolutamente nada
se lo usa cuando el metodo esta Unimplemented
- return : Se lo usa para retornar algun valor
(talves hay mas pero ni idea)
'''

def f(a, b):
    pass

f(1,2)
