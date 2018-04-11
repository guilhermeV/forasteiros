from accounts.api.serializers import UserDetailSerializer
from events.models import Event
from destinies.models import Destiny
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

class EventListSerializer(ModelSerializer):
    user = UserDetailSerializer(read_only=True)
    class Meta:
        model = Event
        fields = [
            'user',
            'title',
            'user',
            'initial_date',
            'final_date',
            'details',
            'payment_options',
            'meeting_point',
            'status',
        ]
        
class EventCreateUpdateSerializer(ModelSerializer):
    destiny = serializers.PrimaryKeyRelatedField(many=False, queryset=Destiny.objects.all())
    class Meta:
        model = Event
        fields = [
            'title',
            'destiny',
            'initial_date',
            'final_date',
            'details',
            'payment_options',
            'meeting_point',
            'status',
        ]
        
    def create(self, instance):
        print self.context['request'].user.__dict__
        return Event.objects.create(**instance)
        
        
class EventDetailSerializer(ModelSerializer):
    user = UserDetailSerializer(read_only=True)
    class Meta:
        model = Event
        fields = [
            'id',
            'title',
            'user',
            'initial_date',
            'final_date',
            'details',
            'payment_options',
            'meeting_point',
            'status',
        ]
        
