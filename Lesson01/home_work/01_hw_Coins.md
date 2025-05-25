# # Задание:
# 1. Создайте список из n-монеток, n - вводится с клавиатуры
# 2. Подбросьте(flip) все монетки. У каждой монетки в списке вызовите метод .flip()
# 3. Выведите соотношение выпавших орлов и решек в процентах
#
# Пояснение: когда вы создаете монетку, то она находится в неопределенном состоянии self.side = None, т.е.
# она находится у вас в руке и не выпала ни орлом ни решкой. \
# Монетка "определеяется" со стороной(орел/решка), только после того, как вы ее подбрасываете(вызываете метод flip())
#
import random


class Coin:
    def __init__(self):
        self.side = None

    def flip(self) -> None:
        """
        Подбрасывание монетки. # heads-орел/tails-решка
        """
        variants = ["heads", "tails"]
        self.side = random.choice(variants)  # random: heads/tails


# ```
if __name__ == '__main__':
    n = int(input("Кол-во монеток: "))
    result = {}
    for i in range(n):
        coin = Coin()
        coin.flip()
        if coin.side in result:
            result[coin.side] += 1
        else:
            result[coin.side] = 1
    print(f"соотношение выпавших орлов : {round(result['heads']*100/n,2)}%")
    print(f"соотношение выпавших и решек : {round(result['tails']*100/n,2)}%")
