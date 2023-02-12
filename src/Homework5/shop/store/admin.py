from django.contrib import admin

from .models import *


#admin.site.register(ItemCategory)
#admin.site.register(Customer)
#admin.site.register(MyBug)

#admin.site.register(StoreOwner)
#admin.site.register(StoreCategory)
#admin.site.register(Store)

#admin.site.register(Purchase)
@admin.register(StoreCategory)
class StoreCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'picture']

@admin.register(StoreOwner)
class StoreOwnerAdmin(admin.ModelAdmin):
    list_display = ['name', 'avatar', 'registrated_at']

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
    list_display = ['name', 'avatar', 'registrated_at']


@admin.register(MyBug)
class MyBugAdmin(admin.ModelAdmin):
    list_display = ['custumer', 'total_price']


@admin.register(Purchase)
class PurchaseAdmin(admin.ModelAdmin):
    list_display = ['total_price', 'buy_time', 'custumer', 'get_items']

    def get_items(self):
        return [item for item in self.items.all()]