metodo = int(input('Hola, en este programa vamos a encontrar la raiz cuadrada de un numero, bajo tres metodos diferentes,Selecciona (1) para el metodo de Aproximacion de soluciones, (2) para el metodo de Busqueda binaria y (3) para el metodo de Enumeracion exhaustiva:  '))
if metodo == 1:
    objetivo = int(input('Escoge un numero: '))
    epsilon = 0.01
    paso = epsilon**2   
    respuesta = 0.0

    while abs(respuesta**2 - objetivo) >= epsilon and respuesta <= objetivo:  #  print(abs(respuesta**2 - objetivo), respuesta)
                respuesta += paso

                if abs(respuesta**2 - objetivo) >= epsilon:
                    print(f'No se encontro la raiz cuadrada {objetivo}')
                else:
                    print(f'La raiz cudrada de {objetivo} bajo el metodo de Aproximacion de soluciones es {respuesta}')
if metodo == 2:
    objetivo = int(input('Escoge un numero: '))
    epsilon = 0.01
    bajo = 0.0
    alto = max(1.0, objetivo)
    respuesta = (alto + bajo) / 2

    while abs(respuesta**2 - objetivo) >= epsilon:
                        print(f'bajo={bajo}, alto={alto}, respuesta={respuesta}')
                        if respuesta**2 < objetivo:
                            bajo = respuesta
                        else:
                            alto = respuesta
                            respuesta = (alto + bajo) / 2
                            print(f'La raiz cuadrada de {objetivo} bajo el metodo de Busqueda binaria es {respuesta}')
if metodo == 3:
    objetivo = int(
          input
          ('Ingresa un numero para saber su raiz cuadrada Enum exhaustiva: '))
    respuesta = 0

    while respuesta**2 < objetivo:
        print(respuesta)
        respuesta += 1
        if respuesta**2 == objetivo:
            print(f'La raiz cuadrada de {objetivo} con Enum exhaustiva es {respuesta}')
        else:
            print(f'El numero objetivo {objetivo} no tiene raiz cuadrada')