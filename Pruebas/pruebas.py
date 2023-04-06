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
