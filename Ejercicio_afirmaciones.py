# assert <expresion  booleana>, <mensaje de error>
def primera_letra(lista_de_palabras):
    primeras_letras = []

    for palabra in lista_de_palabras:
        assert type(palabra) == str, f'{palabra} no es un str'
        assert len(palabra) > 0, 'no se permite str vacios'

        primeras_letras.append(palabra[0])
    return primeras_letras
