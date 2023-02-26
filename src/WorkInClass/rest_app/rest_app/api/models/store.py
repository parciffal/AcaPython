from django.db import models

from .store_owner import StoreOwner
from .store_category import StoreCategory

import json


class Store(models.Model):
    name = models.CharField(max_length=250)
    owner = models.ForeignKey(StoreOwner, on_delete=models.CASCADE)
    store_category = models.ForeignKey(StoreCategory, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name

    def as_json(self):

        data = {
            "id": self.id,
            "name": self.name,
            "owner": self.owner.as_json(),
            "store_category": self.store_category.as_json()}
        return data
    