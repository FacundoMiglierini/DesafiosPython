class Nodo:

    def __init__(self, dato):
        self._dato = dato
        self._sig = None

    @property
    def dato(self):
        return self._dato

    @dato.setter
    def dato(self, dato):
        self._dato = dato

    @property
    def sig(self):
        return self._sig

    @sig.setter
    def sig(self, nodo):
        self._sig = nodo