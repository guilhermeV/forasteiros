from django.conf.urls import url
from django.contrib import admin

from .views import (
    #DestinyCreateAPIView,
    #DestinyDeleteAPIView,
    #EventDetailAPIView,
    DestinyListCreateAPIView,
    DestinyRetrieveUpdateDeleteAPIView,
    )

urlpatterns = [
    url(r'^$', DestinyListCreateAPIView.as_view(), name='list'),
    url(r'^(?P<name>[-\w]+)/$', DestinyRetrieveUpdateDeleteAPIView.as_view(), name='details'),
    #url(r'^(?P<title>[-\w]+)/edit/$', EventUpdateAPIView.as_view(), name='update'),
    #url(r'^(?P<title>[-\w]+)/delete/$', EventDeleteAPIView.as_view(), name='delete'),
]
