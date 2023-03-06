from django.db import models
import json
from .customer import Customer
from .item import Item

class MyBug(models.Model):
    custumer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    items = models.ManyToManyField(Item)
    total_price = models.BigIntegerField(default=0)

    def __str__(self) -> str:
        return self.custumer.user.get_username()

    def as_json(self):

        data = {
            "id": self.id,
            "custumer": self.custumer.as_json()['name'],
            "items": str([i.as_json() for i in self.items.all()]),
            "total_price": self.total_price
        }
        return data
    