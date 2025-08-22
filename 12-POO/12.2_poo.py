'''
POO es un paradigma de la programacion.
Este paradigma nos premite organizar el codigo de una manera que se asemeja bastante a como pensamos en la vida real 

Utilizando clases podemos agrupar bloques de logica en "OBJETOS" 
'''

'''
Los 4 pilares de POO son:
- Abstraccion
- Herencia
- Polimorfismo 
- Encapsulacion
'''

'''
Abstraccion

La abstraccion oculta al usuario la funcionalidad interna de una aplicacion

Nosotros vemos la abtraccion en nuestros dias a dias 
usamos el celular pero no sabemos que pasa por detras

Por ejemplo, creamos una clase abstracta FIGURA que define un contrato:
todas las figuras deben poder calcular su area y perimetro.

- No damos la implementacion de la clase abstracta solo definimos el que
'''

from abc import ABC, abstractmethod

class Figura(ABC):
    
    @abstractmethod
    def area(self) -> float:
        pass

    @abstractmethod
    def perimetro(self) -> float:
        pass

'''NOTA: VIMOS QUE ESTAMOS IMPORTANDO ABC Y ABSTRAC METHOD QUE SON ESTOS?
abc = abstract base class 

esta en el modulo standar de Python y se usa para crear clases abstractas

Una clase abstracta es una clase que no se puede instanciar directamente
Sirve como plantilla/contrato
En python se logra heredando de ABC y usando el decorador @abstractmethod
'''

# Implementaciones concretas
class Cuadrado(Figura):
    def __init__(self, lado: float):
        self.lado = lado

    def perimetro(self) -> float:
        return self.lado * 4

    def area(self) -> float:
        return self.lado * self.lado


'''
Herencia

Ya vimos todo sobre herencia en el capitulo 10. 10.1 Herencia
'''


'''
Polimorfismo

El polimorfismo nos permite modificar ligeramente los metodos y atributos 
de subclases previamente definidos en la superclase

El sginficado de polimorfismo es "MUCHAS FORMAS". Esto se debe a que construimos un metodo con el mismo nombre
pero con diferente funcionalidad
'''

class Rectangulo(Figura):
    def __init__(self, lado: float):
        self.lado = lado

    def area(self) -> float:
        return self.lado * self.lado

    def perimetro(self) -> float:
        return self.lado + self.lado

# Esta funcion tiene la misma funcion pero con distintos comportamientos
def mostrarInfo(figura: Figura):
    print(figura.perimetro())
    print(figura.area())

mostrarInfo(Rectangulo(5))
mostrarInfo(Cuadrado(5))


'''
Encapsulacion

Proceso en el que protegemos la integridad de los datos de una clase

Aunque no existe un privado en Python, podemos aplicar encapsulacion usando mangling en Python.

'''

class CuentaBancaria:
    def __init__(self, titular: str, saldo: float):
        self.titular = titular
        self.__saldo = saldo   # atributo privado (encapsulado)

    # Método público para acceder al saldo (getter)
    def get_saldo(self):
        return self.__saldo

    # Método público para modificar el saldo (setter con validación)
    def depositar(self, monto: float):
        if monto > 0:
            self.__saldo += monto
            print(f"Se depositaron {monto}. Nuevo saldo: {self.__saldo}")
        else:
            print("El monto debe ser positivo.")

    def retirar(self, monto: float):
        if monto <= self.__saldo:
            self.__saldo -= monto
            print(f"Se retiraron {monto}. Nuevo saldo: {self.__saldo}")
        else:
            print("Fondos insuficientes.")

cuenta = CuentaBancaria("Diego", 1000)

# Acceso al saldo solo mediante método (encapsulación)
print(cuenta.get_saldo())  # ✅ 1000

cuenta.depositar(500)      # ✅ aumenta saldo
cuenta.retirar(2000)       # ❌ fondos insuficientes

# Acceso directo al atributo privado (no recomendable)
print(cuenta.get_saldo())      # 🔴 AttributeError
