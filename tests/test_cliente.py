import unittest
from modelo.cliente import (Cliente, ClienteTranquilo,
                            ClienteExigente, ClienteApurado)
from modelo.enums import FaseCliente


class TestCliente(unittest.TestCase):

    def test_cliente_abstracto_no_se_instancia(self):
        with self.assertRaises(TypeError):
            Cliente()

    def test_nacen_en_cola(self):
        for clase in (ClienteTranquilo, ClienteExigente, ClienteApurado):
            self.assertEqual(clase()._fase, FaseCliente.EN_COLA)

    def test_tranquilo(self):
        c = ClienteTranquilo()
        self.assertAlmostEqual(c.calcular_propina(80), 30)
        self.assertAlmostEqual(c.calcular_propina(50), 10)
        self.assertAlmostEqual(c.calcular_propina(20), 0)

    def test_exigente(self):
        c = ClienteExigente()
        self.assertAlmostEqual(c.calcular_propina(80), 60)
        self.assertAlmostEqual(c.calcular_propina(50), 0)
        self.assertAlmostEqual(c.calcular_propina(20), 0)

    def test_apurado(self):
        c = ClienteApurado()
        self.assertAlmostEqual(c.calcular_propina(80), 72)
        self.assertAlmostEqual(c.calcular_propina(50), 45)
        self.assertAlmostEqual(c.calcular_propina(20), 0)

    def test_valores_frontera(self):
        t, e, a = ClienteTranquilo(), ClienteExigente(), ClienteApurado()
        self.assertAlmostEqual(t.calcular_propina(70), 10)
        self.assertAlmostEqual(e.calcular_propina(70), 0)
        self.assertAlmostEqual(a.calcular_propina(70), 63)
        self.assertAlmostEqual(t.calcular_propina(30), 10)
        self.assertAlmostEqual(e.calcular_propina(30), 0)
        self.assertAlmostEqual(a.calcular_propina(30), 27)
        for c in (t, e, a):
            self.assertAlmostEqual(c.calcular_propina(29.9), 0)