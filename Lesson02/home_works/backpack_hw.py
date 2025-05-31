class Item:
    def __init__(self, name, weight, cost):
        self.name = name  # Название предмета
        self.weight = weight  # Вес предмета, в килограммах
        self.cost = cost  # Цена предмета, пусть будет, в рублях

    def show(self):
        return f"{self.name} вес:{self.weight} цена:{self.cost}"


class BackPack:  # рюкзак
    def __init__(self, max_weight: float):
        self.items = []  # Предметы, которые хранятся в рюкзаке
        self.max_weight = max_weight
        self.current_weight = 0.0

    def add_item(self, item: Item) -> None:
        current_weight = self.sum_weight()
        if current_weight + item.weight > self.max_weight:
            print(f"Предмет {item.name} слишком тяжелый")
        else:
            self.items.append(item)
            print(f"Предмет {item.name} добавлен в рюкзак")

    def sum_weight(self) -> float:
        total_weight = 0
        for item in self.items:
            total_weight += item.weight

        return total_weight

    def show_items(self) -> None:
        for i, item in enumerate(self.items, 1):
            print(i, item.show())

    def sum_cost(self) -> int:
        total_cost = 0
        for item in self.items:
            total_cost += item.cost

        return total_cost

    def max_weightt(self):
        if not self.items:
            print("Рюкзак пустой")
            return None
        heaviest_item = max(self.items, key=lambda item: item.weight)
        print(f"Самый тяжелый предмет: {heaviest_item.show()}")
        return heaviest_item

    def max_valuable(self):
        if not self.items:
            print("Рюкзак пустой")
            return None
        most_valuable = max(self.items, key=lambda item: item.cost / item.weight)
        print(f"Самый ценный предмет: {most_valuable.show()}")
        return most_valuable


backpack = BackPack(max_weight=7)

items = [
    Item("Гиря", 25, 500),
    Item("Арбуз", 4, 300),
    Item("Ноутбук", 2.5, 22500),
    Item("Кот", 0.5, 250),
    Item("Трос", 3, 150),
]
for item in items:
    backpack.add_item(item)
backpack.show_items()
backpack.max_weightt()
backpack.max_valuable()

#Vladimir Ghilas
