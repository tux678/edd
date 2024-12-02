from unittest import TestCase, main
from cola import Cola

class Test_Cola(TestCase):
    def setUp(self):
        self.c = Cola()
        return super().setUp()
    
    def test_cola_vacia(self):
        self.assertTrue(self.c.esta_vacia())
        self.c.encolar('a')
        self.assertFalse(self.c.esta_vacia())

    def test_desencolar(self):
        self.c.encolar('a')
        self.assertEqual(self.c.extraer(), 'a')
        self.assertTrue(self.c.esta_vacia())
        self.c.encolar('a')
        self.c.encolar('b')
        self.assertEqual(self.c.extraer(), 'a')
        self.assertEqual(self.c.extraer(), 'b')

if __name__ == "__main__":
    main()