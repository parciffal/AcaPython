from ..serialize import PurchaseSerializer
from ..models import Purchase

from rest_framework import viewsets
from rest_framework.permissions import AllowAny


class PurchaseView(viewsets.ModelViewSet):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer
    permission_classes = [AllowAny]