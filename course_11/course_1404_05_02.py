# from abc import ABC, abstractmethod


# class Car(ABC):
#     @abstractmethod
#     def change_tire(self):
#         pass

#     @abstractmethod
#     def start(self):
#         pass


# class Benz(Car):
#     def change_tire(self):
#         print("Change tire")

#     def start(self):
#         print("Start")


# # c1 = Car()
# b1 = Benz()
# b1.change_tire()
# b1.start()

from abc import ABC, abstractmethod


class Bank:
    def __init__(self, name, branch, address, credit):

        self.name = name
        self.branch = branch
        self.address = address
        self.credit = credit
        self.accounts = []

    def add_account(self, account):
        self.accounts.append(account)

    def credit_update(self):
        all_balance = [i.balance for i in self.accounts]
        print(all_balance)
        self.credit = sum(all_balance)
        return self.credit


class BankAccount(ABC):

    def __init__(self, account_id, account_name, account_type, balance=0):
        self.account_id = account_id
        self.balance = balance
        self.account_name = account_name
        self.__type = account_type

    def show_type(self):
        print(self.__type)

    @abstractmethod
    def deposit(self):
        pass

    @abstractmethod
    def withdraw(self):
        pass

    def show_balance(self):
        print(self.balance)


class ProfitMixin:
    def profit(self, percent=0.05):
        if percent <= 0.3:
            self.balance = self.balance + (percent * self.balance)


# a = ProfitMixin()
# print(a.profit())


class IndividualAccount(BankAccount, ProfitMixin):
    def __init__(self, account_id, account_name, balance=0):
        super().__init__(account_id, account_name, "individual", balance)

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount


class LegalAccount(BankAccount, ProfitMixin):
    def __init__(self, account_id, account_name, balance=0):
        super().__init__(account_id, account_name, "legal", balance)

    def deposit(self, amount):
        if amount > 10000:
            self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount and amount <= 1000:
            self.balance -= amount


new_bank = Bank("khodemuni", "maktab", "tehran", 0)
hassani_account = IndividualAccount(1, "hassani", 2000)
new_bank.add_account(hassani_account)

maktab_account = LegalAccount(2, "maktab")
new_bank.add_account(maktab_account)

maktab_account.deposit(11000)
maktab_account.show_balance()
maktab_account.withdraw(5000)
maktab_account.show_balance()
maktab_account.__type = "hello"
hassani_account.show_type()
maktab_account.show_type()
maktab_account.profit()
maktab_account.show_balance()
print(new_bank.credit_update())