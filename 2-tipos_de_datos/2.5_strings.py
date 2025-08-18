'''
str
Para definir un string simplemente o:
- encerramos la palabra en " _ "
- encerramos la palabra en ' _ '

'''

texto = 'hola mundo'
texto = "adios mundo"

'''

LAS CADENAS SON INMUTABLES
(revisar la jerarquita_de_tipos.png)

'''

#Podemos definir cadenas largas con triple 
#asterisco
texto = '''
Esta es mi cadena 
larga larga
'''

print(texto)

'''
Prefijos en cadenas

Las cadenas pueden estar precedidas por algun caracter:
r: indica que se trata una cadena raw (cruda)
f: es u formateo de cadena, lo que ingresemos en {}
sera un valor en python que se traducira a string

'''
texto = r'home\user\download'
print(texto)

'''

Cadenas de escape:
\\ -> Backslash
\' -> Comillas simple
\" -> comillas doble
\n -> salto de linea


'''

'''
OPERADORES SOBRE STRINGS:
- + : Contatenacion
- * : Repeticion
'''

texto = 'hola' + 'chau'
print(texto)
texto = 'hola' * 3
print(texto)

'''
Formateo de cadenas.

Existe la calse format que nos ofrese muchas
herramietnas para formatear nuestra salida

'''

# Alinear una cadena de caracteres a la derecha en 30 caracteres, con la siguiente sentencia:
print("{:>30}".format("raíz cuadrada de dos"))

# Alinear una cadena de caracteres a la izquierda en 30 caracteres (crea espacios a la derecha), con la siguiente sentencia:
print("{:30}".format("raíz cuadrada de dos"))

# Alinear una cadena de caracteres al centro en 30 caracteres, con la siguiente sentencia:
print("{:^30}".format("raíz cuadrada de dos"))

# Truncamiento a 9 caracteres, con la siguiente sentencia:
print("{:.9}".format("raíz cuadrada de dos"))

# Alinear una cadena de caracteres a la derecha en 30 caracteres con truncamiento de 9, con la siguiente sentencia:
print("{:>30.9}".format("raíz cuadrada de dos"))

'''
Con format tambien podemos pasarle variables a nuestro string
ya sea posicional o por kwargument

Pero otro ejemplo mas facil es hacerlo con f' _ '
'''

texto = f'La suma de 2 + 2 es {2+2}'
print(texto)