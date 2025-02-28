# Atspausdinkite tą patį teksta taip:
#  1.
#  Event: Workshop & Tutorial proposals
#  Date: November 21, 2019
#  2.
#  Event: Notification of acceptance
#  Date: December 1, 2019
#  ir t.t.
import re

text = '''
Workshop & Tutorial proposals: November 21, 2019
Notification of acceptance: December 1, 2019
Workshop & Tutorial websites online: December 18, 2019
Workshop papers: February 28, 2020
Workshop paper notifications: March 27, 2020
Workshop paper camera-ready versions: April 10, 2020
Tutorial material due (online): April 10, 2020
'''

date_pattern = re.compile(
    r'''
    (January|February|March|April|May|June|July|August|September|October|November|December)  # month
    \s
    ([0-9]?[1-9]|1[0-9]?|2[0-9]|3[0-1]), # day
    \s
    (\d{4})  # year
    ''', re.X)
text_pattern = re.compile(r'^(.*)(?=:)', re.M)


def split_text(given_text):
    date_res = date_pattern.findall(given_text)
    text_res = text_pattern.findall(given_text)
    for index in range(len(text_res)):
        print(f'{index + 1}.')
        print(f'Event: {text_res[index]}')
        month, day, year = date_res[index]
        print(f'Date: {month} {day} {year}')


split_text(text)
