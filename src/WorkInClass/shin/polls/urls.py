from django.contrib import admin
from django.urls import path
from .api.category import ItemCategoryView


urlpatterns = [
    path('itemcategory/<int:id>/', ItemCategoryView.check_view),
    path('itemcategory/', ItemCategoryView.as_view())
]
