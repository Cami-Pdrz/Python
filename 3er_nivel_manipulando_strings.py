# Reto 1 "longitud del string"
import re
curso = str(input('Por favor ingresa tu curso favorito: '))
longitud = len(curso)
print(f'El curso que ingresaste es  un string de {longitud} caracteres')
# Reto 2 "Suma de strings"
nombre = input('Por favor ingresa tu nombre: ')
apellido = input('Por favor ingresa tu apellido: ')
comida = input('Por favor ingresa tu comida favorita: ')
while not re.match("[A-Za-z]+$", nombre):
    print('ingresa un nombre valido')
    nombre = input('Por favor ingresa tu nombre: ')
while not re.match("[A-Za-z]+$", apellido):
    print('ingresa un apellido valido')
    apellido = input('Por favor ingresa tu apellido: ')
while not re.match("[A-Za-z]+$", comida):
    print('ingresa una comida valida')
    comida = input('Por favor ingresa tu comida favorita: ')
print(f'Hola, mi nombres es {nombre} {apellido} y mi comida favorita es'
      f' {comida}')
