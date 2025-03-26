import pandas as pd

# 1
data_html = pd.read_html(
    'https://work.studentnews.eu/s/3695/75547-European-countries-the-table-language-population-capital-currency-phone-code-internet-code.htm')

table_data = data_html[1]
print(f'[1 uzdt.]\n{table_data.to_string()}')

# 2
# CSV
table_data.to_csv('csv_result.csv')
# XLSX
table_data.to_excel('excel_result.xlsx', sheet_name='European Countries')

# 3
accidents_data = pd.read_csv('top_20_CA_wildfires.csv')
print(f'{'*' * 160}\n[3 uzdt.]\nTable of fire accidents: \n{accidents_data.to_string()}')

# 4
unique_count = accidents_data['cause']
print(f'{'-' * 160}\n[4 uzdt.]\nUnique count of \'cause\': {unique_count.nunique()}')

# 5
unique_count = accidents_data['cause']
print(f'{'-' * 160}\n[5 uzdt.]\n{unique_count.value_counts()}')

# 6
year_count = accidents_data['year']
year_count_value = year_count.value_counts()
print(
    f'{'-' * 160}\n[6 uzdt.]\nThe year with the most fires: {year_count_value.idxmax()}, {year_count_value.max()} accidents')

# 7
casualties_count = accidents_data['deaths'] > 0
print(f'{'-' * 160}\n[7 uzdt.]\nFire accidents count in which people died: {casualties_count.sum()}')

# 8
sorted_values = accidents_data.sort_values('year', ascending=False)
print(f'{'-' * 160}\n[8 uzdt.]\nSorted rows by year:\n{sorted_values.to_string()}')

# 9
months = {1: 'January',
          2: 'February',
          3: 'March',
          4: 'April',
          5: 'May',
          6: 'June',
          7: 'July',
          8: 'August',
          9: 'September',
          10: 'October',
          11: 'November',
          12: 'December'}


def change_months_format(given_month):
    find_keys = filter(lambda key: months[key] == given_month, months)
    keys = list(find_keys)
    result = str(keys).replace('[', '').replace(']', '')
    return result


accidents_data['month'] = accidents_data['month'].apply(change_months_format)
print(f'{'-' * 160}\n[9 uzdt.]\nMonth name converted to number:\n{accidents_data.to_string()}')

# 10
# 10.1
wikipedia_html = pd.read_html('https://lt.wikipedia.org/wiki/S%C4%85ra%C5%A1as:Lietuvos_miestai_pagal_gyventojus',
                              index_col=1)
lithuania_cities = wikipedia_html[0]
wikipedia_result = lithuania_cities.head().to_string()
print(f'{'*' * 160}\n[10.1 uzdt.]\nLithuanian cities by population:\n{wikipedia_result}')

# 10.2
columns = [col for col in lithuania_cities.columns if 'm.' in col]
convert = lambda col: pd.to_numeric(col, errors='coerce').fillna(0).astype(int)
lithuania_cities[columns] = lithuania_cities[columns].apply(convert)

print(f'{'-' * 160}\n[10.2 uzdt.]\nConverted values to int:\n')
lithuania_cities.loc[:, columns].info()
