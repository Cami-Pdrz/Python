# Reto 1 "Curso favorito"
curso = input('Por favor ingresa tu curso de Platzi favorito: ')
for i in range(8):
    print(curso)
# Reto 2 "Curso favorito ‘n’ veces"
curso = input('Por favor ingresa tu curso de Platzi favorito: ')
veces = int(input('Por favor ingres el numero de veces que quieres mostrar el'
                  f' curso: '))
while veces <= 0:
    veces = int(input('Se admiten números mayores a 0, intenta de nuevo: '))
for i in range(veces):
    print(curso)
# Reto 3 "Curso en una columna"
curso = str(input('Por favor ingresa tu curso favorito de Platzi: '))
for carácter in curso:
    print(carácter)
# Reto 4 "Animal en columna ‘n’ veces"
animal = str(input('Por favor Ingresa tu animal favorito:  '))
veces = int(input('Por favor ingres el numero de veces que quieres mostrar el '
                  'animal: '))
for i in range(veces):
    for carácter in animal:
        print(carácter)
    print('\n')
# Reto 5 "Tabla de multiplicar"
numero = int(input('Ingresa un número para mostrar su tabla de multiplicar: '))
for i in range(1, 11):
    resultado = numero * i
    print(f'{numero} X {i} = {resultado}')
# Reto 6 "Cuenta regresiva"
numero = int(input('Ingresa un número para mostrar su cuenta regresiva: '))
if numero >= 0:
    for i in range(numero, 0, -1):
        print(i)
else:
    for i in range(numero, 0, 1):
        print(i)
print('¡Cuenta regresiva finalizada!')
# Reto 7 "Curso favorito, sin exagerar"
curso = input('Por favor ingresa tu curso de Platzi favorito: ')
veces = int(input('Por favor ingres el numero de veces que quieres mostrar el'
                  ' curso: '))
if veces <= 0:
    veces = int(input('Se admiten números mayores a 0, intenta de nuevo: '))
elif veces >= 15:
    print(f'El numero {veces} es muy grande, mo te pases de listo ')
    veces = 3
for i in range(veces):
    print(curso)
# Reto 8 "Suma autorizada"
total = 0
for i in range(4):
    num = int(input('Ingresa un número: '))
    sumar = input('¿Deseas sumar este número al total? (s/n): ')
    if sumar == 's':
        total += num

print(f"El total de la suma de los números aceptados es: {total}")
# Reto 9 "recta numérica"
while True:
    signo = input('Ingresa el sentido de la recta numérica (+/-): ')

    if signo not in ['+', '-']:
        print('Error, signo invalido, intenta de nuevo')
    else:
        numero = int(input('Indica el limite de la recta numérica: '))
        if signo == '+':
            for i in range(0, numero + 1, 1):
                print(i)
            else:
                numero = int(input('Indica el limite de la recta numérica: '))
                for i in range(0, - numero - 1, - 1):
                    print(i)
                    break
