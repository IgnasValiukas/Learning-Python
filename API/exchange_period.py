# sukurkite programą, kuri pagal parametruose pateiktas valiutų poras, periodo pradžios ir pabaigos datą surastų dienas kai:
# kursas buvo aukščiausias ir kai kursas buvo žemiausias

import requests

currency_type = [
    'AUD', 'BGN', 'BRL', 'CAD', 'CHF', 'CNY', 'CZK', 'DKK', 'EUR', 'GBP', 'HKD', 'HUF',
    'IDR', 'ILS', 'INR', 'ISK', 'JPY', 'KRW', 'MXN', 'MYR', 'NOK', 'NZD', 'PHP', 'PLN', 'RON',
    'RUB', 'SEK', 'SGD', 'THB', 'TRY', 'USD', 'ZAR']


def rate_interval(date_from, date_to, currency_from, currency_to):
    response = requests.get(
        f'https://api.frankfurter.dev/v1/{date_from}..{date_to}?base={currency_from}&symbols={currency_to}')
    data = response.json()

    rates = data['rates']

    dates_list = list(rates.keys())
    first_date = dates_list[0]
    first_rate = rates[first_date][currency_to]

    max_rate = first_rate
    min_rate = first_rate
    max_rate_date = first_date
    min_rate_date = first_date

    for date in dates_list:
        exchange_rate = rates[date][currency_to]

        if exchange_rate > max_rate:
            max_rate = exchange_rate
            max_rate_date = date

        if exchange_rate < min_rate:
            min_rate = exchange_rate
            min_rate_date = date

    print(f'\nCurrency pair {currency_from}-{currency_to} for the period {date_from} to {date_to}:')
    print(f'Maximum Exchange Rate: {max_rate} on {max_rate_date}')
    print(f'Minimum Exchange Rate: {min_rate} on {min_rate_date}')


while True:
    print("Available currencies:")
    print(", ".join(currency_type))
    print("\n---Leave blank input and press Enter to exit---")
    print("For testing purpose dates: from 2020-01-01 to 2024-01-01")
    date_from_input = input("Add data from (yyyy-mm-dd): ")
    if not date_from_input: break
    date_to_input = input("Add data to (yyyy-mm-dd): ")
    currency_from_input = input("Type the currency you want to convert from: ").upper()
    currency_to_input = input("Type the currency you want to convert to: ").upper()

    if currency_from_input in currency_type and currency_to_input in currency_type:
        try:
            rate_interval(date_from_input, date_to_input, currency_from_input, currency_to_input)
            print("-" * 50)
        except KeyError:
            print("\nCurrency is not available!\n")
    else:
        print("\nInvalid input!")
