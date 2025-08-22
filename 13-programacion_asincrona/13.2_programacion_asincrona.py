'''
Como ya mencionamos en la introduccion

Python es singre-threaded o mono hilo. Lo que significa que el interprete de instrucciones solo puede
ejecutar una cosa a la vez. Esto es debido a que utiliza un mecanimos de proteccion conoci ocomo el Global Interpreter Lock
el cual limita la capacidad de Python.

Para solventar esto, los lenguajes de un sólo hilo, como Python y JavaScript, entre otros,
utilizan un mecanismo llamado “event loop”. El event loop es una estructura
de control que maneja la ejecución de varias tareas de forma “simultánea”. Es decir,
una tarea puede ser pausada y reanudada en cualquier momento, lo que permite que otras tareas
puedan ser procesadas. Cuando una tarea se pausa, el event loop la suspende y comienza a procesar
otra tarea. Cuando la tarea pausada está lista para continuar, el event loop la reanuda.

'''


'''
El event loop es el encargado de gestioanr que tarea pasa a ejecutarse en base a una prioridad.
Estas tareas se almacenan en una Tasks/Ready queue, que es una estructura similar a un heap.

En python 3.4 podemos utilizar la biblioteca asyncio para obtener programacion asincrona de manera nativa.
Esta biblioteca nos provee de la sintaxis async/await.
'''


'''
async 
le indica al interprete de Python que se trata de una funcion asincrona, es decir, que dentro de esta funcion
vamos a poder realizar operaciones de forma asincrona sin bloquear la ejecucion principal de nuestro programa 
'''

'''
await
se utiliza para indicar a nuestra funcion asincrona, que vamos a esperar a que se resuelva una determinada operacion
antes de seguir ejecutando el codigo
'''

'''
NOTA: Tenemos el modulo request, el cual se encarga de realizar peticiones http
'''

import requests
from datetime import datetime

def tarea_sincrona():
    start_time = datetime.now()
    for _ in range(10):
        response = requests.get("https://dog.ceo/api/breeds/image/random").json()
        print(response)
    end_time = datetime.now()
    print(end_time - start_time)

tarea_sincrona()

'''
El resultado termina siendo como 7 segundos

Pero que pasa si lo hacemos asincrono?
'''

import asyncio
import aiohttp # Libreria para peticiones http asincronas
from datetime import datetime


async def asynchronous_task():
    start_time = datetime.now()
    print("We are going to perform an asynchronous operation")
    async with aiohttp.ClientSession() as session:
        for _ in range(10):
            async with session.get("https://dog.ceo/api/breeds/image/random") as resp:
                print(await resp.json())
    end_time = datetime.now()
    print('Duration async: {}'.format(end_time - start_time))

asyncio.run(asynchronous_task())

'''
Hemos realizado algunas mejoras en la definición de nuestra función al añadir el modificador async,
 lo que la convierte en una corutina, que son las que trabajan de forma efectiva con el event loop. 
 Además, hemos incluido la palabra clave await en el punto donde debemos esperar a que una tarea se realice.
 
 En este caso, realizamos una petición HTTP, pero podría ser otra operación que pueda requerir algún tiempo. 
 Es en ese momento, cuando el intérprete de Python se libera y el event loop asume el control para ejecutar otra tarea.
'''