import math
from typing import ForwardRef, Callable, Self

from edd.cola.cola import Cola
from edd.heap.heap import Heap

class GrafoException(Exception):
    pass

class Vertice:
    def __init__(self, id):
        self._id = id
        self._grado = 0
        self._aristas:set[tuple[Vertice, int | float | None]] = set()

    def __hash__(self):
        return hash(self._id)
    
    def __eq__(self, value):
        if not isinstance(value, Vertice):
            return False
        return self._id.__eq__(value._id)
    
    def __gt__(self, value):
        if not isinstance(value, Vertice):
            return True
        return self._id.__gt__(value._id)
    
    def __lt__(self, value):
        if not isinstance(value, Vertice):
            return True
        return self._id.__lt__(value._id)
    

    def _agregar_arista(self, arista:'Arista'):
        adyacente = (arista._vertice_destino, arista._peso)
        if adyacente in self._aristas:
            raise GrafoException("La Arista ya existe")
        self._aristas.add(adyacente)
    
    def __str__(self):
        return str(self._id)

    
class Arista:
    def __init__(self, vertice_origen:Vertice, vertice_destino:Vertice, peso:int | float | None = None):
        self._vertice_origen = vertice_origen
        self._vertice_destino = vertice_destino
        self._peso = peso

    def __eq__(self, value):
        if not isinstance(value, Arista):
            return False
        return self._vertice_origen.__eq__(value._vertice_origen) and self._vertice_destino.__eq__(value._vertice_destino)



class Grafo:
    def __init__(self):
        self._vertices:dict[Vertice,Vertice] = {}
    def agregar_arista(self, arista:Arista):
        vertice_origen = self._vertices.setdefault(arista._vertice_origen, arista._vertice_origen)
        vertice_destino = self._vertices.setdefault(arista._vertice_destino, arista._vertice_destino)
        try:
            vertice_origen._agregar_arista(Arista(vertice_origen, vertice_destino, arista._peso))
        except GrafoException as e:
            raise e
        else:
            vertice_destino._grado += 1

    def existe_vertice(self, id) -> bool:
        return Vertice(id) in self._vertices.keys()
    
    def obten_aristas(self, id) -> set[Arista]:
        v = self._vertices[Vertice(id)]

        return {Arista(v, w, p) for w,p in v._aristas }
    
    def existe_arista(self, arista:Arista) -> bool:
        v = self._vertices.get(arista._vertice_origen, None)
        if v is None:
            return False
        a = arista._vertice_destino, arista._peso
        return a in v._aristas
    
    def agregar_aristas(self, *aristas):
        for v, w in aristas:
            self.agregar_arista(Arista(Vertice(v),Vertice(w)))

    def agregar_aristas_ponderadas(self, *aristas):
        for v, w, p in aristas:
            self.agregar_arista(Arista(Vertice(v),Vertice(w), p))

    def obten_grado(self):
        return len(self._vertices)
    
    def obten_adyacentes(self, id) -> set[tuple[Vertice, int | float | None]]:
        return self._vertices[Vertice(id)]._aristas

    def obten_orden_topologico(self, visitar:Callable[[Vertice],None]) ->dict[Vertice, int]:
        cola_ceros = Cola()

        grados:dict[Vertice, int] = {v:v._grado for v in self._vertices.values()}

        cola_ceros._cola = [v for v in self._vertices.keys() if v._grado == 0]

        while not cola_ceros.esta_vacia():
            v:Vertice = cola_ceros.extraer()
            visitar(v)
            for w,_ in v._aristas:
                grados[w] -= 1
                if grados[w] == 0:
                    cola_ceros.encolar(w)

        return grados
    
    def obten_dijkstra(self, s:Vertice) ->tuple[dict[Vertice, int |float],dict[Vertice,Vertice|None]]:
        inicio = self._vertices[s]
        origen:dict[Vertice, Vertice] = {}
        distancias:dict[Vertice, int | float] = {}
        visitados:set[Vertice] = set()
        pq = Heap()
        
        for v in self._vertices.keys():
            origen[v] = None
            distancias[v] = math.inf
        distancias[inicio] = 0
        pq.encolar((0,inicio))

        while not pq.esta_vacio():
            distancia, v = pq.extraer()
            visitados.add(v)
            adyacentes = self._vertices[v]._aristas
            for w, peso in adyacentes:
                if w not in visitados:
                    if (distancia+peso) < distancias[w]:
                        distancias[w] = distancia+peso
                        origen[w] = v
                        pq.encolar((distancia+peso, w))
        
        return distancias, origen
    
    def imprimir_dijkstra(dijkstra:Callable[[Vertice],tuple[dict[Vertice, int |float],dict[Vertice,Vertice|None]]]):
        def imprimir(self, inicio:Vertice):
            costos, origenes = dijkstra(self, inicio)
            del origenes[inicio]
            destinos = {o:d for d,o in origenes.items() }
            def recorrer(i:Vertice, recorrido:list):
                if (origen := destinos.get(i,i)) != i:
                    recorrido.append((str(origen), costos[origen]))
                    recorrer(origen, recorrido)
            camino=[]
            recorrer(inicio,camino)
            print(camino)
        return imprimir

    @imprimir_dijkstra
    def _obten_dijkstra(self, i:Vertice):
        return self.obten_dijkstra(i)
            