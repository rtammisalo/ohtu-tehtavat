from kps import KPS


class KPSTekoaly(KPS):
    def __init__(self, tekoaly):
        self.tekoaly = tekoaly

    def _toisen_siirto(self, ensimmaisen_siirto):
        siirto = self.tekoaly.anna_siirto()
        print(f"Tietokone valitsi: {siirto}")
        self.tekoaly.aseta_siirto(ensimmaisen_siirto)
        return siirto
