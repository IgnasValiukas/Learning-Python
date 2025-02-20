# Turėtų klasę Zmogus, su savybėmis vardas ir amzius
# Klasėje būtų repr metodas, kuris atvaizduotų vardą ir amžių
# Inicijuoti kelis Zmogus objektus su vardais ir amžiais
# Įdėti sukurtus Zmogus objektus į naują sąrašą
# Surūšiuotų ir atspausdintų sąrašo objektus pagal vardą ir pagal amžių (ir atbulai)
# Patarimai: Naudoti sorted, attrgetter, reverse, funkciją repr
class Zmogus:
    def __init__(self, vardas, amzius):
        self.vardas = vardas
        self.amzius = amzius

    def __repr__(self):
       return f"vardas:'{self.vardas}', amžius:'{self.amzius}'"

zmogus1 = Zmogus("Tomas", 34)
zmogus2 = Zmogus("Adomas", 19)
zmogus3 = Zmogus("Benas", 28)
zmoniu_sarasas = [zmogus1, zmogus2, zmogus3]
print(f'Žmonių sąrašas {zmoniu_sarasas}\n')

def rusiavimas_pagal_varda(zmogus):
    return zmogus.vardas

pagal_varda = sorted(zmoniu_sarasas, key=rusiavimas_pagal_varda)
reverse_pagal_varda = sorted(zmoniu_sarasas, key=rusiavimas_pagal_varda, reverse=True)
print(f'Surūšiuota (vardas) -> {pagal_varda}')
print(f'Atvirkščiai (vardas) -> {reverse_pagal_varda}\n')

def rusiavimas_pagal_amziu(zmogus):
    return zmogus.amzius

pagal_amziu = sorted(zmoniu_sarasas, key=rusiavimas_pagal_amziu)
reverse_pagal_amziu = sorted(zmoniu_sarasas, key=rusiavimas_pagal_amziu, reverse=True)
print(f'Surūšiuota (amžius) -> {pagal_amziu}')
print(f'Atvirkščiai (amžius) -> {reverse_pagal_amziu}')

