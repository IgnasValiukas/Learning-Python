# Sukurkite vektorių iš integer reikšmių nuo 1 iki 100. Priskirkite kintamąjam ir atlikite šiuos veiksmus:
# Iš jo ištraukite visus skaičius, didesnius už 90
# Iš pradinio vektoriaus ištraukite visus skaičiaus 7 kartotinius

import numpy as np

vector = np.arange(1, 101)
greater_than = vector[vector > 90]
multiple_number = vector[vector % 7 == 0]
print("Vector range 1-100:\n", vector)
print("\nGreater than 90:\n", greater_than)
print("\nMultiple by 7:\n", multiple_number)
