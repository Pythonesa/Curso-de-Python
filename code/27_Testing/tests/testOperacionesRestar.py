import unittest
from operaciones import Operacioncitas as op

class TestOperacionesRestar(unittest.TestCase):
    def test_dos_enteros(self):
        resultado = op.restar(5, 2)
        self.assertEqual(resultado, 3)
        
if __name__ == '__main__':
    unittest.main()