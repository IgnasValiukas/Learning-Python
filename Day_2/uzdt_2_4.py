# Kauliukų žaidimas
# Sukurti programą, kuri:
# Sugeneruotų tris atsitiktinius skaičius nuo 1 iki 6
# Jei vienas iš šių skaičių yra 5, atspausdinti „Pralaimėjai...“
# Kitu atveju atspausdinti „Laimėjai!“
# Patarimas: Naudoti while ciklą, funkciją random.randint (import random), else, break
# Random skaičiaus generavimo pavyzdys:
# import random
# print(random.randint(1, 6))

import random

# for dice in range(3):
#     _diceNumber = random.randint(1, 6)
#     print(_diceNumber)
#     if _diceNumber == 5:
#         print("You Lost!")
#         break
# else:
#     print("You Won!")

_number = 0
while _number < 3:
    _number += 1
    _dice = (random.randint(1, 6))
    print(_dice)
    if _dice == 5:
        print("You Lost!")
        break
else:
    print("You Won!")
