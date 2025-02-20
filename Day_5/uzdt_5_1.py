# Gražina tekstą atbulai
# Gražina tekstą mažosiomis raidėmis
# Gražina tekstą didžiosiomis raidėmis
# Gražina žodį pagal nurodytą eilės numerį
# Gražina, kiek tekste yra nurodytų simbolių arba žodžių
# Gražina tekstą su pakeistu nurodytu žodžiu arba simboliu
# Atspausdina, kiek sakinyje yra žodžių, skaičių, didžiųjų ir mažųjų raidžių

class Sakinys:
    def __init__(self, tekstas):
        atbulai = tekstas[::-1]
        mazosios = str.lower(tekstas)
        didziosios = str.upper(tekstas)
        indeksas = int(input("Index: "))
        pagal_indeksa = tekstas[indeksas]
        print(f'{atbulai}, \n{mazosios}, \n{didziosios}, \n{pagal_indeksa}')



sakinys = []
sakinys1 = Sakinys("Labas, mano vardas Ignas")
