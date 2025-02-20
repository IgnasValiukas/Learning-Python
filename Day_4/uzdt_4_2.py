# Sukurti funkciją, kuri patikrintų, ar paduotas Lietuvos piliečio asmens kodas yra validus.
# Padaryti, kad programa sugeneruotų teisingą asmens kodą (panaudojus anksčiau sukurtą funkciją) pagal įvestą lytį, gimimo datą ir eilės numerį).
# https://lt.wikipedia.org/wiki/Asmens_kodas

"""NEBAIGTAS"""
import datetime

gender_input = input("Gender Male/Female: ")
birth_date = input("Birth date 2006-05-23: ")
series_number = int(input("Add serial number: "))
given_date = datetime.datetime.strptime(birth_date, "%Y-%m-%d")
century = int((given_date.year - 1) / 100 + 1)
print(f'Century {century}')
def gender_option(x):
    if x == "Male" or x == "male":
        gender = True
    else:
        gender = False
    return gender

y = gender_option(gender_input)

if y == True and century == 21:
    first_number= 5
    print(first_number)
elif y != True and century == 21:
    first_number = 6
    print(first_number)

if y == True and century == 20:
    first_number= 3
    print(first_number)
elif y != True and century == 20:
    first_number = 4
    print(first_number)







