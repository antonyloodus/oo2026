import unittest
from geenid1 import Alleel, Geen

class TestAlleel(unittest.TestCase):

    def test_positiivne_alleel(self):
        a = Alleel("reesus", True)
        self.assertEqual(a.nimetus, "reesus")
        self.assertTrue(a.positiivne)

    def test_negatiivne_alleel(self):
        a = Alleel("reesus", False)
        self.assertEqual(a.nimetus, "reesus")
        self.assertFalse(a.positiivne)


class TestGeen(unittest.TestCase):

    def test_erinevad_nimetused(self):
        with self.assertRaises(ValueError):
            Geen(Alleel("reesus", True), Alleel("geen2", False))

    def test_molemad_positiivsed(self):
        geen = Geen(Alleel("reesus", True), Alleel("reesus", True))
        self.assertTrue(geen.on_positiivne())

    def test_uks_positiivne(self):
        geen = Geen(Alleel("reesus", True), Alleel("reesus", False))
        self.assertTrue(geen.on_positiivne())

    def test_teine_positiivne(self):
        geen = Geen(Alleel("reesus", False), Alleel("reesus", True))
        self.assertTrue(geen.on_positiivne())

    def test_molemad_negatiivsed(self):
        geen = Geen(Alleel("reesus", False), Alleel("reesus", False))
        self.assertFalse(geen.on_positiivne())

    def test_geeni_nimetus(self):
        geen = Geen(Alleel("reesus", True), Alleel("reesus", False))
        self.assertEqual(geen.nimetus, "reesus")


if __name__ == "__main__":
    unittest.main(verbosity=2)