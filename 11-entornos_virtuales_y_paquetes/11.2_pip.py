'''
Que es pip?

pip es el GESTOR DE PAQUETES de Python (el npm de python)

Nos sirve para:
- Instalar librerias desde PyPi
- Actualizar paquetes
- Desintalar paquetes
- Exportar e importar dependencias con requirements.txt

Nota: PyPi es como un appstore de librerias Python
Pero tambien podemos instalar desde repos privados
'''


'''
Instalar un paquete

pip install [paquete]
'''

# Instala algun paquete, para este ejemplo instalaremos flet

'''
Instalar una version en especifico

pip install [paquete]==[version]
'''


'''
Actualizar un paquete

pip install --upgrade [paquete]
'''


'''
Eliminar un paquete

pip uninstall [*paquete]
'''




'''
IMPORTANTE:

Lo que se suele ahcer es crear un archivo con todos los modulos que 
necesitemos instalar.
Este archivo se llama: requirements.txt

ahi pondremos cosas como lo siguiente:

flet==3.1
novas
numpy
...
...
...

Para instalar los paquetes necesarios podemos usar:

pip install -r requirements.txt
'''