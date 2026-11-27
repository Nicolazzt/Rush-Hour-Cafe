from modelo.enums import EstadoMesa
from modelo.excepciones import ErrorMesaOcupada

class Mesa:
    def __init__(self, numero):
        self._estado = EstadoMesa.LIBRE
        self._numero = numero
        self._cliente = None
        self._pedido_en_mesa = None


    @property
    def estado(self):
        return self._estado

    @property
    def pedido_en_mesa(self):
        return self._pedido_en_mesa

    @property
    def numero(self):
        return self._numero


    @property
    def cliente(self):
        return self._cliente

    
    def sentar(self, cliente):
        if self._estado != EstadoMesa.LIBRE:
            raise ErrorMesaOcupada("Mesa no disponible")
        else:
            self._estado = EstadoMesa.OCUPADA
            self._cliente = cliente

    def liberar(self):
        self._estado = EstadoMesa.LIBRE
        self._cliente = None
        self._pedido_en_mesa = None

    def ensuciar(self):   
        self._estado = EstadoMesa.SUCIA
        self._cliente = None

    def asignar_pedido(self,pedido):
        self._pedido_en_mesa = pedido


