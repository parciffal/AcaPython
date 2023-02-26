from ..serialize import StoreSerializer
from ..models import Store

from rest_framework import viewsets
from rest_framework.permissions import AllowAny


class StoreView(viewsets.ModelViewSet):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer
    permission_classes = [AllowAny]

