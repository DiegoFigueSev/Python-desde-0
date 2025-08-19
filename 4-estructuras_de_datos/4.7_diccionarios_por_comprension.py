'''
Tambien podemos crear: 

Dictionary comprenhension
'''

a = ['nombre', 'edad', 'nacionalidad']
b = ['Diego', 23, 'Boliviano']

dicc = {i:j for i, j in zip(a, b)}
print(dicc)