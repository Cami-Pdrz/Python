# Reto 1 "Suma hasta 50"
total = 0
while total <= 50:
    num = input('por favor ingresa un numero para sumar al total: ')
    if num.isdigit():
        total += int(num)
    else:
        print('error solo se admiten números')
print('la suma total es:', total)
# Reto 2 "Más allá del cuarenta y dos"
num = 0
total = 0
while num <= 42:
    num = int(input('por favor ingresa otro numero: '))
    if num <= 42:
        total += num
print('la suma total es:', total)
# Reto 3 "Sumas consecutivas"
num1 = int(input('Por favor ingresa un numero:'))
num2 = int(input('Ingresa otro numero para ser sumado con el anterior: '))
total = num1 + num2
otro_num = input('quieres sumar otro numero mas responde (s/n): ')
while otro_num == str('s'):
    num3 = int(input('Por favor ingresa un ultimo numero:'))
    total = num1 + num2 + num3
    print('la suma de los tres números es:', total)
    break
else:
    print('la suma de los dos numero es:', total)
