from django.conf.urls import url
from django.contrib import admin

from .views import (
    #DestinyCreateAPIView,
    #DestinyDeleteAPIView,
    #EventDetailAPIView,
    EventListCreateAPIView,
    EventRetrieveUpdateDeleteAPIView,
    )

urlpatterns = [
    url(r'^$', EventListCreateAPIView.as_view(), name='list'),
    url(r'^(?P<id>[-\w]+)/$', EventRetrieveUpdateDeleteAPIView.as_view(), name='details'),
    #url(r'^create/$', EventCreateAPIView.as_view(), name='create'),
    #url(r'^(?P<title>[-\w]+)/edit/$', EventUpdateAPIView.as_view(), name='update'),
    #url(r'^(?P<title>[-\w]+)/delete/$', EventDeleteAPIView.as_view(), name='delete'),
]
