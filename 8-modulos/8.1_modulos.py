'''
Si salimos del interprete de Python y volvemos a entrar
todo lo que hayamos hecho se perdera, variables, funciones, etc

Por lo tanto, si queremos escribir un programa mas o menos largo,
es mejor que utilicemos un editor de texto para preparar la entrada 
para el itnerprete y ejecutarlo con ese archivo


A todo esto se lo conoce como crear un script 

A medida que nuestro programa crece, vamos a querer separarlo
en varios archivos para que el mantenimiento sea mas sencillo
osea vamos a querer modular nuestro codigo.

Para esto Python tiene una manera de poner definiciones en un archivo 
y usarlos en un script o en una instancia del interprete.
Este tipo de ficheros se llama MODULO

Un MODULO es un fichero que contiene definiciones y declaraciones de Python
(todo lo que hicimos son modulos o scripts)
'''


'''
Si nosotros creamos un archivo llamado fibo.py podemos importar 
el modulo con la siguiente linea de codigo: 

import fibo

(tanto en el interprete como en el IDE)
'''

import fibo

fibo.fib(10)

fibo.moduleName()

'''
Cuando importamos fibo a nuestro modulo, no añadimos el nombre de sus 
funciones al actual namesapce. Solo añadimos el nombre del modulo fibo

Usando el nombre podemos acceder a sus funciones.

Como lo vimos haciendo fibo.x()
'''

'''
Si pretendemos usar la funcion frecuentemente, podemos aisgnarla 
a un nombre local:
'''

fib = fibo.fib
fib(10)

'--------------------------------------------------------'

'''
Un modulo puede contener tanto declaraciones ejecutables
como definiciones de funciones.

Estas declaraciones estan pensadas para inicializar el modulo.

Se ejecutan unicamente la primera vez que el modulo se encuentra 
en una declaracion de import
'''

'''
Cada modulo tiene su propio espacio de nombres privado, que es 
utilizado como espacio de nombres global por todas las funciones 
definidas en el modulo
De esta forma, el autor puede utilizar variables globales en el modulo
sin procuparse por choques accidentales con las variables globales
'''

'''
Los modulos que importamos, pueden importar otros modulos
'''



'''
Hay algunas variantes de declaraciones import, que importa los nombres
del namespace de un modulo directamente al espacio de nombres
del modulo donde se hace la importacion
'''

from fibo import moduleName

moduleName()

'''
Lo que hicimos fue del(from) modulo <fibo> traer(import) 
la funcion moduleName.


Lo que hacemos como tal es unicamente importar la funcion.
No definimos fibo al spacename
'''

# Se lo puede hacer de otra forma
from fibo import *
# Pero no es recomendado
# Este importa todas las declaraciones, excepto las que comienzan con _
# Esas se las conoce como privadas

'''
Si el nombre del modulo es seguido por as, el nombre que hayamos 
definido despues de as queda ligado directamente al modulo o declaracion
importada
'''

import fibo as fibonacci
from fibo import moduleName as nombreDelFichero

nombreDelFichero()

'''
Basicamente estamos importando el elemento a nuestro modulo, pero 
cambiandole el nombre dentro del namespace global del modulo
'''

'''
Tambien podemos importar modulo como scripts
eso lo vimos en la seccion 7: Entrada y salida
'''

'''
Un modulo NUNCA ejecutara su codigo al momento de importarlo,
ni en otro modulo, ni en el interprete.

Para que se ejecute en el interprete debe ser __main__
'''



''''
Cuando usted importa un módulo, el interprete Python busca por el módulo en la secuencia siguiente:

El directorio actual.

Si el módulo no es encontrado, Python entonces busca en cada directorio en la variable de 
entorno PYTHONPATH del sistema operativo.

Si todas las anteriores fallan, Python busca la ruta predeterminada. 
En UNIX/Linux, la ruta predeterminada normalmente esta /usr/local/lib/python/.

El ruta de búsqueda de módulo es almacenado en el módulo de system sys como 
la variable sys.path. La variable sys.path contiene el directorio actual, PYTHONPATH, 
y las predeterminadas dependencia de instalación.
'''





'''
INFORMACION EXTRA:


La primera vez que un modulo es importado en un script de Python.
Se ejecuta su codigo una sola vez.

Si otro modulo importa el mismo modulo, este no se volvera a cargar.

Esto se debe al codigo objeto compilado, que genera en el mismo directorio del modulo



Este codigo compilado, se encuentra en __pycache__ dentro del directorio donde tengamos nuestro codigo
este __pycache__ contiene el codigo de los modulos YA EJECUTADOS
los mismo se guardan con una version: fibo.cpython-313.pyc
Si hacemos ediciones en el archivo compilado, Python lo que hace es
verificar si la version del archivo o su fecha de edicion varia al archivo original
si es asi lo vuelve a compilar y ejecutar, si no, usa la version compilada.

'''

a = 10
def f():
    global a 
    a = 15
print(a)