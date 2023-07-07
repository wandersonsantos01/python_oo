

class Account:

    def __init__(self, number, person, value, limit):
        self.__number = number
        self.__person = person
        self.__value = value
        self.__limit = limit

    def extract(self):
        print("{} on the account {}".format(self.__value, self.__number))

    def deposit(self, value):
        self.__value += value

    def withdraw(self, value):
        if self.__can_withdraw(value):
            self.__value -= value
        else:
            print("Value {} is over limit of {}".format(value, self.__limit))

    def __can_withdraw(self, value):
        return value <= (self.__value + self.__limit)

    def transfer(self, value, to_account):
        self.__can_withdraw(value)
        to_account.deposit(value)

    def is_negative(self):
        return self.__value < 0

    def get_value(self):
        return self.__value

    def set_value(self, value):
        self.__value = value

    def get_number(self):
        return self.__number

    def set_number(self, number):
        self.__number = number

    def get_person(self):
        return self.__person

    def set_person(self, person):
        self.__person = person

    @property
    def limit(self):
        return self.__limit

    @limit.setter
    def limit(self, limit):
        self.__limit = limit

    @staticmethod
    def bank_codes():
        return {"BB": "001", "Bradesco": "237", "Caixa": "104"}