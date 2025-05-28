# Задание: Создать удобную структуру для работы с курсами валют на определенную дату
# Курсы валют будем брать с этого сайта: https://www.cbr-xml-daily.ru/ .
# Нас будут интересовать только курсы доллара и евро.
# Как получить курс по API со стороннего сайта - смотри в helpers/request_currency.py
import requests


class Currency:
    def __init__(self, type):
        self.type = type

    def __getitem__(self, item):
        valute_map = {
            "usd": "USD",
            "euro": "EUR",
        }
        day, month, year = item.split('.')
        url = f'https://www.cbr-xml-daily.ru/archive/{year}/{month}/{day}/daily_json.js'
        try:
            # Отправляем запрос на указанный url
            response = requests.get(url)
            return f"{item} {valute_map[self.type]}: {response.json()['Valute'][valute_map[self.type]]['Value']}"
        except:
            return f"Ошибка в данных"


usd = Currency("usd")  # Создаем валюту "Доллар"
euro = Currency("euro")  # Создаем валюту "Евро"
print(usd['02.09.2020'])  # ← получение курса доллара на указанную дату
print(euro['12.10.2018'])  # ← получение курса евро на указанную дату
print(euro['12.14.2018'])  # ← в случае некорректной выбрасываем исключение
