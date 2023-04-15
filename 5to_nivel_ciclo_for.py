# Reto 1 "Curso favorito"
curso = input('Por favor ingresa tu curso de Platzi favorito: ')
for i in range(8):
    print(curso)
# Reto 2 "Curso favorito ‘n’ veces"
curso = input('Por favor ingresa tu curso de Platzi favorito: ')
veces = int(input('Por favor ingres el numero de veces que quieres mostrar el'
                  f' curso: '))
while veces <= 0:
    veces = int(input('Se admiten números mayores a 0, intenta de nuevo: '))
for i in range(veces):
    print(curso)
# Reto 3 "Curso en una columna"
curso = str(input('Por favor ingresa tu curso favorito de Platzi: '))
for carácter in curso:
    print(carácter)
