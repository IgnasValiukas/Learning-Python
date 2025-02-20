# Parašyti programą, kuri:
# Leistų vartotojui įvesti norimą datą ir laiką (pvz. gimtadienį)
# Paskaičiuotų ir atspausdintų, kiek nuo įvestos datos ir laiko praėjo:
# Metų
# Mėnesių
# Dienų
# Valandų
# Minučių
# Sekundžių
# Kadangi tiksliai galima paskaičiuoti tik dienas ir sekundes, metus, mėnesius ir t.t. paskaičiuokite apytiksliai.
# Patarimas: naudoti datetime, .days, .total_seconds()
# Example: 1998-04-23 13:24:55

import datetime

current_date = datetime.datetime.now()
date_format = "%Y-%m-%d %H:%M:%S"
print("I will make your life easier ;) 1998-04-23 13:24:55")
date_input = input("Write date that contains 'Y-M-D H:M:S': ")
given_date = datetime.datetime.strptime(date_input, date_format)  # strptime() - String parse time
difference = (current_date - given_date)
days_difference = difference.days
seconds_difference = difference.total_seconds()
print(f"\nResult of ({given_date.date()}):")
print("Years:", int(days_difference/365), "|  Months:", int(days_difference/12),
      "|  Days:", days_difference)
print("Hours:", int((seconds_difference/60)/60), "|  Minutes:", int(seconds_difference/60),
      "|  Seconds:", seconds_difference)
