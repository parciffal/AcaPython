
from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import *

router = DefaultRouter()
router.register(r'customer', CustomerView, basename='customer')
router.register(r'item_category', ItemCategoryView, basename='item_category')
router.register(r'item', ItemView, basename='item')
router.register(r'store_owner', StoreOwnerView, basename='store_owner')
router.register(r'store_category', StoreCategoryView, basename='store_category')
router.register(r'store', StoreView, basename='store')
router.register(r'mybug', MyBugView, basename='mybug')
router.register(r'purchase', PurchaseView, basename='purchase')

urlpatterns = [
    path('', include(router.urls))
]