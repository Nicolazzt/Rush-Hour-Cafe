import random
from modelo.mesa import Mesa
from modelo.cliente import ClienteTranquilo
from modelo.mesera import Mesera
from modelo.caja import Caja
from modelo.cocina_mostrador import Cocina, Mostrador
from modelo.acciones import (TomarPedido, DejarComandas, RecogerPlato,
                             EntregarPlato, Cobrar, RecogerSucio, LlevarAlTraste)

def hacer(accion, mesera):
    accion.validar(mesera)      # siempre se valida primero
    accion.ejecutar(mesera)

random.seed(1)
mesera, caja = Mesera(), Caja()
mostrador = Mostrador()
cocina = Cocina(mostrador)
mesa = Mesa(1)
cliente = ClienteTranquilo()
mesa.sentar(cliente)
cliente.siguiente_fase()            # a LEYENDO_MENU (lo hará el motor)

hacer(TomarPedido(mesa), mesera)
hacer(DejarComandas(cocina), mesera)
for _ in range(100):
    cocina.actualizar(0.1)          # 10 s: el chef termina
hacer(RecogerPlato(mesa, mostrador), mesera)
hacer(EntregarPlato(mesa), mesera)
cliente.avanzar(15)                 # termina de comer y pasa a ESPERANDO_CUENTA
hacer(Cobrar(mesa, caja), mesera)
print(caja.dinero)                  # esperado: 80.0
print(mesa.estado)                  # esperado: EstadoMesa.SUCIA
hacer(RecogerSucio(mesa), mesera)
print(mesa.estado)                  # esperado: EstadoMesa.LIBRE
print(len(mesera.bandejas))         # esperado: 1
hacer(LlevarAlTraste(), mesera)
print(len(mesera.bandejas))         # esperado: 0