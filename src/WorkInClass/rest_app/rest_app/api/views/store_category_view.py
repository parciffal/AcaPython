from ..serialize import StoreCategorySerializer
from ..models import StoreCategory

from rest_framework import viewsets
from rest_framework.permissions import AllowAny


class StoreCategoryView(viewsets.ModelViewSet):
    queryset = StoreCategory.objects.all()
    serializer_class = StoreCategorySerializer
    permission_classes = [AllowAny]