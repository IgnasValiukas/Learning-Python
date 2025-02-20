# Sukurkite ir išsibandykite funkcijas, kurios:
# Gražintų sąrašą tik su nepasikartojančiais paduoto sąrašo elementais.
# Gražintų, ar paduotas skaičius yra pirminis.
# Išrikiuotų paduoto stringo žodžius nuo paskutinio iki pirmojo
# Gražina, ar paduoti metai yra keliamieji, ar ne.
# Atspausdina, kiek nuo paduotos datos praėjo metų, mėnesių, dienų, valandų, minučių, sekundžių.

# Gražinti trijų paduotų skaičių sumą.
# def sum_numbers(x, y, z):
#     result = int(x + y + z)
#     return result
# print(f'Three integers sum = {sum_numbers(1, 2, 4)}\n')

# Gražintų paduoto sąrašo iš skaičių, sumą.
# grade = []
# range_declaration = int(input("Declare how many Integers would you like to input: "))
# for number in range(range_declaration):
#     integer = int(input("Write one integer: "))
#     grade.append(integer)
# def sum_list(given_list):
#       result_1 = sum(given_list)
#       return result_1
# print(f'List sum = {sum_list(grade)}\n')

# Atspausdintų didžiausią iš kelių paduotų skaičių (panaudojant *args).
# def find_max(*args):
#     for numbers in args:
#         print(max(numbers))
# all_numbers = (1,4,5,32,6,7,33,23,5)
# find_max(all_numbers)

# Gražintų paduotą stringą atbulai.
# users_string = input("Add text: ")
# def reverse_string(given_string):
#     return given_string[::-1]
# print("Reversed text:", reverse_string(users_string))

# Atspausdintų, kiek paduotame stringe yra žodžių, didžiųjų ir mažųjų raidžių, skaičių.
users_string_1 = input("Add text: ")
def string_wikipedia(given_string):
    word_count = len(given_string.split())
    capital = sum(1 for c in given_string if c.isupper())
    lower = sum(1 for c in given_string if c.islower())
    return print("Total words", word_count), print("Total capital letters", capital), print("Total lowercase letters", lower)
string_wikipedia(users_string_1)

# Gražintų sąrašą tik su nepasikartojančiais paduoto sąrašo elementais.

