from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from rest_framework_jwt.views import obtain_jwt_token
from accounts.views import (login_view, register_view, logout_view)

app_name='project'

urlpatterns = [
    url(r'^events/', include(('events.urls', 'events'), namespace='events')),
    url(r'^posts/', include(('posts.urls', 'posts'), namespace='posts')),
    url(r'^comments/', include(('comments.urls', 'comments'), namespace='comments')),
    url(r'^api/comments/', include(('comments.api.urls', 'comments-api'), namespace='comments-api')),
    url(r'^api/posts/', include(('posts.api.urls', 'posts'), namespace='posts-api')),

    url(r'^admin/', admin.site.urls),
    url(r'^api/auth/token/', obtain_jwt_token),
    url(r'^register/', register_view, name='register'),
    url(r'^login/', login_view, name='login'),
    url(r'^logout/', logout_view, name='logout'),

    url(r'^destinies/', include(('destinies.urls', 'destinies'), namespace='destinies')),
    url(r'^api/users/', include(('accounts.api.urls', 'users-api'), namespace='users-api')),
    url(r'^api/events/', include(('events.api.urls', 'events-api'), namespace='events-api')),
    url(r'^api/destinies/', include(('destinies.api.urls', 'destinies-api'), namespace='destinies-api')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
