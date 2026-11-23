from modelo.mesa import mesa
from modelo.cliente import ClienteTranquilo

m = mesa(1)
print(m.estado)          # esperado: EstadoMesa.LIBRE
print(m.cliente)         # esperado: None

c = ClienteTranquilo()
m.sentar(c)
print(m.estado)          # esperado: EstadoMesa.OCUPADA
print(m.cliente is c)    # esperado: True

m.sentar(ClienteTranquilo())    # esperado: ErrorMesaOcupada