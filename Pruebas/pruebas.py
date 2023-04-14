numero = input('por favor ingresa un numero mayor a 20 para calcular su raiz: ')

# Se verifica que el valor ingresado sea un número mayor a 20\n
#  atributo isdigit verifica que dentro del string haya solo numeros
while not numero.isdigit() or int(numero) <= 20:
    numero = input('solo se admiten numeros mayores a 20: ')

# Se convierte el valor ingresado a un entero
numero = int(numero)

decimales = input('por favor elige entre 2 o 3 decimales en el resultado: ')

# Se verifica que el valor ingresado sea 2 o 3
while not decimales.isdigit() or int(decimales) not in [2, 3]:
    decimales = input('solo se admiten 2 y 3 decimales en el resultado: ')

# Se convierte el valor ingresado a un entero
decimales = int(decimales)

raiz_cuadrada = numero ** 0.5
resultado = round(raiz_cuadrada, decimales)

print(f'la raiz cuadrada de {numero} es: {resultado}')
