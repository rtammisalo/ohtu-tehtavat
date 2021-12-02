class Komento:
    SUMMA = "Summa"
    EROTUS = "Erotus"
    NOLLAUS = "Nollaus"
    KUMOA = "Kumoa"

    def __init__(self, sovellus, lue_syote):
        self._sovellus = sovellus
        self._lue_syote = lue_syote

    def _muunna_luvuksi(self, arvo):
        try:
            return int(arvo)
        except ValueError:
            return 0


class Summa(Komento):
    def suorita(self):
        luku = self._muunna_luvuksi(self._lue_syote())
        self._sovellus.tulos = self._sovellus.tulos + luku


class Erotus(Komento):
    def suorita(self):
        luku = self._muunna_luvuksi(self._lue_syote())
        self._sovellus.tulos = self._sovellus.tulos - luku


class Nollaa(Komento):
    def suorita(self):
        self._sovellus.tulos = 0


class Tuntematon(Komento):
    def suorita(self):
        pass


class Komentotehdas:
    def __init__(self, sovellus, lue_syote):
        self._sovellus = sovellus
        self.komennot = {
            Komento.SUMMA: Summa(sovellus, lue_syote),
            Komento.EROTUS: Erotus(sovellus, lue_syote),
            Komento.NOLLAUS: Nollaa(sovellus, lue_syote),
            Komento.KUMOA: Tuntematon(sovellus, lue_syote),
        }

    def hae(self, komento):
        if komento in self.komennot:
            return self.komennot[komento]

        return Tuntematon(self._sovellus)
