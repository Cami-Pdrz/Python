import math
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
# Reto 4
# import math
radio = input('por favor ingresa el radio del circulo a calcular su area: ')
while not radio.replace('.', '').isdigit():
    # en esa línea se está utilizando el método replace() de la cadena de \n
    # texto radio para eliminar el punto decimal. El método replace() \n
    # reemplaza todas las ocurrencias de una subcadena dentro de una cadena \n
    # con otra subcadena. En este caso, se está reemplazando el punto decimal\n
    # "." por una cadena vacía "".
    print('Solo se admiten números')
    radio = input('intenta de nuevo, ingresa el radio: ')

radio = float(radio)
area = round(math.pi * radio**2, 3)
print(f'El area del circulo con radio {radio} es {area} unidades cuadradas')
# Reto 5 "Calcular volumen de un cilindro"
radio = input('por favor ingresa el radio del cilindro a calcular su volumen:')
while not radio.replace('.', '').isdigit():
    print('Solo se admiten numeros')
    radio = input('intenta de nuevo, ingresa el radio: ')
altura = input('por favor ingresa la altura del cilindro a calcular su volumen:')
while not altura.replace('.', '').isdigit():
    print('Solo se admiten números')
    altura = input('intenta de nuevo, ingresa la altura: ')
radio = float(radio)
altura = float(altura)
volumen = round(math.pi * radio**2 * altura, 1)
print(f'El volumen del cilindro con radio {radio} y {altura} es {volumen} '
      f'unidades cubicas')
# Reto 6 "Mostrar enteros y residuos"
entero = input('por favor ingresa un entero a dividir: ')
while not entero.isdigit():
    print('solo se admiten números enteros')
    entero = input('ingresa de nuevo un numero entero: ')

divisor = input('ingresa un numero entero para dividir el numero anterior: ')
while not divisor.isdigit():
    print('solo se admiten números enteros')
    divisor = input('ingresa de nuevo un numero entero: ')
resultado, residuo = divmod(int(entero), int(divisor))
# divmod() es una función integrada en Python que toma dos argumentos y \n
# devuelve una tupla que contiene el cociente y el residuo de la división de \n
# los dos argumentos.
print(f'{entero} dividido entre {divisor} es {resultado} y sobra {residuo}.')
# Reto 7 "Calcular perímetros y áreas"
figuras = {'1': 'Triángulo ▲', '2': 'Cuadrado ■ ', '3': 'Pentágono ⬟'}
for key, value in figuras.items():
    print(f'{key}.{value}')
opcion = int(input('Selecciona una figura para calcular su perimetro/area: '))
if opcion == 1:
    print("Ha seleccionado el triángulo. Por favor ingresa ")
    lados = input("los 3 lados del triángulo separados por comas EJ:3,4,5: ")
    l1, l2, l3 = lados.split(",")
    perimetro = int(l1) + int(l2) + int(l3)
    s = (int(l1) + int(l2) + int(l3))/2
    area = (s * (s - int(l1)) * (s - int(l2)) * (s - int(l3)))**0.5
    print(f'El perímetro del triángulo con lados {l1}, {l2} y {l3} es'
          f' {perimetro} unidades lineales')
    print(f'Y su area es: {area} unidades cuadradas con la formula de Heron')
elif opcion == 2:
    print("Ha seleccionado el cuadrado. Por favor ingresa")
    lados = input("los 2 lados del cuadrados separados por comas EJ:3,4: ")
    l1, l2 = lados.split(",")
    perimetro = (int(l1) + int(l2)) * 2
    area = int(l1) * int(l2)
    print(f'El perímetro del cuadrado con lados {l1}, {l2} es'
          f' {perimetro} unidades lineales')
    print(f'Y su area es: {area} unidades cuadradas')
elif opcion == 3:
    print("Ha seleccionado el pentágono. Por favor ingresa")
    lados = input("los 5 lados del pentagono separados por comas EJ:3,4,5,7,8: ")
    l1, l2, l3, l4, l5 = lados.split(",")
    perimetro = (int(l1) + int(l2)) * 2
    area = (1/4) * ((5 + (5 * (5 * 2)**0.5)) * (int(l1)**2 + int(l2)**2 + int(l3)**2 + int(l4)**2 + int(l5)**2))**0.5
    area_print = round(area, 3)
    print(f'El perímetro del pentagono con lados {l1}, {l2}, {l3},'
          f' {l4}, {l5} es {perimetro} unidades lineales')
    print(f'Y su area es: {area_print} unidades cuadradas')
else:
    print("Opción inválida. Por favor seleccione un número válido.")
