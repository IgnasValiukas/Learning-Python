# Parašyti programą, kuri:
# Leistų vartotojui įvesti sveiką skaičių.
# Atspausdinti True, jei skaičius teigiamas
# Atspausdinti False, jei skaičius neigiamas ar lygus 0
# True/False reikšmei išsaugoti naudoti boolean tipo kintamąjį ar_skaicius_teigiamas
# Patarimas: naudoti input, boolean
from contextlib import nullcontext

integer = int(input("Add integer number: "))

if integer > 0:
    ar_skaicius_teigiamas = True  # priskiriam True reiksme
    print(ar_skaicius_teigiamas)
elif integer <= 0:
    ar_skaicius_teigiamas = False  # priskiriam False reiksme
    print(ar_skaicius_teigiamas)

# while True:
#     def checking():
#         integer_test = int(input("Add integer number: "))
#         return print(True) if integer_test > 0 else print(False)
#     checking()