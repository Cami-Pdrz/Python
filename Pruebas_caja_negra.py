import unittest


def sumar(a, b):
    """
    Función que toma dos números como argumentos y devuelve su suma.

    Args:
        a (int): El primer número a sumar.
        b (int): El segundo número a sumar.

    Returns:
        int: La suma de los dos números.

    """
    return a + b


class TestSumar(unittest.TestCase):
    """
    Clase que define las pruebas unitarias para la función 'sumar'.
    """
    def test_suma_positiva(self):
        """
        Método de prueba que comprueba que la función 'sumar' devuelve la \n
        suma correcta para dos números positivos.
        """
        self.assertEqual(sumar(2, 3), 5)

    def test_suma_negativa(self):
        """
        Método de prueba que comprueba que la función 'sumar' devuelve la \n
        suma correcta para dos números negativos.
        """
        self.assertEqual(sumar(-2, -3), -5)

    def test_suma_cero(self):
        """
        Método de prueba que comprueba que la función 'sumar' devuelve \n
        el número correcto cuando se suma cero a cualquier número.
        """
        self.assertEqual(sumar(0, 0), 0)


if __name__ == '__main__':
    """
    Si este archivo se está ejecutando como un programa independiente,
    ejecutar todas las pruebas unitarias definidas en este archivo \n
    utilizando el módulo unittest.
    """
unittest.main()
