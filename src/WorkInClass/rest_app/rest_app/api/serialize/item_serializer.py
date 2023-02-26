from rest_framework import serializers

from ..models import Item

from .item_category_serializer import ItemCategorySerializer
from .store_serializer import StoreSerializer


class ItemSerializer(serializers.ModelSerializer):
    category = ItemCategorySerializer(many=False)
    store = StoreSerializer(many=False)

    class Meta:
        model = Item
        fields = ['id',
                  'picture',
                  'category',
                  'price',
                  'quantity',
                  'info',
                  'store']