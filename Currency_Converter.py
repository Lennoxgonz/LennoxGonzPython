from dis import pretty_flags
from locale import currency
from urllib import response
from requests import get
from pprint import PrettyPrinter

BASE_URL = "https://free.currconv.com/"
API_KEY = "61d46b0c0e18205df15f"

printer = PrettyPrinter()


def get_currencies():
    endpoint = f"api/v7/currencies?apiKey={API_KEY}"
    url = BASE_URL + endpoint
    data = get(url).json()['results']
    
    data = list(data.items())
    data.sort()

    return data

def print_currencies(currencies):
    for name, currency in currencies:
        name = currency['currencyName']
        _id = currency['id']
        symbol = currency.get("currencySymbol", "")
        print(f"{_id} - {name} - {symbol}")

def exchange_rate(currency1, currency2):
    endpoint = f"api/v7/convert?q={currency1}_{currency2}&compact=ultra&apiKey={API_KEY}"
    url = BASE_URL + endpoint
    data = get(url).json()

    if len(data) == 0:
        print('Invalid currencies.')
        return

    rate = list(data.values())[0]
    print(f"{currency1} -> {currency2} = {rate}")

    return rate

def convert(currency1, currency2, amount):
    rate = exchange_rate(currency1, currency2)
    if rate is None:
        return

    try:
        amount = float(amount)
    except:
        print("Invalid amount.")
        return

    converted_ammount = rate * amount * amount
    print(f"{amount} {currency1} is equal to {converted_ammount} {currency2}")
    return converted_ammount

def old(currency1, currency2, date):
    endpoint = f"api/v7/convert?q={currency1}_{currency2}&compact=ultra&date={date}&apiKey={API_KEY}"
    url = BASE_URL + endpoint
    data = get(url).json()
    oldrate = list(data.values())[0]
    print(f"{currency1} -> {currency2} = {oldrate}")


def main():
    currencies = get_currencies()

    print("Welcome to the currency converter!")
    print("List - lists the different currencies")
    print("Convert - convert from one currency to another")
    print("Rate - get the exchange rate of two currencies")
    print("Old - Shows rates for a certain day within the past year")
    print()

    while True:
        command = input("Enter a command(q to quit): ").lower()

        if command == "q":
            break
        elif command == "list":
            print_currencies(currencies)
        elif command == "convert":
            currency1 = input("Enter a base currency: ").upper()
            currency2 = input("Enter a currency to convert to: ").upper()
            amount = input(f"Enter an ammount in {currency1}: ").upper()
            convert(currency1, currency2, amount)
        elif command == "rate":
            currency1 = input("Enter a base currency: ").upper()
            currency2 = input("Enter a currency to convert to: ").upper()
            exchange_rate(currency1, currency2)
        elif command == "old":
            currency1 = input("Enter a base currency: ").upper()
            currency2 = input("Enter a currency to convert to: ").upper()
            date = input("Enter a date(within the past year)[yyyy-mm-dd]: ")
            old(currency1, currency2, date)
        else:
            print("Unknown Command")    

main()