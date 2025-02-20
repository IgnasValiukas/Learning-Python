#Pakeisti 3 užduoti taip, kad neteisingai įvedus duomenis ar įvykus klaidoms,
# programos mestų norimas klaidas lietuvių kalba (panaudoti try/except)
# Example: 1998-04-23 13:24:55

import datetime

current_date = datetime.datetime.now()
date_format = "%Y-%m-%d %H:%M:%S"
print("I will make your life easier ;) >>> 1998-04-23 13:24:55 <<<")

while True:
    try:
        date_input = input("Write date that contains 'Y-M-D H:M:S': ")
        given_date = datetime.datetime.strptime(date_input, date_format)  # strptime() - String parse time
        difference = (current_date - given_date)
        days_difference = difference.days
        seconds_difference = difference.total_seconds()
        print(f"\nResult of ({given_date.date()}):")
        print("Years:", round(days_difference / 365), "|  Months:", round(days_difference / 12),
              "|  Days:", days_difference)
        print("Hours:", round((seconds_difference / 60) / 60), "|  Minutes:", round(seconds_difference / 60),
              "|  Seconds:", seconds_difference)
        break
    except ValueError:
        print("\nWrong date format!\n", "(Date example >>> 1998-04-23 13:24:55 <<<)")
        print("\nPlease try again.")