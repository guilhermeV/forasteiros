from django.db.models import Q
from .serializers import OrderListSerializer
    
from rest_framework.generics import (ListCreateAPIView, RetrieveUpdateDestroyAPIView)
    
from rest_framework.filters import (SearchFilter,OrderingFilter)
    
from rest_framework.permissions import (AllowAny,
    IsAuthenticated,
    #IsAdminUser,
    #IsAuthenticatedOrReadOnly,
    )
    
from orders.models import Order
from django.contrib.auth.models import User
from django.conf import settings

class OrderListCreateAPIView(ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderListSerializer
    filter_backends= [SearchFilter, OrderingFilter]
    permission_classes = [AllowAny]
    search_fields = ['id']
    
    def perform_create(self, serializer):
        serializer.save(user=User.objects.first())
        
class OrderRetrieveUpdateDeleteAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderListSerializer
    permission_classes = [AllowAny]
    lookup_field = 'id'
    
    def perform_update(self, serializer):
        serializer.save(user=User.objects.first())
    







