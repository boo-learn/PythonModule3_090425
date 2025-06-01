# Задание: Создать удобную структуру для работы с курсами валют на определенную дату
# Курсы валют будем брать с этого сайта: https://www.cbr-xml-daily.ru/ .
# Нас будут интересовать только курсы доллара и евро.
import requests
from datetime import datetime


class Currency:
    def __init__(self, type):
        self.type = type.lower()

    def __getitem__(self, item):
        valute_name = {
            "usd": "USD",
            "euro": "EUR"
        }

        if self.type not in valute_name:
            return f"Неизвестная валюта: {self.type}"

        try:
            date = datetime.strptime(item, "%d.%m.%Y")
        except ValueError:
            return f"Неверный формат даты: {item}. Используй ДД.ММ.ГГГГ"

        code = valute_name[self.type]
        url = f"https://www.cbr-xml-daily.ru/archive/{date.strftime('%Y/%m/%d')}/daily_json.js"

        try:
            response = requests.get(url)
        except requests.RequestException:
            return f"Невозможно получить курс для: {item}"

        if response.status_code != 200:
            return f"Невозможно получить курс для: {item}"

        try:
            data = response.json()
        except ValueError:
            return f"Ошибка в данных для: {item}"

        try:
            value = data["Valute"][code]["Value"]
            return f"{item} {code}: {value}"
        except KeyError:
            return f"Курс для {code} недоступен на дату {item}"

usd = Currency("usd")
euro = Currency("euro") 
print(usd['02.09.2020']) 
print(euro['12.10.2018']) 
print(euro['12.14.2018']) 

#Vladimir Ghilas
