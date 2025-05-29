class Item:
    # TODO-0: копируем реализацию всех методов из практики или дописываем самостоятельно
    def __init__(self, name, weight, cost):
        self.name = name
        self.weight = weight
        self.cost = cost

    def show(self):
        return f"{self.name} вес:{self.weight} цена:{self.cost}"


class BackPack:  # рюкзак
    # TODO-0: копируем реализацию всех методов из практики или дописываем самостоятельно
    def __init__(self, max_weight: float):
        self.items = []
        self.max_weight = max_weight

    def add_item(self, item: Item) -> None:
        """
        Добавляет предмет(item) в этот рюкзак
        """
        current_weight = self.sum_weight()
        if current_weight + item.weight > self.max_weight:
            print(f"Предмет {item.name} слишком тяжелый")
        else:
            self.items.append(item)
            print(f"Предмет {item.name} добавлен в рюкзак")

    def show_items(self) -> None:
        """
        Вывод все предметы, содержащиеся в рюкзаке в виде нумерованного списка
        """
         for i, item in enumerate(self.items, 1):
            print(i, item.show())

    def sum_weight(self) -> float:
        """
        Возвращает суммарный вес всех предметов в рюкзаке
        """
        total_weight = 0
        for item in self.items:
            total_weight += item.weight

        return total_weight

    def find_heaviest_item(self):
        heaviest_item = max(self.items, key=lambda item: item.weight)
        print(f"Самый тяжелый предмет в рюкзаке: {heaviest_item.show()}")
        return heaviest_item

    def max_valuable(self):
        most_valuable = max(self.items, key=lambda item: item.cost / item.weight)
        print(f"Самый ценный предмет в рюкзаке: {most_valuable.show()}")


# Создаем рюкзак, указываем максимальный вес
backpack = BackPack(max_weight=5.5)

# TODO-1: Создаем 5-8 предметов и добавляем их в рюкзак
item1 = Item("Наушники", 0.3, 200)
item2 = Item("Банан", 0.12, 1)
item3 = Item("Кроссовки", 0.8, 120)
item4 = Item("Гантеля", 20, 40)
item5 = Item("Кастрюля", 1.5, 50)
item6 = Item("Персики", 3, 3)
item7 = Item("Одеяло", 1.3, 30)

# TODO-2: В рюкзаке найдите самый тяжелый предмет и выведите его на экран
#  поиск предмета реализуйте в виде метода .max_weight()
backpack.find_heaviest_item()
# TODO-3: В рюкзаке найдите самый ценный предмет и выведите его на экран
#  ценным предметом, считать предмет, с самым высоким значение цены на единицу веса
#  поиск предмета реализуйте в виде метода .max_valuable()
backpack.max_valuable()
