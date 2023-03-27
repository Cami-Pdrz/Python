def approx_sqrt(number, precision):
    """
    Esta función aproxima la raíz cuadrada de un número dado con la precisión especificada.
    """
    x = 1  # Establecemos el primer valor de la aproximación como 1.
    while True:
        y = (x + number / x) / 2  # Realizamos el cálculo de la aproximación.
        if abs(y - x) < precision:  # Comparamos la precisión deseada con la diferencia entre la aproximación actual y la anterior.
            return y  # Si se cumple la precisión deseada, devolvemos el valor de la aproximación actual.
        x = y  # Actualizamos el valor de la aproximación actual con el valor calculado.

# Solicitamos al usuario que ingrese el número y la precisión deseada.
number = int(input("Ingrese un número entero: "))
precision = float(input("Ingrese la precisión deseada: "))

# Llamamos a la función approx_sqrt para aproximar la raíz cuadrada del número ingresado.
approximation = approx_sqrt(number, precision)

# Imprimimos el resultado.
print(f"La raíz cuadrada de {number} es aproximadamente {approximation:.{len(str(precision))-2}f}")
