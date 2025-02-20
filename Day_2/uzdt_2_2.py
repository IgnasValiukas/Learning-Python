# Parašyti programą, kuri:
# Leistų vartotojui įvesti skaičių.
# Jei įvestas skaičius yra teigiamas, paprašyti įvesti dar vieną skaičių
# Jei įvestas skaičius neigiamas, nutraukti programą ir atspausdinti visų įvestų teigiamų skaičių sumą
# Patarimas: Naudoti ciklą while, sąlygą if, break

_list = []
number = int(input("Add number: \n"))

while number >= 0:
    _list.append(number)
    _sum = sum(_list)
    number = int(input("Add number: \n"))
    if number < 0:
        print(_list)
        print("List sum: ", _sum)
        break

# while number >= 0:
#     _list.append(number)
#     _sum = sum(_list)
#     number = int(input("Add number: \n"))
#     if number < 0:
#         break
#
# print(_list)
# print("List sum: ", _sum)

# _sum = 0
# while number >= 0:
#     _sum += number
#     _list.append(number)
#     number = int(input("Add number: \n"))
#     if number < 0:
#         print(_list)
#         print("List sum: ", _sum)
#         break