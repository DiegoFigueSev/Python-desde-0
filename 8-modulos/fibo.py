def fib(n):
    """Write Fibonacci series up to n"""
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a + b
    print()
    
def moduleName():
    print(__name__) # El valro GLOBAL __NAME__ nos regresa el nombre del archivo