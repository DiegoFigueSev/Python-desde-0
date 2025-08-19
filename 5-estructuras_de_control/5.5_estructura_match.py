'''
Python nos ofrece algo similar al switch en otros lenguajes

Este es llamado: match
donde cada case define un camino posible. EL _ es la opcion
default que se ejecuta si la entrada no coincide con ningun caso
'''

hora = 8

match hora:
    case 8:
        print('Desayuno')
    case 14:
        print('comida')
    case _:
        print('default')
        
'''
El match nos permite realizar lo mismo que con multiples 
if elif elif else 
En si ambos codigos son mas equivalentes

(pero el match llega a ser mas rapido y mas legible)
Lo recomendado es que si llegasemos a tener multiples if
no concatenarlos si no, usar match

Solo se ejecutara el primer patron coincidente, el resto no
'''

'''
Tambien podemos tener en nuestros case  multiples condiciones
donde | es interpretado como un or
'''

mes = 4 
match mes: 
    case 12 | 1 | 2: print('invierno')
    case 3 | 4 | 2: print('No se')
    case _: print('Ninguno')
    
    
'''
Aunque no acabe ahi.
Podemos hacer un matching de cualquier objeto, como tuplas, listas, etc
De hecho el match es muy poderoso, similar a programacion funcional
podemos hacer:
- pattern matching
- guards
'''

point = 3, 1

match point: 
    case (0, 0): print('Origen')
    case (0, y): print(f'{y=}')
    case (x, 0): print(f'{x=}')
    case (x, y): print(f'{x=}, {y=}')
    
'''
Como vimos podemos hacer matcheos pesados como el anterior visto

En algunos casos, estamos combinando un literal con una VARIABLE

La variable liga uno de los elementos del sujeto point.
'''

lista = [2, 2, 3, 4, 5]

match lista:
    case [1, 2, *xs] if len(xs) != 10: print(xs)
    case [*xs, 5]: print(xs)
    case []: print('vacio')
    case _: print('nada')

'''
Como vimos podemos hasta usar condicionales dentro de un match
podemos verificar el contenido inicial y el resto obtenerlo,
etc.
Podemos hacer combinaciones local y muy interesante


El ejemplo anterior resulta muy practico aplciarlo para programacion
dinamica o funcional
'''

'''
Podemos aplicar matchs similares al anterior incluso con clases 
creadas por nosotros mismos
'''