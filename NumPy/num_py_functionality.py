import numpy as np

# Sukurkite vektorių su skaičiais nuo 1 iki 9
vector_range = np.arange(1, 9)
print("Range 1-9: ",vector_range)
# Sukurkite vektorių iš 10 nulių
vector_zero = np.zeros(10)
print("With zeros: ",vector_zero)
# Sukurkite vektorių iš 10 vienetų
vector_ones = np.ones(10)
print("With ones: ",vector_ones)
# Sukurkite vektorių iš 10 ketvertų
vector_fours = np.ones(10)
vector_fours[:] = 4
# alternative
vector_fours_alternative = np.ones(10) * 4
print("With fours: ",vector_fours)
print("Alternative: ", vector_fours_alternative)
# Sukurkite vektorių iš lyginių skaičių nuo 0 iki 100
vector_even = np.arange(0, 100, 2)
print("Range 0-100 of even numbers:\n",vector_even)
