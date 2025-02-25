# Perdaryti 1 užduoties programą, kad:
# Į šaknies funkciją padavus string tipo argumetrą, į log failą būtų išsaugoma išimties klaida su norimu tekstu
# Į dalybos funkciją antrą argumentą padavus 0, į log failą būtų išsaugoma išimties klaida su norimu tekstu
# Patarimas: panaudoti try/except/else, logging.exception()

import math, logging

logging.basicConfig(filename='log_data_2uzdt.log', level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')


# Gražintų visų paduotų skaičių sumą (su *args argumentu)
def numbers_sum(*args):
    sum_result = sum(args)
    logging.info(f"Numbers {args} sum is equal: {sum_result}")
    print(sum_result)


# Gražintų paduoto skaičiaus šaknį (panaudoti math.sqrt())
def square_root(number):
    try:
        square_result = math.sqrt(number)
        logging.info(f"Square root of {number} is {square_result}")
        print(square_result)
    except TypeError:
        logging.exception(f"Input must be Integer or Float! wrong input: \"{number}\"")


# Gražintų paduoto sakinio simbolių kiekį (su len())
def text_length(text):
    text_result = len(text)
    logging.info(f"Given text \"{text}\" length is {text_result} symbols")
    print(text_result)


# Gražintų rezultatą, skaičių x padalinus iš y
def division(number1, number2):
    try:
        division_result = number1 / number2
        logging.info(
            f"Number {number1} divided by {number2} is equal {division_result}")
        print(division_result)
    except ZeroDivisionError:
        logging.exception(f"Number ({number1}) can't be divided by 0!")

# wrong inputs
square_root("Labas")
division(4, 0)
# good inputs
print("Good Inputs result:")
numbers_sum(1, 2, 3, 4, 5, 20, 12, 15, 7, 3)
square_root(4)
text_length("Hello World!")
division(4, 2)

