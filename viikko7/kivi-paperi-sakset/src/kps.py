from tuomari import Tuomari


class KPS:
    def pelaa(self):
        tuomari = Tuomari()

        ekan_siirto, tokan_siirto = self._kysy_siirrot()

        while self._onko_ok_siirto(ekan_siirto) and self._onko_ok_siirto(tokan_siirto):
            tuomari.kirjaa_siirto(ekan_siirto, tokan_siirto)
            print(tuomari)
            ekan_siirto, tokan_siirto = self._kysy_siirrot()

        print("Kiitos!")
        print(tuomari)

    def _kysy_siirrot(self):
        ekan_siirto = self._ensimmaisen_siirto()
        tokan_siirto = self._toisen_siirto(ekan_siirto)
        return ekan_siirto, tokan_siirto

    def _ensimmaisen_siirto(self):
        return input("Ensimmäisen pelaajan siirto: ")

    # tämän metodin toteutus vaihtelee eri pelityypeissä
    def _toisen_siirto(self, ensimmaisen_siirto):
        # metodin oletustoteutus
        return "k"

    def _onko_ok_siirto(self, siirto):
        return siirto == "k" or siirto == "p" or siirto == "s"
