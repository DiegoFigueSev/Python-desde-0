'''
Los paquetes en Python no son mas que carpetas que contienen 
otros modulos y otros paquetes.

El unico requisito para que python reconozca un paquete es 
crear un archivo llamado __init__.py dentro de el. 
Este archivo puede estar vacio.


Los paquetes como tal son una forma de estructurar el espacio
de nombres de modulos de Python usando <nombres con punto>
por ejemplo tengo:
math
--operations
----fibo.py

Al importarlo desde la raiz haria:
import math.operations.fibo (nomres con punto)

Asi nos salvamos de tener que preocuperanos por los nombres
de las variables globales de un modulo. 
'''

# Por ejemplo importemos nuestro modulo utils
import paquete.utils.example # Podemos importar modulos individuales de un apquete

paquete.utils.example.fun()


# Otra alternativa es:
from paquete.utils import example_2 as utils # O tambien un paquete
# Podemos importar al namespace el submodulo example_2 y lo podemos 
# usar sin escribir todo el prefijo

utils.f()


'''
Que pasa si queremos usar * en el import de un paquete ? 
Pues que tendriamos muchos errores. 

Para evitar esto teneos el archivo __init__.py 
Dentro de este podemos realizar algunas delcaraciones como ser:

__all__ = [<todos los modulos>]

Cuando lo usamos vamos a nosotros definir, que modulos se van a 
importar cuando llamemos al operador * 
Podemos dejarlo vacio
'''

from paquete.utils import *

example_2.f()


'''
Hay que tener en cuenta que los submodulos pueden quedar ocultos 
por nombres definidos localmente
'''



'''
Podemos tambien tener tambien imports absolutos, para asi evitar 
algunos errores
'''

from . import echo
from .. import formats
'etc'