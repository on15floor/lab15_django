from django.contrib import admin
from django.urls import path, include

from django.views.static import serve as mediaserv
from django.conf.urls import url
from config import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('', include('blog.urls')),
    path('', include('money.urls')),
    path('', include('birthdays.urls')),
    path('', include('api.urls'))
]

if not settings.DEBUG:
    urlpatterns += [
        url(f'^{settings.STATIC_URL.lstrip("/")}(?P<path>.*)$', mediaserv, {'document_root': settings.STATIC_ROOT}),
    ]
