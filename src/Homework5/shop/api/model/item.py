from django.db import models
import json

from .item_category import ItemCategory
from .store import Store

class Item(models.Model):
    name = models.CharField(max_length=250)
    picture = models.ImageField(upload_to='media/items', blank=True, null=True)
    category = models.ForeignKey(ItemCategory, on_delete=models.CASCADE)
    price = models.BigIntegerField(default=0)
    quantity = models.IntegerField(default=0)
    info = models.TextField(default="")
    store = models.ForeignKey(Store, on_delete=models.CASCADE)


    class Meta:
        verbose_name_plural = "Item"

    def __str__(self) -> str:
        return self.name

    def as_json(self):
        data = {
            "id": self.id,
            "name": self.name,
            "category": self.category.as_json(),
            "price": self.price,
            "quantity": self.category,
            "info": self.info,
            "store": self.store.as_json()
        }
        return data