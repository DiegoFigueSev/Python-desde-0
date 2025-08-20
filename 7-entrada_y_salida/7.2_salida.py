'''
La forma general de mostrar informacion por pantalla es 
mediante una consola de comando.

Para esto usamos: print
'''

print('salida standar')

'''
Podemos utilizar print con un formateo de impresion basico
que nos permite aternar entre texto y variables.

Este modo de texto es llamada f-strings
'''

print(f'la suma de 2 + 2 es: {2 + 2}')


'''
Hay otras formas de formateo mucho mas robustas, como es el metodo
format() dentro de los str
'''

'''
En estos podemos definir campos {} como en f-string, pero estos pueden ser
posicionales o con nombre.

ESte tipo de format() es util para tablas alineadas, etc
'''

for x in range(6):
    print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))

'''
La sintaxis:

{[n]:[m]}

Simboliza:
n -> Es el elemento a imprimir
m -> Es el formateo elegante que se le da

m muchas veces se lo usa para centrar, el texto en base a un ancho dado
'''

yes_votes = 42_572_654
total_votes = 85_705_149
percentage = yes_votes / total_votes
print('{:-9} YES votes  {:2.2%}'.format(yes_votes, percentage))


'''
Una chuleta para tomar en cuenta estos formados y los valores
que puede tener m es:
'''

'''
cuando [n] es un numero

- :.3f → flotante **punto fijo** con 3 decimales.
- :.3e → **notación científica** con 3 decimales.
- :.3g → **3 cifras significativas**.
- :d / :x / :X / :b → entero decimal / hex / HEX / binario.
- :% → porcentaje (multiplica por 100 y añade `%`).
'''

import math
print(f"{math.pi:.3f}")  # '3.142'
print(f"{math.pi:.3e}")   # '3.142e+00'
print(f"{255:#x}")      # '0xff'
print(f"{0.256:%}")       # '25.600000%'

'''
para alinear el contenido

- Alineación: `>`, `<`, `^` (derecha/izquierda/centro).
- Ancho mínimo: `:10` (reserva 10 cols).
- Relleno con carácter: `:*^10` (centra y rellena con *).
'''

print(f"{'hi':>6}")    # '    hi'
print(f"{'hell':*^6}")   # '**hi**'


'''
TODOS ESTOS FORMATEOS SE PUEDEN USAR TANTO EN F-STRING COMO EN FORMAT()
'''