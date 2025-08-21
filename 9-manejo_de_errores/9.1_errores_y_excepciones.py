'''
Hasta ahora los mensajes de error no habian sido mas que mencionados

Hay almenos dos tipos diferentes de errores:
- Errores de sintaxis 
- Excepciones
'''

'''
ERRORES DE SINTAXIS : SyntaxError

Los errores de sintaxis, son el tipo mas comun de error.
Estos ocurren cuando el parser encuentra codigo invalido
por ej: falta :, etc
'''


'''
EXEPCIONES 

Cuando la sintaxis es correcta, podemos encontrar errores
en tiempo de ejecucion, estos errores se llaman EXCEPCIONES.

La mayoria de excepciones no son gestionadas y bloquearan nuestro programa
'''



'''
GESTION DE EXCEPCIONES 

ES posible escribir programas que gestionene determiandas excepciones

Para hacer ello utilizaremos la sentencia: try
'''

while True:
    try:
        x = int(input('Please enter a number: '))
        break
    except ValueError:
        print('NO INGERSASTE UN NUMERO VALIDO')
    except KeyboardInterrupt:
        print('No ingresaste ningun numero')

'''
La sentencia try funciona de la siguiente manera: 

- Primero se ejecuta la clausula try <block dentro de try>
- Si no ocurre ningun tipo de excepcion la clausula de omite
- Si ocurre alguna excepcion durante la ejecucion del bloque de codigo try
se omite el resto de la clausula. Luego si su tipo coincide con la excepcion nombrada (como un match)
se ejecuta la clausula o el <block> de ese except y luego la ejecucion continua.
- Si una excepcion ocurre y no tiene ningun match con alguno de los errores que manejamos
esta se convierte a un <Unhandled exception> o excepcion no manejada
'''


'''
Como vimos la clausula try puede tener varias clausulas except continuas

Una clausula except puede nombrar multiples excpeciones
'''

try:
    a = '10' + 3 # TypeError
except ValueError:
    pass
except (KeyError, TypeError):
    pass


'''
La clausula except peude especificar una variable despues del nombre de la excpecion
La variable esta ligada a la instancia de la excepcion que 
normalmente tiene atributos args que almacenan los argumentos
pro conveniencia, los tips de excepcion incorporados definen __str__() 
para imrpimir todos los argumentos sin acceder explicitamente a args
'''

try:
    raise Exception('spam', 'eggs')
except Exception as inst:
    print(type(inst))
    print(inst.args)
    print(inst)
    
'''
lo que hace <raise> es lanzar un error, como throw en dart
'''

'''
BaseException es la clase comun para todas las excepciones.

Una de sus subclases es Excepcion que es la clase base de todas las 
excepciones no fatales, estas son las que se manejan o gestionan.

El resto de excepciones recomiendadn terminar el programa

Excepcion se puede utilizar como un COMODIN cuando no sabemos 
que exepciones mas podemos gestionar.

El patron mas comun es registrar la excepcion y luego vovler a re lanzarla
'''

try:
    with open('hola.txt') as f:
        f.readline()
except OSError as err:
    print(err)
except ValueError:
    print('el error es un error de valor')
except Exception as err:
    print(f'error inesperado: {err=}')
    raise

print('continua')


'''
Las declaraciones try...except pueden tener una clausula else
Cuando esta esta presente, significa que debe seguir todas las clausas except

Esta es util para el codigo que debe ejecutarse si la clausula try no lanza una excepcion
'''

import sys

for arg in sys.argv[1:]:
    try:
        f = open(arg, 'r') # Abrimos un archivo
    except OSError:
        print('cannot open', arg)
    else: # Si no encuentra ninguna excepcion gestionada se ejecuta:
        print(arg, 'has', len(f.readlines()), 'lines')
        f.close()
        
    

'''
Exepciones definidas por el usuario

Los programas pueden nombrar sus propias excepciones creando una 
nueva clase excepcion. Estas derivan de la clase Exepcion

'''

class MyException(Exception('Exepcion propia')):
    pass

'''
Accion de limpieza : finally

Si la clausula finally esta presente, el bloque finally se ejecutara
antes de que todo el bloque try se complete.

A diferencia de else, el bloque finally se ejecuta siemrpe habiendo o no excepcion
- Si ocurre una excepcion durante try, y ninguna clausula except es gestionada
ejecuta el bloque finally y luego lanza la excepcion
- Si la clausula finally ejecuta un break, continue o return no lanza las excepciones
- Si try tiene alguna clausula try, break o return, ejecuta finally antes de esas
'''

def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("division by zero!")
    else:
        print("result is", result)
    finally:
        print("executing finally clause")

divide(2, 1)

divide(2, 0)

# divide("2", "1") -> Lanza un error

'''
Basicamente si hay un except gestionado lo ejecuta y luego limpia
Si hay un else lo ejecuta y luego limpia
Si hay un excepcion NO gestionado ejecuta la limpieza y luego la excepcion
'''


'''
IMPORTANTE!

Algunos objetos ya definen acciones de limpieza estandar en sus funciones
para llevar a cabo cuando el objeto ya no es necesario.

Para llamar a estas acciones de limpieza podemos usar la declaracion with
esta permite que los objetos que tengan esta limpieza, realice dicha la limpieza automaticamente 
cuando ya no son usados
'''
try:
    with open('myfile') as f:
        print(f)
except Exception as err:
    print(err)
    
'''
Podemos enriquecer las excepciones con notas:

'''

try:
    with open('myfile') as f:
        print(f)
except Exception as err:
    err.add_note('Este es n error al intentar abrir el archivo')
    raise

'''
Como nota adicional, podemos manejar igual multiples expceiones

para esto podemos desenpaquetarlo usando except*
'''