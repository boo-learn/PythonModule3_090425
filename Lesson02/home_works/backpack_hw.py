class Item:
    def __init__(self, name: str, weight: float, cost: int):
        self.name = name  # Название предмета
        self.weight = weight  # Вес предмета, в килограммах
        self.cost = cost  # Цена предмета, пусть будет, в рублях

    def show(self):
        return f"{self.name} вес:{self.weight} цена:{self.cost}"


class BackPack:  # рюкзак
    def __init__(self, max_weight):
        self.items = []  # Предметы, которые хранятся в рюкзаке
        self.max_weight = max_weight

    def add_item(self, item: Item) -> None:
        """
        Добавляет предмет(item) в этот рюкзак
        """
        if self.sum_weight() + item.weight > self.max_weight:
            print(f"Предмет {item.name} слишком тяжелый")
        else:
            self.items.append(item)
            print(f"Предмет {item.name} добавлен в рюкзак")

    def show_items(self) -> None:
        """
        Выводит(print'ом) все предметы, содержащиеся в рюкзаке в виде нумерованного списка
        """
        for i, item in enumerate(self.items, start=1):
            print(i, item.show())

    def sum_weight(self) -> float:
        """
        Возвращает суммарный вес всех предметов в рюкзаке
        """
        total_weight = 0
        for item in self.items:
            total_weight += item.weight

        return total_weight

    def sum_cost(self) -> int:
        """
        Возвращает суммарную стоимость всех предметов в рюкзаке
        """
        total_cost = 0
        for item in self.items:
            total_cost += item.cost

        return total_cost

    def add_items(self, items: list[Item]):
        """
        :param items: Список вещей(объектов класса Item)
        """
        # реализуйте метод так, чтобы из переданного списка предметов выбиралось и помещалось в рюкзак,
        # максимальное количество, с учетом ограничения общего веса в рюкзаке. Т.е. берем самые легкие предметы.
        sorted_items = sorted(items, key=lambda item: item.weight)
        for item in sorted_items:
            self.add_item(item)

    def maximum_weight(self):
        # В рюкзаке найдите самый тяжелый предмет и выведите его на экран
        #  поиск предмета реализуйте в виде метода .maximum_weight()
        max_weight_item = sorted(self.items, key=lambda item: item.weight, reverse=True)[0]
        print(f"Самый тяжелый предмет в рюкзаке: {max_weight_item.show()}")

    def max_valuable(self):
        #  В рюкзаке найдите самый ценный предмет и выведите его на экран
        #  ценным предметом, считать предмет, с самым высоким значение цены на единицу веса
        #  поиск предмета реализуйте в виде метода .max_valuable()
        max_valuable_item = sorted(self.items, key=lambda item: item.cost, reverse=True)[0]
        print(f"Самый ценный предмет в рюкзаке: {max_valuable_item.show()}")


# Создаем рюкзак, указываем максимальный вес
backpack = BackPack(max_weight=7)

items = [
    Item("Гиря", 25, 500),
    Item("Арбуз", 4, 300),
    Item("Ноутбук", 2.5, 22500),
    Item("Кот", 0.5, 250),
    Item("Трос", 3, 150),
]

backpack.add_items(items)

backpack.show_items()

backpack.maximum_weight()

backpack.max_valuable()
