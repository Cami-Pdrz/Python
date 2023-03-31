# Reto 1 hola mundo, print hola,[nombre]
import re
# modulo re y función match para verificar solo letras
nombre = input('Hola, Ingresa tu nombre: ')
while not re.match("^[A-Za-z]+$", nombre):
    """^[A-Za-z]+$" verifica si la cadena solo contiene letras (tanto \n
    mayúsculas como minúsculas) y no tiene espacios en blanco ni caracteres \n
    especiales."""
    print('ingresa un nombre valido.')
    nombre = input('Hola de nuevo, por favor ingresa tu nombre: ')
print(f'hola, {nombre}')
# Reto 2 hola,[nombre][apellido]
apellido = input('ingresa tu apellido: ')
while not re.match("^[A-Za-z]+$", apellido):
    print('ingresa un nombre valido.')
    apellido = input('Por favor ingresa un apellido valido: ')
print(f'hola, {nombre} {apellido}')
# Reto 3 Mensaje multilínea
categorías = ["Desarrollo e Ingeniería", "Diseño y UX", "Marketing",
              "Negocios y emprendimiento", "Contenido Digital", "Liderazgo",
              "Startups", "Ingles", ]
# for categoría in categorías:
# print(categoría)
print('\n'.join([str(categoría)for categoría in categorías]))
"""Usar la función join() para unir los elementos de la lista en una sola \n
cadena separados por un salto de línea. La comprensión de lista se utiliza \n
para convertir cada elemento de la lista en una cadena"""
# Reto 4  "suma de enteros"
Num_1 = int(input('ingresa cualquier numero real:'))
Num_2 = int(input('ingresa otro numero real: '))
Cant_decimal = int(input('Cantidad de decimales a tener en cuenta: '))
resultado = round(Num_1 + Num_2, Cant_decimal)
# suma y redondea {resultado} a los decimales especificada por el usuario
print(f'La suma de {Num_1} y {Num_2} es {resultado}')
# Reto 5 "suma y multiplicación"
Num_one = int(input('ingresa cualquier numero real:'))
Num_two = int(input('ingresa otro numero real:'))
Num_three = int(input('multiplicador de la suma de los números anteriores:'))
Cant_decimal = int(input('Cantidad de decimales a tener en cuenta: '))
resultado = round((Num_one + Num_two)*Num_three, Cant_decimal)
print(f'Sumando {Num_one} y {Num_two} multiplicado por {Num_three}'
      f' es {resultado}')
# Reto 6 "suma y resta de 🍕"
Pizza_comer = int(input('Cuantas porciones de 🍕 traes al 🎉 ✨ : '))
Pizza_digerida = int(input('Cuantas 🍕 quedaron del 🎉 ✨ : '))
Pizza_sobrante = (Pizza_comer - Pizza_digerida)
print(f'El 🎉 ✨  estuvo genial y nos quedan {Pizza_sobrante} 🍕,'
      f'para el after 🎉 ✨ ')
# Reto 7 "Edad futura y pasada"
nombre_1 = str(input('Hola ingresa tu nombre: '))
Edad = int(input('Por favor ingresa tu edad: '))
print(f'{nombre_1} el año pasado tenias {Edad - 1} años'
      f', para el proximo año vas a tener {Edad + 1} años de edad')
# Reto 8 "divide la cuenta "
Cuenta = int(input('Ingresa el valor de la cuenta: '))
Personas = int(input('En cuantas personas se va a dividir la cuenta:'))
Propina = int(input('Ingresa el porcentaje de propina a incluir: '))
Impuestos = int(input('Ingresa el porcentaje de impuesto a incluir: '))
Total_pagar = Cuenta * 1 * ((Propina/100)+(Impuestos/100))
print(f'El total de la cuenta a pagar es {Total_pagar} incluyendo impuestos y'
      f' propina, dividido entre {Personas} personas,'
      f' cada uno debe pagar {Total_pagar/Personas}')
# Reto 9 "Calculando días"
Dias = int(input('ingresa una cantidad de días: '))
print(f'La cantidad de {Dias} días, equivale a {Dias*24} horas, '
      f'ha {Dias*24*60} minutos y a {Dias*24*60*60} segundos ')
# Reto 10 "conversion a  millas"
millas = float(input('Ingresa las millas a convertir en kilómetros: '))
km = float(1.609344*millas)
print(f'{millas} millas son igual a: {km} Kilómetros')
# Reto 11 "Cuantas veces un número en otro"
numero_mayor = int(input('Ingresa un número mayor a 1000: '))
numero_menor = int(input('Ingresa un número menor a 100: '))
# // operador division entera
veces_cabe = numero_mayor // numero_menor
print(f'El número {numero_menor} cabe {veces_cabe} veces en el número'
      f'{numero_mayor}.')
