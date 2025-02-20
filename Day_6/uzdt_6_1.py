# Turėtų klasę Automobilis
# Automobilis turėtų savybes: metai, modelis, kuro_tipas
# Automobilis turėtų metodus: vaziuoti, stoveti, pildyti_degalu, kurie atitinkamai atspausdintų „Važiuoja“, „Priparkuota“, „Degalai įpilti“
# Sukūrus objektą, automatiškai atspausdintų automobilio metus, modelį ir kuro tipą
# Turėtų klasę Elektromobilis (jo tėvinis objektas – Automobilis) *Elektromobilis pakeistų Automobilio metodą pildyti_degalu taip,
# kad jis atspausdintų „Baterija įkrauta“
# Elektromobilis turėtų metodą vaziuoti_autonomiskai, kuris spausdintų „Važiuoja autonomiškai“
# Sukurti norimą Automobilio objektą
# Sukurti norimą Elektromobilio objektą
# Su sukurtu Automobilio objektu paleisti funkcijas vaziuoti, stoveti, pildyti_degalu
# Su sukurtu Elektromobilio objektu paleisti funkcijas vaziuoti, stoveti, pildyti_degalu, vaziuoti_autonomiskai

class Automobilis:
    def __init__(self, metai, modelis, kuro_tipas):
        self.metai = metai
        self.modelis = modelis
        self.kuro_tipas = kuro_tipas
        print(metai, modelis, kuro_tipas)

    def vaziuoti(self):
        print("Važiuoja")

    def stoveti(self):
        print("Priparkuota")

    def pildyti_degalu(self):
        print("Degalai įpilti")


class Elektromobilis(Automobilis):
    def pildyti_degalu(self):
        print("Baterija įkrauta")

    def vaziuoti_autonomiskai(self):
        print("Važiuoja autonomiškai")


automobilis1 = Automobilis(2020, "911 GT2 RS,", "benzinas")
automobilis1.vaziuoti()
automobilis1.stoveti()
automobilis1.pildyti_degalu()
print("")
elektromobilis1 = Elektromobilis(2024, "Model X,", "elektra")
elektromobilis1.vaziuoti()
elektromobilis1.stoveti()
elektromobilis1.pildyti_degalu()
elektromobilis1.vaziuoti_autonomiskai()
