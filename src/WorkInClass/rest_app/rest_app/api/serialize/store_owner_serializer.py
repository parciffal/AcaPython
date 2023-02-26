from rest_framework import serializers

from ..models import StoreOwner

from .user_serializer import UserSerializer


class StoreOwnerSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False)

    class Meta:
        model = StoreOwner
        fields = ['id',
                  'user',
                  'avatar',
                  'registrated_at']