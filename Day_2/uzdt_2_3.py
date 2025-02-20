# Sukurti programą, kuri:
# Leistų vartotojui po vieną įvesti 5 žodžius
# Pridėtų įvestus žodžius į sąrašą
# Atspausdintų kiekvieną žodį, jo ilgį ir eilės numerį sąraše (nuo 1)
# Sudėtingiau: kad programa leistų įvesti norimą žodžių kiekį
# Patarimas: Naudoti sąrašą (list), ciklą for, funkcijas len ir index

_list = []
_range = int(input("Declare how many Words would you like to input: \n"))
for number in range(_range):
    word = (input("Write one word: "))
    _list.append(word)

i = 0
for _listElements in _list:
    print("| Word:", "'",_list[i], "'", "| Word length: ", len(_list[i]), "| Word index: ", _list.index(_list[i]))
    i+=1