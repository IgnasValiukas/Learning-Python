# Parašykite dekoratorių, kuris leidžia į funkciją įrašyti tik string tipo parametrus
# ir turi galimybę būti panaudotas kaip papildomas dekoratorius.

def string_decorator(function):
    def wrapper(text):
        if type(text) != str:
            return '<it must be string>'
        function_text = function(text)
        return function_text

    return wrapper


@string_decorator
def text_input(text):
    return text


@string_decorator
def reverse_text(text1):
    return text1[::-1]


given_text = "Hello User!"
given_number = 12
print(text_input(given_text))
print(text_input(given_number))
print(reverse_text(given_text))
print(reverse_text(given_number))
