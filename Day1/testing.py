# Leistų įvesti skaičius a ir b (int arba float)
# Išvestų į ekraną „a mažesnis už b“, jei taip yra
# Išvestų į ekraną „a lygu b“, jei taip yra
# Išvestų į ekraną „a didesnis už b“, jei taip yra

firstNumber = float(input("Add first number (a)\n"))
secondNumber = float(input("Add second number (b)\n"))

if firstNumber < secondNumber:
    print("First number '%s' is smaller than Second number '%s'" % (firstNumber, secondNumber))
elif firstNumber == secondNumber:
    print("First number '%s' is equals to Second number '%s'" % (firstNumber, secondNumber))
else:
    print("First number '%s' is bigger than Second number '%s'" % (firstNumber, secondNumber))

