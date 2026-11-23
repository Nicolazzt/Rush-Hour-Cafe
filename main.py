from modelo.mesa import mesa
from modelo.pedido import pedido

p = pedido(mesa(1))
p.enviar_a_cocina()
p.descartar()
print(p.estado)       # esperado: EstadoPedido.DESCARTADO

p.descartar()         

p2 = pedido(mesa(2))
p2.enviar_a_cocina()
p2.empezar_a_cocinar()
p2.poner_en_mostrador()
p2.recoger()
p2.entregar()
p2.descartar()        # esperado: ErrorAccionInvalida (ya está en la mesa)