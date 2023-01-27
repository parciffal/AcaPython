class AmountMinusException(Exception):

    def __init__(self, value: object) -> None:
        super().__init__(value)
        self.__value = value
    
    def __str__(self) -> str:
        return super().__str__()+ "Amount should be not negative number: {}".format(self.__value)

class WrongCurrencyException(Exception):
    
    def __init__(self, value: object) -> None:
        super().__init__(value)
        self.__value = value

    def __str__(self) -> str:
        return super().__str__() + "Amount should be [ AMD RUB USD EUR ] not: {}".format(self.__value) 
