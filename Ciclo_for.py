def approx_sqrt(number, precision):
    """
    Esta función aproxima la raíz cuadrada de un número dado con la precisión especificada.
    """
    x = int(input('Por favor ingresa un numero entero: '))  # Establecemos el primer valor de la aproximación como 1.
    while True:
        y = (x + number / x) / 2  # Realizamos el cálculo de la aproximación.
        if abs(y - x) < precision:  # Comparamos la precisión deseada con la diferencia entre la aproximación actual y la anterior.
            return y  # Si se cumple la precisión deseada, devolvemos el valor de la aproximación actual.
        x = y  # Actualizamos el valor de la aproximación actual con el valor calculado.
        print(y)z