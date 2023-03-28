# Creamos un diccionario con algunos alimentos y sus precios
dict_alimentos = {'carne': 10000, 'huevos': 5500, 'pan': 3500, 'arroz': 7800}

# Utilizamos un dict comprehension para crear un nuevo diccionario con el
# mismo conjunto de claves,
# pero con los valores multiplicados por 1.19 (para calcular el IVA)
dict_iva = {k: v * 1.19 for (k, v) in dict_alimentos.items()}

# Imprimimos el diccionario original y el diccionario con el IVA incluido
print(f'El valor neto de los productos es: {dict_alimentos}')
print(f'El valor con iva de los productos es: {dict_iva}')
