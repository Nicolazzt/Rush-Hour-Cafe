from modelo.enums import EstadoMesa
from modelo.excepciones import ErrorMesaOcupada

class mesa:
    def __init__(self, numero):
        self._estado = EstadoMesa.LIBRE
        self._numero = numero
        self._cliente = None


    @property
    def estado(self):
        return self._estado


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

    def ensuciar(self):   
        self._estado = EstadoMesa.SUCIA
        self._cliente = None


