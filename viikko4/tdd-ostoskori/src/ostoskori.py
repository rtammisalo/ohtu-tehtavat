from tuote import Tuote
from ostos import Ostos


class Ostoskori:
    def __init__(self):
        self._ostokset = {}
        # ostoskori tallettaa Ostos-oliota, yhden per korissa oleva Tuote

    def tavaroita_korissa(self):
        tavaroita = 0
        for ostos in self._ostokset.values():
            tavaroita += ostos.lukumaara()
        return tavaroita
        # kertoo korissa olevien tavaroiden lukumäärän
        # eli jos koriin lisätty 2 kpl tuotetta "maito", tulee metodin palauttaa 2
        # samoin jos korissa on 1 kpl tuotetta "maito" ja 1 kpl tuotetta "juusto", tulee metodin palauttaa 2

    def hinta(self):
        hinta = 0
        for ostos in self._ostokset.values():
            hinta += ostos.hinta()
        return hinta
        # kertoo korissa olevien ostosten yhteenlasketun hinnan

    def lisaa_tuote(self, lisattava: Tuote):
        # lisää tuotteen
        if lisattava.nimi() in self._ostokset:
            self._ostokset[lisattava.nimi()].muuta_lukumaaraa(1)
        else:
            self._ostokset[lisattava.nimi()] = Ostos(lisattava)

    def poista_tuote(self, poistettava: Tuote):
        # poistaa tuotteen
        if poistettava.nimi() in self._ostokset:
            ostos = self._ostokset[poistettava.nimi()]
            ostos.muuta_lukumaaraa(-1)

    def tyhjenna(self):
        pass
        # tyhjentää ostoskorin

    def ostokset(self):
        return list(self._ostokset.values())
        # palauttaa listan jossa on korissa olevat ostos-oliot
        # kukin ostos-olio siis kertoo mistä tuotteesta on kyse JA kuinka monta kappaletta kyseistä tuotetta korissa on
