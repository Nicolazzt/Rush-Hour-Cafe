import random
from modelo.mesa import Mesa
from modelo.pedido import Pedido
from modelo.mesera import Mesera
from modelo.acciones import RecogerPlato
from modelo.cocina_mostrador import Cocina, Mostrador

mesera = Mesera()
mostrador = Mostrador()
cocina = Cocina(mostrador)
m1, m2, m3 = Mesa(1), Mesa(2), Mesa(3)
p1, p2, p3 = Pedido(m1), Pedido(m2), Pedido(m3)
for p in (p1, p2, p3):
    cocina.pedido_a_cocina(p)

random.seed(1)
for _ in range(300):
    cocina.actualizar(0.1)

a = RecogerPlato(m2, mostrador)
a.validar(mesera)                  # esperado: no pasa nada
a.ejecutar(mesera)
print(len(mesera.bandejas))        # esperado: 1
print(p1.estado, p2.estado, p3.estado)
# esperado: EN_MOSTRADOR EN_CAMINO_A_MESA EN_MOSTRADOR
a.validar(mesera)                  # esperado: ErrorAccionInvalida