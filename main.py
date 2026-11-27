import random
from modelo.mesa import Mesa
from modelo.pedido import Pedido
from modelo.mesera import Mesera
from modelo.acciones import DejarComandas
from modelo.cocina_mostrador import Cocina, Mostrador

mesera = Mesera()
cocina = Cocina(Mostrador())
p1, p2 = Pedido(Mesa(1)), Pedido(Mesa(2))
mesera.comandas.agregar(p1)
mesera.comandas.agregar(p2)

a = DejarComandas(cocina)
a.validar(mesera)                  # esperado: no pasa nada
a.ejecutar(mesera)
print(len(mesera.comandas))        # esperado: 0
print(p1.estado, p2.estado)        # esperado: EN_COCINA EN_COCINA

random.seed(1)
for _ in range(200):
    cocina.actualizar(0.1)         # 20 segundos simulados
print(p1.estado, p2.estado)        # esperado: EN_MOSTRADOR EN_MOSTRADOR
a.validar(mesera)                  # esperado: ErrorAccionInvalida