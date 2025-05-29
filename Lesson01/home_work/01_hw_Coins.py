import random

class Coin:
    def __init__(self):
        self.side = None

    def flip(self):
        self.side = random.choice(["Heads", "Tails"])

    def __str__(self):
        return f"coin: {self.side}"

num_coins = 10

coins = [Coin() for _ in range(num_coins)]

for coin in coins:
    coin.flip()

num_heads = 0
num_tails = 0

for coin in coins:
    if coin.side == "Heads":
        num_heads +=1
    else:
        num_tails +=1

num_tails = num_tails*100/num_coins
num_heads = num_heads*100/num_coins

print(f"Procentaj Tails: {num_tails}%")
print(f"Procentaj Heads: {num_heads}%")

#Vladimir Ghilas
