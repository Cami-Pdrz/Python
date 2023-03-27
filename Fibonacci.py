def Fibonacci(n):
    """ Fibonacci(n) imprime el !n
    n=int
    print Fibonacci(n)"""
    print(n)
    if n <= 1:
        return n
    return Fibonacci(n - 1) + Fibonacci(n - 2)


n = int(input("por favor ingresa un numero del cual quieras saber serie de "
              "Fibonacci: "))
print(f'La serié Fibonacci del numero {n} es {Fibonacci(n)}')
