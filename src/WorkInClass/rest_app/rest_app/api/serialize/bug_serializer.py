from rest_framework import serializers

from ..models import MyBug

from .item_serializer import ItemSerializer
from .customer_serializer import CustomerSerializer

class MyBugSerializer(serializers.ModelSerializer):
    items = ItemSerializer(many=True)
    customer = CustomerSerializer(many=False)

    class Meta:
        model = MyBug
        fields = ['id', 'custumer', 'items', 'total_price']

    