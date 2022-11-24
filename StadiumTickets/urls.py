from django.contrib import admin
from django.urls import path, include

from App1 import views


urlpatterns = [
    path('', views.index),
    path('admin/', admin.site.urls),
    path('App1/', include('App1.urls')),
    path('ProfilesApp/', include('ProfilesApp.urls')),
]
