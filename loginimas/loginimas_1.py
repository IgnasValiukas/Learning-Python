# Nustatyti standartinį logerį (logging) taip, kad jis:
# Saugotų pranešimus į norimą failą
# Saugotų INFO lygio žinutes
# Pranešimai turi būti tokiu formatu: data/laikas, lygis, žinutė
# Kiekviena funkcija turi sukurti INFO lygio log pranešimą
# Paleisti kiekvieną funkciją su norimais argumentais

import math, logging

logging.basicConfig(filename='log_data.log', level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')


# Gražintų visų paduotų skaičių sumą (su *args argumentu)
def numbers_sum(*args):
    sum_result = sum(args)
    logging.info(f"Numbers {args} sum is equal: {sum_result}")
    print(sum_result)


# Gražintų paduoto skaičiaus šaknį (panaudoti math.sqrt())
def square_root(number):
    square_result = math.sqrt(number)
    logging.info(f"Square root of {number} is {square_result}")
    print(square_result)


# Gražintų paduoto sakinio simbolių kiekį (su len())
def text_length(text):
    text_result = len(text)
    logging.info(f"Given text \"{text}\" length is {text_result} symbols")
    print(text_result)


# Gražintų rezultatą, skaičių x padalinus iš y
def division(number1, number2):
    division_result = number1 / number2
    logging.info(
        f"Number {number1} divided by {number2} is equal {division_result}")
    print(division_result)


numbers_sum(1, 2, 3, 4, 5, 20, 12, 15, 7, 3)
square_root(4)
text_length("Hello World!")
division(4, 2)
