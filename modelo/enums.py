from enum import Enum

class FaseCliente(Enum):
    EN_COLA = 1
    LEYENDO_MENU = 2
    ESPERANDO_COMIDA = 3
    COMIENDO = 4
    ESPERANDO_CUENTA = 5 
    

class EstadoMesa(Enum):
    LIBRE = 1
    OCUPADA = 2
    SUCIA = 3


class EstadoPedido(Enum):
    ANOTADO = 1
    EN_COCINA = 2
    COCINANDOSE = 3
    EN_MOSTRADOR = 4
    EN_CAMINO_A_MESA = 5
    EN_MESA = 6
    EN_BANDEJA_PARA_LAVAR = 7
    DESCARTADO = 8