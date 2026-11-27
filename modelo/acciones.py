from abc import ABC, abstractmethod
from modelo.excepciones import ErrorAccionInvalida
from modelo.enums import FaseCliente
from modelo.pedido import Pedido, EstadoPedido
from modelo.cocina_mostrador import Cocina, Mostrador


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


class EntregarPlato(Accion):
    def __init__(self,mesa):
        self._mesa = mesa

    def _buscar_pedido(self,mesera):
        for pedido in mesera.bandejas:
            if pedido.mesa is self._mesa and pedido.estado == EstadoPedido.EN_CAMINO_A_MESA:
                return pedido

        return None

    def validar(self,mesera):
        if self._mesa.cliente is None:
            raise ErrorAccionInvalida("La mesa se encuentra vacia")
        
        if self._mesa.cliente.fase != FaseCliente.ESPERANDO_COMIDA:
            raise ErrorAccionInvalida("Error. Accion Invalida")
        
        if self._buscar_pedido(mesera) is None:
            raise ErrorAccionInvalida("La mesera aun no tiene el pedido de esta mesa")

    def ejecutar(self,mesera):
        pedido = self._buscar_pedido(mesera)
        mesera.bandejas.eliminar(pedido)
        pedido.entregar()

        self._mesa.cliente.siguiente_fase()


class LlevarAlTraste(Accion): #No apunta a ninguna mesa, asi que no guarda nada y no necesita __init__
    def _buscar_sucio(self,mesera):
        for pedido in mesera.bandejas:
            if pedido.estado == EstadoPedido.EN_BANDEJA_PARA_LAVAR:
                return pedido

        return None


    def validar(self,mesera):
        if self._buscar_sucio(mesera) is None:
            raise ErrorAccionInvalida("No hay ningun plato sucio")


    def ejecutar(self,mesera):
        sucio = self._buscar_sucio(mesera)
        while sucio is not None:
            mesera.bandejas.eliminar(sucio)
            sucio = self._buscar_sucio(mesera)


class DejarComandas(Accion):
    def __init__(self, cocina):
        self._cocina = cocina

    def _buscar_comanda(self,mesera):
        for pedido in mesera.comandas:
            if pedido.estado == EstadoPedido.ANOTADO:
                return pedido

        return None

    def validar(self,mesera):
        if len(mesera.comandas) == 0:
            raise ErrorAccionInvalida("La mesera no tiene comandas en mano")

    def ejecutar(self,mesera):
        comanda = self._buscar_comanda(mesera)
        while comanda is not None:
            self._cocina.pedido_a_cocina(comanda)
            mesera.comandas.eliminar(comanda)
            comanda = self._buscar_comanda(mesera)




            
        
    







