class Komento:
    SUMMA = "Summa"
    EROTUS = "Erotus"
    NOLLAUS = "Nollaus"
    KUMOA = "Kumoa"

    def __init__(self, sovellus, lue_syote):
        self._sovellus = sovellus
        self._lue_syote = lue_syote

    def suorita(self):
        self._edellinen_tulos = self._sovellus.tulos
        self._suorita_komento()
        self._sovellus.edellinen_komento = self

    def _suorita_komento(self):
        pass

    def kumoa(self):
        self._sovellus.tulos = self._edellinen_tulos

    def _muunna_luvuksi(self, arvo):
        try:
            return int(arvo)
        except ValueError:
            return 0


class Summa(Komento):
    def _suorita_komento(self):
        luku = self._muunna_luvuksi(self._lue_syote())
        self._sovellus.tulos = self._sovellus.tulos + luku


class Erotus(Komento):
    def _suorita_komento(self):
        luku = self._muunna_luvuksi(self._lue_syote())
        self._sovellus.tulos = self._sovellus.tulos - luku


class Nollaa(Komento):
    def _suorita_komento(self):
        self._sovellus.tulos = 0


class Kumoa(Komento):
    def _suorita_komento(self):
        self._sovellus.edellinen_komento.kumoa()


class Tuntematon(Komento):
    def _suorita_komento(self):
        pass


class Komentotehdas:
    def __init__(self, sovellus, lue_syote):
        self._sovellus = sovellus
        self.komennot = {
            Komento.SUMMA: Summa(sovellus, lue_syote),
            Komento.EROTUS: Erotus(sovellus, lue_syote),
            Komento.NOLLAUS: Nollaa(sovellus, lue_syote),
            Komento.KUMOA: Kumoa(sovellus, lue_syote),
        }

    def hae(self, komento):
        if komento in self.komennot:
            return self.komennot[komento]

        return Tuntematon(self._sovellus)
