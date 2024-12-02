from colorama import init


class Heap:
    def __init__(self):
        self._heap = []
    def esta_vacio(self):
        return len(self._heap) == 0
    def encolar(self, dato):
        def up_heap(hijo):
            padre = abs(hijo -1) //2
            if self._heap[hijo] < self._heap[padre]:
                cambio = self._heap[padre]
                self._heap[padre] = self._heap[hijo]
                self._heap[hijo] = cambio
                up_heap(padre)
        self._heap.append(dato)
        up_heap(len(self._heap) -1)

    def ver_cima(self):
        return self._heap[0]
    
    def extraer(self):
        def down_heap(padre):
            hijo_i = 2*padre +1
            hijo_d = hijo_i +1
            if hijo_i < len(self._heap):
                hijo = hijo_i
                if hijo_d < len(self._heap):
                    if self._heap[hijo_d] < self._heap[hijo]:
                        hijo = hijo_d
                if self._heap[padre] > self._heap[hijo]:
                    dato = self._heap[padre]
                    self._heap[padre] = self._heap[hijo]
                    self._heap[hijo] = dato
                    down_heap(hijo)

        dato = self._heap[0]
        self._heap[0] = self._heap[-1]
        self._heap = self._heap[:-1]
        down_heap(0)
        return dato
        