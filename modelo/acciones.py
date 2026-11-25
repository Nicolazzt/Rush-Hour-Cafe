from abc import ABC, abstractmethod
from modelo.mesera import Mesera
from modelo.cliente import Cliente
from modelo.excepciones import ErrorAccionInvalida
from modelo.enums import FaseCliente
from estructuras import lista_acotada
from modelo.pedido import Pedido, EstadoPedido


class Accion(ABC):
    @abstractmethod
    def validar(self,Mesera):
        pass

    @abstractmethod
    def ejecutar(self,Mesera):
        pass


class TomarPedido(Accion):
    def __init__(self,mesa):
        self._mesa = mesa

    def validar(self,mesera):
        if self._mesa.cliente is None:
            raise ErrorAccionInvalida("La mesa se encuentra vacia")
        elif self._mesa.cliente.fase != FaseCliente.LEYENDO_MENU:
            raise ErrorAccionInvalida("Accion Invalida en este momento")
        elif mesera.comandas.estaLlena():
            raise ErrorAccionInvalida("La mesera no puede en este momento")

    def ejecutar(self, mesera):
         pedido = Pedido(self._mesa)
         mesera.comandas.agregar(pedido)

         self._mesa.cliente.siguiente_fase()
        



