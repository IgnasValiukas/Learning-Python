# Sukurkite matricą iš 25 narių, pradedant 1, baigiant 25. Priskirkite ją kintamąjam.
# Iš anksčiau sukurtos matricos ištraukite skaičių 12
# Iš anksčiau sukurtos matricos ištraukite paskutinę eilutę.
# Iš anksčiau sukurtos matricos ištraukite submatricą:
#       [1 2 3]
#       [6 7 8]
#       [11 12 13]
# Iš anksčiau sukurtos matricos ištraukite submatricą:
#       [7 8 9 10]
#       [12 13 14 15]
#       [17 18 19 20]
# Iš anksčiau sukurtos matricos ištraukite submatricą:
#       [16 17 18]
#       [21 22 23]

import numpy as np

number_range = np.arange(1, 26)
matrix = number_range.reshape(5,5)
print("Matrix:\n", matrix)
print("\nExtracted number: ", matrix[2,1])
print("\nExtracted last row: ", matrix[-1:])
print("\nExtracted First submatrix:\n", matrix[0:3, 0:3])
print("\nExtracted Second submatrix:\n", matrix[1:4, 1:])
print("\nExtracted Third submatrix:\n", matrix[-2:, 0:3])

