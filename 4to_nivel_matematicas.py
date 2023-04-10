# Reto 1 "Multiplicar decimales"
numero1 = float(input('Por favor ingresa un numero con muchos decimales: '))
numero2 = float(input('Por favor ingresa otro numero con muchos decimales: '))
resultado = numero1*numero2
print(f'El resultado de multiplicar los dos numero es: {resultado}')
# reto 2 "Multiplicar decimales y mostrar determinados decimales"
numero1 = float(input('Por favor ingresa un numero con muchos decimales: '))
numero2 = float(input('Por favor ingresa otro numero con muchos decimales: '))
resultado = numero1*numero2
decimales = int(input('por favor elige 1, 2 , 3 o 4 decimales a mostrar: '))
if decimales < 1 or decimales > 4:
    decimales = int(input('Por favor seleccione un número entre 1 y 4:'))
resultado_redondeado = round(resultado, decimales)
print(f'El resultado de multiplicar los dos numero es:{resultado_redondeado}')
# Reto 3 "Raíces cuadradas redondeadas"
numero = input('por favor ingresa un numero mayor a 20 para calcular su raiz: ')

# Se verifica que el valor ingresado sea un número mayor a 20\n
#  atributo isdigit verifica que dentro del string haya solo numeros
while not numero.isdigit() or int(numero) <= 20:
    numero = input('solo se admiten números mayores a 20: ')

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

print(f'la raíz cuadrada de {numero} es: {resultado}')