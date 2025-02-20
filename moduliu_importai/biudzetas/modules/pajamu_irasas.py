from modules.irasas import Irasas


class PajamuIrasas(Irasas):
    def __init__(self, suma, siuntejas, papildoma_informacija):
        super().__init__(suma)  #  iskvieciam
        self.siuntejas = siuntejas
        self.papildoma_informacija = papildoma_informacija

    def __str__(self):
        return f"{super().__str__()} Pajamos -> Siuntejas: {self.siuntejas}, Papildoma informacija: {self.papildoma_informacija}"