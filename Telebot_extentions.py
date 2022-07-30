import requests


class APIException(Exception):
    pass


class Converter:
    @staticmethod
    def get_exchange_amount(base_curr, exchange_curr, amount):
        data = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()

        if base_curr != "RUB":
            try:
                nominal_base = data["Valute"][f"{base_curr}"]["Nominal"]
            except KeyError:
                raise APIException(f'Валюты {base_curr} в базе данных нет!')
        elif exchange_curr != "RUB":
            try:
                nominal_exchange = data["Valute"][f"{exchange_curr}"]["Nominal"]
            except KeyError:
                raise APIException(f'Валюты {exchange_curr} в базе данных нет!')
        else:
            pass
        try:
            amount = float(amount)
        except ValueError:
            raise APIException(f'Не удалось обработать количество {amount}!')

        if exchange_curr == "RUB":
            nominal_base = data["Valute"][f"{base_curr}"]["Nominal"]
            exchange_value = data["Valute"][f"{base_curr}"]["Value"] / nominal_base
        elif base_curr == "RUB":
            nominal_exchange = data["Valute"][f"{exchange_curr}"]["Nominal"]
            exchange_value = 1 / (data["Valute"][f"{exchange_curr}"]["Value"] / nominal_exchange)
        else:
            nominal_base = data["Valute"][f"{base_curr}"]["Nominal"]
            nominal_exchange = data["Valute"][f"{exchange_curr}"]["Nominal"]
            exchange_value = (data["Valute"][f"{base_curr}"]["Value"] / nominal_base) / (
                    data["Valute"][f"{exchange_curr}"]["Value"] / nominal_exchange)
        exchange_amount = exchange_value * float(amount)

        return exchange_amount
