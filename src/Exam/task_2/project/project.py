from typing import List

from Exam.task_2.product.product import Product


class Inventory:
    def __init__(self, products: List[Product] = ...):
        self.__products = products

    def __repr__(self):
        return "{}".format(self.products)

    @property
    def products(self):
        return self.__products

    @products.setter
    def products(self, products: List[Product]):
        self.__products = products

    def get_by_id(self, id: int):
        for i in self.products:
            if i.id == id:
                return i

    def sum_of_products(self):
        return len(self.products)
