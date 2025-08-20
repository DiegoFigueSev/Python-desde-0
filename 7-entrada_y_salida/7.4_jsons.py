'''
Python viene con un modulo por defecto para el manejo de json:

json (si asi se llama)
'''

import json

a = json.dumps(['foo', {'bar': ('baz', None, 1.0, 2)}], sort_keys=True, indent=3)

print(a)

dicc = dict(
    nombre='Diego',
    apellido='Figueroa',
    edad=23,
    habilidades=dict(
        blandas=['social',' amigable', 'enfocado'],
        tecnicas=['comprometido', 'genio']   
    )    
)

'''
Para una impresion linda usar: indent=int
'''
user_json = json.dumps(dicc, sort_keys=True, indent=2)
print(user_json)


archivo = open('7-entrada_y_salida/carpeta/datos.txt', 'w')
print(archivo)

json.dump(dicc, archivo, indent=2) # ESCRIBE EN UN ARCHIVO

archivo.close()