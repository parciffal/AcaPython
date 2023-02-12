from django.db import models
from django.contrib.auth.models import User
import datetime

# Store

class StoreCategory(models.Model):
    name = models.CharField(max_length=250)
    picture = models.ImageField(upload_to='media/storeCategory')

    class Meta:
        verbose_name_plural = 'storeCategory'
    
    def __str__(self) -> str:
        return self.name

class ItemCategory(models.Model):
    name = models.CharField(max_length=250)
    picture = models.ImageField(upload_to='media/itemCategory')
    
    class Meta:
        verbose_name_plural = 'itemCategory'
    
    def __str__(self) -> str:
        return self.name

class StoreOwner(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='media/users')
    registrated_at = models.DateTimeField(datetime.datetime.now())

    class Meta:
        verbose_name_plural = 'storeOwner'
    
    def __str__(self) -> str:
        return self.name

class Store(models.Model):
    name = models.CharField(max_length=250)
    owner = models.ForeignKey(StoreOwner, on_delete=models.CASCADE)
    store_category = models.ForeignKey(StoreCategory, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'store'
    
    def __str__(self) -> str:
        return self.name

class Item(models.Model):
    name = models.CharField(max_length=250)
    picture = models.ImageField(upload_to='media/items')
    category = models.ForeignKey(ItemCategory, on_delete=models.CASCADE)
    price = models.BigIntegerField(default=0)
    quantity = models.IntegerField(default=0)
    info = models.TextField(default="")
    store = models.ForeignKey(Store, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'item'
    
    def __str__(self) -> str:
        return self.name

#Customer

class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='media/users')
    registrated_at = models.DateTimeField(datetime.datetime.now())

    class Meta:
        verbose_name_plural = 'customer'
    
    def __str__(self) -> str:
        return self.user.get_full_name()


class MyBug(models.Model):
    custumer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    items = models.ManyToManyField(Item)
    total_price = models.BigIntegerField(default=0)

    class Meta:
        verbose_name_plural = 'myBag'
    
    def __str__(self) -> str:
        return self.custumer.user.get_full_name()

class Purchase(models.Model):
    items = models.ManyToManyField(Item)
    buy_time = models.DateTimeField()
    custumer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    total_price = models.BigIntegerField(default=0) 

    class Meta:
        verbose_name_plural = 'storeOwner'
    
    def __str__(self) -> str:
        return self.custumer.user.get_full_name()


