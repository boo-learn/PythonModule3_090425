 Сюда отправляем готовое решение IBank часть-5
class Operation:
    # Типы операций храним в свойствах класса
    DEPOSIT = 'Пополнение'
    WITHDRAW = 'Снятие'
    TRANSFER_OUT = 'Перевод'
    TRANSFER_IN = 'Поступление'

    # Напоминаю: обращение к этим переменным происходит через имя класса, пример: Operation.WITHDRAW

    def __init__(self, type, amount, target_account=None, commission=0):
        self.type = type
        self.amount = amount
        self.target_account = target_account
        self.commission = commission

    def __repr__(self) -> str:
        """
        :return: возвращает строковое представление операции. Формат указан в 02_IBank_part2.md
        """
        str_out = f"{self.type} {self.amount} руб. (комиссия: {int(self.amount * self.commission / 100)} руб.)"
        if self.type == Operation.TRANSFER_OUT:
            str_out += f" на счет клиента: {self.target_account.name}"
        if self.type == Operation.TRANSFER_IN:
            str_out += f" со счета клиента: {self.target_account.name}"
        return str_out


class Account:
    COMMISSION_PERCENT = 2
    def __init__(self, name: str, passport: str, phone_number: str, start_balance: int = 0):
        self.name = name
        self.passport = passport
        self.phone_number = phone_number
        self.__balance = start_balance
        # историю храним как список объектов класса Operation, добавив свойство в конструктор:
        self.__history: list[Operation] = []

    @property
    def balance(self) -> int:
        return self.__balance

    # Данный метод дан в готовом виде. Изучите его и используйте как пример, для доработки других
    def deposit(self, amount: int, to_history: bool = True) -> None:
        """
        Внесение суммы на текущий счет
        :param amount: сумма
        :param to_history: True - записывать операцию в историю, False - не записывать
        """
        self.__balance += amount
        if to_history:
            operation = Operation(amount=amount, type=Operation.DEPOSIT)
            self.__history.append(operation)

    def _enough_money(self, amount) -> bool:
        return amount < self.__balance

    def _calculate_amount_with_commission(self, amount: int) -> int:
        return int(amount * (1 + self.COMMISSION_PERCENT / 100))

    def withdraw(self, amount: int, to_history: bool = True) -> None:
        """
        Снятие суммы с текущего счета
        :param amount: сумма
        """
        amount_with_commission = self._calculate_amount_with_commission(amount)
        if not self._enough_money(amount_with_commission):
            raise ValueError("Недостаточно средств")

        self.__balance -= amount_with_commission
        if to_history:
            operation = Operation(amount=amount, type=Operation.WITHDRAW, commission=self.COMMISSION_PERCENT)
            self.__history.append(operation)

    def transfer(self, target_account: 'Account', amount: int, to_history: bool = True) -> None:
        """
        Перевод денег на счет другого клиента
        :param target_account: счет клиента для перевода
        :param amount: сумма перевода
        :return:
        """
        self.withdraw(amount, to_history=False)
        target_account.deposit(amount, to_history=False)

        if to_history:
            # Деньги ушли ->
            operation_out = Operation(
                amount=amount,
                type=Operation.TRANSFER_OUT,
                target_account=target_account,
                commission=self.COMMISSION_PERCENT
            )
            # Деньги поступили <-
            operation_in = Operation(amount=amount, type=Operation.TRANSFER_IN, target_account=self)
            self.__history.append(operation_out)
            target_account.__history.append(operation_in)


    def get_history(self) -> list[Operation]:
        """
        :return: возвращаем историю операций в виде списка операций
        """
        return self.__history

    def __str__(self):
        return f"{self.name} баланс: {self.balance} руб. паспорт: {self.passport} тел.{self.phone_number}"


class CreditAccount(Account):
    COMMISSION_PERCENT = 5

    def __init__(self, name, passport, phone_number, start_balance=0, negative_limit=0):
        super().__init__(name, passport, phone_number, start_balance)
        self.negative_limit = negative_limit

    def _enough_money(self, amount) -> bool:

        return amount <= self.balance + self.negative_limit

    def _calculate_amount_with_commission(self, amount: int) -> int:
        if self.balance >= 0:
            commission = 2
        else:
            commission = 5
        return round(amount * (1 + commission / 100))

    def __str__(self):
        return f"<К> {self.name} баланс: {self.balance} руб. паспорт: {self.passport} т.{self.phone_number}"


if __name__ == "__main__":
    pass
