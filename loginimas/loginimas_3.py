# Perdaryti 2 užduoties programą, kad:
# Būtų sukurtas savo logeris, kuris fiksuotų visus anksčiau aprašytus pranešimus
# Sukurtas logeris ne tik išsaugotų pranešimus faile, bet ir atvaizduotų juos konsolėje

import math, logging

logger = logging.getLogger(__name__)
file_handler = logging.FileHandler('log_data_3uzdt.log')
logger.addHandler(file_handler)

logger.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(message)s')
file_handler.setFormatter(formatter)

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)
logger.addHandler(stream_handler)


# Gražintų visų paduotų skaičių sumą (su *args argumentu)
def numbers_sum(*args):
    sum_result = sum(args)
    logger.info(f"Numbers {args} sum is equal: {sum_result}")


# Gražintų paduoto skaičiaus šaknį (panaudoti math.sqrt())
def square_root(number):
    try:
        square_result = math.sqrt(number)
        logger.info(f"Square root of {number} is {square_result}")
    except TypeError:
        logger.exception(f"Input must be Integer or Float! wrong input: \"{number}\"")


# Gražintų paduoto sakinio simbolių kiekį (su len())
def text_length(text):
    text_result = len(text)
    logger.info(f"Given text \"{text}\" length is {text_result} symbols")


# Gražintų rezultatą, skaičių x padalinus iš y
def division(number1, number2):
    try:
        division_result = number1 / number2
        logger.info(
            f"Number {number1} divided by {number2} is equal {division_result}")
    except ZeroDivisionError:
        logger.exception(f"Number ({number1}) can't be divided by 0!")


# wrong inputs
square_root("Labas")
division(4, 0)
# good inputs
numbers_sum(1, 2, 3, 4, 5, 20, 12, 15, 7, 3)
square_root(4)
text_length("Hello World!")
division(4, 2)
