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
num1 = 1
sumar = input('deseas sumar el numero al total responde si/no:  ')
if sumar == str('si'):
    total = num1
else:
    num2 = 2
    sumar = input('deseas sumar el numero al total responde si/no:  ')
    if sumar == str('si'):
        total = + num2
    else:
        num3 = 3
        sumar = input('deseas sumar el numero al total responde si/no:  ')
        if sumar == str('si'):
            total = + num3
        else:
            num4 = 4
            sumar = input('deseas sumar el numero al total responde si/no:  ')
            total = + num4
            if sumar == str('si'):
                print(total)