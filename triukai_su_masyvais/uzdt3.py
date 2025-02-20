from functools import reduce

sarasas = [2.5, 2, "Labas", True, 5, 7, 8, 2.8, "Vakaras"]
# Paskaičiuotų ir atspausdintų visų sąrašo skaičių sumą
skaiciu_suma = sum(filter(lambda skaicius: type(skaicius) is int, sarasas))
print(f'Suma {skaiciu_suma}')
# Sudėtų ir atspausdintų visus sąrašo žodžius
zodziai = filter(lambda zodis: type(zodis) is str, sarasas)
sujungta = " ".join(zodziai)
print(sujungta)
# Suskaičiuotų ir atspausdintų, kiek sąraše yra loginių (boolean) kintamųjų su True reikšme
tipo_kiekis = filter(lambda tipas: tipas == True, sarasas)
tipo_suma = sum(type(reiksme) is bool for reiksme in tipo_kiekis)
print(f'True reiksmiu kiekis: {tipo_suma}')

print("\n<kitas sumos budas>")
skaiciu_suma1 = filter(lambda skaicius: type(skaicius) is int, sarasas)
skaiciusuma = reduce(lambda x, y: x + y, skaiciu_suma1)
print(f'Suma {skaiciusuma}')
