# Turėtų klasę Zmogus, su savybėmis vardas ir amzius
# Klasėje būtų repr metodas, kuris atvaizduotų vardą ir amžių
# Inicijuoti kelis Zmogus objektus su vardais ir amžiais
# Įdėti sukurtus Zmogus objektus į naują sąrašą
# Surūšiuotų ir atspausdintų sąrašo objektus pagal vardą ir pagal amžių (ir atbulai)
# Patarimai: Naudoti sorted, attrgetter, reverse, funkciją repr
from operator import attrgetter

class Zmogus:
    def __init__(self, vardas, amzius):
        self.vardas = vardas
        self.amzius = amzius

    def __repr__(self):
       return '(vardas: {}, amzius: {})'.format(self.vardas, self.amzius)

zmones = [Zmogus("Tomas", 34), Zmogus("Adomas", 19), Zmogus("Benas", 28)]

print(f'Žmonių sąrašas {zmones}\n')

pagal_varda = sorted(zmones, key=attrgetter('vardas'))
reverse_pagal_varda = sorted(zmones, key=attrgetter('vardas'), reverse=True)
print(f'Surūšiuota (vardas) -> {pagal_varda}')
print(f'Atvirkščiai (vardas) -> {reverse_pagal_varda}\n')

pagal_amziu = sorted(zmones, key=attrgetter('amzius'))
reverse_pagal_amziu = sorted(zmones, key=attrgetter('amzius'), reverse=True)
print(f'Surūšiuota (amžius) -> {pagal_amziu}')
print(f'Atvirkščiai (amžius) -> {reverse_pagal_amziu}')

