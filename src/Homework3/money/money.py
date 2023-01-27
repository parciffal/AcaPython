from moneyException import  WrongCurrencyException
from enum import Enum

class Currency(Enum):
    AMD = 1
    RUB = 5.8
    USD = 400
    EUR = 430


class Money:
    """
    Class Money
    Some Logic:
    If we have 2 objects with different currency we need to have some conversation
    method. Try to come up with some exchange logic. Here is some note for you.
    Use class variable.
    exchange = {&#39;AMD&#39;: 1, &#39;RUB&#39;: 5.8, &#39;USD&#39;: 400, &#39;EUR&#39;: 430}
    Data members:
    1. amount: integer
    2. currency: string
    Data methods:
    1. __init__
    2. __repr__
    3. get_amount (name=amount)
    4. set_amount (name=amount)
    5. get_currency (name=currency)
    6. set_currency (name=currency)
    7. conversation
    8. __add__
    9. __sub__
    10. __truediv__
    11. __eq__
    12. __ne__
    13. __lt__
    14. __gt__
    15. __le__
    16. __ge__
    """

    __exchange = {"AMD": 1, "RUB": 5.8, "USD": 400, "EUR": 430}

    
    def __init__(self, amount: int, currency: str):
        self.__amount = amount
        self.__currency = self.check_currency(currency)
    
    def __repr__(self) -> str:
        return "{}: {}".format(self.amount, self.currency)

    def __add__(self, other):
        if self.currency == other.currency:
            return self.__class__(self.amount + other.amount, self.currency)
        amount = (self.convert("AMD") + other.convert("AMD"))/self.exchange[self.currency]
        return self.__class__(int(amount), self.currency)

    def __sub__(self, other):
        if self.currency == other.currency:
            return self.__class__(self.amount - other.amount, self.currency)
        amount = (self.convert("AMD") - other.convert("AMD"))/self.exchange[self.currency]
        return self.__class__(int(amount), self.currency)
    
    def __eq__(self, other: 'Money') -> bool:
        return self.convert("AMD") == other.convert("AMD")

    def __ne__(self, other: 'Money') -> bool:
        return not self == other

    def __lt__(self, other: 'Money') -> bool: 
        return self.convert("AMD") < other.convert("AMD")

    def __le__(self, other: 'Money') -> bool:
        return self.convert("AMD") <= other.convert("AMD")

    def __gt__(self, other: 'Money') -> bool:
        return self.convert("AMD") > other.convert("AMD")

    def __ge__(self, other: 'Money') -> bool:
        return self.convert("AMD") >= other.convert("AMD")

    def __truediv__(self, other):
        if isinstance(other, Money):
            if other.amount == 0:
                raise ZeroDivisionError
            return self.amount / other.amount
        else:
            if other == 0:
                raise ZeroDivisionError
            amount = self.amount / other
            return self.__class__(int(amount), self.currency)

    def check_currency(self, c: str):
        if c.upper() in self.exchange.keys():
            return c
        else:
            raise WrongCurrencyException(c)

    @property
    def amount(self):
        return self.__amount

    @amount.setter
    def amount(self, value: int):
        self.__amount = value

    @property
    def exchange(self):
        return self.__exchange

    @property
    def currency(self):
        return self.__currency

    @currency.setter
    def currency(self, value):
        self.__currency = self.check_currency(value)
    
    def convert(self, curr: str = "AMD"):
        if curr.upper() == "AMD":
            return self.amount
        else:
            return self.amount * self.exchange[curr.upper()]



