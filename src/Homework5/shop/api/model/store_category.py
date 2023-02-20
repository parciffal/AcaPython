from django.db import models

import json


class StoreCategory(models.Model):
    name = models.CharField(max_length=250)
    picture = models.ImageField(upload_to='media/storeCategory', blank=True, null=True)

    def __str__(self) -> str:
        return self.name

    def as_json(self):
        return {
            "id": self.id,
            "name": self.name
            }
    


