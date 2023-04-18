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