'''
Una clase puede heredar de otra usando la sintaxis:

class Hija(Padre):
    ...


Cuando creamos una clase HIja, esta hereda los atributos de la clase Padre
'''


'''
Una clase hija puede sobreescribir metodos de la clase padre

Todos los metodos en Python son virtuales por defecto, si el padre
llama a un metodo, pero la hija lo redefinio, se ejecutara la version de la hija.

Si queremos extender el comportamiento del metodo padre, podemos llamarlo explicitamente

Padre.metodo(self, args)

o tambien:

super().metodo(args)
'''


'''
Se puede tener tambien herencia multiple

class Hija(Padre1, Padre2, Padre3):
    ...
    
La busqueda de atributos se hace de izquierda ad erecha
'''

class Animal:
    def __init__(self, nombre):
        self.nombre = nombre
        
    def hablar(self):
        return 'Hace algun ruido'

class Perro(Animal): # Si no modificamos el constructor no llamamos al del padre
    def hablar(self):
        return f'{self.nombre} dice: GUAUUU'
    
p = Perro('Firulais')
print(p.hablar())

class Vehiculo:
    def __init__(self, marca):
        self.marca = marca
    
    def info(self):
        return f'Vehiculo marca {self.marca}'

class Coche(Vehiculo):
    def __init__(self, marca, modelo):
        super().__init__(marca)
        self.modelo = modelo
    
    def info(self):
        return super().info() + f', modelo {self.modelo}'
    
c = Coche('Toyota', 'Corolla')

print(c.info())

