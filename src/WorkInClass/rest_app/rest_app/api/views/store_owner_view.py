from ..serialize import StoreOwnerSerializer
from ..models import StoreOwner

from rest_framework import viewsets
from rest_framework.permissions import AllowAny


class StoreOwnerView(viewsets.ModelViewSet):
    queryset = StoreOwner.objects.all()
    serializer_class = StoreOwnerSerializer
    permission_classes = [AllowAny]