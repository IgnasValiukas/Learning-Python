from statistics import mean, median

# Sukurtų sąrašą iš skaičių nuo 0 iki 50
sarasas = []

i = 0
for i in range(i, 50):
    sarasas.append(i)
    i += 1
print(sarasas)
# Padaugintų visus sąrašo skaičius iš 10 ir atspausdintų
# padauginta = map(lambda skaicius: skaicius * 10, sarasas)
padauginta = [skaicius * 10 for skaicius in sarasas]
print(padauginta)
# Atrinktų iš sąrašo skaičius, kurie dalinasi iš 7 ir atspausdintų
dalinasi = filter(lambda skaicius: skaicius % 7 == 0, sarasas)
print(list(dalinasi))
# Pakeltų visus sąrašo skaičius kvadratu ir atspausdintų.
# Šį sąrašą (list masyvą) priskirti naujam kintamajam.
kvadratu = [skaicius ** 2 for skaicius in sarasas]
print(kvadratu)
# Su kvadratų sąrašu (nauju kintamuoju) atliktų šiuos veiksmus: atspausdintų sumą, mažiausią ir didžiausią skaičių, vidurkį, medianą
print(f'Suma {sum(kvadratu)}')
print(f'Mažiausias skaičius {min(kvadratu)}')
print(f'Didžiausias skaičius {max(kvadratu)}')
print(f'Vidurkis {mean(kvadratu)}')
print(f'Mediana {median(kvadratu)}')
# Surūšiuotų ir atspausdintų kvadratų sąrašą atbulai
print(sorted(kvadratu, reverse=True))
