# Sukurtų failą „Tekstas.txt“ su pilnu tekstu, gauto python kode paleidus „import this“.
# Atspausdintų visą failo tekstą atbulai
# Atspausdintų, kiek failo tekste yra žodžių, skaičių, didžiųjų ir mažųjų raidžių
# Nukopijuotų visą sukurto failą tekstą į naują failą, tik DIDŽIOSIOMIS RAIDĖMIS
# Patarimai:
# Naudoti from datetime import datetime, datetime.today()
# Kintamajam priskirti sakinį, kuriuo bus operuojama, eilutėmis
# Kai kur galima panaudoti funkcijas iš praeitų pamokų

from datetime import datetime

today = datetime.today()

# Atspausdintų tekstą iš sukurto failo
# with open("Tekstas.txt", "r") as failas:
#     print(failas.read())

# Paskutinėje sukurto failo eilutėje pridėtų šiandienos datą ir laiką
# with open("Tekstas.txt", "a") as failas:
#     failas.write("\n")
#     failas.write(str(today))

# Sunumeruotų teksto eilutes (kiekvienos pradžioje pridėtų skaičių).
# with open("Tekstas.txt", 'r') as failas:
#     turinys = failas.read()
# turinio_sarasas = turinys.split("\n")
# count = 0
# for turinys in turinio_sarasas:
#     count += 1
#     print(f'{count}) {turinys}')

# Sukurtame faile eilutę "Beautiful is better than ugly." pakeistų į "Gražu yra geriau nei bjauru."
with open("Tekstas.txt", "w", encoding="utf-8") as failas:
    failas.seek(0)
    failas.write("Gražu yra geriau nei bjauru.")

with open("Tekstas.txt", "r") as failas:
     print(failas.read())



