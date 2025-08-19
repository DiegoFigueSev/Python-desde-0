'''
El bucle: while 
nos permite ejecutar ciclos o secuencias periodicas 
las cuales ejecutan codigo multiples veces
'''

'''
Tipos de bucle while
'''

# Controlado por conteo
suma, numero = 0, 1
while numero <= 10:
    suma = numero + suma
    numero = numero + 1
print(f'la suma es {suma}')


# Controlado por evento
promedio, total, contar = 0.0, 0, 0
grado = int(input())
while grado != -1:
    total = total + grado
    contar = contar + 1
    grado = int(input())
promedio = total / contar
print(f'El promedio es: {promedio}')

# while con else
promedio, total, contar = 0.0, 0, 0
mensaje = "Introduzca la nota de un estudiante (-1 para salir): "

grado = int(input(mensaje))
while grado != -1:
    total = total + grado
    contar += 1
    grado = int(input(mensaje))
else:
    promedio = total / contar
    print(f"Promedio de notas del grado escolar: {str(promedio)}")

'''
SENTENCIAS UTILITARIAS
'''

# Sentencia: break
# Esta rompe todo el ciclo
variable = 10
while variable > 0:
    print('Bucle while con break')
    variable = variable - 1
    if variable == 8:
        break

# Sentencia: continue
# Esta hace un salgo a la siguiente iteracion del ciclo

counter = 0;
lista = []
while counter < 10:
    if counter == 5: 
        counter += 1
        continue
    lista.append(counter)
    counter = counter + 1

print(lista)
