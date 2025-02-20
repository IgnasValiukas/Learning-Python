# Turėtų klasę Darbuotojas
# Darbuotojas turėtų savybes: vardas, valandos_ikainis, dirba_nuo
# Turėtų privatų metodą kuris paskaičiuotų, kiek darbuotojas nudirbo dienų nuo įvestos dienos (dirba_nuo)->
# iki šiandien (turint omeny, kad darbuotojas dirba 7 dienas per savaitę)
# Turėtų metodą paskaiciuoti_atlyginima, kuris panaudodamas aukščiau aprašytu metodu,->
# paskaičiuotų bendrą atlyginimą (turint omeny, kad darbuotojas dirba 8 valandas per dieną)
# Turėtų klasę NormalusDarbuotojas, kuri pakeistų Darbuotojo klasę taip, kad ji skaičiuotų atlyginimą turint omeny,->
# kad darbuotojas dirba 5 dienas per savaitę (o ne 7, kaip įprastas darbuotojas).
# Sukurti norimą Darbuotojo objektą
# Sukurti norimą NormalusDarbuotojas objektą
# Su abiem objektais paleisti funkciją paskaiciuoti_atlyginima
import datetime


class Darbuotojas:
    def __init__(self, vardas, valandos_ikainis, dirba_nuo):
        self.vardas = vardas
        self.valandos_ikainis = valandos_ikainis
        #  gale pridejau date(), nes 'datetime.date.today()' yra date formato
        self.dirba_nuo = datetime.datetime.strptime(dirba_nuo, "%Y-%m-%d").date()

    def _paskaiciuoti_dienas(self):
        dabar = datetime.date.today()
        self.skirtumas = (dabar - self.dirba_nuo).days + 1
        return self.skirtumas

    def paskaiciuoti_atlyginima(self):
        dienos = self._paskaiciuoti_dienas()
        dienos_atlyginimas = self.valandos_ikainis * 8
        atlyginimas = dienos * dienos_atlyginimas
        print(f'{self.vardas}, your total salary is {atlyginimas}€')


class NormalusDarbuotojas(Darbuotojas):
    def _paskaiciuoti_dienas(self):
        dabar = datetime.date.today()
        skirtumas = (dabar - self.dirba_nuo).days + 1
        count = 0
        for i in range(skirtumas):
            diena = self.dirba_nuo + datetime.timedelta(days=i)
            if diena.weekday() < 5:
                count += 1
        return count


darbuotojas1 = Darbuotojas("Lukas", 15, "2025-01-16")
darbuotojas1.paskaiciuoti_atlyginima()

normalus_darbuotojas1 = NormalusDarbuotojas("Tomas", 15, "2025-01-16")
normalus_darbuotojas1.paskaiciuoti_atlyginima()
