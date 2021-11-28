import unittest
from unittest.mock import Mock, ANY
from kauppa import Kauppa
from viitegeneraattori import Viitegeneraattori
from varasto import Varasto
from tuote import Tuote

class TestKauppa(unittest.TestCase):
    def setUp(self):
        self.pankki_mock = Mock()
        self.viitegeneraattori_mock = Mock()
        self.varasto_mock = Mock()
        self.kauppa = Kauppa(self.varasto_mock, self.pankki_mock, self.viitegeneraattori_mock)

    def test_ostoksen_paaytyttya_pankin_metodia_tilisiirto_kutsutaan(self):
        pankki_mock = Mock()
        viitegeneraattori_mock = Mock()

        # palautetaan aina arvo 42
        viitegeneraattori_mock.uusi.return_value = 42

        varasto_mock = Mock()

        # tehdään toteutus saldo-metodille
        def varasto_saldo(tuote_id):
            if tuote_id == 1:
                return 10

        # tehdään toteutus hae_tuote-metodille
        def varasto_hae_tuote(tuote_id):
            if tuote_id == 1:
                return Tuote(1, "maito", 5)

        # otetaan toteutukset käyttöön
        varasto_mock.saldo.side_effect = varasto_saldo
        varasto_mock.hae_tuote.side_effect = varasto_hae_tuote

        # alustetaan kauppa
        kauppa = Kauppa(varasto_mock, pankki_mock, viitegeneraattori_mock)

        # tehdään ostokset
        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(1)
        kauppa.tilimaksu("pekka", "12345")

        # varmistetaan, että metodia tilisiirto on kutsuttu
        pankki_mock.tilisiirto.assert_called()
        # toistaiseksi ei välitetä kutsuun liittyvistä argumenteista

    def test_ostoksen_paatyttya_pankin_tilisiirtoa_kutsutaan_oikeilla_argumenteilla(self):
        def saldo(tuote):
            if tuote == 2112:
                return 2

        def hae_tuote(tuote):
            if tuote == 2112:
                return Tuote(2112, "rush", 10)

        self.varasto_mock.saldo.side_effect = saldo
        self.varasto_mock.hae_tuote.side_effect = hae_tuote
        self.viitegeneraattori_mock.uusi.return_value = 1

        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(2112)
        self.kauppa.tilimaksu("geddy", "555")

        self.pankki_mock.tilisiirto.assert_called_with("geddy", 1, "555", self.kauppa._kaupan_tili, 10)

    def test_kahden_varastoidun_eri_tuotteen_oston_paatyttya_kutsutaan_tilisiirtoa_oikeilla_argumenteilla(self):
        def saldo(tuote):
            if tuote == 2112:
                return 2
            if tuote == 1221:
                return 10

        def hae_tuote(tuote):
            if tuote == 2112:
                return Tuote(2112, "rush", 10)
            if tuote == 1221:
                return Tuote(1221, "vasara", 15)

        self.varasto_mock.saldo.side_effect = saldo
        self.varasto_mock.hae_tuote.side_effect = hae_tuote
        self.viitegeneraattori_mock.uusi.return_value = 1

        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(2112)
        self.kauppa.lisaa_koriin(1221)
        self.kauppa.tilimaksu("geddy", "555")

        self.pankki_mock.tilisiirto.assert_called_with("geddy", 1, "555", self.kauppa._kaupan_tili, 25)

    def test_kahden_varastoidun_saman_tuotteen_oston_paatyttya_kutsutaan_tilisiirtoa_oikeilla_argumenteilla(self):
        def saldo(tuote):
            if tuote == 2112:
                return 2

        def hae_tuote(tuote):
            if tuote == 2112:
                return Tuote(2112, "rush", 10)

        self.varasto_mock.saldo.side_effect = saldo
        self.varasto_mock.hae_tuote.side_effect = hae_tuote
        self.viitegeneraattori_mock.uusi.return_value = 1

        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(2112)
        self.kauppa.lisaa_koriin(2112)
        self.kauppa.tilimaksu("geddy", "555")

        self.pankki_mock.tilisiirto.assert_called_with("geddy", 1, "555", self.kauppa._kaupan_tili, 20)

    def test_yhden_varastoidun_ja_yhden_varastoimattoman_tuotteen_ostossa_kutsutaan_tilisiirtoa_oikeilla_argumenteilla(self):
        def saldo(tuote):
            if tuote == 2112:
                return 13
            if tuote == 1221:
                return 0

        def hae_tuote(tuote):
            if tuote == 2112:
                return Tuote(2112, "rush", 10)
            if tuote == 1221:
                return Tuote(1221, "vasara", 15)

        self.varasto_mock.saldo.side_effect = saldo
        self.varasto_mock.hae_tuote.side_effect = hae_tuote
        self.viitegeneraattori_mock.uusi.return_value = 1

        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(2112)
        self.kauppa.lisaa_koriin(1221)
        self.kauppa.tilimaksu("geddy", "555")

        self.pankki_mock.tilisiirto.assert_called_with("geddy", 1, "555", self.kauppa._kaupan_tili, 10)

    def test_edellinen_asiointi_ei_nay_uuden_ostoksen_hinnassa(self):
        def saldo(tuote):
            if tuote == 2112:
                return 13

        def hae_tuote(tuote):
            if tuote == 2112:
                return Tuote(2112, "rush", 10)

        self.varasto_mock.saldo.side_effect = saldo
        self.varasto_mock.hae_tuote.side_effect = hae_tuote
        self.viitegeneraattori_mock.uusi.return_value = 1

        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(2112)
        self.kauppa.tilimaksu("geddy", "555")
        self.pankki_mock.tilisiirto.assert_called_with(ANY, ANY, ANY, ANY, 10)

        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(2112)
        self.kauppa.lisaa_koriin(2112)
        self.kauppa.lisaa_koriin(2112)
        self.kauppa.tilimaksu("neil", "111")
        self.pankki_mock.tilisiirto.assert_called_with(ANY, ANY, ANY, ANY, 30)

    def test_kauppa_pyytaa_uutta_viitenumeroa_jokaiselle_maksutapahtumalle(self):
        self.viitegeneraattori_mock = Mock(wraps=Viitegeneraattori())
        self.kauppa = Kauppa(self.varasto_mock, self.pankki_mock, self.viitegeneraattori_mock)

        def saldo(tuote):
            if tuote == 2112:
                return 13

        def hae_tuote(tuote):
            if tuote == 2112:
                return Tuote(2112, "rush", 10)

        self.varasto_mock.saldo.side_effect = saldo
        self.varasto_mock.hae_tuote.side_effect = hae_tuote

        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(2112)
        self.kauppa.tilimaksu("geddy", "555")
        self.pankki_mock.tilisiirto.assert_called_with("geddy", 2, "555", self.kauppa._kaupan_tili, 10)

        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(2112)
        self.kauppa.lisaa_koriin(2112)
        self.kauppa.lisaa_koriin(2112)
        self.kauppa.tilimaksu("neil", "111")
        self.pankki_mock.tilisiirto.assert_called_with("neil", 3, "111", self.kauppa._kaupan_tili, 30)
        self.assertEqual(self.viitegeneraattori_mock.uusi.call_count, 2)

    def test_ostoskorista_tuotteen_palauttaminen_kutsuu_varaston_palauta_varastoon_metodia(self):
        def saldo(tuote):
            if tuote == 2112:
                return 13

        def hae_tuote(tuote):
            if tuote == 2112:
                return Tuote(2112, "rush", 10)

        self.varasto_mock.saldo.side_effect = saldo
        self.varasto_mock.hae_tuote.side_effect = hae_tuote

        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(2112)
        self.kauppa.poista_korista(2112)

        self.varasto_mock.palauta_varastoon.assert_called_once()
