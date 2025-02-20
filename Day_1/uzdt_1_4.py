# Leistų įvesti pirmą skaičių
# Leistų įvesti antrą skaičių
# Paklaustų, kokį matematinį veiksmą reiktų atliktų
# Atspausdintų rezultatą: pasirinktų skaičių suma, daugybą ar pan.

firstNumber = float(input("Add First Number\n"))
secondNumber = float(input("Add Second Number\n"))
action = (input("Add Math Action (  +  -  *  /  )\n"))

if action == "+":
    result = firstNumber + secondNumber
    print(f'{firstNumber} + {secondNumber} = {result}')
elif action == "-":
    result = firstNumber - secondNumber
    print(f'{firstNumber} - {secondNumber} = {result}')
elif action == "*":
    result = firstNumber * secondNumber
    print(f'{firstNumber} * {secondNumber} = {result}')
elif action == "/":
    if firstNumber and secondNumber != 0:
        result = firstNumber / secondNumber
        print(f'{firstNumber} / {secondNumber} = {result}')
    else:
        print("Division by 0 is not allowed!")
else:
    print("Input is not Valid!")