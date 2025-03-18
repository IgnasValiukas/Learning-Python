# Sukurkite programą, kuri duoda įvestos valiutų poros dabartinį kursą.
# Naudokitės Frankfurter API

import requests

currency_type = [
    'AUD', 'BGN', 'BRL', 'CAD', 'CHF', 'CNY', 'CZK', 'DKK', 'EUR', 'GBP', 'HKD', 'HUF',
    'IDR', 'ILS', 'INR', 'ISK', 'JPY', 'KRW', 'MXN', 'MYR', 'NOK', 'NZD', 'PHP', 'PLN', 'RON',
    'RUB', 'SEK', 'SGD', 'THB', 'TRY', 'USD', 'ZAR']


def exchange(from_currency, to_currency):
    currency = requests.get(f'https://api.frankfurter.dev/v1/latest?base={from_currency}&symbols={to_currency}')
    result = currency.json()
    exchange_rate = result["rates"][to_currency]
    print(f'\n{from_currency}-{to_currency}: {exchange_rate}')


while True:
    print("Available currencies:")
    print(", ".join(currency_type))
    print("\n---Leave blank input and press Enter to exit---")
    input_from = input("Type the currency you want to convert from: ").upper()
    if not input_from: break
    input_to = input("Type the currency you want to convert to: ").upper()

    if input_from in currency_type and input_to in currency_type:
        try:
            exchange(input_from, input_to)
            print("-" * 50)
        except KeyError:
            print("\nCurrency is not available!\n")
    else:
        print("\nInvalid currency selection!")
