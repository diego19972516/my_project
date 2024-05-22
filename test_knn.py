import unittest
from knn import classify

class TestClassify(unittest.TestCase):
    def test_classify(self):
        # Caso de prueba 1: Valores de clasificación A
        result = classify(160, 70)
        self.assertEqual(result['resultado'], 'A')

        # Caso de prueba 2: Valores de clasificación B
        result = classify(25, 5)
        self.assertEqual(result['resultado'], 'B')

        # Caso de prueba 3: Valores de clasificación en el límite entre A y B
        result = classify(140, 65)
        self.assertEqual(result['resultado'], 'A')


if __name__ == '__main__':
    unittest.main()
