# Leistų įvesti skaičių
# Išvesti į ekraną „Skaičius yra lyginis“, jei taip yra
# Išvesti į ekraną „Skaičius yra nelyginis“, jei taip yra
# Išvesti į ekraną „Skaičius dalinasi iš 3“, jei skaičius dalinasi iš trijų
# Patarimas: naudoti input(), if, print, %

number = int(input("Add number\n"))

if number%2==0:
    print(f'Number {number} is Even')
else:
    print(f'Number {number} is Odd')

if number % 3 == 0:
    print(f'Number {number} Can be divided by 3')
else:
    print(f'Number {number} Cant be divided by 3')