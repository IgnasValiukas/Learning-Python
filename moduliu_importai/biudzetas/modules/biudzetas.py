from modules.islaidu_irasas import IslaiduIrasas
from modules.pajamu_irasas import PajamuIrasas


class Biudzetas:
    def __init__(self):
        self.zurnalas = []

    def prideti_pajamu_irasa(self, suma, siuntejas, papildoma_informacija):
        self.zurnalas.append(PajamuIrasas(suma, siuntejas, papildoma_informacija))

    def prideti_islaidu_irasa(self, suma, atsiskaitymo_budas, isigyta_preke_paslauga):
        self.zurnalas.append(IslaiduIrasas(suma, atsiskaitymo_budas, isigyta_preke_paslauga))

    def gauti_balansa(self):
        pajamu_suma = sum(irasas.suma for irasas in self.zurnalas if isinstance(irasas, PajamuIrasas))
        islaidu_suma = sum(irasas.suma for irasas in self.zurnalas if isinstance(irasas, IslaiduIrasas))
        return pajamu_suma - islaidu_suma

    def parodyti_ataskaita(self):
        for irasas in self.zurnalas:
            print(irasas)