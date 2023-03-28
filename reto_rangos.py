""" Range que imprime números impares
range(inicio, final, incremento)"""
inicio = int(input("Escribe un numero inicial: "))
final = int(input('Escribe un numero final: '))
incremento = int(input('Escribe el numero de incremento: '))
for i in range(inicio, final, incremento):
    print(i)
