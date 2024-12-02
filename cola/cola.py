from typing import Any


class ColaException(Exception):
    pass
class Cola:
    def __init__(self):
        self._cola = []
    def encolar(self, dato):
        self._cola.append(dato)
    def extraer(self) -> Any:
        if self.esta_vacia():
            raise ColaException
        return self._cola.pop(0)
    def esta_vacia(self) -> bool:
        return len(self._cola) == 0
    