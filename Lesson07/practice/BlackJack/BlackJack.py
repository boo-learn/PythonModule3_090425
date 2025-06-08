from classes import Deck, Card
from tools import sum_points


def log(message):
    print(message)
    with open("game_log.txt", "a", encoding="utf-8") as f:
        f.write(str(message) + "\n")

def play_round(player_money: int, rate_value: int) -> int:
    # 0. Игрок делает ставку
    player_money -= rate_value
    if player_money < 0:  # Если денег на новую ставку недостаточно, то игра заканчивается
        log("У вас закончились деньги. Игра окончена!")
        return player_money
    log(f"Игрок делает ставку: {rate_value}")
    # 1. В начале игры создаем колоду и перемешиваем ее
    deck = Deck(3)
    deck.shuffle()
    # 2. Игроку выдаем две карты
    player_cards = deck.draw(2)
    # 3. Дилер берет одну карту
    dealer_cards = deck.draw(1)
    # 4. Отображаем в консоли карты игрока и дилера
    log(f"{player_cards=}")
    log(f"{dealer_cards=}")
    # 5. Проверяем нет ли у игрока блэкджека (21 очко)
    if sum_points(player_cards) == 21:
        # Выплачиваем выигрышь 3 и 2
        player_money += rate_value * 1.5
        log(f"Black Jack!!! Вы победили, ваш выигрыш {rate_value * 1.5}")
        # Заканчиваем игру
        return player_money
    # Если нет блэкджека, то

    while True:  # Игрок добирает карты пока не скажет "достаточно" или не сделает перебор (>21)
        player_choice = input("еще(1)/достаточно(0): ")
        if player_choice == "1":
            player_cards += deck.draw(1)
            log(f"{player_cards=}")
            # Раздаем еще одну карту
            # Если перебор (>21), заканчиваем добор
            if sum_points(player_cards) > 21:
                log(f"Перебор: {sum_points(player_cards)} очков. Вы проиграли")
                return player_money
        elif player_choice == "0":
            # Заканчиваем добирать карты
            break
        else:  # Обработка некорректного ввода
            log("Введите 1 — еще карту или 0 — достаточно.")

    # Если у игрока не 21(блэкджек) и нет перебора, то
    if sum_points(player_cards) < 21:
        log("Диллер добирает карты")
        while True:  # дилер начинает набирать карты.
            ...  # Смотри подробные правила добора дилера в задании
            if sum_points(dealer_cards) < 17:
                dealer_cards += deck.draw(1)
            else:
                log(f"{dealer_cards=}")
                break
#        log(f"{dealer_cards=}")
    # Выясняем кто набрал больше очков. Выплачиваем/забираем ставку
    if sum_points(player_cards) > sum_points(dealer_cards) or sum_points(dealer_cards)> 21:
        player_money += rate_value * 1.5
        log(f"Вы победили, ваш выигрыш {rate_value * 1.5}")
    elif sum_points(player_cards) < sum_points(dealer_cards):
        log(f"Вы проиграли, ваш проигрыш {rate_value }")
    else:
        log(f"Ничья получите вашу ставку {rate_value}")
    return player_money

def main_menu():
    player_money = 0
    rate_value = 10

    while True:
        log("1. Посмотреть счёт")
        log("2. Пополнить счёт")
        log("3. Сыграть партию")
        log("4. Покинуть стол")

        choice = input("Ваш выбор: ")

        if choice == "1":
            log(f"Ваш счёт: {player_money} руб.")
        elif choice == "2":
            try:
                amount = int(input("Сколько хотите внести? "))
                player_money += amount
                log(f"Баланс пополнен. Текущий счёт: {player_money} руб.")
            except ValueError:
                log("Введите корректное число.")
        elif choice == "3":
            player_money = play_round(player_money, rate_value)
        elif choice == "4":
            log("До свидания!")
            break
        else:
            log("Некорректный выбор.")

if __name__ == "__main__":
    main_menu()

#Vladimir Ghilas
