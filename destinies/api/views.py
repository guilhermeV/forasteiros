from django.db.models import Q
from .serializers import DestinyListSerializer
from django.http import HttpResponse
from accounts.models import User
from rest_framework.generics import (ListCreateAPIView, RetrieveUpdateDestroyAPIView)
    
from rest_framework.filters import (SearchFilter,OrderingFilter)
    
from rest_framework.permissions import (AllowAny,
    IsAuthenticated,
    #IsAdminUser,
    #IsAuthenticatedOrReadOnly,
    )
    
from destinies.models import Destiny
from django.conf import settings

class DestinyListCreateAPIView(ListCreateAPIView):
    queryset = Destiny.objects.all()
    serializer_class = DestinyListSerializer
    filter_backends= [SearchFilter, OrderingFilter]
    permission_classes = [AllowAny]
    search_fields = ['name']
    
    def perform_create(self, serializer):
        serializer.save()
        
class DestinyRetrieveUpdateDeleteAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Destiny.objects.all()
    serializer_class = DestinyListSerializer
    permission_classes = [AllowAny]
    lookup_field = 'name'
    
    def perform_update(self, serializer):
        serializer.save(user=User.objects.first())
    
    







