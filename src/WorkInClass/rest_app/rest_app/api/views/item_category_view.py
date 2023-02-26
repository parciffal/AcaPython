from ..serialize import ItemCategorySerializer
from ..models import ItemCategory

from rest_framework import viewsets
from rest_framework.permissions import AllowAny


class ItemCategoryView(viewsets.ModelViewSet):
    queryset = ItemCategory.objects.all()
    serializer_class = ItemCategorySerializer
    permission_classes = [AllowAny]