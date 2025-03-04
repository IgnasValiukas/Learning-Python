# Parašykite dekoratorių, bet kokios funkcijos vykdymo laikui fiksuoti.
# Galite patobulinti, pvz funkcijos (vardas), su tokiais ir tokiais argumentais vykdymo laikas - XX s.
# Ištestuokite, su funkcija, grąžinančia svetainės atsako kodą ir su funkcija, išrenkančia pirminius skaičius užduotame diapazone.

import requests
from time import time


def time_decorator(function):
    def execution_time(*args):
        start_time = time()
        given_func = function(*args)
        end_time = time()
        time_result = end_time - start_time
        return f'Function result {given_func}, \nFunction <{function.__name__}> execution time is {time_result:.20f}\n'  # :.20f formatuoja skaiciu, 20 nurodo skaiciu seka po kablelio

    return execution_time


@time_decorator
def web_request(*link):
    for i in link:
        r = requests.get(i)
        result = r.status_code
        links.append(result)
    return links


@time_decorator
def primary_numbers(*numbers):
    for number in numbers:
        if number > 1:
            for i in range(2, (number // 2) + 1):
                if (number % i) == 0:
                    break
            else:
                given_numbers.append(number)
    return given_numbers


given_numbers = []
links = []
print(web_request('http://www.cnn.com', 'https://www.astuteo.com/404/'))
print(primary_numbers(-1, 2, 3, 4, 5, 6, 7, 8, 9, 2, -5, 5))
