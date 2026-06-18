import unittest
from konto import Konto

class TestKonto(unittest.TestCase):
  def setUp(self):
    self.k = Konto()

  def test_algne_jaak(self):
    self.assertEqual(self.k.jaak(), 0)

  def test_sissemakse(self):
    self.k.sissemakse(50)
    self.assertEqual(self.k.jaak(), 50)

  def test_negatiivne_sissemakse(self):
    self.k.sissemakse(-30)
    self.assertEqual(self.k.jaak(), 0)

  def test_valjamakse(self):
    self.k.sissemakse(100)
    self.assertTrue(self.k.valjamakse(40))
    self.assertEqual(self.k.jaak(), 60)

  def test_liiga_suur_valjamakse(self):
    self.k.sissemakse(20)
    self.assertFalse(self.k.valjamakse(50))
    self.assertEqual(self.k.jaak(), 20)

  def test_mitu_tehingut(self):
    self.k.sissemakse(100)
    self.k.valjamakse(30)
    self.k.sissemakse(10)
    self.assertEqual(self.k.jaak(), 80)


suite = unittest.TestLoader().loadTestsFromTestCase(TestKonto)
runner = unittest.TextTestRunner(verbosity=0)
result = runner.run(suite)
print(f'Teste: {result.testsRun}')
