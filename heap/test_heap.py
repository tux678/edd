from unittest import TestCase, main
from edd.heap.heap import Heap

class Test_heap(TestCase):
    def setUp(self):
        self.h = Heap()
        return super().setUp()
    
    def test_heap_vacio(self):
        self.assertTrue(self.h.esta_vacio())
        self.h.encolar('a')
        self.assertFalse(self.h.esta_vacio())

    def test_encolar(self):
        self.h.encolar('a')
        self.assertEqual(self.h.ver_cima(),'a')

    def test_extraer(self):
        self.h.encolar('a')
        self.assertEqual(self.h.extraer(),'a')
        self.assertTrue(self.h.esta_vacio())
        self.h.encolar('a')
        self.h.encolar('b')
        self.assertEqual(self.h.extraer(),'a')
        self.assertEqual(self.h.extraer(),'b')
        self.h.encolar('c')
        self.h.encolar('b')
        self.assertEqual(self.h.extraer(),'b')
        self.h.encolar('c')
        self.h.encolar('x')
        self.h.encolar('b')
        self.h.encolar('l')
        self.assertEqual(self.h.extraer(),'b')
        self.assertEqual(self.h.extraer(),'c')
        self.assertEqual(self.h.extraer(),'c')
        self.assertEqual(self.h.extraer(),'l')
        self.assertEqual(self.h.extraer(),'x')
    def test_con_clases(self):
        class Calderon:
            def __init__(self, nombre, edad):
                self.nombre:str = nombre
                self.edad = edad
            def __hash__(self):
                return hash(self.nombre)
            def __eq__(self, value):
                if not isinstance(value, Calderon):
                    return False
                return self.nombre.__eq__(value.nombre)
            def __gt__(self, value):
                if not isinstance(value, Calderon):
                    return True
                if self.nombre > value.nombre:
                    return True
                return False
            
            def __lt__(self, value):
                if not isinstance(value, Calderon):
                    return True
                if self.nombre < value.nombre:
                    return True
                return False
        mate = Calderon("Mateo",7)
        mati = Calderon("Matias",20)
        agus = Calderon("Agus", 14)
        self.h.encolar(mate)
        self.h.encolar(agus)
        self.h.encolar(mati)
        self.assertEqual(self.h.extraer(),agus)
        self.assertEqual(self.h.extraer(),mate)

    def test_con_tuplas(self):
        self.h.encolar(('mate',7))
        self.h.encolar(('agus',14))
        self.assertTupleEqual(self.h.extraer(),('agus',14))
        self.assertTupleEqual(self.h.extraer(),('mate',7))
        self.h.encolar((14,'agus'))
        self.h.encolar((7,'mate'))
        self.h.encolar((20,'mati'))
        self.assertTupleEqual(self.h.extraer(),(7,'mate'))
        self.assertTupleEqual(self.h.extraer(),(14,'agus'))
        self.assertTupleEqual(self.h.extraer(),(20,'mati'))

if __name__ == "__main__":
    main()
