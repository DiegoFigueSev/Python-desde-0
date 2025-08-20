'''
Las funciones recursivas son funciones que se llaman a si
mismas, durante su propia ejecucion.

Funcionan de forma similar a las iteraciones, pero deben encargarse 
de planificar el momento en el que dejan de llamarse a si mismas

Estas funciones se las utiliza en PROGRAMACION DINAMICA
'''

# Sin retorno
def cuenta_regresiva(numero):
    numero -= 1
    if numero > 0:
        print(numero)
        cuenta_regresiva(numero)
    else:
        print('BOOOOOOOOOOOOOOOOOOOOM!')
    print('Fin de la funcion', numero)

cuenta_regresiva(5)


# Con retorno
def fibonacci(n): # n es la posicion de fibonacci
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2) 

print(fibonacci(5))