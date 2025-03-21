# Sukurkite tokią matricą:
# [[0.025 0.05 0.075 0.1 0.125 0.15 0.175 0.2],
#  [0.225 0.25 0.275 0.3 0.325 0.35 0.375 0.4],
#  [0.425 0.45 0.475 0.5 0.525 0.55 0.575 0.6],
#  [0.625 0.65 0.675 0.7 0.725 0.75 0.775 0.8],
#  [0.825 0.85 0.875 0.9 0.925 0.95 0.975 1.]])

# Sukurkite tokią matricą (sveiki sk. nuo 2 iki 1000 iš kurių traukiasi sveika šaknis):
# [[  4   9  16  25  36],
#  [ 49  64  81 100 121],
#  [144 169 196 225 256],
#  [289 324 361 400 441],
#  [484 529 576 625 676],
#  [729 784 841 900 961]])

import numpy as np

number_range = np.arange(0.025, 1.025, 0.025)
matrix = number_range.reshape(5, 8)
print("Matrix numbers 0.025 -> 1:\n", matrix)

int_range = np.arange(2, 1000)
sqrt_root = np.sqrt(int_range)
check_root = int_range[sqrt_root % 1 == 0]
matrix_filtered = check_root.reshape(6, 5)
print("\nNumbers from 2 to 1000 that have an integer square root:\n", matrix_filtered)
