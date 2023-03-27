Nombre_1 = input('Primer participante, ingresa tu nombre: ')
Edad_1 = int(input('Ingresa tu edad: '))
Nombre_2 = input('Segundo participante ingresa tu nombre: ')
Edad_2 = int(input('Ingresa tu edad: '))

if Edad_1 > Edad_2:
    print(f"{Nombre_1} es mayor que {Nombre_2}")
elif Edad_1 < Edad_2:
    print(f"{Nombre_1} es menor que {Nombre_2}")
else:
    print(f"{Nombre_1} es de la misma edad que {Nombre_2}")
