import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_saldo_alussa_oikea(self):
        self.assertEqual(self.maksukortti.saldo_euroina(), 10)

    def test_saldo_nousee_oikein(self):
        self.maksukortti.lataa_rahaa(100)
        self.assertEqual(self.maksukortti.saldo_euroina(), 11)

    def test_saldo_laskee_oikein(self):
        self.maksukortti.ota_rahaa(200)
        self.assertEqual(self.maksukortti.saldo_euroina(), 8)

    def test_saldo_ei_laske1(self):
        self.maksukortti.ota_rahaa(1100)
        self.assertEqual(self.maksukortti.saldo_euroina(), 10)

    def test_saldo_ei_laske2(self):
        self.assertEqual(self.maksukortti.ota_rahaa(1100), False)
    
    def test_saldo_ei_laske3(self):
        self.assertEqual(self.maksukortti.ota_rahaa(1000), True)

    def test_oikea_teksti(self):
        self.maksukortti.ota_rahaa(100)
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 9.00 euroa")

