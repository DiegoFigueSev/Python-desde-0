"""
1. Clases en Python
- Una clase es una "plantilla" para crear objetos.
- Los objetos tienen atributos (datos) y métodos (funciones).
"""

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def saludar(self):
        return f"Hola, soy {self.nombre} y tengo {self.edad} años"

p = Persona("Diego", 25)
print(p.saludar())


"""
2. Variables de instancia vs variables de clase
- Variables de instancia → únicas para cada objeto (self).
- Variables de clase → compartidas por todas las instancias.
"""

class Ejemplo:
    contador = 0  # variable de clase
    
    def __init__(self, valor):
        self.valor = valor  # variable de instancia
        Ejemplo.contador += 1

a = Ejemplo(10)
b = Ejemplo(20)
print(a.valor, b.valor)       # 10 20
print(a.contador, b.contador) # 2 2 (compartido)


"""
3. Métodos de instancia, clase y estáticos
- Método de instancia: recibe self.
- Método de clase: recibe cls (usa @classmethod).
- Método estático: no recibe ni self ni cls (usa @staticmethod).
"""

class Utilidad:
    def metodo_instancia(self):
        return "Método de instancia"
    
    @classmethod
    def metodo_clase(cls):
        return f"Método de clase en {cls.__name__}"
    
    @staticmethod
    def metodo_estatico():
        return "Método estático"

u = Utilidad()
print(u.metodo_instancia())
print(Utilidad.metodo_clase())
print(Utilidad.metodo_estatico())


"""
4. Herencia y sobreescritura
- Una clase puede heredar de otra.
- Se pueden sobrescribir métodos.
- Con super() se puede llamar al método del padre.
"""

class Animal:
    def hablar(self):
        return "Hace un sonido"

class Perro(Animal):
    def hablar(self):
        return "Guau!"
    
class Gato(Animal):
    def hablar(self):
        return "Miau!"

print(Perro().hablar())
print(Gato().hablar())


"""
5. Clases abstractas (interfaces en Python)
- Python no tiene interfaces "puras".
- Se usan clases abstractas con el módulo abc.
- Obligan a las subclases a implementar ciertos métodos.
"""

from abc import ABC, abstractmethod

class Figura(ABC):
    @abstractmethod
    def area(self):
        pass

class Cuadrado(Figura):
    def __init__(self, lado):
        self.lado = lado
    def area(self):
        return self.lado * self.lado

c = Cuadrado(4)
print(c.area())

"""
6. Variables privadas
- Python no tiene verdaderos "privados".
- Convención: _variable = "protegido"
- Convención: __variable = "privado" (name mangling)
"""

class Cuenta:
    def __init__(self, saldo):
        self._saldo = saldo          # convención: interno
        self.__pin = 1234            # name mangling

    def mostrar_saldo(self):
        return self._saldo

c = Cuenta(500)
print(c._saldo)          # posible, pero no recomendado
# print(c.__pin)         # ERROR
print(c._Cuenta__pin)    # acceso con name mangling


"""
7. Todo es un objeto
- Incluso las clases mismas son objetos.
- Se pueden crear dinámicamente.
"""

print(type(123))        # <class 'int'>
print(type("hola"))     # <class 'str'>
print(type(Persona))    # <class 'type'>


"""
8. Curiosidades
- Métodos mágicos (dunder methods) como __init__, __str__, __len__, etc.
- Se pueden redefinir para cambiar el comportamiento de objetos.
"""

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        return f"({self.x}, {self.y})"
    
    def __add__(self, otro):
        return Vector(self.x + otro.x, self.y + otro.y)

v1 = Vector(1, 2)
v2 = Vector(3, 4)
print(v1 + v2)  # (4, 6)
