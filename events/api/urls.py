from django.conf.urls import url
from django.contrib import admin

from .views import (
    EventCreateAPIView,
    EventDeleteAPIView,
    EventDetailAPIView,
    EventListAPIView,
    EventUpdateAPIView,
    search_event,
    )

urlpatterns = [
    url(r'^$', EventListAPIView.as_view(), name='list'),
    url(r'^create/$', EventCreateAPIView.as_view(), name='create'),
    url(r'^(?P<title>[-\w]+)/$', EventDetailAPIView.as_view(), name='details'),
    #url(r'^(?P<title>[-\w]+)/edit/$', EventUpdateAPIView.as_view(), name='update'),
    #url(r'^(?P<title>[-\w]+)/delete/$', EventDeleteAPIView.as_view(), name='delete'),
]
