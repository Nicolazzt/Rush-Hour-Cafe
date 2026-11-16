import unittest
from estructuras.cola import Cola, ColaVaciaError

class TestCola(unittest.TestCase):
    def test_cola_vacia(self):
        c = Cola()
        self.assertTrue(c.estaVacia())
        self.assertEqual(len(c),0)

    def test_encolar_desencolar(self):
        c = Cola()
        c.encolar("Ana")
        c.encolar("Maria")
        c.encolar("Carlos")
        self.assertEqual(c.desencolar(), "Ana")
        self.assertEqual(c.desencolar(), "Maria")
        self.assertEqual(c.desencolar(), "Carlos")

    def test_desencolar_cola_vacia(self):
        c = Cola()
        with self.assertRaises(ColaVaciaError):
            c.desencolar()

    def test_ver_frente_cola_vacia_error(self):
        c = Cola()
        with self.assertRaises(ColaVaciaError):
            c.ver_frente()

    def  test_ver_frente_no_saca_al_primero(self):
        c = Cola()
        c.encolar("Ana")
        c.encolar("Luis")
        self.assertEqual(c.ver_frente(), "Ana")
        self.assertEqual(c.ver_frente(), "Ana")
        self.assertEqual(len(c), 2)

    def test_vaciar_la_cola_y_volver_a_usarla(self):
        c = Cola()
        c.encolar("Ana")
        c.desencolar()
        self.assertIsNone(c._frente)
        self.assertIsNone(c._final)
        c.encolar("Luis")
        self.assertEqual(len(c), 1)
        self.assertEqual(c.ver_frente(), "Luis")
