import numpy as np
import pandas as pd

top_left = pd.read_csv('top1-25-1.csv')
top_right = pd.read_csv('top1-25-2.csv')
bottom_left = pd.read_csv('top26-50-1.csv')
bottom_right = pd.read_csv('top26-50-2.csv')

# 1. Sulipdykite iš 4 fragmentų vieną lentelę
top = pd.merge(top_left, top_right)
bottom = pd.concat([bottom_left, bottom_right], axis=1)
table = pd.concat([top, bottom])

# 2. Sutvarkykite indeksą - padarykite, kad prasidėtų nuo 1
table = table.reset_index().drop(columns="index")
table.index += 1
print(f'{table.to_string()}\n{'-' * 235}')

# 3. Sukurkite grupavimo pagal žanrą objektą
group = table.groupby('Genre')
print(f'{group}\n{'-' * 235}')

# 4. Kokie žanrai lentelėje pasitaiko daugiau negu 3 kartus
genre_count = group.size()
print(genre_count)
filtered_genres = genre_count[genre_count > 3]
print(f'{filtered_genres}\n{'-' * 235}')

# 5. Koks žanras pats populiariausias ir mažiausiai populiarus
most_popular_index = table['Popularity'].idxmax()
least_popular_index = table['Popularity'].idxmin()
most_popular_genre = table.loc[most_popular_index, 'Genre']
least_popular_genre = table.loc[least_popular_index, 'Genre']
print(f"Most popular - {most_popular_genre} ({table.loc[most_popular_index, 'Popularity']})")
print(f"Least popular - {least_popular_genre} ({table.loc[least_popular_index, 'Popularity']})\n{'-' * 235}")
