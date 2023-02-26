from rest_framework import serializers

from ..models import Store

from .store_owner_serializer import StoreOwnerSerializer
from .store_category_serializer import StoreCategorySerializer

class StoreSerializer(serializers.ModelSerializer):
    owner = StoreOwnerSerializer(many=False)
    store_category = StoreCategorySerializer(many=False)

    class Meta:
        model = Store
        fields = ['id',
                  'name',
                  'owner',
                  'store_category']