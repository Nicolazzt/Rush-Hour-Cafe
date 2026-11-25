from modelo.enums import EstadoPedido
from modelo.excepciones import ErrorAccionInvalida

class Pedido:
    ESTADOS_DESCARTABLES = (EstadoPedido.ANOTADO,EstadoPedido.EN_COCINA,EstadoPedido.COCINANDOSE,EstadoPedido.EN_MOSTRADOR,EstadoPedido.EN_CAMINO_A_MESA)
    def __init__(self, mesa):
        self._estado = EstadoPedido.ANOTADO
        self._mesa = mesa

    @property
    def estado(self):
        return self._estado

    @property
    def mesa(self):
        return self._mesa

    def _cambiar_estado(self,estado_requerido,nuevoEstado,accion):
        if self._estado != estado_requerido:
            raise ErrorAccionInvalida(f"No se puede {accion} un pedido en estado {self._estado.name}")

        self._estado = nuevoEstado

    def enviar_a_cocina(self):
        self._cambiar_estado(EstadoPedido.ANOTADO, EstadoPedido.EN_COCINA, "enviar a cocina")

    def empezar_a_cocinar(self):
        self._cambiar_estado(EstadoPedido.EN_COCINA,EstadoPedido.COCINANDOSE, "empezar a cocinar")

    def poner_en_mostrador(self):
        self._cambiar_estado(EstadoPedido.COCINANDOSE,EstadoPedido.EN_MOSTRADOR, "poner en el mostrador")

    def recoger(self):
        self._cambiar_estado(EstadoPedido.EN_MOSTRADOR,EstadoPedido.EN_CAMINO_A_MESA, "recoger")

    def entregar(self):
            self._cambiar_estado(EstadoPedido.EN_CAMINO_A_MESA,EstadoPedido.EN_MESA, "entregar")

    def retirar_sucio(self):
            self._cambiar_estado(EstadoPedido.EN_MESA,EstadoPedido.EN_BANDEJA_PARA_LAVAR, "retirar el plato de")

    def descartar(self):
         if self._estado not in self.ESTADOS_DESCARTABLES:
              raise ErrorAccionInvalida(f"No se puede descartar un plato en {self._estado.name}")

         self._estado = EstadoPedido.DESCARTADO

    