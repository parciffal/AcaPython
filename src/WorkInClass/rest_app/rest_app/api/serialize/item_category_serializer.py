from rest_framework import serializers

from ..models import ItemCategory


class ItemCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = ItemCategory
        fields = ['id', 'name']

    