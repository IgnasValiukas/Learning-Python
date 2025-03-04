# Parašykite dekoratorių kuris riboja parametrų kiekį
# (tarkime, ne daugiau negu 2 parametrai funkcijai)

# dekoratorius
def two_parameters(function):
    if len(function) > 2 or len(function) < 2:
        return 'It must be Two numbers!'
    total_sum = sum(function)
    return f'Total sum: {total_sum}'


def numbers_sum(*args):
    numbers = args
    return numbers


print(two_parameters(numbers_sum(12, 2, 5)))
print(two_parameters(numbers_sum(12, 2)))

# def two_parameters(function):
#     def wrapper(*args):
#         if len(args) > 2 or len(args) < 2:
#             return 'It must be Two numbers!'
#         numbers = function(*args)
#         return f'Total sum: {numbers}'
#
#     return wrapper
#
#
# @two_parameters
# def numbers_sum(*args):
#     total_sum = sum(args)
#     return total_sum
#
#
# good_sum_function = numbers_sum(12, 2)
# bad_sum_function = numbers_sum(12, 2, 8)
# print(good_sum_function)
# print(bad_sum_function)
