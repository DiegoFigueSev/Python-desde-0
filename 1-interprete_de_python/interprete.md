# 1 El interprete de python 

Para acceder al interprete de python debemos correr el siguiente comando: 
```
python
# o tambien
python3.13
```

Se puede salir del interprete con la combinacion de teclas CTRL+D o tambien CTRL+Z. Aunque tambien tenemos la funcion quit() que nos ayuda con lo mismo.

El interprete de python nos ayuda a realizar rapidas ejecuciones de alguno de nuestros scripts. 

## 1.1 Paso de argumentos 

Cuando son conocidos por el interprete, el nombre del script y los argumentos adicionales. Estos se convierten en una lista de cadenas de texto asignada a la variable argv del modulo sys. 

## 1.2 Modo interactivo

Cuando iniciamos el interprete de python y los comandos se leen desde la terminal, o bueno, el flujo de nuestro programa lo hacemos directamente en la terminal, se dice que estamos en el modo interactivo.
En este modo el siguiente comando que le pasemos sera el prompt primario (>>>) y para las lineas de continuacion tenemos el prompt secundario (...)

```
>>> the_world_is_flat = True
>>> if the_wold_is_flat:
...	print("Be careful not to fall off!)
...
Be careful not fall off!
```

