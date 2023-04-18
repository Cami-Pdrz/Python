# Reto1 "Suma hasta 50"
total = 0
while total <= 50:
    num = input('por favor ingresa un numero para sumar al total: ')
    if num.isdigit():
        total += int(num)
    else:
        print('error solo se admiten números')
print('la suma total es:', total)
