from modelo.mesa import Mesa
from estructuras.cola import Cola
from modelo.cocina_mostrador import Mostrador,Cocina
from modelo.mesera import Mesera
from modelo.caja import Caja

class Cafeteria:
    def __init__(self,num_mesas):
        self._mesas = []
        for numero in range(1, num_mesas+1):
            self._mesas.append(Mesa(numero))
        self._fila_puerta = Cola()
        self._mostrador = Mostrador()
        self._cocina_cafeteria = Cocina(self._mostrador)
        self._mesera = Mesera()
        self._caja = Caja()

    @property
    def mesas(self):
        return self._mesas

    @property
    def fila_puerta(self):
        return self._fila_puerta

    @property
    def mostrador(self):
        return self._mostrador

    @property
    def cocina(self):
        return self._cocina_cafeteria

    @property
    def mesera(self):
        return self._mesera

    @property
    def caja(self):
        return self._caja