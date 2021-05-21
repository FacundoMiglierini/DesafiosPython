from Nodo import Nodo

class PopError(Exception):
    """Esta excepción se producirá cuando se intente hacer un pop de una pila
    que está vacía"""

    def __init__(self, valor):
        self.data = valor

    def __str__(self):
        return f"Info: {self.data}"

class Pila:
    
    def __init__(self, dato= None):
        if dato == None:
            self._tope = dato
            self._size = 0
        else:
            self._tope = Nodo(dato)
            self._size = 1

    def push(self, dato):
        nuevo_tope = Nodo(dato)
        nuevo_tope.sig = self._tope
        self._tope = nuevo_tope
        self._size += 1

    def pop(self):
        if self.size != 0:
            aux = self._tope
            self._tope = self._tope.sig
            self._size -= 1
            return aux
        else:
            raise PopError("Pila vacía")

    def is_empty(self):
        return self.size == 0

    @property
    def top(self):
        return self._tope

    @property
    def size(self):
        return self._size