from ..serialize import ItemSerializer
from ..models import Item

from rest_framework import viewsets
from rest_framework.permissions import AllowAny


class ItemView(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = [AllowAny]
