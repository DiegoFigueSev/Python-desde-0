'''
Que son los typehints? 

Son anotaciones de tipo, son una manera de indicar que tipo de datos espera una funcion, variable o clase

No cambia como funciona el codigo en tiempo de ejecucion.

A que me refiero? 

Los typehints solo son una ayuda para el desarrollador, ya que nos ayudan a visualizar que tipo de dato
manejaremos, que tiene q retornar una funcion, etc.
PERO! esta declaracion de tipo no es OBLIGATORIO, puedo decir q una funcion me retorna un int pero en realidad retorna un str o nada
Por eso digo que los typehints son una ayuda visual pero que no son tomadas en cuenta en tiempo de ejecucion


NOTA: Algunas librerias PyPi si toman en cuenta los typehints como fastAPI y BaseModel para realizar la generacion de documentacion y/o codigo

Los typehints nos ayudan a:
- Mejorar la legibilidad
- Ayudar a los IDE y linters a detectar errores
- Facilitar el testint y mantenimiento
'''

# Sin typehints
def suma(a,b):
    return a + b


# Con tpyehints
def suma(a: int, b: int) -> int:
    return a + b


'''
Variables con typehints
'''

nombre: str = 'Diego'

edad: int = 23

numeros: list[int] = [1,2,3]

precios: dict[str, float] = {'manzana': 12}


'''
Funciones
'''

def get_nombre(id: int) -> str | None:
    if id == 1:
        return 'Diego'
    return None


'''
Clases
'''

class Persona: 
    def __init__(self, nombre: str, edad: int):
        self.nombre = nombre
        self.edad = edad
    
    def saludar(self) -> str:
        return 'hola'
