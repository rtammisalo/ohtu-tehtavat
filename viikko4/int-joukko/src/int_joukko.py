KAPASITEETTI = 5
OLETUSKASVATUS = 5


class IntJoukko:
    def __init__(self, kapasiteetti=KAPASITEETTI, kasvatuskoko=OLETUSKASVATUS):
        if not isinstance(kapasiteetti, int) or kapasiteetti < 0:
            raise Exception("Väärä kapasiteetti")

        if not isinstance(kasvatuskoko, int) or kasvatuskoko < 0:
            raise Exception("Väärä kasvatuskoko")

        self.kasvatuskoko = kasvatuskoko
        self.lukujono = [0] * kapasiteetti
        self.alkioiden_lkm = 0

    def kuuluu(self, arvo):
        if arvo in self.lukujono[:self.alkioiden_lkm]:
            return True

        return False

    def _kasvata_lukujono_listan_kokoa(self):
        if self.alkioiden_lkm % len(self.lukujono) == 0:
            self.lukujono.extend([0] * self.kasvatuskoko)

    def lisaa(self, lisattava_arvo):
        if not self.kuuluu(lisattava_arvo):
            self.lukujono[self.alkioiden_lkm] = lisattava_arvo
            self.alkioiden_lkm += 1
            self._kasvata_lukujono_listan_kokoa()
            return True

        return False

    def poista(self, poistettava_arvo):
        try:
            self.lukujono.remove(poistettava_arvo)
            self.lukujono.append(0)
            self.alkioiden_lkm -= 1
        except ValueError:
            return False

        return True

    def mahtavuus(self):
        return self.alkioiden_lkm

    def to_int_list(self):
        return self.lukujono[:self.alkioiden_lkm].copy()

    @staticmethod
    def yhdiste(joukko_a, joukko_b):
        yhdiste_joukko = IntJoukko()

        for arvo in joukko_a.to_int_list() + joukko_b.to_int_list():
            yhdiste_joukko.lisaa(arvo)

        return yhdiste_joukko

    @staticmethod
    def leikkaus(joukko_a, joukko_b):
        leikkaus_joukko = IntJoukko()

        for arvo_a in joukko_a.to_int_list():
            if joukko_b.kuuluu(arvo_a):
                leikkaus_joukko.lisaa(arvo_a)

        return leikkaus_joukko

    @staticmethod
    def erotus(joukko_a, joukko_b):
        erotus_joukko = IntJoukko()

        for arvo_a in joukko_a.to_int_list():
            if not joukko_b.kuuluu(arvo_a):
                erotus_joukko.lisaa(arvo_a)

        return erotus_joukko

    def __str__(self):
        alkioiden_merkkijono = ", ".join(
            [str(arvo) for arvo in self.lukujono[:self.alkioiden_lkm]])
        return f"{{{alkioiden_merkkijono}}}"
