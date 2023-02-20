from .views import *
from django.urls import path

urlpatterns = [
    path('item_category/<int:id>/', ItemCategoryView.check_view),
    path('item_category/', ItemCategoryView.as_view()),
    path('item/<int:id>/', ItemView.check_view),
    path('item/', ItemView.as_view()),
    path('customer/<int:id>/', CustomerView.check_view),
    path('customer/', CustomerView.as_view()),
    path('mybug/<int:id>/', MyBugView.check_view),
    path('mybug/', MyBugView.as_view()),
    path('purchase/<int:id>/', PurchaseView.check_view),
    path('purchase/', PurchaseView.as_view()),
    path('store/<int:id>/', StoreView.check_view),
    path('store/', StoreView.as_view()),
    path('store_owner/<int:id>/', StoreOwnerView.check_view),
    path('store_owner/', StoreOwnerView.as_view()),
    path('store_category/<int:id>/', StoreCategoryView.check_view),
    path('store_category/', StoreCategoryView.as_view()),
    
]