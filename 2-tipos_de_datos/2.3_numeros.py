'''

Los tipos de datos numero son:
- int 
- float
- decimal
- fraction
- long

Python tambien tiene soporte para los
COMPLEX NUMBER
Donde se usa j o J para la parte imaginaria
por ejem: 3 + 5j

'''


# int
entero = 3

# float
flotante = 3.1
flotante = 0.1e-3 # Notacion cientifica : 0.1x10-3

# decimal
decimal = 3.3333

# long
## long = 027 # Octal
long = 0x32 # Hexadecimal

# complejos
complex = 2.1 + 7.8j

# fraccion
from fractions import Fraction
fraction = Fraction(16, -10)

# decimal
from decimal import *
decimal = Decimal(1) / Decimal(7)
print(decimal)
