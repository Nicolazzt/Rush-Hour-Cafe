from modelo.excepciones import ErrorAccionInvalida

class Caja:
    def __init__(self):
        self._dinero = 0

    @property
    def dinero(self):
        return self._dinero

    def insertar(self,monto):
        if monto <= 0:
            raise ErrorAccionInvalida("El Monto debe ser mayor a 0")

        self._dinero += monto

