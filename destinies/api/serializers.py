from accounts.api.serializers import UserDetailSerializer
from destinies.models import Destiny
from accounts.models import User
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

class DestinyListSerializer(ModelSerializer):
    #user = UserDetailSerializer(read_only=True) pra list e esse
    user = serializers.PrimaryKeyRelatedField(many=False, queryset=User.objects.all())
    class Meta:
        model = Destiny
        fields = [
            'user',
            'name',
            'address',
            'details'
        ]
        
    