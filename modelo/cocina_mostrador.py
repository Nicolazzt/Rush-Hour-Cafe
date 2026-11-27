from modelo.mesa import Mesa
from modelo.pedido import Pedido
from modelo.enums import EstadoPedido
from estructuras.cola import Cola
import random

class Mostrador:
    def __init__(self):
        self._pedidos = []


    def agregar(self,pedido):
        self._pedidos.append(pedido)


    def buscar_por_mesa(self,mesa):
        for pedido in self._pedidos:
            if pedido.mesa is mesa and pedido.estado == EstadoPedido.EN_MOSTRADOR:
                return pedido

        return None


    def retirar_plato(self,pedido):
        self._pedidos.remove(pedido)

class Cocina:
    def __init__(self,mostrador):
        self._mostrador = mostrador
        self._pedido_actual = None
        self._cola = Cola()
        self._tiempo_coccion = None

    def pedido_a_cocina(self,pedido):
        pedido.enviar_a_cocina()
        self._cola.encolar(pedido)


    def arrancar_coccion(self):
        while not self._cola.estaVacia() and self._cola.ver_frente().estado == EstadoPedido.DESCARTADO:
            self._cola.desencolar()

        if not self._cola.estaVacia():
            self._pedido_actual = self._cola.desencolar()
            self._pedido_actual.empezar_a_cocinar()
            self._tiempo_coccion = random.uniform(3.0,5.0)

    def actualizar(self,seg_transcurridos):
        if self._pedido_actual is None:
            self.arrancar_coccion()
            return 

        if self._pedido_actual.estado == EstadoPedido.DESCARTADO:
            self._pedido_actual = None
            self._tiempo_coccion = None
            return 

        self._tiempo_coccion -= seg_transcurridos

        if self._tiempo_coccion <= 0:
            self._pedido_actual.poner_en_mostrador()
            self._mostrador.agregar(self._pedido_actual)
            self._pedido_actual = None
            self._tiempo_coccion = None


        

