from accounts.api.serializers import UserDetailSerializer
from destinies.models import Order
from events.models import Event
from rest_framework.serializers import ModelSerializer
from events.serializers import EventDetailSerializer

class OrderListSerializer(ModelSerializer):
    user = UserDetailSerializer(read_only=True)
    event = EventDetailSerializer
    class Meta:
        model = Order
        fields = [
            'user',
            'event',
            'payment_form',
            'status',
            'details',
        ]
        
