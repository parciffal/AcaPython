from rest_framework import serializers

from ..models import Customer

from .user_serializer import UserSerializer


class CustomerSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False)
    
    class Meta:
        model = Customer
        
        fields = ['id',
                  'user',
                  'avatar',
                  'registrated_at']
