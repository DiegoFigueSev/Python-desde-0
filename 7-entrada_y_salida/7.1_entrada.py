'''
Los programas serian de muy poca utilidad si no fueran capaces 
de interaccionar con el usuario
'''

'''
ENTRADA
'''

'''
Entrada standar.

Para pedir informacion al usuario, se debe utilizar funciones 
integradas en el interprete del lenguaje.

Esto se lo hace con la funcion: input()
'''

edad = input('Que edad tiene?: ')
print(edad)


'''
Entrada por script con argumentos

Podemos enviar informacion a un script y manejarla
Para esto utilizamos la libreria de sistema: sys.
En ella encontraremos la lista de argv, que almacenan
los argumentos enviados al script 
'''

import sys
print(sys.argv)
'''
Cuando lo ejecutamos, podemos ver que nos regresa una lista con 
una cadena que contiene el nombre del script. 
Entonces el primer argumento del script, es su nombre.
'''

'''
Sin embargo si mandamos mas informacion al script como:

python3.13 [script] 3, 23

obtenemos que recupero los argumentos pero los transformo a str

Otro ejemplo es el siguiente:
'''

if len(sys.argv) > 1:
    print(int(sys.argv[1]) + int(sys.argv[2]))

print('3' + '3')

