# Sukurti programą, kuri:
# Leistų vartotojui įvesti metus
# Atspausdintų „Keliamieji metai“, jei taip yra
# Atspausdintų „Nekeliamieji metai“, jei taip yra
# Keliamieji metai yra kas 4 metus, išskyrus paskutinius amžiaus metus, kurie keliamieji yra tik kas 400 metų

#_year = int(input("Write year: \n"))

# if _year % 4 == 0:
#     print("Year is a Leap!")
# else:
#     print("Year is Not a Leap!")

_number = "yes"
while _number == "yes":
    _year = int(input("Write year (ex.: 2002): "))
    if _year % 4 == 0:
        print("Year is a Leap!")
        _loop = (input("Do you want to continue? yes/no \n"))
    else:
        print("Year is Not a Leap!")
        _loop = (input("Do you want to continue? yes/no \n"))
    if _loop == "yes":
        _number = "yes"
    elif _loop == "no":
        print("Loop Ended!")
        break
    else:
        print("Invalid Input!")
        break

