# Reto 1 "Suma hasta 50"
total = 0
while total <= 50:
    num = input('por favor ingresa un numero para sumar al total: ')
    if num.isdigit():
        total += int(num)
    else:
        print('error solo se admiten números')
print('la suma total es:', total)
# Reto 2 "Más allá del cuarenta y dos"
num = 0
total = 0
while num <= 42:
    num = int(input('por favor ingresa otro numero: '))
    if num <= 42:
        total += num
print('la suma total es:', total)
# Reto 3 "Sumas consecutivas"
num1 = int(input('Por favor ingresa un numero:'))
num2 = int(input('Ingresa otro numero para ser sumado con el anterior: '))
total = num1 + num2
otro_num = input('quieres sumar otro numero mas responde (s/n): ')
while otro_num == str('s'):
    num3 = int(input('Por favor ingresa un ultimo numero:'))
    total = num1 + num2 + num3
    print('la suma de los tres números es:', total)
    break
else:
    print('la suma de los dos numero es:', total)
# Reto 4 "Lista de invitados"
invitados = []
nombre = input('por favor ingresa el nombre del primer invitado: ')
invitados.append(nombre)
nombre = input('por favor ingresa el nombre del segundo invitado: ')
invitados.append(nombre)
agregar = input('¿Quieres agregar otro invitado? (s/n): ')
while agregar == 's':
    nombre = input('por favor ingresa el nombre del tercer invitado: ')
    invitados.append(nombre)
    print('El numero de invitados va en: ', len(invitados))
    break
else:
    print('El numero de invitados va en: ', len(invitados))
# Reto 5 "Adivina el número secreto"
num_secret = 69
num_user = int(input('Por favor  adivina un numero del 1 al 100: '))
contador = 0
while num_secret != num_user:
    if num_user > num_secret:
        print('Tu numero es mayor al secreto.')
    else:
        print('Tu numero es menor al secreto.')
    num_user = int(input('Por favor intenta de nuevo: '))
    contador += 1
else:
    print(f'felicidades adivinaste el numero secreto {num_secret} y te tomo '
          f'{contador} intentos')
# Reto 6 "Un elefante se balanceaba…"
num_elefante = 1
print(f'{num_elefante} elefante se balanceaba '
      f'Sobre la tela de una araña '
      f'Como veía que resistía '
      f'Fueron a llamar a un camarada.')
while num_elefante < 10:
    elefantes_mas = int(input('Cuántos elefantes más se balancearán? (Ingrese'
                              ' un número más al mostrado): '))
    if elefantes_mas == num_elefante + 1:
        num_elefante += 1
        if num_elefante == 1:
            print(f'{num_elefante} elefante se balanceaba')
        else:
            print(f'{num_elefante} elefantes se balanceaban '
                  f'Sobre la tela de una araña '
                  f'Como veían que resistía '
                  f'Fueron a llamar a un camarada.')
    else:
        print('Número incorrecto, por favor intente de nuevo.')

