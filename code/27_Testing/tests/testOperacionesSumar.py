import unittest
from operaciones import Operacioncitas as op

class TestOperacionesSumar(unittest.TestCase):
    def setUp (self):
        print("Antes del test")
    def tearDown (self):
        print("Despues del test")
    def test_dos_enteros(self):
        print("En el primer test")
        resultado = op.sumar([2, 5])
        self.assertEqual(resultado, 7)
    def test_tres_enteros(self):
        print("En el segundo test")
        resultado = op.sumar([2, 5, 7])
        self.assertEqual(resultado, 14)
        
if __name__ == '__main__':
    unittest.main()