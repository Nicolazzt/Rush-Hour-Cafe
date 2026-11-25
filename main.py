from modelo.mesa import Mesa
from modelo.cliente import ClienteTranquilo
from modelo.mesera import Mesera
from modelo.acciones import TomarPedido

m = Mesa(1)
c = ClienteTranquilo()
m.sentar(c)
c.siguiente_fase()           # a mano: lo pasa a LEYENDO_MENU

mesera = Mesera()
a = TomarPedido(m)
a.validar(mesera)            # esperado: no pasa nada
a.ejecutar(mesera)
print(len(mesera.comandas))  # esperado: 1
print(c.fase)                # esperado: FaseCliente.ESPERANDO_COMIDA
a.validar(mesera)            # esperado: ErrorAccionInvalida