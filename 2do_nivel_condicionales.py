# Reto 1 "número mayor y menor "
num_1 = int(input('Ingresa un numero entero: '))
num_2 = int(input('Ingresa un segundo numero entero: '))
if num_1 == num_2:
    print(f'Los dos números ingresados son iguales y la diferencia es:'
          f' {abs(num_1-num_2)}')
elif num_1 > num_2:
    print(f'El numero mayor es: {num_1} y la diferencia es:'
          f' {abs(num_1-num_2)}')
else:
    print(f'El numero mayor es: {num_2} y la diferencia es:'
          f' {abs(num_1-num_2)}')
# Reto 2 "En el rango por favor"
limite = int(input('Ingresa un numero que servirá de limite: '))
comparar = int(input('Ingresa un numero para comparar con el limite: '))
if limite > comparar:
    print(f'El número {comparar} se encuentra en el rango, gracias')
else:
    print(f'El número {comparar} excede el límite permitido')
# Reto 3 "Rangos cambiantes"
limit_superior = int(input('Ingresa un numero de limite superior: '))
limit_inferior = int(input('Ingresa un numero de limite inferior: '))
num_comparar = int(input('Ingresa un numero para comparar: '))
if num_comparar >= limit_inferior and num_comparar <= limit_superior:
    print(f'El número de comparación {num_comparar} se encuentra entre '
          f' límite inferior {limit_inferior} y el límite superior'
          f' {limit_superior}')
elif num_comparar < limit_inferior:
    print(f'El numero de comparación {num_comparar} es menor al limite'
          f'inferior {limit_inferior}')
else:
    print(f'El numero de comparación {num_comparar} es mayor al limite'
          f'superior {limit_superior}')
# Reto 4 "I like turtles"