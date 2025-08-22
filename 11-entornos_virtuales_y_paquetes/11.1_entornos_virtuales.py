'''
Las aplicaciones de python usualmente hacen uso de paquetes 
y modulos que no forman parte de la libreria standar.

Las aplicaciones a veces necesitan una version especifica de una libreria
debido a que dicha aplicacion requiere que un bug particular haya
sido solucionado o bien la aplicacion ha sido escrita usando una version
obsoleta

Esto quiere decir que posiblemente para uns instalacion de Python 
no sea posible cumplir con todos los requerimientos.
Cuando instalamos un paquete directamente en consola, lo instalamos 
para toda nuestra maquina. 

Es como si nodeJS estuviera en la raiz de nuestro SO y cuando instalamos un paquete
accedemos a esa raiz. Medio raro

Pero aveces la aplicacion A necesita la version 1.0 de un modulo 
y B necesita la version 0.5. 
Como tenemos el paquete directamente instalado en nuestro environment de python local
no podemos estar manejando ese switch entre versiones, ya que todos comparten la misma instalacion
'''

'''
Entonces cual es la solucion? 

La solucion es el CREAR UN ENTORNO VIRTUAL (venv -> virtualenvironment)
este directorio contiene una instalacion de Python de una version en particualar
ademas de unos cuantos paquetes adicionales.
NOTA: Al crear un venv inicia desde 0, no copia los paquetes que tengamos instalado en nuestro global de python
'''


'''
CREANDO ENTORNOS VIRTUALES

El modulo usado paracrear y administrar los entornos virtuales es:

venv

venv crea un entorno virtual con la version de Python que mencionemos

Para craer un entorno virtual, decide en que carpeta quieres crearlo y ejecuta:

python -m venv tutorial-env
python -m venv [nombre del entorno]

Esto crara el directorio tutorial-env si no existe y tambien creara directorios en el
con una copia del interprete de Python y varios archivos de soporte
'''

# Crea el entorno virutal

'''
Para activar el entorno virtual tenemos que correr el siguiente comando

source [nombre del entorno]/bin/activate

'''

# Activa tu entorno virtual

'''
Activar el entorno virtual cambiara el prompt de la consola
nos mostrara que entorno virtual estamos usando
'''


'''
Para desactivar el entorno virtual tenemos que correr el comando en coonsola:

deactivate

'''


'''
Como tal en el IDE no solo vale cambiar de entorno virtual.

Al mometno de programar podemos tener varios errores de sintaxis 

En VSCode tenemos que cambiar el interprete que vayamos a usar.
Para eso debemos hacer:

1. CTRL + shift + P
2. Python: Select interpreter
3. Seleccionamos nuestro venv 

'''