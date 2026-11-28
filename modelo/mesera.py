from estructuras.lista_acotada import ListaAcotada
from constants import BANDEJAS_EN_MANO, COMANDAS_EN_MANO,TIEMPO_VIAJE
from estructuras.cola import Cola
from modelo.excepciones import ErrorAccionInvalida

class Mesera:
    def __init__(self):
        self._bandejas = ListaAcotada(BANDEJAS_EN_MANO)
        self._comandas = ListaAcotada(COMANDAS_EN_MANO)
        self._cola_acciones = Cola()
        self._accion_actual = None
        self._tiempo_restante_accion = None

    @property
    def bandejas(self):
        return self._bandejas

    @property
    def comandas(self):
        return self._comandas

    def encolar_accion(self,accion):
        accion.validar(self)
        if len(self._cola_acciones) == 5:
            raise ErrorAccionInvalida("Error. Cola de acciones llena")

        self._cola_acciones.encolar(accion)

    def _se_puede(self, accion):
        try:
            accion.validar(self)
            return True
        except ErrorAccionInvalida:
            return False

    def actualizar(self, seg_transcurridos):
        while self._accion_actual is None and len(self._cola_acciones) > 0:
            accion = self._cola_acciones.desencolar()
            if self._se_puede(accion):
                self._accion_actual = accion
                self._tiempo_restante_accion = TIEMPO_VIAJE

        if self._accion_actual is not None:
            self._tiempo_restante_accion -= seg_transcurridos
            if self._tiempo_restante_accion <= 0:
                if self._se_puede(self._accion_actual):
                    self._accion_actual.ejecutar(self)
                self._accion_actual = None


            

            


