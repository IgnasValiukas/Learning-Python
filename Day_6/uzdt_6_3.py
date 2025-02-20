# Sukurti tėvinę klasę Irasas, kurioje būtų savybės suma , iš kurios klasės PajamuIrasas ir IslaiduIrasas paveldėtų visas savybes.
# Į klasę PajamuIrasas papildomai pridėti savybes siuntejas ir papildoma_informacija, kurias vartotojas galėtų įrašyti.
# Į klasę IslaiduIrasas papildomai pridėti savybes atsiskaitymo_budas ir isigyta_preke_paslauga, kurias vartotojas galėtų įrašyti.
# Atitinkamai perdaryti klasės Biudzetas metodus gauti_balansa ir parodyti_ataskaita kad pasiėmus įrašą iš žurnalo,->
# atpažintų, ar tai yra pajamos ar išlaidos (pvz., panaudojus isinstance() metodą) ir atitinkamai atliktų veiksmus.
# Padaryti, kad vartotojui (per konsolę) būtų leidžiama įrašyti pajamų ir išlaidų įrašus, peržiūrėti balansą ir ataskaitą.

class Irasas:
    def __init__(self, suma):
        self.suma = suma

    def __str__(self):
        return f"Suma: {self.suma} €"

class PajamuIrasas(Irasas):
    def __init__(self, suma, siuntejas, papildoma_informacija):
        super().__init__(suma)  #  iskvieciam
        self.siuntejas = siuntejas
        self.papildoma_informacija = papildoma_informacija

    def __str__(self):
        return f"{super().__str__()} Pajamos -> Siuntejas: {self.siuntejas}, Papildoma informacija: {self.papildoma_informacija}"

class IslaiduIrasas(Irasas):
    def __init__(self, suma, atsiskaitymo_budas, isigyta_preke_paslauga):
        super().__init__(suma)
        self.atsiskaitymo_budas = atsiskaitymo_budas
        self.isigyta_preke_paslauga = isigyta_preke_paslauga

    def __str__(self):
        return f"{super().__str__()} Išlaidos -> Atsiskaitymo būdas: {self.atsiskaitymo_budas}, Prekė/Paslauga: {self.isigyta_preke_paslauga}"

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

biudzetas = Biudzetas()

while True:
    pasirinkimas = int(input("Pasirinkite: \n1 - Įvesti pajamas \n2 - Įvesti išlaidas \n3 - Peržiūrėti balansą \n4 - Rodyti ataskaitą \n5 - Išeiti\n"))

    if pasirinkimas == 1:
        suma = float(input("Įveskite pajamų sumą: "))
        siuntejas = input("Siuntėjas: ")
        papildoma_info = input("Papildoma informacija: ")
        biudzetas.prideti_pajamu_irasa(suma, siuntejas, papildoma_info)

    elif pasirinkimas == 2:
        suma = float(input("Įveskite išlaidų sumą: "))
        atsiskaitymo_budas = input("Atsiskaitymo būdas: ")
        isigyta_preke = input("Įsigyta prekė/paslauga: ")
        biudzetas.prideti_islaidu_irasa(suma, atsiskaitymo_budas, isigyta_preke)

    elif pasirinkimas == 3:
        print(f"Balansas: {biudzetas.gauti_balansa()} EUR")

    elif pasirinkimas == 4:
        biudzetas.parodyti_ataskaita()

    elif pasirinkimas == 5:
        break
    else:
        print("Neteisingas pasirinkimas, bandykite dar kartą.")
