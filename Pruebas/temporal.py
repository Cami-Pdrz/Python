import re

patron = r'^[a-záéíóúüñ\s]+$'

nombre = input('Por favor ingresa tu nombre en minúsculas: ')
while not re.match(patron, nombre):
    print('Solo se admiten minúsculas, espacios y tildes')
    nombre = input('Por favor ingresa tu nombre en minúsculas: ')

apellido = input('Por favor ingresa tu apellido en minúsculas: ')
while not re.match(patron, apellido):
    print('Solo se admiten minúsculas, espacios y tildes')
    apellido = input('Por favor ingresa tu apellido en minúsculas: ')

pais = input('Por favor ingresa tu pais de origen en minúsculas: ')
while not re.match(patron, pais):
    print('Solo se admiten minúsculas, espacios y tildes')
    pais = input('Por favor ingresa tu pais de origen en minúsculas: ')

# Separamos el nombre completo en palabras individuales
palabras = nombre.split()

# Iteramos sobre cada palabra y capitalizamos la primera letra
capitalizads = [palabra.capitalize() for palabra in palabras]

# Unimos las palabras capitalizadas en un solo string
nombre_capi = ' '.join(capitalizads)

# Hacemos lo mismo para el apellido
palabras = apellido.split()
capitalizads = [palabra.capitalize() for palabra in palabras]
apellido_capi = ' '.join(capitalizads)

# Hacemos lo mismo para el país de origen
palabras = pais.split()
capitalizads = [palabra.capitalize() for palabra in palabras]
pais_capi = ' '.join(capitalizads)

print(f'Nombre: {nombre_capi}')
print(f'Apellido: {apellido_capi}')
print(f'País de origen: {pais_capi}')