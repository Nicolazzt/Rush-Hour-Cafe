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