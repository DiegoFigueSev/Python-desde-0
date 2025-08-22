# Dentro de este .md vamos a estar viendo algunas caracteristicas de python

## Python es MONOHILO
Similar a JS que es monohilo, tambien lo es pero en su nucleo
pero funciona distinto por el GIL
- G : Global
- I : Interpreter
- L : Lock
El gil nos impide que dos threads ejecuten codigo Python puro al mismo tiempo que un proceso. 

Sin embargo, Python permite concurrencia:
- Con threading
- Con asyncio
- Con multiprocessing

Entonces que hace python? 
r. Python NO es estrictamente MONOHILO, puede crear varios hilos con threading. PERO no puede ejecutar todos estos hilos EN PARALELO, lo que hace es ejecutar unicamente un hilo. 
Entonces como maneja los hilos? 
r. El manejo de hilos lo hace con el GIL, este va prestando el interprete a cada hilo, le asigna pedacitos de tiempo para que se turnen. COMO SE LLAMA ESTA TECNICA? EL GRAN ROUND ROBIN!



