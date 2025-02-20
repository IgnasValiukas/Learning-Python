import datetime
from datetime import date
from datetime import date as data

# Importuoti modulį datetime. Atsispausdinti šiandienos datą ir laiką kartu
today_date = datetime.date.today()
now_time = datetime.datetime.now().time()
print(f'import datetime: {today_date} {now_time}')
# Iš paketo datetime importuoti modulį date. Atsispausdinti šiandienos datą
today_date1 = date.today()
print(f'from datetime import date: {today_date1}')
# Iš paketo datetime importuoti modulį date kaip data (as data). Atsispausdinti šiandienos datą.
today_date2 = data.today()
print(f'from datetime import date as data: {today_date2}')