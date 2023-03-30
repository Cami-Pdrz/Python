import unittest


def calcular_descuento(cantidad_artículos):
    """
    Calcula el descuento a aplicar en función de la cantidad de \n
    artículos comprados.
    """
    if cantidad_artículos >= 10:
        descuento = 0.2
    elif cantidad_artículos >= 5:
        descuento = 0.1
    else:
        descuento = 0.0
    return descuento


class PruebaCajaCristal(unittest.TestCase):
    """
    Clase de prueba para la función "calcular_descuento".
    """

    def test_descuento_cero(self):
        """
        Prueba que se devuelve un descuento del 0% para una cantidad de\n
        artículos menor que 5.
        """
        descuento = calcular_descuento(3)
        self.assertEqual(descuento, 0.0)

    def test_descuento_diez(self):
        """
        Prueba que se devuelve un descuento del 10% para una cantidad de \n
        artículos entre 5 y 9.
        """
        descuento = calcular_descuento(7)
        self.assertEqual(descuento, 0.1)

    def test_descuento_veinte(self):
        """
        Prueba que se devuelve un descuento del 20% para una cantidad de \n
        artículos igual o mayor que 10.
        """
        descuento = calcular_descuento(12)
        self.assertEqual(descuento, 0.2)


if __name__ == '__main__':
    unittest.main()
