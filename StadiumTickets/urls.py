from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from App1 import views


urlpatterns = [
    path('', views.index),
    path('admin/', admin.site.urls),
    path('App1/', include('App1.urls')),
    path('ProfilesApp/', include('ProfilesApp.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
