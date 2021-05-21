import unittest
from Nodo import Nodo
from Pila import PopError
from FuncionesPila import crear_pila_con_datos, crear_pila_vacia

class TestPila(unittest.TestCase):

    def test_case1(self):
        """ Testea que el valor size sea 0 cuando la pila está vacía """

        obj = crear_pila_vacia()

        self.assertTrue(obj.is_empty())

    def test_case2(self):
        """ Testea que el tope tenga valor None cuando la pila está vacía"""

        obj = crear_pila_vacia()

        self.assertIsNone(obj.top)

    def test_case3(self):
        """ Testea que el tope no tenga valor None cuando la pila no está vacía"""

        obj = crear_pila_con_datos()

        self.assertIsNotNone(obj)

    def test_case4(self):
        """ Testea que el tope sea una instancia de la clase Nodo cuando la
        pila no está vacía"""

        obj = crear_pila_con_datos()
        self.assertIsInstance(obj.top, Nodo)

    def test_case5(self):
        """ Testea que se levante la excepción PopError cuando se intente hacer
        un pop de una pila vacía """

        obj = crear_pila_vacia()
        
        with self.assertRaises(PopError):
            obj.pop()

if __name__ == '__main__':
    unittest.main()