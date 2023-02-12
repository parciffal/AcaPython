from django.contrib import admin

from .models import *



@admin.register(StoreCategory)
class StoreCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'picture']

@admin.register(StoreOwner)
class StoreOwnerAdmin(admin.ModelAdmin):
    list_display = ['user', 'avatar', 'registrated_at']

@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    list_display = ['name', 'owner', 'store_category']


@admin.register(ItemCategory)
class ItemCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'picture']
    
#admin.site.register(Item)

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ['name','picture', 'category', 'price', 
                    'quantity', 'info', 'store']


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['user', 'avatar', 'registrated_at']


@admin.register(MyBug)
class MyBugAdmin(admin.ModelAdmin):
    list_display = ['custumer', 'total_price', 'items']
    list_display_links = ['items']

    def items(self):
        return self.items.name

@admin.register(Purchase)
class PurchaseAdmin(admin.ModelAdmin):
    list_display = ['total_price', 'buy_time', 'custumer', 'items']
    list_display_links = ['items']

    def items(self):
        return self.items.name