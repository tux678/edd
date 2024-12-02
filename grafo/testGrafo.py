from unittest import TestCase, main
from edd.grafo.grafo import Grafo, Vertice, Arista

class Test_grafo(TestCase):
    def setUp(self):
        self.g:Grafo = Grafo()
        return super().setUp()
    def test_grado(self):
        self.g.agregar_arista( Arista( Vertice('a'), Vertice('b')))
        self.assertEqual(self.g._vertices[ Vertice('b')]._grado,1)
        self.g.agregar_arista( Arista( Vertice('c'), Vertice('b')))
        self.assertEqual(self.g._vertices[ Vertice('b')]._grado,2)
        self.assertEqual(self.g._vertices[ Vertice('c')]._grado,0)
        self.assertEqual(self.g.obten_grado(),3)

    def test_existe_vertice(self):
        self.g.agregar_arista( Arista( Vertice('a'), Vertice('b')))
        self.assertTrue(self.g.existe_vertice('b'))

    def test_existe_arista(self):
        g = self.g
        g.agregar_arista( Arista( Vertice('a'), Vertice('b')))
        self.assertTrue(g.existe_arista( Arista( Vertice('a'),  Vertice('b'))))
    def test_No_existe_arista(self):
        g = self.g
        self.assertFalse(g.existe_arista( Arista( Vertice('a'),  Vertice('c'))))
        g.agregar_arista( Arista( Vertice('a'), Vertice('b')))
        self.assertFalse(g.existe_arista( Arista( Vertice('b'),  Vertice('a'))))

    def test_agregar_aristas(self):
        g = self.g
        g.agregar_aristas(('b','c'),('d','e'))
        self.g.existe_vertice( g.existe_vertice('a'))
        g.agregar_aristas_ponderadas(('x','y',1))
        self.g.existe_vertice( g.existe_vertice('x'))

    def test_orden_topologico(self):
        g:Grafo = self.g
        g.agregar_aristas(('a','b'),('a','c'),('b','c'),('b','e'),('b','g'),('c','d'),('c','e'),('d','f'),('e','d'),('e','f'),('g','f'))
        grados = g.obten_orden_topologico(lambda v:print(v))
        self.assertEqual(sum(x for x in grados.values()), 0)

    def test_dijkstra(self):
        self.g.agregar_aristas_ponderadas(('a','b',4))
        self.assertTrue(self.g.existe_vertice('a'))
        self.assertTrue(Vertice('a') in self.g._vertices.keys())
        print(self.g.obten_dijkstra(Vertice('a')))


if __name__ == '__main__':
    main()