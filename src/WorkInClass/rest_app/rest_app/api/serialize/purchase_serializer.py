from rest_framework import serializers

from ..models import Purchase

from .item_serializer import ItemSerializer
from .customer_serializer import CustomerSerializer


class PurchaseSerializer(serializers.ModelSerializer):
    items = ItemSerializer(many=True)
    customer = CustomerSerializer(many=False)

    class Meta:
        model = Purchase
        fields = ['id', 'custumer', 'items', 'total_price', 'buy_time']

    