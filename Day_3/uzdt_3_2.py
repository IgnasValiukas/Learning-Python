# Parašyti programą, kuri:
# Atspausdintų dabartinę datą ir laiką
# Atimtų iš dabartinės datos ir laiko 5 dienas ir juos atspausdintų
# Pridėti prie dabartinės datos ir laiko 8 valandas ir juos atspausdintų
# Atspausdintų dabartinę datą ir laiką tokiu formatu: 2019 03 08, 09:57:17
# Patarimas: naudoti datetime, timedelta (from datetime import timedelta)
# https://www.w3schools.com/python/python_datetime.asp

import datetime

date_now = datetime.datetime.now()
print("Today:", date_now)

print("Subtracted 5 days:", date_now - datetime.timedelta(days=5))
print("Added 8 hours:", date_now + datetime.timedelta(hours=8))

print("Updated format:", date_now.strftime("%Y %M %d, %H:%M:%S"))  # strftime() - string from time
