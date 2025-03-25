import pandas as pd

df = pd.read_csv('miestai_isvalyti.csv')

# Atspausdinkite pirmas penkias df eilutes
first_five = df.head()  # other way to do: five = df.iloc[:5]
print(f'First Five:\n{first_five}\n{'-' * 100}')

# Padarykite, kad indeksas būtų stulpelis 'Miestas', ir kad šis pasikeitimas išliktų originale
df.set_index('Miestas', inplace=True)
print(f'Changed Index:\n{df}\n{'-' * 100}')

# Ištraukite reikšmę, kiek gyventojų gyveno Marijampolėje 1923 m.
marijampole_1923 = df.loc['Marijampolė', '1923']
print(f'Marijampolė population in 1923: {marijampole_1923}\n{'-' * 100}')

# Ištraukite stulpelį '1897' ir atspausdinkite pirmas penkias eilutes
year_1897 = df['1897'].head()
print(f'First Five of 1897:\n{year_1897}\n{'-' * 100}')

# Ištraukite stulpelius '2019', '1970', '1923' ir atspausdinkite pirmas 10 eilučių
custom_years = df[['2019', '1970', '1923']].head(10)
print(f'First 10 data:\n{custom_years}\n{'-' * 100}')

# Pridėkite stulpelį su numeracija
df['Numbering'] = range(1, len(df) + 1)  # df['Numbering'] = range(1, 104)
print(f'Added numbering:\n{df}\n{'-' * 100}')

# Ištraukite miestus nuo 30 iki 39 pozicijos
cities = df.iloc[range(30, 40)]
print(f'Cities in range of 30-39:\n{cities}\n{'-' * 100}')

# Ištraukite miestus kurių dar nebuvo 1959 m.
zero_data = df.loc[df['1959'] == 0]
print(f'Cities that didn\'t exist in 1959:\n{zero_data['1959']}\n{'-' * 100}')

# Ištraukite miestus kurie 1897 m. turėjo daugiau gyventojų, negu 2019 m.
compare_cities = df.loc[df['1897'] > df['2019']]
print(f'Cities that had more population in 1897 than in 2019:\n{compare_cities[['2019', '1897']]}\n{'-' * 100}')

# Ištraukite miestus kuriuose nuo 2011 m. iki 2019 m. padaugėjo gyventojų
cities_increased = df.loc[df['2011'] < df['2019']]
print(f'Cities where the population increased:\n{cities_increased[['2019', '2011']]}\n{'-' * 100}')

# Ištraukite miestus kuriuose gyventojų skaičius nuosekliai mažėjo nuo pat 1897 m.
years = ['1897', '1923', '1959', '1989', '2001', '2011', '2019']
decreasing_cities = df.loc[(df[years].diff(axis=1).iloc[:, 1:] < 0).all(axis=1)]
print(f'Cities that have been steadily decreasing:\n{decreasing_cities[['2019', '2011']]}\n{'-' * 100}')

# Suraskite labiausiai procentaliai gyventojų skaičiumi padidėjusį ir sumažėjusį miestus nuo 1989 m.
df_percentage = ((df['2019'] - df['1897']) / df['1897']) * 100
print(df_percentage)
percentage_increased = df_percentage.idxmax()
percentage_decreased = df_percentage.idxmin()
print(f'{percentage_increased} had the highest increase, and {percentage_decreased} the biggest decrease.\n{'-' * 100}')

# Nuresetinkite indeksą
df.reset_index(inplace=True)
print(f'Restored index:\n{df}')
