# Задание:
1. Создайте список из n-монеток, n - вводится с клавиатуры
2. Подбросьте(flip) все монетки. У каждой монетки в списке вызовите метод .flip()
3. Выведите соотношение выпавших орлов и решек в процентах

Пояснение: когда вы создаете монетку, то она находится в неопределенном состоянии self.side = None, т.е.
она находится у вас в руке и не выпала ни орлом ни решкой. \
Монетка "определеяется" со стороной(орел/решка), только после того, как вы ее подбрасываете(вызываете метод flip())

```python
import random


class Coin:
    def __init__(self):
        self.side = None

    def flip(self) -> None:
        """
        Подбрасывание монетки. # heads-орел/tails-решка
        """
        sides = ["heads", "tails"]
        self.side = random.choice(sides)  # random: heads/tails

n = int(input("Введите количество монет: "))
coins = [Coin() for _ in range(n)]
for coin in coins:
    coin.flip()
    print(coin.side)

heads_count = sum(1 for coin in coins if coin.side == "heads")
tails_count = n - heads_count

heads_percentage = round((heads_count / n) * 100, 1)
tails_percentage = round((tails_count / n) * 100, 1)

print(f"Орлы: {heads_percentage}%\nРешки: {tails_percentage}%")
```
