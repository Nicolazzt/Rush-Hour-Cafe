class ErrorColaVacia(Exception):
    pass


class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None


class Cola:
    def __init__(self):
        self._frente=None
        self._final=None
        self._tamano=0

    def estaVacia(self):
        if self._tamano == 0:
            return True
        else:
            return False

    def encolar(self,dato):
        nuevo = Nodo(dato)
        if self.estaVacia() == True:
            self._frente = nuevo
            self._final = nuevo
        else:
            self._final.siguiente = nuevo
            self._final = nuevo

        self._tamano += 1

    def desencolar(self): #self._final = None
        if self.estaVacia():
            raise ErrorColaVacia("La cola esta vacía")
        else:
            temp = self._frente
            self._frente = self._frente.siguiente
            x = temp.dato

            if self._frente == None:
                self._final = None

        self._tamano -= 1

        return x

    def ver_frente(self):
        if self.estaVacia():
            raise ErrorColaVacia("La cola esta vacía")

        return self._frente.dato

    def __len__(self):
        return self._tamano


    