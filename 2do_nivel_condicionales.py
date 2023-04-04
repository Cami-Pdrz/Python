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
Pet_user = str(input('Ingresa tu animal favorito:'))
if Pet_user == 'Tortuga' or Pet_user == 'TORTUGA' or Pet_user == 'tortuga':
    print('También me gustan las tortugas')
else:
    print('Ese animal es genial, pero prefiero las tortugas')
# Reto 5 "como está el clima"
LLuvia = input('¿Esta lloviendo? (Si/No): ')
if LLuvia.lower() == 'si':
    # método.lower convierte la entrada a minúsculas
    print('¿esta haciendo mucho viento? (Si/No):?')
    Viento = input()
    if Viento.lower() == 'si':
        print('hace mucho viento para salir con una sombrilla')
    else:
        print('por favor lleve una sombrilla')
else:
    print('Te deseo un bonito día.')
# Reto 6 "Edad permitida"
while True:
    try:
        Edad = int(input('Ingresa tu edad: '))
        if Edad >= 30:
            print('Nunca es trade para aprender ¿Qué curso tomaremos?')
        elif Edad >= 18:
            print('Es un momento excelente para impulsar tu carrera.')
        else:
            print('Sabes hacia dónde dirigir tu futuro? Seguro puedo ayudarte')
        break
    except ValueError:
        print('valor incorrecto ingresa un numero entero')
# Reto 7 "Mensajes opcionales"
while True:
    try:
        opcion = int(input('Por favor ingresa un numero del 1 al 6: '))
        if opcion == 1:
            print('Hoy aprenderemos sobre prorgamación')
        elif opcion == 2:
            print('¿Qué tal tomar un curso de marketing digital?')
        elif opcion == 3:
            print('Hoy es un gran día para comenzar a aprender de diseño')
        elif opcion == 4:
            print(' ¿Y si aprendemos algo de negocios online?')
        elif opcion == 5:
            print('Veamos un par de clases sobre producción audiovisual')
        elif opcion == 6:
            print('Tal vez sea bueno desarrollar una habilidad blanda'
                  ' en Platzi')
        else:
            print('numero no valido ingresa uno entre 1 y 6')
        break
    except ValueError:
        print('Solo es permitido números del 1 al 6')
