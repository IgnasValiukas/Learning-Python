# Sukurkite vektorių iš 20 atsitiktinių reikšmių nuo 0 iki 1.
# Suraskite didžiausią reikšmę masyve ir jos indeksą.
# Suraskite mažiausią reikšmę ir jos indeksą.
# Atspausdinkite šio vektoriaus duomenų tipą.

import numpy as np

vector = np.random.rand(20)
print(f'Vector:\n{vector}\n')
max_value = max(vector)
min_value = min(vector)
index_max_value = vector.argmax()
index_min_value = vector.argmin()
vector_type = vector.dtype
print(f'Max value {max_value}, Index: {index_max_value}')
print(f'Min value {min_value}, Index: {index_min_value}')
print(f'Vector type: {vector_type}\n')


