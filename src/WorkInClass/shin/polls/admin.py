from django.contrib import admin
from .models import *

admin.site.register(ItemCategory)
"""
@admin.register(ItemCategory)
class ItemCategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
   """ 
admin.site.register(Item)

"""@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'price', 
                    'quantity', 'info', 'store']"""

admin.site.register(Customer)
admin.site.register(MyBug)

admin.site.register(StoreOwner)
admin.site.register(StoreCategory)
admin.site.register(Store)

admin.site.register(Purchase)