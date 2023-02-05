class CountOutOfQuantity(Exception):
    def __init__(self, count, quantity):
        super().__init__("Count out of Quantity: {} > {}".format(count, quantity))


class Product:
    def __init__(self, price: int, quantity: int):
        self.__price = price
        self.__id = id(self)
        self.__quantity = quantity

    def __repr__(self):
        return "Price: {}\nId: {}\nQuantity: {}\n".format(self.price, self.id, self.quantity)

    def buy(self, count: int):
        if count <= self.quantity:
            self.quantity -= count
        else:
            raise CountOutOfQuantity(count, self.quantity)

    @property
    def quantity(self):
        return self.__quantity

    @quantity.setter
    def quantity(self, qu: int):
        self.__quantity = qu

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, pr: int):
        self.__id = pr

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, pr: int):
        self.__price = pr