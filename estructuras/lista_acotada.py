class ErrorListaLlena(Exception):
    pass


class ListaAcotada:
    def __init__(self,capacidad):
        self._capacidad = capacidad
        self._elementos = []


    def __len__(self):
        return len(self._elementos)


    def estaLlena(self):
        return len(self._elementos) >= self._capacidad
         


    def agregar(self,elemento):
        if self.estaLlena() == True:
            raise ErrorListaLlena("No hay espacio disponible")

        self._elementos.append(elemento)


    def eliminar(self,elemento):
        self._elementos.remove(elemento)


    def contiene(self,elemento):
        return elemento in self._elementos


 
