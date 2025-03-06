def sum_number(first_number, second_number, third_number):
    try:
        return float(first_number + second_number + third_number)
    except TypeError:
        return "Type must be Integer or Float!"


def sum_list(given_list):
    try:
        return sum(given_list)
    except TypeError:
        return "Type must be Integer or Float!"


def find_max(*args):
    try:
        return max([number for number in args])
    except TypeError:
        return "Type must be Integer or Float!"


def reverse_string(given_string):
    try:
        return given_string[::-1]
    except TypeError:
        return "Type must be String!"
    except KeyError:
        return f"Action is not valid with type: {type(given_string)}"
