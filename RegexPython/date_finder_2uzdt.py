# Iš šio teksto atspausdinkite datų sąrašą.
import re

text = '''Workshop & Tutorial proposals: November 21, 2019
Notification of acceptance: December 1, 2019
Workshop & Tutorial websites online: December 18, 2019
Workshop papers: February 28, 2020
Workshop paper notifications: March 27, 2020
Workshop paper camera-ready versions: April 10, 2020
Tutorial material due (online): April 10, 2020'''

date_pattern = re.compile(
    r'''
    (January|February|March|April|May|June|July|August|September|October|November|December)  # month
    \s
    ([0-9]?[1-9]|1[0-9]?|2[0-9]|3[0-1]), # day
    \s
    (\d{4})  # year
    ''', re.X | re.M)
date_res = date_pattern.findall(text)
all_dates = []
for date in date_res:
    month, day, year = date
    all_dates.append(f'{month} {day} {year}')
print(all_dates)
