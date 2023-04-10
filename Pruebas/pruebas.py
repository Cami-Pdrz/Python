
palabra = input('Ingresa una palabra que queras traducir a PigLatin: ')
vocales = ["a", "e", "i", "o", "u"]
if palabra[0].lower() in vocales:
    palabra_resultante = palabra + 'way'
else:
    primera_consonante = ''
    for letra in palabra:
        if letra.lower() not in vocales:
            primera_consonante += letra
        else:
            break
    palabra_resultante = palabra[len(primera_consonante):] + primera_consonante + 'ay'
print(f'La palabra en PigLatin es: {palabra_resultante}')
