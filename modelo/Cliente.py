from abc import ABC, abstractmethod
from constants import (PROPINA_EXCELENTE,PROPINA_NORMAL,UMBRAL_EXCELENTE,UMBRAL_NORMAL)
from modelo.enums import FaseCliente

class cliente(ABC):
    def __init__(self):
       self._fase = FaseCliente.EN_COLA
       self._tiempo_restante_de_fase = self.TIEMPOS_FASE[self._fase]
       self._porcentajes_paciencia = []
       self._se_fue = False

    @abstractmethod
    def calcular_propina(self,satisfaccion):
        pass


    def avanzar(self, seg_transcurridos):
        if self._se_fue == True:
            return 

        self._tiempo_restante_de_fase -= seg_transcurridos

        if self._tiempo_restante_de_fase <= 0 and self._fase != FaseCliente.COMIENDO:
            self._se_fue = True
        elif self._tiempo_restante_de_fase <= 0:
            self.siguiente_fase()

        
    def siguiente_fase(self):
        if self._fase != FaseCliente.COMIENDO:
            porcentaje = (self._tiempo_restante_de_fase / self.TIEMPOS_FASE[self._fase]) * 100

            self._porcentajes_paciencia.append(porcentaje)

        if self._fase != FaseCliente.ESPERANDO_CUENTA:
            self._fase = FaseCliente(self._fase.value + 1)
            self._tiempo_restante_de_fase = self.TIEMPOS_FASE[self._fase]


    def satisfaccion(self):
        if not self._porcentajes_paciencia:
            return 0
        
        return sum(self._porcentajes_paciencia)/len(self._porcentajes_paciencia)



class ClienteTranquilo(cliente):
    TIEMPOS_FASE= {
        FaseCliente.EN_COLA: 25,
        FaseCliente.LEYENDO_MENU: 12,
        FaseCliente.ESPERANDO_COMIDA: 45,
        FaseCliente.COMIENDO: 15,
        FaseCliente.ESPERANDO_CUENTA: 20
    }


    def calcular_propina(self,satisfaccion):
        if satisfaccion > UMBRAL_EXCELENTE:
            base = PROPINA_EXCELENTE
        elif satisfaccion >= UMBRAL_NORMAL:
            base = PROPINA_NORMAL
        else:
            base = 0
        return base * 1.0


class ClienteExigente(cliente):
    TIEMPOS_FASE= {
        FaseCliente.EN_COLA: 15,
        FaseCliente.LEYENDO_MENU: 8,
        FaseCliente.ESPERANDO_COMIDA: 0,
        FaseCliente.COMIENDO: 12,
        FaseCliente.ESPERANDO_CUENTA: 12
    }

        
    def calcular_propina(self,satisfaccion):
        if satisfaccion > UMBRAL_EXCELENTE:
            return PROPINA_EXCELENTE * 2.0

class ClienteApurado(cliente):
    TIEMPOS_FASE= {
        FaseCliente.EN_COLA: 10,
        FaseCliente.LEYENDO_MENU: 5,
        FaseCliente.ESPERANDO_COMIDA: 20,
        FaseCliente.COMIENDO: 9,
        FaseCliente.ESPERANDO_CUENTA: 8
    }


    def calcular_propina(self,satisfaccion):
        if satisfaccion < UMBRAL_NORMAL:
            return 0
        return PROPINA_EXCELENTE * 3.0 * (satisfaccion/100)

