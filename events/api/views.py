from django.db.models import Q
from .serializers import (EventListSerializer, EventCreateUpdateSerializer, EventDetailSerializer, EventCreateUpdateSerializer)
    
from rest_framework.generics import (ListAPIView, CreateAPIView, RetrieveAPIView, RetrieveUpdateAPIView, DestroyAPIView)
    
from rest_framework.filters import (SearchFilter,OrderingFilter,)
    
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    #IsAdminUser,
    #IsAuthenticatedOrReadOnly,
    )
    
from events.models import Event
from accounts.models import User
from django.conf import settings

class EventListAPIView(ListAPIView):
    serializer_class = EventListSerializer
    filter_backends= [SearchFilter, OrderingFilter]
    permission_classes = [AllowAny]
    search_fields = ['title', 'initial_date', 'final_date', 'status']
    
    def get_queryset(self, *args, **kwargs):
        #queryset_list = super(PostListAPIView, self).get_queryset(*args, **kwargs)
        queryset_list = Event.objects.all() #filter(user=self.request.user)
        query = self.request.GET.get("q")
        if query:
            queryset_list = queryset_list.filter(
                    Q(title__icontains=query)|
                    Q(initial_date__icontains=query)|
                    Q(final_date__icontains=query) |
                    Q(status__icontains=query)
                    ).distinct()
        return queryset_list

class EventCreateAPIView(CreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventCreateUpdateSerializer
    permission_classes = [AllowAny]
    
    def perform_create(self, serializer):
        serializer.save()

class EventDetailAPIView(RetrieveAPIView, DestroyAPIView, RetrieveUpdateAPIView):
    serializer_class = EventDetailSerializer
    permission_classes = [AllowAny]
    lookup_field = 'title'
    queryset = Event.objects.all()
    
class EventUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventCreateUpdateSerializer
    lookup_field = 'title'
    permission_classes = [AllowAny]
    
    def perform_update(self, serializer):
        #serializer.save(user=self.request.user)
        serializer.save(user=User.objects.first())
        
class EventDeleteAPIView(DestroyAPIView):
    queryset = Event.objects.all()
    serializer_class = EventDetailSerializer
    lookup_field = 'title'
    permission_classes = [AllowAny]
    
def search_event():
    print 'wtf'
    e = events = Event.objects.filter(title='titl')
    print e
    return e
    #e = events = Event.objects.filter(title='teste')










