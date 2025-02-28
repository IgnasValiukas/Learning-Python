import re

pattern = re.compile(r'(\w)(\w+)(\w)', re.UNICODE | re.IGNORECASE)


def censor(given_text, *censored_list):
    text_list = []
    sentence = re.split(r'(\W+)', given_text)

    for word in sentence:  # paima zodi is saraso
        if word.lower() in censored_list:  # zodi padaro is mazuju raidziu ir patikrina zodis yra cenzuruotu zodziu sarase
            censored_word = pattern.search(word)  # atskiria zodi pagal patterno grupes
            censored_word = f'{censored_word.group(1)}{"*" * len(censored_word.group(2))}{censored_word.group(3)}'  # antra grupe uzpildo zvaigzdutem (pagal grupes ilgi)
            text_list.append(censored_word)  # i sarasa prideda uzcenzuruota zodi
        else:
            text_list.append(word)  # i sarasa prideda tinkama zodi


    print("".join(text_list))


censor('baisūs žodžiai, tokie kaip kvaraba, žaltys, gaidys ir išpera. Blet nu tas tai irgi normalus', 'kvaraba',
       'žaltys', 'gaidys', 'blet', 'išpera')
