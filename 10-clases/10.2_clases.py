'''
Las clases introducen un poquito de sintaxis nueva, 
tres nuevos tipos de objetos y algo de semantica nueva
'''

'''
La forma mas sencilla para la definicion de una clase es:

class [className]:
    <statement-1>
    
    <statement-N>

Cuando se ingresa una definicion de clase, se crea un namespace nuevo
el cual se usa como amvito local; por lo tanto, todas las asignaciones
a variables locales van a este nuevo spacename    
Por eso las funciones que se definen dentro de uan clase, quedan asociadas
como metodos de esa clase.
'''

'''
Los objetos clase soportan dos tipos de operaciones:
- hacer referencia a atributos
- instanciacion

Para hacer referencia a atributos, se usa la sintaxis estandar de todas 
las referencias a a tributos en Python:

objeto.nombre

Los nombres de atributos validos son TODOS los nombres que estaban
en el namespace de la clase cuando esta se creo.

Por lo tanto si tenemos:
'''

class MyClass:
    """A simple example class"""
    i = 12345
    
    def f(self):
        return 'hello world'
    
x = MyClass()
print(x.i)

'''
Los atributos validos para su referencia son:
- i 
- f

otro atributo valido es para imprimir la documentacion: __doc__
'''

'''
Como vimos, la instanciacion de una clase usa la notacion de funciones.
Hagamos de cuenta que el objeto de clase es una funcion sin parametros 
que retorna una nueva instancia de la clase.

x = MyClass()

Esto crea una nueva instancia de la clase y asigna este objeto a la 
variable local x
'''

'''
La operacion de instanciacion crea un objeto vacio.
Pero muchas veces necesitamos crear objetos con instancias en un estado
inicial particular.
Por lo tanto una clase puede definir un metodo especial llamado:

__init__() -> BASICAMENTE UN CONSTRUCTOR

se lo hace de esta forma:

def __init__(self):
    self.data = []

NOTA: self es como el this 

Cuando hacemos la instanciacion de la clase automaticamente invoca a __init__
'''

class Complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart

    def f(self):
        print('objeto metodo')
        
x = Complex(3.0, -4.5)
print(x.r)
print(x.i)


'''
Objetos de instancia

Cuando creamos una instancia de una clase, lo principal que podemos hacer
con ella es acceder a atributos.

- Atributos de datos (variables de instancia): No necesitan declararse antes,
simplemente existen cuando se les asigna un valor
'''

x.counter = 1 # Counter no existe, no lo declaramos, pero existe simplemente cuando se le asigno un valor, se lo considera una variable miembro
while x.counter < 10:
    x.counter *= 2
print(x.counter)
del x.counter

'''
En python los atributos de clase SE CREAN DINAMICAMENTE

Cada instancia fuarda sus atributos en un diccionario interno llamado:

__dict__

'''


'''
Otro atributo de una clase son los:

- Metodos: Son funciones que "pertenecen" al objeto. Los metodos que una 
instancia puede usar depende de su clase.

Cuando accedemos a un metodo de una instancia. Python no nos da 
directamente la funcion de la clase, si no un objet metodo el cual 
esta ligado a la instancia x
'''

# Por eso podemos hacer:
x.f() # Ejecuta la funcion f con x como primer argumento implicito
xf = x.f
xf()

'''
Porque esto funciona? si en mi f le necesito mandar self?

Esto pasa porque cuando hacemos x.f(), en realidad ejecutamos:

MyClass.f(x).

Es defir que x se pasa automaticamente como primer argumento para self
'''




'''
Variables de clase y de instancia

En general las variables de instancia son para datos unicos de cada instancia
Y las variables de clase son para atributos y metodos comaprtidos por todas las instancias de la clase

Osea:
- variable de instancia : Pertenece unicamente a la instancia que estemos creando
- Variable de clase : Se comparte a todas las instancias que creemos
'''

class Dog:

    kind = 'canine'         # class variable shared by all instances

    def __init__(self, name):
        self.name = name 
        Dog.kind += '+1'# instance variable unique to each instance

d = Dog('Fido')
e = Dog('Buddy')
d.kind                  # shared by all dogs
'canine'
e.kind                  # shared by all dogs
'canine'
d.name                  # unique to d
'Fido'
e.name                  # unique to e
'Buddy'
e.kind = 'lo edite' # SI LO EDITO YA NO SE COMAPRTE PORQUE YA NO HACE REFERENCIA AL MISMO PUNTO EN MEMORIA
# Todas las instancias de objetos comparten e.kind porque apunta al mismo lugar en memoria, 
# Si modificamos directamente la clase Dog.king estamos modificando el valor de ese espacio en memoria y es por eso que se ve refelado en todas las clases
# Pero si modificamos dicho atributo de clase directamente desde la instancia, la el atributo de la instancia en cuestion ya no apunta al mismo lugar en memoria que el de la clase
# Es por eso que si vuelvo a editar la clase como tal, no se edita la instancia con el atributo de clase ya modificado
print(e.kind)
print(d.kind)
Dog.kind = 'se comparte' # Si modificamos la clariable de clase se modifica en t odas las instancias
print(e.kind)
print(d.kind)

'''
Como hablamos antes, los datos comaprtidos pueden tener efectos 
inesperados si se involucran con objetos mutables.

Ya que este se modificara SIEMPRE que la instancia no cambie su valor por otro
'''

class Cat:
    tricks = []
    
    def __init__(self):
        pass
    
    def add_trick(self, trick):
        self.tricks.append(trick)

a = Cat()
b = Cat()
a.add_trick('salta')
b.add_trick('vuela')

print(a.tricks)

'''
Si vamos a manejar una lista, el correcto diseño es usando una variable de instancia
'''

'''
Métodos que llaman a otros métodos

Los métodos pueden llamarse entre sí usando self:

'''

class Bag:
    def __init__(self):
        self.data = []

    def add(self, x):
        self.data.append(x)

    def addtwice(self, x):
        self.add(x)
        self.add(x)
        
        
'''
NOTAS:

- Los atributos en Python son siemrpe accesibles, la privacidad se maneja
solo por convencion: _atribute

- Se pueden agregar mas atributos dinamicamente a instancias

- self es solo una convencion de this
'''