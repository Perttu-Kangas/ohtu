import unittest
from ostoskori import Ostoskori
from tuote import Tuote

class TestOstoskori(unittest.TestCase):
    def setUp(self):
        self.kori = Ostoskori()
        self.def_tuote = [Tuote("yeet", 5), Tuote("no", 3)]

    def test_ostoskorin_hinta_ja_tavaroiden_maara_alussa(self):
        self.assertEqual(self.kori.hinta(), 0)
        self.assertEqual(self.kori.tavaroita_korissa(), 0)

    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_tavara(self):
        self.kori.lisaa_tuote(self.def_tuote[1])
        self.assertEqual(self.kori.tavaroita_korissa(), 1)
    
    def test_yhden_tuotteen_lisaamisen_jalkeen_ostoskorin_hinta_on_sama_kuin_tuotteen_hinta(self):
        self.kori.lisaa_tuote(self.def_tuote[1])
        self.assertEqual(self.kori.hinta(), 3)
    
    def test_kahden_eri_tuotteen_lisaamisen_jalkeen_ostoskorissa_on_kaksi_tavaraa(self):
        self.kori.lisaa_tuote(self.def_tuote[0])
        self.kori.lisaa_tuote(self.def_tuote[1])
        self.assertEqual(self.kori.tavaroita_korissa(), 2)
    
    def test_kahden_eri_tuotteen_lisaamisen_jalkeen_ostoskorissa_on_kahden_tavaran_hinnan_summa(self):
        self.kori.lisaa_tuote(self.def_tuote[0])
        self.kori.lisaa_tuote(self.def_tuote[1])
        self.assertEqual(self.kori.hinta(), 8)

    def test_kahden_saman_tuotteen_lisaamisen_jalkeen_ostoskorissa_on_kaksi_tavaraa(self):
        self.kori.lisaa_tuote(self.def_tuote[0])
        self.kori.lisaa_tuote(self.def_tuote[0])
        self.assertEqual(self.kori.tavaroita_korissa(), 2)

    def test_kahden_saman_tuotteen_lisaamisen_jalkeen_ostoskorissa_on_kahden_tavaran_hinnan_summa(self):
        self.kori.lisaa_tuote(self.def_tuote[0])
        self.kori.lisaa_tuote(self.def_tuote[0])
        self.assertEqual(self.kori.hinta(), 10)
    
    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_ostosolio(self):
        self.kori.lisaa_tuote(self.def_tuote[0])
        self.assertEqual(len(self.kori.ostokset()), 1)
    
    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_ostosolio_jolla_oikea_tuotteen_nimi_ja_maara(self):
        self.kori.lisaa_tuote(self.def_tuote[0])
        ostos = self.kori.ostokset()[0]
        self.assertEqual(ostos.lukumaara(), 1)
        self.assertEqual(ostos.tuotteen_nimi(), "yeet")
    
    def test_kahden_eri_tuotteen_lisaamisen_jalkeen_korissa_kaksi_ostosolio(self):
        self.kori.lisaa_tuote(self.def_tuote[0])
        self.kori.lisaa_tuote(self.def_tuote[1])
        self.assertEqual(len(self.kori.ostokset()), 2)
    
    def test_kahden_saman_tuotteen_lisaamisen_jalkeen_korissa_yksi_ostosolio(self):
        self.kori.lisaa_tuote(self.def_tuote[0])
        self.kori.lisaa_tuote(self.def_tuote[0])
        self.assertEqual(len(self.kori.ostokset()), 1)
    
    def test_kahden_saman_tuotteen_lisaamisen_jalkeen_korissa_kaksi_lukumaara(self):
        self.kori.lisaa_tuote(self.def_tuote[0])
        self.kori.lisaa_tuote(self.def_tuote[0])
        ostos = self.kori.ostokset()[0]
        self.assertEqual(ostos.tuotteen_nimi(), "yeet")
        self.assertEqual(ostos.lukumaara(), 2)
    
    def test_poisto_kun_kaksi_samaa(self):
        self.kori.lisaa_tuote(self.def_tuote[0])
        self.kori.lisaa_tuote(self.def_tuote[0])
        self.kori.poista_tuote(self.def_tuote[0])
        ostos = self.kori.ostokset()[0]
        self.assertEqual(ostos.lukumaara(), 1)

    def test_poisto_kokonaan(self):
        self.kori.lisaa_tuote(self.def_tuote[0])
        self.kori.poista_tuote(self.def_tuote[0])
        self.assertEqual(len(self.kori.ostokset()), 0)

    def test_tyhjenna(self):
        self.kori.poista_tuote(self.def_tuote[0])
        self.kori.poista_tuote(self.def_tuote[1])
        self.kori.tyhjenna()#
        self.assertEqual(len(self.kori.ostokset()), 0)