# Reto 1 "longitud del string"
import re
"""el módulo re para trabajar con expresiones regulares. Luego, definimos \n
la expresión regular patron que valida que la entrada del usuario solo \n
contiene letras minúsculas, espacios y tildes."""
curso = str(input('Por favor ingresa tu curso favorito: '))
longitud = len(curso)
print(f'El curso que ingresaste es  un string de {longitud} caracteres')
# Reto 2 "Suma de strings"
nombre = input('Por favor ingresa tu nombre: ')
apellido = input('Por favor ingresa tu apellido: ')
comida = input('Por favor ingresa tu comida favorita: ')
while not re.match("^[\\w ]+$", apellido, flags=re.UNICODE):
    """expresión regular utilizada es "^[\\w ]+$", que permite letras, \n
    números, guiones bajos y espacios en blanco."""
    print('ingresa un nombre valido')
    nombre = input('Por favor ingresa tu nombre: ')
while not re.match("^[\\w ]+$", apellido, flags=re.UNICODE):
    print('ingresa un apellido valido')
    apellido = input('Por favor ingresa tu apellido: ')
while not re.match("^[\\w ]+$", apellido, flags=re.UNICODE):
    print('ingresa una comida valida')
    comida = input('Por favor ingresa tu comida favorita: ')
    break
print(f'Hola, mi nombres es {nombre} {apellido} y mi comida favorita es'
      f' {comida}')
# Reto 3  "Ajusta las iniciales"
"""el módulo re para trabajar con expresiones regulares. Luego, definimos \n
la expresión regular patron que valida que la entrada del usuario solo \n
contiene letras minúsculas, espacios y tildes."""
patron = r'^[a-záéíóúüñ\s]+$'
nombre = input('Por favor ingresa tu nombre en minúsculas: ')
while not re.match(patron, nombre):
    print('Solo se admiten minúsculas, espacios y tildes')
    nombre = input('Por favor ingresa tu nombre en minúsculas: ')
apellido = input('Por favor ingresa tu apellido en minúsculas: ')
while not re.match(patron, apellido):
    print('Solo se admiten minúsculas, espacios y tildes')
    apellido = input('Por favor ingresa tu apellido en minúsculas: ')
país = input('Por favor ingresa tu país de origen en minúsculas: ')
while not re.match(patron, país):
    print('Solo se admiten minúsculas, espacios y tildes')
    país = input('Por favor ingresa tu país de origen en minúsculas: ')
# Separamos el nombre completo en palabras individuales
palabras = nombre.split()

# Iteramos sobre cada palabra y capitalizamos la primera letra
capitalizads = [palabra.capitalize() for palabra in palabras]

# Unimos las palabras capitalizadas en un solo string
nombre_capi = ' '.join(capitalizads)
palabras = apellido.split()
capitalizads = [palabra.capitalize() for palabra in palabras]
apellido_capi = ' '.join(capitalizads)
apeliido_capi = ' '.join(capitalizads)
palabras = país.split()
capitalizads = [palabra.capitalize() for palabra in palabras]
pais_capi = ' '.join(capitalizads)
print(f'Nombre: {nombre_capi}')
print(f'Apellido: {apellido_capi}')
print(f'País de origen: {pais_capi}')
# Reto 4 "string fragmentado"
oración = str(input('Por favor ingresa una línea de un poema o canción que'
                    'supere los 10 caracteres: '))
while len(oración) < 10:
    oración = str(input('La oración debe tener al menos 10 caracteres.'
                        ' Por favor, ingresa una nueva línea: '))
longitud_string = len(oración)
print(f'la longitud del texto es: {longitud_string}')
inicial = int(input(f'Por favor ingresa un rango inicial de 1 a '
                    f'{longitud_string}: '))
while inicial < 1 or inicial > longitud_string:
    inicial = int(input(f'El rango inicial debe estar entre 1 y '
                        f'{longitud_string}.Por favor, ingresa un nuevo número'
                        f' de rango inicial: '))
final = int(input(f'Por favor ingresa un rango final que no supere '
                  f'{longitud_string}: '))
while final < inicial or final > longitud_string:
    final = int(input(f'El rango final debe estar entre {inicial} y'
                      f' {longitud_string}. Por favor, ingresa un nuevo número'
                      f' de rango final: '))
# Obtener fragmento de texto a partir de un rango de índices
fragmento = oración[inicial-1:final]
print(f'El fragmento correspondiente al rango ({inicial}, {final}) es:'
      f' {fragmento}')
# Reto 5 Mayúsculas y minúsculas
palabra_1 = str(input('ingresa por favor una palabra en minúsculas: '))
# se garantiza solo mayúsculas no números
while not palabra_1.isalpha() or not palabra_1.islower():
    print('La palabra debe contener solo letras en mayúsculas: ')
    palabra_1 = str(input('Ingrese letras en mayúscula: '))
palabra_2 = str(input('ingresa por favor otra palabra en mayúsculas: '))
# se garantiza solo minúsculas y no números
while not palabra_2.isalpha() or not palabra_2.isupper():
    print('La palabra debe contener solo letras en minúsculas: ')
    palabra_2 = str(input('Ingrese letras en minúscula: '))
mayúsculas = palabra_1.upper()
minúsculas = palabra_2.lower()
print(f'La palabra: ({palabra_1}) se transforma a:{mayúsculas}, gracias al'
      f' atributo upper, la palabra ({palabra_2}) queda en: '
      f'{minúsculas}, gracias al atributo lower.')
# Reto 6 "Nombres cortos y largos"
patron = r'^[a-záéíóúüñ\s]+$'
nombre = str(input('Por favor ingresa tu nombre:'))
while not re.match(patron, nombre, flags=re.UNICODE):
    print('solo se admiten letras en minúsculas, espacios y tildes')
    nombre = str(input('Por favor ingresa de nuevo tu nombre:'))
palabras = nombre.split()
capitalizadas = [palabra.capitalize() for palabra in palabras]
nombre_capitalizado = ' '.join(capitalizadas)
if len(nombre) >= 5:
    print(f'Hola como estas {nombre_capitalizado}')
else:
    apellido = str(input('Por favor ingresa tu apellido: '))
    while not re.match(patron, apellido, flags=re.UNICODE):
        print('solo se admiten letras en minúsculas, espacios y tildes')
        apellido = str(input('Por favor ingresa de nuevo tu apellido: '))
    palabras = apellido.split()
    capitalizadas = [palabra.capitalize() for palabra in palabras]
    apellido_capitalizado = ' '.join(capitalizadas)
    print(f'Hola como estas {nombre_capitalizado} {apellido_capitalizado}')
# Reto 7 "Hablemos Pig Latin! (Puerco Latino)"
palabra = input('Ingresa una palabra que queras traducir a PigLatin: ')
vocales = ["a", "e", "i", "o", "u"]
if palabra[0].lower() in vocales:
    palabra_resultante = palabra + 'way'
else:
    primera_consonante = ''
    for letra in palabra:
        if letra.lower() not in vocales:
            primera_consonante += letra
        else:
            break
    palabra_resultante = palabra[len(primera_consonante):] + primera_consonante + 'ay'
print(f'La palabra en PigLatin es: {palabra_resultante}')
