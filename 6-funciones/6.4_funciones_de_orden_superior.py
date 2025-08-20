'''
Las funciones de orden superior son funciones que entre sus 
parametros tienen una funcion
Y tambien son funciones que pueden retornar otra funcion
'''

def suma(x, y):
    return x + y

def f(operation, x, y):
    return operation(x, y)

print(f(suma, 2, 2)) # 4
print(f(lambda x, y: x - y, 2, 2)) # 0

'''
Como vimos, las funciones anonimas o lambdas son muy utiles 
cuando se necesita una funcion como parametro
'''


'''
Algunas funciones de orden superior que viene por defecto en python son:
'''

# filter
lista = [1,2,3,4,5,6,7,8,9]
print(list(filter(lambda x : x % 2 != 0, lista)))

# usando lsitas por comprension
print([x for x in range(10) if x % 2]) # Recodemos que 0 es False siempre


# map 
print(list(map(lambda x : x * 2, lista)))