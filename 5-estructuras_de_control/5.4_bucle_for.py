'''
En lugar de SIEMPRE ITERARA en una progresion aritmetica de numeros 
o darle la posibilidad de definir tnato el paso de la iteracion
como la condicion de fin (for int i = 0; i < 10; i++)

La sentencia for en Python itera SOBRE LOS ITEMS de cualquier secuencia
'''

'''
TIPOS DE BUCLE FOR
'''

# Bucle for con listas
animals = ['perro', 'gato', 'conejo', 'serpiente']
for animal in animals:
    print(f'el animal es: {animal}')
    
# for con listas y funcion range()
# Cuando necesitemos iterar sobre una progresion aritmetica.
# la solucion seria generar una lsita con dicha progesion
oracion = 'pavlito clavo un clavito'
frases = oracion.split()
for index in range(len(frases)): #range crae una lista hasta un limite x
    print (f'la palabra es: {frases[index]}')
    
# for con tuplas
# Es lo mismo que con listas

# for con Diccionarios
usuario = {
    'nombre': 'Diego',
    'apellido': 'Figueroa',
    'edad': 23,
    'estado civil': 'soltero',
    'esVaron': True
}

for k, v in usuario.items():
    print(f'{k=} y {v=}')
    

'''
Tambien podemos unir el bucle for con else

en un for, la sentencia else se ejecuta despues de la finalizacion
del loop. Siempre y cuando no haya ocurrido ningun break

A diferencia del while, que la sentencia else, se ejecuta 
cuando la condicion del bucle se vuelve falsa
'''
for n in range(2,10):
    for x in range(2,n):
        if n % x == 0:
            print('entrando al break')
            print(n, 'equals', x, '*', n // x)
            break
    else:
        print('No se ejecuto el break')
        print(n, 'is a prime number')


'''
Al igual que los whiles, los for pueden contener sentencias
break y continue
'''

for n in range(10):
    if (n == 5):
        break
    print(n)
    
    