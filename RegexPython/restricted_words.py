# Parašykite funkciją, kuri į parametrus priimtų tekstą ir žodžių, kuriuos reikia jame išcenzūruoti sąrašą.
# Pvz, žodis "kvaraba" yra baisus keiksmažodis, ir mums reikia duotame tekste pakeisti k*****a. Pradėkite maždaug taip:
import re

pattern = re.compile(r'([a-ząčęėįšųūž])([a-ząčęėįšųūž]+)([a-ząčęėįšųūž])', re.UNICODE | re.IGNORECASE)
teksto_pattern = re.compile(r'\w+', re.UNICODE | re.IGNORECASE)
listas = []


def censor(given_text, *bad_word):
    paieska2 = teksto_pattern.findall(given_text)
    length = (len(paieska2))
    index = 0
    while 0 < length:
        if paieska2[index] == bad_word[0] or paieska2[index] == bad_word[1]:
            paieska = pattern.search(paieska2[index])
            zvaigzdute = len(paieska.group(2))
            cenzura = "*" * zvaigzdute
            b = f'{paieska.group(1)}{cenzura}{paieska.group(3)}'
            listas.append(b)
        else:
            listas.append(paieska2[index])
        index += 1
        length -= 1
    print(*listas)


censor('baisūs žodžiai, tokie kaip kvaraba, žaltys', 'kvaraba', 'žaltys')