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
Num_1 = float(input('ingresa cualquier numero real:'))
Num_2 = float(input('ingresa otro numero real: '))
Cant_decimal = int(input('Cantidad de decimales a tener en cuenta: '))
resultado = round(Num_1 + Num_2, Cant_decimal)
# suma y redondea {resultado} a los decimales especificada por el usuario
print(f'La suma de {Num_1} y {Num_2} es {resultado}')
# Reto 5 "suma y multiplicación"
Num_one = float(input('ingresa cualquier numero real:'))
Num_two = float(input('ingresa otro numero real:'))
Num_three = float(input('multiplicador de la suma de los números anteriores:'))
Cant_decimal = int(input('Cantidad de decimales a tener en cuenta: '))
resultado = round((Num_one + Num_two)*Num_three, Cant_decimal)
print(f'Sumando {Num_one} y {Num_two} multiplicado por {Num_three}'
      f' es {resultado}')
