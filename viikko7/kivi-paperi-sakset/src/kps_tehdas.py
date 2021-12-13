from kps_tekoaly import KPSTekoaly
from kps_pelaaja_vs_pelaaja import KPSPelaajaVsPelaaja
from tekoaly import Tekoaly
from tekoaly_parannettu import TekoalyParannettu


class KPSTehdas:
    @staticmethod
    def peli_ihmista_vastaan():
        return KPSPelaajaVsPelaaja()

    @staticmethod
    def peli_tekoalya_vastaan():
        return KPSTekoaly(Tekoaly())

    @staticmethod
    def peli_parannettua_tekoalya_vastaan():
        return KPSTekoaly(TekoalyParannettu(10))
