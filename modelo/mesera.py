from estructuras.lista_acotada import ListaAcotada
from constants import BANDEJAS_EN_MANO, COMANDAS_EN_MANO

class Mesera:
    def __init__(self):
        self._bandejas = ListaAcotada(BANDEJAS_EN_MANO)
        self._comandas = ListaAcotada(COMANDAS_EN_MANO)

    @property
    def bandejas(self):
        return self._bandejas

    @property
    def comandas(self):
        return self._comandas


