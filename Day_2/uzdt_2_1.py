# Sukurti norimą sąrašą ir žodyną ir juose:
# Atspausdinti vieną norimą įrašą
# Pridėti įrašą
# Ištrinti įrašą
# Pakeisti įrašą
# Išbandyti kitas sąrašų ir žodynų funkcijas: clear(), index(), insert(), remove...
# https://www.w3schools.com/python/python_ref_list.asp
# https://www.w3schools.com/python/python_ref_dictionary.asp

_list = ["I want Porsche", 911, ["GT2", "RS", 2020], 4]
_car = {"Brand": "Porsche", "Model": "911 GT2 RS", "Year": 2020, "Kilometer": 23000, "None": 000}

# Atspausdinti įrašą
print("Printed:", _list[0][7::], _car["Model"])  #print

# Pridėti įrašą
_list.append(3200000)  # append
print("Added:", _list)

_car["Price"] = 230000  # add
print("Added:", _car)

# Ištrinti įrašą
_list.pop(3)  #pop
print("Deleted: ", _list)

_car.pop("None")  #pop
print("Deleted: ", _car)

# Pakeisti įrašą
_list[0] = "I will have Porsche"  #change
print("Changed", _list)

_car["Kilometer"] = 50000  #change
print("Changed:", _car)

print('-' * 100)

"""List"""
print("LIST")
_text = ["Learning", 2025]
_test = ["test", 10010]
_stringList = ["Car", "Tree", "Dog"]

print("Count:", _text.count(2025))  #count - suskaiciuoja kiek tokiu elementu yra

_text.extend(_test)  #extend - sujungia dvieju sarasu turini
print("Extended:", _text)

print("Index:", _text.index("test"))  #index - nurodo pasirinkto elemento vieta

_text.insert(1, "Inserted")  #insert - iterpia elementa i pasirinkta saraso vieta

_text.reverse()  #reverse - apvercia sarasa
print("Reversed:", _text)

_text.remove("test")  #remove - pasalina pasirinkta pirma elementa
print("Removed:", _text)

_stringList.sort(reverse=True)  #sort - surusiuoja pagal pasirinkta buda (siuo atveju apvercia sarasa)
print("String list Sorted:", _stringList)

print('-' * 100)

"""Dictionary"""
print("DICTIONARY")
_data = {"Year": 2025, "Month": "February", "Day": 11, "Test": "test"}
_items = ('tent', 'matches', 'water')

print("Removed:", _data.popitem())  #popitem - istrina pasirinkta elementa

_getData = _data.get("Month")  #get - parodo pasirinkto rakto reiksme
print("Get method:", _getData)

_keys = dict.fromkeys(_items, 1)  #fromkeys - kiekvienam raktui priskiria reiksmes
print("Returned:", _keys)

_data.update({"Weekday": "Tuesday"})  #update - gale dictionary prideda nauja elementa
print("Updated", _data)

print(_data.values())  #values - isveda dictionary reiksmes saraso pavidalu

print("Value of the Key (Day):",
      _data.setdefault("Day"))  #setdefault jei egzistuoja raktas - isveda reiksme pagal pasirinkta rakta
_value = _data.setdefault("Default", "Working")  #setdefault jei neegzistuoja raktas - priskiariama jam reiksme
print("Value of the Key (Default):", _value)  #setdefault - isveda reiksme pagal pasirinkta rakta

_items = _data.items()  #items - sarase isveda elementus tuples pavidalu
print(_items)

_data.clear()  #clear - pasalina visus elementus
print("Cleared Dictionary:", _data)
