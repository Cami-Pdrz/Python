import re
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
