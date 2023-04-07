import re
patron = r'^[a-záéíóúüñ\s]+$'
nombre = str(input('Por favor ingresa tu nombre:'))
while not re.match(patron, nombre, flags=re.UNICODE):
    print('solo se admiten letras en minúsculas, espacios y tildes')
    nombre = str(input('Por favor ingresa de nuevo tu nombre:'))
if len(nombre) >= 5:
    print(f'Hola como estas {nombre}')
else:
    apellido = str(input('Por favor ingresa tu apellido: '))
    while not re.match(patron, apellido, flags=re.UNICODE):
        print('solo se admiten letras en minúsculas, espacios y tildes')
        apellido = str(input('Por favor ingresa de nuevo tu apellido: '))
    print(f'Hola como estas {nombre} {apellido}')
