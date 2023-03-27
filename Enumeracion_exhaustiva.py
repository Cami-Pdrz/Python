objetivo = int(input('Hola, Por favor ingresa un numero objetivo del cual quieras saber su raiz cuadrada: '))
respuesta = 0

while respuesta**2 < objetivo:
    print(respuesta)
    respuesta += 1
if respuesta**2 == objetivo:
    print(f'La raiz cuadrada del objetivo {objetivo} es el numero {respuesta}')
else:
    print(f'El numero objetivo {objetivo} no tiene raiz cuadrada')
