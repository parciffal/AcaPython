from ..serialize import MyBugSerializer
from ..models import MyBug

from rest_framework import viewsets
from rest_framework.permissions import AllowAny


class MyBugView(viewsets.ModelViewSet):
    queryset = MyBug.objects.all()
    serializer_class = MyBugSerializer
    permission_classes = [AllowAny]