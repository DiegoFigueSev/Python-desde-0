'''
Las clases proveen una forma de empaquetar datos y funcionalidad
juntos.
AL crear una clase nueva, se crea un nuevo tipo de objeto.

Cada instancia de claes puede tener atributos adjuntos par mantener
su estado
Cada clase puede tener tambien metodos para modificar su estado
'''

'''
El mecanismo de clases de Python agrega clases con un minimo
de nuevas sintaxis y semanticas.
Las clases en python proveen todas las caracteristicas normales de la 
POO.
'''

'''
Hay que tener en cuenta que en python:
- Todos los miembos son publicos (aunque por definicion _var no lo es)
- Todas las funciones de la clase son virtuales (puede hacerse override)
- Las clases mismas son OBJETOS -> Podemos asignarlas, pasarlas y modificarlas

TODO EN PYTHON ES UN OBJETO 
'''

'''
En python un nombre es solo una referencia (alias) a un OBJETO en MEMORIA
donde varias variables pueden apuntar al mismo objeto (aisling)
Con tipos inmutables no suele inportar mucho porque estos NO MUTAN pero con
tipos mutables si importa y ya vimos porque, porque van cambiando.
'''

a = 2
b = a
b += 3 # .> al ser no mutable ya no apunta al mismo objeto
print(a) # NO MUTA

a = [1,2,3]
b = a # -> ambos apuntan al mismo objeto
b.append(10) # -> al ser mutable, se modifica el objeto como tal
print(a) # MUTO

'''
Tener este comportamiento hace que pasar objetos a funciones sea eficiente
Python no crea una cpia, solo pasa la referencia del objeto en memoria
Por ello si una funcion modifica un objeto mutable recibido como parametro
el cambio es visible tambien fuera de la funcion.
Esto elimina mecanismo como "paso por referencia" o "paso por valor"
'''


'''
ESPACIO DE NOMBRES

El namespace es la relacion que antiene los nombres o identificadores con los 
objetos que representan.
Aunque internamente suelen representarse como diccionarios 
En el nivel de usuario se perviben como ambitos donde los nombres estan definidos

Existen distintos tipos de namespaces en Python:
- Builints: que incluyen funciones como len() y abs() y todas las excepciones
- global: El global de cada modulo donde se almacenan funciones clases y variables definidas
- local: De una funcion, creado cada vez que la funcion es llamada y destruido al terminar
Ademas de esto las clases crean su propio namespace al ser definidas conteniendo atributos y metodos
'''


'''
AMBITOS EN PYTHON

El <ambito> es la region de un programa donde un nombre puede ser accedido directamente
sin necesidad de prefijos. 
Python sigue la regla conocida como LEGB(local, enclosing, global, builtin) para resolver los nombres
1. Primero busca en los ambitos locales de la funcion
2. Luego en los ambitos de funciones externas
3. Despues en el global del modulo donde la funcion fue definida
4. Finalmente en los builtins

Python tambien permite modificar como se asignan los nombresm ediante las declaraciones global y nonlocal.
- global: Indica que una variable debe usarse y reasignarse en el ambito global del modulo
- nonlocal: Sirve para modificar variables definidas en un ambio externo (comun en funciones anidadas)
si no se usa este, las asignaciones siemrpe crean o modifican variables en el ambito mas interno
'''

def scope_test():
    def do_local():
        spam = "local spam" # Aqui nunca modifica el spam 

    def do_nonlocal():
        nonlocal spam # le decimos: 'voy a manejar una variable llamada spam, que no es local, esta en mis funciones'
        spam = "nonlocal spam" # Aqui le decimos q spam no es local y lo modifica

    def do_global():
        global spam # le decimos: 'voy a manejar una variable que no es local ni enclosing, es global del modulo'
        spam = "global spam" # Aqui lo modifica de manera global pero no de manera local por eso no ahce nada

    spam = "test spam"
    do_local()
    print("After local assignment:", spam)
    do_nonlocal()
    print("After nonlocal assignment:", spam)
    do_global()
    print("After global assignment:", spam)

scope_test()
print("In global scope:", spam)
