from django.conf.urls import url
from django.contrib import admin

from .views import (
	#event_list,
	destiny_create,
	#event_detail,
	#event_update,
	#event_delete,
	)

urlpatterns = [
	#url(r'^$', event_list, name='list'),
	
    url(r'^create/$', destiny_create, name='create'),
    #url(r'^(?P<slug>[\w-]+)/$', event_detail, name='detail'),
    #url(r'^(?P<slug>[\w-]+)/edit/$', event_update, name='update'),
    #url(r'^(?P<slug>[\w-]+)/delete/$', event_delete),
    #url(r'^events/$', "<appname>.views.<function_name>"),
]
