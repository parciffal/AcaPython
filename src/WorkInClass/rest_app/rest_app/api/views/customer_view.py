from ..serialize import CustomerSerializer
from ..models import Customer

from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from rest_framework.decorators import action

from django.http import HttpResponse

import json

class CustomerView(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [AllowAny]
