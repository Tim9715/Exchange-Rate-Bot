import requests
import json
from Settings import values

class ConvertionException(Exception):
    pass

class Misstakes:
    @staticmethod
    def misstake(value1 = str, value2 = str, count = str):
        if value1 == value2:
            raise ConvertionException(f'Невозможно перевести одинаковые валюты {value2} :|')
        try:
            value1_ticker = values[value1]
        except KeyError:
            raise ConvertionException(f'Не удалось обработать валюту {value1} :(')
        try:
            value2_ticker = values[value2]
        except KeyError:
            raise ConvertionException(f'Не удалось обработать валюту {value2} :(')
        try:
            amount = float(count)
        except ValueError:
            raise ConvertionException(f'Не удалось обработать количество {count} :(')
        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={value1_ticker}&tsyms={value2_ticker}')
        result = json.loads(r.content)[values[value2]] * int(count)
        return result