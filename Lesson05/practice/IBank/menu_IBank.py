from IBank_part5 import  CreditAccount

EMPLOYEE_PASSWORD = "123"
from typing import List

class BankSystem:
    def __init__(self):
        self.account: List[CreditAccount] = []

def close_account(self):
    name = input("Введите имя клиента, чей счет хотите закрыть: ")
    account = self.name
    if account.balance == 0:
        self.accounts.remove(account)
        print("Счёт успешно закрыт.")
    else:
        print("Операция отменена.")

def view_accounts_list(accounts: List[CreditAccount]):
    for acc in accounts:
        print(f"{acc.name} баланс: {acc.balance} руб. паспорт: {acc.passport} т.{acc.phone_number}")

def view_account_by_passport(accounts: List[CreditAccount]):
    passport_to_find = input("Введите номер паспорта: ").strip()
    found = False
    for acc in accounts:
        if acc.passport == passport_to_find:
            print(f"{acc.name} баланс: {acc.balance} руб. паспорт: {acc.passport} т.{acc.phone_number}")
            found = True
            break

    if not found:
        print("Клиент с таким паспортом не найден.")


def view_client_account():
    passport = input("Введите номер паспорта: ").strip()

    found = False
    for acc in accounts:
        if acc.passport == passport:
            print(f"{acc.name} баланс: {acc.balance} руб.")
            found = True

    if not found:
        print("Клиент с таким паспортом не найден.")

def put_account():
    def deposit_to_account(accounts: list[CreditAccount]):
        passport = input("Введите номер паспорта: ").strip()
        account = next((acc for acc in accounts if acc.passport == passport), None)
        if account is None:
            print("Клиент с таким паспортом не найден.")
            return

        amount = int(input("Введите сумму для пополнения: "))
        account.deposit(amount)
        print(f"Счет пополнен на {amount} руб. Новый баланс: {account.balance} руб.")

def withdraw():
    passport = input("Введите номер паспорта: ")
    try:
        amount = int(input("Введите сумму для снятия: "))
    except ValueError:
        print("Ошибка: введите корректное число.")
        return

    account = next((acc for acc in accounts if acc.passport == passport), None)
    if not account:
        print("Счет с таким паспортом не найден.")
        return

    try:
        account.withdraw(amount)
        print(f"Снято {amount} руб. с вашего счета.")
    except ValueError as e:
        print(f"Ошибка: {e}")


def transfer():
    phone = input("Введите номер телефона получателя: ")
    amount_str = input("Введите сумму перевода: ")

    try:
        amount = int(amount_str)
        if amount <= 0:
            print("Сумма должна быть положительной.")
            return
    except ValueError:
        print("Некорректная сумма.")
        return

    target_account = next((acc for acc in accounts if acc.phone_number == phone), None)
    if target_account is None:
        print("Клиент с таким номером телефона не найден.")
        return

    passport = input("Введите ваш паспорт: ")
    source_account = next((acc for acc in accounts if acc.passport == passport), None)
    if source_account is None:
        print("Ваш счет не найден.")
        return

    try:
        source_account.transfer(target_account, amount)
        print(f"Перевод на {amount} руб. выполнен успешно.")
    except ValueError as e:
        print(f"Ошибка: {e}")
    pass


def create_new_account(self, name: str, passport: str, phone_number: str, start_balance: int = 0, negative_limit: int = 0):
    print("Укажите данные клиента")
    name = input("Имя:")
    passport = input("Номер паспорта: ")
    phone_number = input("Номер телефона: ")
    start_balance = int(input("Начальный баланс: "))
    negative_limit = int(input("Лимит кредита"))
    account = CreditAccount(name, passport, phone_number, start_balance)
    self.accounts.append(account)
    print("Обычный счет создан.")

def client_menu(account):
    while True:
        print("***********Меню клиента <Иванов И.И.>*************")
        print("1. Состояние счета")
        print("2. Пополнить счет")
        print("3. Снять со счета")
        print("4. Перевести деньги другому клиенту банка")
        print("5. Exit")
        choice = input(":")
        if choice == "1":
            view_client_account()
        elif choice == "2":
            put_account()
        elif choice == "3":
            withdraw()
        elif choice == "4":
            transfer()
        elif choice == "5":
            return
    # input("Press Enter")


def employee_menu():
    while True:
        print("***********Меню сотрудника*************")
        print("1. Создать новый счет")
        print("2. Закрыть счет")
        print("3. Посмотреть список счетов")
        print("4. Посмотреть счет по номеру паспорта")
        print("5. Exit")
        choice = input(":")
        if choice == "1":
            create_new_account()
        elif choice == "2":
            close_account()
        elif choice == "3":
            view_accounts_list()
        elif choice == "4":
            view_account_by_passport()
        elif choice == "5":
            return


def employee_access():
    """
    Проверяет доступ сотрудника банка, запрашивая пароль
    """
    password = input("Пароль: ")
    if password == EMPLOYEE_PASSWORD:
        return True
    return False


def client_access(accounts):
    """
    Находит аккаунт с введеным номером паспорта
    Или возвращает False, если аккаунт не найден
    """
    try:
        passport = int(input("Номер паспорта: "))
    except ValueError:
        return False
    for account in accounts:
        if passport == account.passport8:
            return account

    return False


def start_menu():
    while True:
        print("Укажите вашу роль:")
        print("1. Сотрудник банка")
        print("2. Клиент")
        print("3. Завершить работу")

        choice = input(":")
        if choice == "3":
            break
        elif choice == "1":
            if employee_access():
                employee_menu()
            else:
                print("Указан неверный пароль, укажите роль и повторите попытку...")
        elif choice == "2":
            account = client_access(accounts)
            if account:
                client_menu(account)
            else:
                print("Указан несуществующий пасспорт, укажите роль и повторите попытку...")
        else:
            print("Указан некорректный пункт меню, повторите выбор...")


if __name__ == "__main__":
    accounts = []
    start_menu()
