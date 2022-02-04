import requests
import json
from config import keys


class ConvertionExeption(Exception):
    pass

class CurrencyCalc:
    @staticmethod
    def get_price(quote: str, base: str, amount: str):
        if quote == base:
            raise ConvertionExeption(f'Вы ввели одинаковую валюту: {base}.')

        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise ConvertionExeption(f'Проверьте правильность ввода названия валюты: {quote}.')

        try:
            base_ticker = keys[base]
        except KeyError:
            raise ConvertionExeption(f'Проверьте правильность ввода названия валюты: {base}.')

        try:
            amount = float(amount)
        except ValueError:
            raise ConvertionExeption(f'Проверьте введенное количество валюты для конвертации: {amount}.')

        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={quote_ticker}&tsyms={base_ticker}')
        total_base = json.loads(r.content)[keys[base]]

        return total_base * amount

