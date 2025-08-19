'''

Los bolleanos son sencillos de interpretar
o son TRUE o son False

'''

es_verdad = True
es_falso = False

''' 

Un booleanos es una subclase de int 
sus Valores son 0 o 1 

'''

es_verdad = int(True)
es_falso = int(False)
print(f'el valor true {es_verdad=} el valor false {es_falso=}')

'''

Los operadores booleanos son los siguientes:
- and
- or
- not

'''
print(True and False)
print(True or False)
print(not True)


'''
Para realizar la conversion de cualquier tipo 
a booleano se hace:

bool(x) 
False si x ∈ {0, 0.0, 0j, '', [], {}, set(), range(0), None}
todo lo demás es True. Ojo: bool("False") → True.
'''