<<<<<<< HEAD
import re
nombre = input('Por favor ingresa tu nombre: ')
apellido = input('Por favor ingresa tu apellido: ')
comida = input('Por favor ingresa tu comida favorita: ')
while not re.match("^[\\w ]+$", apellido, flags=re.UNICODE):
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
=======

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
>>>>>>> Tercer-nivel-manipulando-strings
