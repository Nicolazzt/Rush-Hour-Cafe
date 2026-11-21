from abc import ABC, abstractmethod
from constants import (PROPINA_EXCELENTE,PROPINA_NORMAL,UMBRAL_EXCELENTE,UMBRAL_NORMAL)
from modelo.enums import FaseCliente

class Cliente(ABC):
    def __init__(self):
       self._fase = FaseCliente.EN_COLA

    @abstractmethod
    def calcular_propina(self,satisfaccion):
        pass


class ClienteTranquilo(Cliente):
    def calcular_propina(self,satisfaccion):
        if satisfaccion > UMBRAL_EXCELENTE:
            base = PROPINA_EXCELENTE
        elif satisfaccion >= UMBRAL_NORMAL:
            base = PROPINA_NORMAL
        else:
            base = 0
        return base * 1.0


class ClienteExigente(Cliente):
    def calcular_propina(self,satisfaccion):
        if satisfaccion > UMBRAL_EXCELENTE:
            return PROPINA_EXCELENTE * 2.0

class ClienteApurado(Cliente):
    def calcular_propina(self,satisfaccion):
        if satisfaccion < UMBRAL_NORMAL:
            return 0
        return PROPINA_EXCELENTE * 3.0 * (satisfaccion/100)

