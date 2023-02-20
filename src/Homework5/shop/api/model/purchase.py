from datetime import datetime
from django.db import models
import json

from .customer import Customer
from .item import Item
from datetime import datetime

class Purchase(models.Model):
    items = models.ManyToManyField(Item)
    buy_time = models.DateTimeField(default=datetime.now())
    custumer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    total_price = models.BigIntegerField(default=0) 
    
    class Meta:
        verbose_name_plural = "Purchase"

    def __str__(self) -> str:
        return self.custumer.user.get_full_name()

    def as_json(self):
        data = {
            "id": self.id,
            "items": str([i.as_json() for i in self.items]),
            "buy_time": str(self.buy_time),
            "custumer": self.custumer.as_json(),
            "total_price": self.total_price.as_json()
        }
        return data
    